"""Gate the finite canonical contraction class modulo exact source syzygies."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_finite_quotient_class_gate.json'
def load(name):return json.loads((RES/name).read_text())
def main():
 exact={A:load(f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{A}.json') for A in (12,14,16,18)}
 natural=load('cosmology_rank26_p_normal_source_constructor_ambient_naturality.json');cover=load('cosmology_rank26_p_normal_two_monomial_source_cover.json');overlap=load('cosmology_rank26_p_normal_two_monomial_overlap_syzygies.json');torsor=load('cosmology_rank26_p_normal_contraction_torsor_nonuniqueness.json');vertical={A:load(f'cosmology_rank26_p_normal_K_q_boundary_exact_difference_syzygies_a{A}.json') for A in (14,16,18)};compositions=[load('cosmology_rank26_p_normal_K_q_boundary_exact_difference_composition.json'),load('cosmology_rank26_p_normal_K_q_boundary_exact_difference_composition_a14_a16_a18.json')]
 assert all(x['passed'] for x in [*exact.values(),natural,cover,overlap,torsor,*vertical.values(),*compositions])
 fibers=sum(x['targets_verified'] for x in exact.values());edge_cells=sum(sum(v['cells'] for v in x['summary'].values()) for x in vertical.values());overlap_cells=sum(v['zero_syzygies'] for v in overlap['summaries'].values());composition_cells=sum(x['strict_coefficient_matches'] for x in compositions)
 # Algebraic gate: for d:S->R and nonempty F_r=d^{-1}(r), any w,w' in F_r differ by ker(d), so F_r/ker(d) is a singleton.
 assert fibers==48+60+72+84 and edge_cells==48+60+48+72+60 and overlap_cells==36+48+60 and composition_cells==48+60
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-finite-quotient-class-gate.v1','status':'finite_contraction_quotient_classes_are_canonical_and_ambient_compatible','ambient_degrees':[12,14,16,18],'nonempty_contraction_fibers':fibers,'verified_vertical_difference_cells':edge_cells,'verified_two_cover_overlap_cells':overlap_cells,'verified_composition_cells':composition_cells,'quotient_statement':'For each verified target r, d^{-1}(r)/ker(d) is a singleton. Source-natural ambient maps preserve ker(d), so these singleton classes transport independently of representative.','decision':'The finite ambient mechanism has a canonical quotient class of contractions even though it has no canonical contraction word.','limitations':['finite degrees only','the quotient class encodes absorption, not a surviving p-normal line','arbitrary-degree constructor naturality and colimit existence are separate gates'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
