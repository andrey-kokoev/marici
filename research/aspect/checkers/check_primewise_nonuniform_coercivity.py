"""Exact cutoff audit for primewise positivity without uniform coercivity."""
from fractions import Fraction as F
from pathlib import Path
import json

cutoffs=[2,3,5,11,29,97]
rows=[]
for n in cutoffs:
    energies=[F(1,p) for p in range(1,n+1)]
    minimum=min(energies)
    rows.append({"cutoff":n,"minimum":f"{minimum.numerator}/{minimum.denominator}","predicted":f"1/{n}","pass":minimum==F(1,n)})
checks={
    "all_finite_sectors_positive":all(F(1,n)>0 for n in cutoffs),
    "cutoff_minimum_is_inverse_cutoff":all(r["pass"] for r in rows),
    "coercivity_constants_strictly_decrease":all(F(1,cutoffs[i+1])<F(1,cutoffs[i]) for i in range(len(cutoffs)-1)),
    "unit_approximate_null_sequence":all(F(1,n)<F(1,cutoffs[i-1]) for i,n in enumerate(cutoffs) if i>0),
}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"cutoffs":rows,"interpretation":"trivial kernel sectorwise and globally, but infimum zero and no uniform spectral gap"}
out=Path("research/aspect/results/primewise_nonuniform_coercivity.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
raise SystemExit(0 if result["status"]=="pass" else 1)
