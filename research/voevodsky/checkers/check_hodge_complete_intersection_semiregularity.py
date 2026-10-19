"""Exact specialized trace/Lefschetz model; geometric transgression is a written input."""
from itertools import combinations
from pathlib import Path
import json
from check_hodge_deligne_lift_image import rank


def wedge(a,b):
    out={}
    for x,c in a.items():
        for y,d in b.items():
            if set(x)&set(y):continue
            z=tuple(sorted(x+y));sign=(-1)**sum(i>j for i in x for j in y)
            out[z]=out.get(z,0)+sign*c*d
    return {z:c for z,c in out.items() if c}


def main():
    root=Path(__file__).resolve().parents[3]
    prior=json.loads((root/'research/voevodsky/results/hodge-transverse-infinitesimal-interface-v1.json').read_text(encoding='utf-8'))
    assert prior['passed'] and prior['smooth_control_h1_normal']==135
    pairs=list(combinations(range(6),2))
    rows=[a+tuple(i+6 for i in b) for a in pairs for b in combinations(range(6),4)]
    l={(i,i+6):1 for i in range(6)};l2=wedge(l,l)
    images=[wedge(l2,{tuple(i+6 for i in b):1}) for b in pairs]
    lef=[[image.get(row,0) for image in images] for row in rows]
    assert rank(lef)==15
    cols=[(i,j,a) for i in range(3) for j in range(3) for a in range(15)]
    sigma=[[lef[r][a] if i==j else 0 for i,j,a in cols] for r in range(225)]
    assert rank(sigma)==15
    kernel=[]
    for index,(i,j,a) in enumerate(cols):
        if i!=j:
            v=[0]*135;v[index]=1;kernel.append(v)
    for i in (0,1):
        for a in range(15):
            v=[0]*135;v[cols.index((i,i,a))]=1;v[cols.index((2,2,a))]=-1;kernel.append(v)
    assert len(kernel)==120 and rank(kernel)==120
    assert all(sum(x*y for x,y in zip(row,v))==0 for row in sigma for v in kernel)
    # Ambient contraction: the alternating quotient of a 6 by 6 matrix.
    alt=[[int((i,j)==(a,b))-int((i,j)==(b,a)) for i in range(6) for j in range(6)] for a,b in pairs]
    assert rank(alt)==15 and 36-rank(alt)==21
    ob=[[alt[a][k] if i==j else 0 for k in range(36)] for i,j,a in cols]
    assert rank(ob)==15
    composed=[[sum(sigma[r][j]*ob[j][k] for j in range(135)) for k in range(36)] for r in range(225)]
    expected=[[3*sum(lef[r][a]*alt[a][k] for a in range(15)) for k in range(36)] for r in range(225)]
    assert composed==expected and rank(composed)==15
    result={'passed':True,'classification':'complete_intersection_trace_semiregularity_rank15_kernel120',
        'normal_obstruction_space_dimension':135,'semiregularity_target_dimension':225,
        'semiregularity_rank':15,'semiregularity_kernel_dimension':120,
        'ambient_obstruction_image_dimension':15,'polarized_tangent_dimension':21,
        'ambient_obstruction_image_intersection_semiregularity_kernel_dimension':0,
        'semiregularity_injective':False,'polarized_control_actually_lifts':True,
        'rank_formula_input':'Koszul-Atiyah transgression sigma(beta)=l^2 tr(beta)',
        'unknown_Weil_cycle_obstruction_computed':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Noncommuting bundle deformation obstruction and a separately justified comparison with embedded-cycle obstructions.'}
    (root/'research/voevodsky/results/hodge-complete-intersection-semiregularity-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
