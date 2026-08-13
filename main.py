import logging
import time
import os

telemarketingpoints=0
food=0
doihavemoney=0
truetelemarketer=0
stage=""
sick=0
hp=100
logging.basicConfig(
    filename="save.log", 
    filemode="a", 
    level=logging.DEBUG
)

def log(telemarketingpoints,food,doihavemoney,truetelemarketer,stage,sick,hp):
       logging.info("readme: telemarketingpoints",telemarketingpoints)
       logging.info("readme: food",food)
       logging.info("readme: do i have money",doihavemoney)
       logging.info("readme: truetelemarketer", truetelemarketer)
       logging.info("readme: stage", stage)
       logging.info("readme: sick", sick)
       logging.info("readme: hp", hp)
   
def check_invalid_funds(telemarketingpoints):
  if telemarketingpoints <= 0:
    doihavemoney=False
    print("You may not have enough telemarketing points")

  else:
    doihavemoney = True
def lojadecaboverde(telemarketingpoints,food,doihavemoney,truetelemarketer,stage):
   stage="loja de cabo verde"
   log(telemarketingpoints,food,doihavemoney,truetelemarketer,stage)
   
   print("welcome to the shop")
   print("You have", telemarketingpoints)
   item=input("You can buy: 1. Food (10 telemarketing points) (Restores Health). Select an item here")
   check_invalid_funds(telemarketingpoints)
   if doihavemoney == True:
      if item == 1:
         food+=1
         telemarketingpoints +=-10
      else:
         print("invalid choice")
         lojadecaboverde(telemarketingpoints,food,doihavemoney,truetelemarketer,stage)
def openworld():
   stage="openworld"
   log(telemarketingpoints,food,doihavemoney,truetelemarketer,stage)
   movement=input("where do you want to go? A) loja de cabo verde. B) Home. C) Telemarketer Company. D) Airport E) Hospatial F) Cave")
   if movement == "A":
    lojadecaboverde(telemarketingpoints,food,doihavemoney,truetelemarketer,stage)
   if movement == "B":
    print("You feel an urge to go back")
    print("But you resist...")
   if movement == "C":
    if truetelemarketer == 1:
         print("you enter your house to go to your computer")
         #this is where the other endings like ldl and you make a game endings happen
    if truetelemarketer == 0:
        print("You have not became a true telemarketer at the big pylon intersection of the cave")
   if movement == "D":
     if truetelemarketer == 1:
              print("The Smort Person ENDING")
              print("You fly back to planet pylon and live a normal life. ")
              raise Exception ("thats the game")
     if truetelemarketer == 0: 
        print("You have not became a true telemarketer at the big pylon intersection of the cave")
   if movement == "E":
      if sick == 1:
         sick = 0
         print("You were healed!")
      else:
         print("you werent sick")
   if movement == "F":
    print("To be continued...")
    time.sleep(2.5)
    print("Tranferring to the new cave... (or define function)")
    cave()
      

      
def cave():
   print("Welcome to the cave")
   print("Your true challange begins here")
   print("where your health matters")
   print("if at any point you need to see your stats type info during the inputs")
  
         




      

print("===========================================================================")
print("      Telemarketer Pylon Procrastination Corner Quest Thingy (TPPCQT) ")
print("===========================================================================")
print(">>>>>>>>>>>>>>>>V.1 or something>>>>>>>>>>>>>>>>>>>")
time.sleep(2.5)
boblebuilder=input("Press enter to continue or save to go to your last checkpoint. \n if you want to reset type reset: ")

if boblebuilder == "reset":
   confirm=input("are you sure; this will delete your save file and replace it. Press any key to continue (other than N that means no)")
   if confirm != "N":
    if os.path.exists("save.log"):
       os.remove("save.log")
       print("yay your save is deleted")
    else:
       raise Warning ("The file could not be deleted. Please try again. \n If the issue still persists, send us an angry report on the issues tab here: https://github.com/nick12357/Televeunder")

