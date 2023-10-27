create table Account (
email varchar(25),
firstName varchar(25),
lastName varchar(25),
primary key (email));

create table Chat (
chatID int not null,
startTime timestamp,
endTime timestamp,
primary key (chatID));

create table Message (
messageID int not null,
text varchar(255) not null,
timestamp timestamp not null,
email varchar(25) not null,
chatID int not null,
primary key (messageID),
foreign key (email) references Account(email),
foreign key (chatID) references Chat(chatID));

create table HelpDeskTickets (
inforID int primary key,
question text,
response text,
date date,
category varchar(255)
);

create table AIResponse (
responseID int not null,
text varchar(255),
timestamp timestamp,
chatID int not null,
inforID int,
primary key (responseID),
foreign key (chatID) references Chat(chatID),
foreign key (inforID) references HelpDeskTickets(inforID));
