import json
from decimal import Decimal, getcontext
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
getcontext().prec=100
D=Decimal

S0=[
 [D(0),D('0.45817697275369973'),D('0.17841587689616611'),D('-0.55027661013538387'),D('-0.37644211228438901'),D('0.56011483222692338')],
 [D('-0.63538704398078227'),D(0),D('-0.5094713149644986'),D('-0.48889033968845658'),D('0.0082493604828593001'),D('-0.31247474705885059')],
 [D('-0.27816302374695018'),D('-0.50284017437630824'),D(0),D('-0.058073862348780536'),D('0.46804327630365239'),D('0.66883481498785669')],
 [D('-0.27868928969357498'),D('0.53678304918232644'),D('0.45404147396496292'),D(0),D('0.63517444940278522'),D('-0.1568311056928941')],
 [D('-0.16452984636769791'),D('0.47970294824626064'),D('-0.5501140996228282'),D('0.56876584465731139'),D(0),D('0.3416063549140344')],
 [D('-0.64356106648882616'),D('-0.13774853857409267'),D('0.44702077294594211'),D('0.36237374154093333'),D('-0.48550200252964121'),D(0)]]
q=[D(6)/23,D(8)/23,D(1)/23,D(4)/23,D(2)/23,D(2)/23]
u=D(1)/6
gauge={(4,5),(5,2),(5,3),(5,4)}
vars=[(i,j) for i in range(6) for j in range(6) if i != j and (i,j) not in gauge]
assert len(vars) == 26
index={e:k for k,e in enumerate(vars)}

def build(x):
    X=[row[:] for row in S0]
    for e,v in zip(vars,x): X[e[0]][e[1]]=v
    return X

def F(x):
    X=build(x); out=[]
    for i in range(6): out.append(sum(X[i][j]**2 for j in range(6))-1)
    for i in range(6):
        for k in range(i+1,6): out.append(sum(X[i][j]*X[k][j] for j in range(6)))
    # The sixth q equation follows from row orthonormality and sum q_j=1.
    for i in range(5): out.append(sum(q[j]*X[i][j]**2 for j in range(6))-u)
    assert len(out) == 26
    return out

def J(x):
    X=build(x); rows=[]
    for i in range(6):
        row=[D(0)]*26
        for n,(a,b) in enumerate(vars):
            if a == i: row[n]=2*X[a][b]
        rows.append(row)
    for i in range(6):
        for k in range(i+1,6):
            row=[D(0)]*26
            for n,(a,b) in enumerate(vars):
                if a == i: row[n]=X[k][b]
                elif a == k: row[n]=X[i][b]
            rows.append(row)
    for i in range(5):
        row=[D(0)]*26
        for n,(a,b) in enumerate(vars):
            if a == i: row[n]=2*q[b]*X[a][b]
        rows.append(row)
    return rows

def inverse(A):
    n=len(A); M=[A[i][:]+[D(k == i) for k in range(n)] for i in range(n)]
    for c in range(n):
        p=max(range(c,n),key=lambda r:abs(M[r][c]))
        M[c],M[p]=M[p],M[c]
        pivot=M[c][c]
        assert pivot != 0
        M[c]=[x/pivot for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f=M[r][c]; M[r]=[M[r][k]-f*M[c][k] for k in range(2*n)]
    return [row[n:] for row in M]

def matvec(A,v): return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]

x=[S0[i][j] for i,j in vars]
for _ in range(20):
    residual=F(x)
    if max(abs(v) for v in residual) < D('1e-80'): break
    delta=matvec(inverse(J(x)),[-v for v in residual])
    x=[x[i]+delta[i] for i in range(26)]
residual=F(x)
newton_residual=max(abs(v) for v in residual)
assert newton_residual < D('1e-80')

