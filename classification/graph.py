from matplotlib import pyplot


acc = [
    0.5968,
    0.8189,
    0.8835,
    0.9071,
    0.9286,
    0.9357,
    0.9471,
    0.9316,
    0.9631,
    0.9605,
    0.9678,
    0.9686,
    0.9727,
    0.9742,
    0.9739
]

val_acc = [
    0.2863,
    0.7099,
    0.7122,
    0.8011,
    0.6294,
    0.8873,
    0.4032,
    0.8589,
    0.8916,
    0.7658,
    0.8806,
    0.9189,
    0.8928,
    0.8772,
    0.7931,
    0.7908
]

loss = [
    1.1521,
    0.5550,
    0.3666,
    0.2912,
    0.2271,
    0.1915,
    0.1625,
    0.2023,
    0.1191,
    0.1181,
    0.0988,
    0.1024,
    0.0877,
    0.0821,
    0.0803   
]

val_loss = [
    2.0885,
    0.9243,
    0.9412,
    0.8080,
    1.2008,
    0.3573,
    3.4270,
    0.4603,
    0.3577,
    0.8812,
    0.4170,
    0.2538,
    0.3529,
    0.4106,
    0.7123,
    0.7209
]




pyplot.plot(range(1,16), acc, label='Training Accuracy', color='r')
pyplot.plot(range(1,17), val_acc, label='Validation Accuracy', color='g')
pyplot.legend(loc='best')
pyplot.ylabel('Accuracy')
pyplot.xlabel('Epochs')
pyplot.xticks(list(range(0,15))[::5])
pyplot.savefig('accuracy.png')
pyplot.close()


pyplot.plot(range(1,16), loss, label='Training Loss', color='r')
pyplot.plot(range(1,17), val_loss, label='Validation Loss', color='g')
pyplot.legend(loc='best')
pyplot.ylabel('Loss')
pyplot.xlabel('Epochs')
pyplot.xticks(list(range(0,15))[::5])
pyplot.savefig('loss.png')
pyplot.close()
