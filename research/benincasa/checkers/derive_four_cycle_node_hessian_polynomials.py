"""Derive exact restricted Hessian polynomials without a CAS dependency."""
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-cycle-triple-points.json"
OUT = ROOT / "research/benincasa/results/four-cycle-node-hessian-polynomials.json"
VARS = ("A", "B", "C", "D", "F", "G")


def rref_nullspace(rows, n=4):
    a = [[Fraction(x) for x in row] for row in rows]
    r, pivots = 0, []
    for c in range(n):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x/q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x-q*y for x, y in zip(a[i], a[r])]
        pivots.append(c); r += 1
    out = []
    for free in (c for c in range(n) if c not in pivots):
        x = [Fraction(0)]*n; x[free] = 1
        for row, pivot in reversed(list(zip(a, pivots))):
            x[pivot] = -sum(row[c]*x[c] for c in range(pivot+1, n))
        out.append(x)
    return out


def delta(z): return [z[1]-z[0], z[2]-z[1], z[3]-z[2]]


def lin_pair(x, y):
    return [x[0]*y[0], x[1]*y[1], x[2]*y[2],
            x[0]*y[1]+x[1]*y[0], x[0]*y[2]+x[2]*y[0],
            x[1]*y[2]+x[2]*y[1]]


def ladd(*terms): return [sum(t[i] for t in terms) for i in range(6)]
def lscale(q, x): return [q*z for z in x]


def mul(x, y):
    p = {}
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            key = tuple(sorted((i, j)))
            p[key] = p.get(key, Fraction(0)) + a*b
    return {k:v for k,v in p.items() if v}


def padd(x, y, scale=1):
    z = dict(x)
    for k, v in y.items(): z[k] = z.get(k, Fraction(0)) + scale*v
    return {k:v for k,v in z.items() if v}


def substitute(poly, solve, relation):
    out = {}
    for (i,j), q in poly.items():
        left = relation if i == solve else [Fraction(k == i) for k in range(6)]
        right = relation if j == solve else [Fraction(k == j) for k in range(6)]
        out = padd(out, mul(left, right), q)
    return out


def normalize(poly):
    first = next(poly[k] for k in sorted(poly) if poly[k])
    return tuple((k, poly[k]/first) for k in sorted(poly) if poly[k])


def qstr(q): return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def expression(poly):
    terms=[]
    for (i,j), q in sorted(poly.items()):
        mon = f"{VARS[i]}^2" if i == j else f"{VARS[i]}*{VARS[j]}"
        terms.append(f"({qstr(q)})*{mon}")
    return "+".join(terms).replace("+-", "-") or "0"


records = json.loads(SOURCE.read_text())["incidence_records"]
classes, packet = Counter(), []
for record in records:
    y = [Fraction(x) for x in record["projective_y_point"]]
    k = next(i for i,x in enumerate(y) if x)
    gauge=[0]*4; gauge[k]=1
    p,q = rref_nullspace([record["pivot_normal"], gauge])
    d0=delta([x*x for x in y]); da=delta([2*y[i]*p[i] for i in range(4)])
    db=delta([2*y[i]*q[i] for i in range(4)])
    daa=delta([p[i]*p[i] for i in range(4)]); dab=delta([2*p[i]*q[i] for i in range(4)])
    dbb=delta([q[i]*q[i] for i in range(4)])
    aa=lscale(-1,ladd(lin_pair(da,da),lscale(2,lin_pair(d0,daa))))
    ab=lscale(-1,ladd(lscale(2,lin_pair(da,db)),lscale(2,lin_pair(d0,dab))))
    bb=lscale(-1,ladd(lin_pair(db,db),lscale(2,lin_pair(d0,dbb))))
    disc=padd({k:4*v for k,v in mul(aa,bb).items()},mul(ab,ab),-1)
    activation=lin_pair(d0,d0)
    if any(activation):
        solve=next(i for i,x in enumerate(activation) if x)
        relation=[-x/activation[solve] for x in activation]; relation[solve]=0
        disc=substitute(disc,solve,relation)
    key=normalize(disc); classes[(tuple(record["projective_y_point"]),key)]+=1

for (point, poly), count in sorted(classes.items(), key=lambda x:(x[0][0],str(x[0][1]))):
    packet.append({"point":list(point),"count":count,
                   "normalized_hessian":expression(dict(poly))})

assert sum(classes.values()) == 296
payload={"schema":"marici.benincasa.four_cycle_node_hessian_polynomials.v1",
         "records":296,"class_count":len(classes),"classes":packet,
         "note":"Polynomials are exact modulo the linear branch-activation equation; overall nonzero scalars are removed."}
OUT.write_text(json.dumps(payload,indent=2)+"\n")
print(json.dumps({"records":296,"classes":len(classes),
                  "counts":sorted(classes.values())}))
