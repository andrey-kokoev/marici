"""Test ambient multiplication naturality of T, S_K, and Q source-row constructors."""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_source_constructor_ambient_naturality.json'
def key(d):
 f,k,l,ax,m,e=d;return (f,k,tuple(l),ax,m,tuple(e))
def shift_desc(d,n=2):
 f,k,l,ax,m,e=d;return (f,k,tuple(l),ax,m,(e[0],e[1]+n))
def packet(A,point,td):
 rees.AMBIENT=A;_,cols=rees.column_packet();inv={i:k for k,i in cols.items()};sp=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,td);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));full,sk=compat.descriptors(A);q=[d for d in full if d[0]=='q'];return {'columns':cols,'inverse':inv,'T':T,'S_K':sp[nI:nI+nK],'Q':sp[nI+nK:],'descriptors':{'T':full,'S_K':sk,'Q':q}}
def shift_row(row,inv,target_cols,n=2):
 out={}
 for c,v in row.items():
  label=inv[c];e=label[-1];sl=(*label[:-1],(e[0],e[1]+n));out[target_cols[sl]]=v
 return out
def main():
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);summaries={};failures=[]
 for lo,hi in ((12,14),(14,16),(16,18)):
  L=packet(lo,point,td);H=packet(hi,point,td);entry={}
  for kind in ('T','S_K','Q'):
   hiidx={key(d):i for i,d in enumerate(H['descriptors'][kind])};matches=0;diff=[]
   for i,d in enumerate(L['descriptors'][kind]):
    j=hiidx[shift_desc(d)];a=shift_row(L[kind][i],L['inverse'],H['columns']);b=H[kind][j]
    if a==b:matches+=1
    else:
     n=sum(a.get(c,0)!=b.get(c,0) for c in set(a)|set(b));diff.append(n);failures.append({'inclusion':f'A{lo}_to_A{hi}','kind':kind,'source_index':i,'difference_columns':n})
   entry[kind]={'rows':len(L[kind]),'literal_matches':matches,'failures':len(diff),'difference_columns_min':min(diff) if diff else 0,'difference_columns_max':max(diff) if diff else 0}
  summaries[f'A{lo}_to_A{hi}']=entry
 passed=not failures;out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-source-constructor-ambient-naturality.v1','status':'all_source_constructors_transport_naturally' if passed else 'some_source_constructors_fail_literal_naturality','summaries':summaries,'failure_sample':failures[:12],'decision':'Ambient multiplication by the second monomial variable commutes rowwise with every T, S_K, and Q constructor.' if passed else 'The typed descriptor inclusion does not commute literally with every tested source-row constructor.','limitations':['even inclusions A12 through A18','single exact integer presentation at the rank-26 test point','does not construct a natural contracting homotopy'],'passed':passed};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
