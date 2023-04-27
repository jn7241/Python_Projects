'''
Create a dictionary
that contains 15
countries with their capitals.
Then pick a country randomly from
the dictionary. Ask the user to
enter the capital of the country.
If the user answers incorrectly,
repeatedly ask them for the capital name
until they either enter the correct answer
or type the word "exit". if the user answers
correctly, display "Correct" and end the
program
'''
import random

#STEP 1: 15 random countries with capitals
Countries = {"KOSOVA":"PRISHTINA","ALBANIA":"TIRANA", "FRANCE":"PARIS", "CHINA":"BEIJING", "SPAIN":"MADRID", "PORTUGAL":"LISBON", "EGYPT":"CAIRO",
             "CANADA":"OTTAWA", "SWITZERLAND":"BERN", "AUSTRALIA":"CANBERRA", "BOTSWANA":"GABORONE", "GERMANY":"BERLIN", "USA":"WASHINGTON", "URUGUAY":"MONTEVIDEO",
             "KAZAKHSTAN":"ASTANA"}


#STEP 2: picking a capital randomly
X= int(random.randint(0,14))


QUESTIONS = [] # setting up an an answer box
for i in Countries:
    QUESTIONS.append(i)

ANSWERS = []
for i in Countries.values():
    ANSWERS.append(i)

answer = str(ANSWERS[X])
question = str(QUESTIONS[X])

#STEP 3: ask the user
print("type 'exit' or 'EXIT' to exit program")
playerAnswer = str(input("What is " + str(question) + "'s capital? Type answer in all caps: "))

if playerAnswer == "exit" or playerAnswer == "EXIT":
        print("exiting...")
        exit()
#STEP 4: evaluate the answer
while playerAnswer != answer:
    x = str(input("Wrong. Try again : "))
    if x == "exit" or x == "EXIT":
        print("exiting...")
        exit()
    if x == answer:
        break

#STEP 5: correct condition
if playerAnswer == answer or x == answer:
    print("Correct")
    
