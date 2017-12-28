import copy
import dataset
import attributes
import math


class DTree:
    def ID3(self, classifier, training_data, attributes):

        newAtrributeList = copy.copy(attributes)
        tempEntropy = training_data.entropy(classifier)
        attributeArray = []
        for k, z in enumerate(attributes):
            list = []

            valueDict[z.name]={}
            entropy = training_data.entropy(classifier)
            for i in z.values:  # sunny
                da = dataset.DataSet()
                pCounter = 0
                nCounter = 0
                for x, y in enumerate(training_data):
                    if (training_data[x].get_value(attributes.attributes[k].name) == i):
                        da.all_examples.append(training_data[x])  # sunny Data
                for m, n in enumerate(da.all_examples):
                    if (da.all_examples[m].get_value(classifier) == classifier.values[0]):
                        pCounter = pCounter + 1  # sunny Positive
                    else:
                        nCounter = nCounter + 1  # sunny negative
                value = (float(pCounter + nCounter)) / float(len(training_data.all_examples))
                list.append(value * da.entropy(classifier))
                valueDict[z.name][i] = da.entropy(classifier)

            totalInformationGain = entropy - sum(list)
            totalGainArray.append(totalInformationGain)
            attributeArray.append(z.name)
        gain = 0.0

        if (totalGainArray):
            gain,maxAttributeName=self.getMax(totalGainArray,attributeArray)

        temp = {}
        temp["attr"] = maxAttributeName

        for i in attributes[maxAttributeName].values:  # sunny
            data = dataset.DataSet()
            for j, k in enumerate(training_data):
                if (training_data[j].get_value(maxAttributeName) == i):
                    data.all_examples.append(training_data.all_examples[j])
            newAtrributeList.remove(maxAttributeName)
            if (valueDict[maxAttributeName][i] != 0):
                dict=self.function(classifier, data, newAtrributeList)
                temp[dict["attr"]]=dict
                trackDictionary = {}
                trackDictionary[maxAttributeName] = temp
                self.finalPath.append(trackDictionary)
            else:
                temp["result"]="sda"
        return temp


    def __init__(self, classifier, training_data, attributes):
        self.classifier = classifier
        self.training_data = training_data
        self.attributes = attributes
        self.function(classifier, training_data, attributes)
