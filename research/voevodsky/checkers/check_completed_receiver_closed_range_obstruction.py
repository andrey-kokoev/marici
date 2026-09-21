"""Exact forgotten-suffix family for the weighted receiver range obstruction."""
from pathlib import Path
import runpy
import json
ROOT=Path(__file__).resolve().parents[3]
b=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))
rel,mul,D=b['relation'],b['multiply'],b['derivative']
base=rel((0,1),0)
base_image=D(0,base)
assert sum(abs(c) for c in base_image.values())==4
witness=(0,1,(),0,())
assert base_image[witness]==1
fixtures=[]
for n in (2,3,4,8,16,32,64):
    suffix={(tuple(range(2,n)),(0,)*(n-2)):1}
    column=mul(base,suffix)
    image=D(0,column)
    assert image==base_image
    assert sum(abs(c) for c in column.values())==2
    # a>=1, so (n+1) is a conservative lower bound on the quotient norm.
    fixtures.append({'events':n,'source_quotient_norm_lower_bound':n+1,
                     'target_cut_l1_norm':4,
                     'unit_source_image_norm_upper_bound':f'4/{n+1}'})
result={'passed':True,'forgotten_suffix_fixtures':fixtures,
 'scope':'Exact derivative images. Quotient lower bound uses a coordinate functional annihilating I^2; nonclosed range follows from the Banach inverse theorem in the companion note. No spectral approximation.'}
out=ROOT/'research/voevodsky/results/completed-receiver-closed-range-obstruction.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
