import sqlite3

month_list = ["January","Febuary","March","April","May","June","July","August","September","October","November","December"]

DATABASE = 'arp_vtuber.db'

def get_data_from_database(sql, params=None): 
    """This function is pulling data from database base on sql that put on"""
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        results = cursor.fetchall()
    return results

def create_language_dict():
    """This function is pulling language data from database and create a dictionary"""
    language = {}
    sql = "SELECT * FROM language;"
    results = get_data_from_database(sql)
    for data in results:
        language[data[0]] = data[1]
    return language

def print_all_member_data():
    """This function is printing out member all data"""
    language_dict = create_language_dict()
    sql = "SELECT * FROM basic;"
    results = get_data_from_database(sql)
    print(f"\n{'No.':<3}{'Name':<15}{'Character':<30}{'Operation & Unit':<32}{'Fanname':<25}{'Youtube Subscriber':<20}{'Debut':<20}{'Birthday':<14}{'Height':<8}{'Language':<28}{'Model Artist':<16}Model Rigger")
    for vtuber in results:
        unit = f"{vtuber[3]} - {vtuber[4]}"
        debut_info = vtuber[7].split()
        month_debut = int(debut_info[1])
        debut = f"{debut_info[2]} {month_list[month_debut-1]} {debut_info[0]}"
        birthday_info = vtuber[8].split()
        month_bd = int(birthday_info[0])
        birthday = f"{birthday_info[1]} {month_list[month_bd-1]}"
        height = f"{vtuber[9]} cm."
        if vtuber[12] is not None:
            language = f"{language_dict[vtuber[10]]}, {language_dict[vtuber[11]]} and {language_dict[vtuber[12]]}"
        elif vtuber[11] is not None:
            language = f"{language_dict[vtuber[10]]} and {language_dict[vtuber[11]]}"
        else:
            language = f"{language_dict[vtuber[10]]}"
        print(f"{vtuber[0]:<3}{vtuber[1]:<15}{vtuber[2]:<30}{unit:<32}{vtuber[5]:<25}   {vtuber[6]:<16}{debut:<20}{birthday:14}{height:<8}{language:<29}{vtuber[13]:<16}{vtuber[14]}")

def print_all_member_name():
    """This function is printing out all member name"""
    sql = "SELECT name FROM basic ORDER BY lower(name);"
    results = get_data_from_database(sql)
    print("\nName")
    for name in results:
        print(name[0])

def print_all_member_order_by_subsciber():
    """This function is printing out all member name and subscriber"""
    sql = "SELECT name, youtube_subsciber FROM basic ORDER BY youtube_subsciber DESC;"
    
    results = get_data_from_database(sql)
    # print nicely
    print(f"\n{'No':3}{'Name':15}Youtube Subsciber")
    for i in range(len(results)):
        print(f"{i + 1:<3}{results[i][0]:<15}{results[i][1]}")
                    
def print_all_member_order_by_birthday():
    """This function is printing out all member name and birthday"""
    sql = "SELECT name, birthday FROM basic ORDER BY birthday;"
    results = get_data_from_database(sql)
    print(f"\n{'Name':<15}Birthday")
    for vtuber in results:
        birthday = vtuber[1].split()
        month = int(birthday[0])
        print(f"{vtuber[0]:<15}{birthday[1]} {month_list[month-1]}")
            
def print_all_member_unit():
    """This function is printing out all member name with their operation and unit"""
    sql = "SELECT name, operation, unit FROM basic ORDER BY operation;"
    results = get_data_from_database(sql)
    print(f"\n{'Name':<15}Operation & Unit")
    for vtuber in results:
        print(f"{vtuber[0]:<15} {vtuber[1]} - {vtuber[2]}")

def print_all_member_character():
    """This function is printing out all member name and their character"""
    sql = "SELECT name, character_type FROM basic ORDER BY lower(name);"
    results = get_data_from_database(sql)
        
    print(f"\n{'Name':<15}Character")
    for vtuber in results:
        print(f"{vtuber[0]:<15}{vtuber[1]}")
            
