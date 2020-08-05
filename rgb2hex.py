#1 Creating rgb_hex() method
def rgb_hex():
  #2. Storing error message
  invalid_msg = "Error. Input value invalid."
  #3. Prompting RGB input
  red = int(raw_input("Enter Red Value: "))
  #4. Checking if input is valid
  if red < 0 or red > 255:
    #5 Error message when invalid input entered
    print invalid_msg
    return
  #6 Prompting to enter value for green
  green = int(raw_input("Enter Green Value: "))
  if green < 0 or green > 255:
    #7 Error message when invalid input entered
    print invalid_msg
    return
  #8 Prompting user to enter blue
  blue = int(raw_input("Enter Blue Value: ")) 
  if red < 0 or red > 255:
    #9 Error message when invalid input entered
    print invalid_msg
    return
  #10. Building the rest of the method using hexaddecimal numbers
  #11. Creating the variable val
  val = (red << 16) + (green << 8) + blue
  print "%s" % (hex(val)[2:]).upper()

#13 Adding the hex_rgb() method
def hex_rgb():
  #14 Prompts the user to input the hex value 
  hex_val = raw_input("Enter a hexdecimal value: ")
  #15 Error check to see if value is 6 numbers long
  if len(hex_val) != 6:
    #16 Error message and return
    print "Invalid value entered."
    return
  #17 Accepting the hex value as an integer
  else:
    hex_val = int(hex_val, 16)
  #18 Creating two_hex_digits outside of the else block
  two_hex_digits = 2 ** 8
  #19 Calculating blue
  blue = hex_val % two_hex_digits
  #20 Shifting hex_val to the right by 8 bits
  hex_val = hex_val >> 8
  #21 Calculating green
  green = hex_val % two_hex_digits
  #22 Shifting hex_val to the right (again) by 8 bits
  hex_val = hex_val >> 8
  #23 Calculating red
  red = hex_val % two_hex_digits
  #24 Printing out the RGB Values
  print "Red: %s Green: %s Blue: %s" % (red, green, blue)
#25 Creating the convert() method
def convert():
  #26 Adding the while loop with the condition as True
  while True:
    #27 Prompt user option
    option =str(raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:"))
    #28 If 1 is chosen
    if option == '1':
      #29 Calling rgb_hex()
      print "RGB to Hex... "
      rgb_hex()
    #30 If 2 is chosen
    elif option == '2':
      print "Hex to RGB..."
      hex_rgb()
    #31 If user chooses to close program
    elif option == "x" or option == "X":
      break
    #32 Error message
    else:
      print "Error."

#33 Calling convert()
convert()