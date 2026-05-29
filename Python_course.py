#how to use sm codes
age=15
height=180.0
name="Justiceden"
#study=input("are you a student?") #input
#print(study, type (study))
print()
qualification=None
print(age, type(age))             #type
print(height, type (height))
print(name, type(name))
print(qualification, type (qualification))
print(age.bit_length())          #bit_length
print("what is your age?:"+str(age)) #string
print(len(name))                  #length

my_experience="""it has been confusing but rewarding for now . I have been able to get a grasp of what is happening for quite a good while and it has been going steady .One of thr best things I could have done is make notes of each fucntion"""
print(my_experience .count("I"))  #count 
number=("+49(176) 123-4567")
print(number.replace(" ","").replace("+","").replace("-","").replace("(","").replace(")",""))
print("my name is",age,"my height is",height,"and my name is",name)
print("my name is " +name+ " I am " +str(height)+ "cm tall "" and my age is " +str(age)) #21,22 are just two inferior methods to write code

#(f"{}") a magician's tool
print(f"I am {name} and I am {age} years old and my current qualification are {qualification}")

#use curly brackets twice if you want it in thr text

fruits="mango,apple,orange,dragon_fruit,tamrind,jack_fruit"
print(fruits .split(",")) #.split 

print("\t","\n","@"*30) # * for multiplying a character for design and so that we can change it whenever desired
print(" ")
#indexes and slicing 
print(name[0])


#cleaning: upper() lower() lstrip() rstrip()

print(len(my_experience ) )
print(len(my_experience .strip()))
print(len(my_experience ) == len(my_experience .strip()))

print(my_experience .count("a"))

#challange for me (clean)
cstring="968-Maria, ( D@t@ Engineer );; 27y"


print(("name:"),cstring[4:9].lower().strip(),("|role:"),cstring[13:30].replace("@",("a")).replace(";","").replace(")","").lower().strip(),"|age:",cstring [-3:-1] .lower().strip())



phone="+91,578387,84857"
phone1="-78,8374893,3848"
phone3="-8888,8374849,93884"

#using find to aid another function 
print(phone.find(","))
print(phone[phone.find(",")+1:])
print(phone1[phone1.find(",")+1:])
print(phone3[phone3.find(",")+1:])



#abs = absolute value of sum/subtraction of two integers

x=10
y=20

print(abs(x-y))

#use ** for  exponents
#use % to find remainder of a number divided by another 
print(20%2)


#floor(),ceil(),round()
import math
x=1.7
print(math.floor(x))
print(math.ceil(x))
print(round(x))

#to yse floor() and ceil() which are not included in std library we have to import math and then use math. before each time we use thr command 

#floor() brings it to the closest lower number 1.7 to 1

#ceil() brings it to thr closest higher number 1.3 to 2

#round() brings the number to the closest number 1.3 to 1 and 1.7 to 2 but if the number is inbetween the two exactly like 1.5 it brings it to the closest even number that is 2 by increasing thr number but for 2.5 it will not be 3 but rather by decreasing it will be 2
x=34.5445
print(round (x))
#we get 35 but what if we need some details? use this
print(round(x,2))
#the second number represents how many decimels we want left out 


#we are mad and we want to remove all decimals but not ny rounding..use trunc()
print(math.trunc(x))
import random 
age=1
age2=20
x="ironman,superman,batman"
print(random.random())
print(random.randint(age,age2))


#isinstance to comfirm which data type does a code belong to 
print(isinstance(age, int))
#obv used in "if" conditions 

#.is_integer to check whether a code is an integer or not
print(age.is_integer())

print(random.randint(1,100)%2==0)


#bool 
print("\n",True)
print(False) 
print(type(True))
print(bool(123))
print(bool("Hi"))
print(bool())
print(bool(0))
print(bool(""))
print(bool (None))
print("just see and understand")


#any ,allows registration if any field is true
x=7
y=8
z=""
print(any([x,y,z]))
#use [] to include many variable as just one

#all ,needs all fields as true to allow registration 

# == checks if two values are equal or not.<= equal or small .!= not equal.< smaller .>bigger

print(2<=3)


#not ,or ,and .in not it changes true to false
print(not 3<5)
#in or atleast one of the two values must be true to get true and in and both values must ne true
print("\n","\n","\n","\n")
print("challange:atleast 8charafter eith no space")
age=10
print(age !="" and age >=18)
password="h1848hdekj"
print(len (password )>=8 and " " not in password)


print("\n\n\n")


print("challange: pass is not empty and contains @ and ends with .com")
password="wihdu7@.com"

print(password !="" and "@" in password and password.endswith(".com"))


print("\n\nchallange:check ,is string ,is not none and is higher than 5chracters ")
username="Justiceden"

print(isinstance(username,str),username  is not None,len(username) >=5)



print("\n\nchallange:check if user admin or moderator and either banned or verified email")
user="user"
moderator_list= ["user","random"]
banned_list=["user","age","height"]
admin_list=["justicjd","rjgodo"]
verified_mail=["user","jamin","disco"]
print(" ")

