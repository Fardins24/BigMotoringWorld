#!bin/bash

# install requirements/create venv
sudo apt-get update 
sudo apt-get install python3-venv python3-pip -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r test_requirements.txt

# pytest coverage service_1
cd service_1
python3 -m pytest --cov=app
cd .. 

# pytest coverage service_2
cd service_2
python3 -m pytest --cov=app
cd .. 

# pytest coverage service_3
cd service_3
python3 -m pytest --cov=app
cd .. 

# pytest coverage service_4
cd service_4
python3 -m pytest --cov=app
cd .. 
