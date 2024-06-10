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
        
        print("Name")
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
        order = 1
        # print nicely
        print("Name           Youtube Subsciber")
        for name in results:
            print(f"{order}. {name[0]:<15}{name[1]}")
            order += 1
            
def print_all_member_order_by_birthday():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT name, birthday FROM basic ORDER BY birthday;"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        # print nicely
        print("Name           Birthday")
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
        
        print("Name            Operation & Unit")
        for vtuber in results:
            print(f"{vtuber[0]:<15} {vtuber[1]} - {vtuber[2]}")

def print_all_member_character():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT name, character_type FROM basic ORDER BY lower(name);"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        print("Name           Character")
        for vtuber in results:
            print(f"{vtuber[0]:<15}{vtuber[1]}")
            
def print_all_member_model_maker():
      with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT name, model_artist, model_rigger FROM basic"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        print("Name           Model Artist    Model Rigger")
        for vtuber in results:
            print(f"{vtuber[0]:<15}{vtuber[1]:<16}{vtuber[2]}")
            
def menu():
    user_choice = input("""This is a database about Vtuber from the Algorhythm project.
What do you want to know?
Please enter only a number!

1. Exit
2. What is Vtuber?
3. What is the Algorhythm project?
4. Member in Algorhythm project
5. Member youtube subscriber
6. Member debut date
7. Member birthday
8. 
""")
    if user_choice == "2":
        print("")
    elif user_choice == "3":
        print("""The Algorhythm Project, or Algorithm + Rhythm, is a journey of operating systems with the rhythm of music. 
We are a project that brings together VTubers (Virtual YouTubers) with diverse talents and personalities in one place. 
Our project focuses on entertaining everyone through live streaming and music. 
We believe that you will definitely find a VTuber you like because we truly have all kinds!""")
    elif user_choice == "4":
        print_all_member_name()
    elif user_choice == "5":
        print_all_member_order_by_subsciber()

if __name__ == "__main__":
    print_all_member_order_by_subsciber()
    
    
#   with sqlite3.connect(DATABASE) as db:
#         cursor = db.cursor()
#         sql = "SELECT ??? FROM ??? ..."
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         
#         print("???")
#         for ??? in results:
#             print(f"{???}")