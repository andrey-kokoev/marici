#!/usr/bin/env python3
"""How much smooth-tail Gram can be absorbed relative to the directed jump-tail shape?"""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';S=np.load(root/'regularized_union_tail_maps_L0649_L065.npz')['schur'][4];T=np.load(root/'residual_jump_variation_gram_L06495.npz')['tail_gram'];alpha=1.067569476012246
def f(c):return float(np.linalg.eigvalsh((S-c*T/alpha+(S-c*T/alpha).T)/2)[0])
lo,hi=0.,1000.
for _ in range(100):
 mid=(lo+hi)/2
 if f(mid)>0:lo=mid
 else:hi=mid
out={'schema':'marici.voevodsky.smooth-tail-allocation-vs-jump-gram.v1','maximum_total_tail_multiplier_before_loss_of_positivity':lo,'available_smooth_multiplier_beyond_jump':lo-1,'lower_at_total_multiplier_8':f(8),'interpretation':'directional reserve only; PSD domination is impossible because the jump Gram is rank deficient','passed':False,'rh_proved':False};p=root/'smooth_tail_allocation_vs_jump_gram.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
