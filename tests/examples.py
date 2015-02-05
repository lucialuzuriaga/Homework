__author__ = 'user'

#Dictionaries
my_dict = {1: 'Test 1', 2: 'Test 2', '3rd': True}

for each_id, each_value in my_dict.iteritems():
    print str(each_id) + '-' + str(each_value)