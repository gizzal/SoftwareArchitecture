import json
import requests
import psycopg2
import paho.mqtt.client as mqtt

DB_HOST = '35.187.119.223'
DB_NAME = 'optimus'
DB_USER = 'optimus'
DB_PASSWORD = 'optimus'

db = psycopg2.connect(
    "dbname='{}' user='{}' host='{}' password='{}'".format(
        DB_NAME, DB_USER, DB_HOST, DB_PASSWORD
    ))
cursor = db.cursor()


def on_message(client, userdata, msg):
    json_data = json.loads(msg.payload.decode('utf-8'))
    print(json_data)

    try:
        cursor.execute(
            "INSERT INTO "
            "mission_point(mission_id, vehicle_id, timestamp, lat, long, alt) "
            "values ({}, {}, {}, {}, {}, {});".format(
                json_data['mission_id'],
                json_data['vehicle_id'],
                json_data['timestamp'],
                json_data['location']['lat'],
                json_data['location']['lon'],
                json_data['location']['alt']))

        cursor.execute('SELECT LASTVAL();')
        id_of_new_row = cursor.fetchone()[0]
        for sensor in json_data['sensors']:
            if 'value' not in sensor:
                sensor['value'] = ""

            try:
                cursor.execute(
                    "INSERT INTO mission_point_sensors_data("
                    "mission_point_id, slug, warning, value) "
                    "values ({}, '{}', {}, '');".format(
                        id_of_new_row,
                        sensor['slug'],
                        sensor['warning']))

                cursor.execute('SELECT LASTVAL();')
                id_new_row = cursor.fetchone()[0]
                try:
                    if isinstance(sensor['value'], float):
                        cursor.execute(
                            "UPDATE mission_point_sensors_data "
                            "SET value={} WHERE id={}".format(
                                sensor['value'], id_new_row
                            ))
                    else:
                        cursor.execute(
                            "UPDATE mission_point_sensors_data "
                            "SET value='{}' WHERE id={}".format(
                                sensor['value'], id_new_row
                            ))
                    db.commit()
                except psycopg2.Error as e:
                    print("cannot update mission point sensor data:(")
                    print(e.pgerror)
                    print(e.diag.message_detail)
            except psycopg2.Error as e:
                print("cannot insert mission point sensor data:(")
                print(e.pgerror)
                print(e.diag.message_detail)
    except psycopg2.Error as e:
        print("cannot insert mission point :(")
        print(e.pgerror)
        print(e.diag.message_detail)


if '__main__':
    client = mqtt.Client()
    client.on_message = on_message

    client.connect(
        '35.189.64.191',
        1883,
        60)
    client.subscribe("test")

    while True:
        client.loop()
