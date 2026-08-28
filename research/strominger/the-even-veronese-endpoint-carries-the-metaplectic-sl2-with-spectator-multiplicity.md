# The Even-Veronese Endpoint Carries the Metaplectic sl2 with Spectator Multiplicity

## Source question

Grothendieck's theta control algebra has generators

\[
E=\frac{Q^2}{2},
\qquad
F=-\frac{P^2}{2},
\qquad
H=\frac{QP+PQ}{2},
\]

with fixed Casimir \(-3/4\). The Cartan endpoint has the same classical
Veronese conic. The question is whether it also carries the same operator
algebra, rather than only the same quadratic equation.

## Spinor realization

The Cartan algebra is the even binary-form algebra

\[
\mathcal C
\cong
\mathbb C[u,v]_{\mathrm{even}}
=
\bigoplus_{l\geq0}\operatorname{Sym}^{2l}\mathbb C^2.
\]

Choose a spinor coordinate \(u\). On \(\mathcal C\), define

\[
E=\frac{u^2}{2},
\qquad
F=-\frac{\partial_u^2}{2},
\qquad
H=u\partial_u+\frac12.
\]

These operators preserve even total parity. The operators \(E\) and \(F\)
raise and lower Cartan grade by one, while \(H\) preserves grade.

## Exact commutators

On a monomial \(u^nv^r\), direct calculation gives

\[
[H,E]=2E,
\qquad
[H,F]=-2F,
\qquad
[E,F]=H.
\]

The Casimir in Grothendieck's ordering is

\[
H^2+2H+4FE=-\frac34I.
\]

The identity holds for every \(n\) and every spectator exponent \(r\).
Therefore the Strominger endpoint realizes the same metaplectic
\(\mathfrak{sl}_2\) algebra and the same fixed Casimir, not merely the same
classical conic.

## Multiplicity distinction

The realization is not a literal identification of source systems. The
operator triple acts only in the chosen \(u\)-direction and leaves the exponent
of \(v\) fixed. Hence

\[
\mathcal C
=
\bigoplus_{r\geq0}v^r\mathbb C[u]_{n+r\;\mathrm{even}}
\]

is a direct sum of metaplectic parity sectors with spectator multiplicity.
Grothendieck's native theta oscillator is one such direction, whereas the
Cartan endpoint retains the full binary-spinor family.

Changing the chosen spinor coordinate conjugates the construction by the
spinor symmetry. No preferred \(u\) is supplied by the invariant conic alone;
a source-labelled axis is required to select one metaplectic subalgebra.

## Relation to normalized endpoint shifts

Multiplication by \(u^2\) is one Cartan grade-raising direction. The normalized
spin-weighted endpoint shift differs from raw polynomial multiplication by a
nonzero grade scalar. Entry 3639 shows that this scalar sequence is removable
in the bare algebraic chain. Thus the normalized endpoint module is
algebraically conjugate to the displayed metaplectic realization.

The dagger enhancement fixes a particular normalization and should not be
identified with the Bargmann adjoint convention without an explicit norm
comparison.

## Classical and quantum relations

The three quadratic classical symbols satisfy the Veronese relation after a
linear coordinate change. Operator ordering replaces the zero classical
quadratic by the central Casimir value \(-3/4\). The nonzero constant is not a
failure of the conic; it is the quantized correction carried by the chosen
metaplectic representation.

## Scope

This is an exact algebraic representation theorem. It does not identify the
theta source, seam currents, or completion data with the celestial endpoint.
It supplies a comparison of operator algebras together with a typed difference
in multiplicity and source-axis selection.

## Evidence replay

The checker verifies all three commutators, the fixed Casimir, parity
preservation, grade shifts, spectator invariance, and independence of the
Casimir from spectator multiplicity on monomials through total degree eighty.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/endpoint_metaplectic_sl2_checks.py
```

Machine-readable results are written to
`research/strominger/results/endpoint_metaplectic_sl2_checks.json`.

