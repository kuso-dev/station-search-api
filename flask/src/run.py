from flask import Flask, jsonify
from flask_cors import CORS
import pymysql.cursors
app = Flask(__name__)
CORS(app)


def getDBConnection():
    return pymysql.connect(
        host='db',
        port=3306,
        user='user',
        passwd='password',
        db='station_database',
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route("/api/v1/station/")
def getStation():
    station = getStation()
    return jsonify(station)


@app.route("/api/v1/station/pref/<int:prefectureCode>")
def getByPrefectureCode(prefectureCode):
    station = getStationByPrefectureCode(prefectureCode)
    return jsonify(station)


def getStation():
    conn = getDBConnection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM `m_station`"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        conn.close()
        return result


def getStationByPrefectureCode(prefectureCode):
    conn = getDBConnection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM `m_station` WHERE pref_cd = %s"
            cursor.execute(sql, (prefectureCode,))
            result = cursor.fetchall()
            return result
    finally:
        conn.close()
        return result


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
