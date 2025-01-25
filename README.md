# Scalable Web-Application Deployment
This project demonstrates how to build and deploy a scalable web application on a cloud platform using Kubernetes. The application is built with Flask, containerized using Docker, and deployed on a Kubernetes cluster. The deployment includes load balancing, autoscaling, and cost optimization.   

## Features
- Containerized web application using Docker
- Deployed on DigitalOcean Kubernetes (DOKS)
- Horizontal pod autoscaling (HPA) and cluster autoscaling 
- Load balancing
- Cost optimization strategies

## Prerequisites 
- DigitalOcean account
- GitHub account
- DigitalOcean CLI (doctl)
- Kubernetes CLI (kubectl)
- Docker

## Setup Instructions  

1) Authenticate DigitalOcean CLI
   
```
doct auth init 
```

3) Create Flask application
   - Create app.py file 

   ```
   from flask import Flask
   import os
   import socket

   app = Flask(__name__)

   @app.route("/")
   def hello():
       html = """Hello {name}!
       Hostname: {hostname}"""
       return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

   if __name__ == "__main__":
       app.run(host='0.0.0.0', port=80)
    ```

   - Create a requirements.txt file

   ```
   Flask
   ```
  
3) Containerize the application
   - Create Dockerfile

   ```
   # Use an official Python runtime as a parent image
   FROM python

   # Set the working directory to /app
   WORKDIR /app

   # Copy the current directory contents into the container at /app
   ADD . /app   

   # Install any needed packages specified in requirements.txt
   RUN pip install -r requirements.txt

   # Make port 80 available to the world outside this container
   EXPOSE 80

   # Define environment variable
   ENV NAME World

   # Run app.py when the container launches
   CMD ["python", "app.py"]
   ```

   - Build and test locally

   ```
   docker build -t my-python-app .
   docker run -p 80:80 my-python-app  
   ```
   
3) Deploy to container registry on cloud platform
   - Create registry

   ```
   doctl registry create <your-registry-name>
   ```
   
   - Login to registry

   ```
   doctl registry login
   ```

   - Tag and push image

   ```
   docker tag my-python-app registry.digitalocean.com/<your-registry-name>/my-python-app
   docker push registry.digitalocean.com/<your-registry-name>/my-python-app 
   ```
   
5) Create Kubernetes cluster

   ```
   doctl kubernetes cluster create <your-cluster-name> --tag do-tutorial --auto-upgrade=true --node-pool "name=mypool;count=2;auto-scale=true;min-nodes=1;max-   nodes=3;tag=do-tutorial" 
   ```
   
7) Deploy application to Kubernetes 
   - Authorize registry

  ```
  doctl registry kubernetes-manifest | kubectl apply -f –
  ```

   - Deploy Application

   ```
   kubectl create deployment my-python-app --image=registry.digitalocean.com/<your-registry-name>/my-python-app 
   ```

   - Expose with load balancer

   ```
   kubectl expose deployment my-python-app --type=LoadBalancer --port 80 --target-port 80
   ```

8) Enable autoscaling
   - Setup horizontal pod autoscaling (HPA) based on CPU usage
   - Setup cluster autoscaling 
9) Monitor and scale the application
   - Check the status of your cluster and pods

   ```
   kubectl get nodes
   kubectl get pods
   kubectl get hpa
   ```
   
   - Scale the application
  
   ```
   kubectl scale deployment/my-python-app --replicas=20
   ```
   
10) Cost optimization
   - Autoscaling with HPA and cluster techniques    
   - Load balancing
   - Spot instances
   - Right size nodes based on resource utilization metrics

## Conclusion 
This project demonstrates how to deploy a scalable, containerized web-application on a cloud platform using Kubernetes. By following these steps, you can create a robust and efficient deployment with optimized costs and performance. 
