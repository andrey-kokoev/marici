"""Exact ordinary-blowup audit for the four D1-D2/D3 Gysin crossings."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
from sympy.polys.domains import GF

P=2305843009213693951
K=GF(P).frac_field('t'); t=K.gens[0]; Z=K.zero; O=K.one

def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]: a.pop()
    return a or [Z]
def add(a,b):
    o=[Z]*max(len(a),len(b))
    for i in range(len(o)): o[i]=(a[i] if i<len(a) else Z)+(b[i] if i<len(b) else Z)
    return trim(o)
def neg(a): return trim([-x for x in a])
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    o=[Z]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): o[i+j]+=x*y
    return trim(o)
def scale(a,c): return trim([c*x for x in a])
def order(a): return next((i for i,x in enumerate(a) if x),10**9)

class ER:
    def __init__(self,n,d=None): self.n,self.d=trim(n),trim(d or [O])
    def __add__(self,x): return ER(add(mul(self.n,x.d),mul(x.n,self.d)),mul(self.d,x.d))
    def __neg__(self): return ER(neg(self.n),self.d)
    def __sub__(self,x): return self+(-x)
    def __mul__(self,x): return ER(mul(self.n,x.n),mul(self.d,x.d))
    def sc(self,c): return ER(scale(self.n,c),self.d)
    def shift(self,k): return ER(([Z]*k+self.n) if k>=0 else self.n, self.d if k>=0 else ([Z]*(-k)+self.d))
    def valuation(self): return order(self.n)-order(self.d)
    def leading(self):
        on=order(self.n)
        if on==10**9: return 10**9,Z
        od=order(self.d); return on-od,self.n[on]/self.d[od]

def epow_shift(c,s,n):
    out=[Z]
    for k in range(n+1):
        while len(out)<=k: out.append(Z)
        out[k]+=K.convert(math.comb(n,k))*K.convert(c)**(n-k)*s**k
    return trim(out)

def substitute_fit(fit,u0,v0,su,sv):
    def conv(terms):
        out=[Z]
        for i,j,c in terms:
            out=add(out,scale(mul(epow_shift(u0,su,i),epow_shift(v0,sv,j)),K.convert(c)))
        return out
    return ER(conv(fit['numerator']),conv(fit['denominator']))

def rank(a):
    a=[row[:] for row in a]; r=0
    for c in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]; z=1/a[r][c]; a[r]=[z*x for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                z=a[i][c]; a[i]=[a[i][j]-z*a[r][j] for j in range(len(a[0]))]
        r+=1
    return r

def nullspace(a):
    a=[row[:] for row in a]; rows=len(a); cols=len(a[0]); piv=[]; r=0
    for c in range(cols):
        p=next((i for i in range(r,rows) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]; z=1/a[r][c];a[r]=[z*x for x in a[r]]
        for i in range(rows):
            if i!=r and a[i][c]:
                z=a[i][c];a[i]=[a[i][j]-z*a[r][j] for j in range(cols)]
        piv.append(c);r+=1
    out=[]
    for f in [c for c in range(cols) if c not in piv]:
        x=[Z]*cols;x[f]=O
        for i,p in enumerate(piv):x[p]=-a[i][f]
        out.append(x)
    return out

def const_int(x):
    if not x:return 0
    if x.denom.degree() or x.numer.degree():raise ValueError(f'nonconstant {x}')
    return int(x.numer)/int(x.denom)

def const_mod(x):
    if not x:return 0
    if x.denom.degree() or x.numer.degree():raise ValueError(f'nonconstant {x}')
    n=int(x.numer.to_dict()[(0,)]);d=int(x.denom.to_dict()[(0,)])
    return (n*pow(d,P-2,P))%P

def mod_matrix(a):return [[const_mod(x) for x in row] for row in a]

def indicial(r,m=1):
    a=[[Z]*4 for _ in range(4)]
    for q in range(2):
      for k in range(2):
       col=2*q+k
       for i in range(2):
        for j in range(2):
         row=2*i+j; z=Z
         if q==i and k==j: z-=K.convert(m)
         if q==i: z+=r[k][j]
         if k==j: z-=r[i+2][q+2]
         a[row][col]=z
    return a

def matrix_residue_e(a):
    out=[]
    for i,row in enumerate(a):
        rr=[]
        for j,x in enumerate(row):
            q,c=x.leading()
            if q < -1: raise ValueError(f'higher exceptional pole {q} at {i},{j}')
            rr.append(c if q==-1 else Z)
        out.append(rr)
    return out

def matrix_finite_e(a):
    out=[]
    for row in a:
        rr=[]
        for x in row:
            q,c=x.leading()
            if q<0: raise ValueError(f'nonfinite tangential coefficient {q}')
            rr.append(c if q==0 else Z)
        out.append(rr)
    return out

def val_at(fr,point):
    def vp(poly):
        R=GF(P).poly_ring('t'); tt=R.gens[0]
        q=R.convert(poly); lin=tt-R.domain.convert(point); n=0
        while q and q.evaluate(tt,R.domain.convert(point))==0:
            q,r=R.div(q,lin); assert not r; n+=1
        return n
    return vp(fr.numer)-vp(fr.denom)

def residue_t(x,point):
    # K elements are exact univariate rational functions in t.
    if not x: return Z,10**9
    q=val_at(x,point)
    if q>=0: return Z,q
    if q != -1: return Z,q
    # residue of x dt at t=point by exact derivative cancellation.
    num=x.numer; den=x.denom
    # evaluate (t-point)*num/den through polynomial division by t-point.
    R=GF(P).poly_ring('t'); tt=R.gens[0]; lin=tt-R.domain.convert(point)
    dq,dr=R.div(den,lin); assert not dr
    nv=num.evaluate(tt,K.domain.convert(point)); dv=dq.evaluate(tt,K.domain.convert(point))
    return K.convert(int(nv))/K.convert(int(dv)),q

def text_matrix(a): return [[str(x) for x in row] for row in a]

def shear_connection(ae,at,weights):
    be=[];bt=[]
    for i in range(4):
        re=[];rt=[]
        for j in range(4):
            x=ae[i][j].shift(weights[i]-weights[j]); y=at[i][j].shift(weights[i]-weights[j])
            if i==j and weights[i]: x=x+ER([K.convert(weights[i])],[Z,O])
            re.append(x);rt.append(y)
        be.append(re);bt.append(rt)
    return be,bt

def main():
    ap=argparse.ArgumentParser();ap.add_argument('connection',type=Path);ap.add_argument('output',type=Path);args=ap.parse_args()
    d=json.loads(args.connection.read_text()); fits={(e['axis'],e['row'],e['col']):e['fit'] for e in d['entries']}
    sm3=pow(P-3,(P+1)//4,P); s5=pow(5,(P+1)//4,P); inv2=pow(2,P-2,P)
    cases=[('D1_D2_plus',(1+sm3)*inv2%P,'D2'),('D1_D2_minus',(1-sm3)*inv2%P,'D2'),
           ('D1_D3_plus',(-1+s5)*inv2%P,'D3'),('D1_D3_minus',(-1-s5)*inv2%P,'D3')]
    results=[]
    for name,u0,other in cases:
      charts=[]
      for chart,su,sv in [('u_chart',O,t),('v_chart',t,O)]:
        au=[[substitute_fit(fits[('u',i,j)],u0,u0,su,sv) for j in range(4)] for i in range(4)]
        av=[[substitute_fit(fits[('v',i,j)],u0,u0,su,sv) for j in range(4)] for i in range(4)]
        ae=[[au[i][j].sc(su)+av[i][j].sc(sv) for j in range(4)] for i in range(4)]
        at=[[av[i][j]*ER([Z,O]) if chart=='u_chart' else au[i][j]*ER([Z,O]) for j in range(4)] for i in range(4)]
        weights=[0,0,1,1];ae,at=shear_connection(ae,at,weights)
        re=matrix_residue_e(ae); tang=matrix_finite_e(at); l1=indicial(re,1)
        # Strict-transform locations in the chart.
        if chart=='u_chart':
            p1=1; p2=(4*u0-1)%P if other=='D2' else (-4*u0-1)%P
        else:
            p1=1; raw=(4*u0-1)%P if other=='D2' else (-4*u0-1)%P; p2=pow(raw,P-2,P)
        strict=[]
        for label,pt in [('D1',p1),(other,p2)]:
            rr=[]; orders=[]
            for row in tang:
                ro=[]; oo=[]
                for x in row:
                    z,q=residue_t(x,pt);ro.append(z);oo.append(q)
                rr.append(ro);orders.append(oo)
            # The exceptional residue is itself meromorphic at the incident
            # point.  Its t-residue is the corner coherence datum; direct
            # restriction of an exceptional kernel is therefore untyped.
            cr=[]; co=[]
            for row in re:
                cro=[];coo=[]
                for x in row:
                    z,q=residue_t(x,pt);cro.append(z);coo.append(q)
                cr.append(cro);co.append(coo)
            ls=indicial(rr,1); bs=nullspace(ls)
            lc=indicial(cr,0)
            incidence=[[sum(lc[i][k]*bs[j][k] for k in range(4)) for j in range(len(bs))] for i in range(4)]
            if label!= 'D1': incidence=[[-x for x in row] for row in incidence]
            ce=[cr[2][0],cr[2][1],cr[3][0],cr[3][1]]
            if label!='D1':ce=[-x for x in ce]
            augmented=[incidence[i]+[ce[i]] for i in range(4)]
            strict.append({'divisor':label,'coordinate':pt,'minimum_order':min(min(x) for x in orders),
                           'residue':text_matrix(rr),'residue_rank':rank(rr),
                           'residue_kernel_dimension':4-rank(rr),'residue_cokernel_dimension':4-rank(rr),
                           'indicial_L1_kernel_dimension':4-rank(indicial(rr,1)),
                           'exceptional_corner_minimum_order':min(map(min,co)),
                           'exceptional_corner_residue':text_matrix(cr),
                           'exceptional_corner_residue_mod_p':mod_matrix(cr),
                           'exceptional_corner_residue_rank':rank(cr),
                           'strict_L1_kernel_basis_mod_p':[mod_matrix([x])[0] for x in bs],
                           'oriented_corner_incidence_mod_p':mod_matrix(incidence),
                           'oriented_augmented_corner_map_mod_p':mod_matrix(augmented)})
        charts.append({'chart':chart,'derived_exceptional_weights':weights,'exceptional_residue':text_matrix(re),'exceptional_residue_rank':rank(re),
                       'exceptional_kernel_dimension':4-rank(re),'exceptional_cokernel_dimension':4-rank(re),
                       'exceptional_indicial_L1_kernel_dimension':4-rank(l1),'exceptional_indicial_L1_cokernel_dimension':4-rank(l1),
                       'strict_transforms':strict})
      results.append({'crossing':name,'u0':u0,'charts':charts,
                      'chart_transition':'e_v=e_u*t; s=1/t; sheared-frame transition=diag(1,1,t,t)'})
    args.output.write_text(json.dumps({'schema':'marici.gm.gysin_ordinary_crossing_blowup.v1','prime':P,
      'conventions':{'D1':'v-u','D2':'(u+v)/2-1-u^2','D3':'(u+v)/2-1+u^2',
      'u_chart':'u=u0+e, v=u0+e*t','v_chart':'u=u0+e*s, v=u0+e'},'results':results},indent=2))
if __name__=='__main__':main()
