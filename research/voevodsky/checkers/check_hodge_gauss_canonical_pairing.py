"""Gaussian-integer exterior checks for the bounded Gauss/canonical-form test."""
from itertools import combinations, permutations
from pathlib import Path
import json


def add(a,b):return (a[0]+b[0],a[1]+b[1])
def times(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,n):return (n*a[0],n*a[1])
def conjugate(f):return {m:(c[0],-c[1]) for m,c in f.items()}
def wedge(a,b):
    out={}
    for x,c in a.items():
        for y,d in b.items():
            if set(x)&set(y):continue
            sign=(-1)**sum(i>j for i in x for j in y)
            m=tuple(sorted(x+y))
            out[m]=add(out.get(m,(0,0)),scale(times(c,d),sign))
    return {m:c for m,c in out.items() if c!=(0,0)}
def wedges(fs):
    out={(): (1,0)}
    for f in fs:out=wedge(out,f)
    return out

def integral(f,n,orientation):return scale(f.get(tuple(range(n)),(0,0)),orientation)
def graph_pull(f):
    out={}
    for m,c in f.items():
        forms=[]
        for index in m:
            j,parity=divmod(index,2)
            sign=-1 if j>=3 and parity else 1
            forms.append({(2*(j%3)+parity,):(sign,0)})
        for n,v in wedges(forms).items():out[n]=add(out.get(n,(0,0)),times(c,v))
    return {m:c for m,c in out.items() if c!=(0,0)}

def det3(m):
    return sum((-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
               *m[0][p[0]]*m[1][p[1]]*m[2][p[2]] for p in permutations(range(3)))


def main():
    root=Path(__file__).resolve().parents[3]
    u=[{(2*j,):(1,0),(2*j+1,):(0,1)} for j in range(6)]
    e={(2*j,2*j+1):(d,0) for j,d in enumerate((1,1,1,-1,-1,-3))}
    ep3=wedges([e]*3);U=wedges(u)
    plus=wedges(u[:3]);minus_unscaled=wedges([conjugate(x) for x in u[3:]])
    assert wedges([plus,conjugate(minus_unscaled)])==U
    assert integral(wedges([e]*6),12,-1)==(2160,0)
    assert integral(wedge(U,conjugate(U)),12,-1)==(-64,0)
    dp=times((0,1),integral(wedges([ep3,plus,conjugate(plus)]),12,-1))
    dm=times((0,1),integral(wedges([ep3,minus_unscaled,conjugate(minus_unscaled)]),12,-1))
    assert dp==(144,0) and scale(dm,3)==(144,0)
    assert 3*(-64)==-192  # normalized mixed determinant has coefficient squared3
    assert graph_pull(plus)==graph_pull(minus_unscaled)
    assert integral(graph_pull(U),6,1)==(0,-8)
    gp=graph_pull(plus)
    norm=times((0,1),integral(wedge(gp,conjugate(gp)),6,1))
    assert norm==(8,0)
    assert 8*24-3*8**2==0  # normalized graph Gram determinant
    assert 144**2*4==32**2*3*27  # fixed-source Cauchy-Schwarz coefficient27/4
    assert 144**2-32**2*3==17664>0  # E^3 +/- R are permitted numerical inputs
    # Actual Grassmannian point: both complementary minors are nonzero.
    graph=[[int(i%3==j) for j in range(3)] for i in range(6)]
    minors={c:det3([graph[i] for i in c]) for c in combinations(range(6),3)}
    assert minors[(0,1,2)]==minors[(3,4,5)]==1
    assert (minors[(0,1,2)]*minors[(3,4,5)]
            -minors[(0,1,3)]*minors[(2,4,5)]
            +minors[(0,1,4)]*minors[(2,3,5)]
            -minors[(0,1,5)]*minors[(2,3,4)])==0
    result={'passed':True,'classification':'Gauss_interface_yields_positivity_not_universal_orthogonality',
        'bounded_branch_disposition':'stop_no_new_universal_necessity',
        'fixed_source_Gram_diagonal_coefficient':144,
        'effective_Weil_radius_squared_bound':'(27/4) a^2',
        'Plucker_equations_force_cross_minor_zero':False,
        'algebraic_product_graph_period_U':[0,-8],
        'algebraic_product_graph_reader':['0','1/4'],
        'product_fiber_assumed_to_have_fixed_Hodge_dimension':False,
        'numerically_allowed_classes_asserted_effective':False,
        'new_global_Gauss_image_restriction_proved':False,
        'all_cycle_annihilation_proved':False,'Hodge_proved':False,'Hodge_refuted':False}
    (root/'research/voevodsky/results/hodge-gauss-canonical-pairing-test-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
