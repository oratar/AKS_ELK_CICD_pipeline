# AKS_ELK_cicd_pipeline

This project demonstrates a CI/CD pipeline using Jenkins, Terraform, Docker, AKS (Azure Kubernetes Service), and Filebeat. The pipeline enables automatic deployment of a CRUD Python Flask application to an AKS cluster, along with log forwarding to an ELK (Elasticsearch, Logstash, and Kibana) stack for centralized log analysis.

## Prerequisites

    Azure subscription with access to create AKS clusters
    Azure CLI installed and configured
    Docker installed
    Terraform cli installed

## Deployment Steps
### Clone the git repository:
   git clone https://github.com/oratar/AKS_ELK_cicd_pipeline

### Create the AKS cluster using terraform:
   cd AKS
   terraform init 
   terraform apply 

### Configure Jenkins:
#### installing Jenkins master using Docker container:
   docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11

# CI/CD_project![Screenshot from 2023-05-18 17-32-12](https://github.com/oratar/mix_project_repo/assets/121873526/8c97e5e0-c98a-4513-994b-aba2dbe23c36)
