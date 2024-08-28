#MadLib.py
#Name: Cooper Brungardt
#Date: 8/28/2024
#Assignment: Lab 1

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Give a noun for the story: ")
  noun2 = input("Give another noun to be used in the story: ")
  noun3 = input("Give one more noun to be used in the story: ")
  verb1 = input("Give a verb to be used in the story: ")
  verb2 = input("Give another verb to be used in the story: ")
  verb3 = input("Lastly, give one last verb for the story: ")
  #Print the story with the user supplied words.
  print("I like to take my" , noun1 , "with my friend" , noun2 , "to go to the" , noun3 , ". While we are there we will" , verb1 , "and" , verb2 , "and also" , verb3 , "which is all very fun." )


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
