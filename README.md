# AKS_ELK_cicd_pipeline

This project demonstrates a CI/CD pipeline using Jenkins, Terraform, Docker, AKS (Azure Kubernetes Service), and Filebeat. The pipeline enables automatic deployment of a CRUD Python Flask application to an AKS cluster, along with log forwarding to an ELK (Elasticsearch, Logstash, and Kibana) stack for centralized log analysis.

## Prerequisites

    Azure subscription with access to create AKS clusters
    Azure CLI installed and configured
    Docker installed
    Jenkins installed 
    terraform cli installed

## Deployment Steps
### clone the git repository:
   git clone https://github.com/oratar/AKS_ELK_cicd_pipeline

### create the AKS cluster using terraform:
   cd AKS
   terraform init 
   terraform apply 

### configure Jenkins:
   

# CI/CD_project![Screenshot from 2023-05-18 17-32-12](https://github.com/oratar/mix_project_repo/assets/121873526/8c97e5e0-c98a-4513-994b-aba2dbe23c36)
