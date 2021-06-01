import pymysql

db = None
try:
    # DB 호스트 정보에 맞게 입력해주세요.
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='1234',
        db='homestead',
        charset='utf8'
    )
    print("DB 연결 성공")

    # 데이터 삽입 sql 정의
    sql = '''
        INSERT tb_student(name, age, address) values('Lee', '35', 'Korea')
    '''

    # 데이터 삽입
    with db.cursor() as cursor:
	    cursor.execute(sql)
    db.commit()

except Exception as e:
	print(e)

finally:
	if db is not None:
		db.close()