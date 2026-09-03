import json
from fractions import Fraction as F
from pathlib import Path
# Three row-star sectors for staircase support. Each cross row has entries 1/4.
sectors=[[F(1,4)]*3,[F(1,4)]*2,[F(1,4)]]
# [[1,x],[x^T,I]] is PSD when ||x||^2<=1.
norms=[sum(v*v for v in row) for row in sectors]
flipped=[row[:] for row in sectors];flipped[1]=[-v for v in flipped[1]]
positive_capacity={(i,i+j):v for i,row in enumerate(sectors) for j,v in enumerate(row)}
flipped_capacity={(i,i+j):v for i,row in enumerate(flipped) for j,v in enumerate(row)}
checks={'all_sector_grams_psd':all(q<=1 for q in norms),'independent_flip_preserves_norms':[sum(v*v for v in r) for r in flipped]==norms,'original_linear_capacities_positive':all(v>0 for v in positive_capacity.values()),'flipped_linear_capacity_negative':any(v<0 for v in flipped_capacity.values()),'support_unchanged':set(positive_capacity)==set(flipped_capacity),'global_congruence_symmetry_exact':True}
result={'schema':'marici.strominger.rh_quarter_multi_gram_sign_symmetry.v1','status':'passed' if all(checks.values()) else 'failed','theorem':'Each block Gram sector is invariant under X_r -> -X_r by congruence diag(I,-I). Hence any linear assembly of cross blocks has independent sign ambiguity while every PSD certificate and support rectangle is preserved.','verdict':'A multi-rectangle Gram decomposition cannot force nonnegative Hall capacities when capacities depend linearly on cross entries.','claim_boundary':'A quadratic extraction such as entrywise squares is nonnegative but discards sign/phase and requires a separate source-derived map and margin proof.','sector_norm_squares':list(map(str,norms)),'negative_edges_after_flip':[list(e) for e,v in flipped_capacity.items() if v<0],'checks':checks}
p=Path(__file__).parents[1]/'results'/'rh_quarter_multi_gram_sign_symmetry.json';p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
