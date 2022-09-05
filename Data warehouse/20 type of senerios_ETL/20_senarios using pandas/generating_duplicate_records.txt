create table input (guest_name varchar2(20),
                     city varchar2(15),
                     phone number(12),
                     company varchar(20),
                     no_of_records number(2));

insert into input values ('Tim','NY',12345678,'Chase',2);
insert into input values ('Bill','Dallas',67898899,'First Advantage',3);
insert into input values ('Ram','Bangalore','234234234','Intel',1);
insert into input values ('Raghu','Bangalore',829324923,'UB Group',2);
insert into input values ('Aman','NY',678123789,'UB Group',0);
insert into input values ('linus','NY',678123789,'UB Group',3);
select * from input;

select guest_name,city,phone,company 
from input i,
           (select rownum repeat from dual
            connect by level<=
           (select max(no_of_records) from input))m
where i.no_of_records >= m.repeat
order by guest_name;


