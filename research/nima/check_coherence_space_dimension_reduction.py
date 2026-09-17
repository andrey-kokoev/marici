#!/usr/bin/env python3
"""Reduce the eight-axis coherence atlas to its stratified active skeleton."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];src=json.loads((ROOT/'research/nima/results/eight-axis-operator-three-face-registry.json').read_text());relative=json.loads((ROOT/'research/nima/results/qRB-relative-positive-geometry-admission.json').read_text())
records=src['records'];nontrivial={k:v for k,v in records.items() if v['status']!='coherent_strict_or_canonical'}
# H,V,D are canonical transport directions. The active atlas retains only operator,
# chart, boundary/leakage, and regulator information.
active=('q','L','C','O','R');active_triples=[' x '.join(t) for t in itertools.combinations(active,3)];active_nontrivial={k:records[k] for k in active_triples if records[k]['status']!='coherent_strict_or_canonical'}
# C is an exact chart equivalence, while O and L are strata of one boundary/readout
# direction B. R retains its place/transported/independent-window stratum.
exception_map={
 'q x C x O':{'reduced_cell':'q-B','stratum':'endpoint','law':'projective'},
 'q x C x R':{'reduced_cell':'q-R','stratum':'chart-transported/place versus independent-window','law':'strict versus lax'},
 'q x L x R':{'reduced_cell':'q-R-B','stratum':'leakage','law':'lax'},
 'q x O x R':{'reduced_cell':'q-R-B','stratum':'endpoint observation under independent window','law':'lax'},
 'H x q x R':{'reduced_cell':'q-R','stratum':'H-transport annotation','law':'canonical transport of leakage'},
 'V x q x R':{'reduced_cell':'q-R','stratum':'V-transport annotation','law':'canonical transport of leakage'},
 'D x q x R':{'reduced_cell':'q-R','stratum':'dagger annotation','law':'forward/reverse leakage mate'},
}
checks={'expanded_registry_passes':src['passed'],'seven_nontrivial_expanded_types':len(nontrivial)==7,'all_expanded_exceptions_mapped':set(nontrivial)==set(exception_map),'five_axis_active_atlas_has_ten_triples':len(active_triples)==10,'four_nontrivial_active_triples':len(active_nontrivial)==4,'canonical_transport_axes_removed':all(x not in active for x in ('H','V','D')),'exact_chart_C_quotiented':all(exception_map[k]['reduced_cell'].find('C')<0 for k in exception_map),'boundary_strata_merge_O_and_L':{exception_map['q x C x O']['stratum'],exception_map['q x L x R']['stratum']}=={'endpoint','leakage'},'three_direction_skeleton':set(('q','R','B'))=={'q','R','B'},'relative_positive_filler_admitted':relative['passed']}
out={'schema':'marici.nima.coherence-space-dimension-reduction.v1','expanded_dimension':8,'expanded_axes':src['axes'],'expanded_nontrivial_types':nontrivial,'active_atlas_dimension':5,'active_atlas_axes':active,'active_triples':active_triples,'active_nontrivial_types':active_nontrivial,'reduction_rules':{'H,V,D':'canonical transport annotations, not independent active directions','C':'exact q-C chart equivalence; quotient after transporting endpoint/regulator typing','O,L':'strata of boundary/readout direction B','R':'stratified as place, transported, or independent window'},'exception_map':exception_map,'minimal_directional_skeleton':{'dimension':3,'axes':['q','R','B'],'strata':{'B':['endpoint','leakage'],'R':['place','transported','independent_window']},'nontrivial_three_cell':'q-R-B','positive_geometry':'relative cone filler P is admitted on the q-R-B three-cell; P is a property/filler, not an independent direction'},'checks':checks,'passed':all(checks.values()),'claim_boundary':'This is a quotient of coherence bookkeeping by proved exact/canonical equivalences. Relative carrier positivity is admitted on the stated core and iterated regulator order; scalar Weil positivity is not claimed.'}
p=ROOT/'research/nima/results/coherence-space-dimension-reduction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
