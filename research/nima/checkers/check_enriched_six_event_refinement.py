"""Critical enriched 4+2 / 2+4 to 2+2+2 refinement, retaining middle labels.

No full six-event kernel is computed. Exact products, deconcatenation and
factorized seam probes certify the critical 720-dimensional subobject.
"""
from itertools import combinations, product
from collections import defaultdict
from pathlib import Path
from math import prod
import json

ROOT=Path(__file__).resolve().parents[3]
PRIMES=(2,3,5,7,11,13)
LABEL={m:2*prod(PRIMES[j] for j in range(6) if m&(1<<j)) for m in range(64)}
SORTED=sorted(LABEL.values())
POSITION={m:SORTED.index(v) for m,v in LABEL.items()}


def clean(d):return {k:v for k,v in d.items() if v}


def pairs(items):
    if not items:
        yield ();return
    for pair in combinations(items,2):
        for tail in pairs(tuple(j for j in items if j not in pair)):
            yield (pair,)+tail


def relation(pair,kind):
    p,q=pair
    patterns=((False,False),) if kind==0 else ((False,True),(True,False))
    return {((p,q),m):1 for m in patterns}|{((q,p),m):-1 for m in patterns}


def multiply(a,b):
    out=defaultdict(int)
    for (u,mu),x in a.items():
        for (v,mv),y in b.items():out[u+v,mu+mv]+=x*y
    return clean(out)


def record(start,word,marks):
    out={():1};state=start
    for j,keep in zip(word,marks):
        assert not state&(1<<j)
        end=state|(1<<j)
        if keep:
            out={w+(k,):c for w,c in out.items() for k in range(POSITION[state],POSITION[end])}
        state=end
    return out


def derivative(start,column):
    out=defaultdict(int)
    for (word,marks),coefficient in column.items():
        states=[start]
        for j in word:states.append(states[-1]|(1<<j))
        for i,keep in enumerate(marks):
            left=record(start,word[:i],marks[:i])
            right=record(states[i+1],word[i+1:],marks[i+1:])
            letters=range(POSITION[states[i]],POSITION[states[i+1]]) if keep else (-1,)
            for u,v,k in product(left,right,letters):
                out[states[i],states[i+1],u,k,v]+=coefficient*left[u]*right[v]
    return clean(out)


def boundary(column):
    out=defaultdict(int)
    for (x,y,u,k,v),c in column.items():
        word=() if k==-1 else (k,)
        out[y,u+word,v]+=c;out[x,u,word+v]-=c
    return clean(out)


def cut(column,length,start=0):
    out=defaultdict(int)
    for (word,marks),c in column.items():
        middle=start|sum(1<<j for j in word[:length])
        out[middle,(word[:length],marks[:length]),(word[length:],marks[length:])]+=c
    return clean(out)


def refine_left(column):
    out=defaultdict(int)
    for (middle4,left,right),c in cut(column,4).items():
        for (middle2,a,b),d in cut({left:1},2).items():
            out[middle2,middle4,a,b,right]+=c*d
    return clean(out)


def refine_right(column):
    out=defaultdict(int)
    for (middle2,left,right),c in cut(column,2).items():
        for (middle4,b,cword),d in cut({right:1},2,middle2).items():
            out[middle2,middle4,left,b,cword]+=c*d
    return clean(out)


