"""Verify two monomial-square source inclusions and their boundary-coordinate cover."""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_two_monomial_source_cover.json'
def key(d):f,k,l,ax,m,e=d;return(f,k,tuple(l),ax,m,tuple(e))
def shift_desc(d,axis):
 f,k,l,ax,m,e=d;q=list(e);q[axis]+=2;return(f,k,tuple(l),ax,m,tuple(q))
def packet(A,point,td):
 rees.AMBIENT=A;_,cols=rees.column_packet();inv={i:k for k,i in cols.items()};sp=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,td);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));full,sk=compat.descriptors(A);q=[d for d in full if d[0]=='q'];return{'columns':cols,'inverse':inv,'T':T,'S_K':sp[nI:nI+nK],'Q':sp[nI+nK:],'descriptors':{'T':full,'S_K':sk,'Q':q}}
def shift_row(row,inv,target,axis):
 out={}
 for c,v in row.items():
  label=inv[c];e=list(label[-1]);e[axis]+=2;out[target[(*label[:-1],tuple(e))]]=v
 return out
def main():
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);summaries={};total_fail=0
 for lo,hi in ((12,14),(14,16),(16,18)):
  L=packet(lo,point,td);H=packet(hi,point,td);entry={}
  for axis in (0,1):
   ae={}
   for kind in ('T','S_K','Q'):
    idx={key(d):i for i,d in enumerate(H['descriptors'][kind])};matches=0
    for i,d in enumerate(L['descriptors'][kind]):matches+=shift_row(L[kind][i],L['inverse'],H['columns'],axis)==H[kind][idx[shift_desc(d,axis)]]
    failures=len(L[kind])-matches;total_fail+=failures;ae[kind]={'rows':len(L[kind]),'matches':matches,'failures':failures}
   entry[f'axis{axis}']=ae
  higher=[e for e in base.monomials_at_most(hi-4) if sum(e)>=hi-6];covered=[e for e in higher if e[0]>=2 or e[1]>=2];overlap=[e for e in higher if e[0]>=2 and e[1]>=2];entry['boundary_cover']={'targets_per_pole':len(higher),'covered':len(covered),'uncovered':len(higher)-len(covered),'overlap':len(overlap)};summaries[f'A{lo}_to_A{hi}']=entry
 assert total_fail==0 and all(v['boundary_cover']['uncovered']==0 for v in summaries.values())
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-two-monomial-source-cover.v1','status':'two_source_natural_monomial_inclusions_cover_every_higher_boundary','summaries':summaries,'decision':'Multiplication by either monomial variable squared is source-natural, and the two images cover every higher cutoff-boundary coordinate; their nonempty overlap requires descent coherence.','limitations':['finite inclusions A12 through A18','rank-26 test point','does not yet verify overlap contraction coherence or choose a section'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
