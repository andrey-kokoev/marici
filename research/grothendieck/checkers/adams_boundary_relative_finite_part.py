"""Formal exact audit of regulator cancellation in the relative finite part."""


def add(*terms):
    out = {}
    for term in terms:
        for symbol, coefficient in term.items():
            out[symbol] = out.get(symbol, 0) + coefficient
    return {symbol: coefficient for symbol, coefficient in out.items() if coefficient}


prime_sharp = {"B1": 1}
gamma_sharp = {"psi_a": -1}
prime_abel = {"B1": 1, "EulerGamma": -1}
gamma_abel = {"psi_a": -1, "EulerGamma": -1}

relative_sharp = add(prime_sharp, {k: -v for k, v in gamma_sharp.items()})
relative_abel = add(prime_abel, {k: -v for k, v in gamma_abel.items()})

assert relative_sharp == {"B1": 1, "psi_a": 1}
assert relative_abel == relative_sharp

result = {
    "sharp_relative_constant": "B1+psi(a)",
    "abel_relative_constant": "B1+psi(a)",
    "EulerGamma_regulator_shift_cancels": True,
    "quarter_shift_value": "B1+psi(1/4)=B1-EulerGamma-pi/2-3log(2)",
    "same_regulator_on_both_legs_required": True,
    "scope": "T=0 relative finite part; full height family not constructed",
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "adams-boundary-relative-finite-part.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

