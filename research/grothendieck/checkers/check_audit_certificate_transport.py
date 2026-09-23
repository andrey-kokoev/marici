"""No-solver proof transport on admitted joint certificates and envelope families."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,subprocess,sys
from audit_certificate_transport import transport,expand
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(gzip.decompress(p.read_bytes())) if p.suffix=='.gz' else json.loads(p.read_text())
# This replay validates source rows, expected history, signed/axis objectives,
# source witnesses and all input primal/dual/Farkas identities without a solver.
subprocess.run([sys.executable,str(HERE/'verify_audit_elimination.py')],check=True)
up=load(R/'audit-elimination.json.gz');uc=load(R/'audit-elimination-contract.json')
contract={'schema':'audit-certificate-transport-contract.v1','upstream_packet_sha256':sha(R/'audit-elimination.json.gz'),'upstream_contract_sha256':sha(R/'audit-elimination-contract.json'),'families':[2,3,4,8,16,64,256],'repair_controls':['OPTIMUM','INCONSISTENT'],'composition':{'n':16,'indices':[2,0,0]},'scope':'supported joint inequality proofs and exact normalized-envelope row combinations; no native-to-source fallback coercion; no optimization calls'}
cp=R/'audit-certificate-transport-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def row(a,b):return {'normal':list(map(str,a)),'upper':str(b)}
def decode(rows):return [(tuple(map(Q,r['normal'])),Q(r['upper'])) for r in rows]
def move(rows,weights,index,repair):
 answer=transport(rows,weights,index,repair);restored=expand(rows,index,answer['terms']);expected=list(map(Q,weights))
 if answer['repair']:expected[answer['repair']['row']]+=Q(answer['repair']['weight'])
 assert restored==expected
 return answer
cases=[]
for si,(plan,case) in enumerate(zip(uc['plans'],up['compactions'])):
 index=2+plan['audits'].index(plan['retire'])
 for qi,q in enumerate(case['queries']):
  certificate=q['fine_certificate'];rows=decode(certificate['rows']);answer=move(rows,certificate['multipliers'],index,True)
  cases.append({'scenario_index':si,'query_index':qi,'status':certificate['status'],'statement_sha256':digest({'source_packet':contract['upstream_packet_sha256'],'plan':plan,'query_index':qi,'objective':q['objective'],'input_certificate':certificate}),'transport':answer})
repairs=[]
for status in contract['repair_controls']:
 rows=[]
 for j,b in enumerate((Q(306),Q(100)+Q(102,128)+Q(104,16384),Q(100))):
  for sign in (-1,1):rows.append((tuple(Q(sign*int(k==j)) for k in range(3)),b if sign>0 else Q(0)))
 rows.append(((Q(0),Q(0),Q(1)),Q(0 if status=='OPTIMUM' else -1)))
 weights=[Q(0)]*6+[Q(1)];answer=move(rows,weights,2,True)
 repairs.append({'m':3,'audits':[0],'status':status,'rows':[row(a,b) for a,b in rows],'weights':list(map(str,weights)),'transport':answer})
def family_rows(n):
 knots=[Q(2*i+1-n,n) for i in range(n)];rows=[]
 for a in knots:rows.append(((2*a,Q(0),Q(-1),Q(0)),a*a))
 for a in knots:rows.append(((Q(0),2*a,Q(1),Q(-1)),a*a))
 for j,b in enumerate((1,1,4,4)):
  for sign in (-1,1):rows.append((tuple(Q(sign*int(k==j)) for k in range(4)),Q(b)))
 return rows
families=[]
for n in contract['families']:
 rows=family_rows(n);weights=[1+Q(1,2*n)]*(n-1)+[1-Q(n-1,2*n)]+[Q(1)]*n+[Q(0)]*8
 answer=move(rows,weights,2,False);assert len(answer['terms'])==2*n-1
 families.append({'n':n,'weights':list(map(str,weights)),'transport':answer,'potential_pair_rows':(n+1)**2,'evidence_pair_facets':n*n})
# An independently specified dense pair proof is valid reverse input, not
# merely the syntax produced by the forward greedy mass matching.
n=16;rows=family_rows(n);terms=[{'kind':'pair','positive':n+j,'negative':i,'weight':'1'} for i in range(n) for j in range(n)]
weights=expand(rows,2,terms);repacked=move(rows,weights,2,False);assert len(repacked['terms'])==n
reverse={'n':n,'input_terms':terms,'expanded_weights':list(map(str,weights)),'repacked':repacked}
# Compose on proof rows only, not on an alleged complete projected state.
rows=family_rows(16);weights=[Q(1)]*32+[Q(0)]*8;stages=[]
for index in contract['composition']['indices']:
 answer=move(rows,weights,index,False);stages.append(answer);new_rows=[];new_weights=[]
 for term in answer['terms']:
  if term['kind']=='zero':a,b=rows[term['row']]
  else:
   i=term['positive'];j=term['negative'];ai,bi=rows[i];aj,bj=rows[j];ci=ai[index];cj=aj[index]
   a=tuple(x/ci-y/cj for x,y in zip(ai,aj));b=bi/ci-bj/cj
  assert a[index]==0;new_rows.append((a[:index]+a[index+1:],b));new_weights.append(Q(term['weight']))
 rows,weights=new_rows,new_weights
composition={'stages':stages,'final_normal':str(sum(w*a[0] for w,(a,b) in zip(weights,rows))),'final_upper':str(sum(w*b for w,(a,b) in zip(weights,rows)))}
out={'schema':'audit-certificate-transport-result.v1','contract_sha256':sha(cp),'joint_cases':cases,'repair_cases':repairs,'families':families,'reverse_control':reverse,'composition':composition,'bindings':{str(p):sha(p) for p in (Path(__file__),HERE/'audit_certificate_transport.py',cp,R/'audit-elimination.json.gz',R/'audit-elimination-contract.json')},'counts':{'joint_certificates':len(cases),'repair_certificates':len(repairs),'families':len(families),'largest_projected_proof':len(families[-1]['transport']['terms']),'largest_evidence_pair_dictionary':families[-1]['evidence_pair_facets']}}
(R/'audit-certificate-transport.json.gz').write_bytes(gzip.compress(json.dumps(out,separators=(',',':')).encode(),mtime=0))
print(out['counts'])
