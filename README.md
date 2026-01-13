# ai_decision_engine_v2
A real-time AI decision engine that dynamically selects optimal actions using reinforcement learning (Multi-Armed Bandits) instead of hard-coded business rules.  This system continuously learns from user feedback, improving decisions over time without retraining or manual tuning.
🚀 Problem Statement

Traditional decision systems rely on static, hard-coded rules, such as:

“Always show offer_10 to new users”

“Free shipping for VIP users”

These rules:

Do not adapt

Require manual updates

Fail under changing user behavior

This project replaces static logic with a self-learning AI system that:

Explores different actions

Learns from real-time feedback

Automatically converges to the best-performing decision

🧩 Solution Overview

This project implements an Epsilon-Greedy Multi-Armed Bandit model exposed via a FastAPI-based REST service.

Core Capabilities

Real-time decision making

Online learning via feedback

Exploration vs exploitation control

Live performance statistics

Simulation for testing learning behavior

🏗️ System Architecture
Client / Simulator
        ↓
     /decide API
        ↓
 Reinforcement Learning Model
        ↓
     Decision Output
        ↓
     /feedback API
        ↓
  Model Updates (Learning)

🔧 Tech Stack

Python

FastAPI

Reinforcement Learning (Multi-Armed Bandits)

NumPy

REST APIs

Uvicorn

Simulation Framework

📂 Project Structure
ai-decision-engine-v2/
│
├── app/
│   ├── main.py        # FastAPI application
│   ├── bandit.py      # Epsilon-Greedy Bandit logic
│
├── simulator/
│   └── simulate.py    # User & reward simulator
│
├── bandit_state.json  # Persisted learning state
├── requirements.txt
└── README.md

🔁 API Endpoints
1️⃣ POST /decide

Returns a decision for a user.

Request

{
  "user_id": 1,
  "user_segment": "new"
}


Response

{
  "user_id": 1,
  "segment": "new",
  "decision": "offer_10",
  "strategy": "exploit"
}

2️⃣ POST /feedback

Provides feedback to the model so it can learn.

Request

{
  "user_id": 1,
  "user_segment": "new",
  "decision": "offer_10",
  "reward": 1
}


Response

{
  "status": "learned",
  "decision": "offer_10",
  "reward": 1
}

3️⃣ GET /stats

Returns live learning metrics.

Response

{
  "best_action": {
    "action": "offer_10",
    "count": 113,
    "avg_reward": 0.13
  }
}

🧠 Reinforcement Learning Logic

The engine uses an epsilon-greedy strategy:

Exploration: randomly try actions (ε = 0.2)

Exploitation: choose the best-known action (1 − ε)

Reward-based updates adjust action values continuously

This allows the system to:

Discover new opportunities

Avoid getting stuck in suboptimal decisions

Adapt automatically as user behavior changes

🧪 Simulation

The simulator mimics hundreds of users interacting with the system:

Generates random user segments

Simulates rewards probabilistically

Sends feedback to the API

Displays how the “best action” changes over time

This validates real-world learning behavior.

💡 Key Learnings

Built a production-style AI system, not a notebook model

Implemented online learning instead of offline training

Replaced static logic with adaptive intelligence

Designed APIs suitable for real-time systems

🌍 Real-World Use Cases

Personalized offers & promotions

Pricing optimization

Recommendation systems

Ad selection

Feature rollout experimentation (A/B testing replacement)
📈 Future Improvements

Contextual bandits (user features, time, location)

Thompson Sampling

Database-backed persistence

Cloud deployment (Docker / AWS / Azure)

Dashboard visualization

🧑‍💻 Author

Harsha Vardhan Chavvakula
AI / Data Engineer
📍 USA

⭐ Why This Project Matters

This project demonstrates how AI systems actually behave in production — learning continuously, adapting automatically, and improving decisions without manual intervention.
