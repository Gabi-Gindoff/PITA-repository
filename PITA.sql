create table Account (
psuID varchar(7) not null,
firstName varchar(25),
lastName varchar(25),
email varchar(25),
primary key (PSUID));

create table Chat (
chatID int not null,
startTime timestamp,
endTime timestamp,
primary key (chatID));

create table Message (
messageID int not null,
text varchar(255) not null,
timestamp timestamp not null,
psuID varchar(7) not null,
chatID int not null,
primary key (messageID),
foreign key (psuID) references Account(psuID),
foreign key (chatID) references Chat(chatID));

create table Information (
infoID int not null,
questions varchar(255),
answers varchar(255),
primary key (infoID));

create table AIResponse (
responseID int not null,
text varchar(255),
timestamp timestamp,
chatID int not null,
infoID int not null,
primary key (responseID),
foreign key (chatID) references Chat(chatID),
foreign key (infoID) references Information(infoID));