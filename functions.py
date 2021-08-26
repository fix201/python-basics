# regular function
def function():
  return False

# *args
def test_var_args(f_arg, *argv):
  print("first normal arg:", f_arg)
  for arg in argv:
    print("another arg through *argv:", arg)
test_var_args('yasoob', 'python', 'eggs', 'test')

# **kwargs
def greet_me(**kwargs):
  for key, value in kwargs.items():
    print("{0} = {1}".format(key, value))
greet_me(name="yasoob")

# lambda function
x = lambda a : a + 10 # x is the function name
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))

# map
print(list(map(lambda n: n * 2, [1, 2, 3, 4, 5])))
print(list(map(lambda n: n.split(), ['1', '2', '3s sdsd', 'as4', 'sdfsda'])))

# flat map - from pyspark
# print(list(flatMap(lambda n: n.split(), ['1', '2', '3s sdsd', 'as4', 'sdfsda'])))

# filter
print(list(filter(lambda s: len(s) > 3, ['1', '2', '3s', 'as4', 'sdfsda'])))