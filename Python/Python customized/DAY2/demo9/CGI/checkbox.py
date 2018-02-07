# Im port m odules for CGI handling
import cgi, cgitb
# Create instance of FieldStorage

form = cgi.FieldStorage()
# Get data from fields

if form .getvalue('english'):
    english_flag = "ON"
else:
    english_flag = "OFF"
if form .getvalue('hindi'):
    hindi_flag = "ON"
else:
    hindi_flag = "OFF"
print ("Content-type:text/htm l\r\n\r\n")
print ("<html>")
print ("<body>")
print ("<h2> CheckBox English is : %s</h2>" % english_flag)
print ("<h2> CheckBox Hindi is : %s</h2>" % hindi_flag)