"""Exact edge expansion and conductance on the seven original 17-vertex red cores. One representative per cut by requiring vertex 16 outside. Include ties via rational comparisons."""
import json
from fractions import Fraction
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';out=[]
for row,r in enumerate(json.loads((P/'ramsey_frozen_gain_control.json').read_text())[1]):
 a=r['core'];n=len(a);deg=[v.bit_count() for v in a];total=sum(deg);cuts=[0]*(1<<(n-1));vol=cuts.copy();best=[None,None];examples=[None,None]
 for s in range(1,len(cuts)):
  bit=s&-s;t=s^bit;i=bit.bit_length()-1;cuts[s]=cuts[t]+deg[i]-2*(a[i]&t).bit_count();vol[s]=vol[t]+deg[i];size=s.bit_count()
  for j,den in enumerate((min(size,n-size),min(vol[s],total-vol[s]))):
   b=best[j]
   if b is None or cuts[s]*b.denominator<b.numerator*den:best[j]=Fraction(cuts[s],den);examples[j]=s
 out.append(dict(row=row,score=r['score'],endpoint=r['order'],h=str(best[0]),phi=str(best[1]),masks=examples));print(row,r['order'],*best)
(P/'ramsey_expansion17.json').write_text(json.dumps(out)+'\n')
