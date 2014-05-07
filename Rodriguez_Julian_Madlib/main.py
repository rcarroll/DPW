
#First Prompt
print "Well hello hail and harty traveler, Who may I ask your name?"

NAME= raw_input(" Full Name?:")
print "Ahhh so your name is "+NAME+ " ....I see."

#Second Prompt
CLASS= raw_input(" What Class are you?: _")
print "Ohh so you are a mighty, "+CLASS+", Very interesting..."

#Third Prompt
HOME= raw_input("Where do you hail from?:")
print "I see so you come from the land of "+HOME+", I hear the weather is nice around this time of year."

#Stat Prompt's
print "Tell me more about yourself!"
STR= raw_input("What is your strength value?")
DEX= raw_input("What is your dexterity value?")
LUK= raw_input("How much of a wizard are you?(0-3!)")

#Stats Print, Character info plaved, and Beast array
print "I see, I see... So you have "+STR+" points of STR, "+DEX+" points of DEX and "+LUK+" points LUK."

CharacterInfo= {'Name': NAME, 'Class':CLASS, 'Home':HOME}

BEASTS= ["Dragon", "Ogre", "Litch", "Hell Hound"]

#Start The Quest
print "And so your adventure begins, your name is "+CharacterInfo['Name']+" the mighty "+CharacterInfo['Class']+" and you hail from the land of "+CharacterInfo['Home']+"."

#Loop to determine that luck stat is within a good value and to store it.
for i in range(0, int(LUK)):
    if LUK > 4:
        LUK == 4
    else:
        LUK == LUK

    BEAST= BEASTS[i]

#This prints out what beast you will be facing
print "Your adventure begins wile you make your way to an old dungeon were you face a mighty "+BEAST+"!"

#Variable that will hold your "Skill"
SKILL= raw_input ("What Skill do you wish to use?")


