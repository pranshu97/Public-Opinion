# before using the import modules clean the function calls in each if the module( remove extractfn() from the end of file used for testing)
import extraction
import Analysis
import ppt
import Email
from sys import argv

#extraction.extractfn(str(argv[1]),str(argv[2]))
Analysis.cleanNanalyse(str(argv[1]))
ppt.ppt()
Email.sendemail()

