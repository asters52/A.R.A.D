import sqlite3

def create_table():
    try:
        conn = sqlite3.connect('Applicants.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Applicants (
                entry_number TEXT PRIMARY KEY,
                name TEXT,
                gender TEXT,
                date_of_birth TEXT,
                contact_info TEXT,
                job TEXT,
                occupants INTEGER, 
                requirements TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def fetch_applicants():
    try:
        conn = sqlite3.connect('Applicants.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Applicants')
        applicants = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        applicants = []
    finally:
        conn.close()
    return applicants

def insert_applicant(entry_number, name, gender, date_of_birth, contact_info, job, occupants, requirements):
    try:
        conn = sqlite3.connect('Applicants.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Applicants (entry_number, name, gender, date_of_birth, contact_info, job, occupants, requirements) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (entry_number, name, gender, date_of_birth, contact_info, job, occupants, requirements))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def delete_applicant(entry_number):
    try:
        conn = sqlite3.connect('Applicants.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Applicants WHERE entry_number = ?', (entry_number,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def update_applicant(new_name, new_gender, new_date_of_birth, new_contact_info, new_occupants,new_job, new_requirements, entry_number):
    try:
        conn = sqlite3.connect('Applicants.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Applicants 
            SET name = ?, gender = ?, date_of_birth = ?, contact_info = ?, occupants = ?, job = ?, requirements = ? 
            WHERE entry_number = ?
        ''', (new_name, new_gender, new_date_of_birth, new_contact_info, new_occupants, new_job, new_requirements, entry_number))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def entry_number_exists(entry_number):
    exists = False
    try:
        conn = sqlite3.connect('Applicants.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM Applicants WHERE entry_number = ?', (entry_number,))
        result = cursor.fetchone()
        exists = result[0] > 0
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
    return exists

create_table()
