"""Full q<=1024 prime-power label census for the fixture-only radial source map."""
import copy,json
from pathlib import Path
ROOT=Path('research/nima')
def primes(n):return [q for q in range(2,n+1) if all(q%d for d in range(2,int(q**0.5)+1))]
def census(cutoff=1024):
 out=[]
 for p in primes(cutoff):
  q=p;m=1
  while q<=cutoff:
   out.append({'id':f'p{p}m{m}','prime':p,'power':m,'shell':q,'grade':f'{m}*log({p})','ordered_pair':[p,m],'theta_label':f'log({q})'})
   q*=p;m+=1
 return out
def validate(xs):
 e=[]
 for key in ('id','ordered_pair','shell','grade','theta_label'):
  vals=[json.dumps(x[key],sort_keys=True) for x in xs]
  if len(vals)!=len(set(vals)):e.append(f'nonfaithful_{key}')
 pairs={(x['prime'],x['power']):x for x in xs}
 if any(x['ordered_pair']!=[p,m] for (p,m),x in pairs.items()):e.append('ordered_pair_not_source_derived')
 if any(x['shell']!=x['prime']**x['power'] for x in xs):e.append('shell_not_prime_power')
 return e
base=census();errors=validate(base);assert errors==[]
for cutoff in (16,64,256):
 small=census(cutoff);assert small==[x for x in base if x['shell']<=cutoff]
h={}
x=copy.deepcopy(base);x[1]['grade']=x[0]['grade'];h['collapsed_grade']=validate(x);assert 'nonfaithful_grade' in h['collapsed_grade']
x=copy.deepcopy(base);x[1]['ordered_pair']=x[0]['ordered_pair'];h['collapsed_ordered_pair']=validate(x);assert 'nonfaithful_ordered_pair' in h['collapsed_ordered_pair']
x=copy.deepcopy(base);x[1]['shell']=x[0]['shell'];h['collapsed_shell']=validate(x);assert 'nonfaithful_shell' in h['collapsed_shell']
x=copy.deepcopy(base);x[1]['theta_label']=x[0]['theta_label'];h['collapsed_theta']=validate(x);assert 'nonfaithful_theta_label' in h['collapsed_theta']
out={'schema':'marici.full-prime-power-radial-source-fixture.v1','status':'passed','cutoff':1024,'prime_power_count':len(base),'first':base[0],'last':base[-1],'cutoff_naturality_checked':[16,64,256,1024],'hostile_results':h,'reciprocal_poles':{'pole_2':'pole_half','pole_half':'pole_2'},'remaining_semantic_gap':'the faithful finite label map targets only a synthetic radial carrier; no G4 declaration identifies that target','claim_boundary':'finite source-label census and fixture conformance only'}
(ROOT/'results/full-prime-power-radial-source-fixture.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
