import myDatabase

db=myDatabase.load('table.db')
db.set('name','jagannath')
db.dump()
db.set('key','value')
db.dump()
db.set('age',19)
db.dump()
db.set('gender','male')
db.dump()
db.set('address','noida')
db.dump()
db.set('apple',25)
db.dump()
db.set('mango',22)
db.set('chicken','5kg')
# db.random_insert(5)
# db.dump()

db.rem('age')
db.dump()

# db.del_db()
# db.dump()


a=db.get('key')
print(a)
b=db.get('name')
print(b)
c=db.get_all()
print(c)
print(db.exists('age'))
print(db.total_keys())

#-----------------------------------------
db2=myDatabase.load('table2.db')
db2.set('name','jagan')
print(db2.get('name'))

# #---------------------------
db3=myDatabase.load('some_others.db')
db3.set('some','other')
# print(db1.get('some'))
db.demerge('some_others.db')
print(db.get_all())
