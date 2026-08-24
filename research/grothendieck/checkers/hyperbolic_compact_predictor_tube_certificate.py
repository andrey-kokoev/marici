"""Directed certificate on a thin polynomial predictor tube, p in [0.4,0.7]."""

from decimal import Decimal
from dataclasses import dataclass
import sys

import theta_inner_interval_certificate as interval
import hyperbolic_compact_middle_centered_certificate as base

interval.PRECISION=25
base.PRECISION=25
I,J,chart_evaluate=base.I,base.J,base.chart_evaluate


U0=Decimal("0.3566749439387324")
U1=Decimal("0.9162907318741551")
RHO=Decimal("0.02")
POWERS=((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(4,0),(4,1),(5,0))
COEFFICIENTS=tuple(Decimal(value) for value in (
    "1.164635150766844","0.3517780852211224","0.19755133767897876",
    "0.05033228385167804","0.01978898922398497","0.0193960952110962",
    "0.18498950268144243","-0.01334593293346967","-0.30309010031946954",
    "-0.19722469717057795","-0.07603945507205546","-0.33910216233395035",
    "-0.3560549871042063","0.3937702930671297","0.2217643158516427",
    "0.2772342364691563","0.22307100450986603","-0.28127191534612644",
    "-0.16252394253717495","0.0037800581039069037","0.040614553959312585",
))


def predictor(u:J,c:J)->J:
    cls=type(u)
    x=(u-cls.constant(U0))/cls.constant(U1-U0)
    total=cls.constant(0)
    for coefficient,(i,j) in zip(COEFFICIENTS,POWERS):
        total=total+cls.constant(coefficient)*x.power(i)*c.power(j)
    return total


def face_function(sign:int):
    def function(u:J,c:J)->J:
        m=predictor(u,c)+type(u).constant(RHO*sign)
        return chart_evaluate(u,c,m)[0]
    return function


def tube_curvature(u:J,c:J,e:J)->J:
    return chart_evaluate(u,c,predictor(u,c)+e)[1]


@dataclass(frozen=True)
class J2:
    v:I
    d:tuple[I,I,I]
    h:tuple[tuple[I,I,I],tuple[I,I,I],tuple[I,I,I]]

    @staticmethod
    def constant(value):
        interval=value if isinstance(value,I) else I.point(value)
        zero=I.point(0);row=(zero,zero,zero)
        return J2(interval,row,(row,row,row))

    @staticmethod
    def variable(value:I,index:int):
        zero,one=I.point(0),I.point(1);gradient=[zero,zero,zero];gradient[index]=one;row=(zero,zero,zero)
        return J2(value,tuple(gradient),(row,row,row))

    def __add__(self,other):
        return J2(self.v+other.v,tuple(a+b for a,b in zip(self.d,other.d)),tuple(tuple(self.h[i][j]+other.h[i][j] for j in range(3)) for i in range(3)))
    def __neg__(self):return J2(-self.v,tuple(-a for a in self.d),tuple(tuple(-self.h[i][j] for j in range(3)) for i in range(3)))
    def __sub__(self,other):return self+(-other)
    def __mul__(self,other):
        gradient=tuple(self.d[i]*other.v+self.v*other.d[i] for i in range(3))
        hessian=tuple(tuple(self.h[i][j]*other.v+self.v*other.h[i][j]+self.d[i]*other.d[j]+self.d[j]*other.d[i] for j in range(3)) for i in range(3))
        return J2(self.v*other.v,gradient,hessian)
    def unary(self,value:I,first:I,second:I):
        return J2(value,tuple(first*a for a in self.d),tuple(tuple(first*self.h[i][j]+second*self.d[i]*self.d[j] for j in range(3)) for i in range(3)))
    def reciprocal(self):
        inverse=self.v.reciprocal();first=-inverse*inverse;second=I.point(2)*inverse*inverse*inverse
        return self.unary(inverse,first,second)
    def __truediv__(self,other):return self*other.reciprocal()
    def power(self,n):
        result=J2.constant(1)
        for _ in range(n):result=result*self
        return result
    def exp(self):
        value=self.v.exp();return self.unary(value,value,value)
    def sqrt(self):
        from hyperbolic_compact_middle_centered_certificate import sqrt_i
        value=sqrt_i(self.v);first=I.point(1)/(I.point(2)*value);second=-I.point(1)/(I.point(4)*value*value*value)
        return self.unary(value,first,second)


def centered(function,bounds):
    dimension=len(bounds);mid=tuple((a+b)/2 for a,b in bounds);radius=tuple((b-a)/2 for a,b in bounds)
    point=function(*(J.variable(I.point(mid[i]),i) for i in range(dimension)))
    cell=function(*(J.variable(I(*bounds[i]),i) for i in range(dimension)))
    result=point.v
    for derivative,r in zip(cell.d,[I(-value,value) for value in radius]):result=result+derivative*r
    return result


def centered_second(function,bounds):
    dimension=len(bounds);mid=tuple((a+b)/2 for a,b in bounds);radius=tuple((b-a)/2 for a,b in bounds)
    point=function(*(J2.variable(I.point(mid[i]),i) for i in range(dimension)))
    cell=function(*(J2.variable(I(*bounds[i]),i) for i in range(dimension)))
    delta=[I(-value,value) for value in radius];result=point.v
    for i in range(dimension):result=result+point.d[i]*delta[i]
    half=I.point("0.5")
    for i in range(dimension):
        for j in range(dimension):result=result+half*cell.h[i][j]*delta[i]*delta[j]
    return result


def centered_flat_face(bounds,e_value):
    from hyperbolic_compact_flat_formula_generator import F,flat
    mid=tuple((a+b)/2 for a,b in bounds);radius=tuple((b-a)/2 for a,b in bounds)
    point=flat(F(I.point(mid[0])),F(I.point(mid[1])),F(I.point(e_value)))
    cell=flat(F(I(*bounds[0])),F(I(*bounds[1])),F(I.point(e_value)))
    du,dc=I(-radius[0],radius[0]),I(-radius[1],radius[1]);half=I.point("0.5")
    result=point[0].v+point[1].v*du+point[2].v*dc
    result=result+half*cell[3].v*du*du+cell[4].v*du*dc+half*cell[5].v*dc*dc
    return result


def centered_flat_tube(bounds):
    from hyperbolic_compact_flat_formula_generator import F,flat_tube
    mid=tuple((a+b)/2 for a,b in bounds);radius=tuple((b-a)/2 for a,b in bounds)
    point=flat_tube(*(F(I.point(value)) for value in mid))
    cell=flat_tube(*(F(I(*bound)) for bound in bounds))
    delta=[I(-value,value) for value in radius];half=I.point("0.5")
    result=point[0].v
    for index in range(3):result=result+point[1+index].v*delta[index]
    result=result+half*cell[4].v*delta[0]*delta[0]+cell[5].v*delta[0]*delta[1]+cell[6].v*delta[0]*delta[2]
    result=result+half*cell[7].v*delta[1]*delta[1]+cell[8].v*delta[1]*delta[2]+half*cell[9].v*delta[2]*delta[2]
    return result


def certify(name,function,domain,want_positive,seed,max_depth=12,flat_e=None,flat_tube_mode=False):
    stack=[]
    def seed_boxes(axis,prefix):
        if axis==len(domain):stack.append((tuple(prefix),0));return
        a,b=domain[axis]
        for index in range(seed[axis]):
            lo=a+(b-a)*index/seed[axis];hi=a+(b-a)*(index+1)/seed[axis]
            seed_boxes(axis+1,prefix+[(lo,hi)])
    seed_boxes(0,[])
    accepted=unresolved=processed=0;extreme=None;worst=None
    while stack:
        box,depth=stack.pop();processed+=1
        if flat_e is not None:value=centered_flat_face(box,flat_e)
        elif flat_tube_mode:value=centered_flat_tube(box)
        else:value=centered_second(function,box)
        if processed%250==0:print(f"{name}_progress processed={processed} pending={len(stack)} accepted={accepted} unresolved={unresolved}",flush=True)
        succeeds=value.lo>0 if want_positive else value.hi<0
        if succeeds:
            accepted+=1
            candidate=value.lo if want_positive else value.hi
            if extreme is None or (candidate<extreme if want_positive else candidate>extreme):extreme=candidate;worst=(box,value)
            continue
        if depth>=max_depth:
            unresolved+=1
            if unresolved<=3:print(f"{name}_unresolved={box} value={value}",flush=True)
            continue
        widths=[(b-a)/(domain[i][1]-domain[i][0]) for i,(a,b) in enumerate(box)]
        axis=max(range(len(box)),key=lambda i:widths[i]);a,b=box[axis];middle=(a+b)/2
        for replacement in ((a,middle),(middle,b)):
            child=list(box);child[axis]=replacement;stack.append((tuple(child),depth+1))
    print(f"{name}: processed={processed} accepted={accepted} unresolved={unresolved} extreme={extreme} worst={worst}")
    return unresolved==0


def certify_root_curvature(base,max_depth=12):
    from hyperbolic_compact_flat_formula_generator import F,flat
    stack=[];seed=(8,8)
    for i in range(seed[0]):
        for j in range(seed[1]):
            box=[]
            for axis,index in enumerate((i,j)):
                a,b=base[axis];n=seed[axis];box.append((a+(b-a)*index/n,a+(b-a)*(index+1)/n))
            stack.append((tuple(box),(-RHO,RHO),0))
    processed=accepted=unresolved=0;lower=None;worst=None
    while stack:
        box,e_bounds,depth=stack.pop();processed+=1;contracted=e_bounds
        for _ in range(6):
            ea,eb=contracted;em=(ea+eb)/2
            g_slice=centered_flat_face(box,em)
            values=flat(F(I(*box[0])),F(I(*box[1])),F(I(ea,eb)))
            ge=values[6].v
            if ge.lo<=0<=ge.hi:break
            newton=I.point(em)-g_slice/ge;lo=max(ea,newton.lo);hi=min(eb,newton.hi)
            if lo>hi:
                contracted=None;break
            if lo==ea and hi==eb:break
            contracted=(lo,hi)
        if contracted is None:continue
        value=centered_flat_tube(box+(contracted,))
        if value.lo>0:
            accepted+=1
            if lower is None or value.lo<lower:lower=value.lo;worst=(box,contracted,value)
            continue
        if depth>=max_depth:
            unresolved+=1
            if unresolved<=3:print(f"root_curvature_unresolved={box} e={contracted} value={value}",flush=True)
            continue
        widths=[(b-a)/(base[i][1]-base[i][0]) for i,(a,b) in enumerate(box)];axis=max(range(2),key=lambda i:widths[i]);a,b=box[axis];middle=(a+b)/2
        for replacement in ((a,middle),(middle,b)):
            child=list(box);child[axis]=replacement;stack.append((tuple(child),contracted,depth+1))
        if processed%100==0:print(f"root_curvature_progress processed={processed} pending={len(stack)} accepted={accepted} unresolved={unresolved}",flush=True)
    print(f"root_curvature: processed={processed} accepted={accepted} unresolved={unresolved} lower={lower} worst={worst}")
    return unresolved==0 and accepted>0


def main():
    base=((U0,U1),(Decimal(0),Decimal(1)))
    if "--root-only" in sys.argv:
        tube=certify_root_curvature(base);print(f"root_only_certified={tube}");return
    lower=certify("lower_face",face_function(-1),base,True,(8,8),10,flat_e=-RHO)
    upper=certify("upper_face",face_function(1),base,False,(8,8),10,flat_e=RHO)
    tube=certify_root_curvature(base)
    print(f"certified={lower and upper and tube}")


if __name__=="__main__":main()
