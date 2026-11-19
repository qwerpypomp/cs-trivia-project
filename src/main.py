import sys
sys.path.append("/modules")

from FilteredInput import *
import xml.etree.ElementTree as ET

def filterAttribute(attributeName,attributeValue,list):
    filteredList = []
    for x in list:
        if(x.get(attributeName) == attributeValue):
            filteredList.append(x)

QuestionTree = ET.parse("/data/questions.xml")
playing = True

while playing:
    score = 0
    correctQuestions = 0

    print("Welcome to idk what the game show name is")
    print("insert information about what this is")
    difficulty = Input("What difficulty would you like to play? (Easy/Normal/Hard/Challenging)",["easy","normal","hard","challenging"])
    liveLimit = 6 if difficulty == "easy" else 4 if difficulty == "normal" else 2 if difficulty=="hard" else 1 if difficulty=="challenging" else "if this hits the code isnt working"
    lives = liveLimit
    # also score addition
    difficultyNumber = 0 if difficulty == "easy" else 1 if difficulty == "normal" else 2 if difficulty=="hard" else 4 if difficulty=="challenging" else "if this hits the code isnt working"
    questions = filterAttribute("difficulty",difficultyNumber,QuestionTree.getroot().findall("question"))
    for question in questions:
        playerAnswer = input(question.get("text"))
        if(playerAnswer == question.get("answer")):
            print("whatever the correct answer message is")
            score += question.get("points") + difficultyNumber
        else:
            print("whatever the incorrect answer message is")
            lives -= 1

        if(lives<1):
            print("GAME OVER")
            print("Final score:",score)
            break
    if(Input("Would you like to continue playing? (y/n)",["y","n"]) == "n"):
        playing = False