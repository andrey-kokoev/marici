"""Explicit candidate net: twelve sites, twelve relation ports and three state ports.

These site/sector sizes and Fourier transport are declared construction choices.
Arrows are unique endpoint pairs, not history-tagged comparison occurrences.
Fourier orthogonality proves the twelve-step identity; numerics check every basis
vector independently. The two sectors are uncoupled in this minimal construction.
"""
import cmath
import math
import json
from pathlib import Path


def main():
    sites=12
    sectors=(('R',12),('H',3))
    nodes=[(c,s,i) for c in range(sites) for s,n in sectors for i in range(n)]
    index={v:i for i,v in enumerate(nodes)}
    arrows={}
    for c in range(sites):
        for s,n in sectors:
            for i in range(n):
                for j in range(n):
                    src=(c,s,i);dst=((c+1)%sites,s,j)
                    assert (src,dst) not in arrows and src!=dst
                    arrows[src,dst]=cmath.exp(2j*math.pi*i*j/n)/math.sqrt(n)
    assert len(nodes)==180 and len(arrows)==1836
    counts={s:sum(a[0][1]==s for a in arrows) for s,n in sectors}
    assert counts=={'R':1728,'H':108}
    sparse=[(index[src],index[dst],z) for (src,dst),z in arrows.items()]
    def step(x):
        y=[0j]*len(nodes)
        for src,dst,z in sparse:
            y[dst]+=z*x[src]
        return y
    worst=0.0;worst_norm=0.0
    for b in range(len(nodes)):
        x=[0j]*len(nodes);x[b]=1
        for k in range(1,13):
            x=step(x)
            worst_norm=max(worst_norm,abs(sum(abs(z)**2 for z in x)-1))
            if k<12:
                assert abs(x[b])<1e-12 # current site differs from initial site
        worst=max(worst,max(abs(z-(i==b)) for i,z in enumerate(x)))
    assert worst<1e-11 and worst_norm<1e-11
    # Every structural arrow belongs to an explicit length-12 closed walk.
    union=set()
    for src,dst in arrows:
        c,s,i=src;_,_,j=dst
        route=[src,dst]
        for k in range(2,12): route.append(((c+k)%sites,s,j))
        route.append(src)
        edges=list(zip(route,route[1:]))
        assert len(edges)==12 and route[0]==route[-1]
        assert all(e in arrows for e in edges)
        union.update(edges)
    assert union==set(arrows)
    # Diagonal-within-sector site transport also closes, using only 180 arrows.
    # Hence closure alone does not establish minimality of the dense Fourier net.
    sparse_return={(v,((v[0]+1)%sites,v[1],v[2])) for v in nodes}
    assert len(sparse_return)==180 and sparse_return<=set(arrows)
    report={'status':'passed','sites':sites,'sector_sizes':dict(sectors),
            'port_nodes':len(nodes),'unique_directed_arrows':len(arrows),
            'sector_arrow_counts':counts,'unique_arrows_in_closed_walk_union':len(union),
            'transport':'U = cyclic_shift_12 tensor (F_12 direct_sum F_3)',
            'exact_identity_argument':'F_n^2 reverses port indices, so F_n^4=I; U^12=I. Site shift prevents any earlier positive operator identity.',
            'numerical_basis_vectors_checked':len(nodes),'max_return_error':worst,
            'max_norm_error':worst_norm,'connected_components':2,
            'smaller_identity_return_control':len(sparse_return),
            'scope':'Constructed 1836-arrow phased net. Twelve sites, sector split and dense Fourier transport are explicit assumptions, not consequences of the earlier line-graph tower.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'1836-phase-interaction-net.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print(f'PASS: {len(arrows)} unique arrows, {len(nodes)} ports, full closed-walk union, U^12=I; max numerical error {worst:.3g}.')

if __name__=='__main__': main()
