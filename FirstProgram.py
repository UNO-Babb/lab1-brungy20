#FirstProgram.py
#Name: Cooper Brungardt
#Date: 8/28/2024
#Assignment: Lab 1

def main():
  print("First Program")
  #Say hello
  print ("Hello, how are you?")
  #Ask for the user's name
  name = input("What is your name? ")
  #Use the user's name in the program.
  print("Good to meet you",name)
  #Ask the user for their age.
  age = input("What is your age? ")
  #Tell the user what year they were born in.
  age = int(age)
  birth_year = 2024 - age 
  #Assume that they have not had their birthday yet this year.
  #year1 = "birth_year"
  print("You were born in" + birth_year) 


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
