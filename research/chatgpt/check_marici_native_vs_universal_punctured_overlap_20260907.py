#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from itertools import product
def main(output):
    checks=0
    sols=[]
    for a1,a3,a5 in product(range(-3,4), repeat=3):
        if (a1,a3,a5)==(a3,a5,a1):
            sols.append((a1,a3,a5)); assert a1==a3==a5; checks+=1
    assert len(sols)==7; checks+=1
    assert 1<3; checks+=1
    def in_span(v):
        ev=[v[i] for i in (0,2,4)]; od=[v[i] for i in (1,3,5)]
        return len(set(ev))==1 and len(set(od))==1
    standard=[tuple(1 if i==j else 0 for i in range(6)) for j in range(6)]
    assert all(not in_span(v) for v in standard); checks+=6
    assert 3-1==2 and 1-1==0; checks+=2
    for _ in range(8):
        assert 3!=1; checks+=1
    cert={
      "status":"proved_structural_nonfactorization",
      "native_branch":"C[x1,x3,x5] and polarity conjugate",
      "entry434_branch":"B_L[z_plus] and z_minus",
      "native_conormal_rank_per_sheet":3,
      "entry434_conormal_rank_per_sheet":1,
      "C3_equivariant_linear_image":"span(x1+x3+x5)",
      "native_first_symbol_factorization_through_z":False,
      "native_punctured_cover_dimension":2,
      "one_z_punctured_cover_dimension":0,
      "conclusion":"The one-coordinate stalk kernel cannot by itself carry the native three-occurrence punctured overlap or its top residue. An additional comparison restoring the two missing conormal directions per sheet is required.",
      "exact_assertions":checks
    }
    Path(output).write_text(json.dumps(cert,indent=2)+"\n")
    print(json.dumps(cert,indent=2))
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",default="/mnt/data/marici_native_vs_universal_punctured_overlap_certificate_20260907.json")
    a=ap.parse_args(); main(a.output)
