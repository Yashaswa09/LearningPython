y= [1,2,3,4]
x = [519 ,520,452,654 ]
print(x[2])
# here when we print x(2) so in language we use to count from 0 

# this is used to make list

print(x[1:4])
# [1:4] is going to print  1 and till 4 and not going to print 4
z=x+y
# here when list is added thyey both are combined together so, when we print Z bother list are combined 

print(z)
print(z[3:7])
# [1:4] is going to print  3 and till 7 and not going to print 7



u = [23,56,45,52,65,8,4,9,85]
print(u)
u.append(5*5)
# append is used for updating list or adding an =y digit to it , But this is not going to update any digit present in list
print(u)
print(len(u))
# len used to find lenght  of list  
i=0
while i<len(u):
    print(u[i])
    i+=1
# above code used for making list present vertical in output 


rgb = ["red" , "green", "blue"]
rgba= rgb

print(rgba)

print(id(rgb))
print(id(rgba))
id(rgb)==id(rgba)
# double equals to means to check the relation between two variables 

letter= ["a","b","c","d","e","f","g","h"]
print(letter)
letter[2:5]=["C","D","E"]
# this code is used for updating list 
print(letter)

# l2=[220,54,69]
l1 = [1,2,3,5,6,7,9,23,45,7]
l1.sort()
l1.reverse()
l1.insert(3,335)
l1.pop(5)
l1.remove(335)
# removednum=l1.pop(5)
# print(removednum)
# To add an element to the list, use append
l1.append(222)  
# # Example: add 100 to the end of the list

# To concatenate another list, use +
# l1 = l1 + l2  
# Example: add 100 and 200 to the list

print(l1) 
  
l2=[]
l2.insert(0,5)
l2.insert(1,10)
l2.insert(0,6)
print(l2)
l2.remove(6)
l2.append(9)
l2.append(1)
l2.sort()
print(l2)
l2.pop(3)
l2.reverse()


# print(l2)
l1 = [1, 6, 10, 8, 9, 2, 12, 7, 3, 5]
l1[8:8] = [66, 87, 21, 67]  
l1[1:1] = [30, 75, 44, 44, 75, 48]  
print(l1)
l1.reverse()
print(l1)
l1.sort()
l1 += [2, 5]
l1.remove(2)
print(l1)

l1 = [1, 6, 10, 8, 9, 2, 12, 7, 3, 5]
l1[8:8] = [66, 87, 21, 67]  
l1[1:1] = [30, 75, 44, 44, 75, 48]  
print(l1)
l1.reverse()
print(l1)
l1.sort()
l1 += [2, 5]
l1.remove(2)
print(l1)

 





