CREATE TABLE IF NOT EXISTS m_station (
    station_cd     INT(11)       DEFAULT 0 NOT NULL PRIMARY KEY,
    station_g_cd   INT(11)       DEFAULT 0 NOT NULL,
    station_name   VARCHAR(256)  DEFAULT '' NOT NULL,
    station_name_k VARCHAR(256)  DEFAULT NULL,
    station_name_r VARCHAR(256)  DEFAULT NULL,
    station_name2  VARCHAR(256)  DEFAULT NULL,
    station_number VARCHAR(256)  DEFAULT NULL,
    station_u      VARCHAR(256)  DEFAULT NULL,
    line_cd        INT(11)       DEFAULT 0 NOT NULL,
    pref_cd        SMALLINT(6)   DEFAULT 0,
    post           VARCHAR(32)   DEFAULT NULL,
    address        VARCHAR(1024) DEFAULT NULL,
    lon            DOUBLE        DEFAULT 0,
    lat            DOUBLE        DEFAULT 0,
    open_ymd       date          DEFAULT NULL,
    close_ymd      date          DEFAULT NULL,
    e_status       SMALLINT(6)   DEFAULT 0,
    e_sort         INT(11)       DEFAULT 0
);