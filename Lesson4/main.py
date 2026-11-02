from random import sample


def get_gender(name):
    if name[-1] == "a":
        return "Female"
    return "Male"



def add (a,b):
    print(a+b)

def add_return(a,b):
    return a+b

def double_value(a):
    a = a * 2


def double_values(row):
    for k, v in row.items():
        row[k] = v * 2




names = ["Marek", "anna", "eva", "jan"]
for first_name in names:
    print("{} is a {}".format(first_name, get_gender(first_name)))


add(2,2)
result = add_return(2,2)
print (result)
print (result * 2)


a = 10
double_value(a)
print(a)

b = "samplestring"
double_value(b)
print(b)

sample_dict = {"a":10, "b": "sampleString"}
print(sample_dict)
double_values(sample_dict)
print(sample_dict)



sample_var = 10
print(id(sample_var))
sampe_var = sample_var + 10
print(id(sampe_var))


sample_str = "FFF"
print(id(sample_str))
sampe_var = sample_str + "SD"
print(id(sample_str))


sample_dic = {"a":10}
print(sample_dic)
print(id(sample_dic))
sample_dic["a"] += 10
print(sample_dic)
print(id(sample_dic))



