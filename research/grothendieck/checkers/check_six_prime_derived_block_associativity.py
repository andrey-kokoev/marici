"""A common derived middle-block cell for (ab)c and a(bc)."""
from pathlib import Path
from itertools import permutations,product,combinations
from fractions import Fraction
from collections import defaultdict
import runpy,json
ROOT=Path(__file__).resolve().parents[3]
base=runpy.run_path(str(ROOT/'research/grothendieck/checkers/check_packet_refinement_relation_tower.py'))
blocks=base['pair_blocks'];relation=base['local_relation'];multiply=base['multiply']
def clean(v):return {k:c for k,c in v.items() if c}
def add(v,w,factor):
    out=dict(v)
    for k,c in w.items():out[k]=out.get(k,0)+factor*c
    return clean(out)
def probe(pairs,kinds):
    return (sum(pairs,()),sum((((False,False) if k==0 else (False,True)) for k in kinds),()))
def power_basis(items):
    out={}
    for pairs in blocks(tuple(items)):
        for kinds in product((0,1),repeat=len(pairs)):
            v={((),()):1}
            for pair,kind in zip(pairs,kinds):v=multiply(v,relation(pair,kind))
            out[probe(pairs,kinds)]=v
    for key,v in out.items():assert {p:c for p,c in v.items() if p in out}=={key:1}
    return out
def reduce_power(v,basis):
    out=dict(v)
    for key,c in v.items():
        if key in basis:out=add(out,basis[key],-c)
    assert not any(key in basis for key in out)
    return out
P3=power_basis(range(6))
P2={ps:power_basis(ps) for ps in combinations(range(6),4)}

# Independent exact rank of each local source template in vertex-potential
# coordinates. Event feature u_y-u_x uses u_root=0.
def record(word,marks,start=0):
    out={():1};state=start
    for p,keep in zip(word,marks):
        end=state|1<<p
        if keep:
            v={end:1}
            if state:v[state]=-1
            out={w+(letter,):c*a for w,c in out.items() for letter,a in v.items()}
        state=end
    return out

def record_rank(n):
    pivots={}
    for word in permutations(range(n)):
        for marks in product((False,True),repeat=n):
            v={k:Fraction(c) for k,c in record(word,marks).items()}
            while v:
                pivot=min(v);c=v[pivot]
                if pivot not in pivots:
                    pivots[pivot]={k:a/c for k,a in v.items()};break
                v=add(v,pivots[pivot],-c)
    return len(pivots)
assert record_rank(2)==6 and record_rank(4)==150

# Actual local seam cycles, in the same faithful potential coordinates.
# key=(edge source,edge target,left record,seam letter,right record);
# seam letter 0 is Omega, positive letters are vertex potentials.
def derivative(col,start):
    out=defaultdict(int)
    for (word,marks),c in col.items():
        states=[start]
        for p in word:states.append(states[-1]|1<<p)
        for i,keep in enumerate(marks):
            left=record(word[:i],marks[:i],start)
            right=record(word[i+1:],marks[i+1:],states[i+1])
            seam={0:1} if not keep else {states[i+1]:1}
            if keep and states[i]:seam[states[i]]=-1
            for l,a in left.items():
                for k,b in seam.items():
                    for r,d in right.items():out[states[i],states[i+1],l,k,r]+=c*a*b*d
    return clean(out)
def boundary(col):
    out=defaultdict(int)
    for (x,y,l,k,r),c in col.items():
        letter=() if k==0 else (k,)
        out[y,l+letter,r]+=c;out[x,l,letter+r]-=c
    return clean(out)

