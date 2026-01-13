import random
import requests
import time

API = "http://127.0.0.1:8000"

def reward_for(action):
    # pretend offer_10 is best in the "real world"
    probs = {
        "offer_0": 0.02,
        "offer_5": 0.05,
        "offer_10": 0.12,
        "offer_free_ship": 0.07
    }
    return 1 if random.random() < probs[action] else 0

for i in range(300):
    user_id = i + 1
    segment = random.choice(["new", "returning", "vip"])

    d = requests.post(f"{API}/decide", json={"user_id": user_id, "user_segment": segment}).json()
    action = d["decision"]
    r = reward_for(action)

    requests.post(f"{API}/feedback", json={
        "user_id": user_id,
        "user_segment": segment,
        "decision": action,
        "reward": r
    })

    if i % 50 == 0:
        s = requests.get(f"{API}/stats").json()
        print("Best now:", s["best_action"])

    time.sleep(0.03)

print("Done. Open /stats")
