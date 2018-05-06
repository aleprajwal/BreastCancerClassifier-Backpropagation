from math import  exp
import tkinter as tk
import os

# Calculate neuron activation for an input
def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]
    return activation


# Transfer neuron activation
def transfer(activation):
    return 1.0 / (1.0 + exp(-activation))

# Find the min and max values for each column
def dataset_minmax(dataset):
    minmax = list()
    stats = [[min(column), max(column)] for column in zip(*dataset)]
    return stats


# Forward propagate input to a network output
def forward_propagate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = transfer(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs

network = [[{'weights': [0.61656466406301, -2.304451471105474, 3.886294204592707, 1.4430617936440708, 0.6714810368227554, 5.267503208662743, 0.6564786812093671, -0.48248924348761635, -3.312541051067754, 0.1773300284135868], 'output': 0.9427048359840458, 'delta': -5.28784954100112e-06}, {'weights': [-4.043169059959117, 0.8724597014133574, 3.7317300755695166, 5.932765675989101, -8.929081206826343, -0.01398498717017012, 3.4097368117586315, 0.1845058413110936, 6.931176128522689, -3.8400657024612124], 'output': 0.9995354705685285, 'delta': 9.614988357950791e-08}, {'weights': [-0.02927998399706532, 3.7275957390816656, 1.9616808207202459, 0.595818975037974, 2.3629420131933965, -3.5690499861938507, -2.357247022547524, 2.3339061201929883, 0.16209608867340006, 1.0647260663404572], 'output': 0.9930211837697143, 'delta': -5.486811994983739e-07}, {'weights': [3.9309920708929256, 7.827445076919603, 1.5091674574029157, 6.320344611250513, -2.504857064706007, -12.95342600087905, 3.935505907312049, -2.235798897229903, -2.6981078143875505, 2.8645900420005352], 'output': 0.8643789080562039, 'delta': -2.7022219480356473e-05}, {'weights': [1.7689835176577664, 7.06326675503925, 3.6330873216157435, 6.377011002814873, -2.6261305636914387, 4.029586603825342, -1.036198266989724, 4.001708962457671, 6.805285789189929, -25.015073129878008], 'output': 0.9826769758275163, 'delta': 4.975656168383574e-06}],
           [{'weights': [-4.347015503635213, 9.18212884052442, -3.5154083956640805, -10.227123845590368, 12.969508812829861, 0.204971876115759], 'output': 0.9966609248046903, 'delta': 1.1112194397617418e-05}, {'weights': [4.327866000636012, -9.166636590293251, 3.5000769717021623, 10.197909924540522, -12.929904750104873, -0.18537600233001297], 'output': 0.003390958679034339, 'delta': -1.1459609482864541e-05}]]


global entry_symptom1
global entry_symptom2
global entry_symptom3
global entry_symptom4
global entry_symptom5
global entry_symptom6
global entry_symptom7
global entry_symptom8
global entry_symptom9
root = tk.Tk()
root.title('Breast Cancer Detection')
label = tk.Label(root, text='Please Enter Attributes Value\n')
label.grid(row=0, column=0)

def attributesTaking():
    a = int(entry_symptom1.get())
    b = int(entry_symptom2.get())
    c = int(entry_symptom3.get())
    d = int(entry_symptom4.get())
    e = int(entry_symptom5.get())
    f = int(entry_symptom6.get())
    g = int(entry_symptom7.get())
    h = int(entry_symptom8.get())
    i = int(entry_symptom9.get())


    row = [a, b, c, d, e, f, g, h, i]
    output = forward_propagate(network, row)
    if output[0] > output[1]:
        a = 'Malignant'
    else:
        a = 'Benign'

    tk.Label(root,text=a).grid(row=11, column=1)

symptom1 = tk.Label(root, text="Clump Thickness")
symptom2 = tk.Label(root, text="Uniformity of Cell size")
symptom3 = tk.Label(root, text="Uniformity of Cell Shape")
symptom4 = tk.Label(root, text="Marginal Adhesion")
symptom5 = tk.Label(root, text="Single Epithelial Cell Size")
symptom6 = tk.Label(root, text="Bare Nuclei")
symptom7 = tk.Label(root, text="Bland Chromatin")
symptom8 = tk.Label(root, text="Normal Nucleoli")
symptom9 = tk.Label(root, text="Mitosis")
entry_symptom1 = tk.Entry(root)
entry_symptom2 = tk.Entry(root)
entry_symptom3 = tk.Entry(root)
entry_symptom4 = tk.Entry(root)
entry_symptom5 = tk.Entry(root)
entry_symptom6 = tk.Entry(root)
entry_symptom7 = tk.Entry(root)
entry_symptom8 = tk.Entry(root)
entry_symptom9 = tk.Entry(root)
symptom1.grid(row=1, column=0)
symptom2.grid(row=2, column=0)
symptom3.grid(row=3, column=0)
symptom4.grid(row=4, column=0)
symptom5.grid(row=5, column=0)
symptom6.grid(row=6, column=0)
symptom7.grid(row=7, column=0)
symptom8.grid(row=8, column=0)
symptom9.grid(row=9, column=0)
entry_symptom1.grid(row=1, column=1)
entry_symptom2.grid(row=2, column=1)
entry_symptom3.grid(row=3, column=1)
entry_symptom4.grid(row=4, column=1)
entry_symptom5.grid(row=5, column=1)
entry_symptom6.grid(row=6, column=1)
entry_symptom7.grid(row=7, column=1)
entry_symptom8.grid(row=8, column=1)
entry_symptom9.grid(row=9, column=1)
ok = tk.Button(root, text='Ok', command=attributesTaking)
ok.grid(columnspan=2)

root.mainloop()



