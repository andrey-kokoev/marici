"""Independent mass-conservation replay; imports no transporter or optimizer."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,runpy,copy
if not __debug__:raise RuntimeError('Verification requires assertions enabled')
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(gzip.decompress(p.read_bytes())) if p.suffix=='.gz' else json.loads(p.read_text())
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def decode(rows):return [(tuple(map(Q,r['normal'])),Q(r['upper'])) for r in rows]
packet=load(R/'audit-certificate-transport.json.gz');cp=R/'audit-certificate-transport-contract.json';contract=load(cp)
assert sha(cp)==packet['contract_sha256']
for p,h in packet['bindings'].items():assert sha(Path(p))==h
assert sha(R/'audit-elimination.json.gz')==contract['upstream_packet_sha256'] and sha(R/'audit-elimination-contract.json')==contract['upstream_contract_sha256']
# This verifier is itself solver-free and checks the independently expected
# source/schema/history and axis queries of every input proof.
upstream=runpy.run_path(str(HERE/'verify_audit_elimination.py'));up=upstream['packet'];uc=upstream['contract']

def unpack(rows,index,terms):
 weights=[Q(0)]*len(rows);public=[Q(0)]*(len(rows[0][0])-1);upper=Q(0)
 for term in terms:
  mass=Q(term['weight']);assert mass>0
  if term['kind']=='zero':
   i=term['row'];assert rows[i][0][index]==0;recipe=[(i,mass)]
  else:
   assert term['kind']=='pair';i=term['positive'];j=term['negative'];ci=rows[i][0][index];cj=rows[j][0][index];assert ci>0>cj
   recipe=[(i,mass/ci),(j,-mass/cj)]
  for i,w in recipe:
   assert 0<=i<len(rows);weights[i]+=w;a,b=rows[i];a=a[:index]+a[index+1:]
   public=[v+w*x for v,x in zip(public,a)];upper+=w*b
 return weights,tuple(public),upper

def check(rows,weights,index,out,allow_repair):
 weights=list(map(Q,weights));assert len(weights)==len(rows) and all(w>=0 for w in weights)
 assert out['retired_position']==index;normalized=weights[:];beta=sum(w*a[index] for w,(a,b) in zip(weights,rows));repair=out['repair']
 if beta==0:assert repair is None
 else:
  assert allow_repair and beta>0 and repair is not None
  i=repair['row'];assert Q(repair['weight'])==beta and rows[i]==(tuple(Q(-int(j==index)) for j in range(len(rows[0][0]))),Q(0));normalized[i]+=beta
 restored,public,upper=unpack(rows,index,out['terms']);assert restored==normalized
 assert sum(w*a[index] for w,(a,b) in zip(restored,rows))==0
 assert upper==sum(w*b for w,(a,b) in zip(weights,rows))
 expected=tuple(sum(w*a[j] for w,(a,b) in zip(weights,rows)) for j in range(len(rows[0][0])) if j!=index);assert public==expected
 k=sum(w!=0 for w in weights);kn=sum(w!=0 for w in normalized);p=sum(w!=0 and a[index]>0 for w,(a,b) in zip(normalized,rows));n=sum(w!=0 and a[index]<0 for w,(a,b) in zip(normalized,rows))
 assert out['counts']=={'input_nonzero':k,'normalized_nonzero':kn,'positive_nonzero':p,'negative_nonzero':n,'projected_nonzero':len(out['terms'])}
 assert len(out['terms'])<=kn-(1 if p else 0) and len(out['terms'])<=k
 return public,upper

expected=[(si,qi) for si,case in enumerate(up['compactions']) for qi in range(len(case['queries']))]
assert [(c['scenario_index'],c['query_index']) for c in packet['joint_cases']]==expected
for case in packet['joint_cases']:
 si=case['scenario_index'];qi=case['query_index'];plan=uc['plans'][si];query=up['compactions'][si]['queries'][qi];old=query['fine_certificate'];index=2+plan['audits'].index(plan['retire'])
 assert case['statement_sha256']==digest({'source_packet':contract['upstream_packet_sha256'],'plan':plan,'query_index':qi,'objective':query['objective'],'input_certificate':old})
 assert case['status']==old['status'];normal,bound=check(decode(old['rows']),old['multipliers'],index,case['transport'],True)
 if case['status']=='INCONSISTENT':assert all(v>=0 for v in normal) and bound<0
 else:
  c=tuple(map(Q,query['objective']));point=tuple(map(Q,old['point']));public=point[:index]+point[index+1:]
  assert all(v>=u for v,u in zip(normal,c)) and dot(c,public)==bound==Q(old['value'])
  # The old admitted source witness proves membership in the exact projection.
  audits=[j for j in plan['audits'] if j!=plan['retire']];observe=upstream['source'](plan['m'],audits)[2]
  assert observe(tuple(map(Q,old['source_lift'])))==public

assert [c['status'] for c in packet['repair_cases']]==contract['repair_controls']
for case in packet['repair_cases']:
 rows=[]
 for j,b in enumerate((Q(306),Q(100)+Q(102,128)+Q(104,16384),Q(100))):
  for sign in (-1,1):rows.append((tuple(Q(sign*int(k==j)) for k in range(3)),b if sign>0 else Q(0)))
 rows.append(((Q(0),Q(0),Q(1)),Q(0 if case['status']=='OPTIMUM' else -1)))
 assert decode(case['rows'])==rows and list(map(Q,case['weights']))==[Q(0)]*6+[Q(1)]
 normal,bound=check(rows,case['weights'],2,case['transport'],True);assert normal==(0,0) and bound==rows[-1][1]
 if case['status']=='OPTIMUM':assert all(dot(a,(Q(0),)*3)<=b for a,b in rows) and bound==0
 else:assert bound<0

def family(n):
 knots=[Q(2*i+1-n,n) for i in range(n)];rows=[((2*a,Q(0),Q(-1),Q(0)),a*a) for a in knots]+[((Q(0),2*a,Q(1),Q(-1)),a*a) for a in knots]
 for j,b in enumerate((1,1,4,4)):
  for sign in (-1,1):rows.append((tuple(Q(sign*int(k==j)) for k in range(4)),Q(b)))
 assert all(dot(a,(Q(0),Q(0),Q(0),Q(3)))<=b for a,b in rows)
 return rows
assert [f['n'] for f in packet['families']]==contract['families']
for case in packet['families']:
 n=case['n'];rows=family(n);weights=[1+Q(1,2*n)]*(n-1)+[1-Q(n-1,2*n)]+[Q(1)]*n+[Q(0)]*8
 assert list(map(Q,case['weights']))==weights and case['potential_pair_rows']==(n+1)**2 and case['evidence_pair_facets']==n*n
 check(rows,weights,2,case['transport'],False);assert len(case['transport']['terms'])==2*n-1
rev=packet['reverse_control'];assert rev['n']==16;rows=family(16)
assert rev['input_terms']==[{'kind':'pair','positive':16+j,'negative':i,'weight':'1'} for i in range(16) for j in range(16)]
weights,normal,bound=unpack(rows,2,rev['input_terms']);assert weights==list(map(Q,rev['expanded_weights']))==[Q(16)]*32+[Q(0)]*8
new_normal,new_bound=check(rows,weights,2,rev['repacked'],False);assert (normal,bound)==(new_normal,new_bound) and len(rev['repacked']['terms'])==16

assert contract['composition']=={'n':16,'indices':[2,0,0]}
rows=family(16);weights=[Q(1)]*32+[Q(0)]*8
assert len(packet['composition']['stages'])==3
for index,out in zip(contract['composition']['indices'],packet['composition']['stages']):
 check(rows,weights,index,out,False);next_rows=[];next_weights=[]
 for term in out['terms']:
  # Recover the one projected row separately from its external multiplier.
  unit=dict(term,weight='1');_,normal,bound=unpack(rows,index,[unit]);next_rows.append((normal,bound));next_weights.append(Q(term['weight']))
 rows,weights=next_rows,next_weights
assert Q(packet['composition']['final_normal'])==sum(w*a[0] for w,(a,b) in zip(weights,rows))==-16
assert Q(packet['composition']['final_upper'])==sum(w*b for w,(a,b) in zip(weights,rows))==Q(85,8)

def reject(rows,weights,index,out,repair):
 try:check(rows,weights,index,out,repair)
 except (AssertionError,IndexError,KeyError):return
 raise AssertionError('invalid transported certificate accepted')
case=packet['families'][1];rows=family(case['n']);weights=case['weights']
bad=copy.deepcopy(case['transport']);bad['terms'][0]['weight']='-1';reject(rows,weights,2,bad,False)
bad=copy.deepcopy(case['transport']);bad['terms'].pop();reject(rows,weights,2,bad,False)
bad=copy.deepcopy(case['transport']);bad['terms'][0]['positive'],bad['terms'][0]['negative']=bad['terms'][0]['negative'],bad['terms'][0]['positive'];reject(rows,weights,2,bad,False)
bad=copy.deepcopy(case['transport']);bad['retired_position']=1;reject(rows,weights,2,bad,False)
case=packet['repair_cases'][1];rows=decode(case['rows'])
bad=copy.deepcopy(case['transport']);bad['repair']=None;reject(rows,case['weights'],2,bad,True)
bad=copy.deepcopy(case['transport']);bad['repair']['weight']='2';reject(rows,case['weights'],2,bad,True)
bad=copy.deepcopy(case['transport']);bad['repair']['row']=5;reject(rows,case['weights'],2,bad,True)
print('PASS: 12 joint proofs, two explicit nonnegativity repairs, seven sparse envelope transports through n=256, independent reverse proof, three composed eliminations and seven rejection controls; no optimizer invoked')
