#nm1 is the list of most prefixes
nm1 = [["Êl", "Star"], ["Aeg", "Sharp Point"], ["Aen", "Holy"], ["Aer", "Holy"], ["Arrad", "Without a Path"], ["Arth", "Exalted"], ["Aur", "Day/Sunlight"], ["Auth", "War/Battle"], ["Belt", "Strong"], ["Beren", "Bold"], ["Brêg", "Violent/Sudden/Fierce"], ["Calad", "Light"], ["Calithil", "Moon Light"], ["Celair", "Brilliant"], ["Claur", "Splendour/Glory"], ["Curu", "Skilled"], ["Dû", "Nightfall"], ["Dûr", "Dark"], ["Dae", "Shadow"], ["Daug", "Warrior/Soldier"], ["Daw", "Night/Gloom"], ["Delu", "Hateful/Deadly/Fell"], ["Doll", "Dark/Dusky"], ["Duvain", "Beautiful Darkness"], ["Edlen", "Exiled"], ["Eglan", "Forsaken"], ["Egnas", "Sharp Point"], ["Erthor", "Uniter"], ["Estel", "Hope/Trust"], ["Fuin", "Night/Darkness"], ["Gail", "Star/Bright Light"], ["Gal", "Light"], ["Galad", "Light/Radiance"], ["Galu", "Good Fortune"], ["Garth", "Fortress"], ["Gellui", "Triumphant"], ["Glaur", "Golden Light"], ["Glaw", "Radiance"], ["Gorn", "Impetuous/Valor"], ["Gwend", "Bond/Friendship"], ["Hûr", "Vigour/Fiery Spirit"], ["Haerel", "Distant Star"], ["Hall", "Exalted"], ["Hinnor", "Fire Eyes"], ["Iest", "Wish"], ["Ind", "Inner Thought/Meaning/Heart"], ["Ladrengil", "Valley of Stars"], ["Laeg", "Keen/Sharp/Acute"], ["Lagor", "Swift/Rapid"], ["Lain", "Free"], ["Lamaen", "Clever Tongue"], ["Lang", "Cutlass/Sword"], ["Leithian", "Release/Freeing"], ["Lend", "Journey"], ["Lif", "Link"], ["Loth", "Flower"], ["Lothuial", "Twilight Blossom"], ["Lum", "Shade"], ["Môr", "Darkness/Night"], ["Maen", "Skilled/Clever"], ["Maeth", "Battle/Fight"], ["Magol", "Sword"], ["Megor", "Sharp/Pointed"], ["Merilin", "Nightingale"], ["Milui", "Friendly/Loving/Kind"], ["Mist", "Wandering"], ["Muin", "Dear/Beloved"], ["Nórui", "Sunny"], ["Orel", "Morning Star"], ["Pelinel", "Fading Star"], ["Pelingil", "Fading Star"], ["Rîl", "Brilliance"], ["Raeg", "Crooked"], ["Raeg", "Wrong"], ["Raen", "Crooked"], ["Rain", "Erratic Wandering"], ["Tû", "Strength"], ["Tûr", "Mastery/Victory"], ["Thîn", "Evening"], ["Thala", "Stalwart/Steady"], ["Thalawest", "Steady Oath"], ["Thand", "Firm/True"], ["Tharbad", "Crossroad"], ["Thaw", "Corrupt/Rotten"], ["Tinnu", "Twilight"], ["Tint", "Spark"], ["Tinu", "Star"], ["Tirnel", "Star Gazer"], ["Uial", "Twilight"], ["Uir", "Eternity"], ["Uireb", "Eternal"]]
#nm2 is the list of only the prefixes of the form "To blank"
nm2 = [["Gal", "To Shine Clear"], ["Míria", "To Shine"], ["Beria", "To Protect"], ["Northa", "To Make Run/Ride"], ["Trasta", "To Harass/Trouble"], ["Ertha", "To Unite"], ["Heria", "To Have an Impulse"], ["Theria", "To Flourish"], ["Ran", "To Wander/Stray"], ["Renia", "To Stray/Wander"], ["Revia", "To Fly/Sail/Wander"], ["Raitha", "To Strive"], ["Rada", "To Make/Find a Way"], ["Presta", "To Affect/Disrupt"], ["Orthor", "To Master/Conquer"], ["Maetha", "To Fight"], ["Nag", "To Bite"], ["Mista", "To Stray/Be Mistaken"], ["Lútha", "To Enchant"], ["Harna", "To Wound"], ["Hartha", "To Hope"], ["Gwesta", "To Swear/Oath"], ["Elia", "To Bless/Help Out"], ["Brenia", "To Endure"]]
#nm3 is a list which gets filled in later (after a gender check and checking what is appropriate based on the ending of the previous name sections/what conjugation is needed from the other name sections)
# a name is created by taking an item from nm1 or nm2 and then nm3,  with some extra formatting
nm3 = [["", "", ""]]
#last char is needed to figure out appropriate nm3
lastChar = ""
lastTwoChar = ""
#type/tp is inputted to the function. 1 = female,  2 = neutral,  0 = male
tp = 1 
f = open('elfnames.txt', 'w')

