SET DEFINE OFF;
DROP TABLE RESTAURANTS;
create table RESTAURANTS ("STATION_NAME" varchar(60), "RESTAURANTS_NAME" varchar(60), "REV_NUM" varchar(60), "CTGR" varchar(60), "URL" varchar(400));
CREATE UNIQUE INDEX "RESTAURANTS_NAME_PK" ON "RESTAURANTS" ("RESTAURANTS_NAME");
ALTER TABLE "RESTAURANTS" ADD CONSTRAINT "RESTAURANTS_NAME_PK" PRIMARY KEY ("RESTAURANTS_NAME");
ALTER TABLE "RESTAURANTS" MODIFY ("RESTAURANTS_NAME" NOT NULL ENABLE);
ALTER TABLE "RESTAURANTS" ADD CONSTRAINT "RESTAURANTS_FK" FOREIGN KEY ("STATION_NAME") REFERENCES "STATIONS" ("STATION_NAME") ENABLE;