if boblebuilder == "":
  stage="opening scene"
  log(telemarketingpoints,food,doihavemoney,truetelemarketer,stage)
  time.sleep(2.5)
  print("...")
  time.sleep(2.5)
  print("Are you going to wait here?")
  time.sleep(2.5)
  print("We're getting late for our flight to Telemarketingland we have to go NOW")
  time.sleep(2.5)
  print("I hear you're a bit scared")
  time.sleep(2.5)
  print("But everything is going to be alright")
  #for the record everything is not alright
  time.sleep(2.5)
  print("Let us hop aboard a plane")
  time.sleep(2.5)
  print("You will be OKAY")
  time.sleep(2.5)
  print("10 years later...")
  time.sleep(5)
  print("Hi, my name is generictelemarketernumber#1229 the Pylon, and this is MY story.")
  print("I had the most telemarketing points at the University of Telemarketing (or Utelemarketing) until THE INCIDENT!")
  print("What incident you may ask, well that’s the larp of 26.")
  print("You see, as the top student at Telemarketing university, I lowkey had mad opps for real. ")
  print("And one of these opps, well he was Devious Daniel. Devious Daniel was notorious for being devious, being named Daniel and worst of all, AN ARCH USER!")
  print("This was because he got the arch user virus from a very young age which is unfortunately incurable.")
  print("Devious Daniel did not like me. He had a poster on his wall the said, ‘Eat, Sleep, Mog generictelemarketernumber#1229, Repeat’")
  print("Before I say this, let’s rewind for like 12 lines of code worth of story or smth idk I’m just in the writing department.")
  print("Anyways let’s go back to 1 week ago, the biggest moment of any telemarketer's career.")
  bobthebuilderpt2=input("type idc to continue or enter idk: ")
  if bobthebuilderpt2 == "idc" or "":
    print("Chapter 2: Examination 1 year earlier It’s the day of the entrance exam, the most stressful day of my life.")
    print("Everything has led up to this. Telemarketing school entrance exams are the most important day of any students life.")
    time.sleep(10)
    print("It’s time. ")
    print("You look at the questions and begin")
    print("Question 1: Who is the best telemarketer? (CASE SENITIVE CAPITALS ONLY): ")
    stage="quiz"
    log(telemarketingpoints,food,doihavemoney,truetelemarketer,stage)
    hi=input("A.Neekan (was number 2 at the time until winter of 25/26) \n B.Bob (the builder) (just bob) \n C.Dirpy (wasn't on the leaderboard at the time) \n D.Tung man 41 (wasn't a meme at the time) \n")
    if hi == "B":
      print("your correct 100 telemarketing points")
      telemarketingpoints += 100
    else:
      print("-100 telemarketing points")
      telemarketingpoints += -100
            ###############################################################################################################
    print("NEXT QUESTION")
    ilovegdcologne=input("Question 2: what is the best gym class item? \n A.Pool Noodle \n B.Hoola Hoop \n C.Pylon  \n D.John Chungus \n")
    if ilovegdcologne == "C":
      print("your correct 100 telemarketing points")
      telemarketingpoints += 100
    else:
      print("-100 telemarketing points")
      telemarketingpoints += -100
            ###############################################################################################################
    inputvar=input("Question 3: What do you throw at Samar? \n A) Yogurt \n B) Samar popo uncle \n C) Clothes \n D) Apples \n")
    if inputvar == "A":
      print("your correct 100 telemarketing points")
      telemarketingpoints += 100
    else:
      print("-100 telemarketing points")
      telemarketingpoints += -100
      ###############################################################################################################
inputvar=input("Question 4: what is the Telemarketing OS? \n A) UwUntu \n B) Arch \n C) Mint \n D) Windows \n")
if inputvar == "C":
      print("your correct 100 telemarketing points")
      telemarketingpoints += 100
else:
      print("-100 telemarketing points")
      telemarketingpoints += -100
if telemarketingpoints > 100:
  print("you can continue")
else:
  print("Tab 14 ENDING")
  print("you have failed and have been sent to the google doc: https://docs.google.com/document/d/1QUeC6_UcQXmG1JxoDBRfEsDzFy47bcwvLeZozBydWkE/ in Tab 14 eternally")
  raise Exception ("thats the game")
print("Welcome to the open world of telemarketingland")
stage = "the main world"
openworld()
