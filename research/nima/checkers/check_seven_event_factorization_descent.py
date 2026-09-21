"""Seven-event I^3 presentation and balanced seam descent.

The full 645120-row source matrix is not materialized. A 20160-column
identity minor certifies independence of all degree-one balancing relations;
flatness in the companion note proves these generate the multiplication kernel.
"""
from itertools import combinations, permutations, product
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from math import factorial
import json

ROOT=Path(__file__).resolve().parents[3]


def clean(d):return {k:v for k,v in d.items() if v}


def pairs(items):
    if not items:
        yield ();return
    for pair in combinations(items,2):
        for tail in pairs(tuple(j for j in items if j not in pair)):
            yield (pair,)+tail


def relation(pair,kind):
    p,q=pair
    patterns=((0,0),) if kind==0 else ((0,1),(1,0))
    return {((p,q),m):1 for m in patterns}|{((q,p),m):-1 for m in patterns}


def multiply(a,b):
    out=defaultdict(int)
    for (u,mu),x in a.items():
        for (v,mv),y in b.items():out[u+v,mu+mv]+=x*y
    return clean(out)


def chain_product(columns):
    out={((),()):1}
    for column in columns:out=multiply(out,column)
    return out


def feature(x,y,keep):
    if not keep:return {():1}
    # Independent vertex potentials, with u_root=0.
    return {(y,):1}|({(x,):-1} if x else {})


def record(start,word,marks):
    out={():1};state=start
    for p,keep in zip(word,marks):
        assert not state&(1<<p)
        end=state|(1<<p);nxt=defaultdict(int)
        for u,c in out.items():
            for v,b in feature(state,end,keep).items():nxt[u+v]+=c*b
        out=clean(nxt);state=end
    return out


def rank(columns):
    basis={}
    for column in columns:
        v={k:Fraction(c) for k,c in column.items() if c}
        while v:
            p=min(v);c=v[p]
            if p not in basis:
                basis[p]={k:a/c for k,a in v.items()};break
            for k,a in basis[p].items():
                value=v.get(k,Fraction(0))-c*a
                if value:v[k]=value
                else:v.pop(k,None)
    return len(basis)


def derivative(start,column):
    out=defaultdict(int)
    for (word,marks),coefficient in column.items():
        states=[start]
        for j in word:states.append(states[-1]|(1<<j))
        for i,keep in enumerate(marks):
            left=record(start,word[:i],marks[:i])
            right=record(states[i+1],word[i+1:],marks[i+1:])
            for u,a in left.items():
                for v,b in right.items():
                    # The seam letter remains the actual marked generator.
                    out[states[i],states[i+1],u,keep,v]+=coefficient*a*b
    return clean(out)


def boundary(column):
    out=defaultdict(int)
    for (x,y,u,keep,v),c in column.items():
        for letter,b in feature(x,y,keep).items():
            out[y,u+letter,v]+=c*b;out[x,u,letter+v]-=c*b
    return clean(out)


def raw_joint(cuts,columns):
    return {(cuts,)+tuple(k for k,c in entries):
            entries[0][1]*entries[1][1]*entries[2][1]
            for entries in product(*(column.items() for column in columns))}


def balanced(raw):
    out=defaultdict(int)
    for (_,a,b,c),coefficient in raw.items():
        x,y,u,k,v=a;xx,yy,uu,kk,vv=b;xxx,yyy,uuu,kkk,vvv=c
        separators=(('e',x,y,k),('e',xx,yy,kk),('e',xxx,yyy,kkk))
        buffers=(u,v+uu,vv+uuu,vvv)
        out[separators,buffers]+=coefficient
    return clean(out)


def balanced_boundary(column):
    out=defaultdict(int)
    for (separators,buffers),c in column.items():
        assert all(marker[0]=='e' for marker in separators)
        for i,(_,x,y,keep) in enumerate(separators):
            for word,b in feature(x,y,keep).items():
                marks=list(separators);bs=list(buffers)
                marks[i]=('v',y);bs[i]=bs[i]+word
                out[tuple(marks),tuple(bs)]+=(-1)**i*c*b
                marks=list(separators);bs=list(buffers)
                marks[i]=('v',x);bs[i+1]=word+bs[i+1]
                out[tuple(marks),tuple(bs)]-=(-1)**i*c*b
    return clean(out)


def vacuum_collision_check(left,right):
    # Independent constructor: pair distinct fine vacuum shapes exactly
    # when memory-slot merging gives the same typed balanced shape.
    keys=set(left)|set(right)
    normal={key:next(iter(balanced({key:1}))) for key in keys}
    def fine(x,y):return sum(c*y.get(k,0) for k,c in x.items())
    def current(x,y):
        return sum(a*b for k,a in x.items() for l,b in y.items()
                   if k!=l and normal[k]==normal[l])
    kernel=defaultdict(int)
    for k,c in left.items():kernel[k]+=c
    for k,c in right.items():kernel[k]-=c
    kernel=clean(kernel)
    for x in (left,right,kernel):
        for y in (left,right,kernel):
            assert fine(x,y)+current(x,y)==fine(balanced(x),balanced(y))
    assert fine(kernel,kernel)==128 and current(kernel,kernel)==-128
    assert fine(left,right)==0 and current(left,right)==64
    assert not balanced(kernel)
    return {'raw_kernel_self_pairing':128,'collision_current_on_kernel':-128,
            'new_cross_pairing':64,'corrected_kernel_pairing':0}


