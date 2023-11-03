# Cryptomining-Detection-Kubernetes-Explainable-Machine-Learning

This repository contains the source code to reproduce some of the results of our paper:

`Karn, Rupesh Raj, Prabhakar Kudva, Hai Huang, Sahil Suneja, and Ibrahim M. Elfadel. "Cryptomining detection in container clouds using system calls and explainable machine learning." IEEE transactions on parallel and distributed systems 32, no. 3 (2020): 674-691.`

Raw syscalls files collected for different cryptominers and helathy workloads can be downloaded from:

    https://drive.google.com/open?id=1BQPYvYPY2luTYaW4kXhbUgaFJ0vMnc1i

Cryptominers are run following the steps mentioned in 

          1. Bitcoin https://github.com/amacneil/docker-bitcoin 
          2. Bytecoin https://github.com/RafalSladek/bytecoin-docker
          3. Dashcoin https://github.com/berrywallet/bitcore-node-dash-docker
          4. Litecoin https://github.com/sreekanthgs/litecoin-docker
          5. Vertcoin https://github.com/lukechilds/docker-vertcoind
          
Normal (healthy application workloads)
          
          1. Deep Learning: https://github.com/jaehong-yoon93/DEN
          2. Cassandra Stress: https://github.com/kradio3/cassandra-stress 
          3. MySQL: https://hub.docker.com/r/progrium/stress/
          
Explainable Model:

          1. Decision tree: Graphviz   https://pythonprogramminglanguage.com/decision-tree-visual-example/ 
          2. Xgboost Ensemble: LIME    https://github.com/slundberg/shap 
          3. Neural Network: SHAP      https://github.com/marcotcr/lime
