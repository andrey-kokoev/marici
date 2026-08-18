"""Audit local q-homotopy lifts of the invariant endpoint conormal jet."""

from fractions import Fraction as Q

# Evaluate the rational identities away from their excluded endpoints.
for b in (Q(-3), Q(0), Q(2)):
    a = Q(5)
    if b != -1:
        f_plus = a / (12 * (b + 1))
        m_plus = f_plus * (b + 1) * a
        assert -Q(3, 2) * m_plus == -a * a / 8
    if b != 1:
        f_minus = a / (12 * (1 - b))
        m_minus = f_minus * (1 - b) * a
        assert -Q(3, 2) * m_minus == -a * a / 8

# A polynomial f cannot solve f*(b+1)*a=a^2/12: after cancelling a it
# would be a/[12(b+1)].  The conjugate chart similarly needs 1/(1-b).
# Their overlap difference has a pole along c=1-b^2.
for b in (Q(-3), Q(0), Q(2)):
    if b not in (-1, 1):
        a = Q(5)
        difference = a / (12 * (b + 1)) - a / (12 * (1 - b))
        assert difference == -a * b / (6 * (1 - b * b))

print("U_- lift coefficient: a/[12(b+1)]")
print("U_+ lift coefficient: a/[12(1-b)]")
print("overlap difference: -ab/[6(1-b^2)]")
print("verdict: the endpoint conormal jet has local but no global polynomial orbit lift")
