create table ACTIVITIES (STATION_NAME varchar(60), ACTIVITY_NAME varchar(60), REV_NUM varchar(60), CTGR varchar(60), URL varchar(400));
CREATE UNIQUE INDEX ACTIVITY_NAME_PK ON ACTIVITIES (ACTIVITY_NAME);
ALTER TABLE ACTIVITIES ADD CONSTRAINT ACTIVITY_NAME_PK PRIMARY KEY (ACTIVITY_NAME);
ALTER TABLE ACTIVITIES MODIFY ACTIVITY_NAME varchar(60) NOT NULL;
ALTER TABLE ACTIVITIES ADD CONSTRAINT ACTIVITIES_FK FOREIGN KEY (STATION_NAME) REFERENCES STATIONS (STATION_NAME);
