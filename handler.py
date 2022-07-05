import pymysql

# Configure Values
endpoint = '<Your RDS DB Endpoint>'
username = '<Your RDS DB Username>'
password = '<Your RDS DB Password>'
database_name = '<Your RDS DB Name>'

# Connection
connection = pymysql.connect(host=endpoint, user=username,
                             passwd=password, db=database_name)

def lambda_handler(event, context):
    cursor = connection.cursor()

    cursor.execute('''SELECT 
                          *
                      FROM 
                          Potential_Buyers''')
    rows = cursor.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2], row[3]))


