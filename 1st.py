# a=10
# b="20"
# # print(a+b)  will give error because you cannot add an integer and a string in Python. You need to convert the string to an integer first. You can do this by using the int() function:
# print(a+int(b))  # Output: 30   due to sum 
# print(str(a)+b)  #output 1020   due to str concatenation

# # mutability and immutability
# x = 10
# y = x 
# y = 20

# print(x)  #output 10
# print(y)  #output 20    as we can see y is updated but x remains same that is called immuatbilty  as y is another object and x is other object

# # mutabilty
# l1=[1,2,3]
# l2=l1
# l2.append(4)
# print(l1)  # see the l1 was not updated but it got updated  beacause both l1 and l2 refrences to same object -that is called mutabilty

# # boolean logic
# p=11
# print(p>5 and p<2)
# print(p>10 or p==10)

# #write code to take age
# age=input("enter your age");
# print(age)

# user={
#     "is_loggedin":"True",
#     "isAdmin":True,
#     "password":"32er433"
# }
# if(user["is_loggedin"]=="True" and user["isAdmin"]==True):
#        password=input("enter your password to go forward ")
#        if(password==user["password"]):
#               print("welcome to admin panel")
#        else:
#               print("wrong password:-access denied")

# for i in range(1,20):
#        if(i%5==0):
#          print("divisible by 5",i)

# nums=[10,20,30,40]
# # sum=0
# # for i in nums:
# #       sum+=i
# # 
# numbers = [1, 2, 3, 4, 5]
# result = sum(numbers,2)
# print(result) # Output: 15

# text="pyhton developer"
# print(len(text))

# text1 = "hello world hello python hello"
# listt=text1.split(" ")
# print(listt.count("hello"))
# print(text1.count("hello"))

# number = [10, 20, 10, 30, 20, 40, 10]
# newnum=[]
# for i in number:
#       if(i in newnum):
#             continue
#       else:
#             newnum.append(i)
# print(newnum)

# numberss = [10, 50, 20, 80, 40, 70]
# first=0
# second=0
# for i in numberss:
#       if(i>first):
#             second=first
#             first=i
#       elif(i>second):
#             second=i
# print("second largest:-",second)

# texti = "python is easy and python is powerful"
# dict={}

# texti_list=texti.split(" ")
# print(texti_list)
# for i in texti_list:
#       if(dict.get(i) ):
#             dict[i]+=1
#       else:
#             dict[i]=1
# print(dict)


transactions = [
    {"user": "A", "type": "credit", "amount": 1000},
    {"user": "B", "type": "credit", "amount": 2000},
    {"user": "A", "type": "debit", "amount": 300},
    {"user": "A", "type": "credit", "amount": 500},
    {"user": "B", "type": "debit", "amount": 700},
    {"user": "C", "type": "credit", "amount": 1500},
]

summart_dict={}
for summary in transactions:
     
      if(summary["user"] in summart_dict):
            
            if(summary["type"]=="credit"):
                  summart_dict[summary["user"]]=summary["amount"]+summart_dict[summary["user"]]
            else:
                 summart_dict[summary["user"]]=summart_dict[summary["user"]]-summary["amount"] 
      else:
          if(summary["type"]=="credit"):
                            summart_dict[summary["user"]]=0+summary["amount"]
          else:
                           summart_dict[summary["user"]]=0-summary["amount"]  
print(summart_dict) 


# print("Add expense-click 1")
# print("View expenses-click 2")
# print("Delete expense-click 3")
# print("Show total-click 4")
# print("Show category summary-click 5")
# print("Exit-any number")


expenses = [
    {"category": "food", "amount": 500},
    {"category": "travel", "amount": 300},
    {"category": "food", "amount": 200},
    {"category": "shopping", "amount": 1000},
]


def add_expense(expenses, category, amount):
    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)


def show_expenses(expenses):
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['category']} - ₹{expense['amount']}")


def delete_expense(expenses, index):
    if index < 1 or index > len(expenses):
        return False

    expenses.pop(index - 1)
    return True


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def category_summary(expenses):
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        summary[category] = summary.get(category, 0) + amount

    return summary


# Testing

print("Initial expenses:")
show_expenses(expenses)

print("\nAdding expense:")
add_expense(expenses, "food", 150)
show_expenses(expenses)

print("\nTotal:")
print(calculate_total(expenses))

print("\nCategory Summary:")
print(category_summary(expenses))

print("\nDeleting expense:")
result = delete_expense(expenses, 2)

if result:
    print("Expense deleted successfully")
else:
    print("Invalid expense number")

show_expenses(expenses)