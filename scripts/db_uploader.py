import mysql.connector
import logging
from mysql.connector import Error
from scripts.config import DB_NAME, DB_PASSWORD, DB_USER, DB_HOST

logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG)
BASE_MEDIA_PATH = "C:\\Users\\Public\\Pictures\\Sample Pictures\\1.jpg"


# using print until demo

def convert_to_binary_data(filename):
    with open(filename, "rb") as file:
        binaryDATA = file.read()
    return binaryDATA


def insertBLOB(picture):
    print("Inserting BLOB file into picture_post table!")
    try:
        connection = mysql.connector.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        cursor = connection.cursor()
        sql_insert_blob_query = "INSERT INTO picture_post(picture) VALUES (%s);"
        post_picture = convert_to_binary_data(picture)
        insert_blob_tuple = (post_picture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image inserted succesfully as a BLOB file", result)

    except mysql.connector.Error as error:
        print(f"Failed inserting BLOB data into MySQL table {error}")

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed!")


insertBLOB(BASE_MEDIA_PATH)
#IS NOT WORK FIX LATER