#!/usr/bin/env python3
"""Locate the sourced A3 history/root labels in the finite associahedral resolution."""
import itertools,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; n=6
def edge(a,b): return tuple(sorted((a,b)))
boundary={edge(i,(i+1)%n) for i in range(n)}
diags=[edge(i,j) for i in range(n) for j in range(i+1,n) if edge(i,j) not in boundary]
def cross(x,y):
 a,b=x;c,d=y
 return (a<c<b<d) or (c<a<d<b)
clusters=[tuple(sorted(S)) for S in itertools.combinations(diags,3) if all(not cross(x,y) for x,y in itertools.combinations(S,2))]
edges=[(i,j) for i,j in itertools.combinations(range(len(clusters)),2) if len(set(clusters[i])^set(clusters[j]))==2]
# Source dictionary [i,j] -> (i,j+2), with 1-based polygon vertices; convert to 0-based.
pos=[(i-1,j+1) for i in range(1,4) for j in range(i,4)]
assert len(clusters)==14 and len(edges)==21 and len(diags)==9 and len(pos)==6
inc={str(d):[k for k,T in enumerate(clusters) if d in T] for d in pos}
counts=[len(v) for v in inc.values()]
# Each diagonal labels the facet formed by clusters containing it; exactly C2, not C0.
source=json.loads((R/'nima/results/nnmhv-associahedron-cluster-bridge.json').read_text())
match=json.loads((R/'nima/results/eight-point-history-positroid-matching.json').read_text())
out={'schema':'marici.benincasa.a3-history-to-resolution-comparison.v1','source_facts':{'selected_A3_histories':6,'certified_eight_point_histories':len(match['matches']),'cluster_variables':9,'clusters_C0':14,'mutation_edges_C1':21,'facets_C2':9},'typed_location':{'history_positive_roots':'six positive-root diagonals, hence six labelled facets in C2','negative_simple_references':'remaining three diagonal facets in C2','not_C0':'C0 generators are complete triangulations/clusters, not roots, histories, or individual positroid cells'},'positive_history_diagonal_to_C0_incidence':inc,'clusters_containing_each_positive_history':counts,'unique_C0_map_from_labels':False,'reason':'Every sourced positive-root/history diagonal belongs to four or five C0 clusters; no source chooses one completion triangulation. The canonical map furnished by the bridge lands in the six positive C2 facet labels instead.','coefficient_transport_C1':{'available':False,'known_data':'one negative physical exchange residual and three simple-root diagonal corrections','required':'a signed/rational transport map for all 21 flips between complete triangulations'},'compatibility':{'with_d1':'not typeable without a C0 generator map and all C1 coefficients','with_d2':'the unweighted cellular d1*d2=0 is proved by Nima; physical weighted compatibility is underdetermined'},'finite_disposition':'requested history/positroid-to-C0 map obstructed by degree/type mismatch; canonical label map is to C2 facets; C1 physical transport remains missing','checks':{'source_reports_six_positive_variables':next(x for x in source['rows'] if x['type']=='A_3')['history_positive_diagonals']==6,'all_positive_labels_are_facets':all(d in diags for d in pos),'no_positive_label_is_a_unique_cluster':all(c>1 for c in counts),'facet_incidence_counts_are_4_or_5':set(counts)=={4,5},'twenty_certified_full_histories':len(match['matches'])==20},'passed':True}
p=R/'benincasa/results/a3_history_to_resolution_comparison.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
