import sqlite3

member_name = []
month_list = ["January","Febuary","March","April","May","June","July","August","September","October","November","December"]


DATABASE = 'arp_vtuber.db'

def get_data_from_database(sql, params=None): 
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        results = cursor.fetchall()
    return results

def create_language_dict():
    language = {}
    sql = "SELECT * FROM language;"
    results = get_data_from_database(sql)
    for data in results:
        language[data[0]] = data[1]
    return language

def print_all_member_name():
    sql = "SELECT name FROM basic ORDER BY lower(name);"
    results = get_data_from_database(sql)
    print("\nName")
    for name in results:
        print(name[0])

def print_all_member_order_by_subsciber():

    sql = "SELECT name, youtube_subsciber FROM basic ORDER BY youtube_subsciber DESC;"
    
    results = get_data_from_database(sql)
    # print nicely
    print(f"\n{'No':3}{'Name':15}Youtube Subsciber")
    for i in range(len(results)):
        print(f"{i + 1:<3}{results[i][0]:<15}{results[i][1]}")
                    
def print_all_member_order_by_birthday():
    sql = "SELECT name, birthday FROM basic ORDER BY birthday;"
    results = get_data_from_database(sql)
    print(f"\n{'Name':<15}Birthday")
    for vtuber in results:
        birthday = vtuber[1].split()
        month = int(birthday[0])
        print(f"{vtuber[0]:<15}{birthday[1]} {month_list[month-1]}")
            
def print_all_member_unit():
    sql = "SELECT name, operation, unit FROM basic ORDER BY operation;"
    results = get_data_from_database(sql)
    print(f"\n{'Name':<15}Operation & Unit")
    for vtuber in results:
        print(f"{vtuber[0]:<15} {vtuber[1]} - {vtuber[2]}")

def print_all_member_character():
    sql = "SELECT name, character_type FROM basic ORDER BY lower(name);"
    results = get_data_from_database(sql)
        
    print(f"\n{'Name':<15}Character")
    for vtuber in results:
        print(f"{vtuber[0]:<15}{vtuber[1]}")
            
def print_all_member_model_maker():
    sql = "SELECT name, model_artist, model_rigger FROM basic"
    results = get_data_from_database(sql)
    print(f"\n{'Name':<15}{'Model Artist':<16}Model Rigger")
    for vtuber in results:
        print(f"{vtuber[0]:<15}{vtuber[1]:<16}{vtuber[2]}")
            
def print_all_member_debut():   
        sql = "SELECT name, debut FROM basic ORDER BY debut;"        
        results = get_data_from_database(sql)
        print(f"\n{'Name':<15}Debut")
        for vtuber in results:
            debut = vtuber[1].split()
            month = int(debut[1])
            print(f"{vtuber[0]:<15}{debut[2]} {month_list[month-1]} {debut[0]}")
            
def print_all_member_height():
        sql = "SELECT name, height FROM basic ORDER BY height;"
        results = get_data_from_database(sql)
        print(f"\n{'Name':<15}Height")
        for vtuber in results:
            print(f"{vtuber[0]:<15}{vtuber[1]} cm.")

def print_all_member_language():
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
            
            
def menu():
    user_choice = input("""
This is a database about Vtuber from the Algorhythm project.
What do you want to know?
Please enter only a number!

1. Exit
2. What is Vtuber?
3. What is the Algorhythm project?
4. Member in Algorhythm project
5. Member unit
6. Member youtube subscriber from highest
7. Member debut date
8. Member birthday
9. Member model
10. Member Character
11. Member height from shortest to highest 

Enter a number: """)
    while user_choice != "1":
        
        if user_choice == "2":
            print("""
A VTuber is an online entertainer who uses a virtual avatar generated using computer graphics. 
Real-time motion capture software or technology are often but not always used to capture movement.""")
        elif user_choice == "3":
            print("""
The Algorhythm Project, or Algorithm + Rhythm, is a journey of operating systems with the rhythm of music. 
We are a project that brings together VTubers (Virtual YouTubers) with diverse talents and personalities in one place. 
Our project focuses on entertaining everyone through live streaming and music. 
We believe that you will definitely find a VTuber you like because we truly have all kinds!
""")
        elif user_choice == "4":
            print_all_member_name()
        elif user_choice == "5":
            print_all_member_unit()
        elif user_choice == "6":
            print_all_member_order_by_subsciber()
        elif user_choice == "7":
            print_all_member_debut()
        elif user_choice == "8":
            print_all_member_order_by_birthday()
        elif user_choice == "9":
            print_all_member_model_maker()
        elif user_choice == "10":
            print_all_member_character()
        elif user_choice == "11":
            print_all_member_height()
        else:
            print("\nPlease enter a number from 1 - 11")
            user_choice = input("Enter a number: ")
            continue
            
            
        user_choice = input("""
What do you want to know?
Please enter only a number!

1. Exit
2. What is Vtuber?
3. What is the Algorhythm project?
4. Member in Algorhythm project
5. Member unit
6. Member youtube subscriber from highest
7. Member debut date
8. Member birthday
9. Member model
10. Member Character
11. Member height from shortest to highest 

Enter a number: """)

if __name__ == "__main__":
    print_all_member_language()
    # menu()
    # search_about_birthday()
    # create_language_dict()
