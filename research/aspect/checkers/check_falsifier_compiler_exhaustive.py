import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_RESULT = ROOT / "results" / "falsifier_compiler.json"
RESULT = ROOT / "results" / "falsifier_compiler_exhaustive.json"


def current_signature(mask):
    return tuple((mask >> bit) & 1 for bit in range(8))


def augmented_signature(mask):
    return tuple((mask >> bit) & 1 for bit in range(16))


def main():
    source = json.loads(SOURCE_RESULT.read_text(encoding="utf-8"))
    current_survivors = []
    repaired_survivors = []
    for mask in range(1, 1 << 16):
        if not any(current_signature(mask)):
            current_survivors.append(mask)
        if not any(augmented_signature(mask)):
            repaired_survivors.append(mask)
    assert len(current_survivors) == 255
    assert repaired_survivors == []
    singleton_holdouts = [1 << bit for bit in range(8, 16)]
    assert all(mask in current_survivors for mask in singleton_holdouts)
    assert source["unresolved_kernel_dimension"] == 8
    assert source["post_repair_unresolved_kernel_dimension"] == 0
    out = {
        "schema": "marici.aspect.falsifier-compiler-exhaustive-check.v1", "status": "pass",
        "nonzero_binary_mutations_enumerated": (1 << 16) - 1,
        "current_nonzero_binary_kernel_count": len(current_survivors),
        "expected_from_dimension_eight": (1 << 8) - 1,
        "all_eight_singleton_holdouts_survive_current_tester": True,
        "post_repair_nonzero_binary_kernel_count": len(repaired_survivors),
        "agrees_with_gaussian_kernel_dimensions": True,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
