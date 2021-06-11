#!/bin/bash

# copy over compose yaml to manager node
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@manager:/home/jenkins/docker-compose.yaml

# docker stack deploy
ssh -i ~/.ssh/ansible_id_rsa jenkins@manager << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file docker-compose.yaml bigmotoringworld
EOF
