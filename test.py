from getpass import getpass
from unittest import result
from mysql.connector import connect, Error
import webbrowser


try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="TESTPY"
    ) as connection:
        sum_of_sales = """
            select sum(sales) from testpy.orders
         """
        customer_report = """
            
            select * from orders where `Customer Name`='Ted Butterfield' and `Order Date`='17-06-2016';   
            """

        with connection.cursor() as cursor:
            cursor.execute(customer_report)
            # cursor.execute(sum_of_sales)
            # cursor.execute(customer_report)
            result = cursor.fetchall()
            p = []
            tbl = "<tr><td>ID</td><td>Row ID</td><td>Order Id</td><td>Order Date</td><td>Ship Date</td><td>Ship Mode</td><td>Customer Id</td><td>Customer Name</td><td>Segment</td><td>Country</td><td>City</td><td>State</td><td>Postal Code</td><td>Region</td><td>Product ID</td><td>Category</td><td>Sub-Category</td><td>Product Name</td><td>Sales</td><td>Quantity</td><td>Discount</td><td>Profit</td></tr>"
            p.append(tbl)
            for row in result:
                a = "<tr><td>%s</td>" % row[0]
                p.append(a)
                b = "<td>%s</td>" % row[1]
                p.append(b)
                c = "<td>%s</td>" % row[2]
                p.append(c)
                d = "<td>%s</td>" % row[3]
                p.append(d)
                e = "<td>%s</td>" % row[4]
                p.append(e)
                f = "<td>%s</td>" % row[5]
                p.append(f)
                g = "<td>%s</td>" % row[6]
                p.append(g)
                h = "<td>%s</td>" % row[7]
                p.append(h)
                i = "<td>%s</td>" % row[8]
                p.append(i)
                j = "<td>%s</td>" % row[9]
                p.append(j)
                k = "<td>%s</td>" % row[10]
                p.append(k)
                l = "<td>%s</td>" % row[11]
                p.append(l)
                m = "<td>%s</td>" % row[12]
                p.append(m)
                n = "<td>%s</td>" % row[13]
                p.append(n)
                o = "<td>%s</td>" % row[14]
                p.append(o)
                z = "<td>%s</td>" % row[15]
                p.append(z)
                q = "<td>%s</td>" % row[16]
                p.append(q)
                r = "<td>%s</td>" % row[17]
                p.append(r)
                s = "<td>%s</td>" % row[18]
                p.append(s)
                t = "<td>%s</td>" % row[19]
                p.append(t)
                u = "<td>%s</td></tr>" % row[20]
                p.append(u)

except Error as e:
    print(e)


contents = '''
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>Testing the CSV file</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
''' % (p)

filename = 'index.html'


def main(contents, filename):
    output = open(filename, "w")
    output.write(contents)
    output.close()


main(contents, filename)
webbrowser.open(filename)

if (connection.is_connected()):
    cursor.close()
    connection.close()
    print("MySQL connection is closed.")
