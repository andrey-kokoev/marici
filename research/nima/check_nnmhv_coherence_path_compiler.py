#!/usr/bin/env python3
"""Structural checks for compiling PNNMHVnew into two-phase histories."""
import json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/nima'))
from nnmhv_coherence_paths import compile_nnmhv_histories
rows=[]
for n in range(5,11):
 h=compile_nnmhv_histories(n);branches=Counter(x.branch for x in h);updates=Counter(u.side for x in h for u in x.boundary_updates);rows.append({'n':n,'histories':len(h),'branches':dict(branches),'boundary_updates':dict(updates),'adjacent_inner_pairs':sum(x.inner_pair[1]==x.inner_pair[0]+1 for x in h)})
h6=compile_nnmhv_histories(6)
checks={'vanishes_below_minimal_multiplicity':rows[0]['histories']==0,'six_point_has_one_boundary_sensitive_history':len(h6)==1,'all_pairs_obey_source_separation':all(b>=a+2 for n in range(6,11) for x in compile_nnmhv_histories(n) for a,b in (x.outer_pair,x.inner_pair)),'six_point_is_single_left_nested_base_case':{x.branch for x in h6}=={'left-nested'},'boundary_updates_match_source_superscripts':all(all(u.replacement_path==x.outer_pair for u in x.boundary_updates) for x in h6),'history_count_strictly_grows':all(rows[i]['histories']<rows[i+1]['histories'] for i in range(1,len(rows)-1))}
out={'schema':'marici.nima.nnmhv-coherence-path-compiler.v1','source':'arXiv:0808.2475 equations PNNMHVnew, superscripts, Lrep, Urep','finite_counts':rows,'six_point_histories':[{'outer':list(x.outer_pair),'inner':list(x.inner_pair),'branch':x.branch,'prefix':list(x.inner_prefix),'updates':[{'side':u.side,'path':list(u.replacement_path)} for u in x.boundary_updates]} for x in h6],'checks':checks,'passed':all(checks.values()),'count_formula':'C(n-2,4)+C(n-3,4)','scope':'Combinatorial compilation of the authored separated-pair nested sums with typed boundary updates; generalized-R weights are not yet evaluated.'}
p=ROOT/'research/nima/results/nnmhv-coherence-path-compiler.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
