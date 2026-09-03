#!/usr/bin/env python3
"""Construct the minimal labelled chain cospan on exceptional points -1,0,+1."""
import json
from pathlib import Path
# Rows: central plus, central minus, moving plus, moving minus.
# Columns: edge 0->+1 and edge -1->0.
D=[[ -1,0],[0,1],[1,0],[0,-1]]
assert [sum(D[i][j] for i in range(4)) for j in range(2)]==[0,0]
# Forget central occurrence labels: endpoint boundary of the summed chain is (+1)-(-1).
endpoint=[D[2][0]+D[2][1],D[3][0]+D[3][1]];assert endpoint==[1,-1]
out={'schema':'marici.benincasa.cosmology-normalized-three-point-conductor-cospan.v1','points':[-1,0,1],'edge_chains':['0 -> +1','-1 -> 0'],'row_labels':['central b+x at r=0','central a+y at r=0','moving b+x-E at r=+1','moving a+y-E at r=-1'],'boundary_matrix':D,'each_edge_boundary_sum_zero':True,'central_occurrences_retained_separately':True,'forgotten_central_endpoint_boundary':[1,-1],'matches_abstract_endpoint_orientation':True,'combinatorial_cospan_constructed':True,'source_geometric_cospan_constructed':False,'precise_gap':'the existing endpoint chain uses coordinate xi; no source map identifies xi with the exceptional coordinate r and its four labelled wall trajectories','consequence':'the matrix is the minimal chain shape and satisfies boundary-of-boundary zero, but it cannot yet carry residues or Gauss-Manin transport','next_test':'derive or obstruct a source coordinate map xi -> r matching endpoint ports and both central/moving wall labels','passed':True}
R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_normalized_three_point_conductor_cospan.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
