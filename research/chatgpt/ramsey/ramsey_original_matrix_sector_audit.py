#!/usr/bin/env python3
"""Matrix/row tests for the initial Ramsey R/G/0 construction.

This explicitly tests a proposed embedding, not an interpretation silently
assumed by the original colored-row experiment:
  - one colored position is marked as the diagonal/root;
  - every other R or G entry is a specified edge color;
  - 0 means unassigned, filled by R or G;
  - all other rows are cyclic shifts (a circulant graph).
The script tests BOTH assignments of graph red to R versus G; these are not
interchangeable for R(3,k) when k>3, so both results are reported.

Separate tests concern the point-reflection matrix J_p and real/complex
quarter-turns with Q^2=J_p. No Ramsey values are used as input.
"""
from itertools import combinations, product
from math import pi, sqrt
import cmath


def seed(k):
    return ''.join(('R' if j%2==0 else 'G') for j in range(k-2))+'00'


def reflect_about(row, pivot):
    n=len(row)
    return ''.join(row[(2*pivot-j)%n] for j in range(n))


def root_options(row, pivot):
    n=len(row)
    if row[pivot]=='0': return None
    forced={};free=[]
    for d in range(1,n//2+1):
        colors={row[(pivot+d)%n],row[(pivot-d)%n]}-{'0'}
        if len(colors)>1:return None
        if colors:forced[d]=next(iter(colors))
        else:free.append(d)
    return forced,free


def circulant_graph(n,dist_colors,red):
    adj=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            d=min((j-i)%n,(i-j)%n)
            if dist_colors[d]==red:
                adj[i]|=1<<j
                adj[j]|=1<<i
    return adj


def triangle_free(adj):
    return all(not(adj[i]&adj[j]) for i in range(len(adj))
               for j in range(i+1,len(adj)) if (adj[i]>>j)&1)


def alpha(adj):
    """Exact maximum independent-set size for small graphs."""
    n=len(adj);best=0
    for mask in range(1<<n):
        if mask.bit_count()<=best:continue
        rem=mask;ok=True
        while rem:
            bit=rem & -rem
            i=bit.bit_length()-1
            rem^=bit
            if adj[i]&rem:
                ok=False;break
        if ok:best=mask.bit_count()
    return best


def root_scan(k):
    row=seed(k)
    out=[]
    for pivot in range(k-2):
        opts=root_options(row,pivot)
        if opts is None:continue
        forced,free=opts
        valid={'R':[], 'G':[]}
        for values in product('RG',repeat=len(free)):
            dist_colors=dict(forced)
            dist_colors.update(zip(free,values))
            for red in 'RG':
                A=circulant_graph(k,dist_colors,red)
                if triangle_free(A) and alpha(A)<k:
                    valid[red].append((tuple(d for d in sorted(dist_colors) if dist_colors[d]==red),alpha(A)))
        out.append((pivot,valid))
    return out


def permutation_reflection_root(n):
    swaps=[(i,n-i) for i in range(1,n) if i<n-i]
    if len(swaps)%2:return None
    p=list(range(n))
    for (a,b),(c,d) in zip(swaps[::2],swaps[1::2]):
        p[a],p[c],p[b],p[d]=c,b,d,a
    assert all(p[p[j]]==(-j)%n for j in range(n))
    return p


def natural_reflection_root(n):
    """Square root of the reflection through the two empty cells, if possible."""
    involution=lambda j:(n-3-j)%n
    swaps=[];fixed=[];seen=set()
    for j in range(n):
        if j in seen:continue
        h=involution(j)
        seen.update((j,h))
        if j==h:fixed.append(j)
        else:swaps.append((j,h))
    if len(swaps)%2:return None,swaps,fixed
    p=list(range(n))
    for (a,b),(c,d) in zip(swaps[::2],swaps[1::2]):
        p[a],p[c],p[b],p[d]=c,b,d,a
    assert all(p[p[j]]==involution(j) for j in range(n))
    return p,swaps,fixed


def natural_phase_rows(row, permutation):
    if permutation is None:return None
    n=len(row)
    current=row
    out=[current]
    for _ in range(4):
        nxt=['']*n
        for j in range(n):nxt[permutation[j]]=current[j]
        current=''.join(nxt)
        out.append(current)
    assert out[-1]==out[0]
    return out


def fourier_errors(n):
    F=[[cmath.exp(2j*pi*j*h/n)/sqrt(n) for h in range(n)] for j in range(n)]
    F2=[[sum(F[i][h]*F[h][j] for h in range(n)) for j in range(n)] for i in range(n)]
    F4=[[sum(F2[i][h]*F2[h][j] for h in range(n)) for j in range(n)] for i in range(n)]
    e2=max(abs(F2[i][j]-(1 if j==(-i)%n else 0)) for i in range(n) for j in range(n))
    e4=max(abs(F4[i][j]-(1 if i==j else 0)) for i in range(n) for j in range(n))
    return e2,e4


def restricted_phase_validation(n):
    """A source-generated real phase carrier satisfying P^2=H on that carrier.

    For even n: E=span(x, a) where x=R/G contrast and a=empty-pair contrast.
    For odd n>=5: E=span(x, a, b) where b=colored-block endpoint contrast.
    The quarter-turn acts on a 2-plane and fixes the common line for odd n.
    Does not assert P^2=H on the whole ambient R^n.
    """
    assert n>=4
    x=[(1 if j%2==0 else -1) if j<n-2 else 0 for j in range(n)]
    a=[int(j==n-2)-int(j==n-1) for j in range(n)]
    b=[int(j==0)-int(j==n-3) for j in range(n)]
    H=lambda z:[z[(n-3-j)%n] for j in range(n)]
    if n%2==0:
        u=[v/sqrt(n-2) for v in x]
        v=[w/sqrt(2) for w in a]
        z0=x
        dimension=2
    else:
        u=[w/sqrt(2) for w in a]
        v=[w/sqrt(2) for w in b]
        z0=[x[j]+a[j] for j in range(n)]
        dimension=3
    dot=lambda z,w:sum(z[j]*w[j] for j in range(n))
    assert abs(dot(u,u)-1)<1e-12 and abs(dot(v,v)-1)<1e-12 and abs(dot(u,v))<1e-12
    def P(z):
        cu,cv=dot(z,u),dot(z,v)
        return [z[j]+(-cu-cv)*u[j]+(cu-cv)*v[j] for j in range(n)]
    orbit=[list(map(float,z0))]
    for _ in range(4):orbit.append(P(orbit[-1]))
    err=lambda y,z:max(abs(a-b) for a,b in zip(y,z))
    assert err(orbit[4],orbit[0])<1e-11
    assert all(err(orbit[t+2],H(orbit[t]))<1e-11 for t in range(3))
    assert all(err(orbit[t],orbit[s])>1e-5 for t in range(4) for s in range(t+1,4))
    return dimension, orbit[:4]


def quarter_turn_orbit_validation():
    """Recheck actual 13->17 block-matrix orbit construction, standalone."""
    n=13
    G13=[0]*n
    for u in range(n):
        for d in (1,5,8,12):
            v=(u+d)%n
            G13[u]|=1<<v
    assert triangle_free(G13) and alpha(G13)==4
    sigma=lambda x:(5*x)%13
    assert all(sum(1<<sigma(v) for v in range(n) if (G13[u]>>v)&1)==G13[sigma(u)]
               for u in range(n))
    S0={1,7,11}
    stages=[{(x*pow(5,t,13))%13 for x in S0} for t in range(4)]
    assert all(all(not ((G13[a]>>b)&1) for a,b in combinations(S,2)) for S in stages)
    assert all(not (a&b) for a,b in combinations(stages,2))
    G17=G13+[0]*4
    for t,S in enumerate(stages):
        for u in S:
            v=13+t
            G17[u]|=1<<v
            G17[v]|=1<<u
        u,v=13+t,13+(t+1)%4
        G17[u]|=1<<v
        G17[v]|=1<<u
    assert triangle_free(G17) and alpha(G17)==5
    assert sum(x.bit_count() for x in G17)//2==42
    return ('G13: 13 vertices, alpha 4; orbit supports = '+str([tuple(sorted(s)) for s in stages])+
            '; G17: 17 vertices, 42 red edges, alpha 5, triangle-free.')


def main():
    print('ORIGINAL SYMBOLIC ROWS: arbitrary root/pivot, exact cyclic completion test')
    print('k  row           reflection roots  valid roots if R=red  valid roots if G=red')
    for k in range(3,11):
        results=root_scan(k)
        piv=[p for p,_ in results]
        redp=[p for p,valid in results if valid['R']]
        greenp=[p for p,valid in results if valid['G']]
        print(f'{k:2} {seed(k):<13} {str(piv):<18} {str(redp):<21} {greenp}')
        assert ((k%2==0 and piv==list(range(k-2))) or
                (k==3 and piv==[0]) or
                (k%2==1 and piv==list(range((k-5)//2,(k-5)//2+3))))
    for k in range(3,35):
        piv=[p for p,_ in root_scan(k)] if k<=10 else [p for p in range(k-2) if root_options(seed(k),p) is not None]
        assert (piv==list(range(k-2)) if k%2==0 else
                piv==([0] if k==3 else list(range((k-5)//2,(k-5)//2+3))))
    print('Verified reflection-root position theorem at lengths 3..34')
    print('\nQUARTER-TURN LIFT OF CYCLIC POINT REFLECTION')
    print('k  negative_eigenspace_dim  det(J)  real_root_P  extra_real_dim  Fourier_F2=J,F4=I')
    for k in range(3,11):
        swaps=(k-1)//2 if k%2 else (k-2)//2
        real=permutation_reflection_root(k)
        f2,f4=fourier_errors(k)
        assert (real is not None)==(swaps%2==0)
        assert f2<1e-11 and f4<1e-11
        print(f'{k:2} {swaps:^24} {(-1)**swaps:^7} {str(real is not None):^11} {swaps%2:^15} yes')
    print('\nINTRINSIC REFLECTION THROUGH THE TWO TERMINAL EMPTY CELLS')
    print('k  color_reflection  real_P^2=H  orbit_length  phase_rows')
    for k in range(3,11):
        x=seed(k)
        H=''.join(x[(k-3-j)%k] for j in range(k))
        dual=x.translate(str.maketrans('RG','GR'))
        assert H==(x if k%2 else dual)
        p,swaps,fixed=natural_reflection_root(k)
        assert len(swaps)==k//2
        assert (p is not None)==(k%4 in (0,1))
        phases=natural_phase_rows(x,p)
        nph='N/A' if phases is None else len(set(phases[:4]))
        if phases is not None:
            assert nph==(4 if k%2==0 else 2)
        print(f'{k:2} {"preserves" if k%2 else "swaps R/G":<17} {str(p is not None):<11} {str(nph):<13} {phases[:4] if phases else "—"}')
    print('\nRESTRICTED REAL PHASE CARRIER (NOT A FULL-SPACE MATRIX ROOT)')
    print('k  carrier_dim  four_distinct_phases  squared_phase=natural_reflection')
    for k in range(4,11):
        dim,phases=restricted_phase_validation(k)
        print(f'{k:2} {dim:^12} yes                   yes')
    print('k=3: colored endpoint contrast vanishes; this particular source carrier is degenerate.')
    print('\nACTUAL RAMSEY BLOCK CONSTRUCTION')
    print(quarter_turn_orbit_validation())
    print('\nScope: root scan is a proposed circulant embedding; the 13->17 orbit is an actual Ramsey witness.')

if __name__=='__main__':main()
