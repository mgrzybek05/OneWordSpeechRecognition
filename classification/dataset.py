import os
import numpy as np
import pandas as pd
import random

from glob import glob

from matplotlib import pyplot as plt

from scipy.io import wavfile
from scipy.signal import stft

from sklearn.model_selection import train_test_split

from keras.utils import to_categorical


class DatasetGenerator():
    def __init__(self, label_set,
                 sample_rate=16000):

        self.label_set = label_set
        self.sample_rate = sample_rate

    # Covert string to numerical classes
    def text_to_labels(self, text):
        return self.label_set.index(text)

    # Reverse translation of numerical classes back to characters
    def labels_to_text(self, labels):
        return self.label_set[labels]

    def load_data(self, DIR, random_state):

        # Get all paths inside DIR that ends with wav
        wav_files = glob(os.path.join(DIR, f'*{os.sep}*wav'))
        # print(len(wav_files))

        wav_files = [
            f'{os.sep}'.join(os.path.normpath(x).split(os.sep))
            for x in wav_files
            if len(os.path.normpath(x).split(os.sep)) >= 3
        ]

        # print(len(wav_files))

        # wav_files = [x.split(sep='/')[1] + '/' + x.split(sep='/')[2] for x in wav_files]

        # Loop over files to get samples
        data = []
        for e in wav_files:
            label, name = e.split(os.sep)[-2:]

            if label in self.label_set:  # filters for only needed keywords
                label_id = self.text_to_labels(label)
                fle = os.path.join(DIR, e)

                sample = (label, label_id, name, fle)
                data.append(sample)

        # for testing purposes
        # data = data[:100]

        # Data Frames with samples' labels and paths
        df = pd.DataFrame(
            data, columns=['label', 'label_id', 'user_id', 'wav_file'])

        # TODO: remove test set from here

        self.df = df.sample(frac=1, random_state=random_state)

        return self.df

    def load_test_set(self, DIR, TEST_SET, random_state):
        df = pd.read_csv(TEST_SET)
        df['wav_file'] = df['wav_file'].apply(
            lambda p: os.path.normpath(os.path.join(DIR, p.replace("\\", "/")))
        )
        df['label_id'] = df['label'].apply(
            lambda p: self.text_to_labels(p)
        )

        self.df_test = df.sample(frac=1, random_state=random_state)

        # print(self.df['wav_file'])
        # print(self.df_test['wav_file'])
        mask = ~self.df['wav_file'].isin(self.df_test['wav_file'])
        self.df = self.df[mask].reset_index(drop=True)

        # is_in = self.df['wav_file'].isin(self.df_test['wav_file'])
        # print(sum([1 for i in is_in if i == True]))

        return self.df_test

    # should be 85/15 bc the rest ~2000 already in test set
    def apply_train_val_split(self, val_size, random_state):
        self.df_train, self.df_val = train_test_split(
            self.df, test_size=val_size, random_state=random_state
        )

    def read_wav_file(self, x):
        # Read wavfile using scipy wavfile.read
        _, wav = wavfile.read(x)
        # Normalize
        y = wav.astype(np.float32)
        y -= np.mean(y)
        y /= np.max(np.abs(y))
        # wav = wav.astype(np.float32) / np.iinfo(np.int16).max # this may have been a problem

        return y

    def process_wav_file(self, x, threshold_freq=5500, eps=1e-10):
        # Read wav file to array
        wav = self.read_wav_file(x)
        # Sample rate
        L = self.sample_rate
        # If longer then randomly truncate
        if len(wav) > L:
            i = np.random.randint(0, len(wav) - L)
            wav = wav[i:(i+L)]
        # If shorter then randomly add silence
        elif len(wav) < L:
            rem_len = L - len(wav)
            silence_part = np.random.uniform(-0.1, 0.1, 16000)
            j = np.random.randint(0, rem_len)
            silence_part_left = silence_part[0:j]
            silence_part_right = silence_part[j:rem_len]
            wav = np.concatenate([silence_part_left, wav, silence_part_right])
        # Create spectrogram using discrete FFT (change basis to frequencies)
        freqs, times, spec = stft(
            wav,
            L,
            nperseg=400,
            noverlap=240,
            nfft=512,
            padded=False,
            boundary=None)
        # Cut high frequencies
        if threshold_freq is not None:
            spec = spec[freqs <= threshold_freq, :]
            freqs = freqs[freqs <= threshold_freq]
        # Log spectrogram
        amp = np.log(np.abs(spec)+eps)

        '''
        # Plot spectrogram
        # need to make time axis in seconds
        cep = np.expand_dims(amp, axis=2)
        num_frames = cep.shape[0]
        time_axis = np.linspace(0, len(wav)/self.sample_rate, num_frames)


        plt.rcParams.update({'font.size': 8}) # Set default font size to 12
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'

        plt.figure(figsize=(3.5, 2.5), tight_layout=True)
        plt.imshow(cep, aspect='auto', origin='lower', extent=[time_axis[0], time_axis[-1], freqs[0], freqs[-1]])
        plt.colorbar()
        plt.set_cmap('jet')
        plt.xticks
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        plt.savefig('log_spectrogram.pdf', bbox_inches='tight', dpi=300)
        plt.show()
        '''

        return np.expand_dims(amp, axis=2)

    def generator(self, batch_size, mode):
        while True:
            # Depending on mode select DataFrame with paths
            if mode == 'train':
                df = self.df_train
                ids = random.sample(range(df.shape[0]), df.shape[0])
            elif mode == 'val':
                df = self.df_val
                ids = list(range(df.shape[0]))
            elif mode == 'test':
                df = self.df_test
                ids = list(range(df.shape[0]))
            else:
                raise ValueError('The mode should be either train or val.')

            # Create batches (for training data the batches are randomly permuted)
            for start in range(0, len(ids), batch_size):
                X_batch = []
                y_batch = []
                end = min(start + batch_size, len(ids))
                i_batch = ids[start:end]
                for i in i_batch:
                    X_batch.append(self.process_wav_file(
                        df.wav_file.values[i]))
                    y_batch.append(df.label_id.values[i])
                    # if mode != 'test':
                    #    y_batch.append(df.label_id.values[i])
                X_batch = np.array(X_batch)
                y_batch = to_categorical(
                    y_batch, num_classes=len(self.label_set))
                yield (X_batch, y_batch)

                '''
                if mode != 'test':
                    y_batch = to_categorical(y_batch, num_classes = len(self.label_set))
                    yield (X_batch, y_batch)
                else:
                    yield X_batch
                '''
