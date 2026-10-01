"""Endpoint ledgers for the shared-seed pair, without conflating graph levels.

Enumerate (a) all retained geometric cell edges, (b) the actually specified seed
comparison operator, and (c) the same dense three-stage protocol used for 1836.
These are distinct endpoint types. Their counts are not silently identified or
promoted into a full seed-construction cost.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
from check_twenty_four_triangle_shared_seed import (
    A,B,SWAP,closure,proper,cell_boundary,surface_check,laplacian,
)
from check_twelve_triangle_positive_geometry import (
    POINTS,ONE,ZERO,OMEGA,I,mean,transpose,mm,mv,det,sub,
    zmv,zmul,zconj,zscale,zmm,zreal,projector,znorm,
)


def main():
    group=closure((A,B,SWAP));even=set(closure((A,B)))
    assert len(group)==24 and len(even)==12
    half=[int(p not in even) for p in group]
    rotations=[proper(p) for p in group]
    X0=transpose((mean([POINTS[k] for k in 'ABC']),POINTS['A'],POINTS['B']))
    v0=zmv(X0,(ONE,OMEGA,zmul(OMEGA,OMEGA)))
    vs=[zmv(R,v0) for R in rotations];Ps=[projector(v) for v in vs]
    u=tuple(z for v in vs for z in v)
    assert sum(znorm(z) for z in u)==160 and all(z!=ZERO for z in u)
    # Dense protocol: exactly the same local, transport, feedback conventions
    # as the earlier 1836-arrow graph, now on the actual 24 triangle positions.
    local=tuple(tuple(Ps[i//3][i%3][j%3] if i//3==j//3 else ZERO for j in range(72)) for i in range(72))
    blocks=[[mm(R,transpose(S)) for S in rotations] for R in rotations]
    symmetry=tuple(tuple(blocks[i//3][j//3][i%3][j%3]/24 for j in range(72)) for i in range(72))
    collective=projector(u)
    # Verify every 3x3 block of GL=LG=N; avoid a needless cubic 72x72 product.
    for g in range(24):
        for h in range(24):
            T=zreal(tuple(tuple(x/24 for x in row) for row in blocks[g][h]))
            Nblock=tuple(tuple(collective[3*g+i][3*h+j] for j in range(3)) for i in range(3))
            assert zmm(T,Ps[h])==Nblock and zmm(Ps[g],T)==Nblock
    matrices=(local,zreal(symmetry),collective)
    arrows=[]
    for stage,M in enumerate(matrices):
        arrows.append({((stage,i),((stage+1)%3,j)):M[j][i]
                       for i in range(72) for j in range(72) if M[j][i]!=ZERO})
    counts=list(map(len,arrows));assert counts==[216,1728,5184]
    all_edges=set().union(*(set(a) for a in arrows));assert len(all_edges)==7128
    partitions={'body_A':set(),'body_B':set(),'between_bodies':set()}
    for e in all_edges:
        i,j=e[0][1],e[1][1]
        key=('body_A' if half[i//3]==0 else 'body_B') if half[i//3]==half[j//3] else 'between_bodies'
        partitions[key].add(e)
    assert {k:len(v) for k,v in partitions.items()}=={'body_A':1836,'body_B':1836,'between_bodies':3456}
    assert set().union(*partitions.values())==all_edges
    assert sum(map(len,partitions.values()))==len(all_edges)
    # Literal closed-traversal union: every dense feedback edge has a unique
    # local->transport return path. Every cycle weight is positive.
    used=set();weight_sum=ZERO;cycles=0
    for closing,z in arrows[2].items():
        k=closing[0][1];i=closing[1][1]
        possible=[b for b in range(3*(i//3),3*(i//3)+3)
                  if ((0,i),(1,b)) in arrows[0] and ((1,b),(2,k)) in arrows[1]]
        assert len(possible)==1
        b=possible[0];e0=((0,i),(1,b));e1=((1,b),(2,k))
        w=zmul(zmul(arrows[0][e0],arrows[1][e1]),z)
        assert w[1]==0 and w[0]>0
        weight_sum=(weight_sum[0]+w[0],weight_sum[1]+w[1])
        used.update((e0,e1,closing));cycles+=1
    assert used==all_edges and cycles==5184 and weight_sum==ONE
    # Existing sparse pair comparison, kept separate from the dense extension.
    L,undirected=laplacian(group,(A,B,SWAP))
    comparison={}
    for i in range(24):
        for j in range(24):
            w=F(i==j)-L[j][i]/6
            if w: comparison[(i,j)]=w
    nonself={e for e in comparison if e[0]!=e[1]}
    cross={e for e in comparison if half[e[0]]!=half[e[1]]}
    assert len(undirected)==60 and len(nonself)==120
    assert len(comparison)==144 and len(cross)==24
    assert all((b,a) in nonself for a,b in nonself)
    quotient_cross={(half[i],half[j]) for i,j in cross}
    assert quotient_cross=={(0,1),(1,0)}
    # One coarse undirected link stands for twelve physical endpoint pairs.
    # It is not a one-arrow primitive extension of the first body.
    # Positive geometric cell ledger: retained internal edges stay in the union
    # even after their faces cancel from the external boundary.
    cp={'O':(F(0),)*3}
    def ax(i,s): return ('+' if s>0 else '-')+'xyz'[i]
    def ap(s): return 'V'+''.join('+' if x>0 else '-' for x in s)
    gray=((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,-1,1),(-1,-1,-1),(-1,1,-1),(-1,1,1))
    for i in range(3):
        for s in (-1,1): cp[ax(i,s)]=tuple(F(s if i==j else 0) for j in range(3))
    for s in gray: cp[ap(s)]=tuple(map(F,s))
    def orient(t):
        p,q,r,s=[cp[k] for k in t]
        volume=det(transpose((sub(q,p),sub(r,p),sub(s,p))))/6
        if volume<0: t=(t[0],t[1],t[3],t[2]);volume=-volume
        assert volume>0
        return t,volume
    core=[];tips={1:[],-1:[]}
    for s in gray:
        base=tuple(ax(i,s[i]) for i in range(3))
        core.append(orient(('O',)+base))
        tips[s[0]*s[1]*s[2]].append(orient((ap(s),)+base))
    def geometric_edges(cells):
        return {(a,b) for t,v in cells for a in t for b in t if a!=b}
    common=geometric_edges(core)
    body_a=geometric_edges(core+tips[1]);body_b=geometric_edges(core+tips[-1])
    assert len(common)==36 and len(body_a)==len(body_b)==60
    assert body_a&body_b==common
    geometry=body_a|body_b;assert len(geometry)==84
    assert len(body_b-body_a)==24
    chain=Counter();retained=set();stages=[];volume=F(0)
    for k,(t,v) in enumerate(core+tips[1]+tips[-1]):
        new=geometric_edges([(t,v)])
        addition=new-retained;retained.update(new)
        for f,n in cell_boundary(t).items(): chain[f]+=n
        boundary=surface_check(chain);volume+=v
        stages.append({'stage':k+1,'new_directed_geometric_arrows':len(addition),
                       'retained_unique_arrows':len(retained),'positive_volume':str(volume)})
        assert all((b,a) in retained for a,b in retained)
    assert retained==geometry and volume==4
    # Each geometric arrow is in a triangle loop of an actual retained cell.
    witnesses={}
    for t,v in core+tips[1]+tips[-1]:
        for face,n in cell_boundary(t).items():
            a,b,c=face if n==1 else (face[0],face[2],face[1])
            route=((a,b),(b,c),(c,a))
            assert set(route)<=geometry
            for edge in route: witnesses.setdefault(edge,route)
    assert set(witnesses)==geometry
    # Four new apices each have three distinct midpoint neighbors. Both
    # orientations occur in the closed face assembly: 4*3*2 new arrows.
    extra_apices={t[0] for t,v in tips[-1]}
    assert len(extra_apices)==4
    for vertex in extra_apices:
        outgoing={b for a,b in body_b-body_a if a==vertex}
        incoming={a for a,b in body_b-body_a if b==vertex}
        assert outgoing==incoming and len(outgoing)==3
    report={'audit_assertions_passed':True,
            'dense_1836_convention':{'stage_counts':counts,'unique_arrows':len(all_edges),
                                     'partition':{k:len(v) for k,v in partitions.items()},
                                     'increment_over_one_body':len(all_edges)-len(partitions['body_A']),
                                     'closed_three_step_cycles':cycles,'closed_walk_union_complete':True,
                                     'positive_cycle_weight_sum':'1',
                                     'interpretation':'Explicit dense protocol extension; the existing sparse consensus operator is a different graph.'},
            'existing_sparse_comparison':{'directed_nonself':120,'self_loops':24,'total':144,
                                          'body_A_internal_including_loops':60,'body_B_internal_including_loops':60,
                                          'directed_cross_arrows':24,'undirected_cross_pairs':12,
                                          'coarse_body_quotient_directed_cross_arrows':len(quotient_cross)},
            'retained_geometric_cell_ledger':{'body_A':60,'body_B':60,'shared_core':36,'union':84,
                                             'companion_increment':24,'all_edges_in_closed_cell_walks':True,
                                             'assembly_stages':stages},
            'endpoint_conventions':{'geometry':'ordered pairs of actual geometric cell vertex labels; shared labels counted once',
                                    'comparison':'ordered pairs of generated triangle positions; self-loops separately identified',
                                    'dense':'ordered pairs of (stage, triangle position, coordinate) ports, as in the original 1836 graph'},
            'target_1836_plus_1_obtained':False,
            'full_seed_compilation_cost':'Not identified with any of these ledgers: constructing coordinate records and operator coefficients still needs its own explicit primitive execution trace. Counts at different endpoint types are not silently added.',
            'conclusion':'The current pair does not give one extra primitive arrow. Its geometric second branch adds 24 directed edges; its seed comparison has 24 directed cross-arrows; the original dense 1836 convention gives 7128 arrows for the pair.'}
    dest=Path(__file__).resolve().parents[1]/'results'
    (dest/'pair-arrow-ledger.json').write_text(json.dumps(report,indent=2)+'\n')
    def port(v):
        stage,i=v;g=i//3
        return (('raw','local','aligned')[stage],''.join('ABCD'[j] for j in group[g]),'xyz'[i%3])
    records=[]
    for stage,amap in enumerate(arrows):
        for (src,dst),w in sorted(amap.items()):
            records.append({'source':port(src),'target':port(dst),'real':str(w[0]),'imag_sqrt3':str(w[1])})
    (dest/'pair-dense-7128-arrows.json').write_text(json.dumps(records,indent=2)+'\n')
    records=[{'source':a,'target':b,'shared_core':(a,b) in common,
              'closed_walk':witnesses[a,b]} for a,b in sorted(geometry)]
    (dest/'pair-geometric-arrows.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PASS ledger: geometry 60+60-36=84 (companion +24); directed cross-comparisons 24; dense protocol 1836+1836+3456=7128. Target 1837 is not obtained; complete seed-compilation cost is not conflated with these ledgers.')

if __name__=='__main__': main()
