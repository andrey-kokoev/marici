#!/usr/bin/env python3
"""Exhaustive reciprocal-equivariance audit on the two P4 schedule sheets."""
import hashlib,json,platform
from itertools import permutations,combinations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/polarized_permutohedron_reciprocal_equivariance.v1.json';OUT=ROOT/'research/voevodsky/results/polarized_permutohedron_reciprocal_equivariance.json';D=json.loads(FIX.read_text());dual={int(k):int(v) for k,v in D['atom_duality'].items()};P=list(permutations(range(1,5)))
def W(p):return tuple(dual[x] for x in reversed(p))
def swap(p,i):
 q=list(p);q[i-1],q[i]=q[i],q[i-1];return tuple(q)
def facet(I):
 I=set(I);k=len(I);return {p for p in P if set(p[:k])==I}
def WF(I):return {dual[x] for x in set(range(1,5))-set(I)}
involution=all(W(W(p))==p for p in P);gen={1:3,2:2,3:1};naturality=all(W(swap(p,i))==swap(W(p),gen[i]) for p in P for i in (1,2,3))
edges={frozenset((p,swap(p,i))) for p in P for i in (1,2,3)}
subsets=[set(c) for k in (1,2,3) for c in combinations(range(1,5),k)];facet_ok=all({W(p) for p in facet(I)}==facet(WF(I)) for I in subsets);sizes=[len(facet(I)) for I in subsets]
# Relation-word transport under generator reversal.
def mapword(word):return tuple(gen[i] for i in word)
relations={'interchange':((1,3),(3,1)),'braid12':((1,2,1),(2,1,2)),'braid23':((2,3,2),(3,2,3))};mapped={k:(mapword(a),mapword(b)) for k,(a,b) in relations.items()}
checks={'schedule_bijection':len({W(p) for p in P})==24,'strict_round_trip_on_schedules':involution,'all_generator_naturality_squares':naturality,'edge_count_each_sheet':len(edges)==D['expected']['swap_edges_per_sheet'],'all_14_facets_transport_by_dual_complement':len(subsets)==14 and facet_ok,'six_squares_eight_hexagons':sizes.count(4)==6 and sizes.count(6)==8,'interchange_preserved':set(mapped['interchange'])=={(3,1),(1,3)},'braid_hexagons_exchanged':set(mapped['braid12'])==set(relations['braid23']) and set(mapped['braid23'])==set(relations['braid12']),'bulk_orientation_not_silently_fixed':D['bulk_transport']['combinatorial_orientation']=='not_fixed','semantic_four_cell_remains_missing':D['disposition']['semantic_Xi_W_status']=='missing'}
out={'schema':'marici.voevodsky.polarized-permutohedron-reciprocal-equivariance-check.v1','passed':all(checks.values()),'checks':checks,'observed':{'schedules_per_sheet':len(P),'edges_per_sheet':len(edges),'facets_per_sheet':len(subsets),'facet_sizes':{'square':sizes.count(4),'hexagonal':sizes.count(6)},'mapped_relations':{k:[list(a),list(b)] for k,(a,b) in mapped.items()}},'disposition':'Reciprocal transport is a strict involutive isomorphism of the two abstract schedule complexes, reversing generator index and exchanging braid families. The semantic bulk comparison Xi_W remains unconstructed.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_polarized_permutohedron_reciprocal_equivariance.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
