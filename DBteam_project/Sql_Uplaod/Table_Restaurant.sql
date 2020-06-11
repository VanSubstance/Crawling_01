create table RESTAURANTS (STATION_NAME varchar(60), RESTAURANT_NAME varchar(60), CTGR varchar(60), REV_NUM varchar(60), URL varchar(400));
ALTER TABLE RESTAURANTS ADD CONSTRAINT RESTAURANT_NAME_PK PRIMARY KEY (RESTAURANT_NAME, STATION_NAME);
ALTER TABLE RESTAURANTS MODIFY COLUMN RESTAURANT_NAME VARCHAR(60) NOT NULL;
ALTER TABLE RESTAURANTS ADD CONSTRAINT RESTAURANT_FK FOREIGN KEY (STATION_NAME) REFERENCES STATIONS (STATION_NAME);
