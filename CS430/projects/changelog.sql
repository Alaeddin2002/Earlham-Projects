CREATE TABLE changelog (
pre text,
types text,
tstamp timestamp DEFAULT now()
);

\i ialaed20_pet_data.sql

\i ialaed20_pets_changelog.sql
        
Insert into household values('Tex','04/02/2025',10, 5251, 'chicken');

UPDATE household
set name = 'Mufasa' where name = 'Simba';

DELETE FROM household where name = 'Rex' and type = 'chicken';

select * from changelog;