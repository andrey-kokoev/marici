"""Exact-pin audit placement and residual conditioning on the owning boxes."""
from pathlib import Path
from fractions import Fraction as Q
from bisect import bisect_right
import sys,subprocess,json,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];R=HERE.parent/'results';ND=ROOT/'nima/checkers'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
subprocess.run([sys.executable,str(HERE/'verify_two_moment_tail_complexity.py')],check=True)
subprocess.run([sys.executable,str(ND/'verify_audited_tail_section.py')],check=True)
sys.path.insert(0,str(ND));from check_audited_tail_section import AuditedGenerator
contract={'schema':'audit-conditioning-design.v1','source':'owning normalized bounded-atom tail faces and actual AuditedGenerator','source_norm':'L1 on source coordinates; exact pins do not move','input_norm':'absolute |delta U|+|delta V| with pin values held EXACTLY fixed','m_values':[3,4,6,8,10],'optimization':'exact best unavoidable vertical constant over all audit sets at each cardinality; globally within additive one via conditional greedy section; exact global optimization when at most two coordinates remain free','boundary':'No noisy-pin model, no claim that more audits monotonically improve stability, and no claim of a polynomial-time design algorithm.'}
cp=R/'audit-conditioning-design-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
def model(free):
 caps=[Q(100+2*j) for j in free];slopes=[Q(1,128**j) for j in free];C=[Q(0)];W=[Q(0)]
 for b,r in zip(caps,slopes):C.append(C[-1]+b);W.append(W[-1]+b*r)
 def greedy(U):
  k=bisect_right(C,U)-1;p=U-C[k];value=W[k]+(p*slopes[k] if k<len(free) else 0)
  vector=[b if j<k else p if j==k else Q(0) for j,b in enumerate(caps)]
  return value,vector
 return caps,slopes,C,W,greedy
records=[];summaries=[];runtime=[]
for m in contract['m_values']:
 start=len(records);by_budget={k:[] for k in range(m+1)}
 for mask in range(2**m):
  free=[j for j in range(m) if not (mask>>j&1)];q=len(free);caps,slopes,C,W,greedy=model(free);T=C[-1]
  if q==0:lower=upper=Q(0);where=None;kind='point'
  elif q==1:lower=upper=1/(1+slopes[0]);where=None;kind='one_free_exact'
  else:
   k=sum(C[j]<=T-C[j+1] for j in range(q));mass=C[k]
   def ratio(U):
    width=greedy(U)[0]-(W[-1]-greedy(T-U)[0]);assert width>0
    distance=2*(min(U,mass)-max(Q(0),U-(T-mass)))
    return distance/width
   candidates=[(2/(slopes[0]-slopes[-1]),Q(0))]+[(ratio(U),U) for U in sorted(set(C)|{T-z for z in C}) if 0<U<T]
   lower,where=max(candidates)
   upper=max(lower,1+slopes[0]*lower)
   kind='vertical_exact_global_sandwich'
   if q==2:
    assert lower==2/(slopes[0]-slopes[-1]);upper=lower;kind='two_free_exact'
   if free[0]>=1:assert upper==lower
  record={'m':m,'audit_mask':mask,'free':free,'audit_count':m-q,'unavoidable_lower':str(lower),'greedy_upper':str(upper),'maximizing_mass_or_tip':None if where is None else str(where),'case':kind}
  by_budget[m-q].append(len(records));records.append(record)
 for budget,indices in by_budget.items():
  best=min(indices,key=lambda i:(Q(records[i]['unavoidable_lower']),records[i]['free']))
  worst=max(indices,key=lambda i:Q(records[i]['unavoidable_lower']))
  q=m-budget;win=records[best]
  if q==2:assert win['free']==[0,m-1]
  if q==1:assert win['free']==[0]
  summaries.append({'m':m,'audit_count':budget,'best_record':best,'worst_record':worst,'design_lower':win['unavoidable_lower'],'design_upper':win['greedy_upper']})
  # Exercise the actual audit-aware API for both optimal and worst placements.
  for index in sorted({best,worst}):
   rr=records[index];free=rr['free'];pins=[(j,Q(100+2*j,3)) for j in range(m) if j not in free];G=AuditedGenerator(m,pins)
   caps,slopes,C,W,greedy=model(free);T=C[-1];U=T/2
   high,hi=greedy(U);comp,co=greedy(T-U);low=W[-1]-comp;lo=[b-v for b,v in zip(caps,co)]
   V=low+(high-low)/3
   offset=(sum(v for j,v in pins),sum(v*Q(1,128**j) for j,v in pins));point=(offset[0]+U,offset[1]+V)
   answer=G.section(point);assert answer['residual_membership']['admitted']
   dense=[G.coordinate(answer,j) for j in range(m)]
   assert all(dense[j]==h for j,h in pins) and sum(dense)==point[0] and sum(v*Q(1,128**j) for j,v in enumerate(dense))==point[1]
   assert [dense[j] for j in free]==[(2*a+b)/3 for a,b in zip(lo,hi)]
   runtime.append({'record':index,'point':list(map(str,point)),'section':answer,'source_lift':list(map(str,dense))})
# A certified monotonicity failure in the same metrics: pinning only atom 0
# changes m=3 from a global upper <4 to the exact free-pair constant >258.
before=next(i for i,r in enumerate(records) if r['m']==3 and r['audit_mask']==0)
after=next(i for i,r in enumerate(records) if r['m']==3 and r['audit_mask']==1)
assert Q(records[after]['unavoidable_lower'])>Q(records[before]['greedy_upper'])
out={'schema':'audit-conditioning-design-result.v1','contract_sha256':sha(cp),'records':records,'budgets':summaries,'runtime_controls':runtime,'nonmonotonicity':{'before_record':before,'after_record':after,'strict_ratio_lower':str(Q(records[after]['unavoidable_lower'])/Q(records[before]['greedy_upper']))},'bindings':{str(p):sha(p) for p in (Path(__file__),cp,ND/'check_audited_tail_section.py',ND/'check_symbolic_tail_interface.py',R/'two-moment-tail-complexity.json')},'status':'EXACT_AUDIT_PLACEMENT_SANDWICHES_AND_NONMONOTONICITY','scope':'Global optimal placements are exact only in the declared low-dimensional cases; otherwise the optimized vertical bound gives an additive-one global design guarantee.'}
(R/'audit-conditioning-design.json').write_text(json.dumps(out,indent=2)+'\n')
print('Audit sets:',len(records),'budgets:',len(summaries),'actual API checks:',len(runtime))
print('m=3 pin-first instability:',records[before]['greedy_upper'],records[after]['unavoidable_lower'])