def print_all_member_model_maker():
    """This function is printing out all member name with their model artist and model rigger"""
    sql = "SELECT name, model_artist, model_rigger FROM basic"
    results = get_data_from_database(sql)
    print(f"\n{'Name':<15}{'Model Artist':<16}Model Rigger")
    for vtuber in results:
        print(f"{vtuber[0]:<15}{vtuber[1]:<16}{vtuber[2]}")
            
def print_all_member_debut():
    """This function is printing out all member name with their debut date"""   
    sql = "SELECT name, debut FROM basic ORDER BY debut;"        
    results = get_data_from_database(sql)
    print(f"\n{'Name':<15}Debut")
    for vtuber in results:
        debut = vtuber[1].split()
        month = int(debut[1])
        print(f"{vtuber[0]:<15}{debut[2]} {month_list[month-1]} {debut[0]}")
            
def print_all_member_height():
    """This function is printing out all member name with their height"""
    sql = "SELECT name, height FROM basic ORDER BY height;"
    results = get_data_from_database(sql)
    print(f"\n{'Name':<15}Height")
    for vtuber in results:
        print(f"{vtuber[0]:<15}{vtuber[1]} cm.")

def print_all_member_language():
    """This function is printing out all member name with the language that they can speak"""
    language = create_language_dict()
    sql = "SELECT name, language1, language2, language3 FROM basic ORDER BY name;"
    results = get_data_from_database(sql)
    print(f"\n{'Name':<15}Language")
    for vtuber in results:
        if vtuber[3] is not None:
            print(f"{vtuber[0]:<15}{language[vtuber[1]]}, {language[vtuber[2]]} and {language[vtuber[3]]}")
        elif vtuber[2] is not None:
            print(f"{vtuber[0]:<15}{language[vtuber[1]]} and {language[vtuber[2]]}")
        else:
            print(f"{vtuber[0]:<15}{language[vtuber[1]]}")

def search_about_in_name():
    """This function is printing out member name that have letter or word that user ask for"""
    beginOrIn = input("""A letter or word …
1. At the beginning of the name 
2. In anywhere of the name
Enter a number: """)
    while beginOrIn not in ["1", "2"]:
        beginOrIn = input("""Please enter a number 1 or 2:
Enter a number: """)
    letter_name = input("What word or letter? : ")    
    if beginOrIn == "1":
        sql = f"SELECT name FROM basic WHERE name LIKE '{letter_name}%' ORDER BY name;"
    elif beginOrIn == "2":
        sql = f"SELECT name FROM basic WHERE name LIKE '%{letter_name}%' ORDER BY name;"
    
    results = get_data_from_database(sql)
    if len(results) == 0:
        print(f'No one has "{letter_name}" in their name.')
    else:
        print(f'Name of Vtuber who has "{letter_name}" in name!')
        for vtuber in results:
            print(f"{vtuber[0]}")

def search_about_subscriber():
    """This function is printing out member name with their subscriber who have subscriber more or less than the number that user put in"""
    higherOrLower = input("""Subscriber ...
1. lower than
2. higher than
Enter a number: """)
    while higherOrLower not in ["1", "2"]:
        higherOrLower = input("""Please enter a number 1 or 2 
Enter a number: """)
    subscriber = input("How Many?:")
    while not subscriber.isdigit():
        subscriber = input("""Please enter a number!
Enter a number: """)
    if higherOrLower == "1":
        sql = "SELECT name, youtube_subsciber FROM basic WHERE youtube_subsciber < ? ORDER BY youtube_subsciber DESC;"
    elif higherOrLower == "2":
        sql = "SELECT name, youtube_subsciber FROM basic WHERE youtube_subsciber > ? ORDER BY youtube_subsciber DESC;"
        
    results = get_data_from_database(sql,(subscriber,))

    # print nicely
    print(f"\n{'No':<3}{'Name':<15}Youtube Subsciber")
    for i in range(len(results)):
        print(f"{i + 1:<3}{results[i][0]:<15}{results[i][1]}")
        
