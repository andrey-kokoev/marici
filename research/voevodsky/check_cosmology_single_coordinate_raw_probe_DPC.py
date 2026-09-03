"""DPC test of single raw-coordinate probes at A14 grade eight."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_collapse_relation_sector as s
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_single_coordinate_raw_probe_DPC.json'
def main():
 oldA=s.rees.AMBIENT;oldp=s.base.PRIME;s.rees.AMBIENT=14
 try:
  _,cols=s.rees.column_packet();inv={i:l for l,i in cols.items()};ibp,K,q=s.tr.descs(14);alls=ibp+K+q;nK=len(K);descs=alls+K+q;grades=[s.clf.grade(d) for d in descs];point=tuple(json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text())['test_point_xyz']);pack={}
  for p in s.ex.PS:
   s.base.PRIME=p;raw=list(s.rees.raw_relations(point,cols));T,_=s.adapter.derivative_rows(cols,point,(1,-1,0));D2,_=s.adapter.derivative_rows(cols,point,(3,0,-1));pack[p]={'source':T+raw[len(ibp):len(ibp)+nK]+raw[len(ibp)+nK:],'target':D2}
  s.base.PRIME=oldp;source=[s.ex.exact_row([pack[p]['source'][i] for p in s.ex.PS]) for i in range(len(descs)) if grades[i]<=8];occupied=set().union(*(set(r) for r in source));data=json.loads((RES/'cosmology_filtered_classification_transport.json').read_text());rec=next(x for x in data['A14_transports'] if x['grade']==8 and x['axis_square']=='x2');d=tuple([rec['descriptor'][0],rec['descriptor'][1],rec['descriptor'][2],tuple(rec['descriptor'][3]),tuple(rec['descriptor'][4])]);idx={d:i for i,d in enumerate(alls)};target=s.ex.exact_row([pack[p]['target'][idx[d]] for p in s.ex.PS]);free=[c for c,v in target.items() if c not in occupied and v];success=bool(free)
  out={'schema':'marici.voevodsky.cosmology-single-coordinate-raw-probe-DPC.v1','status':('single_coordinate_probe_found' if success else 'single_coordinate_probe_falsified'),'conjecture':'One raw coefficient coordinate annihilates every grade-eight relation row and is nonzero on the target.','attempted_construction':'Intersect target support with columns absent from every allowed T/raw-K/raw-q row at A14.','source_relation_count':len(source),'target_support_count':len(target),'unoccupied_target_coordinate_count':len(free),'witness_labels':[list(inv[c]) for c in free[:20]],'DPC_disposition':('corroborated candidate' if success else 'falsified at A14 by empty support intersection'),'surviving_alternatives':['multi-coordinate cancellation probe','structured residue/extraction functional'],'next_gate':('test-coordinate-probe-shift' if success else 'search-two-coordinate-raw-probe'),'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
 finally:s.base.PRIME=oldp;s.rees.AMBIENT=oldA
if __name__=='__main__':main()
