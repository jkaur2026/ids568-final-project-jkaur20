# ids568-final-project-jkaur20
# IDS 568 Final Project - Monitoring, Governance & Reflection

## System Overview

This project implements a production-style MLOps framework for a simulated AI prediction service. The system includes monitoring, A/B testing, governance documentation, drift detection, and AI risk assessment.

## Repository Structure

- src/monitoring - monitoring API
- src/ab_test - A/B testing simulation
- src/drift - drift detection
- docs - reports and documentation
- logs - audit trail
- visualizations - screenshots and plots
- dashboards - configuration files

## Components

### Component 1: Monitoring
- API: src/monitoring/app.py
- Interpretation: docs/dashboard-interpretation.md

### Component 2: A/B Testing
- Code: src/ab_test/ab_test_simulation.py
- Docs: docs/experiment-specification.md, docs/recommendation-memo.md

### Component 3: Governance
- Model card: docs/model-card.md
- Risk register: docs/risk-register.md
- Lineage diagram: docs/lineage-diagram.png

### Component 4: Drift Detection
- Code: src/drift/drift_detection.py
- Report: docs/drift-diagnostic-report.md

### Component 5: Risk Assessment
- Governance review: docs/governance-review.md
- Risk matrix: docs/risk-matrix.md
- CTO memo: docs/cto-memo.md

## Setup
1. Clone the repository:
git clone https://github.com/jkaur2026/ids568-final-project-jkaur20.git
cd ids568-final-project-jkaur20

3. Create venv:
python -m venv .venv
source .venv/bin/activate

4. Install dependencies:
pip install -r requirements.txt

5. Run the monitoring AP:
uvicorn src.monitoring.app:app --reload

6. Run A/B test:
python src/ab_test/ab_test_simulation.py

6. Run drift detection:
python src/drift/drift_detection.py

Running
uvicorn src.monitoring.app:app --reload
python src/ab_test/ab_test_simulation.py
python src/drift/drift_detection.py

Lessons Learned

This project demonstrated how monitoring, evaluation, governance, and risk assessment are critical for production AI systems. It showed how models must be continuously evaluated and documented beyond just accuracy.
