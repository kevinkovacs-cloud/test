def bar(x):
    x = x + 90

my_var = 3
bar(my_var)
print(my_var)

#you don't need to call x to the list
def foo(x):
    x[0] = 99
my_list = [1, 2, 3]
foo(my_list)
print(my_list)

#if i assign a = [1, 2, 3] and a = b and then a =42, b is no longer a
#but if i a.append(4) changes affect both variables

#But the bar() function assigns "x" to 
# a new value, so the "my_var" variable isn't touched. In fact, 
# there is no way in Python to have changed "x" or "my_var" 
# directly, because integers are immutable variables.

#---------------------------------------------------

#mutable default arguments are dangerous

def foo(var=None):
    if var is None:
        var = []
    var.append(1)
    return var
foo()
#vs (this down here is the bad one)
#def foo(var=[]):
    #var.append(1)
    #return var
#foo()

print("hello")
