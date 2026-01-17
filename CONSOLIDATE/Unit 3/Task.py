def calculate_area(shape): 

if shape == "circle":  
   radius = float(input("enter the radius of the circle: ")) 
   area = 3.14 * radius ** 2 
   print(" The area of the circle is: ", area) 
    
    
elif shape == "square":  
    side = float(input("enter the side of length the square: ")) 
    area = side ** 2 
    print(" The area of the square is: ", area) 
   
elif shape == "rectangle":  
    side = float(input("enter the side of length the rectangle: ")) 
    area = side ** 2 
    print(" The area of the rectangle is: ", area) 
 
   
else:  
    print("!! Invalid Shape") 
       
  

def main(): 

while True: 
     
    print("Please Enter Option: 1: circle, 2: square, 3: rectangle or to Exit Enter 4: exit") 
     
    choice = int(input("input the choice (1/2/3/4)")) 
     
    if choice == 1: 
        calculate_area("circle") 
         
    elif choice == 2: 
        calculate_area("square") 
         
         
    elif choice == 3: 
        calculate_area("rectangle") 
         
         
    elif choice == 4: 
        print("Exiting the program. ") 
         
     
    else: 
        print("Invalid input, please try again. ") 
         
  

if name == "main": main() 