def local_three_event_check():
    contexts=[]
    for pair in combinations(range(3),2):
        e=next(j for j in range(3) if j not in pair)
        for kind,mark in product((0,1),repeat=2):
            r=relation(pair,kind);arrow={((e,),(mark,)):1}
            contexts.extend((multiply(r,arrow),multiply(arrow,r)))
    columns=[record(0,w,m) for w in permutations(range(3)) for m in product((0,1),repeat=3)]
    assert rank(columns)==26 and rank(contexts)==22
    for context in contexts:
        observed=defaultdict(int)
        for (w,m),c in context.items():
            for key,v in record(0,w,m).items():observed[key]+=c*v
        assert not clean(observed)
    return 22


def specs():
    for e in range(7):
        for blocks in pairs(tuple(j for j in range(7) if j!=e)):
            for kinds in product((0,1),repeat=3):
                for mark in (0,1):yield e,blocks,kinds,mark


def probe(e,blocks,kinds,mark,interface):
    factors=[(pair,((0,0) if kind==0 else (0,1))) for pair,kind in zip(blocks,kinds)]
    factors.insert(interface+1,((e,),(mark,)))
    return tuple(j for w,m in factors for j in w),tuple(j for w,m in factors for j in m)


def main():
    local_dimension=local_three_event_check()
    indices={}
    for interface in (0,1):
        component=322 if interface==0 else 223
        for specification in specs():
            key=(component,probe(*specification,interface))
            assert key not in indices
            indices[key]=len(indices)
    assert len(indices)==20160
    checked=0
    for interface in (0,1):
        component=322 if interface==0 else 223
        for e,blocks,kinds,mark in specs():
            a,b,c=[relation(pair,kind) for pair,kind in zip(blocks,kinds)]
            arrow={((e,),(mark,)):1}
            if interface==0:
                positive=chain_product((multiply(a,arrow),b,c))
                negative=chain_product((a,multiply(arrow,b),c))
            else:
                positive=chain_product((a,b,multiply(arrow,c)))
                negative=chain_product((a,multiply(b,arrow),c))
            assert positive==negative and positive
            # Selected rows live in the two extreme factorization types;
            # the negative (232) component contributes to none of them.
            selected={indices[component,k]:v for k,v in positive.items() if (component,k) in indices}
            j=indices[component,probe(e,blocks,kinds,mark,interface)]
            assert selected=={j:1}
            checked+=1
    assert checked==20160

    # Explicit raw seam failure and normal-form repair for all marking types
    # of one seven-event placement, at BOTH internal factor boundaries.
    blocks=((0,1),(3,4),(5,6));e=2;seam_checks=0;collision=None
    for kinds in product((0,1),repeat=3):
        for mark in (0,1):
            a,b,c=[relation(pair,kind) for pair,kind in zip(blocks,kinds)]
            arrow={((e,),(mark,)):1}
            m2=sum(1<<j for j in blocks[0]);m3=m2|(1<<e)
            m4=m2|sum(1<<j for j in blocks[1]);m5=m4|(1<<e)
            cases=(
                ((m3,m5),(derivative(0,multiply(a,arrow)),derivative(m3,b),derivative(m5,c)),
                 (m2,m5),(derivative(0,a),derivative(m2,multiply(arrow,b)),derivative(m5,c))),
                ((m2,m4),(derivative(0,a),derivative(m2,b),derivative(m4,multiply(arrow,c))),
                 (m2,m5),(derivative(0,a),derivative(m2,multiply(b,arrow)),derivative(m5,c))))
            for cuts_l,dl,cuts_r,dr in cases:
                assert all(dl) and all(dr)
                assert all(not boundary(d) for d in dl+dr)
                raw_l,raw_r=raw_joint(cuts_l,dl),raw_joint(cuts_r,dr)
                assert raw_l and raw_r and set(raw_l).isdisjoint(raw_r)
                if collision is None:
                    assert kinds==(0,0,0) and mark==0
                    collision=vacuum_collision_check(raw_l,raw_r)
                bl,br=balanced(raw_l),balanced(raw_r)
                assert bl==br and bl
                assert not balanced_boundary(bl)
                # Actual seam edges and all FOUR typed coefficient buffers
                # survive the normalization; it is not scalar forgetting.
                assert all(len(markers)==3 and len(buffers)==4 for markers,buffers in bl)
                seam_checks+=1
    assert seam_checks==32

    raw_dimension=3*(factorial(7)//(factorial(3)*factorial(2)**2))*local_dimension*2*2
    kernel_dimension=len(indices)
    assert raw_dimension==55440 and raw_dimension-kernel_dimension==35280
    result={'schema':'marici.nima.seven-event-factorization-descent.v1','passed':True,
        'local_three_event_terminal_rank':26,'local_three_event_ideal_dimension':local_dimension,
        'raw_factorization_dimension':raw_dimension,
        'independent_balancing_relations_identity_minor':kernel_dimension,
        'I_cubed_dimension_from_flatness_and_kernel_minor':raw_dimension-kernel_dimension,
        'raw_joint_seam_descent_hostiles_and_balanced_repairs':seam_checks,
        'normal_form_retained_seams':3,'normal_form_retained_coefficient_buffers':4,
        'source_constructed_vacuum_collision_descent':collision,
        'scope':'Exact source potential coordinates, a 20160-column balancing identity minor, and 32 literal seam comparisons. Completeness of the kernel and faithful general balanced descent use hereditary-flatness proofs in the note. No 645120-row global rank computation, spectral sampling, or Green-isometry claim is made.'}
    out=ROOT/'research/nima/results/seven-event-factorization-descent.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
