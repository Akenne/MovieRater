'''
Adam's first useful script
'''

from os import listdir
from os.path import isfile, join
import shutil
import winshell

mypath = "F:\\Movies\\NOTSEEN\\"   #where it reads movies you haven't rated yet
shortcut = "F:\\Movies\\Movies\\"  #where your shortcuts go
rated = "F:\\Movies\\"             #where your rated movies go, should have sub directories labeled 1/2/3...
files = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ] #list of all unrated movies

while 1:
  for i in range(len(files)):
    print (str(i+1) + '. ' + files[i])     # prints list of all movies in unrated
  print ()
  print ("Please enter the number corresponding with the movie you want to rate")
  mov = int(input('-->'))
  print ()
  print ("Please enter a rating from 1 to 10 for the movie " + files[mov-1])  #these are user inputs
  rate = int(input('-->'))
  print ()
  print ("Confirm a " + str(rate) + "/10 rating for " + files[mov-1] + "? Y/N")
  yesno = input('-->').lower()
  yesno = yesno.lower()
  if yesno != 'y':
    print ("\n" * 100)
    continue     
  choice = (mypath + files[mov-1])
  shutil.move(choice, (rated + str(rate)))
  print ()
  print ("Want a shortcut? Y/N")
  yesno = input('-->').lower()    #checks if they want a shortcut, if so it uses winshell to make one
  if yesno == 'y':
    winshell.CreateShortcut (
      Path=os.path.join (shortcut, (files[mov-1] + '.lnk')),
      Target=(mypath + files[mov-1])
      )
  print ()
  print ('Is that all then? Y/N') #loops if more rating needs done
  yesno = input('-->').lower()
  if yesno == 'n':
    files.pop(mov-1)
    print ("\n" * 100)
    continue
  else:
    break