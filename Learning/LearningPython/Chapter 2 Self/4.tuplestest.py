t1 = (2,4,3,6,False,"yash", 25, "DSAI")
print(t1)
print(type(t1))

i=t1.index(25)
print(i)
# index id used for counting on which place is the digit or the str is on which place it is 
# in index the counting start from 0 
# (2,4,3,6,False,"yash", 25, "DSAI")
# (0,1,2,3,  4,    5,     6   ,7) So, this is how we count in programming  language 


c=t1.count(6)
print(c)
# Count command is used for how many time the digit  is repeated 
print(len(t1))

t2 = (2,3,5,3,6,4,58,65,87)
print(max(t2))
# max method is used for taking the maximum number from the tuples  
print(min(t2))
# min method is used for taking the minimum number from the tuples  
print(sum(t2))
# sum mrthod is used for taking the sum of all the digit 

l1 = [1,2,3,5,6,7,9,23,45,7]
l2t = tuple(l1)
print(l2t)
# above command is used for making a list into a tuples 
tuple1 =(2,6,5)
tuple2 =(3,8,4)
new_tuple=tuple1+tuple2
print(new_tuple)
# this command is used for adding both the tuple 
tuple1 = (2,6,5)
repeated=tuple1*3
print(repeated)
# this above code is used for repeating tuple 
