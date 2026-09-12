#!/usr/bin/env python3
"""Verify parity-dependent refinement when two ordered points are inserted in a gap."""

import json, random
from fractions import Fraction
from pathlib import Path


def amplitude(gaps):
    z=Fraction(1)
    for i in range(0,len(gaps),2): z*=gaps[i]
    return z

def main():
    rng=random.Random(20260912);rows=[]
    for points in (2,4,6,8,10):
        for trial in range(20):
            gaps=[Fraction(rng.randrange(1,10),rng.randrange(1,10)) for _ in range(points-1)]
            old=amplitude(gaps)
            for k,g in enumerate(gaps):
                l=Fraction(rng.randrange(1,10),rng.randrange(1,10));m=Fraction(rng.randrange(1,10),rng.randrange(1,10));r=g/(l*m)
                refined=gaps[:k]+[l,m,r]+gaps[k+1:];ratio=amplitude(refined)/old
                expected=m if k%2 else 1/m
                assert ratio==expected
                rows.append({'points':points,'gap_index':k,'gap_parity':'between_pairs' if k%2 else 'inside_pair','ratio':str(ratio),'inserted_pair_amplitude':str(m)})
    result={'schema':'marici.coherence.pair-insertion-refinement.v1','cases':len(rows),'all_refinements_exact':True,'inside_pair_law':'Z(refined)/Z(old)=Z(inserted_pair)^(-1)','between_pairs_law':'Z(refined)/Z(old)=Z(inserted_pair)','consequence':'the theory is metric and parity-polarized, not invariant under arbitrary subdivision','rows':rows}
    Path(__file__).with_name('pair-insertion-refinement.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','all_refinements_exact','inside_pair_law','between_pairs_law','consequence')},indent=2))
if __name__=='__main__':main()
