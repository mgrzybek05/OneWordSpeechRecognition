import time
from tensorflow import keras

class TimeHistory(keras.callbacks.Callback):
	def on_train_begin(self, logs=None):
		self.times = []
		self.start = time.time()
		
	def on_epoch_begin(self, epoch, logs=None):
		self.epoch_start = time.time()
		
	def on_epoch_end(self, epoch, logs=None):
		epoch_time = time.time() - self.epoch_start
		self.times.append(epoch_time)
		
	def on_train_end(self, logs=None):
		self.total_time = time.time() - self.start

class InfoCallback(keras.callbacks.Callback):
	def on_train_begin(self, logs=None):
		self.batch_counts = []
		#self.steps_counts = []
		
	def on_epoch_begin(self, epoch, logs=None):
		self._batches_seen = 0
		#self._steps = self.params.get("steps")
		
		'''
		self._total_samples = self.params.get("samples")
		self._batch_size = self.params.get("batch_size")
		
		if self._total_samples and self._batch_size and not self._steps:
			self._steps = math.ceil(self._total_samples/self.batch_size)
		'''
		
	def on_train_batch_begin(self, batch, logs=None):
		self._batches_seen += 1
		
	def on_epoch_end(self, epoch, logs=None):
		self.batch_counts.append(self._batches_seen)
		#self.steps_counts.append(self._steps)
		#self.sample_counts.append(self._samples_seen)
		'''
		if self._total_samples is not None:
			self.sample_counts.append(self._total_samples)
		elif self._batch_size is not None and self._steps is not None:
			self.sample_counts.append(self._batch_size * self._steps)
		else:
			self.sample_counts.append(None)
		'''
