import sqlalchemy
import psycopg2

conn = psycopg2.connect(
    database=" ",
    user=" ",
    password=" ")


def create_db(conn):
    with conn.cursor() as cur:
        cur.execute('''create table if not exists clients(
        id_client  serial primary key,
        surname varchar (80),
        name varchar (60));''')
        cur.execute('''create table if not exists email_address(
        id_client integer not null references clients(id_client),
        email varchar(50)  unique not null);''')
        cur.execute('''create table if not exists phone_number(
        id_client integer not null references clients(id_client),
        phone_number varchar(12) unique not null);''')
        conn.commit()


def add_client(conn, first_name, last_name, email, phone=None):
    with conn.cursor() as cur:
        if email is not None and first_name is not None and last_name is not None:
            count_id = cur.execute('''select count(id_client) from clients''')
            count_id = cur.fetchone()[0]
            cur.execute(
                '''insert into clients (id_client, surname,name) values (%s,%s,%s);''',
                (int(
                    count_id +
                    1),
                    first_name,
                    last_name))
            cur.execute(
                ''' insert into email_address(id_client,email) values(%s,%s);''',
                (int(
                    count_id +
                    1),
                    email))
        else:
            print(
                "Регистрация без электронного адреса недопустима. Добавьте, пожалуйста, email")

        if len(phone) > 12 or phone[0:2] != '+7' or len(phone) < 12:
            if len(phone) < 11 or len(phone) > 11 or phone[0:1] != '8':
                print(f'Введите корректный номер телефона, с 8 или +7')
            else:
                cur.execute('''insert into phone_number(id_client,phone_number) values(%s,%s);''',
                            (int(count_id + 1), phone))
                conn.commit()


def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        if len(phone) > 12 or phone[0:2] != '+7' or len(phone) < 12:
            if len(phone) < 11 or len(phone) > 11 and phone[0:1] != '8':
                print("Введите корректный номер телефона,  с 8 или  +7")
        else:
            cur.execute(
                '''insert into phone_number(id_client,phone_number) values (%s,%s);''',
                (client_id,
                 phone))
            conn.commit()


def change_client(conn, client_id, first_name=None,
                  last_name=None, email=None):
    with conn.cursor() as cur:
        changes_name = cur.execute(
            '''select surname,name from clients where id_client=%s;''', (client_id,))
        changes_name = cur.fetchone()
        changes_email = cur.execute(
            '''select email from email_address where id_client=%s;''', (client_id,))
        changes_email = cur.fetchone()
        print(
            f'Данные по клиенту {changes_name[0]} {changes_name[1]} отредактированы')
        cur.execute(
            '''update clients set surname=%s,name=%s where id_client=%s;''',
            (first_name,
             last_name,
             client_id))
        cur.execute(
            '''update email_address set email=%s where id_client=%s;''',
            (email,
             client_id))
        conn.commit()


def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        current = cur.execute(
            '''select phone_number from phone_number where id_client=%s and phone_number=%s;''',
            (client_id,
             phone))
        current = cur.fetchone()
        if current is not None:
            cur.execute(
                '''delete from phone_number where id_client=%s and phone_number=%s;''',
                (client_id,
                 phone))
            conn.commit()
        else:
            print(f'Клиент с таким номером отсутствует в базе')


def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute(
            '''delete  from email_address where id_client=%s;''', (client_id,))
        cur.execute(
            '''delete  from phone_number where id_client=%s;''', (client_id,))
        cur.execute(
            '''delete  from clients where id_client=%s;''', (client_id,))
        conn.commit()


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        if first_name is not None or last_name is not None or email is not None and phone is None:
            select = cur.execute('''select surname, name from clients cl
            join email_address ed on cl.id_client=ed.id_client
            where name=%s or surname=%s or email=%s;''', (last_name, first_name, email))
            select = cur.fetchall()
            print(select)
        if phone is not None and first_name is None and last_name is None and email is None:
            select = cur.execute('''select name,surname from clients cl
            join phone_number  ph on cl.id_client=ph.id_client
            where phone_number=%s
            group by cl.id_client;''', (phone,))
            select = cur.fetchall()
            print(select)
        conn.close()


create_db(conn)
add_client(
    conn,
    first_name='Козлов',
    last_name='Юрий',
    email='nik_kozlov@ygmail.ru',
    phone='+79371111113')
add_phone(conn, client_id='3', phone='+79270000000')
change_client(
    conn,
    client_id=4,
    first_name='Сидоров',
    last_name='Иван',
    email='i_sidorov@gmail.com')
delete_phone(conn, client_id=3, phone='89960000000')
delete_client(conn, client_id=7)
find_client(
    conn,
    first_name=None,
    last_name=None,
    email=None,
    phone='89060000000000')

conn.close()
