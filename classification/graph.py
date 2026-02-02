import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 8}) # Set default font size to 12
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right'] = True

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

'''
acc = [
0.577668965,
0.797273159,
0.87265867,
0.905751526,
0.919121027,
0.92997551,
0.941690385,
0.950360715,
0.953736186,
0.955589354,
0.959428132,
0.968098462,
0.967899919,
0.968098462,
0.974849403
]

val_acc = [
0.744749844,
0.807906091,
0.835237801,
0.714175403,
0.804045737,
0.807288468,
0.737337887,
0.903489828,
0.885886371,
0.823038936,
0.890982091,
0.892680645,
0.871834457,
0.899166167,
0.90997529,
0.9062
]

loss = [
1.212517858,
0.61614418,
0.392775714,
0.296143442,
0.248206735,
0.216255575,
0.180915236,
0.154131323,
0.141376793,
0.133560494,
0.126096815,
0.098614655,
0.098216094,
0.096220709,
0.077458858
]

val_loss = [
0.796547174,
0.548189402,
0.49810496,
0.912278116,
0.750231445,
0.647037327,
0.920206666,
0.337857515,
0.422766179,
0.560604572,
0.353239447,
0.352451861,
0.410414755,
0.388598293,
0.332719117,
0.5293
]
'''



plt.figure(figsize=(3.5, 2.8), tight_layout=True)
plt.plot(range(1,16), acc, label='Training Accuracy', color='r')
plt.plot(range(1,17), val_acc, label='Validation Accuracy', color='g')
plt.legend(loc='best')
plt.ylabel('Accuracy')
plt.xlabel('Epochs')
plt.xticks(list(range(0,15))[::5])
plt.ylim(bottom=0, top=1)
plt.grid(True)
plt.savefig('accuracy_icc.pdf', bbox_inches='tight')
plt.close()

plt.figure(figsize=(3.5, 2.8), tight_layout=True)
plt.plot(range(1,16), loss, label='Training Loss', color='r')
plt.plot(range(1,17), val_loss, label='Validation Loss', color='g')
plt.legend(loc='best')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.xticks(list(range(0,15))[::5])
plt.ylim(0, 3.5)
plt.grid(True)
plt.savefig('loss_icc.pdf', bbox_inches='tight')
plt.close()
