#!/usr/bin/python

import os, re, commands, string
path = os.getcwd()

for file in os.listdir(path):
   result = re.match('.*\.py$', file)
   if result != None: #found a .py file
      #print result.group(0)
      commands.getoutput('code2html -n %s html/%s.html -o html-dark' \
               % (result.group(0), result.group(0).replace(".", "")))
print "done converting to html"
commands.getoutput('scp -r html/ 477grp4@shay.ecn.purdue.edu:/web/entities/477grp4/Matt/src/')
print "done uploading"