g = open("elfcelestial.txt", "r")
h = open("elfcombat.txt", "r")
p = open("elfbetrayal.txt", "r")

list1 = g.readlines()
list2 = h.readlines()
list3 = p.readlines()

count = 0

for j in nm1:
    lastChar = j[0][-1]
    lastTwoChar = j[0][-2:]
    for tp in range(1, 3) :
        if(tp == 1):
            if lastChar == "a":
                nm3 = [["eth", "Female", "eth"], ["el", "Female", "el"], ["il", "Female", "il"], ["ien", "Daughter of", "ien"], ["iell", "Daughter of", "iel"], ["sell", "Girl", "ahel"], ["gwend", "Maiden", "awen"], ["neth", "Girl", "aneth"], ["dîs", "Bride", "anis"], ["dess", "Woman", "anes"], ["nîth", "Sister", "anith"], ["thêl", "Sister", "athel"], ["bess", "Wife", "aves"]]
                name1 = j[0][:-1]
            elif lastChar == "e":
                nm3 = [["eth", "Female", "eth"], ["el", "Female", "el"], ["il", "Female", "il"], ["ien", "Daughter of", "ien"], ["iell", "Daughter of", "iel"], ["sell", "Girl", "ehel"], ["gwend", "Maiden", "ewen"], ["neth", "Girl", "eneth"], ["dîs", "Bride", "enis"], ["dess", "Woman", "enes"], ["nîth", "Sister", "enith"], ["thêl", "Sister", "ethel"], ["bess", "Wife", "eves"]]
                name1 = j[0][:-1]
            elif lastChar ==  "i":
                nm3 = [["eth", "Female", "eth"], ["el", "Female", "el"], ["il", "Female", "il"], ["ien", "Daughter of", "ien"], ["iell", "Daughter of", "iel"], ["sell", "Girl", "ihel"], ["gwend", "Maiden", "iwen"], ["neth", "Girl", "ineth"], ["dîs", "Bride", "inis"], ["dess", "Woman", "ines"], ["nîth", "Sister", "inith"], ["thêl", "Sister", "ithel"], ["bess", "Wife", "ives"]]
                name1 = j[0][:-1]
            elif lastChar ==  "o":
                nm3 = [["eth", "Female", "eth"], ["el", "Female", "el"], ["il", "Female", "il"], ["ien", "Daughter of", "ien"], ["iell", "Daughter of", "iel"], ["sell", "Girl", "ohel"], ["gwend", "Maiden", "owen"], ["neth", "Girl", "oneth"], ["dîs", "Bride", "onis"], ["dess", "Woman", "ones"], ["nîth", "Sister", "onith"], ["thêl", "Sister", "othel"], ["bess", "Wife", "oves"]]
                name1 = j[0][:-1]
            elif lastChar ==  "u":
                nm3 = [["eth", "Female", "eth"], ["el", "Female", "el"], ["il", "Female", "il"], ["ien", "Daughter of", "ien"], ["iell", "Daughter of", "iel"], ["sell", "Girl", "uhel"], ["gwend", "Maiden", "uwen"], ["neth", "Girl", "uneth"], ["dîs", "Bride", "unis"], ["dess", "Woman", "unes"], ["nîth", "Sister", "unith"], ["thêl", "Sister", "uthel"], ["bess", "Wife", "uves"]]
                name1 = j[0][:-1]
            elif lastChar ==  "b":
                nm3 = [["eth", "Female", "eth"], ["el", "Female", "el"], ["il", "Female", "il"], ["ien", "Daughter of", "ien"], ["iell", "Daughter of", "iel"], ["bess", "Wife", "es"]]
                name1 = j[0]
            elif lastChar ==  "c":
                nm3 = [["eth", "Female", "geth"], ["el", "Female", "gel"], ["il", "Female", "gil"], ["ien", "Daughter of", "gien"], ["iell", "Daughter of", "giel"], ["gwend", "Maiden", "gwen"]]
                name1 = j[0][:-1]
            elif lastChar ==  "d":
                if(lastTwoChar == "nd"):
                    nm3 = [["eth", "Female", "neth"], ["el", "Female", "nel"], ["il", "Female", "nil"], ["ien", "Daughter of", "nien"], ["iell", "Daughter of", "niel"], ["sell", "Girl", "hel"], ["gwend", "Maiden", "gwen"], ["neth", "Girl", "neth"], ["dîs", "Bride", "dis"], ["dess", "Woman", "des"], ["nîth", "Sister", "nith"], ["thêl", "Sister", "thel"], ["bess", "Wife", "bes"]]
                    name1 = j[0][:-1]
                else:
                    nm3 = [["eth", "Female", "deth"], ["el", "Female", "del"], ["il", "Female", "dil"], ["ien", "Daughter of", "dien"], ["iell", "Daughter of", "diel"], ["sell", "Girl", "ssel"], ["gwend", "Maiden", "dwen"], ["dîs", "Bride", "dis"], ["dess", "Woman", "des"]]
                    name1 = j[0][:-1]
            elif lastChar == "f":
                nm3 = [["eth", "Female", "veth"], ["el", "Female", "vel"], ["il", "Female", "vil"], ["ien", "Daughter of", "vien"], ["iell", "Daughter of", "viel"], ["bess", "Wife", "ves"]]
                name1 = j[0][:-1]
            elif lastChar ==  "g":
                nm3 = [["eth", "Female", "geth"], ["el", "Female", "gel"], ["il", "Female", "gil"], ["ien", "Daughter of", "gien"], ["iell", "Daughter of", "giel"], ["sell", "Girl", "gel"], ["gwend", "Maiden", "gwen"], ["neth", "Girl", "gneth"], ["dîs", "Bride", "gnis"], ["dess", "Woman", "gnes"], ["nîth", "Sister", "gnith"], ["thêl", "Sister", "cthel"]]
                name1 = j[0][:-1]
            elif lastChar ==  "h":
                if(lastTwoChar == "ch"):
                    nm3 = [["eth", "Female", "eth"], ["il", "Female", "il"], ["ien", "Daughter of", "ien"], ["iell", "Daughter of", "iel"], ["sell", "Girl", "el"]]
                    name1 = j[0]
                else:
                    nm3 = [["eth", "Female", "es"], ["el", "Female", "el"], ["il", "Female", "il"], ["ien", "Daughter of", "ien"], ["iell", "Daughter of", "iel"], ["sell", "Girl", "el"], ["thêl", "Sister", "el"]]
                    name1 = j[0]
            elif lastChar ==  "l":
                if(lastTwoChar == "ll"):
                    nm3 = [["eth", "Female", "eth"], ["el", "Female", "el"], ["il", "Female", "il"], ["ien", "Daughter of", "ien"], ["iell", "Daughter of", "iel"], ["sell", "Girl", "hel"], ["gwend", "Maiden", "wen"], ["neth", "Girl", "neth"], ["dîs", "Bride", "dis"], ["dess", "Woman", "des"], ["nîth", "Sister", "nith"], ["thêl", "Sister", "thel"], ["bess", "Wife", "bes"]]
                    name1 = j[0][:-1]
                else:
                    nm3 = [["eth", "Female", "eth"], ["el", "Female", "el"], ["il", "Female", "il"], ["ien", "Daughter of", "ien"], ["iell", "Daughter of", "iel"], ["sell", "Girl", "hel"], ["gwend", "Maiden", "wen"], ["neth", "Girl", "neth"], ["dîs", "Bride", "dis"], ["dess", "Woman", "des"], ["nîth", "Sister", "nith"], ["thêl", "Sister", "thel"], ["bess", "Wife", "bes"]]
                    name1 = j[0]
            elif lastChar ==  "m":
                nm3 = [["eth", "Female", "eth"], ["el", "Female", "el"], ["il", "Female", "il"], ["ien", "Daughter of", "ien"], ["iell", "Daughter of", "iel"], ["dîs", "Bride", "dis"], ["dess", "Woman", "des"], ["bess", "Wife", "bes"]]
                name1 = j[0]
            elif lastChar ==  "n":
                nm3 = [["eth", "Female", "neth"], ["el", "Female", "nel"], ["il", "Female", "nil"], ["ien", "Daughter of", "nien"], ["iell", "Daughter of", "niel"], ["sell", "Girl", "ssel"], ["gwend", "Maiden", "ngwen"], ["neth", "Girl", "neth"], ["dîs", "Bride", "ndis"], ["dess", "Woman", "ndes"], ["nîth", "Sister", "nith"], ["thêl", "Sister", "nthel"], ["bess", "Wife", "mes"]]
                name1 = j[0][:-1]
            elif lastChar ==  "p":
                if(lastTwoChar == "mp"):
                    nm3 = [["eth", "Female", "meth"], ["el", "Female", "mel"], ["il", "Female", "mil"], ["ien", "Daughter of", "mien"], ["iell", "Daughter of", "miel"], ["sell", "Girl", "hel"], ["dîs", "Bride", "dis"], ["dess", "Woman", "des"], ["bess", "Wife", "bes"]]
                    name1 = j[0][:-1]
                else:
                    nm3 = [["eth", "Female", "beth"], ["el", "Female", "bel"], ["il", "Female", "bil"], ["ien", "Daughter of", "bien"], ["iell", "Daughter of", "biel"], ["bess", "Wife", "bes"]]
                    name1 = j[0][:-1]
            elif lastChar ==  "r":
                nm3 = [["eth", "Female", "eth"], ["el", "Female", "el"], ["il", "Female", "il"], ["ien", "Daughter of", "ien"], ["iell", "Daughter of", "iel"], ["sell", "Girl", "hel"], ["gwend", "Maiden", "wen"], ["neth", "Girl", "neth"], ["dîs", "Bride", "dis"], ["dess", "Woman", "des"], ["nîth", "Sister", "nith"], ["thêl", "Sister", "thel"], ["bess", "Wife", "bes"]]
                name1 = j[0]
            elif lastChar ==  "s":
                if(lastTwoChar == "ss"):
                    nm3 = [["eth", "Female", "seth"], ["el", "Female", "sel"], ["il", "Female", "sil"], ["ien", "Daughter of", "sien"], ["iell", "Daughter of", "siel"], ["sell", "Girl", "sel"], ["gwend", "Maiden", "sengwen"], ["neth", "Girl", "seneth"], ["dîs", "Bride", "sendis"], ["dess", "Woman", "sendes"], ["nîth", "Sister", "senith"], ["thêl", "Sister", "senthel"], ["bess", "Wife", "semes"]]
                    name1 = j[0][:-1]
                else:
                    nm3 = [["eth", "Female", "seth"], ["el", "Female", "sel"], ["il", "Female", "sil"], ["ien", "Daughter of", "sien"], ["iell", "Daughter of", "siel"], ["sell", "Girl", "sel"], ["dîs", "Bride", "dis"], ["dess", "Woman", "des"], ["bess", "Wife", "bes"]]
                    name1 = j[0]
            elif lastChar ==  "t":
                if(lastTwoChar == "lt"):
                    nm3 = [["eth", "Female", "eth"], ["il", "Female", "il"], ["ien", "Daughter of", "ien"], ["iell", "Daughter of", "iel"], ["gwend", "Maiden", "wen"], ["neth", "Girl", "neth"], ["dîs", "Bride", "dis"], ["dess", "Woman", "des"], ["nîth", "Sister", "nith"], ["bess", "Wife", "ves"]]
                    name1 = j[0][:-1]
                elif(lastTwoChar == "nt"):
                    nm3 = [["eth", "Female", "nneth"], ["el", "Female", "nnel"], ["il", "Female", "nnil"], ["ien", "Daughter of", "nnien"], ["iell", "Daughter of", "nniel"], ["sell", "Girl", "nthel"], ["gwend", "Maiden", "ngwen"], ["neth", "Girl", "nneth"], ["dîs", "Bride", "ndis"], ["dess", "Woman", "ndes"], ["nîth", "Sister", "nnith"], ["bess", "Wife", "mbes"]]
                    name1 = j[0][:-2]
                else:
                    nm3 = [["eth", "Female", "teth"], ["el", "Female", "tel"], ["il", "Female", "til"], ["ien", "Daughter of", "tien"], ["iell", "Daughter of", "tiel"], ["sell", "Girl", "sel"]]
                    name1 = j[0][:-1]
            elif lastChar ==  "w":
                nm3 = [["eth", "Female", "weth"], ["el", "Female", "wel"], ["il", "Female", "wil"], ["ien", "Daughter of", "wien"], ["iell", "Daughter of", "wiel"], ["sell", "Girl", "hel"], ["gwend", "Maiden", "wen"], ["neth", "Girl", "neth"], ["dîs", "Bride", "nis"], ["dess", "Woman", "nes"], ["nîth", "Sister", "nith"], ["thêl", "Sister", "thel"], ["bess", "Wife", "ves"]]
                name1 = j[0][:-1]
        elif(tp == 2):
            if lastChar == "a":
                nm3 = [["pen", "Person", "ben"], ["", "", ""]]
                name1 = j[0]
            elif lastChar == "e":
                nm3 = [["pen", "Person", "ben"], ["", "", ""]]
                name1 = j[0]
            elif lastChar == "i":
                nm3 = [["pen", "Person", "ben"], ["", "", ""]]
                name1 = j[0]
            elif lastChar == "o":
                nm3 = [["pen", "Person", "ben"], ["", "", ""]]
                name1 = j[0]
            elif lastChar == "u":
                nm3 = [["pen", "Person", "ben"], ["", "", ""]]
                name1 = j[0]
            elif lastChar == "b":
                nm3 = [["pen", "Person", "en"], ["", "", ""]]
                name1 = j[0]
            elif lastChar == "c":
                nm3 = [["", "", ""]]
                name1 = j[0]
            elif lastChar == "d":
                if(lastTwoChar == "nd"):
                    nm3 = [["pen", "Person", "mben"], ["", "", "nd"]]
                    name1 = j[0][:-2]
                else:
                    nm3 = [["", "", ""]]
                    name1 = j[0]
            elif lastChar == "f":
                nm3 = [["pen", "Person", "phen"], ["", "", "f"]]
                name1 = j[0][:-1]
            elif lastChar == "g":
                    nm3 = [["", "", ""]]
                    name1 = j[0]
            elif lastChar == "h":
                if(lastTwoChar == "ch"):
                    nm3 = [["", "", ""]]
                    name1 = j[0]
                else:
                    nm3 = [["pen", "Person", "ben"], ["", "", ""]]
                    name1 = j[0]
            elif lastChar == "l":
                if(lastTwoChar == "ll"):
                    nm3 = [["pen", "Person", "ben"], ["", "", ""]]
                    name1 = j[0][:-1]
                else:
                    nm3 = [["pen", "Person", "ben"], ["", "", ""]]
                    name1 = j[0]
            elif lastChar == "m":
                nm3 = [["pen", "Person", "ben"], ["", "", ""]]
                name1 = j[0]
            elif lastChar == "n":
                nm3 = [["pen", "Person", "mben"], ["", "", ""]]
                name1 = j[0][:-1]
            elif lastChar == "p":
                if(lastTwoChar == "mp"):
                    nm3 = [["pen", "Person", "ben"], ["", "", ""]]
                    name1 = j[0][:-1]
                else:
                    nm3 = [["pen", "Person", "en"], ["", "", ""]]
                    name1 = j[0]
            elif lastChar == "r":
                nm3 = [["pen", "Person", "phen"], ["", "", ""]]
                name1 = j[0]
            elif lastChar == "s":
                if(lastTwoChar == "ss"):
                    nm3 = [["pen", "Person", "pen"], ["", "", ""]]
                    name1 = j[0][:-1]
                else:
                    nm3 = [["pen", "Person", "pen"], ["", "", ""]]
                    name1 = j[0]
            elif lastChar == "t":
                if(lastTwoChar == "lt"):
                    nm3 = [["pen", "Person", "ben"], ["", "", ""]]
                    name1 = j[0][:-1]
                elif(lastTwoChar == "nt"):
                    nm3 = [["pen", "Person", "mben"], ["", "", ""]]
                    name1 = j[0][:-2]
                else:
                    nm3 = [["", "", ""]]
                    name1 = j[0]
            elif lastChar == "w":
                nm3 = [["", "", ""]]
                name1 = j[0]
        for k in nm3:
            names1 = name1 + k[2]
            names2 = "(" + j[0] + " (" + j[1] + ") + " + k[0] + " (" + k[1] + "))"
            if (names1 + " " + names2 + "\n").encode('utf-8').decode('Windows-1252') not in list1 and (names1 + " " + names2 + "\n").encode('utf-8').decode('Windows-1252') not in list2 and (names1 + " " + names2 + "\n").encode('utf-8').decode('Windows-1252') not in list3:
                f.write(names1 + " " + names2 + "\n")
