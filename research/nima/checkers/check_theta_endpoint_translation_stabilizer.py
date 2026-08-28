import json
import math
from pathlib import Path


def main() -> None:
    tested_shifts = (0.25, 0.5, 1.0, 2.0)
    decay_coefficients = []
    for shift in tested_shifts:
        coefficient = math.pi * (math.exp(2 * shift) - 1)
        assert coefficient > 0
        decay_coefficients.append(coefficient)

    result = {
        "schema": "marici.nima.theta-endpoint-translation-stabilizer.v1",
        "tested_positive_shifts": list(tested_shifts),
        "all_tail_decay_coefficients_are_positive": True,
        "positive_shift_ratio_limit": "0",
        "negative_shift_inverse_ratio_limit": "infinity",
        "positive_translations_stabilize_endpoint": False,
        "negative_translations_stabilize_endpoint": False,
        "endpoint_translation_stabilizer": ["0"],
        "graph_completion_requires_endpoint_continuity": True,
        "orientation_of_completed_interaction_proved": False,
    }
    output = Path(__file__).parents[1] / "results" / "theta-endpoint-translation-stabilizer.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
