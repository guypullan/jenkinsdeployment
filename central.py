#!python

import sys, getopt
import createcomponent
import createstack
import configurecomponent

def main (argv):
    # scan input options from commandline and assign to variables
    cloudstackconfigfile = ''
    variablelistingfile = ''
    purpose = ''
    certkey = ''
    certificate = ''
    wrapperfile = ''
    try:
        opts, args = getopt.getopt(argv,"hc:v:p:k:s:w:",["cloudstackconfig=","variablelistingfile=","purpose=","certificate=","certkey=","wrapper="])
    except getopt.GetoptError:
        print 'test.py -c <cloudstackconfig> -v <variablelisting>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print "This command is used to create a cloudstack as follows central.py -c cloudstackconfig -v variablelisting -p function to perform -s certificate -k certificatekey -w wrapperfile"
            sys.exit()
        elif opt in ("-c", "--cloudstackconfig"):
            cloudstackconfigfile = arg
        elif opt in ("-v", "--variablelisting"):
            variablelistingfile = arg
        elif opt in ("-p", "--purpose"):
            purpose = arg
        elif opt in ("-k", "--certkey"):
            certkey = arg
        elif opt in ("-s", "--certificate"):
            certificate = arg
        elif opt in ("-w", "--wrapperfile"):
            wrapperfile = arg

    purposefunction (wrapperfile, cloudstackconfigfile, variablelistingfile, certificate, certkey, purpose)

def purposefunction (wrapperfile, cloudstackconfigfile, variablelisting, certificate, certkey, purpose):
 #based on input decide which function to perform
    if purpose == 'createcomponent':
        createcomponent.componentcreation (wrapperfile, variablelisting, certificate, certkey)
    if purpose == 'createstack':
        createstack.stackcreation (wrapperfile, cloudstackconfigfile, variablelisting, certificate, certkey)
    if purpose == 'configurecomponent':
        configurecomponent.componentconfiguration (wrapperfile, variablelisting, certificate, certkey)

if __name__ == "__main__":
    main (sys.argv[1:])
