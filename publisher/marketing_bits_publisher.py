##############################################################################
#This program publishes the marketing bits template as a ready to go html file.
#It works by accepting the articles as input (with html tags included) and
#mocking everything up by filling in the blanks.
#Its pretty basic and will get a lot of features added as I refine it.
#For the time being, it aims to save me the hassle of mocking up the
#templates manually. In the future, I will have it do it automatically
#from a given directory. So that I can just write articles and have
#the program publish them iteself automatically.
############################################################################



###################################
#importing the template markup from separate files to make this more readable. 
###################################


from template import *


##
# Constants
##

HR = '<hr>'
TOP = top_of_template()
BOTTOM = bottom_of_template()

###


#gets the name of the issue. File name will be name with this. Include .html at end of file. 
issue_name = str(raw_input("Write the filename to be saved under. Include .html at the end.\n>>>"))





#first article from top to bottom
first_article = str(raw_input("Paste the first article with title.\n>>>"))

print "\n\n"

second_article = str(raw_input("Paste the second article with title.\n>>>"))

print "\n\n"

third_article = str(raw_input("Paste the third article with title.\n>>>"))

print "\n\n"

interesting_bit = str(raw_input("Paste the interesting bit.\n>>>"))

#need to fix the html template to include this. Not now. Too lazy to do it.
#tagline = str(raw_input("Paste the tagline.\n>>>")) 


with open(issue_name, 'w') as issue:
    issue.write(TOP)
    issue.write(first_article)
    issue.write(HR)
    issue.write(second_article)
    issue.write(HR)
    issue.write(third_article)
    issue.write(HR)
    issue.write(interesting_bit)
    issue.write(BOTTOM)
    issue.close()

print "its ready, baby!"

