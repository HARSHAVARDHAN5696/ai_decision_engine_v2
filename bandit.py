import random
import json
import os


class EpsilonGreedyBandit:
    """
    Epsilon-Greedy Multi-Armed Bandit
    - explore with probability epsilon
    - exploit (pick best average reward) otherwise
    """

    def __init__(self, actions, epsilon=0.2):
        self.actions = actions
        self.epsilon = float(epsilon)
        self.counts = [0] * len(actions)      # how many times each action chosen
        self.values = [0.0] * len(actions)    # avg reward per action

    def choose(self):
        # Explore
        if random.random() < self.epsilon:
            idx = random.randrange(len(self.actions))
            return self.actions[idx], "explore"

        # Exploit: pick action with highest avg reward
        best_idx = max(range(len(self.actions)), key=lambda i: self.values[i])
        return self.actions[best_idx], "exploit"

    def update(self, chosen_action, reward):
        # Update average reward for the chosen action
        if chosen_action not in self.actions:
            return

        i = self.actions.index(chosen_action)
        self.counts[i] += 1

        # incremental average update
        n = self.counts[i]
        old_avg = self.values[i]
        new_avg = old_avg + (reward - old_avg) / n
        self.values[i] = new_avg

    # ---------- Persistence helpers ----------
    def to_dict(self):
        return {
            "actions": self.actions,
            "epsilon": self.epsilon,
            "counts": self.counts,
            "values": self.values
        }

    @classmethod
    def from_dict(cls, d):
        obj = cls(actions=d["actions"], epsilon=d.get("epsilon", 0.2))
        obj.counts = d.get("counts", [0] * len(obj.actions))
        obj.values = d.get("values", [0.0] * len(obj.actions))
        return obj
