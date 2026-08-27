from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "coherence_preservation_falsifier.json"


def rank_diagonal(diagonal):
    return sum(value != 0 for value in diagonal)


def main():
    # Pauli-transfer coordinates I, X, Y, Z.
    identity = (F(1), F(1), F(1), F(1))
    dephasing = (F(1), F(0), F(0), F(1))
    computational_count_probes = ((F(1), F(0), F(0), F(1)),
                                  (F(1), F(0), F(0), F(-1)))
    count_outputs_identity = [tuple(channel * probe for channel, probe in zip(identity, state))
                              for state in computational_count_probes]
    count_outputs_dephased = [tuple(channel * probe for channel, probe in zip(dephasing, state))
                              for state in computational_count_probes]
    assert count_outputs_identity == count_outputs_dephased
    assert rank_diagonal(identity) == 4 and rank_diagonal(dephasing) == 2
    ghz_000_111_coherence = F(3, 5)
    assert identity[1] * ghz_000_111_coherence == F(3, 5)
    assert dephasing[1] * ghz_000_111_coherence == 0
    out = {
        "schema": "marici.aspect.coherence-preservation-falsifier.v1", "status": "pass",
        "computational_photon_count_outputs_identical": True,
        "identity_process_rank": 4,
        "dephasing_process_rank": 2,
        "input_000_111_coherence": "3/5",
        "identity_output_coherence": "3/5",
        "dephased_output_coherence": "0",
        "required_probe_coordinates": ["I", "X", "Y", "Z", "complex Bargmann triad", "three-wing 000-111 coherence"],
        "verdict": "photon-count preservation does not certify coherent-process preservation",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
