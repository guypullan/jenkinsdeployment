# jenkinsdeployment

creation of jenkins agent component
python central.py -s ../../dev.bbc.co.uk.cert -k ../../dev.bbc.co.uk.key -w config/templates/cosmos/componentcreation -v config/stack_location/ac_32802642264_eu-west-1/jenkinsagentvariablelisting.json -p createcomponent


creation of jenkins agent
python central.py -s ../../dev.bbc.co.uk.cert -k ../../dev.bbc.co.uk.key -w config/templates/jenkinsagent/jenkinsagentwrapper -v config/stack_location/ac_32802642264_eu-west-1/jenkinsagentvariablelisting.json -c config/templates/jenkinsagent/infrastructure.json -p createstack

configure jenkins agent component
python central.py -s ../../dev.bbc.co.uk.cert -k ../../dev.bbc.co.uk.key -w config/templates/cosmos/componentconfiguration -v config/stack_location/ac_32802642264_eu-west-1/jenkinsagentvariablelisting.json -p configurecomponent