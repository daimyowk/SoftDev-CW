'''
mysql
didnt support transactions

postgress
open source
slow but full sql

both upgrade over time

sqlite3
standalone library implement sql language
no server. like shelve in python
not full featured
good enough
types in sql
not all included
ex sqlite command
create table doughnuts(type text, price real, qty integer)
.schema show whats table about, description of data
insert into doughtntus values ("jelly",2.50,10)
insert into doughtnuts values ("glazed",3.00, 20)
.dump doughtnuts gives historyof what done
drop table doughtnuts gets rid of table

make textfile   blah.sql
create table doughts(type text, price real, qty integer);
insert into douhgnuts values ("jelly",2.50,10);
insert into doughnuts values("glazed",3.00,20);
insert into doughtnuts values("choco", 4.00,20);

read in sqlite
.read doughnut.sql

select *(everything) from doughnuts
select type from doughnuts
select type,qty doughnuts 
select * from doughnuts where qty > 5;
select * from doughtnuts where price >2.2 and qty <15;

rowid for each thing
select* from doughnuts where rowid<2;
delete from doughtnuts where rowid<4;

delete from doughnuts where qty=5;

update doughnuts set qty=qty-1 where type="jelly";

update doughnuts set qtty=qty+10

people.sql
name,age,id
homer,40,1
marge,40,2
bart,10,3
lisa,8,4
ralph,8,6
nelson,10,7
kierney,18,8

classes.sql
code,grade,id
