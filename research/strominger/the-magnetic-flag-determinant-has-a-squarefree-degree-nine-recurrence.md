# The magnetic flag determinant has a squarefree degree-nine recurrence

## Discovery result

Let

[
mu_n=det(overline{Delta}_n)
]

be the scalar determinant of the flag-adapted map from the three-dimensional
domain quotient to the fixed image hyperplane. Modular Berlekamp--Massey was
run over the three good auxiliary primes

[
1000003,qquad1000033,qquad1000037.
]

For each prime:

- 220 terms were generated directly from modular constructor matrices;
- the first 150 terms determined the recurrence;
- all 70 disjoint held-out terms satisfied it;
- the minimal degree was 9;
- the minimal characteristic polynomial was exactly the same
  source-derived squarefree envelope.

Put

[
L=147458,qquad
s_0=2,quad s_1=L,quad s_{j+1}=Ls_j-s_{j-1}.
]

The discovered polynomial is

[
Q_{min}(E)
=
(E-1)prod_{j=1}^{4}(E^2-s_jE+1).
]

The degree-49 proposal is falsified because the (j=4) factor is present.
The earlier degree-63 polynomial was a valid annihilator but carried seven
unnecessary copies of every spectral factor.

## Exact integer lift

The source-derived integer polynomial was then evaluated against exact
determinant scalars at grades (0) through (70). All 62 available recurrence
residuals vanish exactly. The order-nine Hankel determinant from the first
17 scalar values is nonzero and has 783 decimal digits. Hence no rational
recurrence of degree at most eight fits this integer sequence.

This finite computation also closes the unbounded obligation. The independently
derived source envelope (Q_{63}) annihilates the complete sequence, and
(Q_9) divides (Q_{63}). Therefore the residual sequence

[
r_n=Q_9(E)mu_n
]

is annihilated by the quotient polynomial (Q_{63}/Q_9), whose degree is 54.
Any sequence governed by an order-54 recurrence is determined by 54 consecutive
values. Here 62 consecutive exact residuals vanish, so (r_n=0) for every grade.
Thus (Q_9) is an unbounded annihilator, while the nonzero order-nine Hankel
minor proves that it is minimal over (mathbf Q).

## Meaning

All modes

[
1,quadlambda^{pm n},quadlambda^{pm2n},
quadlambda^{pm3n},quadlambda^{pm4n}
]

survive, and each occurs with multiplicity one. Every polynomial-in-grade
contribution from the size-two Jordan block at eigenvalue one cancels in the
flag determinant.

Thus the scalar has the form

[
mu_n
=
c_0+sum_{j=1}^{4}
(c_jlambda^{jn}+c_{-j}lambda^{-jn}),
]

with no factors of (n).

The order-nine recurrence is therefore a theorem once the source-derived
degree-63 envelope is admitted. The quotient-annihilator argument proves that
all excess Jordan multiplicities disappear globally; the Hankel witness proves
that none of the nine squarefree spectral modes can be removed.

## Replay

`python research/strominger/checkers/flag_scalar_modular_recurrence_checks.py`

`python research/strominger/checkers/flag_scalar_exact_recurrence_checks.py`
