from pexpect import pxssh

# Here is the hyperlink to install pexpect into your local Linux Python

# https://pexpect.readthedocs.io/en/stable/install.html

#

# sudo pip install pexpect --upgrade

#  You may get an error     ImportError: cannot import name main

#  Try to use the line below, it got some wierd errors but it worked for me

#

# sudo easy_install pexpect

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# PUT YOUR IPADDRESSES INTO THIS FILE:      serversIPAddress.txt


# EDIT THESE FIELDS WITH YOUR CREDENTIALS

username = ""
password = "


# EDIT THIS WITH THE COMMANDS YOU NEED TO RUN ON THE SERVER IN SEQUENTIAL ORDER.

# THIS SCRIPT WILL exit THIS FIRST dzdo -i  AND LOGOUT AFTER ALL OF THE commands   ARE INVOKED

#commands = ["dzdo -i su cliqruser","ls -ld /shared/output"]

#commands = ["dzdo -i su cliqruser","cat /etc/cleanup/cleanup.sh"]

#commands = ["cat /etc/motd | grep CliqrDepEnvName","cat /etc/motd | grep cliqrAppName","cat /etc/motd | grep version"]

#commands = ["cat /etc/motd"]

#commands = ["cat /etc/motd | grep CliqrDepEnvName","cat /etc/motd | grep cliqrAppName","cat /etc/motd | grep version"]

commands = ["dzdo -i", "/opt/dtv/tigase-server/scripts/tigase.sh restart  /opt/dtv/tigase-server/etc/tigase.conf"]

# cliqrNodeId

# cliqrNodeHostname

 

 

 

 

# ALL ERRORS ARE APPENDED TO LOG FILE:    error_log.txt

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# - -               D O   N O T   E D I T                       - -

# - -                                                           - -

errors_file = open("error_log.txt","a")

my_ip_address_file = open("serversIPAddresses.txt", "r")


for ipaddress in my_ip_address_file:

  s = pxssh.pxssh(encoding='utf-8')

  try:  

    if not s.login (ipaddress, username, password ):

        print("SSH session failed on login.")

        print(str(s))

        errors_file.write("Failed to login " + ipaddress)

    else:

        print("SSH session login successful")

        for cmd in commands:

          s.sendline (cmd)

          s.prompt()         # match the prompt

          print(s.before)     # print everything before the prompt.  

        s.sendline("exit")

        s.logout()

    print(ipaddress)

  except Exception as e:

    errors_file.write("Exception " + ipaddress + " " + str(e) ) 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