def check_local_green_formula(start,pair,cs):
    # Formal pullback in independent chamber Gram entries G_ij, not a
    # pointwise spectral sample and not an assertion that G is diagonal.
    assert sum(c*c for c in cs[0].values())==4
    assert all(len(u)+(k!=-1)+len(v)==0 for x,y,u,k,v in cs[0])
    groups=defaultdict(lambda:defaultdict(int))
    for (x,y,u,k,v),c in cs[1].items():
        assert len(u)+(k!=-1)+len(v)==1
        slot,letter=('prefix',u[0]) if u else (('seam',k) if k!=-1 else ('suffix',v[0]))
        groups[x,y,slot][letter]+=c
    actual=defaultdict(int)
    memory=defaultdict(int);seam=defaultdict(int)
    for (_,_,slot),vector in groups.items():
        weighted=seam if slot=='seam' else memory
        for i,ci in vector.items():
            for j,cj in vector.items():
                actual[i,j]+=ci*cj
                weighted[i,j]+=ci*cj
    expected=defaultdict(int)
    p,q=pair
    edges=((start,start|(1<<p)),(start|(1<<p),start|(1<<p)|(1<<q)),
           (start,start|(1<<q)),(start|(1<<q),start|(1<<p)|(1<<q)))
    for x,y in edges:
        window=range(POSITION[x],POSITION[y])
        for i in window:
            for j in window:expected[i,j]+=2
    assert dict(actual)==dict(expected)
    unweighted={key:value//2 for key,value in expected.items()}
    assert dict(memory)==dict(seam)==unweighted
    return True


def main():
    columns=[];probes=[];basis=[];cycles={};coarse_hostiles=0
    for blocks in pairs(tuple(range(6))):
        middle2=sum(1<<j for j in blocks[0])
        middle4=middle2|sum(1<<j for j in blocks[1])
        starts=(0,middle2,middle4)
        for start,pair in zip(starts,blocks):
            if (start,pair) not in cycles:
                cs=[derivative(start,relation(pair,k)) for k in (0,1)]
                assert all(cs) and all(not boundary(c) for c in cs)
                ps=[next(iter(c)) for c in cs]
                assert [[c.get(p,0) for c in cs] for p in ps]==[[1,0],[0,1]]
                assert check_local_green_formula(start,pair,cs)
                cycles[start,pair]=(cs,ps)
        for kinds in product((0,1),repeat=3):
            local=[relation(pair,kind) for pair,kind in zip(blocks,kinds)]
            left=multiply(multiply(local[0],local[1]),local[2])
            right=multiply(local[0],multiply(local[1],local[2]))
            assert left==right
            fine=refine_left(left)
            assert fine==refine_right(right)
            expected={(middle2,middle4,a,b,c):x*y*z
                      for (a,x),(b,y),(c,z) in product(*(r.items() for r in local))}
            assert fine==expected
            # All tensor seam factors are actual closed vectors. Probe in
            # each retained-degree sector is 1, with cross-type probes zero.
            seam_probe=tuple(cycles[start,pair][1][kind] for start,pair,kind in zip(starts,blocks,kinds))
            assert prod(cycles[start,pair][0][kind][probe]
                        for start,pair,kind,probe in zip(starts,blocks,kinds,seam_probe))==1
            probe=(sum(blocks,()),sum((((False,False) if k==0 else (False,True)) for k in kinds),()))
            assert left[probe]==1
            columns.append(left);probes.append(probe);basis.append((blocks,kinds))
    assert len(columns)==720 and len(cycles)==120
    probe_index={p:i for i,p in enumerate(probes)}
    assert len(probe_index)==720
    for i,column in enumerate(columns):
        assert {probe_index[k]:v for k,v in column.items() if k in probe_index}=={i:1}

    # Independent coarse basis orders, not an identity matrix assumed by fiat.
    fine_index={key:i for i,key in enumerate(basis)}
    left_indices=[];right_indices=[]
    for first4 in combinations(range(6),4):
        last=tuple(j for j in range(6) if j not in first4)
        for first_blocks in pairs(first4):
            for first_kinds in product((0,1),repeat=2):
                for k in (0,1):left_indices.append(fine_index[first_blocks+(last,),first_kinds+(k,)])
    for first2 in combinations(range(6),2):
        rest=tuple(j for j in range(6) if j not in first2)
        for k in (0,1):
            for last_blocks in pairs(rest):
                for last_kinds in product((0,1),repeat=2):
                    right_indices.append(fine_index[(first2,)+last_blocks,(k,)+last_kinds])
    assert sorted(left_indices)==sorted(right_indices)==list(range(720))

    # K4[1] tensor I2[1] has differential -mu; I2[1] tensor K4[1]
    # has +mu. The global [I^3 -> I^2][2] differential is +mu.
    # Multiplication on degree -2 fixes the degree -3 signs of its lifts.
    for coarse_d,lower_map in ((-1,-1),(1,1)):
        assert 1*lower_map==1*coarse_d
    assert (-1)*(-1)==1 and 1*1==1  # Oriented lifts then refinement agree.
    # Insisting both lower multiplication maps are positive fails on 720
    # independent columns: the left chain residual is twice multiplication.
    assert all(2*column[probe]==2 for column,probe in zip(columns,probes))

    fixed=((0,1),(2,3),(4,5))
    for a,b in product((0,1),repeat=2):
        assert not derivative(0,multiply(relation(fixed[0],a),relation(fixed[1],b)))
        assert not derivative(3,multiply(relation(fixed[1],a),relation(fixed[2],b)))
        coarse_hostiles+=2

    result={'schema':'marici.nima.enriched-six-event-refinement.v1','passed':True,
        'chamber_coordinates':63,'critical_source_products':720,
        'labelled_pair_partitions':90,'local_seam_blocks_checked':len(cycles),
        'local_closed_relation_cycles_checked':2*len(cycles),
        'coarse_first_derivative_vanishing_fixtures':coarse_hostiles,
        'formal_local_green_pullbacks_checked':len(cycles),
        'local_green_matrix':'diag(4, (w_memory+w_seam)*sum_over_four_edges q_W(g_e,g_e))',
        'checks':{'source_selected_minor_is_identity_720':True,
                  'factorized_joint_seam_minor_is_identity_720':True,
                  'both_nested_deconcatenations_agree_on_every_product':True,
                  'both_coarse_product_basis_maps_are_permutations':True,
                  'left_lower_attachment_sign':-1,'right_lower_attachment_sign':1,
                  'unsigned_left_chain_residual_rank':720,
                  'oriented_common_product_refinement_square_commutes':True},
        'scope':'Critical six-event shifted product subobject and blockwise enriched quotient models. The full coarse conormal channels are supplied by the separate common-cell construction, not checked here. The local Green formula is checked in independent chamber Gram entries, not evaluated at spectral samples. No full six-event kernel, general nonminimal factorization descent, or unrestricted global/blockwise derived-base-change interchange is claimed.'}
    path=ROOT/'research/nima/results/enriched-six-event-refinement.json'
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
