# walmart-genAI-llmops-23rdNov2026

### cicd for llm powered app deployment in k8s 

<img src="k8s1.png">

### pushing image to docker hub so that we can deploy on k8s

```
ureuser@ashumodle-container:~$ sudo docker images
                                                                                                                        i Info →   U  In Use
IMAGE                                                 ID             DISK USAGE   CONTENT SIZE   EXTRA
ashu-walmart:llamacppv1                               9f1e58345c3d        1.7GB          562MB    U   
dockerashu/small-flask:appv2                          daaf5f1d506c        189MB           46MB    U   
dockerashu/smollm-cpu:1.0                             360c9e814f91        1.7GB          562MB    U   
ghcr.io/huggingface/text-generation-inference:3.3.7   c01c6b7c3087       26.7GB         9.25GB        
lmsysorg/sglang:v0.5.23-xeon                          f22c18d17527       7.96GB          2.1GB        
qdrant/qdrant:latest                                  d277592721d2        287MB         78.7MB    U   
small-flask:appv1                                     4b07bcec70f2        189MB           46MB        
small-flask:appv2                                     daaf5f1d506c        189MB           46MB    U   
smollm-cpu:1.0                                        360c9e814f91        1.7GB          562MB    U   
walmart-smoll-llm:lamma-cpp-v1                        456886fdc28a        1.7GB          562MB    U   
azureuser@ashumodle-container:~$ sudo docker  tag  ashu-walmart:llamacppv1   dockerashu/ashu-walmart:llamacppv1
azureuser@ashumodle-container:~$ sudo docker login -u dockerashu

i Info → A Personal Access Token (PAT) can be used instead.
         To create a PAT, visit https://app.docker.com/settings
         
         
Password: 
Login Succeeded
azureuser@ashumodle-container:~$ sudo docker push  dockerashu/ashu-walmart:llamacppv1
The push refers to repository [docker.io/dockerashu/ashu-walmart]
96aae9022e0e: Mounted from dockerashu/smollm-cpu 
340c6376a26a: Pushed 
517b871c26ea: Mounted from dockerashu/smollm-cpu 
44136fa355b3: Mounted from dockerashu/smollm-cpu 
9ff74591318f: Mounted from dockerashu/smollm-cpu 


```


## LLM apps monitoring pillers

<img src="llm2.png">


### Custom mertrics mon for LLMs

<img src="llm3.png">

### Implementing custom metrics 

```
azureuser@ashumodle-container:~$ sudo  docker images
                                                                                                                        i Info →   U  In Use
IMAGE                                                 ID             DISK USAGE   CONTENT SIZE   EXTRA
ashu-walmart:llamacppv1                               9f1e58345c3d        1.7GB          562MB    U   
dockerashu/ashu-walmart:llamacppv1                    9f1e58345c3d        1.7GB          562MB    U   
dockerashu/small-flask:appv2                          daaf5f1d506c        189MB           46MB    U   
dockerashu/smollm-cpu:1.0                             360c9e814f91        1.7GB          562MB    U   
ghcr.io/huggingface/text-generation-inference:3.3.7   c01c6b7c3087       26.7GB         9.25GB        
lmsysorg/sglang:v0.5.23-xeon                          f22c18d17527       7.96GB          2.1GB        
qdrant/qdrant:latest                                  d277592721d2        287MB         78.7MB    U   
small-flask:appv1                                     4b07bcec70f2        189MB           46MB        
small-flask:appv2                                     daaf5f1d506c        189MB           46MB    U   
smollm-cpu:1.0                                        360c9e814f91        1.7GB          562MB    U   
walmart-smoll-llm:lamma-cpp-v1                        456886fdc28a        1.7GB          562MB    U   
azureuser@ashumodle-container:~$ sudo docker  ps 
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
azureuser@ashumodle-container:~$ 


```

### creating vector instance 

```
 docker run -d   --name qdrant-demo   -p 6333:6333   -p 6334:6334   -v qdrant_storage:/qdrant/storage   qdrant/qdrant

```
### using sample data 

```
 cat documents/sample_docs.json 

[
  {
    "id": 1,
    "title": "Kubernetes Pod",
    "category": "Kubernetes",
    "content": "A Kubernetes Pod is the smallest deployable unit in Kubernetes. It can contain one or more containers. Pods are managed by Kubernetes controllers such as Deployments."
  },
  {
    "id": 2,
    "title": "Docker Container",
    "category": "Docker",
    "content": "Docker containers package applications and their dependencies into isolated environments. Docker images are used to create containers, making application deployment consistent across environments."
  },
  {
    "id": 3,
    "title": "Linux Troubleshooting",
    "category": "Linux",
    "content": "Linux administrators use commands such as top, free, df, ps, and journalctl to troubleshoot CPU, memory, disk, process, and system log issues."
  },
  {
    "id": 4,
    "title": "CI/CD Pipeline",
    "category": "DevOps",
    "content": "A CI/CD pipeline automates application building, testing, and deployment. Tools such as Jenkins and GitHub Actions help teams deliver software continuously."
  },
  {
    "id": 5,
    "title": "Kubernetes Scaling",
    "category": "Kubernetes",
    "content": "Kubernetes Horizontal Pod Autoscaler automatically adjusts the number of application Pod replicas based on observed metrics such as CPU and memory utilization."
  }
]

(llmops-env) root@ashumodle-container:~/LLMOps-Lab/qdrant-demo# 

```


## Understanding some basic about fine tuning 

<img src="ft1.png">


