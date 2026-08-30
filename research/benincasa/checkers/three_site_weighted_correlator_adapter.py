"""Labelled Boolean deletion cube for the three-site one-loop correlator adapter."""
import itertools, json
from pathlib import Path

edges=("12","23","31")
sectors=[]
for r in range(4):
    for subset in itertools.combinations(edges,r):
        sectors.append({"deleted":list(subset),"retained":[e for e in edges if e not in subset],"grade":r})
assert len(sectors)==8
assert [sum(s["grade"]==r for s in sectors) for r in range(4)]==[1,3,3,1]

# Boolean-poset incidence.  The displayed sign is an explicitly chosen
# bookkeeping orientation based on the global edge order; the source does not
# type these incidences as a chain differential.
incidence=[]
for s in sectors:
    S=set(s["deleted"])
    for i,e in enumerate(edges):
        if e not in S:
            T=tuple(x for x in edges if x in S|{e})
            sign=(-1)**sum(1 for x in edges[:i] if x in S)
            incidence.append({"from":s["deleted"],"to":list(T),"edge":e,"bookkeeping_sign":sign,"coefficient_map":"untyped"})
assert len(incidence)==12

endpoint={"12":("1","2"),"23":("2","3"),"31":("3","1")}
for s in sectors:
    shifts={"1":[],"2":[],"3":[]}
    for e in s["deleted"]:
        for vertex in endpoint[e]:
            shifts[vertex].append(f"y{e}")
    s["site_energy_shifts"]={k:" + ".join(v) if v else "0" for k,v in shifts.items()}
    s["total_energy_shift"]=" + ".join(f"2*y{e}" for e in s["deleted"]) if s["deleted"] else "0"
    s["augmentation_weight"]=(-2)**s["grade"]

weight_multiplicities={str(r):sum(1 for s in sectors if s["grade"]==r) for r in range(4)}
weighted_grade_totals={str(r):sum(s["augmentation_weight"] for s in sectors if s["grade"]==r) for r in range(4)}
assert weight_multiplicities=={"0":1,"1":3,"2":3,"3":1}
assert weighted_grade_totals=={"0":1,"1":-6,"2":12,"3":-8}

cyclic_edge={"12":"23","23":"31","31":"12"}
sector_keys={tuple(s["deleted"]) for s in sectors}
for s in sectors:
    rotated=tuple(e for e in edges if e in {cyclic_edge[x] for x in s["deleted"]})
    assert rotated in sector_keys
    target=next(t for t in sectors if tuple(t["deleted"])==rotated)
    assert target["grade"]==s["grade"]
    assert target["augmentation_weight"]==s["augmentation_weight"]
fixed_under_generator=sum(
    1 for s in sectors
    if tuple(e for e in edges if e in {cyclic_edge[x] for x in s["deleted"]})==tuple(s["deleted"])
)
assert fixed_under_generator==2

packet={
 "schema":"marici.three-site-weighted-correlator-adapter.v1",
 "source":"Benincasa-Dian arXiv:2401.05207, equations (2.29), (4.71), and the 2^ne edge-erasure rule",
 "edge_labels":list(edges),
 "sector_count":len(sectors),
 "grade_dimensions":[1,3,3,1],
 "augmentation":{
   "domain":"direct sum of the eight independently defined deletion-sector modules",
   "codomain":"common correlator readout",
   "sector_weight":"(-2)^grade",
   "weight_multiplicities":weight_multiplicities,
   "weighted_grade_totals":weighted_grade_totals,
   "intergrade_differential":None,
 },
 "cyclic_action":{
   "edge_generator":{"12":"23","23":"31","31":"12"},
   "fixed_sectors":2,
   "free_orbits":2,
   "permutation_character":[8,2,2],
   "augmentation_weight_invariant":True,
 },
 "sectors":sectors,
 "boolean_poset_incidence":incidence,
 "incidence_typing":"combinatorial only; bookkeeping signs are not source-derived coefficient differentials",
 "source_operations":["retain existing wavefunction graph","erase labelled edge","insert inverse two-point factor 1/y_e","shift endpoint site weights by y_e","change subdivision orientation/weight"],
 "new_polynomial_divisor_introduced_by_combinatorial_adapter":False,
 "Q_can_be_carrier_divisor_at_this_stage":False,
 "classification":"source-derived augmented star: eight independently defined Kummer ports feed one common readout; Boolean incidence indexes sectors but is not a coefficient differential",
 "conclusion":"For the three-edge loop, the wavefunction-to-correlator adapter is indexed by the complete labelled Boolean deletion poset. Its pre-integration operations use existing edge occurrences and linear wavefunction data, so a quartic Q cannot enter as a new carrier divisor here. The deletion sectors have distinct total-energy normals E_T+2*sum_{e in S}y_e; any successor quartic must be derived from their integrated pushforward or other coefficient/physical transport.",
}
out=Path(__file__).parent/'results'/'three-site-weighted-correlator-adapter.json'
out.write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps(packet,indent=2))
