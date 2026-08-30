"""WP51 symbolic: exact eps-expansion of F_class along rays s13 = r*eps.

Masses = exact rationals (OBS17). Symbols: e (s23), r (s13/s23),
s (s12), g (cos delta), Sg (sin delta, t-class only, O(e^0)).
All quantities truncated at O(e^2). Anchors u,c to O(e^2); t to O(e^0).
"""
import sympy as sp

e, r, s, g, Sg = sp.symbols('e r s g Sg', positive=True)

def R(x):  # exact rational mass
    return sp.Rational(x)

yu2 = sp.Rational(704, 10**8)**2
yc2 = sp.Rational(356, 10**5)**2
yt2 = sp.Rational(967, 10**3)**2
yd2 = sp.Rational(154, 10**7)**2
ys2 = sp.Rational(306, 10**6)**2
yb2 = sp.Rational(1630, 10**5)**2
lam = (yd2, ys2, yb2)

c12sq = 1 - s**2
c12 = sp.sqrt(c12sq)
c13sq = 1 - r**2*e**2
c23sq = 1 - e**2

# |V|^2 rows (truncated at O(e^2))
row0 = [c12sq*c13sq, s**2*c13sq, r**2*e**2]
X = 2*s*c12*g*r*e**2  # interference term
row1 = [s**2*c23sq + X, c12sq*c23sq - X, e**2*c13sq]

e1 = sum(lam); e2 = lam[0]*lam[1]+lam[0]*lam[2]+lam[1]*lam[2]; e3 = lam[0]*lam[1]*lam[2]

def ser(x, n=3):
    return sp.expand(sp.series(x, e, 0, n).removeO())

def invert(um):
    d0 = sum(um[i]*lam[i] for i in range(3))
    beta = e3*sum(um[i]/lam[i] for i in range(3))
    e1p = e1 - d0
    d1 = ser((beta*d0 - e3)/(e1p*d0 - e2 + beta))
    v2 = ser((d0-lam[0])*(d0-lam[1])*(d0-lam[2])/(d1-d0))
    w2 = ser((d1-lam[0])*(d1-lam[1])*(d1-lam[2])/(d0-d1))
    return v2, w2

def F_anchor(anchor):
    if anchor == 'u':
        um = row0
        V3 = c12*sp.sqrt(c13sq)*(r*e)*sp.sqrt(ser(row1[0]))
        bg, sc = yt2-yc2, yt2
    elif anchor == 'c':
        um = row1
        V3 = c12*sp.sqrt(c13sq)*sp.sqrt(ser(row1[0]))*e*sp.sqrt(c13sq)
        bg, sc = yt2-yu2, yt2
    else:
        um = row1  # t uses kp=2 -> row2? placeholder fixed below
        raise SystemExit('t handled separately')
    v2, w2 = invert(um)
    Dd = (lam[2]-lam[1])*(lam[2]-lam[0])*(lam[1]-lam[0])
    return ser(bg*Dd*V3/(sc*v2*sp.sqrt(w2)))

for a in ('u', 'c'):
    print("computing F_%s ..." % a, flush=True)
    F = F_anchor(a)
    F0 = sp.simplify(F.subs(e, 0))
    F2 = sp.simplify(sp.expand(F).coeff(e, 2))
    F1 = sp.simplify(sp.expand(F).coeff(e, 1))
    print("F_%s eps^0 = %s" % (a, F0))
    print("F_%s eps^1 = %s" % (a, F1))
    print("F_%s eps^2 = %s" % (a, F2))
    mass = {'u': 1-yc2/yt2, 'c': 1-yu2/yt2}[a]
    print("  normalized eps^0 / mass factor =", sp.simplify(F0/mass))
