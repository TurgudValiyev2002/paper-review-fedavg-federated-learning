from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import FancyArrowPatch, Rectangle


RESULTS = Path("results")


def save_process_diagram() -> None:
    nodes = [
        ("Server\ninitializes", 0.06, 0.55),
        ("Clients\ntrain locally", 0.33, 0.72),
        ("Client updates\nsent back", 0.60, 0.72),
        ("Weighted\naggregation", 0.60, 0.35),
        ("New global\nmodel", 0.33, 0.35),
    ]
    fig, ax = plt.subplots(figsize=(9, 4.8))
    ax.axis("off")
    for text, x, y in nodes:
        rect = Rectangle((x, y), 0.18, 0.16, facecolor="#e2f0df", edgecolor="#3f7a48", linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + 0.09, y + 0.08, text, ha="center", va="center", fontsize=10, weight="bold")
    arrows = [((0.24, 0.63), (0.33, 0.80)), ((0.51, 0.80), (0.60, 0.80)), ((0.69, 0.72), (0.69, 0.51)), ((0.60, 0.43), (0.51, 0.43)), ((0.33, 0.43), (0.24, 0.63))]
    for start, end in arrows:
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="->", mutation_scale=16, linewidth=1.3))
    ax.text(0.5, 0.13, "FedAvg repeats this process for many communication rounds.", ha="center", fontsize=11)
    ax.set_title("Federated Averaging Process", fontsize=15, weight="bold")
    plt.tight_layout()
    plt.savefig(RESULTS / "fedavg_process_diagram.png", dpi=180)
    plt.close()


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    papers = pd.DataFrame(
        [
            {
                "paper": "Communication-Efficient Learning of Deep Networks from Decentralized Data",
                "authors": "McMahan, Moore, Ramage, Hampson, Agüera y Arcas",
                "year": 2017,
                "url": "https://arxiv.org/abs/1602.05629",
                "what_they_did": "Introduced Federated Learning and FedAvg for decentralized training with local client updates and server averaging.",
                "main_result_or_claim": "FedAvg can reduce communication rounds by 10-100x compared with synchronized SGD in their experiments.",
                "lesson": "Communication efficiency is the central design pressure in practical federated learning.",
            },
            {
                "paper": "Federated Optimization in Heterogeneous Networks",
                "authors": "Li, Sahu, Zaheer, Sanjabi, Talwalkar, Smith",
                "year": 2018,
                "url": "https://arxiv.org/abs/1812.06127",
                "what_they_did": "Proposed FedProx, which adds a proximal term to reduce instability from heterogeneous client data and systems.",
                "main_result_or_claim": "FedProx improved stability and accuracy in highly heterogeneous settings.",
                "lesson": "FedAvg is a baseline, but heterogeneity requires extra control against client drift.",
            },
            {
                "paper": "Advances and Open Problems in Federated Learning",
                "authors": "Kairouz et al.",
                "year": 2019,
                "url": "https://arxiv.org/abs/1912.04977",
                "what_they_did": "Surveyed federated learning progress and open problems across optimization, privacy, robustness, and systems.",
                "main_result_or_claim": "Federated learning is not only optimization; it includes privacy, fairness, security, and deployment challenges.",
                "lesson": "A real FL system must be evaluated beyond test accuracy.",
            },
            {
                "paper": "Adaptive Federated Optimization",
                "authors": "Reddi et al.",
                "year": 2020,
                "url": "https://arxiv.org/abs/2003.00295",
                "what_they_did": "Developed federated versions of adaptive optimizers such as Adam, Adagrad, and Yogi.",
                "main_result_or_claim": "Adaptive server optimizers can improve federated learning under heterogeneous data.",
                "lesson": "The server optimizer is an important design choice, not a minor implementation detail.",
            },
        ]
    )
    papers.to_csv(RESULTS / "reviewed_papers.csv", index=False)

    comparison = papers[["paper", "year", "what_they_did", "lesson"]]
    comparison.to_csv(RESULTS / "paper_comparison.csv", index=False)

    algorithm = pd.DataFrame(
        [
            ("1", "Server sends current global model to selected clients."),
            ("2", "Each client trains locally for one or more epochs."),
            ("3", "Clients return model updates or updated model weights."),
            ("4", "Server averages client updates, usually weighted by local data size."),
            ("5", "The averaged model becomes the next global model."),
            ("6", "The process repeats for multiple communication rounds."),
        ],
        columns=["step", "description"],
    )
    algorithm.to_csv(RESULTS / "fedavg_algorithm_steps.csv", index=False)

    limitations = pd.DataFrame(
        [
            ("non-IID data", "Client data distributions can differ strongly, causing client drift."),
            ("systems heterogeneity", "Clients may have different compute, battery, and network quality."),
            ("privacy leakage", "Raw data stays local, but model updates can still leak information."),
            ("communication cost", "Large models and many clients make communication expensive."),
            ("server optimizer choice", "Adaptive server updates can change convergence behavior."),
        ],
        columns=["issue", "why_it_matters"],
    )
    limitations.to_csv(RESULTS / "fedavg_limitations.csv", index=False)
    save_process_diagram()
    print(papers[["year", "paper", "lesson"]].to_string(index=False))


if __name__ == "__main__":
    main()