print((user in moderator_list or user in admin_list) and (user not in banned_list or user in verified_mail))

print("\n\n\n")

#if BE CAREFUL
score= 100
if score >=90: #The : is important 
    print("A") #the four space at  left is necessary 

print("\n\n\n")

#if else and elif
white_list=["Baraa","Zara","Aarya","Adi"]
vip=["Baraa"]
age=0
if "Bara" in white_list:
    if "Baraa" in vip:
        print("full")
    else:
        print("limited")
elif age >=1:
    print("minor")
else:
    print("not allowed")

print("\n\n\n")

#if and else in one line
marks=91
grade="A" if marks >=90 else  "B" if marks >=50 else "fail"
print(grade)

print("\n\n")
#match case 
country= "Indi"
match country:
    case "United States":
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:
        print("Unkown Country")
        
print("\n\n")        
        
username="b@.com"
if username.strip() == "":
    print("it should not be empty")   
elif"@"not in username and "."not in username:
    print("must have ""."",""@""")
elif username.count("@")!=1:
    print("must be one @")
elif not username .endswith((".com",".org",".net")):
    print("must end with . blah")
elif not len(username)<254:
    print("must be shorter than 254")
elif not username[0].isalnum() and username [-1] .isalnum():
    print("start and end with letter/digit")
else:
    print("w email")



# anotherchallange
email="justice@gamil.com"
password=" arpit@gamil.com"
if password.strip() =="":
   print("must not be empty")
elif not len(password)  >=8:
    print("must be 8 character  atleast")
elif email == password:
    print("pass and email should be diffrent")
elif not(password[0].isalnum() and password[-1].isalnum()):
    print("start and end with mumber or letter")
else:
    print("w email")


#for loops
for i in range(10):
    print(f"I love you {i} %")

print("\n\n")

multiplied_by=0
sum=0
for i in range (1,11):
    multiplied_by+=1
    sum=sum+7
    print(f"7x{multiplied_by}={sum}") #imp


for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
    

for i in range(1,7):
    print(f"{"*" * i}")

days_of_week="monday","tuesday","wednesday","thursday","friday","saturday","sunday"



for i in days_of_week:
    if i== "saturday" or i == "sunday":
        continue
    print(i)


#To remmember in for loops  'pass' 'continue 'break', pass does nothing ,continue skips the line and break stops the code (all are used in 'if')


#print all even number and total count of numbers at end
numbers = [4, 7, 10, 13, 16, 19, 22]
for number in numbers:
    if number%2 == 0:
        print(number)
print(f"Total even number {number.bit_length ()}") #i used bit_lenght but better method will be

numbers = [4, 7, 10, 13, 16, 19, 22]
count=0
for number in numbers:
    if number%2 == 0:
        print(number)
        count +=1
print(f"total count of number:{count}")
print("\n\n\n")

#.clear() empties a list
#.remove() removes any value
#.pop() removes by index slot
#max()Find extreme High
#min()Find extreme low
#Sum()Find the Total
#len()Find the Length
#all()Did Everything Pass?
#any()Did Something Pass?
#Count(A)How  often?
#index (A)Where it appears?

#.copy() used to copy a list but shares the inner list 
import copy

a=[
[1,2,3],
[4,5,6],
]

b=a.copy()
b[1].append(2)
print(b)
print("\n\n",a)
print("\n\n\n")
#.extend() used to add a list to other one in the end as if using append

#zip() used to make pairs of two list(ends with a tuple)

print(list(zip(a,b)))


#enumerate to specify the index number and the list itself used in for loops 

a=["a","b ","   c"]
print(enumerate(a,start=1))

for A in a:
    print(A.upper())
#map instead of making a loop for everything we can use the function used in list
print("\n\n")
print(list(map(str.upper,a)))

print("\n\np")
print(list(map(str.strip,a)))

#We use map to use functions or methods like .upper ,.strip etc etc on all of the stuff in a list 
#filter goes through the list to remove what we want to be removed/false stufff


#lambda used to creat a variable which we can change inside a variable
print("\n\n")

even=lambda x:x%2
print(even(6))

even2= lambda x,y:x%y 
print(even2(6,6))



prices = ['$12.50', '$9.99', '$100.00']

print(list(map(lambda p:float(p.replace('$', '')), prices)))


students=[['Maria',85],
['Kumar',90],
['Max',60],
]

print(list(filter(lambda name:name[0] .startswith('M'),students)))
    
name_list=[("Rahul", 45), ("Aman", 82), ("Sneha", 67), ("Priya", 91), ("Karan", 55)]


numbers = [1, 2, 3, 4, 5]
print(list(map(lambda n:n*2,numbers)))

print("\n\n\n")
numbers = [3, 6, 9, 12, 15]
even_odd= list(map(lambda n:f"{n} is even" if n%2==0 else f"{n} is odd",numbers))
print(even_odd,"\n\n")

numbers = [1, 2, 3, 4, 5]
numbers.sort(reverse=True)

