import sqlite3

con = sqlite3.connect("MIC_CHECK.db")

c=con.cursor()

#create table
c.execute('''create table stocks (data text, text num, boin text)''')

#Insert a row of data
c.execute("""insert into stocks values('$B$"$$$&$($*(B','5','aiueo')""")

con.commit()

c.close
