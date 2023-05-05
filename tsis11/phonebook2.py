import psycopg2
import re

def main():
    cn = psycopg2.connect(
        host = "localhost",
        database = "phonebook",
        user = "postgres",
        password = "14521"
    )
    
    on = True
    mode = 'ASC'
    cn.autocommit = True

    with cn.cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS phonebook(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(40) NOT NULL,
        phone_number VARCHAR(40) NOT NULL
        ) """)
        
    while on:
        a = int(input("\n1 - add,\n2 - delete,\n3 - update,\n4 - look,\n5 - clear,\n6 - resort,\n7 - import from csv\n8 - query\n:"))
        if a == 1:
            name = input("enter name: ")
            number = input("enter phone number: ")
            with cn.cursor() as cur:
                cur.execute(f"""INSERT INTO phonebook(first_name, phone_number)
                VALUES ('{name}','{number}')""")
        elif a == 2:
            name = input("enter to delete: ")
            with cn.cursor() as cur:
                cur.execute(f"DELETE FROM phonebook WHERE first_name = '{name}'")
                
        elif a == 3:
            uname = input("what contact you will update?: ")
            name = input("enter new name: ")
            number=input("enter new phone number: ")
            with cn.cursor() as cur:
                cur.execute(f"UPDATE phonebook SET first_name = '{name}' WHERE first_name = '{uname}'")
                cur.execute(f"UPDATE phonebook SET phone_number = '{number}' WHERE first_name = '{name}'")
                
        elif a == 4:
            with cn.cursor() as cur:
                if mode == 'ASC':
                    cur.execute(f"""SELECT * FROM phonebook ORDER BY first_name ASC""")
                if mode == 'DESC':
                    cur.execute(f"""SELECT * FROM phonebook ORDER BY first_name DESC""")
                all = cur.fetchall()
                for _,name,phone in all:
                    print("|"+name+"---"+phone+"|")
                    
        elif a == 5:
            with cn.cursor() as cur:
                cur.execute("TRUNCATE TABLE phonebook;")
                
        elif a == 6:
            change = input("1 - by alphabetical\n2 - by inverse alphabetical\nwhich ?\n")
            if change == 1:
                mode = 'ASC'
            else:
                mode = 'DESC'
                
        elif a == 7:
            #path = input("give path,NOT RELATIVE\n")
            path = "C:/Users/User/Desktop/python/tsis10/table.csv"
            with open(f"{path}",'r') as file:
                content = file.read()
                for cont in list(re.split("\n", content)):
                    conte = list(re.split(",",cont))
                    if conte[0]=='':
                        continue
                    print(conte)
                    with cn.cursor() as cur:
                        cur.execute(f"""INSERT INTO phonebook(first_name,phone_number)
                        VALUES ('{conte[0]}','{conte[1]}')""")
        elif a == 8:
            x = input("What would you like to query?\n1 - name\n2 - phone?\n:")
            if x == '1':
                name = input("enter name: ")
            else:
                name = input("enter phone number: ")
            with cn.cursor() as cur:
                if x == '1':
                    cur.execute(f"""SELECT phone_number FROM phonebook WHERE first_name = '{name}'""")
                else:
                    cur.execute(f"""SELECT first_name FROM phonebook WHERE phone_number = '{name}'""")
                if x == '1':
                    print(name, cur.fetchone())
                else:
                    print(cur.fetchone(), name)

    cn.close()

if __name__ == "__main__":
    main()