def search_about_birthday():
    """This function is printing out member name with their birthday who born in the month that user ask"""
    birthday_month = input("""Birthday in which month?
1. January
2. Febuary
3. March
4. April
5. May
6. June
7. July
8. August
9. September
10. October
11. November
12. December
Enter a number: """).zfill(2)
    while birthday_month not in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
        birthday_month = input("""Please enter a number from 1 to 12
Enter a number: """).zfill(2)
    sql = f"SELECT name, birthday FROM basic WHERE birthday LIKE '{birthday_month}%'"
    results = get_data_from_database(sql)
    print(f"\n{'Name':<15}Birthday")
    for vtuber in results:
        birthday = vtuber[1].split()
        month = int(birthday[0])
        print(f"{vtuber[0]:<15}{birthday[1]} {month_list[month-1]}")
            
def search_about_debut():
    """This function is printing out member name with their debut date who debut in the year that user ask"""
    which_year = input("""Vtuber debut in which year?
Enter a year as 4 digits ex. 2024
Enter a year: """)
    this_year = 2024
    while len(which_year) != 4 or not which_year.isdigit():
        which_year = input("""Please enter 4 DIGITS NUMBER!
Enter a year: """)
    while int(which_year) > this_year:
        which_year = input(f"""It is not {which_year} yet!
Enter a year: """)

    sql = f"SELECT name, debut FROM basic WHERE debut LIKE '{which_year}%' ORDER BY debut;"
    results = get_data_from_database(sql)
    if len(results) == 0:
        print("No one debut in this year.")
    else:
        print(f"\n{'Name':<15}Debut")
        for vtuber in results:
            debut = vtuber[1].split()
            month = int(debut[1])
            print(f"{vtuber[0]:<15}{debut[2]} {month_list[month-1]} {debut[0]}")
    
def search_about_unit():
    """This function is printing out member name with their operation and unit that user ask"""
    which_operation = ""
    which_unit = ""
    operationOrUnit = input("""Search by?
1. Operation
2. Unit
Enter a number: """)
    while operationOrUnit not in ["1","2"]:
        operationOrUnit = input("""Please enter a number 1 or 2
1. Operation
2. Unit
Enter a number: """)
    if operationOrUnit == "1":
        which_operation = input("""Vtuber in which operation?
1. 1st Operation
2. 2nd Operation
3. 3rd Operation
4. 4th Operation
5. Celestial Opertion
6. Secret Operation
Enter a number: """)
        while which_operation not in ["1","2","3","4","5","6"]:
            which_operation = input("""Please enter a number from 1 - 6
1. 1st Operation
2. 2nd Operation
3. 3rd Operation
4. 4th Operation
5. Celestial Opertion
6. Secret Operation
Enter a number: """)
        if which_operation == "6":
            which_operation = "Secret"
        elif which_operation == "5":
            which_operation = "Celestial"
            which_unit = input("""Which unit?
1. Orion
2. Gemini
3. Scorpio
4. All
Enter a number: """)
            while which_unit not in ["1","2","3","4"]:
                which_unit = input("""Please enter a number from 1 - 4
1. Orion
2. Gemini
3. Scorpio
4. All
Enter a number: """)
            if which_unit == "1":
                which_unit = "Orion"
            elif which_unit == "2":
                which_unit = "Gemini"
            elif which_unit == "3":
                which_unit = "Scorpio"
            elif which_unit == "4":
                which_unit = ""
    elif operationOrUnit == "2":
        which_unit = input("""Vtuber in which unit?
1. Apocalypse
2. Eclipse
3. Illusion
4. Ominous
5. Orion
6. Gemini
7. Scorpio
8. Unknown
Enter a number: """)
        while which_unit not in ["1","2","3","4","5","6","7","8"]:
            which_unit = input("""Please enter a number form 1 - 8
1. Apocalypse
2. Eclipse
3. Illusion
4. Ominous
5. Orion
6. Gemini
7. Scorpio
8. Unknown
Enter a number: """)
        if which_unit == "1":
            which_unit = "Apocalypse"
        elif which_unit == "2":
            which_unit = "Eclipse"
        elif which_unit == "3":
            which_unit = "Illusion"
        elif which_unit == "4":
            which_unit = "Ominous"
        elif which_unit == "5":
            which_unit = "Orion"
        elif which_unit == "6":
            which_unit = "Gemini"
        elif which_unit == "7":
            which_unit = "Scorpio"
        elif which_unit == "8":
            which_unit = "Unknown"
    sql = f"SELECT name, operation, unit FROM basic WHERE operation LIKE '{which_operation}%' AND unit LIKE '%{which_unit}%';"
    results = get_data_from_database(sql)
    print(f"\n{'Name':<15}Operation & Unit")
    for vtuber in results:
        print(f"{vtuber[0]:<15}{vtuber[1]} - {vtuber[2]}")

