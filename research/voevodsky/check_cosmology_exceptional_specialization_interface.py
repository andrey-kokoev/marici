"""Audit exceptional specialization after algebraic source recovery."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_exceptional_specialization_interface.json'
REQUIRED=('source_basis','source_differential','exceptional_basis','exceptional_differential','support_correspondence','generator_specialization','chain_residual','provenance')
def main():
 algebra=json.loads((RES/'cosmology_algebraic_source_differential.json').read_text());poles=json.loads((RES/'cosmology_generator_denominator_locus_map.json').read_text());exc=json.loads((RES/'cosmology_exceptional_triangle_relative_localization.json').read_text())
 available={'source_basis':algebra['generator_count']==43564,'source_differential':bool(algebra['complex']),'exceptional_basis':len(exc['primitive_cycle_standard_basis'])==3,'exceptional_differential':exc['edge_boundary_rank']==2,'support_correspondence':False,'generator_specialization':False,'chain_residual':False,'provenance':True}
 missing=[k for k in REQUIRED if not available[k]];assert missing==['support_correspondence','generator_specialization','chain_residual']
 candidate={'g1':'edge12','g2':'edge23','g3':'edge31'}
 source_loci={'K','g1','g2','g3','g23','g31'};unmapped=sorted(source_loci-set(candidate));assert unmapped==['K','g23','g31']
 out={'schema':'marici.voevodsky.cosmology-exceptional-specialization-interface.v1','status':'target_complex_typed_specialization_map_absent','population':available,'missing':missing,'target':{'basis':['edge12','edge23','edge31'],'boundary_rank':2,'primitive_cycle':[1,1,1]},'source':{'labelled_generators':43564,'pole_loci':['V(K)']+[f'V({q})' for q in ('g1','g2','g3','g23','g31')]},'strongest_falsification':{'candidate':'map g1,g2,g3 to the three exceptional edges by display order','residual':'The candidate leaves K, g23, and g31 unmapped and supplies no source-derived incidence correspondence, images for 43,564 generators, or chain residual.','unmapped_loci':unmapped,'rejected':True},'surviving_scope':'The exceptional triangle is a typed three-edge target complex with a primitive cycle; the source is a typed algebraic two-term presentation. They remain separate.','first_missing_typed_object':'A source-derived correspondence from K/q denominator loci or geometric cycles to the three strict-transform lines on E=P2.','acceptance_test':'Derive the correspondence from the blowup geometry, map every labelled generator, and verify boundary commutation and support localization exactly.','disposition':'Do not populate exceptional_specialization. Record the bridge blocker once and reassess the supported-comparison interface using the newly populated algebraic fields.','next_gate':'reassess-supported-comparison-interface-v2','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
