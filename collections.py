### Collections

## List
         #list can collect any type of data       
         #list is an indexed collection
         #list is a mutable collection
         #list can collect repetative data
         #list can be copied

#li=[12,12.76,6+8j,True,"python",["ducat",23,58.76],"python"]
#li1=[34,'abc',54,87.65,False,"python"]

# for x in li:
#     if x  in li1:
#         print(True)
#         break
# else:
#     print(False)    

# print(li+li1)
# print(li-li1)
# print(li*2)

# print(li>li1)

# print(li[-2][0])

# print(len(li))
# print(li[0])
# print(li[-1])

## slicing
# print(li[3:6])
# print(li[-1:1:-1])

# li=[1,2,3,4,5,6,7]       ## array list

# for x in li:
#    print(x**2)

## function

#   print(len(li))
#   print(max(li))
#   print(min(li))
#   print(sum(li))

### methods of list
# li=[12,12.76,6+8j,True,"python",["ducat",23,58.76],"python"]

# li1=li.copy()
# li.append([37,38,39])
# li.insert(3,36)
# li.extend([37,38,39])

# li.remove('python')
# print(li.pop(6))
# li.pop()

# li.clear()

# print(li.count("python"))
# print(li.index("python",5))

# li=[8,12,3,14,5,6,7]
# li.reverse()
# li.sort(reverse=True)
# print(sorted(li,reverse=True))

# print(li)
# print(li1)

#li[3]=False
#print((li))

# print(list(enumerate(li,start=1)))

#li=['Red', 'Green', 'white', 'Black', 'Pink', 'Yellow']
# index=reversed([0,4,5])

# for x in index:
#    li.pop(x)

# print(li)


# li2=[]                                     ##['*','*','*','*','*','*']=2D,3D
# for z in range(3):
#        li1=[]
#        for y in range(4):
#               li=[]
#               for x in range(6):
#                      li.append('*')
#               li1.append(li)       
#        li2.append(li1)
# print(li2)       


#  li=[1,2,3,4,5]
#  li1=[5,4,3,2,1]
#  li2=[]
#  for x in range(len(li)):
#      li2.append(li[x]-li1[x])
#  print(li2)

#  li=['a','b','c','d']
#  s=""
#  for x in li:
#      s+=x
#  print(s)    


## Tuple
           #Tuple can collect any type of data       
           #Tuple is an indexed collection
           #Tuple is a immutable collection
           #Tuple can collect repetative data
           #Tuple can not be copied

# t=(12,12.76,6+8j,True,"python",["ducat",23,58.76],"python")

# t[2]=65
# t[-2].pop()                              ##(pop=de)
# print(t)

#t=(9,)
# print(type(t))
# print(t[3])
# print(t[-3:])

# for x in t:
#     print(x)

# print(len(t))
# print(max(t))
# print(min(t))
# print(sum(t))
# print(tuple(reversed(t)))
# print(sorted())

                                        ##  Method of tuple

# print(t.count(12))
# print(t.index("python"))


                                ## Packin and Unpacking
# x=1,2,3,4,4,5,5,5,
# print(x)

# a,b,c=1,2,3
# print(a,b,c)


## set
           #set can collect any type of data except mutable collection      
           #set is an Unindexed collection
           #set is a mutable collection
           #set can not collect repetative data
           #set can be copied

# s={12,12.76,6+8j,True,"python",("ducat",23,58.76),"python"}
# print(s)

# for x in s:
#     print(x)

# s={1,2,3,4}
# print(max(s))
# print(min(s))
# print(sum(s))
# print(len(s))
# reversed(s)

# print(sorted(s))

                       ## Methods of set
# s.add(125)
# s.add('abc')
# s.update('abc')

# s.remove('python')
# s.discard('python')
#print(s.pop())

# s.clear()
# s1=s.copy()
# print(s)

                      # intersection
                      # union
                      # diffrence
                      # symetric_diffrence 

# s={12,12.76,6+8j,True,"python",("ducat",23,58.76),"python"}
# s1={"python",12}

# print(s.issuperset(s1))
# print(s1.issubset(s))

# print(s.intersection(s1))
#s.intersection_update(s1)

# print(s.union(s1))
# print(s.update(s1))

# print(s.difference(s1))
# print(s.symmetric_difference(s1))

# print(s)


## frozenset
              # frozenset can collect any type of data except mutable collection
              # frozenset is an unindex collection
              # frozenset is immutable collection
              # frozenset can not collect repetative data
# s={12,12.76,6+8j,True,"python",("ducat",23,58.76),"python"}
# fs=frozenset(s)
# print(fs)


## dict                                   #(dictionary)
              #dictionary collect data in the form of keys and values
              #dictionary can collect any type of data in values
              #dictionary can collect onle primitive type of data in keys
              #dictionary is a mutable collection
              #dictionary can not collect repetative keys

# d={'a':'apple',"1":"one",True:1}

# print(d['a'])
# print(d['1'])
# print(d[True])

# d['a']='ant'
# d['b']='box'
# print(d)

# for x in d:
#     print(d[x])

### Methods of dictionary

#d.clear()
# d1=d.copy()
# print(d1)
# print(d.get('a'))

# print(d.keys())
# print(d.values())
# print(d.items())

# d.pop('a')
# d.popitem()

# d.update({'b':'box',"c":"cat"})
# d.setdefault('c','cat')

# d={}
# keys=[1,2,3,4,5,6]
# d=d.fromkeys(keys,'xyz')

# print(d)

# d={2:'b',3:'c',1:'a',4:'d'}
# keys=sorted(d.keys())

# d1={}
# for x in keys:
#     d1[x]=d[x]

# print(d1)

# d={2:'b',3:'c',1:'a',4:'d'}
# value=list(d.values())              #[b,c,a,d]
# value_sorted=sorted(d.values())     #[a,b,c,d]
# keys=list(d.keys())                 #[2,3,1,4]
# d1={}
# for x in value_sorted:
#     index=value.index(x)
#     key=keys[index]
#     d1[key]=x

# print(d1)

### list,set,dict comprehension

# li=[]
# for x in range(1,6):
#    li.append(x**2)


# li=[x**2 for x in range(1,6)]                  ##list

# li={x:x**2 for x in range(1,6)if x>=3}          ##dict

# li={x:x**2 if x>=3 else x**3 for x in range(1,6)}             ## x>3=x**2(squre),x<3=x**3(queb)
# print(li)

# li=[[1,2,3],[4,5,6]]                    ## nested list 
# li1=[]
# for x in li:
#     for y in x:
#         li1.append(y**2)
 
# print(li1)

# li=[[1,2,3],[4,5,6]]  

# li=[y**2 for x in li for y in x]                   ## nested to comprehension
# print(li)

# li=[[1,2,3],[4,5,6]]  
# li=[[y**2 for y in x]for x in li]                    ## comprehension to nested
# print(li)


# li=[[['*' for z in range(6)]for y in range(4)]for x in range(3)]          ## 2d,3d used by comprehension
# print(li)
