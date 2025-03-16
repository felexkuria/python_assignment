inputa = int(input("Enter a number for math calculaulation "))
inputb= int(input("Enter Next number "))
mathoperator=input("Math Operator ➕ ")


 


def addition(a ,b):
 if mathoperator == "+":
  sum =a+b;
  print(f"✔️✔️  {a} + {b} = {sum}")
 else:
  print("Operator doesnot exist ❌❌")

 
 return sum;

addition(inputa,inputb);