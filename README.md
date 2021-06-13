# Big-Motoring-World

## Contents

* [Introduction ](#introduction)
    * [Objective](#objective)
    * [My Project Proposal ](#my-project-proposal)
* [Software architecture](#software-architecture)
    * [Project Tracking](#project-tracking)
    * [Risk Assessment](#risk-assessment)
    * [Entity Relationship Diagram](#entity-relationship-diagram)
    * [CI Pipeline](#ci-pipeline) 
* [Software Infrastructure](#software-infrastructure)
   * [Jenkins](#jenkins)
   * [Swarm Configuration](#swarm-configuration)
   * [Services Setup](#Services-Setup)
* [Testing](#testing)
* [Future Improvements](#future-improvements)
* [Author](#author)

## Introduction
### Objective
This is an individual project in order to meet the SFIA requirements. The objective of this project is to create a web application based on the micro service architecture. This allows the developer to split up the application into more manageable amounts.

The brief set for this project is to create a service orientated object which will either be used or displayed by other services. Service 1 will be used as the main service i.e. the front-end which the user will see. Service 1 will include all the relevant HTML files needed for the web application. Service one will then communicate with the other services. Service 2 and 3 will generate a random object that will be sent to service 1. Furthermore the last service, service 4 will generate an object based on the response from services 2 and 3.

In order to achieve the brief, the following requirements must be followed:

*	Trello board
*	Rational database:  with one table.
*	Version control: GitHub
*	CI server : Jenkins
*	Configuration Management: Ansible
*	Cloud Server: GCP Virtual Machines
*	Containerisation: Docker
*	Orchestration Tool: Docker Swarm
*	Reverse Proxy: NGINX

### My Project Proposal
To achieve these requirements, the idea that I decided to produce is to create a web application called Big-Motoring- World. This application consists of 4 services. The user will firstly, connect to service 1 which will display the webpage. However, before displaying the page a get request is made to services 2 and 3. Service 2 is responsible for generating a random car and service 3 will then generate a random colour. Then a post request is made to service 4, sending the car make and colour information obtained from the previous get request. Service 4 we will then generate a price based on that information.

## Software Architecture 
### Project tracking
Trello board, along with agile methodologies was used to track the progression of the project. Trello board is a lightweight tool to help organise the workflow from start to finish. I have set it up such that there are several lists each containing cards related to that list.
The list which was created are as follows:

•	Project resources - Containing relevant links.
•	User stories - Each card has the format “As a [User]…., I want…. [Feature], so that…. [Details]”
•	Backlog - Tasks which need to be done.
•	In progress - Tasks which are currently being worked on.
•	Complete - Tasks that are finished.
•	Issues - Any problems along the way.

![trello board image 1]()
![trello board image 2](https://github.com/Fardins24/assetsNew/blob/master/tb2.png?raw=true)

### Risk Assessment
Below is the risk assessment for the project split up into two sections before and after. The before section highlights the potential risk that I knew at the beginning of the project. The after section highlights the potential risks I knew by the end of the project. These risks were dealt with accordingly.

<h2>Before</h2>

![risk-assessment1]()

<h2>After</h2>

![risk-assessment2]()

### Entity Relationship Diagram
For the development of this project, only one table structure was created for the database. The reason for this is that the only information that will be stored into the database will be the ID, car manufacturer, car colour and price. Therefore, there are no other relationships in the application. This table will help the developer create data that will persevere in the database after each refresh. The database is set up on a MYSQL server on Google Cloud Platform (GCP). 
![Car-erd]()

### CI Pipeline
The image below portrays the CI Pipeline used for this project. Firstly, to achieve the project goal, a task is taken from the Trello board to be worked on. After, completing a task the code is the pushed up to a Version Control System. For this project, GitHub was commenced as the chosen version control system, which then triggers a web-hook. By initiating a web-hook, this then starts a Jenkins pipeline. Further tests are completed by implementing a unit test and mock test. After the testing was completed the next step is now building and pushing images using Docker-Compose to Docker hub (artefact repository). Jenkins will then initialise Ansible to configure the external nodes; this involves installing Docker on them. Ansible also configures NGINX node to act as a Load-Balancer. The user connects to the load balancer and application is now live.

![CI-Pipeline]()

## Software Infrastructure
### Jenkins 
Jenkins is an open source automation server that automates many parts of the project including testing and deployment. This helps facilitate continuous integration and deployment. For this for this project, the stages of the Jenkins pipeline are as follows:

* Testing – This produces coverage report on the console. The reports generated can be used to help debug issues that occur.
* Build and Push Images – The second stage, is building the image and pushing up the image to Docker hub. For this to proceed, Docker and Docker-Compose needs to be installed.
* Ansible configuration – The third stage in this Pipeline is when Jenkins is running the Ansible folder. This initialises Ansible to configure several servers at once including:– 
* * Installing the necessary dependencies
* * Installing Swarm, to initialise Swarm Manager and Swarm Worker nodes 
* * Configuring the NGINX Load-Balancer.
* Deploy Stack – The application will be deployed as a stack across the Swarm nodes, making it accessible by the users via the NIGNX Load-Balancer.

Details on the stages used in the Jenkins pipeline can be found in the jenkinsfile. 

### Swarm Configuration
The image below portrays the basic setup of the Swarm. After Ansible installs Docker on both Swarm-Manager and Swarm-worker nodes, it then initialises the Swarm on the manager node and joins the worker nodes.
![swarm]()

### Services Setup
As written above, the project task must include four services as part of the project proposal. Service 1 will be the Frontend and will display the information generated from services 2,3 and 4. Service 2 and 3 which is the Backend generates a car make (service 2) and a car colour (service 3) when a get to request is sent from service 1.  Service 4 is automated, when service 2 and 3 are sent to service 1 via a get request, which will then be sent to service 4 via a post request. Here, service 4 will generate a price based on the information it receives and then sends it to service 1.
![services]()

## Testing
For this project, I have decided to implement Pytest to run unit and unit mock test on the application. Unit test allows the developer to validate each function on the application to an expected response. Unit mock test allows the developer to mock responses from components in each service allowing easier and more efficient unit testing than would otherwise be possible.

<h3>Service #1</h3>
Testing service 1 requires input from the other three services. Patch is imported from the Python library and is implemented for this test. In return a mock test was conducted which will produce results that will be expected from the live application.

![service1-test]()

<h3>Service #2</h3>
For this service the unit test produced 100% coverage. Therefore, this connotes that each individual car that will be selected at random through a get request will have the required response.

![service2-test]()

<h3>Service #3</h3>
Also for this service the unit test was conducted with 100% coverage. This shows that from individual car colour that was picked at random, it will generate the required response.

![service3-test]()

<h3>Service #4</h3>
Service for also shows 100% console output which indicates that service 2 and service 3 generates the correct price for each car and colour.

![service4-test]()

## Future Improvements 
In any project there are always a few improvements which could be considered in the future. However, to name a few:

* One way for the application to be more robust is to produce more testing such as integration testing to test the app as a whole. By implementing the selenium approach would be ideal.
* Reduce downtime by using Nexus as opposed to Docker hub.
* Add functionality that allows the user to input data.
* Add images to the cars so the application is more appealing to the end user.

However in general, as a whole this project was successful in creating a service orientated application.

## Author
Fardin Shah 







