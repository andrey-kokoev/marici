"""Verify the linewise source of the restricted Euler-rank defect."""

import json
from pathlib import Path


path = Path(__file__).with_name("restricted_branch_loss_split.json")
data = json.loads(path.read_text(encoding="utf-8"))

generic = data["generic_rank_increments"]
homogeneous = data["homogeneous_rank_increments"]
losses = [left - right for left, right in zip(generic, homogeneous)]

assert data["line_order"] == ["q_g1", "q_g2", "q_g3", "q_g23"]
assert losses == data["increment_losses"] == [2, 2, 2, 0]
assert sum(losses) == data["total_restricted_euler_defect"] == 6
assert [g - h for g, h in zip(data["generic_branch_counts"], data["homogeneous_branch_counts"])] == losses

print("PASS: restricted Euler defect is 2+2+2 on the three forced-square lines")
