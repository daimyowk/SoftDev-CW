'''
cannot run refer to classcode
cvs file
read each line 
split on commas

#doesnt really work cause proper csv has quotes on strings and commas in strings

f=open(file.cvs)
for line in f.readlines():
    print line.strip().split(",")

#easy way
#csv module
#reads csv with quotes and commas in strings and convert all to string
import csv
def csv_list():
    reader = csv.reader(open("people.csv"))
    BASELINE = "Name: %s, id: %s, Age %s"
    for line in reader:
        print BASELINE%(line[0],line[1],line[2])

# %whatever are placeholders

s="%s %d"
type matters
%s for string
%d integer
%f float
%5s leaves five space then string
print variable(stuff for holders)
comes from C

csv_list()

def csv_dict():
    reader = csv.DictRead(open("people.csv"))
    # puts into dictionary
    BASELINE = "Name: %(name)s, id: %(id)s, Age:%(age)d"
    print line
    print BASELINE%line
'''

import sqlite3

#need connection to datebase
conn = sqlite3.connect("demo.db")

c=conn.cursor() #not sure definition of cursor

q="create table people(name text, age integer, id integer)"
c.execute(q)

q="create table classes(name text, grade integer, id integer)"
c.execute(q)

BASE = "INSERT INTO people VALUES(%(name)s, %(age)s, %(id)s)"
for l in csv.DictRead(open("people.csv")):
    q=BASE%l
    print q
    c.excute(q)

BASE="""
INSERT INTO classes
  Values('%(name)s',

conn.commit()


################### QUERY
import sqlite3
conn=sqlite3.conect(demo.db)
c=conn.cursor()
q="""
SELECT people.name, classes.


