# Paper Review: FedAvg and Federated Learning

## Motivation

Federated learning is not just "training without sharing data." It is a full learning setting with communication limits, non-IID client data, unreliable devices, privacy risks, and server-side optimization choices. This review studies FedAvg and three related papers to understand the method and its limitations.

## Project Goal

We reviewed four papers:

1. McMahan et al., 2017: FedAvg.
2. Li et al., 2018: FedProx for heterogeneous networks.
3. Kairouz et al., 2019: open problems in federated learning.
4. Reddi et al., 2020: adaptive federated optimization.

The goal is to understand what FedAvg does, why it became a baseline, and what later work changed or criticized.

## Reviewed Papers

| Paper | Year | Main contribution |
|---|---:|---|
| [Communication-Efficient Learning of Deep Networks from Decentralized Data](https://arxiv.org/abs/1602.05629) | 2017 | Introduced FedAvg for communication-efficient decentralized training. |
| [Federated Optimization in Heterogeneous Networks](https://arxiv.org/abs/1812.06127) | 2018 | Proposed FedProx to improve stability under client heterogeneity. |
| [Advances and Open Problems in Federated Learning](https://arxiv.org/abs/1912.04977) | 2019 | Organized the broader FL research problems: privacy, security, optimization, fairness, and systems. |
| [Adaptive Federated Optimization](https://arxiv.org/abs/2003.00295) | 2020 | Studied adaptive server optimizers such as federated Adam, Adagrad, and Yogi. |

## What The Papers Did

McMahan et al. introduced FedAvg: clients train locally, send updates, and the server averages them. The key result is communication efficiency: local training can reduce how often clients need to communicate.

Li et al. argued that FedAvg can become unstable when clients have very different data or system capabilities. FedProx adds a proximal term to keep local updates closer to the global model.

Kairouz et al. broadened the discussion. Federated learning is not only an optimization problem; it also includes privacy, robustness, fairness, compression, personalization, and deployment constraints.

Reddi et al. showed that the server update rule matters. Adaptive federated optimizers can improve convergence under heterogeneous data.

## FedAvg Process

The basic FedAvg loop is:

1. Server initializes a global model.
2. Server sends it to selected clients.
3. Clients train locally.
4. Clients send updates.
5. Server averages updates by client data size.
6. The new global model is sent out again.

## Results Produced In This Repository

The repository creates:

- `results/reviewed_papers.csv`
- `results/paper_comparison.csv`
- `results/fedavg_algorithm_steps.csv`
- `results/fedavg_limitations.csv`
- `results/fedavg_process_diagram.png`

## Interpretation

FedAvg is important because it made federated learning practical and simple. But it is not enough by itself. Non-IID data, unstable clients, privacy leakage through updates, and server optimizer design all matter.

## Conclusion

FedAvg should be treated as the starting baseline for federated learning. Later work such as FedProx and adaptive federated optimization exists because real FL systems are heterogeneous and difficult.

## How To Run

```bash
pip install -r requirements.txt
python 1_fedavg_review_tables.py
```
