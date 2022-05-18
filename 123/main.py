from mysql.connector import connect, Error

if __name__ == '__main__':
    with connect(
        host='127.0.0.1',
        user='admin',
        password='admin',
        database='RES_PROJEKAT'
    ) as connecting:
        query = "SELECT * FROM potrosnjaBrojila pb, brojilo b where pb.IdBrojila = b.IdBrojila;"
        with connecting.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for res in result:
                print(res)


