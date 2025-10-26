from matplotlib import pyplot


acc = [
    0.5946,
    0.8146,
    0.8813,
    0.9010,
    0.9357,
    0.9414,
    0.9520,
    0.9576,
]

val_acc = [
    0.4237,
    0.7420,
    0.6705,
    0.8754,
    0.8298,
    0.7193,
    0.8725,
    0.8396,
    0.8402,
]

loss = [
    1.1702,
    0.5644,
    0.3694,
    0.3024,
    0.1965,
    0.1780,
    0.1431,
    0.1340
]

val_loss = [
    1.8381,
    0.7161,
    1.0064,
    0.3675,
    0.5551,
    0.8908,
    0.3874,
    0.4867,
    0.4949
]




pyplot.plot(range(1,9), acc, label='Training Accuracy', color='r')
pyplot.plot(range(1,10), val_acc, label='Validation Accuracy', color='g')
pyplot.legend(loc='best')
pyplot.ylabel('Accuracy')
pyplot.xlabel('Epochs')
pyplot.xticks(list(range(0,15))[::5])
pyplot.savefig('accuracy.png')
pyplot.close()


pyplot.plot(range(1,9), loss, label='Training Loss', color='r')
pyplot.plot(range(1,10), val_loss, label='Validation Loss', color='g')
pyplot.legend(loc='best')
pyplot.ylabel('Loss')
pyplot.xlabel('Epochs')
pyplot.xticks(list(range(0,15))[::5])
pyplot.savefig('loss.png')
pyplot.close()