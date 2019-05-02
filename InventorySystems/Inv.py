def drop(item):
    f = open("items.txt", "r")
    inv = f.readlines()
    f.close()
    done = False
    while done == False:
        for x in inv:
            if inv[x] == item:
                inv.pop(x)
                done = True
            else:
                x = x + 1

def fill():
    items = ['if your reading this, i messed up somehow.\n',  #Consumables
             'Monster Candy\n',  #Consumables
             'Spider Donut\n',
             'Spider Cider\n',
             'Butterscotch Pie\n',
             'Snail Pie\n',
             'Snowman Piece\n',
             'Nice Cream\n',
             'Bisicle\n',
             'Unisicle\n',
             'Cinnamon Bunny\n',
             'Astronaut Food\n',
             'Crab Apple\n',
             'Sea Tea\n',
             'Abandoned Quiche\n',
             'Temmie Flakes\n',
             'Dog Salad\n',
             'Instant Noodles\n',
             'Hot Dog\n',
             'Hot Cat\n',
             'Junk Food\n',
             'Hush Puppy\n',
             'Starfait\n',
             'Glamburger\n',
             'Legendary Hero\n',
             'Steak in the Shape of Mettaton\'s Face\n',
             'Popato Chisps\n',
             'Bad Memory\n',
             'Last Dream\n',
             'Puppydough Icecream\n',
             'Pumpkin Rings\n',
             'Rock Candy\n',
             'Croquet Roll\n',
             'Ghost Fruit\n',
             'Stoic Onion\n',
             'Stick\n',  #Equippables - Items
             'Toy Knife\n',
             'Tough Glove\n',
             'Ballet Shoes\n',
             'Torn Notebook\n',
             'Burnt Pan\n',
             'Empty Gun\n',
             'Worn Dagger\n',
             'Real Knife\n',
             'Bandage\n',  #Equippables - Armour
             'Faded Ribbon\n',
             'Manly Bandanna\n',
             'Old Tutu\n',
             'Cloudy Glasses\n',
             'Temmie Armour\n',
             'Stained Apron\n',
             'Cowboy Hatz\n',
             'Heart Locket\n',
             'The Locket\n',
             'Punch Card\n',  #Misc
             'Annoying Dog\n',
             'Dog Residue\n',
             'Mystery Key\n',
             'Undyne\'s Letter\n',
             'Undyne\'s Letter EX\n']


    for x in range(len(items)):
        print(items[x])

    print('loaded')
    import os, random as r
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    z = 0
    while z != 50:
        give = r.choice(items)
        if give == items[0]:
            print("Nope lol")
        else:
            f = open('items.txt', 'a')
            f.write(give.lower())
            f.close()
            print("Given " + give)
            z = z + 1

def show():
    f = open("items.txt", "r")
    inv = f.readlines()
    f.close()
    lines = 0
    for x in range(len(inv)):
        if x == "\n" or x == "":
            pass
        else:
            print(inv[x])
            lines = lines + 1
    print(lines)

def empty():
    f = open("items.txt", "w").close()
    print("Emptied")