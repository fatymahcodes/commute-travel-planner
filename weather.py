distance= float(input("how much distance you want to cover btw ?"))
rain= input("is it raining?")
bike= input("do u have a bike?")
car= input("do you have a car?")
ride_app=input("do you have a ride sharing app?")

if not distance:
    print(False)
elif distance <=1 and rain.lower()=='no':
    print('you can go')  
elif distance> 1 and distance <=6  and bike.lower()=='yes' and  rain.lower()=='no':
    print("you can go")
elif distance>6 and (car=='yes' or ride_app=='yes'):
    print("you can go")  
else:                   
    print("you can't go")