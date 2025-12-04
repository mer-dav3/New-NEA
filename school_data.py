import sqlite3, os, time, pyinputplus as pyip

connection = sqlite3.connect("schooldata.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Students 
               (StudentID INTEGER PRIMARY KEY AUTOINCREMENT,Firstname TEXT, 
               Surname TEXT, DOB DATE, Gender TEXT, Mastery TEXT, 
               Yeargroup INTEGER,  Email TEXT)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Timetable 
               ( StudentID INTEGER, Day TEXT, Period1 TEXT, Period2 TEXT, 
               Period3 TEXT, Period4 TEXT, Period5 TEXT, Period6 TEXT, 
               FOREIGN KEY(StudentID) REFERENCES students(StudentID))''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Student_Info 
               (StudentID INTEGER, Parentname TEXT, Parentnumber INTEGER, 
               Address TEXT, Nationality TEXT, countryofbirth TEXT, Enrollmentdate DATE, 
               FOREIGN KEY(StudentID) REFERENCES students(StudentID))''') 


cursor.execute('''CREATE TABLE IF NOT EXISTS Medical_Info 
               (StudentID INTEGER, Conditions TEXT, Medication TEXT, Allergies TEXT, 
               Needs TEXT, FOREIGN KEY(StudentID) REFERENCES students(StudentID))''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Attendance 
               (AttendanceID INTEGER PRIMARY KEY AUTOINCREMENT, StudentID INTEGER, 
               Date DATE, Status TEXT, FOREIGN KEY(StudentID) REFERENCES students(StudentID))''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Behaviour 
               (BehaviourID INTEGER PRIMARY KEY AUTOINCREMENT, StudentID INTEGER, 
               Date DATE, Type TEXT, Value INTEGER, REASON TEXT, 
               FOREIGN KEY(StudentID) REFERENCES students(StudentID))''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Teachers 
               (TeacherID INTEGER PRIMARY KEY AUTOINCREMENT, Firstname TEXT, 
                Surname TEXT, Gender TEXT, Email TEXT, Role TEXT, SubjectID INTEGER, 
                FOREIGN KEY(SubjectID) REFERENCES subjects(SubjectID))''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Teacher_info 
               (TeacherID INTEGER, phonenumber INTEGER, personal_email TEXT, DOB DATE,
                qualifications TEXT, Emergency_contact INTEGER, Address TEXT,
                employment_start DATE,
                FOREIGN KEY(TeacherID) REFERENCES Teachers(TeacherID))''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Subjects 
                (SubjectID INTEGER PRIMARY KEY AUTOINCREMENT, Subjectname TEXT)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Scores 
               (ScoreID INTEGER PRIMARY KEY AUTOINCREMENT, StudentID INTEGER, SubjectID INTEGER, 
               Mean_Score INTEGER, Assessment1 FLOAT, Assessment2 FLOAT, Assessment3 FLOAT, 
               FOREIGN KEY(StudentID) REFERENCES students(StudentID), 
               FOREIGN KEY(SubjectID) REFERENCES subjects(SubjectID))''')   


cursor.execute('''CREATE TABLE IF NOT EXISTS Assessments
               (AssessmentID INTEGER PRIMARY KEY AUTOINCREMENT, StudentID INTEGER, 
               SubjectID INTEGER, Type TEXT, Score FLOAT, Date DATE, 
               FOREIGN KEY(StudentID) REFERENCES students(StudentID), 
               FOREIGN KEY(SubjectID) REFERENCES subjects(SubjectID))''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Summaries
               (SummaryID INTEGER PRIMARY KEY AUTOINCREMENT, StudentID INTEGER, 
               Week DATE, SummaryText TEXT, 
               FOREIGN KEY(StudentID) REFERENCES students(StudentID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Posts 
               (PostID INTEGER PRIMARY KEY AUTOINCREMENT,Title TEXT, Content TEXT, 
               Date DATE, Time Text, Attachments MEDIUMBLOB, TeacherID INTEGER,
               FOREIGN KEY(TeacherID) REFERENCES teachers(TeacherID))''')


cursor.execute('''CREATE TABLE IF NOT EXISTS M_Posts 
               (MPostID INTEGER PRIMARY KEY AUTOINCREMENT,Title TEXT, Content TEXT, 
               Date DATE, Time Text, Attachments MEDIUMBLOB, TeacherID INTEGER,
               FOREIGN KEY(TeacherID) REFERENCES teachers(TeacherID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS E_Posts 
               (EPostID INTEGER PRIMARY KEY AUTOINCREMENT,Title TEXT, Content TEXT, 
               Date DATE, Time Text, Attachments MEDIUMBLOB, TeacherID INTEGER,
               FOREIGN KEY(TeacherID) REFERENCES teachers(TeacherID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS S_Posts 
               (SPostID INTEGER PRIMARY KEY AUTOINCREMENT,Title TEXT, Content TEXT, 
               Date DATE, Time Text, Attachments MEDIUMBLOB, TeacherID INTEGER,
               FOREIGN KEY(TeacherID) REFERENCES teachers(TeacherID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS C_Posts 
               (CPostID INTEGER PRIMARY KEY AUTOINCREMENT,Title TEXT, Content TEXT, 
               Date DATE, Time Text, Attachments MEDIUMBLOB, TeacherID INTEGER,
               FOREIGN KEY(TeacherID) REFERENCES teachers(TeacherID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS H_Posts 
               (HPostID INTEGER PRIMARY KEY AUTOINCREMENT,Title TEXT, Content TEXT, 
               Date DATE, Time Text, Attachments MEDIUMBLOB, TeacherID INTEGER,
               FOREIGN KEY(TeacherID) REFERENCES teachers(TeacherID))''')



cursor.execute('''CREATE TABLE IF NOT EXISTS G_Replies 
               (ReplyID INTEGER PRIMARY KEY AUTOINCREMENT, PostID INTEGER,
               Content TEXT, Date DATE, Time TEXT, TeacherID INTEGER,
               FOREIGN KEY(PostID) REFERENCES posts(PostID), 
               FOREIGN KEY(TeacherID) REFERENCES teachers(TeacherID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS M_Replies 
               (ReplyID INTEGER PRIMARY KEY AUTOINCREMENT, MPostID INTEGER,
               Content TEXT, Date DATE, Time TEXT, TeacherID INTEGER,
               FOREIGN KEY(MPostID) REFERENCES M_posts(MPostID), 
               FOREIGN KEY(TeacherID) REFERENCES teachers(TeacherID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS E_Replies 
               (ReplyID INTEGER PRIMARY KEY AUTOINCREMENT, EPostID INTEGER,
               Content TEXT, Date DATE, Time TEXT, TeacherID INTEGER,
               FOREIGN KEY(EPostID) REFERENCES E_posts(EPostID), 
               FOREIGN KEY(TeacherID) REFERENCES teachers(TeacherID))''')  

cursor.execute('''CREATE TABLE IF NOT EXISTS S_Replies 
               (ReplyID INTEGER PRIMARY KEY AUTOINCREMENT, SPostID INTEGER,
               Content TEXT, Date DATE, Time TEXT, TeacherID INTEGER,
               FOREIGN KEY(SPostID) REFERENCES S_posts(SPostID), 
               FOREIGN KEY(TeacherID) REFERENCES teachers(TeacherID))''')       

cursor.execute('''CREATE TABLE IF NOT EXISTS C_Replies 
               (ReplyID INTEGER PRIMARY KEY AUTOINCREMENT, CPostID INTEGER,
               Content TEXT, Date DATE, Time TEXT, TeacherID INTEGER,
               FOREIGN KEY(CPostID) REFERENCES C_posts(CPostID), 
               FOREIGN KEY(TeacherID) REFERENCES teachers(TeacherID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS H_Replies 
               (ReplyID INTEGER PRIMARY KEY AUTOINCREMENT, HPostID INTEGER,
               Content TEXT, Date DATE, Time TEXT, TeacherID INTEGER,
               FOREIGN KEY(HPostID) REFERENCES H_posts(HPostID), 
               FOREIGN KEY(TeacherID) REFERENCES teachers(TeacherID))''')   




cursor.execute("INSERT INTO Teachers (Firstname, Surname, Gender, Email, Role, SubjectID) VALUES ('David', 'Akeredolu', 'M', 'akeredolud@mercia.school', 'A', 1)")
cursor.execute("INSERT INTO Teachers (Firstname, Surname, Gender, Email, Role, SubjectID) VALUES ('Carly', 'Perzl', 'F', 'perzlc@mercia.school', 'T', 4)")
cursor.execute("INSERT INTO Teachers (Firstname, Surname, Gender, Email, Role, SubjectID) VALUES ('Joshua', 'Curran', 'M', 'curranj@mercia.school', 'T', 5)")

cursor.execute("INSERT INTO Teacher_info (TeacherID, phonenumber, personal_email, DOB, qualifications, Emergency_contact, Address,employment_start) VALUES (1, 07396208138, 'doludavid15@gmail.com', '1998-07-30', 'MEng - Mechatronics and Robotics (University of Cambridge)', 07453662763, '12 Baker Street, London, UK', '2020-09-01')")
cursor.execute("INSERT INTO Teacher_info (TeacherID, phonenumber, personal_email, DOB, qualifications, Emergency_contact, Address,employment_start) VALUES (2, 07412345678, 'carlyperzl@gmail.com', '1995-05-15', 'BSc - Marine Biology (University of Oxford)', 07855443910, '34 Elm Street, London, UK', '2019-09-01')")
cursor.execute("INSERT INTO Teacher_info (TeacherID, phonenumber, personal_email, DOB, qualifications, Emergency_contact, Address,employment_start) VALUES (3, 07598765432, 'joshuacurran@gmail.com', '2000-11-22', 'PhD - Astrophysics (University of Cambridge)', 07987654321, '56 Oak Avenue, London, UK', '2023-09-01')")

cursor.execute("INSERT INTO Subjects (Subjectname) VALUES ('Admin')")
cursor.execute("INSERT INTO Subjects (Subjectname) VALUES ('Mathematics')")
cursor.execute("INSERT INTO Subjects (Subjectname) VALUES ('English')")
cursor.execute("INSERT INTO Subjects (Subjectname) VALUES ('Science')")
cursor.execute("INSERT INTO Subjects (Subjectname) VALUES ('Computing')")
cursor.execute("INSERT INTO Subjects (Subjectname) VALUES ('History')")

cursor.execute("INSERT INTO Scores  (StudentID, SubjectID, Mean_Score, Assessment1, Assessment2, Assessment3) VALUES (1, 2, 85, 80.0, 87.5, 90.0)")
cursor.execute("INSERT INTO Scores  (StudentID, SubjectID, Mean_Score, Assessment1, Assessment2, Assessment3) VALUES (1, 3, 78, 75.0, 80.0, 79.0)")
cursor.execute("INSERT INTO Scores  (StudentID, SubjectID, Mean_Score, Assessment1, Assessment2, Assessment3) VALUES (1, 4, 92, 90.0, 93.0, 91.0)") 
cursor.execute("INSERT INTO Scores  (StudentID, SubjectID, Mean_Score, Assessment1, Assessment2, Assessment3) VALUES (1, 5, 88, 85.0, 90.0, 89.0)")
cursor.execute("INSERT INTO Scores  (StudentID, SubjectID, Mean_Score, Assessment1, Assessment2, Assessment3) VALUES (1, 6, 74, 70.0, 75.0, 77.0)")

cursor.execute("INSERT INTO Behaviour (StudentID, Date, Type, Value, REASON) VALUES (1, '2025-11-24', 'Housepoints', 2, 'Good')")
cursor.execute("INSERT INTO Behaviour (StudentID, Date, Type, Value, REASON) VALUES (1, '2025-11-24', 'Housepoints', 5, 'Good')")
cursor.execute("INSERT INTO Behaviour (StudentID, Date, Type, Value, REASON) VALUES (1, '2025-11-25', 'Detention', 1, 'Late')")
cursor.execute("INSERT INTO Behaviour (StudentID, Date, Type, Value, REASON) VALUES (1, '2025-11-26', 'Housepoints', 3, 'Good')")
cursor.execute("INSERT INTO Behaviour (StudentID, Date, Type, Value, REASON) VALUES (1, '2025-11-27', 'Detention', 1, 'Talking')")
cursor.execute("INSERT INTO Behaviour (StudentID, Date, Type, Value, REASON) VALUES (1, '2025-11-28', 'Demerit', 1, 'Bad')")
cursor.execute("INSERT INTO Behaviour (StudentID, Date, Type, Value, REASON) VALUES (1, '2025-11-28', 'Housepoints', 4, 'Good')")
cursor.execute("INSERT INTO Behaviour (StudentID, Date, Type, Value, REASON) VALUES (1, '2025-11-28', 'Demerit', 1, 'Bad')")


connection.commit()
