"""Four-factor balanced pentagon, suspension signs and relative currents.

Collision packets are formal pairwise slot kernels, not spectral samples.
Nine-event fixtures exercise nonminimal factorization at four relation factors.
"""
from itertools import product
from pathlib import Path
from collections import defaultdict
import importlib.util
import json

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('descent',Path(__file__).with_name('check_seven_event_factorization_descent.py'))
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
# Pentagon A-B-C-D and A-E-D, with leaf order fixed.
TREES=((((0,1),2),3),((0,(1,2)),3),(0,((1,2),3)),(0,(1,(2,3))),((0,1),(2,3)))


def leaves(tree):
    return (tree,) if isinstance(tree,int) else leaves(tree[0])+leaves(tree[1])


def schedule(tree):
    if isinstance(tree,int):return ()
    left,right=tree
    return schedule(left)+schedule(right)+(max(leaves(left)),)


def shift_exponent(tree,degrees,shifts):
    if isinstance(tree,int):return 0
    left,right=tree
    return (shift_exponent(left,degrees,shifts)+shift_exponent(right,degrees,shifts)
            +sum(shifts[i] for i in leaves(right))*sum(degrees[i] for i in leaves(left)))


def differential_exponent(tree,index,degrees):
    if isinstance(tree,int):
        assert tree==index
        return 0
    left,right=tree
    if index in leaves(left):return differential_exponent(left,index,degrees)
    return sum(degrees[i] for i in leaves(left))+differential_exponent(right,index,degrees)


def sign(exponent):return -1 if exponent%2 else 1


def check_signs():
    differential_checks=shift_checks=0
    for degrees in product((-1,0),repeat=4):
        for tree in TREES:
            assert leaves(tree)==(0,1,2,3)
            for i,d in enumerate(degrees):
                if d==-1:
                    assert sign(differential_exponent(tree,i,degrees))==sign(sum(degrees[:i]))
                    differential_checks+=1
        for shifts in product((-2,-1,0,1,2),repeat=4):
            canonical=sum(shifts[j]*degrees[i] for i in range(4) for j in range(i+1,4))
            assert all(sign(shift_exponent(t,degrees,shifts))==sign(canonical) for t in TREES)
            for i,d in enumerate(degrees):
                if d==-1:
                    raised=list(degrees);raised[i]=0
                    after=sum(shifts[j]*raised[k] for k in range(4) for j in range(k+1,4))
                    source=shifts[i]+sum(degrees[k]-shifts[k] for k in range(i))
                    target=sum(shifts)+sum(degrees[:i])
                    assert sign(source+after)==sign(canonical+target)
            shift_checks+=1
    # A omitted suspension sign gives a concrete chain mismatch.
    degrees=(-1,-1,-1,-1);shifts=(0,1,0,0);i=0
    source=shifts[i]+sum(degrees[k]-shifts[k] for k in range(i))
    target=sum(shifts)+sum(degrees[:i])
    assert sign(source)!=sign(target)
    # Associators themselves are signless; no permutations occur.
    return differential_checks,shift_checks


def state_shape(degrees,cuts,mask):
    slots=[];labels=[]
    for i in range(3):
        if mask&(1<<i):slots.append((degrees[2*i]+degrees[2*i+1],))
        else:
            slots.append((degrees[2*i],degrees[2*i+1]));labels.append((i,cuts[i]))
    return tuple(slots),tuple(labels)


def check_currents():
    # Six internal memory slots, in three adjacent suffix/prefix pairs.
    # Two admissible intermediate vertex choices per interface are retained.
    shapes=list(product(product((0,1),repeat=6),product((0,1),repeat=3)))
    images=[[state_shape(deg,cut,mask) for mask in range(8)] for deg,cut in shapes]
    schedules=[schedule(t) for t in TREES]
    assert schedules==[(0,1,2),(1,0,2),(1,2,0),(2,1,0),(0,2,1)]
    paths=[]
    for order in schedules:
        mask=0;path=[mask]
        for boundary in order:mask|=1<<boundary;path.append(mask)
        assert mask==7
        paths.append(path)
    new_pairs=0;packet_checks=0
    for i,(degrees,cuts) in enumerate(shapes):
        for j,(other,other_cuts) in enumerate(shapes):
            equal=[images[i][mask]==images[j][mask] for mask in range(8)]
            totals=[]
            for path in paths:
                total=0
                for before,after in zip(path,path[1:]):
                    assert not equal[before] or equal[after]
                    # Operational new-match constructor, not a Gram subtraction.
                    total+=int(not equal[before] and equal[after])
                totals.append(total)
            assert len(set(totals))==1 and totals[0]==int(equal[7] and not equal[0])
            if totals[0]:
                new_pairs+=1
                # Formal features retain their own spectral and signature
                # labels. Neither rebracketing nor slot merging changes them.
                left=tuple(('L',i,slot,slot%2) for slot,n in enumerate(degrees) if n)
                right=tuple(('R',j,slot,(slot+1)%2) for slot,n in enumerate(other) if n)
                assert len(left)==len(right)
                packet=('Q_root(x,y)',2*len(left),tuple(zip(left,right)))
                decorated=[]
                for path in paths:
                    contributions=[packet for before,after in zip(path,path[1:])
                                   if not equal[before] and equal[after]]
                    assert len(contributions)==1
                    decorated.append(contributions[0])
                assert all(p==packet for p in decorated)
                packet_checks+=1
    return len(shapes),len(shapes)**2,new_pairs,packet_checks


