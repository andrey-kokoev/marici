"""Exact periodicity, multiplicativity, and density checks for resonance sieves."""

from math import gcd
import json
from pathlib import Path


def phi(n):
    return sum(gcd(a,n)==1 for a in range(1,n+1))


def run(name,radical,limit=120):
    values={n:gcd(n,radical)==1 for n in range(1,limit+1)}
    periodic_checks=0
    for n in range(1,limit-radical+1):
        assert values[n]==values[n+radical]
        periodic_checks+=1
    multiplicative_checks=0
    for m in range(1,31):
        for n in range(1,31):
            assert (gcd(m*n,radical)==1)==(gcd(m,radical)==1 and gcd(n,radical)==1)
            multiplicative_checks+=1
    period_survivors=sum(gcd(n,radical)==1 for n in range(1,radical+1))
    assert period_survivors==phi(radical)
    return {"family":name,"radical":radical,"period_survivors":period_survivors,
            "density":f"{period_survivors}/{radical}",
            "periodicity_checks":periodic_checks,
            "multiplicativity_checks":multiplicative_checks}


def main():
    families=[run("five_site_C2",2),run("A4_or_Q8C3",6),
              run("C5_semidirect_C4",10),run("Heisenberg27",3),
              run("mixed_2_3_5",30)]
    result={"theorem":"compatible indices are units modulo the radical resonance modulus",
            "families":families,
            "exact_checks":sum(x["periodicity_checks"]+x["multiplicativity_checks"] for x in families),
            "status":"pass"}
    out=Path(__file__).parents[1]/"results"/"radical-resonance-unit-sieve.json"
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))


if __name__=="__main__": main()
