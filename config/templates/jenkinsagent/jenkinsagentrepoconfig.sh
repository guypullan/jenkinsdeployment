curl -E ../../dev.bbc.co.uk.p12:certificatepassword https://api.live.bbc.co.uk/cosmos/component/componentname/repositories -H 'Content-Type: application/json' -X PUT --data-binary @- <<BODY
{
    "apache-maven": {
        "type": "mirrorlist",
        "url": "https://repository.api.bbci.co.uk/apache-maven/revisions/head"
    },
    "awslogs": {
        "type": "mirrorlist",
        "url": "https://repository.api.bbci.co.uk/awslogs-el6/revisions/head"
    },
    "cosmos": {
        "type": "mirrorlist",
        "url": "https://repository.api.bbci.co.uk/cosmos/revisions/head",
        "gpg_key": $(cat $(git rev-parse --show-toplevel)/cloudteam-key.gpg | python -c "import json, sys; print (json.dumps(sys.stdin.read()))")
    },
    "epel": {
        "url": "https://mirrors.fedoraproject.org/metalink?repo=epel-6&arch=x86_64",
        "type": "mirrorlist",
        "gpg_key": $(curl https://fedoraproject.org/static/0608B895.txt | python -c "import json, sys; print(json.dumps(sys.stdin.read()))")
    },
    "otg-build-tools": {
        "type": "mirrorlist",
        "url": "https://repository.api.bbci.co.uk/otg-build-tools/revisions/stable",
        "gpg_key": $(cat $(git rev-parse --show-toplevel)/cloudteam-key.gpg | python -c "import json, sys; print(json.dumps(sys.stdin.read()))")
    }
}
BODY
