"""Exact conditional inverse conditioning in the owning audit-aware section."""
from pathlib import Path
from fractions import Fraction as Q
import sys,json
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_audited_tail_section import AuditedGenerator
OUT=ROOT/'research/voevodsky/results'
def obs(x):return sum(x),sum(v*Q(1,128**j) for j,v in enumerate(x))
def norm(x):return sum(map(abs,x))
def reconstruct(x,free):
 g=AuditedGenerator(len(x),[(j,v) for j,v in enumerate(x) if j not in free])
 packet=g.section(obs(x));assert packet['residual_membership']['admitted']
 y=tuple(g.coordinate(packet,j) for j in range(len(x)))
 assert y==x
 return y
records=[]
for m in (3,4,8,16,64,256):
 p,q=m-2,m-1
 x=tuple(Q(100+2*j,2) for j in range(m))
 y=list(x);y[p]+=1;y[q]-=1;y=tuple(y)
 reconstruct(x,{p,q});reconstruct(y,{p,q})
 dx=tuple(b-a for a,b in zip(x,y));do=tuple(b-a for a,b in zip(obs(x),obs(y)))
 actual=norm(dx)/norm(do);expected=Q(2*128**(m-1),127)
 assert actual==expected
 # The one-free residual segment is stable in the SAME observable norm.
 z=list(x);z[q]+=1;z=tuple(z)
 reconstruct(x,{q});reconstruct(z,{q})
 one=Q(1)/(1+Q(1,128**q))
 assert norm(tuple(b-a for a,b in zip(x,z)))/norm(tuple(b-a for a,b in zip(obs(x),obs(z))))==one
 # Compare with the proved global upper bound for the unpinned greedy section.
 full_upper=1+Q(128*m*(m+99),12700)
 assert expected>full_upper
 records.append({'m':m,'free_indices':[p,q],'exact_two_free_constant':str(expected),
  'one_free_constant':str(one),'unpinned_section_upper_bound':str(full_upper)})
report={'passed':True,'norms':'Source L1; observable |delta U|+|delta V|; audited values held exactly fixed.',
 'records':records,'conclusion':'Two free final slopes force exponential conditional sensitivity, despite the polynomial upper bound for the unpinned section. One additional pin leaves a stable segment inverse.',
 'scope':'Exact source-admitted implementation controls plus affine inverse proof; not a noisy-audit-input or bit-complexity bound.'}
(OUT/'audit-conditioning.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'m_values':[r['m'] for r in records],'conclusion':report['conclusion']},indent=2))
