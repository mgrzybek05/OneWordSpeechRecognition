from keras.models import load_model
from numpy import array, asarray, shape

from dataset import DatasetGenerator

def classify_sound(model, sound_file):
	LABELS = 'no yes'.split()
	dsGen = DatasetGenerator(label_set=LABELS) 
	x = array(dsGen.process_wav_file(sound_file))
	x = asarray(x).reshape(-1, 177, 98, 1)
	
	#make a prediction
	y = model.predict(x)
	prediction = y[0]

	if prediction[0] > 0.99:
	    return(1)
	else:
	    return(0)
