import os
import logging
from tqdm import tqdm
from pymysql import connect
from pymysql import Error
from scripts.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG)

BASE_MEDIA_PATH = "./demo-media"

'''
def convert_to_binary_data(folder_path, filename):
    with open(os.path.join(folder_path, filename), "rb") as file:
        binaryDATA = file.read()
    return binaryDATA
'''

def insertBLOB(folder):
    logging.info("Inserting BLOB file into picture_post table!")
    try:
        connection = connect(host=DB_HOST, user=DB_USER, db=DB_NAME, password=DB_PASSWORD)
        cursor = connection.cursor()
        folder_path = os.path.join(BASE_MEDIA_PATH, folder)
        for filename in tqdm(os.listdir(folder_path)):
            if filename.startswith('.'):
                continue

            print(f'Started processing {filename}')
            with open(os.path.join(folder_path,filename),'rb') as file:

                post_value = file.read()
                cursor.execute("insert into picture_post(picture) values(%s)", (post_value))
                connection.commit()
                print("Image inserted succesfully as a BLOB file")

    except Error as error:
        print(f"Failed inserting BLOB data into MySQL table {error}")

    finally:
        if (cursor.connection):
            cursor.close()
            connection.close()
            print("MySQL connection is closed!")


insertBLOB('files')
