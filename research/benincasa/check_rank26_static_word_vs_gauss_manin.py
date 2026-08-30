"""Certify the distinction between static A-word closure and GM closure."""

from __future__ import annotations

import json
from pathlib import Path


HERE=Path(__file__).resolve().parent
SAMPLES=(
    "rank26-primitive-normal-connection-sample-e1-p32003.json",
    "rank26-primitive-normal-connection-sample-e2-p32003.json",
    "rank26-primitive-normal-connection-sample-e1-p32009.json",
)


def main():
    cyclic=json.loads((HERE/"rank26-normal-slice-cyclic-rank-e1-a12-p32003.json").read_text())
    basis=json.loads((HERE/"rank26-normal-slice-word-basis.json").read_text())
    samples=[json.loads((HERE/name).read_text()) for name in SAMPLES]
    assert cyclic["record"]["horizontal_cyclic_rank"] == 26
    assert all(item["rank"] == 26 for item in basis["control_ranks"])
    assert all(item["basis_size"] == 26 for item in samples)
    assert all(not item["all_derivatives_solved"] for item in samples)
    assert all(item["unsolved_derivative_count"] == 25 for item in samples)
    assert len({item["field"] for item in samples}) == 2
    assert len({tuple(item["point"]) for item in samples}) == 3
    result={
        "schema":"marici.benincasa.rank26-static-word-vs-gauss-manin.v1",
        "status":"passed","static_A_word_rank":26,
        "true_covariant_derivatives_unsolved":25,
        "sample_files":list(SAMPLES),
        "fields":sorted({item["field"] for item in samples}),
        "points":[item["point"] for item in samples],
        "classification":"pointwise A-word closure is not a Gauss-Manin submodule",
    }
    output=HERE/"rank26-static-word-vs-gauss-manin.json"
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == "__main__": main()
