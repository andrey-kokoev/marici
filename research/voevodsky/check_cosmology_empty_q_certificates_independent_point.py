"""Classify empty q seed targets at an independent exact p=0 point."""
from __future__ import annotations
import json,os,sys
os.environ['MARICI_AMBIENT']='12'
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as exact
import cosmology_exact_source_certificate as certificate
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_empty_q_certificates_independent_point.json'
def targets(point,indices,columns):
 packets={};orig=base.PRIME
 for p in exact.PS:
  base.PRIME=p;dx,_=adapter.derivative_rows(columns,point,(1,0,0));packets[p]=dx
 base.PRIME=orig
 return [exact.exact_row([packets[p][i] for p in exact.PS]) for i in indices]
def main():
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point0=tuple(protocol['test_point_xyz']);point1=(4,5,-3)
 assert sum(a*b for a,b in zip(protocol['p_normal_covector'],point1))==0 and sum(point1)!=0 and point1!=point0
 _,columns=rees.column_packet();nI=4*len(base.monomials_at_most(12));nK=64*len(base.monomials_at_most(8));qdesc=[]
 for qi in range(len(rees.NAMES)):
  for kp in range(charts.K_DEPTH+1):
   for lev in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
    if lev[qi]==charts.Q_DEPTH:continue
    for e in base.monomials_at_most(11):qdesc.append((qi,kp,lev,e))
 seeds=[(qi,kp,lev,e) for qi in range(5) for kp in range(3) for lev in product((1,2),repeat=5) if lev[qi]==1 for e in ((0,0),(0,1),(1,0),(1,1))]
 indices=[nI+nK+qdesc.index(d) for d in seeds];rows0=targets(point0,indices,columns);rows1=targets(point1,indices,columns)
 records=json.loads((RES/'cosmology_q_exact_source_certificates_a12.json').read_text())['records'];assert len(records)==len(seeds)
 categories={'empty_at_both':0,'empty_only_original':0,'empty_only_independent':0,'nonempty_at_both':0};examples={};by_q_index={str(i):{'empty_at_both':0,'nonempty_at_both':0} for i in range(5)}
 for d,r0,r1,record in zip(seeds,rows0,rows1,records):
  cert=record['source_certificate'];assert certificate.digest(r0)==cert['target_digest']
  a=not r0;b=not r1
  key=('empty_at_both' if a and b else 'empty_only_original' if a else 'empty_only_independent' if b else 'nonempty_at_both');categories[key]+=1
  if key in by_q_index[str(d[0])]:by_q_index[str(d[0])][key]+=1
  examples.setdefault(key,{'q_index':d[0],'k_pole':d[1],'levels':list(d[2]),'exponent':list(d[3]),'original_support':len(r0),'independent_support':len(r1)})
 assert categories=={'empty_at_both':576,'empty_only_original':0,'empty_only_independent':0,'nonempty_at_both':384}
 out={'schema':'marici.voevodsky.cosmology-empty-q-certificates-independent-point.v1','status':'same_576_q_targets_vanish_at_two_noncollinear_exact_points','original_point':list(point0),'independent_point':list(point1),'admissibility':{'p_normal_pairing':0,'total_energy':sum(point1),'noncollinear_with_original':True},'categories':categories,'by_q_index':by_q_index,'examples':examples,'classification':'The empty targets are not peculiar to the original evaluation point: exactly the same 576 vanish at a noncollinear admissible point. Two-point stability is evidence for a structural zero family, but finite evaluations do not prove symbolic identity.','retained':'The 576 empty words replay as exact zero targets at both tested points.','withheld':'The targets vanish identically on the full p=0 source locus.','next_gate':'derive-structural-empty-q-family','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