def normal(columns):
    out=defaultdict(int)
    for terms in product(*(c.items() for c in columns)):
        markers=[];buffers=[];coefficient=1
        for i,(key,c) in enumerate(terms):
            x,y,u,keep,v=key;coefficient*=c
            markers.append(('e',x,y,keep))
            if i==0:buffers.append(u)
            else:buffers[-1]=buffers[-1]+u
            buffers.append(v)
        out[tuple(markers),tuple(buffers)]+=coefficient
    return f.clean(out)


def normal_tree(tree,columns):
    if isinstance(tree,int):
        return {((('e',x,y,k),),(u,v)):c for (x,y,u,k,v),c in columns[tree].items()}
    left=normal_tree(tree[0],columns);right=normal_tree(tree[1],columns)
    out=defaultdict(int)
    for (lm,lb),a in left.items():
        for (rm,rb),b in right.items():
            out[lm+rm,lb[:-1]+(lb[-1]+rb[0],)+rb[1:]]+=a*b
    return f.clean(out)


def derivative_factors(factors):
    state=0;columns=[];cuts=[]
    for factor in factors:
        column=f.derivative(state,factor)
        assert column and not f.boundary(column)
        columns.append(column)
        word=next(iter(factor))[0]
        state|=sum(1<<j for j in word)
        cuts.append(state)
    assert state==511
    return columns,tuple(cuts[:-1])


def check_descent():
    blocks=((0,1),(3,4),(5,6),(7,8));extra=2
    checks=0
    for kinds in ((0,0,0,0),(1,0,1,0)):
        for mark in (0,1):
            original=[f.relation(pair,kind) for pair,kind in zip(blocks,kinds)]
            arrow={((extra,),(mark,)):1}
            for boundary in range(3):
                left=original.copy();right=original.copy()
                left[boundary]=f.multiply(left[boundary],arrow)
                right[boundary+1]=f.multiply(arrow,right[boundary+1])
                assert f.chain_product(left)==f.chain_product(right)
                dl,cl=derivative_factors(left);dr,cr=derivative_factors(right)
                assert cl!=cr
                nl,nr=normal(dl),normal(dr)
                assert nl==nr and nl
                assert not f.balanced_boundary(nl)
                for tree in TREES:
                    assert normal_tree(tree,dl)==nl
                    assert normal_tree(tree,dr)==nl
                checks+=1
    return checks


def main():
    d_checks,s_checks=check_signs()
    shapes,pairs,new,packets=check_currents()
    descent=check_descent()
    result={'schema':'marici.nima.balanced-relative-pentagon.v1','passed':True,
        'balanced_parenthesizations':5,'tensor_differential_sign_checks':d_checks,
        'degree_and_shift_configurations':s_checks,'typed_memory_shapes':shapes,
        'ordered_shape_pairs':pairs,'new_matching_pairs':new,
        'formal_pairwise_kernel_packets_compared':packets,
        'nine_event_balancing_fixtures':descent,
        'checks':{'two_pentagon_paths_have_same_normalization':True,
                  'all_five_current_transport_totals_agree':True,
                  'no_associator_koszul_sign_inserted':True,
                  'tensor_of_shifts_chain_identity':True,
                  'omitted_shift_sign_hostile':True,
                  'nonminimal_factorization_and_parenthesization_commute':True},
        'scope':'Finite four-factor balanced pentagon and source-constructed collision packets below common capacity. Formal kernels retain each spectral pair and the root factor; tail-current identities are inherited, not numerically evaluated. No full nine-event rank, Green-isometry of raw compression, or completed packet limit is asserted.'}
    out=ROOT/'research/nima/results/balanced-relative-pentagon.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
