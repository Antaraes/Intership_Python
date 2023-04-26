#dictionry comprehison
'''keys = {'a','b','c'}

value = [1]

vowels = {key:list(value) for key in keys}
print(vowels)

value.append(2)

print(vowels) '''

#.get()
''' marks = {"Physic":67,"Maths":87}
print(marks.get("Physic"))
print(marks.get("Salary")) #None
print(marks) '''
#In .get() method, if the key has no found return None

#.items() return a list of dictionary

#setdefault() return the value of a key(if the key is in dict if not it inersts key with a value to dict
person = {'name': 'Phill'}

# key is not in the dictionary
''' salary = person.setdefault('salary')
print('person = ',person)
print('salary = ',salary)'''

# key is not in the dictionary
# default_value is provided

''' age = person.setdefault('age', 22)
print('person = ',person)
print('age = ',age) '''

#popitem() remove the last element

#pop(para) remove the items with key

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('guava', 'banana')

print('The popped element is:', element)
print('The dictionary is:', sales)

#update()
dictionary = {'x': 2}

dictionary.update([('y', 3), ('z', 0)])

print(dictionary)