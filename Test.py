import sys
from  DataGenerator import generator
test = generator.generator()
#help(test)
test.dataLooper('int',16,50, True, 0)
test.dataLooper('int',16,50, False, 0)
test.dataLooper('int',16,50, True, 1)
test.dataLooper('string',16,50, True, 0)
test.dataLooper('float',128,100, True,1)
#test.inputParameters()
