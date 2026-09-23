"""Fourier--Motzkin proof packets: eliminate h from exact rational rows.

Rows encode a*U+b*V+c*h<=d. Retain exact deduplicated projected rows.
Each row includes a nonnegative original-row derivation. Completeness follows
from retaining every lower/upper pair and every h-independent row.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def eliminate(rows):
 out={}
 def add(a,b,w):
  # Canonicalize positive multiples without changing inequality orientation.
  scale=next((abs(x) for x in a if x),abs(b) if b else Q(1))
  key=tuple(x/scale for x in a)+(b/scale,)
  out.setdefault(key,[[i,str(v/scale)] for i,v in w])
 for i,r in enumerate(rows):
  if r[2]==0:add(r[:2],r[3],[(i,Q(1))])
 for i,l in enumerate(rows):
  if l[2]>=0:continue
  for j,u in enumerate(rows):
   if u[2]<=0:continue
   wl=Q(1)/(-l[2]);wu=Q(1)/u[2]
   add(tuple(wl*l[k]+wu*u[k] for k in (0,1)),wl*l[3]+wu*u[3],[(i,wl),(j,wu)])
 return [{'row':list(map(str,k)),'weights':w} for k,w in sorted(out.items())]
def fixtures():
 # Source-relative control: exposed x0=h, all other masses zero by U=h.
 # V=U follows from source and is kept explicitly; projecting gives segment.
 yield 'segment',[[1,0,-1,0],[-1,0,1,0],[0,0,-1,0],[0,0,1,1],[1,-1,0,0],[-1,1,0,0]]
 # Nine pair combinations; bounded h and visible square retained. This
 # control reports syntactic expansion, not minimal projected facet count.
 yield 'coupled',[[i,1,-1,2+i] for i in range(3)]+[[1,j,1,5+j] for j in range(3)]+[[1,0,0,3],[-1,0,0,0],[0,1,0,3],[0,-1,0,0]]
def main():
 packets=[]
 for name,raw in fixtures():
  rows=[tuple(map(Q,r)) for r in raw];summary=eliminate(rows)
  encoded=json.dumps(summary,separators=(',',':'))
  packets.append({'name':name,'original':[[str(v) for v in r] for r in rows], 'summary':summary,
   'cost':{'original_rows':len(rows),'summary_rows':len(summary),'original_rational_fields':4*len(rows),
           'summary_rational_fields':3*len(summary),'summary_with_derivations_json_bytes':len(encoded.encode()),
           'original_rows_json_bytes':len(json.dumps([[str(v) for v in r] for r in rows],separators=(',',':')).encode())}})
 (OUT/'certified-linear-audit-elimination.json').write_text(json.dumps({'packets':packets},indent=2)+'\n')
 print(json.dumps([{'name':p['name'],**p['cost']} for p in packets],indent=2))
if __name__=='__main__':main()
