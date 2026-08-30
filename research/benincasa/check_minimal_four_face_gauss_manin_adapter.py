"""Certify the minimal source-derived four-face cutoff adapter."""

from __future__ import annotations

import json
from pathlib import Path


HERE=Path(__file__).resolve().parent


def load(name):return json.loads((HERE/name).read_text())


def main():
    baseline=load("cutoff-inclusion-gauss-manin-adapter-a8-to-a14-p32003-point-2-3-m4.json")
    k_only=load("cutoff-inclusion-gauss-manin-adapter-a8-to-a14-kplus1-qplus0-p32003-point-2-3-m4.json")
    singles={name:load(f"cutoff-inclusion-gauss-manin-adapter-a8-to-a14-{name}plus1-p32003-point-2-3-m4.json")["adapter_cone_rank"] for name in ("g1","g2","g3","g23","g31")}
    pairs={
      "g1,g2":load("cutoff-inclusion-gauss-manin-adapter-a8-to-a14-kplus1-qplus0-g1-g2plus1-p32003-point-2-3-m4.json")["adapter_cone_rank"],
      "g1,g3":load("cutoff-inclusion-gauss-manin-adapter-a8-to-a14-kplus1-qplus0-g1-g3plus1-p32003-point-2-3-m4.json")["adapter_cone_rank"],
      "g2,g3":load("cutoff-inclusion-gauss-manin-adapter-a8-to-a14-kplus1-qplus0-g2-g3plus1-p32003-point-2-3-m4.json")["adapter_cone_rank"],
    }
    no_k=load("cutoff-inclusion-gauss-manin-adapter-a8-to-a14-g1-g2-g3plus1-p32003-point-2-3-m4.json")
    close12=load("cutoff-inclusion-gauss-manin-adapter-a8-to-a12-kplus1-qplus0-g1-g2-g3plus1-p32003-point-2-3-m4.json")
    close14=load("cutoff-inclusion-gauss-manin-adapter-a8-to-a14-kplus1-qplus0-g1-g2-g3plus1-p32003-point-2-3-m4.json")
    close_prime=load("cutoff-inclusion-gauss-manin-adapter-a8-to-a14-kplus1-qplus0-g1-g2-g3plus1-p32009-point-3-5-m7.json")
    insufficient=load("cutoff-inclusion-gauss-manin-adapter-a8-to-a10-kplus1-qplus0-g1-g2-g3plus1-p32003-point-2-3-m4.json")
    assert baseline["adapter_cone_rank"]==2349 and k_only["adapter_cone_rank"]==1724
    assert singles=={"g1":1854,"g2":2693,"g3":2718,"g23":2378,"g31":2379}
    assert pairs=={"g1,g2":667,"g1,g3":732,"g2,g3":925}
    assert no_k["adapter_cone_rank"]==412
    assert insufficient["adapter_cone_rank"]==3032
    assert all(item["adapter_cone_rank"]==0 and item["gauss_manin_compatible"] for item in (close12,close14,close_prime))
    result={
      "schema":"marici.benincasa.minimal-four-face-gauss-manin-adapter.v1","status":"passed",
      "minimal_target_shift":{"polynomial_ambient":4,"K_depth":1,"q_depth":{"g1":1,"g2":1,"g3":1,"g23":0,"g31":0}},
      "baseline_cone_rank":2349,"K_only_cone_rank":1724,"single_q_cone_ranks":singles,
      "K_plus_two_global_cone_ranks":pairs,"three_global_without_K_rank":412,"insufficient_polynomial_plus2_rank":3032,
      "closed_cone_ranks":{"ambient_plus4":0,"ambient_plus6":0,"independent_prime_point":0},
      "classification":"the quartic polynomial shift, one K layer, and all three global marked layers are jointly necessary and sufficient in the declared face cube",
    }
    output=HERE/"minimal-four-face-gauss-manin-adapter.json"
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":main()
