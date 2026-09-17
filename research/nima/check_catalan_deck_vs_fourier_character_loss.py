#!/usr/bin/env python3
"""Quantify character loss when a C4 Catalan action is collapsed to deck parity C2."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def C(m):return math.comb(2*m,m)//(m+1)
rows=[]
for n in range(4,101,4):
 d=C(n-2);h=math.comb(n-2,(n-2)//2);m0=m2=(d+h)//4;m1=m3=(d-h)//4;odd=m1+m3
 rows.append({'n':n,'dimension':d,'multiplicities':[m0,m1,m2,m3],'odd_fourier_characters_lost_by_c2_collapse':odd,'lost_fraction':odd/d,'retained_fraction':1-odd/d})
checks={'multiplicities_integral':all(sum(x['multiplicities'])==x['dimension'] for x in rows),'odd_loss_approaches_half':abs(rows[-1]['lost_fraction']-.5)<1e-10,'finite_loss_positive':all(x['odd_fourier_characters_lost_by_c2_collapse']>0 for x in rows[1:])}
out={'schema':'marici.nima.catalan-deck-vs-fourier-character-loss.v1','range':[4,100,4],'results':rows[:3]+rows[7:9]+rows[-3:],'checks':checks,'passed':all(checks.values()),'statement':'A target retaining only q^2/deck parity cannot faithfully realize the C4 Catalan module: it loses the j=1,3 character sectors, asymptotically half the module.'}
p=ROOT/'research/nima/results/catalan-deck-vs-fourier-character-loss.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'n12':rows[2],'n100':rows[-1]},indent=2));raise SystemExit(0 if out['passed'] else 1)
