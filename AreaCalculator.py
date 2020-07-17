#Codeacademy Project: Area Calculator

#This program calculates the area of a given shape by inputting the lengths of said shape. 
#To run this program, run python AreaCalculator.py in the terminal

#2 This informs the user that the program is runninng.
print "Welcome to the area calculator. This program can calculate the area of a triangle or an area of a circle"

#3
option = raw_input("Enter C for Circle or T for Triangle: ")

#4 Checks if the letter "C" is put in. In my case I used an "or" to ensure that both uppercase and lowercase letters are accepted.
if option == "C" or option == "c":
#5 + 6. Prompts user to enter radius
  radius =float (raw_input("Enter the radius (omit units): "))
  pi = 3.14159
#7 Calculates area of the circle
  area = pi * radius ** 2
#8 Displays the area of the circle
#9 Run using "python AreaCalculator.py"
  print "The area of your circle is " + str(area) 
#10 elif statement for the area of the triangle. Once again, make it user-friendly by accepting either case of the letter t.
elif option == "T" or option == "t":
#11 Base. This program will use the simple base * height / 2 formula. 
  base = float(raw_input("Enter the base length (omit units): "))
#12 Height
  height = float(raw_input("Enter the height (omit units): "))
#13 Calculates area.
  area = base * height / 2
#14 Displays the area
  print "The area of your triangle is " + str(area) + "."
#15 Error handling
else: 
  print "The input is invalid. Please re-start the program"
#16. Informing the user that the program is exiting
print "Thank you for using this program. This was written by donchan91 and feel free to browse his GitHub profile on https://github.com/donchan91"

#17. Run the program to see what happens by typing "python AreaCalculator.py"