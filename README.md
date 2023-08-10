# unsplash-clip-classification
Classifying images by the time of day using the Unsplash dataset. To classify images, I use the CLIP model without fine-tuning, and as a zero-shot classifier. This is a hands-on project to start with MLOps and CI/CI pipelines for machine learning projects.

### Techniques

- DVC
- GitHub actions
- Docker
- Flask
- AWS ECR, EC2

# How to run?
### STEPS:

Clone the repository

```
$ git clone https://github.com/shakibyzn/unsplash-clip-classification.git
```
### STEP 01- Create a virtual environment

```
$ python -m venv your_venv
```

```
$ source your_venv/bin/activate
```


### STEP 02- install the requirements
```
$ pip install -r requirements.txt
```


Finally run the following command

```
$ python app.py
```

Now,
```
open up your browser, and go to localhost:8080
```





# AWS-CICD-Deployment-with-Github-Actions (optional)

You can follow [this](https://www.youtube.com/watch?v=p1bfK8ZJgkE&t=12662s) youtube video from @krishnaik06 for this part of the project.
## 1. Login to AWS console.

## 2. Create IAM user for deployment

	# with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	# Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	# Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess


## 3. Create ECR repo to store/save docker image
    - Save the URI: your_prefix.dkr.your_region.amazonaws.com/your_repository


## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:


	# optinal

	sudo apt-get update -y

	sudo apt-get upgrade

	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker

# 6. Configure EC2 as self-hosted runner:
    setting> actions> runner> new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID =

    AWS_SECRET_ACCESS_KEY =

    AWS_REGION =

    AWS_ECR_LOGIN_URI =

    ECR_REPOSITORY_NAME =


