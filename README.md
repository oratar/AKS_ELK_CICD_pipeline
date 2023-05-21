# AKS_ELK_cicd_pipeline

This project demonstrates a CI/CD pipeline using Jenkins, Terraform, Docker, AKS (Azure Kubernetes Service), ElasticSearch and Filebeat using multi cloud environment such as AWS and Azure. The pipeline enables automatic deployment of a CRUD Python Flask application to an AKS cluster, along with log forwarding to an ELK (Elasticsearch, Logstash, and Kibana) stack for centralized log analysis.

## Prerequisites

    Azure subscription with access to create AKS clusters
    Azure CLI installed and configured
    Docker installed on all EC2 Instances 
    Terraform cli installed
    AWS account 
    MongoDB 

## SETUP
### Clone the git repository:
   git clone https://github.com/oratar/AKS_ELK_cicd_pipeline

### Create the AKS cluster using terraform:
make sure you are logged in to your Azure account:
`
   az login
`
Run the following commands in the 'aks' directory: 
```
   terraform init 
   terraform apply 
```
### Configure Jenkins:
   1. Create an EC2 instance for your Jenkins master and open port 50000 and 8080 in the instance's security group.
   2. Connect to your instance and run the following command:
   ` 
   docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11
   `
   3. Access your Jenkins master's UI through the web: http://<Jenkins_IP>:8080
   4. Configure the project settings in Jenkins, including the Git repository, webhook, DockerHub credentials, etc.
   
### Configure Jenkins agent:
   1. Create an EC2 instance for your Jenkins agent and open port 50000 to allow communication with the Jenkins master.
   2. Connect to the instance and install Java. 
   3. In the Jenkins UI, create a new Node and connect your Jenkins agent by running the agent JAR file.

### Configure ELK stack:
 Create ELK stack on EC2 instance using Docker container:
    1. Create an EC2 instance for your ELK stack and open ports 5601, 9200 and 5044.
    2. Connect to your instance and run the following command to create the ELK stack docker container:
    ```
    sudo sysctl -w vm.max_map_count=262144
    sudo docker run -p 5601:5601 -p 9200:9200 -p 5044:5044 -it --name elk sebp/elk
    ```

   
# CI/CD_project![Screenshot from 2023-05-18 17-32-12](https://github.com/oratar/mix_project_repo/assets/121873526/8c97e5e0-c98a-4513-994b-aba2dbe23c36)
