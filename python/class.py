'''class computer():
    def Desktop(self):
        print("We can handle in some place")
    def laptop(self):
        print("We can carry it with us")
class Mobile(computer):
    pass
class Tab(Mobile):
    pass
M=Mobile()
M.Desktop()
M.laptop()
T=Tab()
T.laptop()'''

import mysql.connector

con=mysql.connector.connect(
    host = "192.168.1.240",
    user = "AIBATCH01",
    password = "AI@123",
    database = "ai_kalai"
    )

print(con)
result = con.cursor()
result.execute("show tables")
resultshow=result.fetchall()
for x in resultshow:
    print(x)


    
        