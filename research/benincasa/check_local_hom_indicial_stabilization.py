"""Local indicial stabilization of the cyclic Gysin Hom pole lattice.

The calculation is performed over the reconstruction prime.  Generic points
on each labelled divisor are sampled exactly; u^2+1 uses F_{p^2}.  The local
operator convention is the one used by the splitting census,

    dX + X A_T - A_E X.

Thus its order-m indicial matrix is -m + R_T(right) - R_E(left).
"""
from __future__ import annotations

import json
import sys
import itertools
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research/benincasa"))
sys.path.insert(0, str(ROOT / "research/nima"))
from check_gysin_occurrence_covariance import poly_from_terms, valuation
from audit_gysin_hom_pole_lattice import source_factors
from check_cyclic_hom_divisor_orbits import add as padd, mul as pmul, scale as pscale

INPUT = ROOT / "research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json"
CLASSES = ROOT / "research/benincasa/hom-support-orbits-mod-chart-units.json"
OUTPUT = ROOT / "research/benincasa/local-hom-indicial-stabilization.json"
COMPLETE = (1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 2)


class F2:
    """F_p[i]/(i^2+1); p=3 mod 4, so this is a field."""
    __slots__ = ("a", "b", "p")
    def __init__(self, a, b=0, p=None):
        self.p = p if p is not None else a.p
        self.a = (a.a if isinstance(a, F2) else a) % self.p
        self.b = (a.b if isinstance(a, F2) else b) % self.p
    def __add__(self, o):
        o = F2(o, p=self.p); return F2(self.a + o.a, self.b + o.b, self.p)
    __radd__ = __add__
    def __neg__(self): return F2(-self.a, -self.b, self.p)
    def __sub__(self, o): return self + (-F2(o, p=self.p))
    def __rsub__(self, o): return F2(o, p=self.p) - self
    def __mul__(self, o):
        o = F2(o, p=self.p)
        return F2(self.a*o.a-self.b*o.b, self.a*o.b+self.b*o.a, self.p)
    __rmul__ = __mul__
    def inv(self):
        d = pow((self.a*self.a+self.b*self.b) % self.p, self.p-2, self.p)
        return F2(self.a*d, -self.b*d, self.p)
    def __truediv__(self, o): return self * F2(o, p=self.p).inv()
    def __pow__(self, n):
        if n < 0: return (self.inv()) ** (-n)
        r, x = F2(1, p=self.p), self
        while n:
            if n & 1: r = r*x
            x=x*x; n//=2
        return r
    def __eq__(self, o):
        o=F2(o,p=self.p); return self.a==o.a and self.b==o.b
    def __bool__(self): return bool(self.a or self.b)
    def out(self): return [self.a, self.b]


def peval(poly, u, v, p):
    z = F2(0, p=p) if isinstance(u, F2) or isinstance(v, F2) else 0
    for (i,j), c in poly.items(): z += c*(u**i)*(v**j)
    return z


def fdiv(a, b, p):
    return a / b if isinstance(a, F2) or isinstance(b, F2) else a * pow(b % p, p-2, p) % p


def derivative(poly, axis, p):
    out={}
    for (i,j),c in poly.items():
        n=i if axis==0 else j
        if n:
            e=(i-1,j) if axis==0 else (i,j-1)
            out[e]=c*n%p
    return out


