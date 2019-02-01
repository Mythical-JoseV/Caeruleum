#####Chaterbot
##Jose Vest
#####1.29.2019

#Exposition
print ("Welcome to Caeruleum, this will tell the tale of... you")
name = input("What is your name?")
print ("Okay now we are set, wait what is your race darn.")
race = input("Are you an Elf, Orc, Human, or Daemonium?")
print ("Okay finally. Welcome to Caeruleunm, this is a tale all about a strong " + race + " who's name was " + name + ". Will he survie to tell his tale? Or die as all the ones before?")

#Intro
print ("You wake up and lift your head to find that you aren't in your home. The sourrondings are familer, yet forein. The colors are warm, almost as if this a the home was in a tree. The bedroom consist of the bed your in, some clothing thrown around, a small desk, and your sword and sheild on the floor. You hear a noise, it startles you.")
Bed_Question = input ("Should you *stay in bed*, or go out to *find the source of the noise*. ")
if Bed_Question.lower()  == "find the source of the noise":
    print ( name + " springs out of bed and grabs his sword. He opens the door and sees a shadow down the hall. You quietly move down the hall and peak your head around the corner, you see a small human near a fire warming up water. You jump out, sword in hand")

elif Bed_Question.lower() == "stay in bed":
    print ("Apparently " + name + " is a crybaby so he stayed in bed. He is being a Ben. Finally he realize that the narrator isn't going to deal with this and gets up. "+ name + " springs out of bed and grabs his sword. He opens the door and sees a shadow down the hall. You quietly move down the hall and peak your head around the corner, you see a small human near a fire warming up water. You jump out, sword in hand") 

print ("just to realize, that this small human was cooking food for what appeared to be two.")
print (""" The human looks up at you and says, "What exactly are you doing". At this point your confused, "I'm not sure" you proclaim as you lower the sword. The humans gets up and smacks you *Smack*. "Listen here dummy, we partied up yesturday. For some reason I thought you could handel liquor, I was wrong. So I brought you to my home as you didn't want to tell me where you live, because you thought I was going to kill your puppy. And here we are, so your call.""""")
Food_Question = input ("Do you want to *eat*, or *contine being dumb*. ")
if Food_Question.lower() == "eat":
    print (""""That's what I thought, here" You thank the human and regret being such an idiot. You ask for her name. "Man how messed up were you, my name is Ada". You thank her properly, "Thank you Ada".""")

elif Food_Question.lower() == "contine being dumb":
    print (""" *Smack*. She smacks you harder and sits you down to eat. You ask for her name. "Ada".""")

print (""" You look up at Ada. She is a small yet mean human. She has long hair and is wearing a red and white dress. She has a bow on her back, along with a quil. "Are you a good shot", you ask. "No, I cary this for fun. Of course I am". "Thanks for the sarcasm, you didn't need to be such a Ben", You respond. "Don't call me a Ben you Ben".""")

Emotion_Question = input("So what will it be " + name + " *be kind* or *be mean*? ")
if Emotion_Question.lower() == "Be kind":
    print(""" "Sorry", you say. She looks at you and says nothing, she puts here attention back to making food. You look at can't help but feel guilt, "Listen, I know that I've been acting dumb, and infact I hardly know you. But we are partied up so it is my intention to work together and do what we have too." She pays no attention to what you said. *Sigh* "Fine", you say. "I'll talk to you later".""")
    print(""" She looks up and says,"Wait... Thank you" . """ + name + """I hope you hold true to that promise". You smile.""")

elif Emotion_Question.lower() == "be mean":
    print("""You really are a Ben. You look at her and tease,"What sort of insult was that, man you really don't know much". She looks up smacks you and leaves crying. You sit there.""")

print ("You go back to the room you were in")

if Emotion_Question.lower() == "be mean":
    print ("""You hear a faint crying from a room left of the one you stayed in. You think to yourself,"Eh Ada deserved it, should've been kinder to me".""")

print ("You look around in the room again, you don't notice anything new. You grab the clothing and armor, you holster you sword. You place your sheild on your back and look at the door")

Emotion_Question2 = Emotion_Question
if Emotion_Question2.lower() == "be kind":
    print(""" You hear a knock. "Come in" you say. Ada opens the door and has a plate of food and a change of clothes, She looks and laughs, "You weren't really going to wear the same clothing were you". "No" you respond trying to play it off. She places the food and clothes desk and leaves the room. "Thank you" you yell.""")

