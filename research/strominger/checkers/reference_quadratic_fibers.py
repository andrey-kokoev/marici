"""Exact missing-triple fibers: all linear channels, then diagonal quadrics.

Complete for complex nullity <=1 and minimum-norm tangencies. Higher-nullity
homogeneous fibers have a certified phase continuum when a witness is supplied;
other higher-nullity cases are explicitly unresolved, not declared unique.
"""
from fractions import Fraction
from field_metric_comparisons import pairing
from field_reconstruction import reconstruct_selected,rref,solve,positive_real,readout

def affine(rows,values,n,zero,one):
    reduced,pivots=rref([list(row)+[value] for row,value in zip(rows,values)],zero,n)
    if any(all(v==zero for v in row[:n]) and row[n]!=zero for row in reduced):raise ValueError('Inconsistent linear reference constraints')
    x=[zero]*n
    for row,pivot in zip(reduced,pivots):x[pivot]=row[n]
    basis=[]
    for free in range(n):
        if free in pivots:continue
        v=[zero]*n;v[free]=one
        for row,pivot in zip(reduced,pivots):v[pivot]=-row[free]
        basis.append(tuple(v))
    return tuple(x),tuple(basis),len(pivots)

def apply(op,x,zero):return tuple(sum((op.get((i,j),zero)*x[j] for j in range(3)),zero) for i in range(3))

def fiber(rows,values,desired,K,ops,zero,one,witness=None):
    x,U,linear_rank=affine(rows,values,3,zero,one)
    dot=lambda a,b:pairing(a,b,K,zero)
    q=lambda a,E,b:dot(a,apply(ops[E],b,zero))
    if U:
        G=tuple(tuple(dot(u,v) for v in U) for u in U)
        coefficients=solve(G,tuple(dot(u,x) for u in U),zero)
        x=tuple(x[i]-sum((u[i]*c for u,c in zip(U,coefficients)),zero) for i in range(3))
        assert all(dot(u,x)==zero for u in U)
    def valid(v):
        return all(sum((a*b for a,b in zip(row,v)),zero)==value for row,value in zip(rows,values)) and all(q(v,E,v)==desired[E] for E in ops)
    if witness is not None and not valid(witness):raise ValueError('Reference witness violates measurements')
    result={'linear_rank':linear_rank,'complex_nullity':len(U),'center':x,'basis':U,
            'quadratics':{E:{'constant':q(x,E,x)-desired[E],
                             'linear':tuple(q(x,E,u) for u in U),
                             'conjugate_linear':tuple(q(u,E,x) for u in U),
                             'quadratic':tuple(tuple(q(u,E,v) for v in U) for u in U)} for E in ops}}
    def unique(v,reason):
        if not valid(v):raise ValueError('Unique candidate violates remaining quadrics')
        return dict(result,kind='unique',solution=v,reason=reason)
    if not U:return unique(x,'all-channel linear constraints')
    remaining=desired['P']+desired['Q']-dot(x,x)
    if remaining.flip(8)!=remaining:raise ValueError('Nonreal residual norm')
    if remaining==zero:return unique(x,'minimum-norm quadratic tangency')
    if not positive_real(remaining):raise ValueError('Negative residual norm')
    if len(U)>1:
        if all(v==zero for v in x) and witness is not None:
            return dict(result,kind='continuous',reason='nonzero homogeneous witness has a full relative-phase orbit')
        return dict(result,kind='unresolved',reason='higher-nullity quadratic intersection not classified')
    u=U[0];radius=remaining/dot(u,u)
    imaginary=type(one)(tuple(Fraction(int(i==8)) for i in range(16)))
    real=lambda z:(z+z.flip(8))/2
    imag=lambda z:(z-z.flip(8))/(2*imaginary)
    equations=[];rhs=[]
    for E in ops:
        a=q(x,E,u);b=q(u,E,x);target=desired[E]-q(x,E,x)-radius*q(u,E,u)
        coefficients=(a+b,imaginary*(a-b))
        for part in (real,imag):
            equations.append(tuple(part(v) for v in coefficients));rhs.append(part(target))
    z,V,real_rank=affine(equations,rhs,2,zero,one)
    result.update(circle_radius_squared=radius,real_constraint_rank=real_rank)
    vector=lambda s,t:tuple(x[i]+u[i]*(s+imaginary*t) for i in range(3))
    if real_rank==2:
        if z[0]*z[0]+z[1]*z[1]!=radius:raise ValueError('Quadratic circle has no solution')
        return unique(vector(*z),'two real constraints on the residual circle')
    if real_rank==0:return dict(result,kind='continuous',reason='entire residual circle')
    row_index=next(i for i,row in enumerate(equations) if any(v!=zero for v in row))
    alpha,beta=equations[row_index];gamma=rhs[row_index];norm=alpha*alpha+beta*beta
    s,t=alpha*gamma/norm,beta*gamma/norm
    gap=radius-s*s-t*t
    if gap==zero:return unique(vector(s,t),'line tangent to the residual circle')
    if not positive_real(gap):raise ValueError('Line misses the residual circle')
    base=vector(s,t);direction=tuple(v*(-beta+imaginary*alpha) for v in u);radicand=gap/norm
    # Both exact algebraic alternatives are base +/- sqrt(radicand)*direction.
    # Verify in the quadratic extension without assuming its root is in A.
    for E in ops:
        assert q(base,E,base)+radicand*q(direction,E,direction)==desired[E]
        assert q(base,E,direction)+q(direction,E,base)==zero
    return dict(result,kind='finite-two',reason='line cuts the residual circle twice',
                alternatives={'base':base,'direction':direction,'radicand':radicand})

def constraints(data,K,ops,zero,one):
    selected=reconstruct_selected(data,K,ops,zero,one)
    field=selected['representative'];rho=selected['normalization_squared'];a,t=data['P']['reference']
    rows=[];values=[];desired={}
    q=lambda left,E,right:pairing(left,apply(ops[E],right,zero),K,zero)
    for E in ops:
        desired[E]=rho*data[E]['blocks']['state'][a][a]-sum((q(field[a,d],E,field[a,d]) for d in range(4) if d not in (a,t)),zero)
        for b in range(4):
            if b in (a,t):continue
            w=field[b,t];op=ops[E]
            forward=tuple(sum((w[i].flip(8)*K[i,k]*op.get((k,j),zero) for i in range(3) for k in range(3)),zero) for j in range(3))
            ew=apply(op,w,zero)
            reverse=tuple(sum((K[j,k]*ew[k] for k in range(3)),zero).flip(8) for j in range(3))
            known_forward=sum((q(field[b,d],E,field[a,d]) for d in range(4) if d not in (a,b,t)),zero)
            known_reverse=sum((q(field[a,d],E,field[b,d]) for d in range(4) if d not in (a,b,t)),zero)
            rows.extend((forward,reverse))
            values.extend((rho*data[E]['blocks']['state'][a][b]-known_forward,
                           (rho*data[E]['blocks']['state'][b][a]-known_reverse).flip(8)))
    return selected,tuple(rows),tuple(values),desired

def validate_completion(data,selected,missing,K,ops,zero):
    field=dict(selected['representative']);field[data['P']['reference']]=tuple(missing)
    rho=selected['normalization_squared'];predicted=readout(field,K,ops,data['P']['reference'],zero)
    if any(predicted[E]['blocks'][branch][i][j]!=rho*v for E in data for branch,m in data[E]['blocks'].items() for i,row in enumerate(m) for j,v in enumerate(row)):
        raise ValueError('Completion fails full measurement regeneration')
    return field,rho
