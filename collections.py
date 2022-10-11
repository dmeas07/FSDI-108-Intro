

# LISTS
def list_1():
    print("List 1")

    colors = ["red", "green", "blue"]
    print(colors)
    print(type(colors))

    # add element
    colors.append("white")

    # count / length
    print(len(colors))

    # delete
    # by index

    del colors[0]

    # by value
    colors.remove("white")

    # travel a list
    for x in colors:
        print(x)

def list_2():
    print("List 2")
    nums = [12,34,-1,53,12,88,55,32,-123,9,1,78,1,-4,11,5,6,4,678,4,883,0, -13, 12, 92]

    # print all numbers
    for n in nums:
        print(n)
    
    # print all numbers that are lower than 0
    for x in nums:
        if x<0:
            print(x)
    
    # print the sum of all numbers
    total = 0
    count = 0
    count2 = 0
    for num in nums:
        total = total + num

        if num > 50:
            count += 1
        
        if num >=10 and num <= 50:
            count2 += 1
    
    # count numbers greater than 50

    # count numbers between 10 and 50
    
        
    print(total)
    print("There are " + str(count) + " greater than 50") 
    print(count2)

    



# Dictionary

def dict_1():
    me = {
        "name" : "Daravy",
        "last" : "Meas",
        "age" : 33,
        "hobbies" : [],
        "address" : {
            "street" : "University",
            "num" : "5757",
            "city" : "San Diego",
            "zip" : "92115"
        }
    }

    print(me)
    print(type(me))

    # add pairs
    me["preferred_color"] = "blue"

    # modify
    me["age"] = 99

    # delete key
    del me["hobbies"]

    print(me)

    # read (option 1)
    print(me["name"])

    # read (option 2)

    name = me ["name"]
    print(name)

    # print the address in the following format:
        #street #, city, zip
    
    # method 1
    #print(me["address"]["street"] + " " + me["address"]["num"])

    # method 2
    address = me["address"]
    print (address["street"] + " " + address["num"] + ", " + address["city"] + ", " + address["zip"])

    # method 3 (f string)(preffered method)
    #address = me["address"]
    #print(f"{address["street"]} {address["num"]}, {address["city"]}m, {address["zip']}")




# start
dict_1()