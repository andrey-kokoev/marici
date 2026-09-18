#!/usr/bin/env python3
"""Seed and typed frontier for the NNMHV positroid decomposition."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/nima'))
from nnmhv_coherence_paths import compile_nnmhv_histories
from nnmhv_positroid_cells import top_cell,nnmhv_cell_requests
seed=top_cell(2,6,0);requests=nnmhv_cell_requests(7)
checks={'six_point_unique_history':len(compile_nnmhv_histories(6))==1,'six_point_cell_is_eight_dimensional':seed.dimension==8,'six_point_affine_permutation_has_k_two':sum(seed.affine_permutation[i]-(i+1) for i in range(6))//6==2,'necklace_has_six_two_subsets':len(seed.grassmann_necklace)==6 and all(len(x)==2 for x in seed.grassmann_necklace),'all_six_seven_point_histories_typed':len(requests)==6,'seven_point_targets_are_eight_dimensional':all(r['target_dimension']==8 for r in requests)}
out={'schema':'marici.nima.nnmhv-positroid-seed.v1','six_point_seed':{'geometry':'top cell G_+(2,6)','affine_permutation':list(seed.affine_permutation),'grassmann_necklace':[list(x) for x in seed.grassmann_necklace],'dimension':seed.dimension},'seven_point_cell_requests':requests,'checks':checks,'passed':all(checks.values()),'frontier':'Derive an on-shell graph or equivalent rank table for each n=7 history; only then compute its decorated permutation and C-matrix chart.'};p=ROOT/'research/nima/results/nnmhv-positroid-seed.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
