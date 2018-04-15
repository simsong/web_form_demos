#!/usr/bin/python3

import cgi

FORM="""
<form action='form1.cgi'>
  Number of apples: <input type="text" name="apples" size='6'/><br>
  Number of oranges: <input type="text" name="oranges" size='6'/><br>
  <input type="submit" value="Calc">
</form>
"""

if __name__=="__main__":
   print("Content-type: text/html\r\n\r\n<html><body>")
   print(FORM)

   form = cgi.FieldStorage()
   if "apples" in form:
      apples = int( form['apples'].value )
      oranges = int( form['oranges'].value )
      fruit   = apples+oranges
      print("<p>{} apples + {} oranges = {} fruit<p>".format(apples, oranges, fruit))

   print("<hr><p>Here is the contents of this script:</p>")
   print("<hr>")
   print("<pre>")
   print( cgi.escape(open(__file__,"r").read()) )
   print("</pre>")
   print("</body></html>")
        
