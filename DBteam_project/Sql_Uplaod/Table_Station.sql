create table STATIONS (STATION_NAME varchar(60), RATE FLOAT(1));
CREATE UNIQUE INDEX STATION_NAME_PK ON STATIONS (STATION_NAME);
ALTER TABLE STATIONS ADD CONSTRAINT STATION_NAME_PK PRIMARY KEY (STATION_NAME);
