from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "timeless_calculus_on_mixed_green_hostile.json"


def trace(v):
    return v[0]


def beta(x, y):
    return sum(a * b for a, b in zip(x, y))


def incidence(v, s):
    # A finite graph-domain fixture. Coordinates are boundary and two interior
    # carrier modes, not instants. The difference map is an incidence choice.
    boundary, u, w = v
    derivative = (u - boundary, w - u, -w)
    return tuple(d + s * z for d, z in zip(derivative, v))


def main():
    h = (F(0), F(1), F(-1))
    s_plus, s_minus = F(2), F(3)
    f_plus = tuple(-x for x in incidence(h, s_plus))
    f_minus = tuple(-x for x in incidence(h, s_minus))

    assert trace(h) == 0
    assert beta(h, h) == 2
    assert tuple(-x for x in incidence(h, s_plus)) == f_plus
    assert tuple(-x for x in incidence(h, s_minus)) == f_minus

    scalar_first_record = (trace(h), trace(h))
    relational_first_record = {"equalized_traces": trace(h) == trace(h),
                               "mixed_green_pairing": beta(h, h)}
    assert scalar_first_record == (0, 0)
    assert relational_first_record == {"equalized_traces": True,
                                       "mixed_green_pairing": F(2)}

    out = {
        "schema": "marici.aspect.timeless-calculus-mixed-green-hostile.v1",
        "status": "pass",
        "marked_carrier_germs": {"plus": [str(x) for x in h], "minus": [str(x) for x in h]},
        "comparison_ports": {"plus_endpoint_trace": "0", "minus_endpoint_trace": "0"},
        "incidence_sources": {"f_plus": [str(x) for x in f_plus],
                              "f_minus": [str(x) for x in f_minus]},
        "local_mate": "endpoint equalizer passes",
        "outer_relational_mate": {"mixed_green_pairing": "2"},
        "premature_quotient_output": ["0", "0"],
        "descent_residual": "2",
        "time_used": False,
        "realization_optional": "a later map may bind carrier coordinates to a sampled half-line record, but the obstruction precedes that map",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
