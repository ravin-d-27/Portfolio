import mysql.connector as m
file=open('commentdetails.txt','r+')
read = file.readlines()
new=[]
for i in read:
    new.append(i[:-1])
file.close()
mydb = m.connect(host='localhost',user='admin',passwd='admin1234',database='comments')
c=mydb.cursor()
c.execute("insert into mycomments values('{}','{}','{}')".format(new[0],new[1],new[2]))
mydb.commit()
open('commentdetails.txt', 'w').close()
