# import {local_file_name}
# from {local_file_name} import {class, function, variable}

# from helper import * (but not recommented)

# from helper import TPL_FORMAT, print_hello, Point

# from helper import TPL_FORMAT
# from helper import print_hello
#from helper import Point
from helper import TPL_FORMAT, print_hello, Point
from helper2 import print_hello as print_formal


print(TPL_FORMAT.format("adam"))
print_hello("eva")
print_formal("adam")

p1 = Point(3,4)
p2 = Point(5,12)


print(p1.length() + p2.length())





