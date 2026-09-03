"""Exhaustive DPC search for support-three raw probes at A14."""
import json,sys
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_collapse_relation_sector as s
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_three_coordinate_raw_probe_DPC.json'
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def solve(v0,v1,v2):
 rows=sorted(set(v0)|set(v1)|set(v2));pivot=None
 for r,u in combinations(rows,2):
  D=v1.get(r,0)*v2.get(u,0)-v2.get(r,0)*v1.get(u,0)
  if D:pivot=(r,u,Fraction(D));break
 if pivot is None:return None
 r,u,D=pivot;a=( -v0.get(r,0)*v2.get(u,0)+v2.get(r,0)*v0.get(u,0))/D;b=(-v1.get(r,0)*v0.get(u,0)+v0.get(r,0)*v1.get(u,0))/D
 return (a,b) if all(v0.get(i,0)+a*v1.get(i,0)+b*v2.get(i,0)==0 for i in rows) else None
def main():
 oldA=s.rees.AMBIENT;oldp=s.base.PRIME;s.rees.AMBIENT=14
 try:
  _,cols=s.rees.column_packet();inv={i:l for l,i in cols.items()};ibp,K,q=s.tr.descs(14);alls=ibp+K+q;nK=len(K);descs=alls+K+q;grades=[s.clf.grade(d) for d in descs];point=tuple(json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text())['test_point_xyz']);pack={}
  for p in s.ex.PS:
   s.base.PRIME=p;raw=list(s.rees.raw_relations(point,cols));T,_=s.adapter.derivative_rows(cols,point,(1,-1,0));D2,_=s.adapter.derivative_rows(cols,point,(3,0,-1));pack[p]={'source':T+raw[len(ibp):len(ibp)+nK]+raw[len(ibp)+nK:],'target':D2}
  s.base.PRIME=oldp;source=[s.ex.exact_row([pack[p]['source'][i] for p in s.ex.PS]) for i in range(len(descs)) if grades[i]<=8];data=json.loads((RES/'cosmology_filtered_classification_transport.json').read_text());rec=next(x for x in data['A14_transports'] if x['grade']==8 and x['axis_square']=='x2');d=tuple([rec['descriptor'][0],rec['descriptor'][1],rec['descriptor'][2],tuple(rec['descriptor'][3]),tuple(rec['descriptor'][4])]);idx={d:i for i,d in enumerate(alls)};target=s.ex.exact_row([pack[p]['target'][idx[d]] for p in s.ex.PS]);c0=next(iter(target));col=defaultdict(dict)
  for i,row in enumerate(source):
   for c,v in row.items():col[c][i]=Fraction(v)
  v0=col[c0];S=set(v0);outside_inc=Counter(i for c,v in col.items() if c!=c0 for i in v if i not in S);eligible=[c for c,v in col.items() if c!=c0 and not any(outside_inc[i]==1 for i in v if i not in S)];groups=defaultdict(list)
  for c,v in col.items():
   if c==c0:continue
   outside=sorted((i,a) for i,a in v.items() if i not in S)
   if outside:
    scale=outside[0][1];sig=tuple((i,a/scale) for i,a in outside)
   else:scale=Fraction(1);sig=()
   groups[sig].append(c)
  tested=0;sols=[]
  for members in groups.values():
   for c1,c2 in combinations(members,2):
    tested+=1;x=solve(v0,col[c1],col[c2])
    if x:sols.append({'labels':[list(inv[c0]),list(inv[c1]),list(inv[c2])],'coefficients':[enc(Fraction(1)),enc(x[0]),enc(x[1])]})
  success=bool(sols);out={'schema':'marici.voevodsky.cosmology-three-coordinate-raw-probe-DPC.v1','status':('support_three_probe_found' if success else 'support_three_probe_falsified'),'projective_outside_support_groups':len(groups),'columns_without_global_private_outside_row':len(eligible),'candidate_pairs_tested':tested,'exact_probe_count':len(sols),'probes':sols[:100],'DPC_disposition':('minimum support exactly three' if success else 'support three falsified; lower bound rises to four'),'next_gate':('test-support-three-probe-shift' if success else 'search-support-four-raw-probe'),'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='probes'},indent=2))
 finally:s.base.PRIME=oldp;s.rees.AMBIENT=oldA
if __name__=='__main__':main()
