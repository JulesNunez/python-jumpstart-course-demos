# import actor
import time
import random
from actors import Wizard, Creature, Weakling, Legend

def main():
    print_header()
    game_loop()



def print_header():
    print('777777777777777777777777777')
    print('7                         7')
    print("7      EPIC ADVENTURE     7")
    print('7                         7')
    print('7      by jules nunez     7')
    print('7                         7')
    print('777777777777777777777777777')
    print()


def game_loop():

    creatures = [
        Weakling('Wormy The Worm',11),
        Creature('Neighbors Doggo', 20),
        Creature('Mister Snail', 35),
        Weakling('Flea', 2),
        Wizard('THOMAS THE TANK DANK WIZARD ENGINE', 75),
        Legend('Massive Legend', 75, 2, True)
    ]

    # print(creatures)

    hero = Wizard('Wizzo The Wizard', 80)



    while True:

        active_creature = random.choice(creatures)
        print('A level {} {} has been summoned!'
              .format(active_creature.level, active_creature.name))

        print()

        cmd = input('YOU MUST CHOOSE TO EITHER [a]ttack, [r]unaway, or [l]ook around ')
        print()
        if cmd == 'a' :
           if hero.attack(active_creature):
               creatures.remove(active_creature)
           else:
               print("{} runs away to a cozy cave to recover and eat philly cheese steak...".format(hero.name))
               time.sleep(5)
               print()
               print("{} has a full tummy and is ready for adventure!".format(hero.name))
               print()
        elif cmd == 'r' :
            print('{} instantly becomes a total wimp thus leading him to run away'.format(hero.name))
            print()
        elif cmd == 'l':
            print(' Our hero {} takes in the surroundings:'.format(hero.name))
            print()
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
            print()
        else:
            print("OK, exiting game... Have a adventurous day.....")
            break


        if not creatures:
            print('Yippie! You have beaten the game.')
            print()
            print('Y O U  W I N!')
            print()
            print()
            print('[Jules_Nunez_2018]')
            break


if __name__ == '__main__':
    main()

