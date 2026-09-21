nums=[1,2,3,4,5,6,7,8]

#Indentation is very important in python. It is used to define the scope of loops, functions, classes, etc. In python, indentation is done using spaces or tabs. The standard practice is to use 4 spaces for indentation.
for num in nums:
    print(num)

    for i in nums:
        print(i)
        print("inside loop")
        
    print(num*2)
