# Paper Review: FedAvg and Federated Learning

## Motivation

Federated learning is important when data is distributed across many clients and cannot be easily centralized. FedAvg is one of the core algorithms in this area, so understanding it is necessary before studying more advanced federated methods.

## Project Goal

We reviewed the main idea of Federated Averaging: clients train locally, send model updates, and the server averages those updates into a new global model.

## Paper / Problem

The reviewed method is Federated Averaging, introduced as a practical algorithm for communication-efficient learning from decentralized data.

## Tools

Python, pandas, and matplotlib.

## Method

We summarized the algorithm as structured tables: algorithm steps, key concepts, and limitations. We also created a simple figure showing the order of the FedAvg process.

## Hyperparameters

No model was trained in this review. Important FedAvg settings discussed conceptually include number of clients per round, local epochs, learning rate, and client-weighted averaging.

## Results

The result files are:

- `results/fedavg_algorithm_steps.csv`
- `results/fedavg_key_concepts.csv`
- `results/fedavg_limitations.csv`
- `results/fedavg_algorithm_flow.png`

## Interpretation

FedAvg is powerful because it reduces communication: clients perform several local updates before sending information to the server. However, it does not solve privacy by itself, and it can struggle when clients have very different data distributions.

## Conclusion

FedAvg is a foundation for federated learning. A serious implementation must still consider non-IID data, privacy leakage from updates, unstable clients, and communication cost.

## How To Run

```bash
pip install -r requirements.txt
python 1_fedavg_review_tables.py
```
