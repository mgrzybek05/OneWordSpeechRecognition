from matplotlib import pyplot


acc = [
    0.8657,
    0.9200,
    0.9357,
    0.9598,
    0.9632,
    0.9621,
    0.9695,
    0.9803,
    0.9740,
    0.9855,
    0.9818,
    0.9870
]

val_acc = [
    0.6997,
    0.9339,
    0.8964,
    0.9039,
    0.9474,
    0.9535,
    0.9625,
    0.9790,
    0.9655,
    0.8664,
    0.9655,
    0.9625
]

loss = [
    0.3422,
    0.1903,
    0.1698,
    0.1144,
    0.0924,
    0.0999,
    0.0827,
    0.0574,
    0.0749,
    0.0472,
    0.0536,
    0.0413
]

val_loss = [
    0.6776,
    0.1639,
    0.2589,
    0.2349,
    0.1122,
    0.1332,
    0.1156,
    0.0784,
    0.0942,
    0.3375,
    0.0904,
    0.0860
]




pyplot.plot(range(1,13), acc, label='Training Accuracy', color='r')
pyplot.plot(range(1,13), val_acc, label='Validation Accuracy', color='g')
pyplot.legend(loc='best')
pyplot.ylabel('Accuracy')
pyplot.xlabel('Epochs')
pyplot.xticks(list(range(0,15))[::5])
pyplot.savefig('accuracy.png')
pyplot.close()


pyplot.plot(range(1,13), loss, label='Training Loss', color='r')
pyplot.plot(range(1,13), val_loss, label='Validation Loss', color='g')
pyplot.legend(loc='best')
pyplot.ylabel('Loss')
pyplot.xlabel('Epochs')
pyplot.xticks(list(range(0,15))[::5])
pyplot.savefig('loss.png')
pyplot.close()