"""DPC audit of raw Hessians and the unchanged algebraic quotient."""
from __future__ import annotations
import json,os,sys
from collections import Counter
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_source_word_axis_square_transport as tr
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_second_jet_interface_audit.json';P=32003
def reduce_row(row,basis,insert=False):
 r={c:v%P for c,v in row.items() if v%P}
 while r:
  p=min(r);b=basis.get(p)
  if b is None:
   if insert:
    q=pow(r[p],-1,P);r={c:(v*q)%P for c,v in r.items()};basis[p]=r
   return r
  a=r[p]
  for c,v in b.items():
   z=(r.get(c,0)-a*v)%P
   if z:r[c]=z
   else:r.pop(c,None)
 return r
def second_rows(columns,point,direction):
 samples=adapter.sampled_rows(columns,point,direction);weights=rees.interpolation_weights(2);return [rees.combine(rows,weights) for rows in zip(*samples,strict=True)]
def rowlin(rows,coefs):return rees.combine(rows,coefs)
def main():
 old=base.PRIME;base.PRIME=P
 try:
  gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz']);nx=(1,0,0);t1=(1,-1,0);t2=(3,0,-1);_,cols=rees.column_packet();ibp,K,q=tr.descs(12);all_desc=ibp+K+q;nI=len(ibp);nK=len(K);raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,t1);source=T+raw[nI:nI+nK]+raw[nI+nK:];basis={}
  for row in source:reduce_row(row,basis,True)
  vectors={'00':nx,'11':t1,'22':t2};diag={k:second_rows(cols,point,v) for k,v in vectors.items()};inv2=pow(2,-1,P);components=dict(diag)
  for a,b,name in [('00','11','01'),('00','22','02'),('11','22','12')]:
   s=second_rows(cols,point,tuple(vectors[a][i]+vectors[b][i] for i in range(3)));components[name]=[rowlin((x,y,z),(inv2,-inv2,-inv2)) for x,y,z in zip(s,diag[a],diag[b],strict=True)]
 finally:base.PRIME=old
 targets=[]
 for family,name in [('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')]:
  for rec in json.loads((RES/name).read_text())['records']:targets.append((family,all_desc.index(tr.target_desc(family,rec))))
 assert len(targets)==1224;raw_nonzero={k:sum(bool(r) for r in rows) for k,rows in components.items()};residual=Counter();support=Counter()
 for k,rows in components.items():
  for family,i in targets:
   rem=reduce_row(rows[i],basis,False);residual[f'{k}:{family}:{"nonzero" if rem else "zero"}']+=1
   if rem:support[len(rem)]+=1
 nonzero=sum(v for k,v in residual.items() if k.endswith(':nonzero'))
 out={'schema':'marici.voevodsky.cosmology-second-jet-interface-audit.v1','problem':'Does the symmetric xyz Hessian define a nonzero second-jet class in the existing relation quotient?','bold_conjecture':'At least one Hessian component survives reduction by the unchanged T/S_K/Q image and defines a second-order Bockstein candidate.','named_rivals':['all six Hessian components remain exact in the unchanged quotient','raw Hessians exist but no second-order connecting quotient is defined','polarization or interpolation fails to materialize a symmetric Hessian'],'risky_consequences':['six symmetric components materialize','a seed target has a nonzero full-image residual','a separately sourced second-order quotient/admissibility rule exists'],'strongest_falsification':{'field':P,'raw_rows_per_component':len(raw),'raw_nonzero_rows':raw_nonzero,'source_image_rank':len(basis),'seed_targets':len(targets),'quotient_residual_census':dict(sorted(residual.items())),'nonzero_residuals':nonzero,'residual_support_census':{str(k):v for k,v in sorted(support.items())}},'interface_contract':{'symmetric_hessian_rows':True,'polarization_checks':True,'target_module':'C0 reused diagnostically','second_order_quotient_or_extension':False,'admissible_second_order_primitives':False,'geometric_or_exceptional_comparison':False},'disposition':{'status':('raw_nonzero_quotient_residuals_found_but_no_typed_second_bockstein' if nonzero else 'bold_conjecture_rejected_in_unchanged_quotient'),'claim_boundary':'Modular residuals classify raw Hessian rows against the unchanged algebraic image only; they do not define a second-order connecting map.','first_missing_typed_object':'A sourced second-order extension or jet complex specifying which differentiated primitives and quotient define the connecting class.'},'next_gate':('classify-second-jet-modular-residuals' if nonzero else 'test-second-jet-exact-membership'),'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
