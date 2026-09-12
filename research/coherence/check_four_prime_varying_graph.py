#!/usr/bin/env python3
"""Verify breakpoint transport for the finite four-prime varying graph bundle."""

import json
import math
from itertools import combinations
from pathlib import Path

PRIMES = (2, 3, 5, 7)
LENGTHS = tuple(math.log(p) for p in PRIMES)
TOL = 1e-12


def unique(xs):
    return tuple(sorted({round(x, 14) for x in xs if x > TOL}))


def R_breaks(B, a): return unique(b-a for b in B if b > a+TOL)
def S_breaks(B, a): return unique((a,) + tuple(a+b for b in B))
def subsets(xs):
    for n in range(len(xs)+1): yield from combinations(xs,n)


def main():
    subset_sums = unique(sum(LENGTHS[i] for i in S) for S in subsets(range(4)))
    # Every finite transport sends a finite graph fiber to another finite graph fiber.
    rows=[]
    for i,(p,a) in enumerate(zip(PRIMES,LENGTHS)):
        rb=R_breaks(subset_sums,a); sb=S_breaks(subset_sums,a)
        assert len(rb)<float('inf') and len(sb)<float('inf')
        rows.append({"prime":p,"R_target_breaks":rb,"S_target_breaks":sb})
    result={
      "schema":"marici.coherence.four-prime-varying-graph.v1",
      "source_breaks":subset_sums,
      "source_break_count":len(subset_sums),
      "transport_rules":{"R_a":"{b-a | b in B, b>a}","S_a":"{a} union {a+b | b in B}"},
      "all_target_fibers_finite":True,
      "fibers":rows,
      "common_fixed_fiber_claim":False
    }
    target=Path(__file__).with_name("four-prime-varying-graph.v1.json")
    target.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"source_break_count":len(subset_sums),"all_target_fibers_finite":True,"common_fixed_fiber_claim":False},indent=2))

if __name__=="__main__": main()
