"""Relative interval residue: exact transport, gauge change and obstruction.
A residue here is two-sided fiber slack, NOT a differential residue jet.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from verify_scalar_envelope_band import envelopes,value,domain
OUT=ROOT/'research/voevodsky/results'
def residue(lo,hi,s):
 assert lo<=hi
 return (s-lo,hi-s)
def decode(s,r):return s-r[0],s+r[1]
def change_base(s,r,t):return (r[0]+t-s,r[1]-(t-s))
def append(s,r,lo,hi):
 if r is None:return None
 a,b=min(r[0],s-lo),min(r[1],hi-s)
 return None if a+b<0 else (a,b)
def center(s,r):
 if r is None:return (None,None)
 t=s+(r[1]-r[0])/2
 return t,change_base(s,r,t)
def replay(lo,hi,s,operations,recenter):
 r=residue(lo,hi,s)
 for a,b in operations:
  r=append(s,r,a,b)
  if r is None:return (None,None)
  if recenter:s,r=center(s,r)
 return center(s,r)
def encoded(result):
 s,r=result
 return {'empty':True} if r is None else {'base':str(s),'slacks':list(map(str,r)),'interval':list(map(str,decode(s,r)))}
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 values=[Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]
 intervals=[(a,b) for a,b in product(values,repeat=2) if a<=b]
 checks=0;shift_checks=0
 for lo,hi in intervals:
  # The base may cease to be admitted: signed slacks still encode the fiber.
  for s in values:
   r=residue(lo,hi,s);assert decode(s,r)==(lo,hi)
   for t in values:
    assert decode(t,change_base(s,r,t))==(lo,hi);shift_checks+=1
   for f,g in product(intervals,repeat=2):
    direct=replay(lo,hi,s,[(max(f[0],g[0]),min(f[1],g[1]))],False)
    staged=replay(lo,hi,s,[f,g],True);permuted=replay(lo,hi,s,[g,f],True)
    assert direct==staged==permuted;checks+=1
    expected=(max(lo,f[0],g[0]),min(hi,f[1],g[1]))
    if expected[0]>expected[1]:assert staged==(None,None)
    else:assert decode(*staged)==expected
 # Selector failure != fiber emptiness: start at h=1, then require h<=1/2.
 old=residue(Q(0),Q(1),Q(1));changed=append(Q(1),old,Q(0),Q(1,2))
 assert changed==(Q(1),Q(-1,2)) and sum(changed)>0
 assert center(Q(1),changed)==(Q(1,4),(Q(1,4),Q(1,4)))
 # Projecting each fine refinement separately loses their common-witness requirement.
 assert append(Q(1,2),residue(Q(0),Q(1),Q(1,2)),Q(0),Q(1,4)) is not None
 assert append(Q(1,2),residue(Q(0),Q(1),Q(1,2)),Q(3,4),Q(1)) is not None
 assert replay(Q(0),Q(1),Q(1,2),[(Q(0),Q(1,4)),(Q(3,4),Q(1))],True)==(None,None)
 # Owning envelope checks at real public vertices; all-domain law is pointwise algebra.
 lower,upper=envelopes(18);controls=[]
 for p in domain(18):
  f=max(value(a,p) for a in lower);g=min(value(a,p) for a in upper)
  for history,interval in [('A',(f,Q(1))),('B',(Q(0),g))]:
   out=replay(*interval,(f+g)/2,[(Q(0),Q(1,2)),(Q(1,4),Q(1))],True)
   controls.append({'point':list(map(str,p)),'history':history,'result':encoded(out)})
 # Minimality for the interval contract: unequal endpoints are distinguished
 # by a rational threshold strictly between them.
 distinctions=0
 for a,b in product(intervals,repeat=2):
  if a==b:continue
  if a[0]!=b[0]:
   q=(a[0]+b[0])/2;assert (a[0]<=q)!=(b[0]<=q)
  else:
   q=(a[1]+b[1])/2;assert (a[1]>=q)!=(b[1]>=q)
  distinctions+=1
 report={'passed':True,'two_refinement_comparisons':checks,'base_changes':shift_checks,
 'interval_distinctions':distinctions,'owning_vertex_controls':controls,
 'signed_slack_control':{'base':'1','slacks_after_upper_half':['1','-1/2'],
 'meaning':'old selector invalid, refined fiber still [0,1/2]'},
 'common_witness_obstruction':{'interval':'[0,1]','individual_refinements':['h<=1/4','h>=3/4'],
 'each_nonempty':True,'joint_empty':True,'farkas_upper':'-1/2'},
 'scope':'Exact minimal semantic descriptor for bounded scalar intervals under arbitrary rational threshold continuations. No minimal bit encoding or general residue-jet claim.'}
 (OUT/'relative-fiber-residue.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ('passed','two_refinement_comparisons','base_changes','interval_distinctions')},indent=2))
if __name__=='__main__':main()
