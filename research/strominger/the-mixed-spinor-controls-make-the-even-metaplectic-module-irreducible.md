# The Mixed Spinor Controls Make the Even Metaplectic Module Irreducible

## Commuting-pair layer

On

\[
\mathcal C=\mathbb C[u,v]_{\mathrm{even}},
\]

the two coordinatewise oscillator triples

\[
(E_u,F_u,H_u)
\qquad\text{and}\qquad
(E_v,F_v,H_v)
\]

commute. Each has Casimir \(-3/4\). Relative to this
\(\mathfrak{sl}_2\oplus\mathfrak{sl}_2\) subalgebra,

\[
\mathcal C
=
(M_u^{\mathrm{even}}\otimes M_v^{\mathrm{even}})
\oplus
(M_u^{\mathrm{odd}}\otimes M_v^{\mathrm{odd}}).
\]

These are the only parity sectors compatible with even total degree.

## Mixed controls

The remaining quadratic-Weyl generators are

\[
E_{uv}=\frac12uv,
\qquad
F_{uv}=-\frac12\partial_u\partial_v,
\qquad
H_{uv}=u\partial_v,
\qquad
H_{vu}=v\partial_u.
\]

The mixed raising and lowering operators switch even-even and odd-odd parity.
The mixed degree-preserving operators exchange spinor occupation. Therefore the
two summands are not invariant under the complete \(\mathfrak{sp}_4\) algebra.

## Irreducibility theorem

The even polynomial module is irreducible under the quadratic metaplectic
\(\mathfrak{sp}_4\) action.

To prove this, let \(W\) be a nonzero invariant algebraic submodule. The trace
Cartan operator separates total degrees, so a polynomial in that operator
isolates a nonzero homogeneous component of any element of \(W\). Products of
the lowering operators \(F_{uu},F_{uv},F_{vv}\) send some nonzero monomial
coefficient of that component to a nonzero constant. Hence \(1\in W\).

Products of \(E_{uu},E_{uv},E_{vv}\) generate every even monomial from the
vacuum. Thus \(W=\mathcal C\).

The spectator decomposition is consequently real for a chosen commuting pair
but disappears under full axis-comparison closure.

## The spectral operator is internal

The diagonal oscillator generators are

\[
H_u=u\partial_u+\frac12,
\qquad
H_v=v\partial_v+\frac12.
\]

On total degree \(2l\), their sum is \(2l+1\). The spectral operator from the
dagger curvature therefore satisfies

\[
D
=
\frac{H_u+H_v+I}{4}.
\]

Indeed, the right side has eigenvalue \((l+1)/2\) on \(H_l\). The operator
\(D\) is an affine Cartan element of the metaplectic closure, not an externally
adjoined grade counter.

Its commutators are forced by the three-part grading:

\[
[D,E_{ij}]=\frac12E_{ij},
\qquad
[D,H_{ij}]=0,
\qquad
[D,F_{ij}]=-rac12F_{ij}.
\]

## Structural hierarchy

The endpoint control hierarchy is now exact:

```text
one selected axis
  -> one vertical metaplectic sl2 with spectator multiplicity
two coordinate axes
  -> commuting sl2 plus sl2 and two parity sectors
mixed axis comparison
  -> four connecting controls
all quadratic controls
  -> irreducible metaplectic sp4 module
```

This hierarchy explains why the spectator is visible in one presentation but
not invariant under the complete source-axis family.

## Scope

Irreducibility is algebraic for finite polynomials. Analytic irreducibility of
a chosen completed representation requires the corresponding closed-operator
domains and exponentiation data. No theta seam identification follows from the
common algebra alone.

## Evidence replay

The checker verifies the commuting pair, both Casimirs, parity decomposition,
mixed-sector switching, vacuum cyclicity, lowering reachability, the affine
Cartan formula for \(D\), and the induced three-part commutator grading through
total degree forty.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/endpoint_sp4_irreducibility_and_internal_grade_checks.py
```

Machine-readable results are written to
`research/strominger/results/endpoint_sp4_irreducibility_and_internal_grade_checks.json`.

