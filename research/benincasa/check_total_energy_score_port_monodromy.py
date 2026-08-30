"""Coefficient characters of the three total-energy tangency score ports."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def character(exponent: Fraction) -> int:
    # All present exponents are integral or half-integral.
    return 1 if exponent.denominator == 1 else -1


def main() -> None:
    # Entries 683--689: F_g3 is proportional to
    # 1/(lambda*x^2*y^2), lambda^2=-2*x*y/(x+y).
    g3 = {"x": Fraction(-5,2), "y": Fraction(-5,2), "x+y": Fraction(1,2)}
    # The exact regularized traces from Entry 2391 are -3/(8xy), and the
    # tangency square root is sqrt(4x^2y^2); hence F_g1,F_g2 ~ x^-2 y^-2.
    tate = {"x": Fraction(-2), "y": Fraction(-2), "x+y": Fraction(0)}
    ports = {
        "g1": {"exponents": tate, "type": "Tate"},
        "g2": {"exponents": tate, "type": "Tate"},
        "g3": {"exponents": g3, "type": "Kummer"},
    }
    for row in ports.values():
        row["semisimple_characters"] = {face:character(value)
                                         for face,value in row["exponents"].items()}
        row["nilpotent_rank"] = 0
        row["exponents"] = {face:str(value) for face,value in row["exponents"].items()}
    assert ports["g1"]["semisimple_characters"] == {"x":1,"y":1,"x+y":1}
    assert ports["g2"]["semisimple_characters"] == {"x":1,"y":1,"x+y":1}
    assert ports["g3"]["semisimple_characters"] == {"x":-1,"y":-1,"x+y":-1}
    result = {
        "schema":"marici.benincasa.total-energy-score-port-monodromy.v1",
        "ports":ports,
        "direct_sum_characters":{
            "x":[1,1,-1], "y":[1,1,-1], "x+y":[1,1,-1]
        },
        "observer_cartier_cokernel_length":0,
        "classification":(
            "semisimple sector-specific coefficient characters with no "
            "observer torsion and no rank-one nilpotent monodromy"
        ),
        "new_carrier_datum":False,
    }
    rendered=json.dumps(result,indent=2,sort_keys=True)+"\n"
    Path(__file__).with_name("total-energy-score-port-monodromy.json").write_text(rendered)
    print(rendered,end="")


if __name__=="__main__":
    main()
