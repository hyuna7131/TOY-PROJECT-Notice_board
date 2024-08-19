'''import pymysql

def get_connection():
    connection = pymysql.connect(
        host='db',  # Docker Compose에서 설정할 데이터베이스 서비스 이름
        user='root',
        password='password',
        db='board',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
    '''
import pymysql
from pymysql import OperationalError

def get_connection():
    try:
        connection = pymysql.connect(
            host='db',                # Docker Compose에서 설정할 데이터베이스 서비스 이름
            user='root',
            password='password',
            db='board',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            port=3306                  # MySQL 기본 포트 설정 (기본값)
        )
        return connection
    except OperationalError as e:
        print(f"Error: Unable to connect to the database. {e}")
        # 여기서 예외를 던지거나, 적절한 오류 처리를 추가할 수 있습니다.
        raise
