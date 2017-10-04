#!/usr/bin/python

import getpass
import telnetlib
import cgi, cgitb 

form = cgi.FieldStorage() 


#HOST = raw_input("Enter Device IP Add: ")
#user = raw_input("Enter your remote account: ")
#password = getpass.getpass()

IP = form.getvalue('IP')
USERNAME = form.getvalue('USERNAME')
PASSWORD = form.getvalue('PASSWORD')
ENABLEPASS = form.getvalue('ENABLEPASS')
COMMAND = form.getvalue('COMMAND')

tn = telnetlib.Telnet(IP)

tn.read_until(b"Username: ")
tn.write(USERNAME.encode('ascii') + b"\n")
if PASSWORD:
    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode('ascii') + b"\n")

tn.write(b"enable\n")
if ENABLEPASS:
    tn.read_until(b"Password: ")
    tn.write(ENABLEPASS.encode('ascii') + b"\n")

tn.write(COMMAND.encode('ascii') + b"\n")

#tn.write(b"sh ip int brie\n")
#tn.read_until(b"#")
tn.write(b"exit\n")

#print(tn.read_all().decode('ascii'))

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello MAlaa - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h1> MAlaa Cisco-Telnet program has been completed successfully... </h1>"
# Required header that tells the browser how to render the text.
print "<h2> MAlaa Cisco-Telnet program %s</h2>" % (tn.read_all().decode('ascii'))
#working - print "<h2> sh ip int bri : %s</h2>" % (tn.read_all().decode('ascii'))
#print "<h1>Welcome to the wonderful MAlaa's world %s %s</h1>" % (first_name, last_name)
print "</body>"
print "</html>"