def search_about_height():
    """This function is printing out member name with their height who is higher or shorter than the number that user put in"""
    shorterOrTaller = input("""Vtuber who ...
1. Shorter than
2. Taller than
Enter a number: """)
    while shorterOrTaller not in ["1","2"]:
        shorterOrTaller = input("""Please enter a number 1 or 2
1. Shorter than
2. Taller than
Enter a number: """)
    height = input("How tall? : ")
    while not height.isdigit():
        height = input("""Please enter a number!
Enter a number: """)
    if shorterOrTaller == "1":
        sql = "SELECT name, height FROM basic WHERE height < ? ORDER BY height, name;"
        key = "shorter"
    elif shorterOrTaller == "2":
        sql = "SELECT name, height FROM basic WHERE height > ? ORDER BY height DESC, name;"
        key = "taller"
    results = get_data_from_database(sql,(height,))
    if len(results) == 0:
        print(f"No one {key} than {height}")
    print(f"\n{'Name':<15}Height")
    for vtuber in results:
        print(f"{vtuber[0]:<15}{vtuber[1]} cm.")

def search_about_language():
    """This function is printing out member name with the language that they can speak who can speak language that user ask"""
    language_dict = create_language_dict()
    language_want = input("""Vtuber who can speak
1. Thai
2. English
3. Chinese
4. Japanese
Enter a number: """)
    while language_want not in ["1","2","3","4"]:
        language_want = input("""Please enter a number from 1 - 4
1. Thai
2. English
3. Chinese
4. Japanese
Enter a number: """)
    language_want = int(language_want)
    sql = f"SELECT name, language1, language2, language3 FROM basic WHERE language1 = {language_want} OR language2 = {language_want} OR language3 = {language_want};"
    results = get_data_from_database(sql)
    print(f"\n{'Name':<15}Language")
    for vtuber in results:
        if vtuber[3] is not None:
            print(f"{vtuber[0]:<15}{language_dict[vtuber[1]]}, {language_dict[vtuber[2]]} and {language_dict[vtuber[3]]}")
        elif vtuber[2] is not None:
            print(f"{vtuber[0]:<15}{language_dict[vtuber[1]]} and {language_dict[vtuber[2]]}")
        else:
            print(f"{vtuber[0]:<15}{language_dict[vtuber[1]]}")

def search_about_model():
    """This function is printing out member name with their model artist and rigger that user ask"""
    artist = ""
    rigger = ""
    artistOrRigger = input("""Search about?
1. Model Artist
2. Model Rigger
Enter a number: """)
    while artistOrRigger not in ["1", "2"]:
        artistOrRigger = input("""Please enter a number 1 or 2
1. Model Artist
2. Model Rigger
Enter a number: """)
    if artistOrRigger == "1":
        artist = input("""Vtuber whose model is drawn by ...
Artist name: """)
    elif artistOrRigger == "2":
        rigger = input("""Vtuber whoes model is rigged by ...
Rigger name: """)
    sql = f"SELECT name, model_artist, model_rigger FROM basic WHERE model_artist LIKE '%{artist}%' AND model_rigger LIKE '%{rigger}%';"
    results = get_data_from_database(sql)
    print(f"\n{'Name':<15}{'Model Artist':<16}Model Rigger")
    for vtuber in results:
        print(f"{vtuber[0]:<15}{vtuber[1]:<16}{vtuber[2]}")
      
