# McMahan et al. 2017: Federated Averaging

Paper: "Communication-Efficient Learning of Deep Networks from Decentralized Data"  
Link: https://arxiv.org/abs/1602.05629

This is the core FedAvg paper. The authors introduced federated learning as a setting where many clients train a shared model while keeping raw data decentralized. The practical motivation is clear: mobile and edge devices contain useful data, but sending all raw data to a central server can be expensive, sensitive, or impossible.

The main method is Federated Averaging. The server sends the current model to selected clients. Clients train locally for one or more epochs. Then they send updates or updated weights back to the server. The server averages them, usually weighted by client dataset size.

The important contribution is communication efficiency. Local training means clients do more work before communicating, which can reduce the number of communication rounds compared with synchronized SGD.

What we learn is that federated learning is not just distributed training. The clients are unreliable, data is often non-IID, and communication is a main bottleneck.

The limitation is that FedAvg is simple and can struggle with heterogeneous client data. It also does not automatically solve privacy, because model updates can still leak information.
