#!/usr/bin/env python3
"""Exact finite-n defect between four forced-channel traces and the full Catalan trace."""
import json,math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def C(m):return math.comb(2*m,m)//(m+1)
rows=[]
for n in range(4,101):
 m=n-2;full=C(m);sector=C(m-1);defect=4*sector-full
 assert defect* (n-1)==6*sector
 relative=Fraction(defect,full);assert relative==Fraction(3,2*n-5)
 rows.append({'n':n,'full_rank':full,'one_sector_rank':sector,'four_sector_rank_sum':4*sector,'finite_overlap_defect':defect,'relative_defect_numerator':relative.numerator,'relative_defect_denominator':relative.denominator,'relative_defect_decimal':float(relative)})
checks={'defect_positive_at_every_finite_n':all(x['finite_overlap_defect']>0 for x in rows),'relative_defect_strictly_decreases':all(rows[i+1]['relative_defect_decimal']<rows[i]['relative_defect_decimal'] for i in range(len(rows)-1)),'relative_defect_tends_numerically_to_zero':rows[-1]['relative_defect_decimal']<.016}
out={'schema':'marici.nima.four-chart-catalan-trace-defect.v1','range':[4,100],'identities':['4 C_(n-3)-C_(n-2)=6 C_(n-3)/(n-1)','(4 C_(n-3)-C_(n-2))/C_(n-2)=3/(2n-5)'],'sample_rows':rows[:5]+rows[28:31]+rows[-3:],'checks':checks,'passed':all(checks.values()),'interpretation':'Four equal forced-channel sectors cannot form a disjoint finite-n chart partition; their rank sum exceeds the full Catalan rank by a boundary-scale defect whose normalized weight vanishes.'}
p=ROOT/'research/nima/results/four-chart-catalan-trace-defect.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'identities':out['identities'],'n33':rows[29],'n100':rows[-1]},indent=2));raise SystemExit(0 if out['passed'] else 1)
