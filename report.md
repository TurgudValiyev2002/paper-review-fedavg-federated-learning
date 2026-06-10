# Report: FedAvg and Federated Learning

## Motivation

We reviewed FedAvg because it is a central baseline in federated learning.

## Paper / Problem

The method addresses learning from decentralized data, where clients keep raw data locally and the server combines model updates.

## Method

We summarized the algorithm steps, key concepts, and limitations in structured result tables.

## Hyperparameters

No training was done. Important FedAvg settings include client fraction, local epochs, learning rate, number of communication rounds, and weighted averaging by client data size.

## Results

The project produced algorithm-step, concept, and limitation tables plus a process-flow figure.

## Interpretation

FedAvg improves communication efficiency by allowing local training before aggregation. Its main weaknesses are non-IID data, client drift, and privacy leakage through model updates.

## Conclusion

FedAvg is a useful foundation, but practical federated learning needs extra methods for privacy, robustness, and heterogeneous clients.
