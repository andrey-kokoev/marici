"""Directed centered certificate for the compactified k>=100 limiting tail."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from theta_inner_interval_certificate import I


@dataclass(frozen=True)
class A:
    v:I;z:I;l:I;zz:I;zl:I;ll:I;zzz:I;zzl:I;zll:I;lll:I
    @staticmethod
    def c(x:int|str|I)->"A":
        v=x if isinstance(x,I) else I.point(x);o=I.point(0);return A(v,o,o,o,o,o,o,o,o,o)
    def __add__(self,o:"A|int|str")->"A":
        o=o if isinstance(o,A) else A.c(o);return A(*(a+b for a,b in zip(self.__dict__.values(),o.__dict__.values())))
    __radd__=__add__
    def __neg__(self)->"A":return A(*(-a for a in self.__dict__.values()))
    def __sub__(self,o:"A|int|str")->"A":return self+(-o if isinstance(o,A) else A.c(-Decimal(o)))
    def __rsub__(self,o:int|str)->"A":return A.c(o)-self
    def __mul__(self,o:"A|int|str")->"A":
        o=o if isinstance(o,A) else A.c(o)
        return A(self.v*o.v,self.z*o.v+self.v*o.z,self.l*o.v+self.v*o.l,
          self.zz*o.v+I.point(2)*self.z*o.z+self.v*o.zz,
          self.zl*o.v+self.z*o.l+self.l*o.z+self.v*o.zl,
          self.ll*o.v+I.point(2)*self.l*o.l+self.v*o.ll,
          self.zzz*o.v+I.point(3)*self.zz*o.z+I.point(3)*self.z*o.zz+self.v*o.zzz,
          self.zzl*o.v+self.zz*o.l+I.point(2)*self.zl*o.z+I.point(2)*self.z*o.zl+self.l*o.zz+self.v*o.zzl,
          self.zll*o.v+self.ll*o.z+I.point(2)*self.zl*o.l+I.point(2)*self.l*o.zl+self.z*o.ll+self.v*o.zll,
          self.lll*o.v+I.point(3)*self.ll*o.l+I.point(3)*self.l*o.ll+self.v*o.lll)
    __rmul__=__mul__
    def __pow__(self,n:int)->"A":
        r=A.c(1)
        for _ in range(n):r=r*self
        return r
    def compose(self,v:I,f:I,ff:I,fff:I)->"A":
        return A(v,f*self.z,f*self.l,ff*self.z*self.z+f*self.zz,ff*self.z*self.l+f*self.zl,ff*self.l*self.l+f*self.ll,
          fff*self.z*self.z*self.z+I.point(3)*ff*self.zz*self.z+f*self.zzz,
          fff*self.z*self.z*self.l+ff*(self.zz*self.l+I.point(2)*self.zl*self.z)+f*self.zzl,
          fff*self.z*self.l*self.l+ff*(self.ll*self.z+I.point(2)*self.zl*self.l)+f*self.zll,
          fff*self.l*self.l*self.l+I.point(3)*ff*self.ll*self.l+f*self.lll)
    def exp(self)->"A":
        v=self.v.exp();return self.compose(v,v,v,v)
    def reciprocal(self)->"A":
        v=self.v.reciprocal();return self.compose(v,-v.power(2),I.point(2)*v.power(3),-I.point(6)*v.power(4))
    def __truediv__(self,o:"A|int|str")->"A":return self*(o if isinstance(o,A) else A.c(o)).reciprocal()


def evaluate(zv:I,lv:I)->tuple[A,A]:
    o=I.point(0);one=I.point(1);z=A(zv,one,o,o,o,o,o,o,o,o);l=A(lv,o,one,o,o,o,o,o,o,o)
    e=l.exp();t=(e-z)/(e+z);s=1-t*t;z2=z*z;one_minus_z2=1-z2;d=A.c(2)/(e+z)
    c00=-(t**3)
    c01=t*"0.5"+t*t*2-t**3*"1.5"-t**4*2
    scaled_c02=d*d*(1+t)*(t*t*9-t-2)/16
    c10=4*t*t*s
    c11=(t*t-1)*(t**3*"2.25"-t*t*"1.25"-t*"0.25"+"0.25")
    c20=(t*t-1)*(t**3*"2.25"-t*"0.25")
    q=z2*c00+one_minus_z2*c01+one_minus_z2**2*scaled_c02+z2*l*c10+one_minus_z2*l*c11+z2*l*l*c20
    return q,t


def centered(za:Decimal,zb:Decimal,la:Decimal,lb:Decimal)->tuple[I,I]:
    zm=(za+zb)/2;lm=(la+lb)/2;rz=(zb-za)/2;rl=(lb-la)/2;dz=I(-rz,rz);dl=I(-rl,rl)
    point,_=evaluate(I.point(zm),I.point(lm));cell,_=evaluate(I(za,zb),I(la,lb))
    q=point.v+cell.z*dz+cell.l*dl
    transverse=-point.l-cell.zl*dz-cell.ll*dl
    return q,transverse


def centered_geometry(za:Decimal,zb:Decimal,la:Decimal,lb:Decimal)->tuple[I,I]:
    zm=(za+zb)/2;lm=(la+lb)/2;dz=I(-(zb-za)/2,(zb-za)/2);dl=I(-(lb-la)/2,(lb-la)/2)
    point=evaluate(I.point(zm),I.point(lm))[0];cell=evaluate(I(za,zb),I(la,lb))[0]
    qz=point.z+cell.zz*dz+cell.zl*dl;ql=point.l+cell.zl*dz+cell.ll*dl
    qzz=point.zz+cell.zzz*dz+cell.zzl*dl
    qzl=point.zl+cell.zzl*dz+cell.zll*dl
    qll=point.ll+cell.zll*dz+cell.lll*dl
    slope=-qz/ql
    curvature=-(qzz+I.point(2)*qzl*slope+qll*slope*slope)/ql
    return slope,curvature


def main()->None:
    z0=Decimal(0);z1=Decimal("0.1");l0=Decimal("0.45");l1=Decimal("0.85");cells=16
    stack=[(z0+(z1-z0)*Decimal(i)/cells,z0+(z1-z0)*Decimal(i+1)/cells,l0+(l1-l0)*Decimal(j)/cells,l0+(l1-l0)*Decimal(j+1)/cells,0) for i in range(cells) for j in range(cells)]
    accepted=discarded=unresolved=0;lower=None;worst=None;max_z_width=Decimal(0);max_l_width=Decimal(0);accepted_boxes=[]
    while stack:
        za,zb,la,lb,d=stack.pop();q,c=centered(za,zb,la,lb)
        if q.lo>0 or q.hi<0:discarded+=1;continue
        if c.lo<=Decimal(1):
            if d>=10:unresolved+=1;continue
            if (zb-za)/(z1-z0)>=(lb-la)/(l1-l0):m=(za+zb)/2;stack.extend([(za,m,la,lb,d+1),(m,zb,la,lb,d+1)])
            else:m=(la+lb)/2;stack.extend([(za,zb,la,m,d+1),(za,zb,m,lb,d+1)])
            continue
        accepted+=1
        max_z_width=max(max_z_width,zb-za);max_l_width=max(max_l_width,lb-la)
        accepted_boxes.append((za,zb,la,lb,0))
        if lower is None or c.lo<lower:lower=c.lo;worst=(za,zb,la,lb,q,c)
    endpoint_unresolved=0;left_lower=None;right_upper=None
    for endpoint,positive in ((l0,True),(l1,False)):
        todo=[(z0,z1,0)]
        while todo:
            a,b,d=todo.pop();q,_=centered(a,b,endpoint,endpoint);ok=q.lo>0 if positive else q.hi<0
            if ok:
                if positive:left_lower=q.lo if left_lower is None else min(left_lower,q.lo)
                else:right_upper=q.hi if right_upper is None else max(right_upper,q.hi)
            elif d<16:
                m=(a+b)/2;todo.extend([(a,m,d+1),(m,b,d+1)])
            else:endpoint_unresolved+=1
    print(f"accepted={accepted}\ndiscarded={discarded}\nunresolved={unresolved}\ntransverse_lower={lower}\nworst={worst}")
    print(f"Q_left_lower={left_lower}\nQ_right_upper={right_upper}\nendpoint_unresolved={endpoint_unresolved}")
    print(f"max_accepted_z_width={max_z_width}\nmax_accepted_l_width={max_l_width}")
    slope_lo=slope_hi=curvature_lo=curvature_hi=None;geometry_accepted=geometry_discarded=geometry_unresolved=0
    while accepted_boxes:
        za,zb,la,lb,d=accepted_boxes.pop();q,_=centered(za,zb,la,lb)
        if q.lo>0 or q.hi<0:geometry_discarded+=1;continue
        slope,curvature=centered_geometry(za,zb,la,lb)
        if slope.lo>Decimal(1) and slope.hi<Decimal("2.5") and curvature.lo>0 and curvature.hi<Decimal(6):
            geometry_accepted+=1;slope_lo=slope.lo if slope_lo is None else min(slope_lo,slope.lo);slope_hi=slope.hi if slope_hi is None else max(slope_hi,slope.hi);curvature_lo=curvature.lo if curvature_lo is None else min(curvature_lo,curvature.lo);curvature_hi=curvature.hi if curvature_hi is None else max(curvature_hi,curvature.hi);continue
        if d>=8:geometry_unresolved+=1;continue
        if (zb-za)/Decimal("0.1")>=(lb-la)/Decimal("0.4"):mid=(za+zb)/2;accepted_boxes.extend(((za,mid,la,lb,d+1),(mid,zb,la,lb,d+1)))
        else:mid=(la+lb)/2;accepted_boxes.extend(((za,zb,la,mid,d+1),(za,zb,mid,lb,d+1)))
    print(f"geometry_accepted={geometry_accepted}; geometry_discarded={geometry_discarded}; geometry_unresolved={geometry_unresolved}")
    print(f"centered_implicit_slope_range=({slope_lo},{slope_hi})")
    print(f"centered_implicit_curvature_range=({curvature_lo},{curvature_hi})")
    print(f"certified={unresolved==0 and endpoint_unresolved==0 and geometry_unresolved==0 and lower is not None and lower>1}")


if __name__=="__main__":main()
