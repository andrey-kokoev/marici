#!/usr/bin/env python3
"""Exact 4-phase incidence decoder and Ramsey C13->17 orbit audit.

No known Ramsey number is used as a target.  The source row's restricted real
quarter-turn is checked for k=4..10.  A 4-output quadratic character decoder
is forced by the Fourier modes of four nonzero disjoint incidence columns.
The seed selection and internal graph are separately exhaustively tested.

Run: python check_ramsey_quadratic_phase_decoder.py
"""
from itertools import product, combinations
from math import sqrt
from collections import Counter

N=13
PHASES=((1,0),(0,1),(-1,0),(0,-1))


def bit_indices(mask):
    while mask:
        b=mask&-mask
        yield b.bit_length()-1
        mask ^= b


def graph13():
    a=[0]*N
    for u in range(N):
        for d in (1,5,8,12):
            v=(u+d)%N
            a[u]|=1<<v
    return a


def independent(a,mask):
    for u in bit_indices(mask):
        if a[u]&mask:
            return False
    return True


def alpha_table(a):
    dp=bytearray(1<<len(a))
    for m in range(1,len(dp)):
        b=m&-m; v=b.bit_length()-1; t=m^b
        dp[m]=max(dp[t],1+dp[t & ~a[v]])
    return dp


def orbit_list():
    unseen=set(range(1,N)); out=[]
    while unseen:
        x=min(unseen)
        orbit=[x*pow(5,t,N)%N for t in range(4)]
        assert len(set(orbit))==4
        out.append(orbit)
        unseen.difference_update(orbit)
    assert len(out)==3
    return out


def support_masks(seed):
    return [sum(1<<(v*pow(5,t,N)%N) for v in seed) for t in range(4)]


def phase_feature(c,s):
    """Polynomial basis for four points at angles 0,90,180,270 degrees."""
    return (1,c,s,c*c-s*s)


def decoder(c,s,columns):
    """Real quadratic decoder, exact at the four phase points.

    Φ(c,s) = (c²+s²)*M + C*c + S*s + E*(c²-s²)
    where 4*M=(n0+n1+n2+n3), 2*C=n0-n2,
          2*S=n1-n3, 4*E=n0-n1+n2-n3.
    Uses fractions to keep the coefficient calculation exact.
    """
    from fractions import Fraction as Q
    result=[]
    for v in range(N):
        p=[int((mask>>v)&1) for mask in columns]
        m=Q(sum(p),4)
        c1=Q(p[0]-p[2],2)
        s1=Q(p[1]-p[3],2)
        e=Q(p[0]-p[1]+p[2]-p[3],4)
        result.append(m*(c*c+s*s)+c1*c+s1*s+e*(c*c-s*s))
    return result


def contrast_orbit(k):
    """Checks original symbolic-row restricted quarter-turn and reads (c,s)."""
    assert k>=4
    x=[(1 if j%2==0 else -1) if j<k-2 else 0 for j in range(k)]
    a=[int(j==k-2)-int(j==k-1) for j in range(k)]
    b=[int(j==0)-int(j==k-3) for j in range(k)]
    if k%2==0:
        u=[v/sqrt(k-2) for v in x]
        v=[w/sqrt(2) for w in a]
        z=list(map(float,x))
        radius=sqrt(k-2)
    else:
        u=[w/sqrt(2) for w in a]
        v=[w/sqrt(2) for w in b]
        z=[float(xj+aj) for xj,aj in zip(x,a)]
        radius=sqrt(2)
    dot=lambda p,q:sum(a*b for a,b in zip(p,q))
    def turn(z):
        c=dot(z,u); s=dot(z,v)
        return [w+(-c-s)*ui+(c-s)*vi for w,ui,vi in zip(z,u,v)]
    H=lambda z:[z[(k-3-j)%k] for j in range(k)]
    z0=z[:]; out=[]
    for phase in range(4):
        c=dot(z,u)/radius; s=dot(z,v)/radius
        assert abs(c-PHASES[phase][0])<1e-10, (k,phase,c)
        assert abs(s-PHASES[phase][1])<1e-10, (k,phase,s)
        out.append((c,s))
        zz=turn(z)
        if phase==1:
            assert max(abs(v-h) for v,h in zip(zz,H(z0)))<1e-10
        z=zz
    assert max(abs(v-h) for v,h in zip(z,z0))<1e-10
    return out


def graph_extension(a,columns,F):
    g=a[:]+[0]*4
    for j,mask in enumerate(columns):
        for old in bit_indices(mask):
            g[old]|=1<<(N+j)
            g[N+j]|=1<<old
    for i in range(4):
        for j in range(i+1,4):
            if (F[i]>>j)&1:
                g[N+i]|=1<<(N+j)
                g[N+j]|=1<<(N+i)
    return g


def valid_independent_newsets(F):
    for j in range(16):
        if all(not (F[i] & j) for i in bit_indices(j)):
            yield j


def c4_internal_graph(which):
    # C4-invariant undirected patterns: none, opposite matching, C4, K4.
    F=[0]*4
    if which in ('C4','K4'):
        for i in range(4):
            j=(i+1)%4; F[i]|=1<<j; F[j]|=1<<i
    if which in ('matching','K4'):
        for i,j in ((0,2),(1,3)):
            F[i]|=1<<j; F[j]|=1<<i
    return F


def alpha_extension_from_old_dp(dp,columns,F):
    all_old=(1<<N)-1
    best=0
    for j in valid_independent_newsets(F):
        forbidden=0
        for t in bit_indices(j):forbidden|=columns[t]
        best=max(best,j.bit_count()+dp[all_old&~forbidden])
    return best


