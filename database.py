import sqlite3

from internet import check_internet_connection



def create_connection():
    connection = sqlite3.connect("memory.db")
    return connection


def get_question_and_answer():
    con = create_connection()
    cur = con.cursor()
    cur.execute("select * from qanda")
    return cur.fetchall()


def insert_question_and_answer(question, answer):
    con = create_connection()
    cur = con.cursor()
    query = "INSERT INTO qanda values('" + question + "','" + answer + "')"
    cur.execute(query)
    con.commit()


def get_answer_from_memory(question):
    rows = get_question_and_answer()
    answer = ""
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break
    return answer


def get_name():
    con = create_connection()
    cur = con.cursor()
    query = "select value from memory where name = 'assistant_name'"
    cur.execute(query)
    con.commit()
    return cur.fetchall()[0][0]


def update_name(newname):
    con = create_connection()
    cur = con.cursor()
    query = "update memory set value = '" + newname + "' where name = 'assistant_name'"
    cur.execute(query)
    con.commit()


def update_last_seen(last_seen_date):
    con = create_connection()
    cur = con.cursor()
    query = "update memory set value ='" + str(last_seen_date) + "' where name = 'last_seen'"
    cur.execute(query)
    con.commit()


def get_last_seen():
    con = create_connection()
    cur = con.cursor()
    query = "select value from memory where name = 'last_seen'"
    cur.execute(query)
    con.commit()
    return str(cur.fetchall()[0][0])


def turn_speech_on():
    if check_internet_connection:
        con = create_connection()
        cur = con.cursor()
        query = "update memory set value ='on' where name = 'speech'"
        cur.execute(query)
        con.commit()
        return "speech turn off"
    else:
        return "hey please turn on internet first"


def turn_speech_off():
    con = create_connection()
    cur = con.cursor()
    query = "update memory set value ='off' where name = 'speech'"
    cur.execute(query)
    con.commit()
    return "ok i won't speak"


def speak_is_on():
    con = create_connection()
    cur = con.cursor()
    query = "select value from memory where name = 'speech'"
    cur.execute(query)
    con.commit()
    ans = str(cur.fetchall()[0][0])
    if ans == "on":
        return True
    else:
        return False