class Interval:
    def __init__(self,lo,hi=None):
        self.lo=lo if hi is None else lo; self.hi=self.lo if hi is None else hi
    def __add__(self,o):
        o=o if isinstance(o,Interval) else Interval(o)
        return Interval(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __sub__(self,o):
        o=o if isinstance(o,Interval) else Interval(o)
        return Interval(self.lo-o.hi,self.hi-o.lo)
    def __rsub__(self,o): return Interval(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Interval) else Interval(o)
        vals=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return Interval(min(vals),max(vals))
    __rmul__=__mul__
    def square(self):
        if self.lo <= 0 <= self.hi: return Interval(D(0),max(self.lo*self.lo,self.hi*self.hi))
        return Interval(min(self.lo*self.lo,self.hi*self.hi),max(self.lo*self.lo,self.hi*self.hi))

def isum(vals):
    out=Interval(D(0))
    for v in vals: out=out+v
    return out

# Krawczyk certificate on a radius-1e-40 coordinate box around x.
radius=D('1e-40')
box=[Interval(v-radius,v+radius) for v in x]
# Interval Jacobian entries from the same analytic formulas.
Xbox=[None]*36
for i in range(6):
    for j in range(6):
        if i == j: Xbox[i*6+j]=Interval(D(0))
        elif (i,j) in gauge: Xbox[i*6+j]=Interval(S0[i][j])
        else: Xbox[i*6+j]=box[index[i,j]]
Jbox=[]
for i in range(6):
    row=[]
    for n,(a,b) in enumerate(vars): row.append(2*Xbox[a*6+b] if a == i else Interval(D(0)))
    Jbox.append(row)
for i in range(6):
    for k in range(i+1,6):
        row=[]
        for n,(a,b) in enumerate(vars):
            if a == i: row.append(Xbox[k*6+b])
            elif a == k: row.append(Xbox[i*6+b])
            else: row.append(Interval(D(0)))
        Jbox.append(row)
for i in range(5):
    row=[]
    for n,(a,b) in enumerate(vars): row.append(2*q[b]*Xbox[a*6+b] if a == i else Interval(D(0)))
    Jbox.append(row)
Y=inverse(J(x))
C=[]
for i in range(26):
    row=[]
    for j in range(26):
        val=Interval(D(i == j))-isum(Y[i][k]*Jbox[k][j] for k in range(26))
        row.append(val)
    C.append(row)
C_norm=max(sum(max(abs(C[i][j].lo),abs(C[i][j].hi)) for j in range(26)) for i in range(26))
assert C_norm < 1
center_correction=matvec(Y,residual)
krawczyk=[]
for i in range(26):
    image=Interval(-center_correction[i])
    for j in range(26): image=image+C[i][j]*Interval(-radius,radius)
    krawczyk.append(image)
assert all(image.lo > -radius and image.hi < radius for image in krawczyk)

# The interval root is nonzero on every off-diagonal edge.
assert all(box[index[i,j]].hi < 0 or box[index[i,j]].lo > 0 for i,j in vars)
assert all(S0[i][j] != 0 for i,j in gauge)
result={
    "schema":"marici.flavor.wp1171.v1",
    "status":"PASS",
    "question":"Does a rigorous exact solution exist near the numerical support-five candidate?",
    "dpc":{
        "conjecture":"The numerical candidate lies in a box containing an exact real orthogonal fixed-q solution.",
        "rivals":["optimizer artifact","Newton refinement","Krawczyk interval certificate","symbolic elimination"],
        "risky_consequences":["26 gauge-fixed equations","radius 1e-40 box","contracting interval Jacobian","nonzero off-diagonal entries"],
        "falsification_attempt":"A Krawczyk operator has infinity-norm contraction below one and maps the coordinate box strictly into itself.",
        "residual":"The certificate proves existence near the candidate but does not give a symbolic closed form or physical production map.",
        "disposition":"accept rigorous exact existence and select production/locality realization"
    },
    "gauge_entries":[list(e) for e in sorted(gauge)],
    "newton_residual":str(newton_residual),
    "box_radius":str(radius),
    "krawczyk_contraction_infinity_norm":str(C_norm),
    "krawczyk_containment":True,
    "exact_real_orthogonal_solution_certified":True,
    "classification":"productive rigorous gate: a zero-diagonal real unistochastic fixed-q solution exists",
    "remaining_gate":"derive source production and locality from the certified modulus",
    "hostile_gate":"do not confuse rigorous interval existence with a sourced physical production law",
    "claim_boundary":"the certificate proves an exact real solution in a 1e-40 box around the Newton point",
    "disposition":"exactification leaf resolved; production-realization rival selected"
}
(ROOT/"results"/"wp1171_exact_unistochastic_certificate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1171 PASS:",newton_residual,C_norm)