print(numbers)
# []list is normal
#()tuple cannot be changed
#{}set can only be changed values inside are not ordered are not indexed and no dublicates

#method add to add in sets but method update is better (can also do a|=b)

#remove and pop can work but discard is recommended

#union combines both unique items from both sets 

#use intersection to find common items in both sets(a & b)

#symmetric_difference to fine unshared value

#issbset (to find if set a exists in set b)
#issuperset to find if  all items are same
#isdisjoint to find if no valued are similar

my_dict = {
    'a': 10,
    'b': 20,
    'c': 20,
    'd': 40
}

print(my_dict)  # Ordered 

# Keys are Unique
# Values allow Duplicates

print(my_dict['b'])  # Access using key (not index)

my_dict['c'] = 80
print(my_dict)  # Mutable

#if we dont know a key is in the dic or not we can use  get() to chrck (we will get none if it doesnt exist)



#we can assign or update values by
#my_dict["x"]= 35


#pop() in dic can remove key and value but can also store it via a variable


#pop() expects a key to remove
#use popitem() to remove with providing key

user = {
    "id": None,
    "name": None,
    "age": None,
    "city": None
}

user= dict.fromkeys(["id","name","age","city"],"yey")
print(user)


user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}

#Create New Dict
#Keep Only Pairs with String Valves
#Convert Values to Uppercase
#Elegant & Short Solution!

str_user={k:v.upper() for k,v in user.items () if isinstance(v,str)}

print(str_user)



print("\n\n")

data = {
    "apple": "red",
    "banana": 10,
    "cherry": "dark red",
    "date": "brown",
    "egg": 5
}
print(data.keys())
print(data.values())
print(data.items())
#Keep only values that are strings
#Keep only strings that contain the letter "r"
#Convert values to UPPERCASE
#Make the key = length of original key
#If keys clash (same length), keep the latest one
print("\n\n\n")

dpot = {len(k): v.upper() for k, v in data.items() if isinstance(v, str) and "r" in v}
print(dpot)





data = {
    "x1": "hello123",
    "y2": "WORLD",
    "z3": 456,
    "a4": "python3",
    "b5": "code"
}


#Keep only values that are strings
#Remove spaces from both sides (strip)
#Keep only values that are lowercase after cleaning
#Convert them to UPPERCASE
dpot={k:v.upper()for k,v in data.items()  if isinstance(v,str) and  v.strip() and v .islower()  }


print(dpot)


print("\n\n")



data = {
    "x1": "",
    "y2": None,
    "z3": None,
    "a4": None,
    "b5": None
}

x= data.fromkeys(["x1","y2","z3","a4","b5"],"yeyy")


print(x,"\n\n")


user = {
    "id": 1,
    "name": "John",
    "age": 30,
    "city": "Berlin"
}

#1 Create New Dict  
#2 Keep Only Pairs with String Valves  
#3 Convert Values to Uppercase  
#4 Elegant & Short Solution!  
  

dpot={k:v.upper() for k,v in user.items() if isinstance(v,str)}
print(dpot,"\n\n")


print("\n\n")

transactions = [
    {"type": "credit", "amount": 500},
    {"type": "debit", "amount": 200},
    {"type": "credit", "amount": 1000},
    {"type": "debit", "amount": 300}
]


print("\n\n")

credit= list(filter(lambda x:x["type"]=="credit",transactions))

debit=list(filter(lambda x:x["type"]=="debit",transactions))


messages = [
    "  Hello World  ",
    "Python is FUN!!!",
    "   ",
    "I love coding 123",
    "TEST message",
    "noNumbersHere"
]


# all messages (remove unnecessary spaces)
#Remove empty messages
#Convert everything to lowercase
#Keep only messages that contain at least one number
#From the remaining messages:
#Create a list of their lengths
#Find the longest message
#Arrange the messages from shortest to longest




    
    


passwords = ["Pass123", "weak", "STRONG123", "123456", "Hello@123", "   ", None]

#Length ≥ 6
#Has at least:
#1 letter (isalpha())
#1 number (isdigit())
#❌ Ignore:
#None
#Empty strings (after strip())
clean_names=[]

for password in passwords:
    if password is None:
        continue 
    password =password.strip()
    if password =="":
        continue 
    if len(password)<6:
        continue 
    letter=False
    digit=False
    for p in password:
       if p .isdigit():
          digit=True
       if p .isalpha():
          letter=True
    if letter and digit:
        clean_names.append(password)

        
    
print(clean_names )



#At least 8 characters
#Has letters
#Has numbers
#Has special characters (like @ # $ %)

password=input()

    password  =password.strip()
    if len(p) >8:
    else:
        print("lenght of pass must be atleast 8")
    has_digit=False
    has_letter=False
    has_special=True
    if p.isdigit():
        has_digit=True
    else:
        print("password must contain  digit")
    if p.isalpha():
        has_letter=True
    else:
        print("password must contain letters")
    if p.isalnum():
        has_special=False
    else:
        print("password must contain special letter")
    if has_letter and has_digit and has_special:
        print("password accpected")
    else:
        print("password must contain special character" )
    break

















