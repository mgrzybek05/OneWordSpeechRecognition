from keras.models import load_model
from numpy import array, asarray, shape

from dataset import DatasetGenerator

model = load_model('RPM.h5')

LABELS = 'no yes'.split()
dsGen = DatasetGenerator(label_set=LABELS) 

x = array(dsGen.process_wav_file('sound_from_client.wav'))
x = asarray(x).reshape(-1, 177, 98, 1)

# make a prediction
y = model.predict(x)
prediction = y[0]

if prediction[0] > 0.99:
    print('wake up')
else:
    print('still asleep...')