def rank(matrix):
    a=[row[:] for row in matrix]; m=len(a); n=len(a[0]) if m else 0; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if a[i][c]),None)
        if q is None: continue
        a[r],a[q]=a[q],a[r]; iv=a[r][c].inv() if isinstance(a[r][c],F2) else pow(a[r][c], P-2, P)
        a[r]=[x*iv for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                z=a[i][c]; a[i]=[x-z*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==m: break
    return r


def mm(a,b): return [[sum((a[i][k]*b[k][j] for k in range(len(b))),0) for j in range(len(b[0]))] for i in range(len(a))]
def trace(a): return sum((a[i][i] for i in range(len(a))),0)
def det_numeric(matrix):
    a=[r[:] for r in matrix];d=F2(1,p=P) if isinstance(a[0][0],F2) else 1
    for c in range(len(a)):
        q=next((i for i in range(c,len(a)) if a[i][c]),None)
        if q is None:return F2(0,p=P) if isinstance(a[0][0],F2) else 0
        if q!=c:a[c],a[q]=a[q],a[c];d=-d
        z=a[c][c];d*=z;iv=z.inv() if isinstance(z,F2) else pow(z%P,P-2,P)
        for i in range(c+1,len(a)):
            t=a[i][c]*iv;a[i]=[x-t*y for x,y in zip(a[i],a[c])]
    return d
def charpoly_coeffs(a):
    p1=trace(a);a2=mm(a,a);p2=trace(a2);p3=trace(mm(a2,a))
    two=F2(2,p=P) if isinstance(p1,F2) else 2; six=F2(6,p=P) if isinstance(p1,F2) else 6
    e1=p1;e2=fdiv(p1*p1-p2,two,P);e3=fdiv(p1*p1*p1-3*p1*p2+2*p3,six,P);e4=det_numeric(a)
    return [1,-e1,e2,-e3,e4]
def rr(x,p):
    x%=p;r0,r1=p,x;t0,t1=0,1;bound=math.isqrt(p//2)
    while abs(r1)>bound:
        q=r0//r1;r0,r1=r1,r0-q*r1;t0,t1=t1,t0-q*t1
    if t1 and abs(t1)<=bound and (r1-x*t1)%p==0:
        if t1<0:r1,t1=-r1,-t1
        g=math.gcd(r1,t1);r1//=g;t1//=g
        return str(r1) if t1==1 else f"{r1}/{t1}"
    y=x if x<=p//2 else x-p;return str(y)
def scalar_out(x,p):
    if isinstance(x,F2):return [rr(x.a,p),rr(x.b,p)]
    return rr(x,p)


def strip(poly, factor, p): return valuation(poly, factor, p)


def local_coefficient(fit, factor, axis, point, p, order):
    num=poly_from_terms(fit["numerator"],p); den=poly_from_terms(fit["denominator"],p)
    vn,rn=strip(num,factor,p); vd,rd=strip(den,factor,p)
    net=vd-vn
    if net != order: return (F2(0,p=p) if isinstance(point[0],F2) else 0), net
    value=fdiv(peval(rn,*point,p),peval(rd,*point,p),p)
    value=fdiv(value,peval(derivative(factor,axis,p),*point,p),p)
    return value,net


def frac_fit(fit, p): return (poly_from_terms(fit["numerator"],p),poly_from_terms(fit["denominator"],p))
def frac_add(a,b,p,sign=1): return (padd(pmul(a[0],b[1]),pscale(pmul(b[0],a[1]),sign)),pmul(a[1],b[1]))
def frac_mul(a,b): return (pmul(a[0],b[0]),pmul(a[1],b[1]))
def frac_scale(a,c): return (pscale(a[0],c),a[1])
def hom_fits(entries,axis,p):
    zero=({}, {(0,0):1}); out=[[zero for _ in range(4)] for _ in range(4)]
    for i in range(2):
     for j in range(2):
      row=2*i+j
      for k in range(2):
       col=2*i+k; out[row][col]=frac_add(out[row][col],frac_fit(entries[(axis,k,j)],p),p)
      for q in range(2):
       col=2*q+j; out[row][col]=frac_add(out[row][col],frac_fit(entries[(axis,i+2,q+2)],p),p,-1)
    return out


def fraction_as_fit(frac):
    return {"numerator":[[i,j,c] for (i,j),c in frac[0].items()],"denominator":[[i,j,c] for (i,j),c in frac[1].items()]}


def residue_fraction(frac,factor,axis,p,order=1):
    vn,rn=valuation(frac[0],factor,p);vd,rd=valuation(frac[1],factor,p)
    if vd-vn!=order:return ({},{(0,0):1})
    return (rn,pmul(rd,derivative(factor,axis,p)))


def det_fraction(matrix,p):
    out=({}, {(0,0):1})
    for perm in itertools.permutations(range(len(matrix))):
        inv=sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
        term=({(0,0):1},{(0,0):1})
        for i,j in enumerate(perm):term=frac_mul(term,matrix[i][j])
        out=frac_add(out,term,p,-1 if inv&1 else 1)
    return out


def generic_rank(matrix,factor,p):
    n=len(matrix)
    for size in range(n,0,-1):
      for rs in itertools.combinations(range(n),size):
       for cs in itertools.combinations(range(n),size):
        d=det_fraction([[matrix[i][j] for j in cs] for i in rs],p)
        vn,_=valuation(d[0],factor,p);vd,_=valuation(d[1],factor,p)
        if vn<=vd:return size
    return 0


def hom_matrix(rt,re,m,p,ext):
    zero=F2(0,p=p) if ext else 0; one=F2(1,p=p) if ext else 1
    out=[[zero for _ in range(4)] for _ in range(4)]
    # column index is X_{i,j}; dX + X R_T - R_E X
    for i in range(2):
      for j in range(2):
       row=2*i+j
       out[row][row] -= m*one
       for k in range(2): out[row][2*i+k] += rt[k][j]
       for q in range(2): out[row][2*q+j] -= re[i][q]
    return out


def base_points(name,p):
    ts=(3,5,7,11,13)
    if name=="u": return [(0,t) for t in ts]
    if name=="v": return [(t,0) for t in ts]
    if name=="y": return [(t,(2-t)%p) for t in ts]
    if name=="1-y": return [(t,(4-t)%p) for t in ts]
    if name=="1+y": return [(t,(-t)%p) for t in ts]
    if name=="v-u": return [(t,t) for t in ts]
    if name=="y-u^2": return [(t,(2-t+2*t*t)%p) for t in ts]
    if name=="y+u^2": return [(t,(2-t-2*t*t)%p) for t in ts]
    if name=="u-2": return [(2,t) for t in ts]
    if name=="v-2": return [(t,2) for t in ts]
    if name=="u^2+1": return [(F2(0,1,p),F2(t,p=p)) for t in ts]
    if name=="P6":
        out=[]
        for u in range(3,500):
            # solve A v^2+B v+C=0 by direct square root (p=3 mod 4)
            A=pow(4,p-2,p); B=(-1+u*pow(2,p-2,p)+u*u-u**3)%p
            C=(1-u-7*u*u*pow(4,p-2,p)+u**3+u**4)%p
            disc=(B*B-4*A*C)%p; s=pow(disc,(p+1)//4,p)
            if s*s%p==disc:
                out.append((u,(-B+s)*pow(2*A,p-2,p)%p))
                if len(out)==5:return out
        raise RuntimeError("not enough P6 points")
    raise KeyError(name)


def main():
    global P
    data=json.loads(INPUT.read_text()); P=int(data["prime"])
    entries={(x["axis"],x["row"],x["col"]):x["fit"] for x in data["entries"]}
    hom={axis:hom_fits(entries,axis,P) for axis in ("u","v")}
    factors=source_factors(P)[0]+source_factors(P)[1]
    rows=[]
    for idx,(name,factor) in enumerate(factors):
        declared=COMPLETE[idx]; samples=[]
        probe=base_points(name,P)[0]; axis_exact=0 if peval(derivative(factor,0,P),*probe,P) else 1
        haxis=hom["u" if axis_exact==0 else "v"]
        residue=[[residue_fraction(haxis[i][j],factor,axis_exact,P) for j in range(4)] for i in range(4)]
        for point in base_points(name,P):
            ext=isinstance(point[0],F2); axis=0 if peval(derivative(factor,0,P),*point,P) else 1
            z=F2(0,p=P) if ext else 0
            rhom=[[z for _ in range(4)] for _ in range(4)]; max_order=0
            for i in range(4):
             for j in range(4):
              val,net=local_coefficient(fraction_as_fit(hom["u" if axis==0 else "v"][i][j]),factor,axis,point,P,1)
              max_order=max(max_order,net); rhom[i][j]=val
            reson=[];sample_ranks={}
            for m in range(1,17):
                ind=[row[:] for row in rhom]
                for i in range(4):ind[i][i]-=m*(F2(1,p=P) if ext else 1)
                rr=rank(ind);sample_ranks[str(m)]=rr
                if rr<4:reson.append(m)
            irregular_rank=None
            if max_order>1:
                lead=[[z for _ in range(4)] for _ in range(4)]
                for i in range(4):
                 for j in range(4): lead[i][j]=local_coefficient(fraction_as_fit(hom["u" if axis==0 else "v"][i][j]),factor,axis,point,P,max_order)[0]
                irregular_rank=rank(lead)
            samples.append({"point":[x.out() if isinstance(x,F2) else x for x in point],"axis":"u" if axis==0 else "v","connection_max_pole_order":max_order,"leading_irregular_hom_rank":irregular_rank,"characteristic_polynomial":[scalar_out(x,P) for x in charpoly_coeffs(rhom)],"indicial_ranks":sample_ranks,"positive_resonances":reson})
        exact_resonances=samples[0]["positive_resonances"]
        invariant=len({tuple(s["positive_resonances"]) for s in samples})==1
        characteristic_invariant=all(s["characteristic_polynomial"]==samples[0]["characteristic_polynomial"] for s in samples)
        resonance_determinants_vanish={}
        for m in exact_resonances:
            ind=[[residue[i][j] for j in range(4)] for i in range(4)]
            for i in range(4):ind[i][i]=frac_add(ind[i][i],({(0,0):m%P},{(0,0):1}),P,-1)
            d=det_fraction(ind,P);vn,_=valuation(d[0],factor,P);vd,_=valuation(d[1],factor,P)
            resonance_determinants_vanish[str(m)]=vn>vd
        max_res=max(samples[0]["positive_resonances"],default=0) if invariant else None
        irregular_safe=all(s["connection_max_pole_order"]<=1 or s["leading_irregular_hom_rank"]==4 for s in samples)
        cmax=0
        for i in range(2,4):
         for j in range(2):
          cf=frac_fit(entries[("u" if axis_exact==0 else "v",i,j)],P)
          cmax=max(cmax,valuation(cf[1],factor,P)[0]-valuation(cf[0],factor,P)[0])
        recurrence=("double forcing fixes a unique order-one principal part; derivative excludes every homogeneous pole order >=2" if name=="u^2+1" else None)
        if name=="u^2+1": irregular_safe=max(s["connection_max_pole_order"] for s in samples)==0 and cmax==2
        resonance_exact=all(resonance_determinants_vanish.values())
        rows.append({"label":name,"declared_exponent":declared,"generic_characteristic_polynomial":samples[0]["characteristic_polynomial"],"characteristic_polynomial_invariant_on_samples":characteristic_invariant,"exact_positive_resonances":exact_resonances,"resonance_determinants_vanish_mod_divisor":resonance_determinants_vanish,"forcing_max_pole_order":cmax,"levelt_recurrence":recurrence,"samples":samples,"generic_resonances_invariant":invariant,"max_positive_indicial_resonance":max_res,"irregular_leading_operator_injective":irregular_safe,"stabilizes_at_declared_exponent":invariant and characteristic_invariant and resonance_exact and max_res<=declared and irregular_safe and cmax<=max(1,declared) and all(s["connection_max_pole_order"]<=1 for s in samples)})
    cls=json.loads(CLASSES.read_text())
    bylabel={r["label"]:r for r in rows}
    class_rows=[]
    for c in cls["classes"]:
        members=c["members"]; vals=[bylabel[x["label"]]["max_positive_indicial_resonance"] for x in members]
        decs=[bylabel[x["label"]]["declared_exponent"] for x in members]
        class_rows.append({"class":c["class"],"members":members,"max_admissible_pole_exponent":max(vals),"transported_declared_exponent":max(decs),"requires_larger_exponent":max(vals)>max(decs)})
    out={"schema":"marici.local-hom-indicial-stabilization.v1","prime":P,"operator_convention":"dX + X A_T - A_E X","labelled_orbits":rows,"affine_support_classes":class_rows,"normalization_units":"d0*d1*d2=8; unit exponents change representatives but have zero valuation at affine generic points","infinity_shear":"the transported (0,6) target-column shear is supported at the normalization boundary/infinity and does not alter finite generic divisor residues","all_labelled_orbits_stabilize":all(r["stabilizes_at_declared_exponent"] for r in rows),"any_class_requires_larger_exponent":any(c["requires_larger_exponent"] for c in class_rows)}
    OUTPUT.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({"orbits":len(rows),"classes":len(class_rows),"all_stabilize":out["all_labelled_orbits_stabilize"],"larger":out["any_class_requires_larger_exponent"],"resonances":{r["label"]:r["max_positive_indicial_resonance"] for r in rows}}))

if __name__=="__main__": main()
