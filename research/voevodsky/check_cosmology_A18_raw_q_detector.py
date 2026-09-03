"""Test the 1,y,x raw-q detector on x-cubed A18 paths."""
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_raw_q_collapse_certificates as c
s=c.s;RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_A18_raw_q_detector.json'
def det(M):return M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def main():
 oldA=s.rees.AMBIENT;oldp=s.base.PRIME;s.rees.AMBIENT=18
 try:
  _,cols=s.rees.column_packet();ibp,K,qrows=s.tr.descs(18);alls=ibp+K+qrows;nA=len(alls);nK=len(K);descs=alls+K+qrows;grades=[s.clf.grade(d) for d in descs];point=tuple(json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text())['test_point_xyz']);pack={}
  for p in s.ex.PS:
   s.base.PRIME=p;raw=list(s.rees.raw_relations(point,cols));T,_=s.adapter.derivative_rows(cols,point,(1,-1,0));D2,_=s.adapter.derivative_rows(cols,point,(3,0,-1));pack[p]={'source':T+raw[len(ibp):len(ibp)+nK]+raw[len(ibp)+nK:],'target':D2}
  s.base.PRIME=oldp;exact=[s.ex.exact_row([pack[p]['source'][i] for p in s.ex.PS]) for i in range(len(descs))];tk={}
  for i in range(nA+nK):
   if grades[i]<=8:s.insert(exact[i],tk)
  qb={}
  for i in range(nA+nK,len(descs)):
   if grades[i]<=8:c.insert_track(s.reduce(exact[i],tk),{i:Fraction(1)},qb)
  z=json.loads((RES/'cosmology_filtered_A16_persistence_induction.json').read_text());base=[x for x in z['A16_classes'] if x['grade']==8 and x['axis_square']=='xx'];records=[]
  for x in base:
   d=tuple([x['descriptor'][0],x['descriptor'][1],x['descriptor'][2],tuple(x['descriptor'][3]),tuple(x['descriptor'][4])]);records.append({'target_id':x['target_id'],'descriptor':s.tr.shift(d,0)})
  idx={d:i for i,d in enumerate(alls)};pre=[]
  for rec in records:
   t=s.ex.exact_row([pack[p]['target'][idx[rec['descriptor']]] for p in s.ex.PS]);pre.append(s.reduce(t,tk))
  full=[s.reduce(x,{p:r for p,(r,w) in qb.items()}) for x in pre];deps=c.relations(full);assert len(deps)==3;sols=[]
  for dep in deps:
   u={}
   for j,a in dep.items():c.add(u,pre[j],a)
   sol={};r=dict(u)
   while r:
    p=min(r);br,bw=qb[p];a=r[p];c.add(r,br,-a);c.add(sol,bw,a)
   sols.append(sol)
  M=[]
  for pair in ((0,0),(0,1),(1,0)):
   i=nA+nK+qrows.index(('q',0,0,(1,1,2,1,1),pair));M.append([v.get(i,Fraction()) for v in sols])
  D=det(M);out={'schema':'marici.voevodsky.cosmology-A18-raw-q-detector.v1','status':('detector_persists' if D else 'detector_fails'),'relation_dimension':len(deps),'target_order':[x['target_id'] for x in records],'relation_basis':[[enc(dep.get(i,Fraction())) for i in range(4)] for dep in deps],'detector_matrix':[[enc(x) for x in row] for row in M],'determinant':enc(D),'decision':('The 1,y,x raw-q detector remains invertible on x-cubed A18 paths.' if D else 'The detector becomes singular at A18.'),'claim_boundary':'Exact algebraic quotient certificate only.','next_gate':'compare-A16-A18-detector-transition','passed':bool(D)};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'determinant':out['determinant'],'passed':out['passed']},indent=2))
 finally:s.base.PRIME=oldp;s.rees.AMBIENT=oldA
if __name__=='__main__':main()
