# The Endpoint Dagger Tower Defines a Toeplitz-Cartan Spectral Triple

## Construction

Let

\[
\mathscr H=\bigoplus_{l\geq0}H_l
\]

carry the source-authorized harmonic inner products. The curvature defect from
the dagger round trip is

\[
\Delta|_{H_l}=\frac{2}{l+1}I_{H_l}.
\]

Define the unbounded positive self-adjoint operator

\[
D=\Delta^{-1},
\qquad
D|_{H_l}=\frac{l+1}{2}I_{H_l}.
\]

For \(a\in H_1\), let

\[
S_a:H_l\longrightarrow H_{l+1}
\]

be normalized Cartan multiplication by \(a\). Let \(\mathcal A_C\) be the
unital star algebra generated on \(\mathscr H\) by the operators \(S_a\) and
their Hilbert adjoints.

## Bounded generators

Cartan multiplication is a slice of the normalized orthogonal projection

\[
C_l:H_1\otimes H_l\longrightarrow H_{l+1}.
\]

Therefore

\[
\lVert S_a\rVert\leq\lVert a\rVert
\]

uniformly in grade. Each generator and adjoint defines a bounded operator on
the Hilbert direct sum.

## Bounded commutators

Since \(S_a\) raises grade by one,

\[
[D,S_a]|_{H_l}
=
\left(\frac{l+2}{2}-\frac{l+1}{2}\right)S_a
=
\frac12S_a.
\]

Similarly,

\[
[D,S_a^\dagger]=-rac12S_a^\dagger.
\]

The Leibniz rule then shows that \([D,A]\) is bounded for every
\(A\in\mathcal A_C\).

## Compact resolvent and summability

The eigenvalue \((l+1)/2\) of \(D\) has multiplicity \(2l+1\). Hence the
resolvent of \(D\) is compact and

\[
\operatorname{tr}(D^{-s})
=
\sum_{l\geq0}(2l+1)
\left(\frac{2}{l+1}\right)^s.
\]

Writing \(n=l+1\) gives the exact spectral zeta function

\[
\zeta_D(s)
=
2^s\left(2\zeta(s-1)-\zeta(s)\right).
\]

It converges for \(\operatorname{Re}s>2\). Thus the triple is finitely
summable for every exponent greater than two and has metric dimension two.
Its meromorphic continuation has simple candidate dimension-spectrum poles at
\(s=2\) and \(s=1\).

## Theorem

The packet

\[
(\mathcal A_C,\mathscr H,D)
\]

is an odd spectral triple in the minimal analytic sense:

- \(\mathcal A_C\) is represented by bounded operators;
- \(D\) is self-adjoint with compact resolvent;
- commutators \([D,A]\) are bounded for all \(A\in\mathcal A_C\).

The construction is source-derived from the Cartan multiplication and the
authorized dagger curvature. No grade counter is added independently.

## What this does not yet prove

This is not yet a commutative spectral reconstruction of the celestial sphere.
The algebra \(\mathcal A_C\) contains raising shifts and their adjoints and is
Toeplitz-like. Further work would be required to identify its quotient or
symbol algebra with functions on the celestial conic.

It is also not yet a Dirac spectral triple in the geometric sense. The current
packet does not supply:

- a Clifford action;
- a real structure;
- an orienting Hochschild cycle;
- a first-order condition relative to an opposite algebra;
- Poincare duality.

Those are explicit next gates rather than consequences of spectral dimension
alone.

## Hostile boundary

If the grade eigenvalues grow faster than linearly, commutators with the
raising shifts become unbounded. If they grow sublinearly, the spectral
dimension changes. Linear reciprocal curvature is exactly what makes bounded
first differences coexist with dimension two.

## Evidence replay

The checker verifies bounded grade differences, exact finite spectral sums,
the zeta decomposition, compact-resolvent multiplicities, and the summability
threshold through grade two hundred.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/endpoint_toeplitz_cartan_spectral_triple_checks.py
```

Machine-readable results are written to
`research/strominger/results/endpoint_toeplitz_cartan_spectral_triple_checks.json`.

