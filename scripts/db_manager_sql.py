import aiomysql
from pymysql import connect
from scripts.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER
from scripts.models import PicturePost

async def create_con(loop):
    con = await aiomysql.connect(host=DB_HOST, user=DB_USER, db=DB_NAME, password=DB_PASSWORD, loop=loop)
    cur = await con.cursor()
    return con, cur



def create_sync_con():
    con = connect(host=DB_HOST, user=DB_USER, db=DB_NAME, password=DB_PASSWORD)
    cur = con.cursor()
    return con, cur


class ChannelManager:
    @staticmethod
    def send_last_picture():
        pass

    @staticmethod
    def clean():
        query = 'delete from clean_test'
        con, cur = create_sync_con()
        cur.execute(query=query)
        con.commit()
        con.close
