from __future__ import annotations
import json
import flint
import scipy
from flint import arb, arb_mat

x = arb(1)
methods = ["lower", "upper", "mid", "rad", "contains", "is_positive", "contains_zero"]
m = arb_mat([[arb(2), arb(1)], [arb(1), arb(2)]])
result = {
    "flint_version": flint.__version__,
    "scipy_version": scipy.__version__,
    "arb_methods": {name: hasattr(x, name) for name in methods},
    "arb_mat_getitem": str(m[0, 0]),
    "positive_comparison_supported": None,
}
try:
    result["positive_comparison_supported"] = bool(x > 0)
except Exception as exc:
    result["positive_comparison_error"] = f"{type(exc).__name__}: {exc}"
print(json.dumps(result, indent=2, sort_keys=True))
