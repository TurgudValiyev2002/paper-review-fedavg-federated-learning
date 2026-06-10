# Kairouz et al. 2019: Open Problems in Federated Learning

Paper: "Advances and Open Problems in Federated Learning"  
Link: https://arxiv.org/abs/1912.04977

This paper is a broad survey of federated learning. It is useful because it prevents us from thinking about FL only as an optimization algorithm. Federated learning is a system-level and privacy-sensitive setting.

The paper discusses many dimensions: optimization, communication, privacy, security, fairness, personalization, robustness, and systems constraints. This matters because a federated model can have good test accuracy and still be weak in practice if it leaks private information, fails under client dropout, or performs unfairly across user groups.

The main contribution is organizing the field and naming open problems. For a researcher, this is valuable because it shows where FedAvg fits: it is one method inside a much larger research landscape.

What we learn is that federated learning needs multi-dimensional evaluation. We should ask about accuracy, communication cost, privacy risk, client heterogeneity, robustness, and fairness.

The limitation is that a survey does not solve these problems directly. Its value is conceptual: it helps define the research agenda and gives structure to later experiments.
