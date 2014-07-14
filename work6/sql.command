#create databae
create database restaurant default character set utf8;

#create tables
#1
create table chefmozaccepts(placeID bigint,Rpayment longtext);
LOAD DATA LOCAL INFILE 'Downloads/RCdata/chefmozaccepts.csv' INTO TABLE chefmozaccepts FIELDS TERMINATED BY ',' IGNORE 1 LINES;

#2
create table chefmozcuisine(placeID bigint,Rcuisine longtext);
LOAD DATA LOCAL INFILE 'Downloads/RCdata/chefmozcuisine.csv' INTO TABLE chefmozcuisine FIELDS TERMINATED BY ',' IGNORE 1 LINES;

#3
create table chefmozhours4(placeID bigint,hours longtext,days longtext);
LOAD DATA LOCAL INFILE 'Downloads/RCdata/chefmozhours4.csv' INTO TABLE chefmozhours4 FIELDS TERMINATED BY ',' IGNORE 1 LINES;

#4
create table chefmozparking(placeID bigint,parking_lot longtext);
LOAD DATA LOCAL INFILE 'Downloads/RCdata/chefmozparking.csv' INTO TABLE chefmozparking FIELDS TERMINATED BY ',' IGNORE 1 LINES;

#5
create table geoplaces2(
placeID bigint,
latitude double,
longitude double,
the_geom_meter longtext,
name longtext,
address longtext,
city longtext,
state longtext,
country longtext,
fax longtext,
zip longtext,
alcohol longtext,
smoking_area longtext,
dress_code longtext,
accessibility longtext,
price longtext,
url longtext,
Rambience longtext,
franchise longtext,
area longtext,
other_services longtext);
LOAD DATA LOCAL INFILE 'Downloads/RCdata/geoplaces2.csv' INTO TABLE geoplaces2 FIELDS TERMINATED BY ',' IGNORE 1 LINES;

#6
create table rating_final(
userID longtext,
placeID bigint,
rating bigint,
food_rating bigint,
service_rating bigint);

LOAD DATA LOCAL INFILE 'Downloads/RCdata/rating_final.csv' INTO TABLE rating_final FIELDS TERMINATED BY ',' IGNORE 1 LINES;

#7
create table usercuisine(
userID longtext,
Rcuisine longtext);
LOAD DATA LOCAL INFILE 'Downloads/RCdata/usercuisine.csv' INTO TABLE usercuisine FIELDS TERMINATED BY ',' IGNORE 1 LINES;

#8
create table userpayment(
userID longtext,
Upayment longtext);
LOAD DATA LOCAL INFILE 'Downloads/RCdata/userpayment.csv' INTO TABLE userpayment FIELDS TERMINATED BY ',' IGNORE 1 LINES;

#9
create table userprofile(
userID longtext,
latitude double,
longitude double,
smoker longtext,
drink_level longtext,
dress_preference longtext,
ambience longtext,
transport longtext,
marital_status longtext,
hijos longtext,
birth_year year,
interest longtext,
personality longtext,
religion longtext,
activity longtext,
color longtext,
weight bigint,
budget longtext,
height double);
LOAD DATA LOCAL INFILE 'Downloads/RCdata/userprofile.csv' INTO TABLE userprofile FIELDS TERMINATED BY ',' IGNORE 1 LINES;
