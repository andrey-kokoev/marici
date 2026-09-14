"""Expose scope conflicts between the global transform wrapper and dependencies."""

import contextlib
import importlib
import io
import json
import sys
from pathlib import Path

ROOT = Path("research/voevodsky").resolve()
sys.path.insert(0, str(ROOT))

MODULES = (
    "check_global_conductor_cech_cospan",
    "check_cellular_log_kernel_framed_identification",
    "check_global_mixed_variance_transform",
)


def output(name):
    module = importlib.import_module(name)
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        module.main()
    return stream.getvalue()


def main():
    outputs = {name: output(name) for name in MODULES}
    assert "left_ringed_morphism: NOT_YET_CONSTRUCTED" in outputs[MODULES[0]]
    assert "ringed_algebraic_six_functor_lift: NOT_YET_CONSTRUCTED" in outputs[MODULES[1]]
    assert "mixed_variance_transform_components: ALL_CONSTRUCTED" in outputs[MODULES[2]]
    assert "normalization_sheet_kernel_in_Kato_sector: COMPLETE" in outputs[MODULES[2]]

    result = {
        "status": "passed",
        "dependency_left_ringed_morphism": "not constructed",
        "dependency_ringed_six_functor_lift": "not constructed",
        "wrapper_components_claim": "all constructed",
        "wrapper_kato_kernel_claim": "complete",
        "scope_consistent": False,
        "safe_retained_claim": "finite cellular and coefficient-level connector candidate with checked local invariants",
        "first_missing_typed_datum": "left ringed morphism, followed by its algebraic six-functor lift",
        "claim_boundary": "String-output scope audit only; no mathematical impossibility is asserted.",
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
