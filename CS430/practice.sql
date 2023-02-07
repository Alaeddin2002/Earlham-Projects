drop table if exists MAKER cascade; 
CREATE TABLE MAKER (
maker varchar(1),
maker_ID int,
country varchar(10),
type varchar(3), 
primary key(maker_ID)
);

insert INTO MAKER values( 'A', 796,'portugal', 'yes');
insert INTO MAKER values( 'A', 111,'America', 'yes');
insert INTO MAKER values( 'B',213, 'palestine', 'no');
insert INTO MAKER values( 'B',000, 'Jordan', 'no');