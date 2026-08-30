"""Flat centered directed certificate for the sharp limiting collar."""

from __future__ import annotations

from decimal import Decimal, ROUND_CEILING, localcontext

from theta_inner_interval_certificate import I, PRECISION


TERMS=(
 (3,0,0,"-1"),(1,0,1,"0.5"),(2,0,1,"2"),(3,0,1,"-1.5"),(4,0,1,"-2"),
 (0,0,2,"-0.125"),(1,0,2,"0.0625"),(2,0,2,"0.75"),(3,0,2,"-0.625"),(4,0,2,"-0.625"),(5,0,2,"0.5625"),
 (2,1,0,"4"),(4,1,0,"-4"),(0,1,1,"-0.25"),(1,1,1,"0.25"),(2,1,1,"1.5"),(3,1,1,"-2.5"),(4,1,1,"-1.25"),(5,1,1,"2.25"),
 (1,2,0,"0.25"),(3,2,0,"-2.5"),(5,2,0,"2.25"),
)


def raw(u:I,l:I)->tuple[I,I,I,I,I,I,I,I]:
    k=u.exp()-I.point(1);e=(l+u/I.point(2)).exp();t=(e-I.point(1))/(e+I.point(1));s=I.point(1)-t.power(2)
    tp=[I.point(1)];lp=[I.point(1)];kp=[I.point(1)]
    for _ in range(5):tp.append(tp[-1]*t)
    for _ in range(2):lp.append(lp[-1]*l);kp.append(kp[-1]*k)
    q=qt=ql=qk=qtt=qtl=qtk=qll=qkl=qkk=I.point(0)
    for a,b,c,cs in TERMS:
        coef=I.point(cs);base=coef*tp[a]*lp[b]*kp[c];q=q+base
        if a:qt=qt+coef*I.point(a)*tp[a-1]*lp[b]*kp[c]
        if b:ql=ql+coef*I.point(b)*tp[a]*lp[b-1]*kp[c]
        if c:qk=qk+coef*I.point(c)*tp[a]*lp[b]*kp[c-1]
        if a>=2:qtt=qtt+coef*I.point(a*(a-1))*tp[a-2]*lp[b]*kp[c]
        if a and b:qtl=qtl+coef*I.point(a*b)*tp[a-1]*lp[b-1]*kp[c]
        if a and c:qtk=qtk+coef*I.point(a*c)*tp[a-1]*lp[b]*kp[c-1]
        if b>=2:qll=qll+coef*I.point(b*(b-1))*tp[a]*lp[b-2]*kp[c]
        if b and c:qkl=qkl+coef*I.point(b*c)*tp[a]*lp[b-1]*kp[c-1]
        if c>=2:qkk=qkk+coef*I.point(c*(c-1))*tp[a]*lp[b]*kp[c-2]
    tu=s/I.point(4);tl=s/I.point(2);tuu=-(t*s)/I.point(8);tul=-(t*s)/I.point(4);tll=-(t*s)/I.point(2);ku=I.point(1)+k
    qu=qt*tu+qk*ku
    qL=ql+qt*tl
    quu=qtt*tu.power(2)+I.point(2)*qtk*tu*ku+qkk*ku.power(2)+qt*tuu+qk*ku
    quL=qtt*tu*tl+qtl*tu+qtk*tl*ku+qt*tul+qkl*ku
    qLL=qll+I.point(2)*qtl*tl+qtt*tl.power(2)+qt*tll
    curvature=-(s*qL)
    su=-(t*s)/I.point(2);sl=-(t*s)
    cu=-(su*qL+s*quL);cl=-(sl*qL+s*qLL)
    return q,qu,qL,curvature,cu,cl,quu,qLL


def centered(ua:Decimal,ub:Decimal,la:Decimal,lb:Decimal)->tuple[I,I]:
    um=(ua+ub)/2;lm=(la+lb)/2;ru=(ub-ua)/2;rl=(lb-la)/2;du=I(-ru,ru);dl=I(-rl,rl)
    point=raw(I.point(um),I.point(lm));cell=raw(I(ua,ub),I(la,lb))
    return point[0]+cell[1]*du+cell[2]*dl, point[3]+cell[4]*du+cell[5]*dl


def log_upper(n:int)->Decimal:
    with localcontext() as c:c.prec=PRECISION;c.rounding=ROUND_CEILING;return Decimal(n).ln()


def certify(name:str,umin:Decimal,umax:Decimal,l0:Decimal,l1:Decimal,target:Decimal)->bool:
    cells=16
    stack=[(umin+(umax-umin)*Decimal(i)/cells,umin+(umax-umin)*Decimal(i+1)/cells,l0+(l1-l0)*Decimal(j)/cells,l0+(l1-l0)*Decimal(j+1)/cells,0) for i in range(cells) for j in range(cells)]
    accepted=discarded=unresolved=0;lower=None;worst=None
    while stack:
        ua,ub,la,lb,d=stack.pop();q,c=centered(ua,ub,la,lb)
        if q.lo>0 or q.hi<0:discarded+=1;continue
        if c.lo<=target:
            if d>=10:unresolved+=1;continue
            if (ub-ua)/(umax-umin) >= (lb-la)/(l1-l0):m=(ua+ub)/2;stack.extend([(ua,m,la,lb,d+1),(m,ub,la,lb,d+1)])
            else:m=(la+lb)/2;stack.extend([(ua,ub,la,m,d+1),(ua,ub,m,lb,d+1)])
            continue
        accepted+=1
        if lower is None or c.lo<lower:lower=c.lo;worst=(ua,ub,la,lb,q,c)
    print(f"zone={name}\naccepted={accepted}\ndiscarded={discarded}\nunresolved={unresolved}\ncurvature_lower={lower}\nworst={worst}")
    left_lower=None;right_upper=None;endpoint_unresolved=0
    for endpoint,want_positive in ((l0,True),(l1,False)):
        endpoint_stack=[(umin,umax,0)]
        while endpoint_stack:
            ua,ub,d=endpoint_stack.pop();q,_=centered(ua,ub,endpoint,endpoint)
            succeeds=q.lo>0 if want_positive else q.hi<0
            if succeeds:
                if want_positive:left_lower=q.lo if left_lower is None else min(left_lower,q.lo)
                else:right_upper=q.hi if right_upper is None else max(right_upper,q.hi)
                continue
            if d>=16:endpoint_unresolved+=1;continue
            m=(ua+ub)/2;endpoint_stack.extend([(ua,m,d+1),(m,ub,d+1)])
    print(f"Q_left_lower={left_lower}\nQ_right_upper={right_upper}")
    print(f"endpoint_unresolved={endpoint_unresolved}")
    certified=(unresolved==0 and endpoint_unresolved==0 and lower is not None and lower>target and left_lower is not None and left_lower>0 and right_upper is not None and right_upper<0)
    print(f"certified={certified}")
    return certified


def main()->None:
    zones=(
        ("k_0_1",Decimal(0),log_upper(2),Decimal("1.5"),Decimal("2.25"),Decimal("0.5")),
        ("k_1_3",log_upper(2),log_upper(4),Decimal("1.2"),Decimal("2.05"),Decimal("0.5")),
        ("k_3_10",log_upper(4),log_upper(11),Decimal("0.8"),Decimal("1.7"),Decimal("0.5")),
        ("k_10_100",log_upper(11),log_upper(101),Decimal("0.45"),Decimal("1.35"),Decimal("0.5")),
    )
    results=[certify(*zone) for zone in zones]
    print(f"all_zones_certified={all(results)}")


if __name__=="__main__":main()
