import json
import math


def f(n, t):
    return math.cos(t / math.sqrt(n)) ** (2 * n)


ns = [4, 16, 64, 256]
fixed_t = 0.75
pointwise_errors = [abs(f(n, fixed_t) - math.exp(-(fixed_t ** 2))) for n in ns]
assert all(pointwise_errors[i + 1] < pointwise_errors[i] for i in range(len(ns) - 1))

escape_lower_bounds = []
for n in ns:
    t_n = 2.0 * math.pi * math.sqrt(n)
    assert abs(f(n, t_n) - 1.0) < 1e-12
    escape_lower_bounds.append(1.0 - math.exp(-(t_n ** 2)))

assert all(x > 0.999 for x in escape_lower_bounds)
assert all(escape_lower_bounds[i + 1] >= escape_lower_bounds[i] for i in range(len(ns) - 1))

result = {
    "schema": "marici.nima.ap-local-completion-hostile.v1",
    "cutoffs": ns,
    "each_cutoff_periodic": True,
    "pointwise_limit": "exp(-t^2)",
    "pointwise_error_decreases_at_fixed_t": True,
    "limit_is_nonzero_C0": True,
    "uniform_escape_lower_bound_min": min(escape_lower_bounds),
    "global_uniform_convergence": False,
    "local_completion_preserves_bohr_ap": False,
}
print(json.dumps(result, indent=2, sort_keys=True))

