"""DPC search for a two-coordinate raw probe at A14 grade eight."""
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_collapse_relation_sector as s
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_two_coordinate_raw_probe_DPC.json'
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def main():
 oldA=s.rees.AMBIENT;oldp=s.base.PRIME;s.rees.AMBIENT=14
 try:
  _,cols=s.rees.column_packet();inv={i:l for l,i in cols.items()};ibp,K,q=s.tr.descs(14);alls=ibp+K+q;nK=len(K);descs=alls+K+q;grades=[s.clf.grade(d) for d in descs];point=tuple(json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text())['test_point_xyz']);pack={}
  for p in s.ex.PS:
   s.base.PRIME=p;raw=list(s.rees.raw_relations(point,cols));T,_=s.adapter.derivative_rows(cols,point,(1,-1,0));D2,_=s.adapter.derivative_rows(cols,point,(3,0,-1));pack[p]={'source':T+raw[len(ibp):len(ibp)+nK]+raw[len(ibp)+nK:],'target':D2}
  s.base.PRIME=oldp;source=[s.ex.exact_row([pack[p]['source'][i] for p in s.ex.PS]) for i in range(len(descs)) if grades[i]<=8];data=json.loads((RES/'cosmology_filtered_classification_transport.json').read_text());rec=next(x for x in data['A14_transports'] if x['grade']==8 and x['axis_square']=='x2');d=tuple([rec['descriptor'][0],rec['descriptor'][1],rec['descriptor'][2],tuple(rec['descriptor'][3]),tuple(rec['descriptor'][4])]);idx={d:i for i,d in enumerate(alls)};target=s.ex.exact_row([pack[p]['target'][idx[d]] for p in s.ex.PS]);assert len(target)==1;c0=next(iter(target));S=[i for i,r in enumerate(source) if r.get(c0)];assert S;cands=set(source[S[0]])-{c0}
  for i in S[1:]:cands &= set(source[i])
  for i,r in enumerate(source):
   if i not in S:cands-=set(r)
  sols=[]
  for c1 in cands:
   ratios={Fraction(source[i][c1],source[i][c0]) for i in S}
   if len(ratios)==1:
    ratio=next(iter(ratios));alpha=-1/ratio;assert all(r.get(c0,0)+alpha*r.get(c1,0)==0 for r in source);sols.append({'second_label':list(inv[c1]),'second_coefficient':enc(alpha)})
  success=bool(sols);out={'schema':'marici.voevodsky.cosmology-two-coordinate-raw-probe-DPC.v1','status':('two_coordinate_probe_found' if success else 'two_coordinate_probe_falsified'),'conjecture':'A two-term coefficient functional annihilates all grade-eight source relations and is nonzero on the one-column raw target.','target_label':list(inv[c0]),'target_column_relation_support':len(S),'support_matched_candidate_columns':len(cands),'exact_probe_count':len(sols),'probes':sols,'DPC_disposition':('corroborated candidates' if success else 'falsified at A14: no proportional companion source column'),'surviving_alternatives':['three-or-more-coordinate cancellation','structured non-coordinate extraction'],'next_gate':('test-two-coordinate-probe-shift' if success else 'search-minimal-multicoordinate-raw-probe'),'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
 finally:s.base.PRIME=oldp;s.rees.AMBIENT=oldA
if __name__=='__main__':main()
