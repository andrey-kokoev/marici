# The Opposite-Weighted Completion Selects a Two-Quadrature Antipode Test, Not Full Modulus Dominance

The source-faithful weighted completion produces

\[
X(a+it)=2C_a(t)+2iS_a(t),
\]

with

\[
C_a(t)=\int f(q)\cosh(aq)\cos(tq)\,dq
\]

and

\[
S_a(t)=\int f(q)\sinh(aq)\sin(tq)\,dq.
\]

Therefore RH requires only that `C_a` and `S_a` have no common zero for
nonzero `a`. Equivalently, the projective ratio of the two weighted sheet
amplitudes must avoid the single antipode `-1`.

Strict modulus dominance forbids the entire unit circle and is sufficient but
stronger than RH. On the seam, `S_0` vanishes identically; off the seam it
becomes the second meaningful comparison channel. RH says the two channels
never vanish together there.

Research packet:
`research/grothendieck/the-opposite-weighted-completion-selects-a-two-quadrature-antipode-test-not-full-modulus-dominance.md`

Checker:
`research/grothendieck/checkers/check_two_quadrature_antipode_scope.py`

The checker passes 5/5 gates.
