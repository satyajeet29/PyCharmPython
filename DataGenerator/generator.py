# 1: Addition of requisite package files
import pandas as pd
import random
import string
import sys

class generator:
    # Code to intilize data size
    def __init__(self):
        dataSize = 16
        dataVolume = 50
        dataType = "int"
        dataMultiplierswitch = False
        # Data Sorted 0  for unsorted, 1 for ascending, 2 for reverse sorting
        dataSorted = 0



    # Declaring private methods that can't be accessed from outside the class

    # Code to generate random strings:
    def __stringGenerator(self, dataSize, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(dataSize))

    # Code to generate random float numbers:
    def __floatGenerator(self, dataSize):
        a = random.getrandbits(dataSize)
        b = a + 1
        return random.uniform(a, b)

    # Code to generate random integers:
    def __intGenerator(self, dataSize):
        return random.getrandbits(dataSize)



    def __dataFileWriter(self, containerBox, dataType, dataSize, dataVolume, dataSorted):
        if  dataSorted == 2:
            fileName = str(dataType)+'_Data_Type_'+str(dataSize)+'_bytes_size_'+str(dataVolume)+'_sorted_desc_rows.csv'
            StringDF = pd.DataFrame(containerBox, columns=['Values'])
            StringDF_Sorted = StringDF.sort_values(by=['Values'], ascending=False)
            StringDF_Sorted.to_csv(fileName, sep='\t', encoding='utf-8')
            print(fileName + " file created")
            containerBox = []
        elif dataSorted == 1:
            fileName = str(dataType)+'_Data_Type_'+str(dataSize)+'_bytes_size_'+str(dataVolume)+'_sorted_asc_rows.csv'
            StringDF = pd.DataFrame(containerBox, columns=['Values'])
            StringDF_Sorted = StringDF.sort_values(by=['Values'], ascending=True)
            StringDF_Sorted.to_csv(fileName, sep='\t', encoding='utf-8')
            print(fileName + " file created")
            containerBox = []
        elif dataSorted == 0:
            fileName = str(dataType) + '_Data_Type_' + str(dataSize) + '_bytes_size_' + str(dataVolume)+'_unsorted_rows.csv'
            StringDF = pd.DataFrame(containerBox, columns=['Values'])
            StringDF.to_csv(fileName, sep='\t', encoding='utf-8')
            print(fileName + " file created")
            containerBox = []




    def __dataGenerator(self,dataType, dataSize, dataVolume, dataMultiplierSwitch, dataSorted):
        #dataGeneratorPoint = self
        if dataMultiplierSwitch == True :
            dataVolume  = dataVolume * 1000
        else:
            dataVolume = dataVolume

        # Container to hold generated data
        container = []
        for volume in range(dataVolume):
            if dataType == "int":
                container.append(self.__intGenerator(dataSize))
            elif dataType == "float":
                container.append(self.__floatGenerator(dataSize))
            elif dataType == "string":
                container.append(self.__stringGenerator(dataSize))
        self.__dataFileWriter(container, dataType, dataSize, dataVolume, dataSorted)
        container = []


    # suitable for user input driven
    def inputParameters(self):

        #Possible future improvement, try to enforce input values along with options to escape

        print('Enter data type int, float, string')
        x = sys.stdin.readline()
        dataType = x.strip('\n')
        print('Data Type entered: ' + x.strip('\n'))

        print('Enter data size as either 16, 128, 1024')
        x = input()
        dataSize = int(x)
        print('Data Size entered: '+ str(x))

        print('Enter data volume 50, 100, 500, 1000, 2000, 10000')
        x = input()
        dataVolume = int(x)
        print('Data Size entered: ' + str(x))

        print('Enter data multiplier switch boolean True/False')
        x = input()
        dataMultiplierSwitch = bool(x)
        print('Data Multiplier entered: ' + str(x))

        print('Enter option 0,1,2 to determine 0- unsorted, 1- ascending, 2- descending')
        x = input()
        dataSorted = bool(x)
        print('Data Sort Option entered (0- unsorted, 1- ascending, 2- descending): ' + str(x))

        self.__dataGenerator(dataType, dataSize, dataVolume, dataMultiplierSwitch, dataSorted)


    # useful for looping through
    def dataLooper(self, dataType, dataSize, dataVolume,dataMultiplierSwitch,dataSorted):
        self.__dataGenerator(dataType, dataSize, dataVolume, dataMultiplierSwitch, dataSorted)












