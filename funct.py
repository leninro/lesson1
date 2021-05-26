a = 'Learn'
b = 'Python'
delimiter = '&'

c = a + delimiter + b
print(c)
    
def print_with_delim(x,y, delimiter = '&'):
    x = str(x)
    y = str(y)
    z = x + delimiter + y
    return z
print_with_delim('Learn','Python')