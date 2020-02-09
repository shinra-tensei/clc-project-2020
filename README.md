# Horizontal & Vertical Pod Autoscaling in Kubernetes

Implementation of Horizontal & Vertical Pod Autoscaler in Kubernetes.
In this example, a Flask backend is dockerized and deployed in a Kubernetes Cluster on Google Cloud. Upon request, an expensive calculation is started and Flask returns the calculated result. The service will be stressed with requests sent from a Locust application, which in turn triggers the horizontal or vertical scaling. 

![alt text](https://github.com/shinra-tensei/clc-project-2020/blob/master/project_concept.JPG)

## Prerequisites
1. Create a Kubernetes Cluster on Google Cloud
2. Install Google Cloud SDK and kubectl
3. Connect to cluster

## Create Deployment

`kubectl apply -f Kubernetes/flask-depl.yaml`

`kubectl describe deployment`

## Create Service with Load Balancer

`kubectl expose deployment flaskcalc --type LoadBalancer --port 8080 --target-port 5000`

`kubectl get services`

## Create Horizontal Pod Autoscaler

The HPA is a Kubernetes API resource and a controller that automatically scales the number of pods in a replication controller, deployment, replica set or stateful set based on defined metric(s). The resource determines the behavior of the controller. The controller periodically adjusts the number of replicas in a replication controller or deployment to match the observed average CPU utilization to the target specified by user. The default value for the control loop period is 15 seconds. During each period, the controller manager queries the resource utilization against the metrics specified in each HorizontalPodAutoscaler definition. The controller manager obtains the metrics from either the resource metrics API or the custom metrics API (for all other metrics). The current stable version, which only includes support for CPU autoscaling, can be found in the `autoscaling/v1` API version. For custom metrics, the `autoscaling/v2beta2` API version is required.

`kubectl create -f Kubernetes/flask-hpa.yaml`

`kubectl get hpa`

## Create Vertical Pod Autoscaler

The Kubernetes Vertical Pod Autoscaler automatically adjusts the CPU and memory reservations for pods to help "right size" desired applications. This adjustment can improve cluster resource utilization and free up CPU and memory for other pods. It can work for both stateful and stateless pods but it is built mainly for stateful services. VPA requires currently for the pods to be restarted to change allocated cpu and memory. When VPA restarts pods it respects pods distribution budget (PDB) to make sure there is always the minimum required number of of pods. VPA has also an interesting feature called the VPA Recommender. It watches the historic resources usage and OOM events of all pods to suggest new values of the request resources spec. Due to the limititations of VPA, a pod distribution budget should be set to limit the amount of pod restarts. To make sure that the cluster can handle the new sizes of the workloads, Cluster Autoscaler and Node Autoprovisioning should also be utilzed.

First update the cluster to support VPA:

`gcloud container clusters update [CLUSTER-NAME] --enable-vertical-pod-autoscaling`

Create the VPA:

`kubectl create -f Kubernetes/flask-vpa.yaml`

`kubectl get vpa`

## Set up Locust

Locust can be used to simulate user behaviour and stress test the cluster.

`pip install locustio`

`locust -f Locust/load_test.py`

Copy the public IP address of the service. You can find the IP address with:

`kubectl get services`


