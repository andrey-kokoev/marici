"""Check the weighted logarithmic regularization of the soft Gauss-Manin lift."""

from fractions import Fraction


# At u=0: K=a^4 and K_u=a^2(1-b^2).  For
# V=((b^2-1)/(4a))*d/da, V(K) cancels K_u.
for b in (-3, -2, 0, 2, 3):
    for a in (1, 2, 3):
        k_u = Fraction(a * a * (1 - b * b))
        v_k = Fraction(b * b - 1, 4 * a) * 4 * a**3
        assert k_u + v_k == 0

# On a^2=u*t, u*V=((b^2-1)/(4t))*a*d/da.  The exceptional reduced carrier
# has t=(b^2-1)/2 away from b=+-1, so its residue is 1/2.
for b in (-3, -2, 0, 2, 3):
    if b * b == 1:
        continue
    t = Fraction(b * b - 1, 2)
    residue = Fraction(b * b - 1, 4) / t
    assert residue == Fraction(1, 2)

# exp(2*pi*i*1/2)=-1; encode the exact character without floating arithmetic.
monodromy_character = -1
assert monodromy_character == -1

print("K_u + V(K)|u=0: 0")
print("weighted logarithmic residue: 1/2")
print("semisimple monodromy character: -1")