for j in nm2:
    lastChar = j[0][-1:]
    lastTwoChar = j[0][-2:]
    for tp in range(1, 3):
        if tp == 1:
            if lastChar == "a":
                nm3 = [["ril", "Female", "ril"], ["dis", "Female", "adis"], ["iell", "Daughter of", "riel"], ["ien", "Daughter of", "rien"]]
                name2 = j[0][:-1]
            elif lastChar == "b":
                nm3 = [["ril", "Female", "ril"], ["dis", "Female", "edis"], ["iell", "Daughter of", "riel"], ["ien", "Daughter of", "rien"]]
                name2 = j[0]
            elif lastChar == "h":
                nm3 = [["ril", "Female", "ril"], ["dis", "Female", "edis"], ["iell", "Daughter of", "riel"], ["ien", "Daughter of", "rien"]]
                name2 = j[0]
            elif lastChar == "w":
                nm3 = [["ril", "Female", "ril"], ["dis", "Female", "edis"], ["iell", "Daughter of", "riel"], ["ien", "Daughter of", "rien"]]
                name2 = j[0]
            elif lastChar == "d":
                nm3 = [["ril", "Female", "ril"], ["dis", "Female", "is"], ["iell", "Daughter of", "issiel"], ["ien", "Daughter of", "issien"], ["iell", "Daughter of", "riel"], ["ien", "Daughter of", "rien"]]
                name2 = j[0]
            elif lastChar == "f":
                nm3 = [["ril", "Female", "vril"], ["dis", "Female", "vedis"], ["iell", "Daughter of", "vriel"], ["ien", "Daughter of", "vrien"]]
                name2 = j[0][:-1]
            elif lastChar == "g":
                nm3 = [["ril", "Female", "ril"], ["dis", "Female", "nis"], ["iell", "Daughter of", "nissiel"], ["ien", "Daughter of", "nissien"], ["iell", "Daughter of", "riel"], ["ien", "Daughter of", "rien"]]
                name2 = j[0]
            elif lastChar == "l":
                nm3 = [["ril", "Female", "lil"], ["dis", "Female", "dis"], ["iell", "Daughter of", "liel"], ["ien", "Daughter of", "lien"], ["iell", "Daughter of", "dissiel"], ["ien", "Daughter of", "dissien"]]
                name2 = j[0]
            elif lastChar == "n":
                nm3 = [["ril", "Female", "dhril"], ["dis", "Female", "ndis"], ["iell", "Daughter of", "ndissiel"], ["ien", "Daughter of", "ndissien"], ["iell", "Daughter of", "dhriel"], ["ien", "Daughter of", "dhrien"]]
                name2 = j[0][:-1]
            elif lastChar == "r":
                nm3 = [["ril", "Female", "il"], ["dis", "Female", "dis"], ["iell", "Daughter of", "iel"], ["ien", "Daughter of", "ien"]]
                name2 = j[0]
        elif(tp == 2):
            if lastChar == "a":
                nm3 = [["or", "Person", "or"]]
                name2 = j[0][:-1]
            elif lastChar == "b":
                nm3 = [["or", "Person", "or"]]
                name2 = j[0]
            elif lastChar == "h":
                nm3 = [["or", "Person", "or"]]
                name2 = j[0]
            elif lastChar == "w":
                nm3=[["or", "Person", "or"]]
                name2 = j[0]
            elif lastChar == "d":
                nm3 = [["or", "Person", "or"]]
                name2 = j[0]
            elif lastChar == "f":
                nm3 = [["or", "Person", "vor"]]
                name2 = j[0][:-1]
            elif lastChar == "g":
                nm3 = [["or", "Person", "or"]]
                name2 = j[0]
            elif lastChar == "l":
                nm3 = [["or", "Person", "or"]]
                name2 = j[0]
            elif lastChar == "n":
                nm3 = [["or", "Person", "or"]]
                name2 = j[0]
            elif lastChar == "r":
                nm3 = [["or", "Person", "or"]]
                name2 = j[0]
        for k in nm3:
            names1 = name2 + k[2]
            names2 = "(" + j[0] + " (" + j[1] + ") + " + k[0] + " (" + k[1] + "))"
            if (names1 + " " + names2 + "\n").encode('utf-8').decode('Windows-1252') not in list1 and (names1 + " " + names2 + "\n").encode('utf-8').decode('Windows-1252') not in list2 and (names1 + " " + names2 + "\n").encode('utf-8').decode('Windows-1252') not in list3:
                f.write(names1 + " " + names2 + "\n")
