# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form .getvalue('gender'):
    gender = form .getvalue('gender')
else:
    gender = "Not set"
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<body>")
print ("<h2> Selected Gender is %s</h2>" % gender)
print ("</body>")
print ("</html>")