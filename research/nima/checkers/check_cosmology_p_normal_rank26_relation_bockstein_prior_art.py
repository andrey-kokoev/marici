"""Audit source-derived rank-26 prior art for a p-normal relation Bockstein test."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; NIMA=ROOT/"nima"; BEN=ROOT/"benincasa"; OUT=NIMA/"results"/"cosmology_p_normal_rank26_relation_bockstein_prior_art.json"
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def main():
    gamma=load(BEN/"results"/"rank26-conductor-gamma-bockstein.json")
    natural=load(BEN/"results"/"rank26-gamma-bockstein-transition-naturality.json")
    atlas=load(BEN/"results"/"rank26-dual-gamma-cyclic-atlas-closure.json")
    moving=load(BEN/"rank26-moving-relation-coherence.json")
    rees=load(BEN/"rank26-total-energy-rees-source-comparison-a12-p32009-point-3-5-m8.json")
    assert gamma["passed"] and gamma["bockstein_image_rank"]==1
    assert natural["passed"] and natural["checks"]["unit_normal_coordinate_slope"]
    assert atlas["passed"] and atlas["bockstein_line_edge_product"]==1
    assert moving["status"]=="pass" and moving["checks"]["total_derived_relation_span_contains_euler_defect"]
    assert rees["tangent_source_closure"]["map"]=="canonical inclusion into the identical labelled Laurent presentation"
    point=[3,6,-3]; p=point[0]+point[1]+3*point[2]; energy=sum(point)
    nx=[1,0,0]; ny=[0,1,0]; tangent=[nx[i]-ny[i] for i in range(3)]
    assert p==0 and energy!=0 and tangent==[1,-1,0]
    packet={
      "schema":"marici.cosmology-p-normal-rank26-relation-bockstein-prior-art.v1",
      "status":"bounded_full_rank26_p_normal_relation_bockstein_test_open",
      "source_presentation":"complete labelled rank-26 Laurent/IBP presentation with marks (g1,g2,g3,g23,g31)",
      "generic_p_normal_test_point":{"xyz":point,"p":p,"total_energy":energy},
      "integral_unit_normals":{"nx":nx,"ny":ny,"difference_tangent_to_p":tangent},
      "prior_mechanisms_available":{
        "dual_normal_exact_relation_bockstein":True,
        "moving_relation_derivative_coherence":True,
        "strict_cyclic_rank26_atlas_with_unit_edge_product":True,
        "Rees_source_inclusion_in_identical_labelled_presentation":True},
      "proposed_test":[
        "evaluate the full labelled relation matrix at p=0",
        "differentiate its source-generated relation rows along nx without global division by p",
        "reduce first derivatives modulo the special exact-relation image",
        "repeat along ny and require equality modulo the p-tangent derived-relation span",
        "map any surviving line through the ordered wall-residue/exceptional-face total complex",
        "require integral unit column (1,1), d^2=0, Rees-shear invariance, and survival over two primes"],
      "typing_restrictions":[
        "do not reuse the gamma-normal Bockstein vector; only its relation-derivative algorithm",
        "do not reuse the total-energy Rees class; p=0 is tested at nonzero total energy",
        "do not identify cyclic Gysin charts with the internal three-wall Cech cover",
        "restrict Hom_R((p),R) to explicitly p-supported relation terms"],
      "full_rank26_p_normal_bockstein_computed":False,
      "tau_p_source_map_constructed":False,
      "physical_period_constructed":False,
      "currently_open_internal_test":True,
      "requires_new_external_source_authority_for_test":False,
      "conclusion":"prior rank-26 work supplies a source-derived algorithm, not a transferable class: compute the p-normal derivative Bockstein of the full labelled exact-relation module and test whether its image supplies the missing tau_p unit cell",
      "passed":True}
    OUT.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8"); print(json.dumps(packet,indent=2))
if __name__=="__main__": main()
