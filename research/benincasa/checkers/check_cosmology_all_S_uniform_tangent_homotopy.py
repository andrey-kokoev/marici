#!/usr/bin/env python3
"""Embed the degree-six exact tangent witness into every larger ambient presentation."""
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky'),str(ROOT/'research'/'benincasa'/'checkers')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_physical_half_twist_seed_exact_rational_minor as exact
OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_all_S_uniform_tangent_homotopy.json'
def key(row):return tuple(sorted(row.items()))
def main():
 witness=json.loads((ROOT/'research'/'benincasa'/'results'/'cosmology_all_S_tangent_killing_exact_lift.json').read_text());protocol=json.loads((ROOT/'research'/'voevodsky'/'results'/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);direction=tuple(protocol['integral_unit_normals']['p_tangent_difference']);origp,origa=base.PRIME,rees.AMBIENT;rees.AMBIENT=6;base.PRIME=32003;_,c6=rees.column_packet();inv6={v:k for k,v in c6.items()};packets={}
 for p in exact.PS:
  base.PRIME=p;packets[p]={'special':list(rees.raw_relations(point,c6))};packets[p]['derived']=adapter.derivative_rows(c6,point,direction)[0]
 base.PRIME=32003;s6=packets[32003]['special'];d6=packets[32003]['derived'];sources=[(x['kind'],x['row_index'],Fraction(x['numerator'],x['denominator'])) for x in witness['sources']];exact_rows={(k,i):exact.exact_row([packets[p][k][i] for p in exact.PS]) for k,i,_ in sources};records=[]
 for degree in (8,10,12):
  rees.AMBIENT=degree;_,cn=rees.column_packet();sn=list(rees.raw_relations(point,cn));dn=adapter.derivative_rows(cn,point,direction)[0];sets={'special':{key(r) for r in sn},'derived':{key(r) for r in dn}};recon={};included=True
  for kind,i,a in sources:
   row=s6[i] if kind=='special' else d6[i];mapped={cn[inv6[c]]:v for c,v in row.items()};included &= key(mapped) in sets[kind]
   for c,v in exact_rows[(kind,i)].items():
    c=cn[inv6[c]];q=recon.get(c,Fraction(0))+a*v
    if q:recon[c]=q
    else:recon.pop(c,None)
  target={cn[(0,1,1,1,1,1,(0,0))]:Fraction(1)};records.append({'ambient_degree':degree,'all_source_rows_included':included,'exact_embedded_reconstruction':recon==target,'target_index':next(iter(target))})
 base.PRIME,rees.AMBIENT=origp,origa;passed=all(r['all_source_rows_included'] and r['exact_embedded_reconstruction'] for r in records);out={'schema':'marici.benincasa.cosmology-all-S-uniform-tangent-homotopy.v1','bounded_source_degree':6,'source_rows':len(sources),'tested_embeddings':records,'monotone_generator_argument':'raw relation exponent ranges and column labels at ambient degree 6 are retained for every ambient degree A>=6','degree_uniform_presentation_theorem':passed,'decision':('The degree-six exact tangent witness embeds unchanged into every ambient presentation A>=6; the all-S primitive derivative is tangent-exact in this unbounded presentation system.' if passed else 'The degree-six witness rows embed, but their exact combination does not reconstruct the target at larger ambient degree; no uniform homotopy was established.'),'scope':'unbounded theorem for the declared algebraic presentation family, not a physical readout or colimit comparison theorem','passed':passed};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
