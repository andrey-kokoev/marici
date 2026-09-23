"""Independent exact projection replay: no compiler, greedy engine or LP import."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,gzip,hashlib,copy
if not __debug__:raise RuntimeError('Verification requires assertions enabled')
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def dec(row):return tuple(map(Q,row['normal'])),Q(row['upper'])
cp=R/'audit-elimination-contract.json';contract=json.loads(cp.read_text());packet=json.loads(gzip.decompress((R/'audit-elimination.json.gz').read_bytes()))
assert sha(cp)==packet['contract_sha256']
for p,h in packet['bindings'].items():assert sha(Path(p))==h
assert sha(HERE/'joint_audit_tail_interface.py')==contract['source_binding']
def source(m,audits):
 d=2+len(audits);caps=[Q(100+2*j) for j in range(m)];r=[Q(1,128**j) for j in range(m)];free=[j for j in range(m) if j not in audits]
 def support(a):return sum(caps[j]*max(Q(0),a[0]+a[1]*r[j]+(a[2+audits.index(j)] if j in audits else 0)) for j in range(m))
 def shear(a,b):return (a,b,*[-a-b*r[j] for j in audits])
 rows=[]
 for j in range(d):
  for s in (-1,1):
   a=tuple(Q(s*int(k==j)) for k in range(d));rows.append((a,support(a)))
 for j in range(len(audits)):
  for s in (-1,1):
   a=tuple(Q(s*int(k==j+2)) for k in range(d));rows.append((a,support(a)))
 if len(free)>=2:
  for j in free:
   for s in (-1,1):a=shear(-s*r[j],Q(s));rows.append((a,support(a)))
  for s in (-1,1):a=shear(Q(s),Q(0));rows.append((a,support(a)))
 elif len(free)==1:
  for s in (-1,1):
   a=shear(Q(s),Q(0));rows.append((a,support(a)));rows.append((shear(-s*r[free[0]],Q(s)),Q(0)))
 else:
  for j in (0,1):
   for s in (-1,1):rows.append((shear(Q(s*int(j==0)),Q(s*int(j==1))),Q(0)))
 def observe(t):return (sum(t),dot(r,t),*[t[j] for j in audits])
 return rows,support,observe,caps

def verify_lp(m,audits,frames,c,p):
 _,support,observe,caps=source(m,audits);rows=[dec(row) for row in p['rows']]
 seen=[]
 for row,(a,b) in zip(p['rows'],rows):
  if row['label'].startswith('frame:'):seen.append((row['label'],a,b))
  else:assert support(a)<=b
 assert seen==[(f'frame:{i}',a,b) for i,(a,b) in enumerate(frames)]
 weights=list(map(Q,p['multipliers']));assert len(weights)==len(rows) and all(w>=0 for w in weights)
 normal=tuple(sum(w*a[j] for w,(a,b) in zip(weights,rows)) for j in range(len(c)));upper=sum(w*b for w,(a,b) in zip(weights,rows))
 if p['status']=='INCONSISTENT':assert all(v>=0 for v in normal) and upper<0
 else:
  assert p['status']=='OPTIMUM';t=tuple(map(Q,p['source_lift']));point=tuple(map(Q,p['point']))
  assert len(t)==m and all(0<=x<=b for x,b in zip(t,caps)) and observe(t)==point
  assert all(dot(a,point)<=b for a,b in frames) and all(a>=b for a,b in zip(normal,c))
  assert upper==dot(c,point)==Q(p['value'])

def verify_case(plan,case):
 m=plan['m'];audits=plan['audits'];index=2+audits.index(plan['retire']);base,_,observe,caps=source(m,audits);frames=list(map(dec,plan['frames']));fine=base+frames
 out=case['projection'];assert out['retired_position']==index
 positive=[i for i,(a,b) in enumerate(fine) if a[index]>0];negative=[i for i,(a,b) in enumerate(fine) if a[index]<0];zero=[i for i,(a,b) in enumerate(fine) if a[index]==0]
 recipes=[[(i,Q(1))] for i in zero]+[[(i,1/fine[i][0][index]),(j,-1/fine[j][0][index])] for i in positive for j in negative]
 def combine(recipe):
  assert all(0<=i<len(fine) and w>=0 for i,w in recipe)
  a=tuple(sum(w*fine[i][0][j] for i,w in recipe) for j in range(len(fine[0][0])));b=sum(w*fine[i][1] for i,w in recipe)
  assert a[index]==0;return a[:index]+a[index+1:],b
 raw=list(map(combine,recipes));final=list(map(dec,out['rows']));d=len(final[0][0])
 assert out['counts']['raw_rows']==len(raw)==len(zero)+len(positive)*len(negative)
 assert out['counts']['positive']==len(positive) and out['counts']['negative']==len(negative) and out['counts']['zero']==len(zero)
 assert out['counts']['final_rows']==len(final)
 for row,value in zip(out['rows'],final):assert combine([(i,Q(w)) for i,w in row['origin']])==value
 for j in range(d):assert (tuple(Q(-int(k==j)) for k in range(d)),Q(0)) in final
 assert len(out['raw_implication_indices'])==len(raw)
 for (a,b),i in zip(raw,out['raw_implication_indices']):
  entry=out['implications'][i];assert dec(entry)==(a,b);proof=entry['proof'];weights=list(map(Q,proof['multipliers']))
  assert len(weights)==len(final) and all(w>=0 for w in weights)
  normal=tuple(sum(w*n[j] for w,(n,h) in zip(weights,final)) for j in range(d));upper=sum(w*h for w,(n,h) in zip(weights,final))
  if proof['status']=='INCONSISTENT':assert all(v>=0 for v in normal) and upper<0
  else:assert proof['status'] in ('BOUND','OPTIMUM') and all(v>=u for v,u in zip(normal,a)) and upper<=b
 coarse_audits=[j for j in audits if j!=plan['retire']];_,support,_,_=source(m,coarse_audits)
 base_implied=[];summary=[]
 for i,(a,b) in enumerate(final):
  if support(a)<=b:base_implied.append({'row':i,'source_support':str(support(a))})
  else:summary.append((a,b))
 assert case['base_implied_rows']==base_implied and list(map(dec,case['runtime']['frames']))==summary
 assert case['runtime']['m']==m and case['runtime']['audits']==coarse_audits and case['runtime']['source_binding']==contract['source_binding']
 assert len(case['queries'])==d
 assert [tuple(map(Q,q['objective'])) for q in case['queries']]==[tuple(Q(int(k==j)) for k in range(d)) for j in range(d)]
 for query in case['queries']:
  c=tuple(map(Q,query['objective']));old_c=c[:index]+(Q(0),)+c[index:]
  verify_lp(m,audits,frames,old_c,query['fine_certificate']);verify_lp(m,coarse_audits,summary,c,query['coarse_certificate'])
  assert query['fine_certificate']['status']==query['coarse_certificate']['status']
  if query.get('status')=='INCONSISTENT':assert query['fine_certificate']['status']=='INCONSISTENT';continue
  assert query['fine_certificate']['value']==query['coarse_certificate']['value']==query['value']
  p=tuple(map(Q,query['public']));full=tuple(map(Q,query['fine_point']));assert full[:index]+full[index+1:]==p
  lows=[(b-dot(a[:index]+a[index+1:],p))/a[index] for a,b in fine if a[index]<0];highs=[(b-dot(a[:index]+a[index+1:],p))/a[index] for a,b in fine if a[index]>0]
  assert tuple(map(Q,query['extension_interval']))==(max(lows),min(highs)) and max(lows)<=full[index]<=min(highs)
  assert all(dot(a,full)<=b for a,b in fine)
  t=tuple(map(Q,query['source_lift']));assert observe(t)==full and all(0<=v<=b for v,b in zip(t,caps))
 assert case['ledger']['projection_proof_bytes']==len(json.dumps(out,separators=(',',':')).encode())

assert len(packet['compactions'])==len(contract['plans'])
for plan,case in zip(contract['plans'],packet['compactions']):assert plan['name']==case['name'];verify_case(plan,case)
# The inner box is admitted by its 16 source-interior vertices and convexity.
e=packet['expansion'];_,_,observe,caps=source(4,[0,1]);center=observe(tuple(b/2 for b in caps));delta=Q(1,128**4)
assert tuple(map(Q,e['center']))==center and Q(e['delta'])==delta
assert {tuple(map(Q,c['local'])) for c in e['inner_box_corners']}==set(product((-1,1),(-1,1),(-4,4),(-4,4)))
for corner in e['inner_box_corners']:
 p=tuple(map(Q,corner['joint']));t=tuple(map(Q,corner['source_lift']));local=tuple(map(Q,corner['local']))
 assert p==tuple(a+delta*b for a,b in zip(center,local))==observe(t) and all(0<v<b for v,b in zip(t,caps))
assert [f['n'] for f in e['families']]==contract['expansion_n']
for family in e['families']:
 n=family['n'];knots=[Q(2*i+1-n,n) for i in range(n)];assert list(map(Q,family['knots']))==knots
 expected=[((2*a,2*b,Q(-1)),a*a+b*b) for a in knots for b in knots];assert list(map(dec,family['projected_pair_facets']))==expected
 assert len(set(expected))==n*n and family['projected_facets']==n*n+5 and family['fine_evidence_rows']==2*n+8
 for i,raw in enumerate(family['exclusive_violation_witnesses']):
  p=tuple(map(Q,raw));assert -1<p[0]<1 and -1<p[1]<1 and -4<p[2]<4
  assert dot(expected[i][0],p)>expected[i][1] and all(dot(a,p)<=b for j,(a,b) in enumerate(expected) if i!=j)
 # The true facet centers are strict in every other row and every box wall.
 for i,(a,b) in enumerate(product(knots,knots)):
  p=(a,b,a*a+b*b);assert dot(expected[i][0],p)==expected[i][1]
  assert all(dot(v,p)<h for j,(v,h) in enumerate(expected) if i!=j)
 for p in ((-1,0,3),(1,0,3),(0,-1,3),(0,1,3),(0,0,4),(0,0,3)):
  assert all(dot(a,p)<b for a,b in expected)
# Rejection controls exercise both directions and expected-history binding.
def reject(plan,case):
 try:verify_case(plan,case)
 except (AssertionError,IndexError,KeyError):return
 raise AssertionError('invalid projection certificate accepted')
plan=contract['plans'][0];case=packet['compactions'][0]
bad=copy.deepcopy(case);bad['projection']['rows'][0]['origin'][0][1]='-1';reject(plan,bad)
bad=copy.deepcopy(case);bad['projection']['raw_implication_indices'].pop();reject(plan,bad)
bad=copy.deepcopy(case);bad['runtime']['frames'].pop();reject(plan,bad)
badplan=copy.deepcopy(plan);badplan['frames'].pop();reject(badplan,case)
bad=copy.deepcopy(case);bad['runtime']['audits']=[0];reject(plan,bad)
print('PASS: five exact projection/compaction certificates, both inclusions, witness extension, independent query proofs, quadratic facet families through n=16, five rejection controls')
