# Horizontal & Vertical Pod Autoscaling in Kubernetes

Implementation of Horizontal & Vertical Pod Autoscaler in Kubernetes.
In this example, a Flask backend is dockerized and deployed in a Kubernetes Cluster on Google Cloud. Upon request, an expensive calculation is started and Flask returns the calculated result. The autoscaling will be started via an overload of requests. The service will be stressed with requests sent from a Locust application, which in turn triggers the horizontal or vertical scaling. 

*insert project overview here*

## Prerequisites
Create a Kubernetes Cluster on Google Cloud.

## Create Deployment

`kubectl apply -f deployment.yaml`

## Create Horizontal Pod Autoscaler

`kubectl create -f hpa.yaml`

`kubectl get hpa`

## Create Vertical Pod Autoscaler

`kubectl create -f vpa.yaml`

`kubectl get vpa`

## Create Service with Load Balancer

`kubectl expose deployment flaskcalc --type LoadBalancer --port 8080 --target-port 5000`

`kubectl get services`
