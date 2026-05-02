# IDS 568 Final Project – Monitoring, Governance & Reflection

## Overview

This project demonstrates a production-style MLOps workflow by integrating monitoring, A/B testing, governance, drift detection, and risk assessment into a unified system. The goal is to go beyond model accuracy and focus on operational reliability, system transparency, and responsible AI deployment.

The system uses a FastAPI-based service with simulated traffic and metrics to represent real-world monitoring scenarios. Supporting components include experiment simulation, governance documentation, and risk analysis.

---

## Repository Structure

src/
├── monitoring/ # Metrics instrumentation (Component 1)
├── ab_test/ # A/B testing simulation (Component 2)
└── drift/ # Drift detection scripts (Component 4)

docs/
├── dashboard-interpretation.md
├── experiment-specification.md
├── recommendation-memo.md
├── model-card.md
├── risk-register.md
├── lineage-diagram.png
├── drift-diagnostic-report.md
├── governance-review.md
├── risk-matrix.md
├── system-boundary-diagram.png
└── cto-memo.md

dashboards/ # Monitoring configurations
logs/ # Audit trail
visualizations/ # Dashboard + drift visuals
requirements.txt
README.md

Setup and Reproduction

1. Clone the repository:
git clone https://github.com/jkaur2026/ids568-final-project-jkaur20.git
cd ids568-final-project-jkaur20

2. Create and activate a virtual environment:
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

Run the monitoring API:

uvicorn src.monitoring.app:app --reload

Run A/B testing simulation:

python src/ab_test/ab_test_simulation.py

Run drift detection:

python src/drift/drift_detection.py

Component Deliverables
Component 1 – Monitoring Dashboard
Metrics instrumentation: src/monitoring/
Dashboard configs: dashboards/
Visualization: visualizations/dashboard.png
Interpretation: docs/dashboard-interpretation.md



Component 2 – A/B Testing
Experiment design: docs/experiment-specification.md
Simulation: src/ab_test/
Recommendation: docs/recommendation-memo.md


Component 3 – Governance
Model card: docs/model-card.md
Risk register: docs/risk-register.md
Lineage diagram: docs/lineage-diagram.png
Audit trail: logs/


Component 4 – Drift Detection
Scripts: src/drift/
Visualizations: visualizations/
Report: docs/drift-diagnostic-report.md


Component 5 – Risk Assessment
System diagram: docs/system-boundary-diagram.png
Governance review: docs/governance-review.md
Risk matrix: docs/risk-matrix.md
CTO memo: docs/cto-memo.md



Lessons Learned
This project showed that building an AI system is not just about model performance, but also about monitoring, reliability, and governance. Key takeaways include the importance of tracking system health through metrics, validating improvements using A/B testing, and documenting risks to ensure responsible AI deployment. The integration of all components highlights how real-world systems require continuous evaluation and oversight.