def menu():
    """This function is the main menu of program for user to do somethings"""
    while True:
        user_choice1 = input("""
This is a database about Vtuber from the Algorhythm project.
What do you want to do?
Please enter only a number!

1. Exit
2. What is Vtuber?
3. What is the Algorhythm project?
4. Print about member information.
5. Search about member information.

Enter a number: """)
        while user_choice1 not in ["1","2","3","4","5"]:
            user_choice1 = input("""Please enter a number from 1 - 5
1. Exit
2. What is Vtuber?
3. What is the Algorhythm project?
4. Print about member information.
5. Search about member information.

Enter a number: """)
            
        if user_choice1 == "1":
            break
        elif user_choice1 == "2":
            print("""
A VTuber is an online entertainer who uses a virtual avatar generated using computer graphics. 
Real-time motion capture software or technology are often but not always used to capture movement.""")
        elif user_choice1 == "3":
            print("""
The Algorhythm Project, or Algorithm + Rhythm, is a journey of operating systems with the rhythm of music. 
We are a project that brings together VTubers (Virtual YouTubers) with diverse talents and personalities in one place. 
Our project focuses on entertaining everyone through live streaming and music. 
We believe that you will definitely find a VTuber you like because we truly have all kinds!
""")
        elif user_choice1 == "4":
            user_choice = menu_print()
            if user_choice == "back":
                continue
            elif user_choice == "1":
                break
        elif user_choice1 == "5":
            user_choice = menu_search()
            if user_choice == "back":
                continue
            elif user_choice == "1":
                break

def menu_print():
    """This function is a sub menu for the main when user ask to print something"""
    user_choice = input("""
This is a database about Vtuber from the Algorhythm project.
What do you want to know?
Please enter only a number!

1. Exit
2. Go back to first page
3. Member in Algorhythm project
4. Member unit
5. Member youtube subscriber from highest
6. Member debut date
7. Member birthday
8. Member model
9. Member Character
10. Member height from shortest to highest
11. Member language
12. Member all data

Enter a number: """)
    while True:
        if user_choice == "1":
            return "1"
        elif user_choice == "2":
            return "back"
        if user_choice == "3":
            print_all_member_name()
        elif user_choice == "4":
            print_all_member_unit()
        elif user_choice == "5":
            print_all_member_order_by_subsciber()
        elif user_choice == "6":
            print_all_member_debut()
        elif user_choice == "7":
            print_all_member_order_by_birthday()
        elif user_choice == "8":
            print_all_member_model_maker()
        elif user_choice == "9":
            print_all_member_character()
        elif user_choice == "10":
            print_all_member_height()
        elif user_choice == "11":
            print_all_member_language()
        elif user_choice == "12":
            print_all_member_data()
        else:
            print("\nPlease enter a number from 1 - 12")
            user_choice = input("Enter a number: ")
            continue
            
            
        user_choice = input("""
What do you want to know?
Please enter only a number!

1. Exit
2. Go back to first page
3. Member in Algorhythm project
4. Member unit
5. Member youtube subscriber from highest
6. Member debut date
7. Member birthday
8. Member model
9. Member Character
10. Member height from shortest to highest
11. Member language
Enter a number: """)

def menu_search():
    """This function is a sub menu for the main when user want to search something"""
    user_choice = input("""
What do you want to search about?
Please enter only a number!

1. Exit
2. Go back to first page
3. Member in Algorhythm project name
4. Member unit name
5. Member youtube subscriber
6. Member debut year
7. Member birthday month
8. Member model artist or rigger
9. Member height
10. Member language

Enter a number: """)
    while True:
        if user_choice == "1":
            return "1"
        elif user_choice == "2":
            return "back"
        if user_choice == "3":
            search_about_in_name()
        elif user_choice == "4":
            search_about_unit()
        elif user_choice == "5":
            search_about_subscriber()
        elif user_choice == "6":
            search_about_debut()
        elif user_choice == "7":
            search_about_birthday()
        elif user_choice == "8":
            search_about_model()
        elif user_choice == "9":
            search_about_height()
        elif user_choice == "10":
            search_about_language()
        else:
            print("\nPlease enter a number from 1 - 10")
            user_choice = input("Enter a number: ")
            continue
        user_choice = input("""
What do you want to search about?
Please enter only a number!

1. Exit
2. Go back to first page
3. Member in Algorhythm project name
4. Member unit name
5. Member youtube subscriber
6. Member debut year
7. Member birthday month
8. Member model artist or rigger
9. Member height
10. Member language

Enter a number: """)
                        
if __name__ == "__main__":
    menu()