elif Emotion_Question2.lower() == "be mean":
    print (""" You hear the door open, and then hear a loud bang. Ada opens the door is yells at you. This narrator refuses to say such vular laguage so just know it was bad. You look at her.""")
    Emotion_QuestionA = input("Will you *be mean* again, or *change* your ways ")
    if Emotion_QuestionA.lower() == "be mean":
        print ("""You proced to yell equally terrible things back, at this point you begin to seem threating. She looks at you and starts to try and make herself small. She begins to cower and move back. She looks at you and says, "Bye". """)
        print ("This is the end of you jounery, losing your party memebers makes you feel even more angry and you spend your time going out and parting more.")
        input("Any input will end your story")
        exit()

    elif Emotion_QuestionA.lower() == "change":
        print(""" You realize being cruel to the only person trying to help you is dumb, so you change your ways. You look and say, "Sorry". "No you listen... Oh I wasn't expecting that to be honest". She looks up and obviously feels regret. "I'm sorry too, I let this get this out of hand". You laugh and wipe the tears from her face. "How about we try again". Ada smiles and agrees.""")

#Quest beings

print ("You finish the food and change again. You notice that this clothing fits a little small. Not very noticable. The outfit is red and white, like the dress Ada wore. Your silver, yet worn and scratch, armor reflects the walls. You go to the door and yet again hear a loud noise that startles you.")

Door_Question = input("Will you go out with sword in hand *(Guns blazing)*, or *be calm*. ")

if Door_Question.lower() == "be calm":
    print(""" You won't fall for it again. You open the door and see Ada on the floor with what seems to be junk on the floor. "Ah" she exclaims. "Oh hey, lend me a hand". You laugh!""")
    Fall_Question = input("Will you *Help*, or *Harm*. ")
    if Fall_Question.lower() == "help":
        print ("""You go over and move the junk off of her. "Thanks" Ada says, "I swear that closet has it in for me". "I bet", you respond as you contine to laugh. "Shut up" she says.""")

    if Fall_Question.lower() == "harm":
        print(""" You contine to laugh and proced to stack more things on top of her. "Cut it out" She yells at you. You contine to laugh. She slides out under all the junk. "Thanks" Ada says. You are still laughing.""")

elif Door_Question.lower() == "guns blazing":
    print ("""You grab you sword, kick down the door and yell. Ada looks up at you from under a pile of junk that had fallen on her. Ada burst out in laughter. "Come on now, this is the second time. Parionod much.". You look at her. "Hey you mmind helping me?" Ada says.""")
    Fall_QuestionA = input("Will you *Help*, or *Harm*. ")
    if Fall_QuestionA.lower() == "help":
        print ("""You put you sword away and start to move the stuff. "Thanks, sorry for laughing, just calm down okay your safe here". You smile, "Your welcome and I know, just on edge this not being my home and all.".""")

    if Fall_QuestionA.lower() == "harm":
        print (""" You put your sword away and grab some more junk. You being to pile it on top of her. "Hey jerk, stop. Come on I'm sorry for laughing", Ada says. You contine. Finally she slides out from under the junk. "Thanks". You look at her and smile.""")

print ("""Ada beings to pick up the mess left over. You help (NO I'M NOT GIVING YOU THE CHOICE ALRIGHT). You ask her,"So why exactly did you open this closet?". She stays silent for a second and then responds,"To grab a potion.". "What for?" you ask. She sighs, "Right your forgot yesturday, we need this potion to get past Zardon in the Ancient Forest". "WHAT?!?!". You realize there is a lot you missed. "I'll tell you when we finish". You guys put everything back, and she grabs a werid flask with a red liquid inside, the potion. You guys go over to a table and sit.""")

print(""" Ada sits down and begins to give an explaination, "Look you rememeber what city your in right.". "Of course Ripeheart", you say. "Correct, well all I know is I met you at the quest bored inside of the OSG guild." "Okay yes that makes sense I was looking for some work". Ada contines," Right so when I saw you pick this quest I jumped up and insisted we party up". "Wait", you say, "I have two questions". She cuts you off," Right well I'll answer them, which on first?". """)

Quest_Question = input ("Will you ask about *why she insisted on going*, or *what the quest is* ")

