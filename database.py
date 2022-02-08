# 다음 조건을 만족하는 python 프로그램을 작성하시오.
# 조건)
# 1. addressbook.txt 파일에 다음과 같은 데이터가 들어 있다.
# 홍길동,hong@naver.com,010-1111-1111,서울시 강남구
# 고길동,go@naver.com,010-1111-1112,서울시 서초구
# 박길동,park@naver.com,010-1111-1113,경기도 수원시
# 2. addressbook.txt의 한 줄 데이터를 표현하는 Namecard 클래스를 모듈로 정의한다.
# class Namecard:
#     pass
# 3. addressbook.txt 파일을 읽어 Namecard의 리스트를 book 변수로 참조한다. 
# 4. book 리스트 변수를 순회하여 화면에 출력한다.
# 5. book 리스트를 sqlite 데이터베이스 파일로 저장한다. 파일명은 addr.db로 한다.

import sqlite3
import sys

try:

    con = sqlite3.connect('addr.db')
    print('데이터베이스 연결 성공')
    cursor = con.cursor()
    cursor.execute('DROP TABLE IF EXISTS NameCard')
    cursor.execute("""
    CREATE TABLE NameCard(
    name CHAR(16) PRIMARY KEY, email CHAR(16), phone CHAR(16),
    address TEXT )
    """)

except Exception as e:
    print('데이터베이스 연결 실패')
    print(e)
    sys.exit(0)