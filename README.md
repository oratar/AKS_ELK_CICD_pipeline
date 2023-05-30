# AKS ELK CICD pipeline

This project demonstrates a CI/CD pipeline using Jenkins, Terraform, Docker, AKS (Azure Kubernetes Service), Elasticsearch, Filebeat, and Kibana. The pipeline enables automatic deployment of a Python Flask application with CRUD functionality to an AKS cluster. Additionally, it sets up log forwarding to an ELK stack for centralized log analysis. The project is designed to work in a multi-cloud environment, supporting both AWS and Azure.
## Prerequisites

    Azure CLI installed and configured 
    AWS CLI installed and configured
    Terraform cli installed
    MongoDB 

## SETUP
### Clone the git repository:
   ```
   git clone https://github.com/oratar/AKS_ELK_cicd_pipeline
   ```
### Create the AKS cluster using terraform:
Run the following commands in the 'terraform/aks' directory: 
```
   terraform init 
   terraform apply 
```
### Configure Jenkins:
    Create an EC2 instance for your Jenkins master using Terraform. 
    Navigate to the terraform/EC2 directory and run the following command:
   ```
   terraform init 
   terraform apply -var-file=Jenkins.tfvars 
   ```
    Access your Jenkins master's UI through the web: http://<Jenkins_IP>:8080
    Configure the project settings in Jenkins, including the Git repository, webhook, DockerHub credentials, etc.
   
### Configure dynamic Jenkins agent:
   In the Jenkins UI, install the Kubernetes plugin and configure Jenkins to use a Kubernetes dynamic agent: Navigate to "Manage Nodes and Clouds" -> "Configure Clouds" -> "Add a new cloud" -> "Kubernetes".
   Refer to the official Jenkins guide for detailed instructions on configuring Kubernetes: Jenkins Kubernetes Plugin.
   
### Configure ELK stack:
   To set up the ELK stack, use Terraform to create the ELK stack instance. In the terraform/EC2 directory, run the following commands:  
   ```
   terraform init 
   terraform apply -var-file=ELK.tfvars
   ```
   Access the Kibana UI at http://<ELK_IP>:5601 to interact with the ELK stack.   
   
### Configure filebeat deamonset:
   To enable filebeat daemonset for delivering application logs to Elasticsearch,
   run the following command from your AKS cluster:
   ```
   kubectl apply -f manifests/filebeat-kubernetes.yaml
   ```
   ![Screenshot from 2023-05-30 08-17-40](https://github.com/oratar/AKS_ELK_CICD_pipeline/assets/121873526/743e103a-5f60-4ae6-a5eb-13c66c0c3889)

