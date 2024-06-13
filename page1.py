import sqlite3

member_name = []
month_list = ["January","Febuary","March","April","May","June","July","August","September","October","November","December"]


DATABASE = 'arp_vtuber.db'

def member_info_list():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM basic ;"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        # for vtuber in results:
        #     member_name.append(vtuber[1])
        # # print nicely
        # member_name.sort()
        print(results)
        

def print_all_member_name():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM basic ORDER BY lower(name);"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        print("\nName")
        order = 1
        for name in results:
            print(f"{order}. {name[1]}")
            order += 1

def print_all_member_order_by_subsciber():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT name, youtube_subsciber FROM basic ORDER BY youtube_subsciber DESC;"
        cursor.execute(sql)
        results = cursor.fetchall()
        order = 0
        # print nicely
        print("\nName              Youtube Subsciber")
        for name in results:
            order += 1
            if order >= 10:               
                print(f"{order}. {name[0]:<15}{name[1]}")
            else:
                print(f"{order}. {name[0]:<16}{name[1]}")
            
def print_all_member_order_by_birthday():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT name, birthday FROM basic ORDER BY birthday;"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        # print nicely
        print("\nName           Birthday")
        for vtuber in results:
            
            birthday = vtuber[1].split()
            month = int(birthday[0])
            print(f"{vtuber[0]:<15}{birthday[1]} {month_list[month-1]}")
            
def print_all_member_unit():
     with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT name, operation, unit FROM basic ORDER BY operation;"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        print("\nName            Operation & Unit")
        for vtuber in results:
            print(f"{vtuber[0]:<15} {vtuber[1]} - {vtuber[2]}")

def print_all_member_character():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT name, character_type FROM basic ORDER BY lower(name);"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        print("\nName           Character")
        for vtuber in results:
            print(f"{vtuber[0]:<15}{vtuber[1]}")
            
def print_all_member_model_maker():
      with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT name, model_artist, model_rigger FROM basic"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        print("\nName           Model Artist    Model Rigger")
        for vtuber in results:
            print(f"{vtuber[0]:<15}{vtuber[1]:<16}{vtuber[2]}")
            
def print_all_member_debut():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT name, debut FROM basic ORDER BY debut;"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        # print nicely
        print("\nName           Debut")
        for vtuber in results:
            
            debut = vtuber[1].split()
            month = int(debut[1])
            print(f"{vtuber[0]:<15}{debut[2]} {month_list[month-1]} {debut[0]}")
            
def print_all_member_height():
      with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT name, height FROM basic ORDER BY height;"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        print("\nName           Height")
        for vtuber in results:
            print(f"{vtuber[0]:<15}{vtuber[1]} cm.")
   
def search_about_in_name():
    letter_name = input("What word or letter? : ")
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = f"SELECT name FROM basic WHERE name LIKE '%{letter_name}%' ORDER BY name;"
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) == 0:
            print(f'No one has "{letter_name}" in their name.')
        else:
            print(f'Name of Vtuber who has "{letter_name}" in name!')
            for vtuber in results:
                print(f"{vtuber[0]}")

def search_about_subscriber():
    subscriber = input("How Many? :")
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT name, youtube_subsciber FROM basic WHERE youtube_subsciber > ? ORDER BY youtube_subsciber DESC;"
        cursor.execute(sql,(subscriber,))
        results = cursor.fetchall()
        order = 0
        # print nicely
        print("\nName              Youtube Subsciber")
        for name in results:
            order += 1
            if order >= 10:               
                print(f"{order}. {name[0]:<15}{name[1]}")
            else:
                print(f"{order}. {name[0]:<16}{name[1]}")
            
            
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
    search_about_in_name()
    
    
#   with sqlite3.connect(DATABASE) as db:
#         cursor = db.cursor()
#         sql = "SELECT ??? FROM ??? ..."
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         
#         print("???")
#         for ??? in results:
#             print(f"{???}")