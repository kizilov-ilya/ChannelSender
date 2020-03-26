from pymysql import connect
from pymysql import Error
from scripts.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

BASE_MEDIA_PATH = "C:\\Users\\Ilya\\PycharmProjects\\ChannelSender\\scripts\\demo-media\\pics\\photo.jpg"


def convert_to_binary_data(filename):
    with open(filename, "rb") as file:
        binaryDATA = file.read()
    return binaryDATA


def insertBLOB(picture):
    print("Inserting BLOB file into picture_post table!")
    try:
        connection = connect(host=DB_HOST, user=DB_USER, db=DB_NAME, password=DB_PASSWORD)
        cursor = connection.cursor()
        post_picture = convert_to_binary_data(picture)
        result = cursor.execute("insert into picture_post values(%s,%s,%s,%s)", ('7', '0', '0', post_picture))
        connection.commit()
        print("Image inserted succesfully as a BLOB file", result)

    except Error as error:
        print(f"Failed inserting BLOB data into MySQL table {error}")

    finally:
        if (connection.open()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed!")


insertBLOB(BASE_MEDIA_PATH)
