from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

RESULTS = Path("results")

def main():
    RESULTS.mkdir(exist_ok=True)
    steps = pd.DataFrame([
        ("1", "Server initializes global model", "All clients start from the same model."),
        ("2", "Server selects clients", "Only a subset may participate in each round."),
        ("3", "Clients train locally", "Each client updates the model on private local data."),
        ("4", "Clients send updates", "The server receives model weights or weight changes, not raw data."),
        ("5", "Server averages updates", "Updates are weighted by client dataset size."),
        ("6", "New global model is broadcast", "The process repeats for multiple communication rounds."),
    ], columns=["step", "fedavg_action", "meaning"])
    steps.to_csv(RESULTS / "fedavg_algorithm_steps.csv", index=False)
    concepts = pd.DataFrame([
        ("communication efficiency", "Local epochs reduce how often clients communicate with the server."),
        ("data privacy direction", "Raw user data stays on devices, although updates can still leak information."),
        ("non-IID challenge", "Client data may have very different distributions."),
        ("weighted averaging", "Large clients influence the global model more than small clients."),
        ("baseline importance", "FedAvg became a reference algorithm for later federated learning work."),
    ], columns=["concept", "interpretation"])
    concepts.to_csv(RESULTS / "fedavg_key_concepts.csv", index=False)
    limitations = pd.DataFrame([
        ("privacy is not automatic", "Model updates can still reveal information without secure aggregation or differential privacy."),
        ("client drift", "Local training can move clients in different directions under non-IID data."),
        ("systems heterogeneity", "Devices differ in compute, battery, and network quality."),
    ], columns=["limitation", "why_it_matters"])
    limitations.to_csv(RESULTS / "fedavg_limitations.csv", index=False)
    plt.figure(figsize=(8, 4))
    plt.bar(steps["step"], range(1, len(steps) + 1), color="#3d6fb6")
    plt.xlabel("FedAvg step")
    plt.ylabel("Process order")
    plt.title("FedAvg Algorithm Flow")
    plt.tight_layout()
    plt.savefig(RESULTS / "fedavg_algorithm_flow.png", dpi=160)
    print(steps.to_string(index=False))

if __name__ == "__main__":
    main()
