def calculatePN(self, classifier, training_data, len):
    pCounter = 0
    nCounter = 0
    value = 0.0
    for i, j in enumerate(training_data):
        if (training_data[i].get_value(classifier) == classifier.values[0]):
            pCounter = pCounter + 1
        else:
            nCounter = nCounter + 1
    value = (float(pCounter + nCounter)) / float(len)
    return value


def calculateInformationGain(self, targetAttribute, training_data, attributesList, classifier, mainEntropy):
    list = []
    attributeArray = []
    totalInformationGain = 0
    for i in targetAttribute.values:  # sunny
        d = dataset.DataSet()
        for j, k in enumerate(training_data):
            if (training_data[j].get_value(targetAttribute) == i):
                d.all_examples.append(training_data[j])

        tempEntropy = d.entropy(classifier)
        entropy = self.calculatePN(classifier, d.all_examples, j + 1) * tempEntropy
        list.append(entropy)
    totalInformationGain = mainEntropy - sum(list)
    return totalInformationGain, targetAttribute.name


def getMax(self, totalGainArray, attributeArray):
    tempAttribute = ""
    max_num = float("-inf")
    max_index = -1
    for i in range(len(totalGainArray)):
        if (max_num < totalGainArray[i]):
            max_num = totalGainArray[i]
            max_index = i
        elif max_num == totalGainArray[i]:
            if (attributeArray[i] < attributeArray[max_index]):
                max_index = i
    return max_num, attributeArray[max_index]
