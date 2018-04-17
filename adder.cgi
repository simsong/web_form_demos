#!/usr/bin/python3

import cgi
import json

if __name__=="__main__":
   form = cgi.FieldStorage()
   try:
      apples = int( form['apples'].value )
   except KeyError:
      apples = 0
   try:
      oranges = int( form['oranges'].value )
   except KeyError:
      oranges = 0
   
   print("Content-type: text/text\r\n\r\n")
   ret = { "apples":apples,
           "oranges": oranges,
           "fruit": apples + oranges
   }
   print(json.dumps(ret))
