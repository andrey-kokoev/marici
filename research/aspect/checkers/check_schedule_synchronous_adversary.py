from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "schedule_synchronous_adversary.json"


def single_family_means(period):
    # Cyclic rotation p=c+b has synchronous phase p-b=c modulo period.
    return [F(int(cell % period == 0)) for cell in range(32)]


def offset_family_means(period):
    # Family offset s changes p to c+b+s. Across s=0..31 every cell samples
    # each synchronous residue equally because period divides 32.
    means = []
    phase_counts = {}
    for cell in range(32):
        counts = Counter((cell + offset) % period for offset in range(32))
        phase_counts[cell] = counts
        means.append(F(counts[0], 32))
    return means, phase_counts


def main():
    periods = (2, 4, 8, 16, 32)
    witnesses = {}
    for period in periods:
        fixed = single_family_means(period)
        balanced, counts = offset_family_means(period)
        assert max(fixed) - min(fixed) == 1
        assert max(balanced) - min(balanced) == 0
        assert all(set(counter.values()) == {32 // period} for counter in counts.values())
        witnesses[str(period)] = {
            "single_family_false_cell_spread": "1",
            "offset_family_balanced_cell_spread": "0",
            "common_balanced_mean": str(F(1, period)),
            "phase_multiplicity_per_cell": 32 // period,
        }
    out = {
        "schema": "marici.aspect.schedule-synchronous-adversary.v1", "status": "pass",
        "periods": list(periods), "witnesses": witnesses,
        "marginal_cell_and_position_balance_can_pass": True,
        "joint_block_phase_position_balance_required": True,
        "repair": "use 32 independently sealed permutation-family offsets and test residual Fourier power at periods 2,4,8,16,32",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