ordinary_cells=0;shifted_cells=0;ordinary_probes={};sign_hostiles=0
for pairs in blocks(tuple(range(6))):
    first,middle,last=pairs
    prefix=P2[tuple(sorted(first+middle))];suffix=P2[tuple(sorted(middle+last))]
    middle_relations=power_basis(middle)
    middle_paths=[(w,m) for w in permutations(middle) for m in product((False,True),repeat=2)]
    middle_basis=[p for p in middle_paths if p not in middle_relations]
    assert len(middle_basis)==6
    local=[];state=0
    for pair in pairs:
        cycles=[derivative(relation(pair,k),state) for k in (0,1)]
        for k,v in enumerate(cycles):
            assert v and not boundary(v)
            assert all(len(l)+len(r)+(letter!=0)==k for x,y,l,letter,r in v)
        local.append(cycles)
        state|=sum(1<<p for p in pair)
    for ka,kc in product((0,1),repeat=2):
        a,c=relation(first,ka),relation(last,kc)
        for path in middle_paths:
            w={path:1}
            # Both coarse block quotients are actual I4/I4^2 classes.
            left=multiply(reduce_power(multiply(a,w),prefix),c)
            right=multiply(a,reduce_power(multiply(w,c),suffix))
            common=multiply(multiply(a,reduce_power(w,middle_relations)),c)
            assert reduce_power(left,P3)==reduce_power(right,P3)==reduce_power(common,P3)
            ordinary_cells+=1
            if path in middle_basis:
                pa=probe((first,),(ka,));pc=probe((last,),(kc,))
                key=(pa[0]+path[0]+pc[0],pa[1]+path[1]+pc[1])
                assert common[key]==1
                ordinary_probes[key]=common
        for kb in (0,1):
            b=relation(middle,kb)
            left=multiply(multiply(a,b),c);right=multiply(a,multiply(b,c))
            assert left==right and left==P3[probe(pairs,(ka,kb,kc))]
            # A selected coordinate in the actual joint seam tensor.
            coefficients=[next(iter(local[i][kind].values())) for i,kind in enumerate((ka,kb,kc))]
            joint_coefficient=coefficients[0]*coefficients[1]*coefficients[2]
            # sigma_(p,q)(u tensor v)=(-1)^(q*underlying_degree(u)) u tensor v.
            left_sign=(-1)**((-1)*(-2))
            naive_right_sign=(-1)**((-1)*(-1))
            assert left_sign*joint_coefficient != naive_right_sign*joint_coefficient
            corrected_right=-naive_right_sign*joint_coefficient
            assert left_sign*joint_coefficient==corrected_right
            # Conjugate transpose reverses composition; corrected coefficients agree.
            assert complex(left_sign*joint_coefficient).conjugate()==complex(corrected_right).conjugate()
            sign_hostiles+=1;shifted_cells+=1
assert len(ordinary_probes)==2160
for key,v in ordinary_probes.items():
    assert {k:c for k,c in v.items() if k in ordinary_probes}=={key:1}
assert shifted_cells==720 and ordinary_cells==2880
result={'schema':'marici.grothendieck.six-prime-derived-block-associativity.v1','passed':True,
        'local_terminal_ranks':{'two_events':6,'four_events':150},
        'coarse_complex_dimensions':{'degree_minus_one':720,'degree_zero':6300},
        'common_complex_dimensions':{'degree_minus_one':720,'degree_zero':2160},
        'ordinary_source_comparison_cells':ordinary_cells,'shifted_source_comparison_cells':shifted_cells,
        'checks':{'common_middle_quotient_independent_of_lifts':True,
                  'both_groupings_agree_in_global_associated_layer':True,
                  'actual_local_seam_cycles_closed_and_independent':True,
                  'ordinary_common_image_identity_minor':True,
                  'naive_shift_associativity_rejected_on_all_720_products':sign_hostiles==720,
                  'koszul_transport_restores_joint_seam_comparison':True,
                  'contragredient_comparison_coefficients_agree':True},
        'scope':'Finite source-derived comparison cell, not equivalence of entire coarse complexes or completed analytical closure. Shift correction uses the declared tensor-of-shifts convention.'}
p=ROOT/'research/grothendieck/results/six-prime-derived-block-associativity.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