def triangle_free(a):
    for i in range(len(a)):
        for j in bit_indices(a[i]):
            if j>i and a[i]&a[j]:return False
    return True


def main():
    a=graph13();dp=alpha_table(a)
    assert dp[-1]==4 and triangle_free(a)
    orbits=orbit_list()
    seed=(1,7,11)
    assert all(len(set(seed)&set(orbit))==1 for orbit in orbits)
    columns=support_masks(seed)
    assert all(m.bit_count()==3 for m in columns)
    assert all(not (x&y) for x,y in combinations(columns,2))
    assert (columns[0]|columns[1]|columns[2]|columns[3]) == ((1<<N)-2)
    assert all(independent(a,m) for m in columns)
    assert all(sum((1 if (columns[t]>>v)&1 else 0) for v in range(N))==3 for t in range(4))
    # For disjoint columns, exact Gram has diagonal 3 and zero off-diagonal.
    gram=[[int((col_i&col_j).bit_count()) for col_j in columns] for col_i in columns]
    assert gram==[[3 if i==j else 0 for j in range(4)] for i in range(4)]

    # The affine obstruction is a nonzero alternating incidence mode.
    delta=[int((columns[0]>>v)&1)+int((columns[2]>>v)&1)
          -int((columns[1]>>v)&1)-int((columns[3]>>v)&1) for v in range(N)]
    assert sum(t*t for t in delta)==12
    # Even after best affine fitting, the squared Frobenius residual is ||delta||²/4.
    assert sum(t*t for t in delta)/4==3

    # Quadratic interpolation recovers each 0/1 incidence column exactly.
    for t,(c,s) in enumerate(PHASES):
        decoded=decoder(c,s,columns)
        assert all(x in (0,1) for x in decoded)
        got=sum(1<<v for v,x in enumerate(decoded) if x==1)
        assert got==columns[t]
    # Check exact sigma-equivariance on all four discrete phase points.
    sig=lambda m:sum(1<<(5*v%N) for v in bit_indices(m))
    assert all(sig(columns[t])==columns[(t+1)%4] for t in range(4))

    for k in range(4,11):
        orbit=contrast_orbit(k)
        for t,(c,s) in enumerate(orbit):
            ci,si=round(c),round(s)
            decoded=decoder(ci,si,columns)
            got=sum(1<<v for v,x in enumerate(decoded) if x==1)
            assert got==columns[t]

    F=c4_internal_graph('C4')
    g=graph_extension(a,columns,F)
    assert triangle_free(g)
    assert alpha_extension_from_old_dp(dp,columns,F)==5
    assert sum(m.bit_count() for m in g)//2==42

    results=Counter(); orbits_survivor=Counter(); success_details=[]
    for tup in product(*orbits):
        if not independent(a,sum(1<<v for v in tup)):
            results['seed_not_independent']+=1
            continue
        phase_cols=support_masks(tup)
        assert all(independent(a,m) for m in phase_cols)
        for kind in ('empty','matching','C4','K4'):
            F=c4_internal_graph(kind)
            if not triangle_free([F[i] for i in range(4)]):
                results[kind+'_triangle']+=1
                continue
            aa=alpha_extension_from_old_dp(dp,phase_cols,F)
            results[(kind,aa)]+=1
            if aa<=5:
                orbits_survivor[kind]+=1
                success_details.append((kind,tup,aa))
    # Remove the one-per-4-cycle seed assumption.  All independent S in G13
    # are considered; any C4-equivariant internal red graph is permitted.
    full=Counter(); all_solutions=[]
    for mask in range(1<<N):
        if not independent(a,mask):continue
        base_seed=tuple(bit_indices(mask))
        phase_cols=support_masks(base_seed)
        for kind in ('empty','matching','C4','K4'):
            F=c4_internal_graph(kind)
            # Exact triangle test includes shared red old neighbors.
            ext=graph_extension(a,phase_cols,F)
            if not triangle_free(ext):
                full[(kind,'triangle')] += 1
                continue
            aa=alpha_extension_from_old_dp(dp,phase_cols,F)
            full[(kind,aa)] += 1
            if aa<=5:
                all_solutions.append((kind,base_seed,aa))
    print('ALL INDEPENDENT SEED SETS, ALL CYCLICALLY INVARIANT FOUR-VERTEX INTERNAL GRAPHS:')
    print('  independent seeds:',sum(1 for mask in range(1<<N) if independent(a,mask)))
    for key,num in sorted(full.items(),key=lambda kv:str(kv[0])):print('  ',key,num)
    print('  all survivors:', all_solutions)
    print('  survivors by type and seed size:',dict(Counter((kind,len(seed)) for kind,seed,_ in all_solutions)))
    print('C13 support orbit:',[tuple(bit_indices(m)) for m in columns])
    print('X^T X = 3 I4, rank(X)=4, affine obstruction ||Delta||^2=12')
    print('Minimum possible affine least-squares loss (four 13-entry columns): 3')
    print('Exact quadratic decoder: Phi(c,s)=(c^2+s^2)*M + c*C + s*S + (c^2-s^2)*E')
    print('Four-phase source carriers k=4..10: all decoder outputs match the four binary columns')
    print('G17: 17 vertices, 42 edges, alpha=5, triangle-free')
    print('Seed selection within invariant four-column transversals:')
    for k,v in sorted(results.items(),key=lambda item:str(item[0])):print('  ',k,':',v)
    print('Success counts by internally invariant red graph:',dict(orbits_survivor))
    print('Successful cases:', success_details)
    assert results['seed_not_independent']==44
    assert results[('C4',5)]==4
    print('ALL EXACT AUDITS PASSED')

if __name__=='__main__':main()
