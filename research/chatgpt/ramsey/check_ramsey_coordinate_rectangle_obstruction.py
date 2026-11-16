#!/usr/bin/env python3
"""Exact finite and analytic-size checks of projection obstructions.

The mathematical claim is proved in the accompanying note; this checker
verifies the finite values and the necessary double-rectangle criterion.
All large-scale calculations use source counts, NOT an n-vertex graph.
"""
from math import ceil, floor, isqrt, log, sqrt


def prime(q):
    if q<2: return False
    for d in range(2, isqrt(q)+1):
        if q%d==0: return False
    return True


def rotneg(t,q): return (t[1]%q, -t[0]%q)


def rotated_orbit(v,q):
    out=set();cur=v
    for _ in range(4):
        out.add(cur)
        cur=rotneg(cur,q)
    assert cur==v and len(out)==4
    return out


def settings(q):
    assert prime(q) and q%3==2
    r=floor(log(q)**2)
    assert 2*r<q
    s=4*r+1; m=q*q; n=m*s
    K=floor(10*sqrt(n*log(n)))
    theta=0.5-0.001
    t=ceil(theta*K)-1
    a=isqrt((K+s-1)//s)
    if a*a < (K+s-1)//s: a+=1
    assert a+2*r<q
    mean_numerator=s*t*t
    mean_denominator=m
    cross_upper=a*a+4*a*r
    return dict(q=q,r=r,s=s,m=m,n=n,K=K,t=t,a=a,
                average_rectangle_edge_count=mean_numerator/mean_denominator,
                average_impossibility=mean_numerator>=K*mean_denominator,
                cross_blue_projection_upper=cross_upper,
                cross_violates_projection=max(a*a,cross_upper)<=t)


def exact_finite_sumsets(q):
    cfg=settings(q); r=cfg['r']; s=cfg['s']; K=cfg['K'];a=cfg['a']
    h=(K+s-1)//s
    U=[(x,y) for x in range(a) for y in range(a)][:h]
    assert len(U)*s>=K
    assert len(U)==h
    cross={(0,0)}
    parab={(0,0)}
    for j in range(1,r+1):
        cross.update(rotated_orbit((0,j),q))
        parab.update(rotated_orbit((j,j*j%q),q))
    assert len(cross)==len(parab)==s
    def sumset(T):
        return len({((x+tx)%q,(y+ty)%q) for x,y in U for tx,ty in T})
    c=sumset(cross); p=sumset(parab)
    assert c<=cfg['cross_blue_projection_upper']
    assert max(h,c)<=cfg['t']
    assert max(h,p)<=cfg['t']
    return dict(cfg,chosen_red_projection=h,
                actual_cross_blue_projection=c,
                actual_interval_parabola_blue_projection=p)




def collinear_triplet_line_obstruction(cfg):
    """Three shifts on one affine line yield 3*q*floor(t/q) incidences."""
    q=cfg['q']; t=cfg['t']; K=cfg['K']
    cosets=t//q
    selected=cosets*q
    assert selected<=t<=q*q
    return dict(cosets=cosets,
                coordinates_per_projection=selected,
                guaranteed_incidences=3*selected,
                projection_lemma_violated=3*selected>=K)


def circle_carrier(q,r):
    """Select r quarter-turn orbits from the norm-one affine conic.

    q=1013 is a valid prime with q == 1 (mod 4).  The construction
    uses an element of multiplicative order q-1 (primitive root).
    """
    assert q%4==1 and r<(q-1)//4
    def factors(n):
        div=[];p=2
        while p*p<=n:
            if n%p==0:
                div.append(p)
                while n%p==0:n//=p
            p+=1
        if n>1:div.append(n)
        return div
    fac=factors(q-1)
    g=next(x for x in range(2,q) if all(pow(x,(q-1)//p,q)!=1 for p in fac))
    i=pow(g,(q-1)//4,q)
    assert i*i%q==q-1
    inv2=pow(2,-1,q)
    inv2i=pow(2*i%q,-1,q)
    conic=set()
    for j in range(r):
        z=pow(g,j,q);zin=pow(z,-1,q)
        x=(z+zin)*inv2%q
        y=(z-zin)*inv2i%q
        conic.update(rotated_orbit((x,y),q))
    assert len(conic)==4*r
    assert (0,0) not in conic
    assert all((x*x+y*y)%q==1 for x,y in conic)
    return conic


def circle_finite_test(q=1013):
    cfg=settings(q)
    T=circle_carrier(q,cfg['r'])
    s=len(T);n=q*q*s;K=floor(10*sqrt(n*log(n)))
    h=(K+s-1)//s
    U,a=([],isqrt(h))
    if a*a<h:a+=1
    U=[(x,y) for x in range(a) for y in range(a)][:h]
    assert len(U)==h
    sums=len({((x+tx)%q,(y+ty)%q) for x,y in U for tx,ty in T})
    t=ceil((0.5-0.001)*K)-1
    assert sums>t
    return dict(q=q,s=s,K=K,t=t,red_projection_upper=h,
                blue_projection_for_source_square=sums,
                this_one_square_not_obstructed=sums>t)

if __name__=='__main__':
    small=exact_finite_sumsets(1013)
    big=settings(1_000_037)
    assert small['average_impossibility']
    assert small['actual_cross_blue_projection']==13905
    assert small['actual_interval_parabola_blue_projection']==246516
    assert not big['average_impossibility']
    assert big['cross_violates_projection']
    assert big['m']>big['t']
    line_small=collinear_triplet_line_obstruction(small)
    line_big=collinear_triplet_line_obstruction(big)
    circle=circle_finite_test(1013)
    assert line_small['projection_lemma_violated']
    assert line_big['projection_lemma_violated']
    print('q=1013:',small)
    print('q=1,000,037:',big)
    print('collinear-shift fatal rectangles:',line_small,line_big)
    print('quarter-turn conic example:',circle)
    print('PASS: rectangle obstruction, asymptotic-axis failure, collinear-triplet failure, conic construction')
