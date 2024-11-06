#!/usr/bin/python3
#### Abdulbari Ahmed
#### Automating User Management
#### Program Creation Date: 11/05/2024
#### Program Last Updated Date: 11/06/2024

#Import modules for system commands, regular expressions, and standard input
import os
import re
import sys

def main():
    for line in sys.stdin:

        #Loop through each line provided as input to the script
        match = re.match("^#",line)

        print(match)
	#Split the line into fields using ':' as the delimiter, removing any extra whitespace
        fields = line.strip().split(':')

        #Skip processing if the line is a comment or does not have exactly 5 fields
        if match or len(fields) != 5:
            continue

	#Assign values from fields to variables for user details
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])
	    
	#Split the group field by ',' to allow multiple groups per user
        groups = fields[4].split(',')
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        #print cmd
        os.system(cmd)
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #print cmd
        os.system(cmd)
	
	#Loop through each group in the list for the user
        for group in groups:
            #If the group is not '-', assign the user to this group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()
