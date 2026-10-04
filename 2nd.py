# exception handling

try:
    amount=int(input("enter value"))
    print(type(amount))
except ValueError:
    print("enter a vlaid number")
finally:
    print("hey")



    # custom exeception handling
class InvalidNumberError(Exception):
        pass

def validate_amount(amount):
     if(amount<=0):
           raise InvalidNumberError("Amount must be greater than 0")
     else:
          return True
def get_amount():
     while True:
        try: 
          x=int(input("Enter valid number"))
          
          if(validate_amount(x)):
              return x
          else:
              continue
        except ValueError:
          print("enter valid number like 500 ")
        except InvalidNumberError:
          print("enter number greater than 0")



try:
     amount=get_amount()
     print(amount)
except InvalidNumberError as e:
     print("error",e)
except ValueError:
    print("Please enter a number, for example: 500")

     





