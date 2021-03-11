# EC2 deployment pipeline

A process for deploying the th3-server.py script using CI/ID philosophy.  
The primary orchestrator in this example is Ansible leveraging AWS as a platform.

## Ansible prerequisites

Ansible server running version 2.9.*  
Ansible Vault credentials of AWS access credentials  
Boto3

## AWS prerequisites
AWS account  
AWS access credentials  
S3 bucket to hold latest version of th3-server.py  
Application Elastic Load Balancer(ELB)  

## Instructions for setting up AWS prerequisites
[AWS Services](https://docs.aws.amazon.com/index.html?nc2=h_ql_doc_do)  
[AWS Access Credentials](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-your-credentials.html)

## Instructions for setting Ansible prerequisites
[Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)  
[Ansible Vault credentials](https://docs.ansible.com/ansible/latest/user_guide/vault.html)  
[Boto3](https://pypi.org/project/boto3/)

# Command to run deployment process
The 'tags' parameter will depend on whether you wish you to deploy a new build or rollback to an old build

```ansible-playbook translate-api-deployment.yml --ask-vault-pass --tags deploy/build```

# Pipeline deployment process

```
1. Grab the latest version of the script from an S3 bucket
2. Provision new EC2 servers
3. Deploy script and start script on newly provisioned EC2 servers
4. Confirm application on EC2 servers are up and running
  a. If not, restart the script and test
  b. If still failing, fail the deployment
5. Register EC2 instances to ELB target group to start receiving traffic
  a. Wait for load balancing health checks to confirm instances are healthy
  b. If instances remain unhealthy for a certain period of time, deregister, and fail deployment
6. Deregister old EC2 instances from ELB target group
```

# Pipeline rollback process

```
1. User provides a list of instances to roll back to
2. Start application on instances provided
  a. Confirm services are running and healthy
  b. If not, rollback fails
3. Register rollback instances to ELB target group
  a. Wait for load balancing health checks to confirm instances are healthy
  b. If unhealthy, deregister, and fail rollback
4. Deregister broken EC2 instances from ELB target group
```

### Notes
At the moment, the rollback would depend on a list of EC2 instance IDs that would be provided by the user.  
A more ideal solution would be to build the instances with tags specifying their application and build version.  
Then a user could simply supply the application and the build version to roll back to and Ansible will look for instances that satisfy these requirement.  

Failures induce the whole job to fail.  
A more ideal solution would be to have Ansible have a separate job for each EC2 instance instead of a clumping them as a group.  
This would allow successful builds to continue even if there are broken builds during the process.

## Authors
Francis Kim
