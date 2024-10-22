import random
import datetime

# Setting length of tasks in hours/minutes. Setting the time of day and time when the day ends.
flag = True
time_of_day = datetime.datetime.now().replace(hour=9, minute=00)
time_to_sleep = datetime.datetime.now().replace(hour=21, minute=00)
time_to_eat = datetime.timedelta(minutes=30)
time_to_workout = datetime.timedelta(hours=1, minutes=15)
time_to_study = datetime.timedelta(minutes=45)
time_to_stretch = datetime.timedelta(minutes=20)
time_to_rest = datetime.timedelta(minutes=20)
time_to_socialize = datetime.timedelta(minutes=50)


# Setting a class where player can define a name of the character.
class Character:
    def __init__(self):
        self.name = input('What will be your character name?')

    def __str__(self):
        return f'{self.name}'


# Setting a class where player receives stats of the character.
class Stats:
    def __init__(self):
        self.hp = random.randint(75, 100)
        self.sp = random.randint(75, 100)
        self.intel = random.randint(1, 7)
        self.strength = random.randint(1, 7)
        self.flex = random.randint(1, 7)
        self.max_hp = 100
        self.min_hp = 0
        self.max_sp = 100
        self.min_sp = 0

# Defining the maximum value of hp.
    def func_hp(self):
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        elif self.hp < self.min_hp:
            self.hp = self.min_hp
        else:
            self.hp = self.hp

# Defining the maximum value of Stamina.
    def func_sp(self):
        if self.sp > self.max_sp:
            self.sp = self.max_sp
        elif self.sp < self.min_sp:
            self.sp = self.min_sp
        else:
            self.sp = self.sp

# Giving other stats, with what a player can play around.
    def __str__(self):
        return f'''Your stats are randomized, for extra fun:
        HitPoints: {self.hp}
        StaminaPoints: {self.sp}
        Intelligence: {self.intel}
        Strength: {self.strength}
        Flexibility: {self.flex}
        Have fun and good luck in the game!
'''


# Introduction in the game.
print('''Hello!

Here in this game you will try to gain as many stats to the maximum of 10 points.
Every step that you take, uses a specific amount of time, specific amount of HP and SP.
To restore HP, eat and to restore SP, rest. Simple enough?
Don`t forget, you get tired after 12 hours and will go to sleep.
In next run your characteristics will randomize again.

Good luck in your run!
''')

# A game itself, based on a while loop. Player chooses tasks, they cost HP or Stamina.
# For tasks player receives stats, HP or Stamina.
# Here we also have a check-up if the insert of a player is correct for the code or not.
while time_of_day <= time_to_sleep:

    if flag:
        Player = Character()
        Player_stats = Stats()
        print(Player)
        print(Player_stats)
        flag = False

    print(time_of_day)
    decision = input('''What would you like to do, choose an option by writing 1-6:
     1. Eat - restore HP
     2. Workout - Strength+1
     3. Study - Intelligence+1
     4. Stretch - Flexibility+1
     5. Rest - restore Stamina
     6. Socialize - restore Stamina and HP
     ''')
    print(decision)

    try:
        decision = int(decision)

        if decision < 1 or decision > 6:
            print("Invalid option, please choose a number between 1 and 6.")

    except ValueError:
        print("Invalid input, please enter a number between 1 and 6.")

    if decision == 1:
        print('Ouf, i am so hungry. Lets check the fridge. Wait, what is that Hp above my head and why is it red?')
        Player_stats.hp += 15
        Player_stats.func_hp()
        print(f'Your HP now is: {Player_stats.hp}')
        time_of_day = time_of_day + time_to_eat

    elif decision == 2:
        if Player_stats.hp < 30:
            print('You dont have enough HP, choose something else')

        if Player_stats.sp < 40:
            print('You dont have enough Stamina, choose something else')

        else:
            print('Ooh yeah, look at my muscles. Ooh yes, my strength grows bigger. Strength+2')
            Player_stats.strength += 2
            Player_stats.hp -= 30
            Player_stats.sp -= 40
            Player_stats.func_hp()
            Player_stats.func_sp()
            print(f'''Your Strength, HP and Stamina are now: 
{Player_stats.strength} 
{Player_stats.hp} 
{Player_stats.sp}''')
            time_of_day = time_of_day + time_to_workout

    elif decision == 3:
        if Player_stats.sp < 15:
            print('You dont have enough Stamina, choose something else')

        else:
            print('Yay, study. Someone from geeky film would say, hope it doesnt drain me to bits... Intelligence+1')
            Player_stats.intel += 1
            Player_stats.sp -= 15
            Player_stats.func_sp()
            print(f'''Your Intelligence and Stamina now is: 
{Player_stats.intel}
{Player_stats.sp}''')
            time_of_day = time_of_day + time_to_study

    elif decision == 4:
        if Player_stats.hp < 5:
            print('You dont have enough HP, choose something else')

        if Player_stats.sp < 5:
            print('You dont have enough Stamina, choose something else')

        else:
            print('Does this bone has to crack? Flexibility+1')
            Player_stats.flex += 0.5
            Player_stats.hp -= 5
            Player_stats.sp -= 5
            Player_stats.func_hp()
            Player_stats.func_sp()
            print(f'''Your Flexibility, HP and Stamina now is: 
{Player_stats.flex}
{Player_stats.hp}
{Player_stats.sp}''')
            time_of_day = time_of_day + time_to_stretch

    elif decision == 5:
        print('Sleep, it is. Its not like im tired or somethatsffksnl......ZzZzZ Stamina+')
        Player_stats.sp += 15
        Player_stats.func_sp()
        print(f'''Your Stamina now is: 
{Player_stats.sp}''')
        time_of_day = time_of_day + time_to_rest

    elif decision == 6:
        print('And then he said: What does a fox say???? Can you imagine?? HP/Stamina+')
        Player_stats.hp += 5
        Player_stats.hp += 10
        Player_stats.func_hp()
        Player_stats.func_sp()
        print(f'''Your HP now is: 
{Player_stats.hp}
{Player_stats.sp}  ''')
        time_of_day = time_of_day + time_to_socialize

# End of the game and showcase of what a player achieved.
if time_of_day >= time_to_sleep:

    Player = Character()
    Player_stats = Stats()
    print(Player)
    print(Player_stats)

    print('''
    
    What a nice day, Good night! Lets get better next day!''')
