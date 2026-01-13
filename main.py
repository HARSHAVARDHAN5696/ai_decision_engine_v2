from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

from app.bandit import EpsilonGreedyBandit


app = FastAPI(title="AI Decision Engine v2")

ACTIONS = ["offer_0", "offer_5", "offer_10", "offer_free_ship"]
STATE_PATH = "bandit_state.json"

# Load bandit if saved, else create new
if os.path.exists(STATE_PATH):
    with open(STATE_PATH, "r") as f:
        bandit = EpsilonGreedyBandit.from_dict(json.load(f))
else:
    bandit = EpsilonGreedyBandit(actions=ACTIONS, epsilon=0.2)


# ---------- Request Schemas ----------
class DecideRequest(BaseModel):
    user_id: int
    user_segment: str


class FeedbackRequest(BaseModel):
    user_id: int
    user_segment: str
    decision: str
    reward: float


# ---------- Endpoints ----------
@app.post("/decide")
def decide(req: DecideRequest):
    action, strategy = bandit.choose()
    return {
        "user_id": req.user_id,
        "segment": req.user_segment,
        "decision": action,
        "strategy": strategy
    }


@app.post("/feedback")
def feedback(req: FeedbackRequest):
    bandit.update(req.decision, req.reward)

    # Save updated state so learning persists
    with open(STATE_PATH, "w") as f:
        json.dump(bandit.to_dict(), f)

    return {
        "status": "learned",
        "decision": req.decision,
        "reward": req.reward
    }


@app.get("/stats")
def stats():
    actions_data = []
    for i, a in enumerate(bandit.actions):
        actions_data.append({
            "action": a,
            "count": bandit.counts[i],
            "avg_reward": bandit.values[i]
        })

    best_action = max(actions_data, key=lambda x: x["avg_reward"]) if actions_data else None

    return {
        "epsilon": bandit.epsilon,
        "actions": actions_data,
        "best_action": best_action
    }