if Quest_Question.lower() == "why she insisted on going":
    print (""" You ask,"Why were you so insistent on parting up?". She stays silent, then suddenly," Zardon has my sister, I need to save her, however, I couldn't do it alone. So I posted a quest to have someone help me kill Zardon. You were the only person in 2 weeks that even paid attention to my offer". You are at a lost for words," Sorry." you mange to say. " It's fine, right now the only thing that matters is getting ready and saving my sister". "Agreeed", so now the other question, what are the details of this quest?". """)
    print (""" "Right the quest is, we need to travel far away from Ripeheart, pass through the Cave of Tenbris. After that we will arive in the Town Of Dolorem. As you probably know, the Ancient Forest boreders Dolorem, so from there we will move across the Forest until we find Zardons Sky Arce. There we will sneak past, Zardon and save my sister, then we kill him. Oh did I forget to mention that this is a dangerous route with many mosters, demons, and Zardons Custodis at evey turn. Well my bad". You look at her with your mouth open,"Do you want me to move the moon while your at it". She laughs,"I know its hopeless, but I have to try. Plus we partied up." You begin to regret eveything.""")

elif Quest_Question.lower() == "what the quest is":
    print (""" You ask,"So what exactly is this quest?" She sighs and says, "Right the quest is, we need to travel far away from Ripeheart, pass through the Cave of Tenbris. After that we will arive in the Town Of Dolorem. As you probably know, the Ancient Forest boreders Dolorem, so from there we will move across the Forest until we find Zardons Sky Arce. There we will sneak past, Zardon and save my sister, then we kill him. Oh did I forget to mention that this is a dangerous route with many mosters, demons, and Zardons Custodis at evey turn. Well my bad". You look at her with your mouth open,"Do you want me to move the moon while your at it". She laughs,"I know its hopeless, but I have to try. Plus we partied up." You begin to regret eveything. "Now my second question, Why were you so persistent?".""")
    print ("""  She stays silent, then suddenly," Zardon has my sister, I need to save her, however, I couldn't do it alone. So I posted a quest to have someone help me kill Zardon. You were the only person in 2 weeks that even paid attention to my offer". You are at a lost for words," Sorry." you mange to say. " It's fine, right now the only thing that matters is getting ready and saving my sister". "Agreeed".""")

print(""" "Right, now that we are rested, ate, and have all of our materials shall we?" "Sure" you say.""")

#Combat enabled
print ("            Okay, so hey... I'm the narrator. I you know, cut off your story to explain how the combact system will work. Yes there is a combact system, don't worry story, choices, and talking still happen. So this is a D&D type combact where you randomly roll a D12 (Vitual don't worry), Damage works as such, 0-5 0 points of damage, 6-8 1 point of damage, 9-10 2 points of damage, 11-12 3 points of damage. On top of that you will have events during the battle that can change how the battle happens or ends. This will be the jist of things though. So yeah back to the game... bye")

print(""" "Great" Ada says. You both venture of of the home, you turn and realize that the home was infact in a tree. "So thats why the roomed look like that", you say. Ada laughs, "No duh, how did you not realize it's in a tree. Well we should probably go the merchant or would you rather head out now.".""")

Merchant_Question = input ("Will you *go to the store*, or*head out*.")
if Merchant_Question.lower() == "go to the store":
    print (""" "Let's go to the store you say." Ada looks at you and ask," """ + name + """ do you even have money?". "Oh yeah no... guess lets head out".""")

elif Merchant_Question.lower() == "head out":
    print (""" "Great", Ada says.""")

print("You and Ada head out, hopeful this won't be very hard. Then almost as if the enemy heard me jinx it one of Zardon's custodi jumps out. This will be a tutorial of combat")

Fight1 = input("Oh no an enemy, jumps out and challenges you. Will you *Fight*, *Heal*, or *Run*. (Your health starts at 10 HP in any battle, enemys have 5")

Your_HP = 10
Enemey_HP = 5
             
if Fight1.lower() == "fight":
    import random
    Combat = random.randint(1,12)
    if Combat == 1 or Combat == 2 or Combat == 3 or Combat == 4 or Combat == 5:
               print ("Miss")

    if Combat == 6 or Combat == 7 or Combat == 8:
               print ("Hit Enemey HP at 4")
               Enemey_HP = Enemey_HP - 1

    if Combat == 9 or Combat == 10:
        print ("Hit Enemey HP at 3")
        Enemey_HP = Enemey_HP - 2
        
               
