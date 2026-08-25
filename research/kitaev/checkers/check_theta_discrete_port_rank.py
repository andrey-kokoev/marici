import json
from pathlib import Path
import sympy as sp


def main():
    D = sp.Matrix([[1, 0, 1], [0, 1, 1]])
    witness = sp.Matrix([-1, -1, 1])
    columns = [tuple(D[:, j]) for j in range(D.cols)]
    assert len(set(columns)) == 3
    assert D * witness == sp.zeros(2, 1)
    assert D.rank() == 2 and len(D.nullspace()) == 1

    rank_table = []
    for n in range(1, 9):
        classical_bits = (n - 1).bit_length()
        linear_rows = n
        rank_table.append({"labels": n, "classical_identification_bits": classical_bits,
                           "minimum_linear_scalar_rows": linear_rows})

    one_hot = sp.eye(5)
    gram = one_hot.T * one_hot
    assert gram == sp.eye(5)

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "finite_dimensional_rank_theorem_and_resource_lower_bound",
        "three_label_two_bit_code": [[int(v) for v in row] for row in D.tolist()],
        "columns_pairwise_distinct": True,
        "hidden_superposition": [int(v) for v in witness],
        "hidden_output": [int(v) for v in D * witness],
        "code_rank": D.rank(),
        "rank_table": rank_table,
        "five_label_one_hot_gram": [[int(v) for v in row] for row in gram.tolist()],
        "one_hot_uniform_lower_bound": "1",
        "fixed_finite_dimensional_port_suffices_for_unbounded_labels": False,
        "physical_instrument_authority": "not_established",
    }
    out = Path(__file__).parents[1] / "results" / "theta-discrete-port-rank.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
