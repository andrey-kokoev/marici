"""Directed centered-box certificate prototype for the compact no-fold chart."""

from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext

import theta_inner_interval_certificate as interval

interval.PRECISION=40
I=interval.I
PRECISION=interval.PRECISION


ZERO=I.point(0);ONE=I.point(1);TWO=I.point(2)


def sqrt_i(value:I)->I:
    assert value.lo>=0
    with localcontext() as context:
        context.prec=PRECISION;context.rounding=ROUND_FLOOR;lo=value.lo.sqrt()
    with localcontext() as context:
        context.prec=PRECISION;context.rounding=ROUND_CEILING;hi=value.hi.sqrt()
    return I(lo,hi)


@dataclass(frozen=True)
class J:
    v:I
    d:tuple[I,I,I]

    @staticmethod
    def constant(value:int|str|Decimal|I)->"J":
        interval=value if isinstance(value,I) else I.point(value)
        return J(interval,(ZERO,ZERO,ZERO))

    @staticmethod
    def variable(value:I,index:int)->"J":
        derivatives=[ZERO,ZERO,ZERO];derivatives[index]=ONE
        return J(value,tuple(derivatives))

    def __add__(self,other:"J"):
        return J(self.v+other.v,tuple(a+b for a,b in zip(self.d,other.d)))
    def __neg__(self):return J(-self.v,tuple(-a for a in self.d))
    def __sub__(self,other:"J"):return self+(-other)
    def __mul__(self,other:"J"):
        return J(self.v*other.v,tuple(a*other.v+self.v*b for a,b in zip(self.d,other.d)))
    def reciprocal(self):
        inverse=self.v.reciprocal();square=inverse*inverse
        return J(inverse,tuple(-a*square for a in self.d))
    def __truediv__(self,other:"J"):return self*other.reciprocal()
    def power(self,n:int):
        result=J.constant(1)
        for _ in range(n):result=result*self
        return result
    def exp(self):
        value=self.v.exp();return J(value,tuple(value*a for a in self.d))
    def sqrt(self):
        value=sqrt_i(self.v);return J(value,tuple(a/(TWO*value) for a in self.d))


def evaluate(p:J,c:J,h:J)->tuple[J,J]:
    cls=type(p);one,two=cls.constant(1),cls.constant(2)
    q=p*c
    ep=h.exp()*(((one+p)/(one-p)*(one-q)/(one+q)).sqrt())
    t=(ep-one)/(ep+one)
    er=((one-q.power(2))/(one-p.power(2))).sqrt()*(p*h).exp()
    r=(er-one)/(er+one)
    slope_sum=p+q;product=p*q
    nt=cls.constant(4)*t.power(3)+two*t*product-two*t*(cls.constant(2)+product)*r.power(2)-slope_sum*r*(one-r.power(2))
    nr=-t*slope_sum+two*(one-two*t.power(2)-t.power(2)*product)*r+cls.constant(3)*t*slope_sum*r.power(2)
    vt=one-t.power(2);vr=p*(one-r.power(2))
    g=vt*nt+vr*nr
    ntt=cls.constant(12)*t.power(2)+two*product-two*(cls.constant(2)+product)*r.power(2)
    ntr=-cls.constant(4)*t*(cls.constant(2)+product)*r-slope_sum*(one-cls.constant(3)*r.power(2))
    nrr=two*(one-two*t.power(2)-t.power(2)*product)+cls.constant(6)*t*slope_sum*r
    dg=-two*t*vt*nt-two*p*r*vr*nr+vt.power(2)*ntt+two*vt*vr*ntr+vr.power(2)*nrr
    reserve=-dg
    return g,reserve


def chart_evaluate(u:J,c:J,m:J)->tuple[J,J]:
    cls=type(u)
    p=(-u).exp()
    h=m+cls.constant(2)*u
    return evaluate(p,c,h)


def centered(bounds:tuple[tuple[Decimal,Decimal],...])->tuple[I,I]:
    mid=tuple((a+b)/2 for a,b in bounds)
    radius=tuple((b-a)/2 for a,b in bounds)
    point=chart_evaluate(*(J.variable(I.point(mid[i]),i) for i in range(3)))
    cell=chart_evaluate(*(J.variable(I(*bounds[i]),i) for i in range(3)))
    displacement=tuple(I(-r,r) for r in radius)
    enclosures=[]
    for point_jet,cell_jet in zip(point,cell):
        result=point_jet.v
        for derivative,delta in zip(cell_jet.d,displacement):result=result+derivative*delta
        enclosures.append(result)
    return tuple(enclosures)


def certify()->None:
    # u=-log(p), M=H-2u=H+2log(p) aligns the critical sheet.
    domain=((Decimal("1.6094379124341002"),Decimal("2.302585092994046")),(Decimal(0),Decimal(1)),(Decimal("0.8"),Decimal("1.1")))
    divisions=(8,8,48)
    stack=[]
    for i in range(divisions[0]):
        for j in range(divisions[1]):
            box=[]
            for axis,index in enumerate((i,j)):
                a,b=domain[axis];n=divisions[axis];box.append((a+(b-a)*index/n,a+(b-a)*(index+1)/n))
            for k in range(divisions[2]):
                a,b=domain[2];n=divisions[2]
                stack.append((tuple(box),(a+(b-a)*k/n,a+(b-a)*(k+1)/n),0))
    accepted=discarded=unresolved=0;lower=None;worst=None
    target=Decimal(0)
    processed=0
    while stack:
        processed+=1
        if processed%2000==0:
            print(f"progress processed={processed} pending={len(stack)} accepted={accepted} discarded={discarded} unresolved={unresolved}",flush=True)
        base,m_bounds,depth=stack.pop()
        initial_g,_=centered((base[0],base[1],m_bounds))
        if initial_g.lo>0 or initial_g.hi<0:
            discarded+=1;continue
        # Parametric interval Newton contraction in the transverse M coordinate.
        contracted=m_bounds
        empty=False
        for _ in range(6):
            ma,mb=contracted;middle=(ma+mb)/2
            slice_box=(base[0],base[1],(middle,middle))
            g_slice,_=centered(slice_box)
            full_box=(base[0],base[1],contracted)
            u=J.variable(I(*base[0]),0);c=J.variable(I(*base[1]),1);m=J.variable(I(*contracted),2)
            derivative=chart_evaluate(u,c,m)[0].d[2]
            if derivative.lo<=0<=derivative.hi:break
            newton=I.point(middle)-g_slice/derivative
            lo=max(ma,newton.lo);hi=min(mb,newton.hi)
            if lo>hi:empty=True;break
            if lo==ma and hi==mb:break
            contracted=(lo,hi)
        if empty:
            discarded+=1;continue
        box=(base[0],base[1],contracted);g,curvature=centered(box)
        if curvature.lo>target:
            accepted+=1
            if lower is None or curvature.lo<lower:lower=curvature.lo;worst=(box,g,curvature)
            continue
        if depth>=10:
            unresolved+=1
            if unresolved<=5:print(f"unresolved_example={box} g={g} reserve={curvature}",flush=True)
            continue
        full=(base[0],base[1],contracted)
        widths=[b-a for a,b in full]
        normalized=[widths[i]/(domain[i][1]-domain[i][0]) for i in range(3)]
        axis=max(range(3),key=lambda i:normalized[i]);a,b=full[axis];middle=(a+b)/2
        for replacement in ((a,middle),(middle,b)):
            child=list(full);child[axis]=replacement
            stack.append(((child[0],child[1]),child[2],depth+1))
    print(f"accepted={accepted}\ndiscarded={discarded}\nunresolved={unresolved}\nreserve_lower={lower}\nworst={worst}")
    print(f"certified={unresolved==0 and accepted>0 and lower is not None and lower>target}")


if __name__=="__main__":certify()
