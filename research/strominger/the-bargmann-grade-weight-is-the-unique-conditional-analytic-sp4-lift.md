# The Bargmann Grade Weight Is the Unique Conditional Analytic sp4 Lift

## Completion family

On

\[
\mathcal C=\mathbb C[u,v]_{\mathrm{even}},
\]

give monomials the Bargmann norm

\[
\lVert u^nv^r\rVert_B^2=n!r!.
\]

This norm is rotationally invariant on every fixed total degree. Every other
rotationally invariant grade-diagonal norm has the form

\[
\langle f,g\rangle_w
=
w_l\langle f,g\rangle_B,
\qquad
f,g\in H_l,
\]

for a positive sequence \((w_l)\).

## Adjoint recurrence

Let

\[
E_{ij}=\frac12x_ix_j
\]

map grade \(l\) to grade \(l+1\). With the weighted norm,

\[
E_{ij}^{\dagger_w}
=
\frac{w_{l+1}}{w_l}
\frac12\partial_i\partial_j.
\]

The fixed algebraic lowering generator is

\[
F_{ij}=-\frac12\partial_i\partial_j.
\]

Therefore

\[
F_{ij}=-E_{ij}^{\dagger_w}
\quad\Longleftrightarrow\quad
w_{l+1}=w_l
\]

for every grade. The compatible weight sequence is constant and hence unique
up to one global positive scalar.

## Conditional analytic lift

With constant grade weights, the Hilbert completion is the even
Bargmann-Fock space. The polynomial subspace is a common invariant dense core
for all ten quadratic generators. Multiplication and differentiation are
mutual adjoints with the required signs, so every real-form generator is
closable.

Finite-particle vectors are analytic for the quadratic generators. For
example, repeated application of \(E_{uu}=u^2/2\) to the vacuum gives

\[
\frac{\lVert E_{uu}^k1\rVert}{k!}
=
\frac{\sqrt{(2k)!}}{2^kk!},
\]

whose consecutive ratio tends to one. Its analytic-vector series therefore
has positive radius. The same estimate applies after any fixed finite initial
degree.

The standard analytic-vector theorem then integrates the quadratic Lie algebra
to the even metaplectic representation, provided the source authorizes this
completion and real form.

## Uniqueness theorem

Among rotationally invariant grade-diagonal Hilbert completions of the Cartan
endpoint, the Bargmann-Fock completion is the unique one, up to global norm
scale, for which the fixed algebraic raising and lowering operators satisfy

\[
F_{ij}=-E_{ij}^{\dagger}
\]

simultaneously at every grade.

Thus the missing analytic constructor has no hidden functional modulus. It is
a binary authority choice: either admit the Bargmann cross-grade weighting and
its common domain, or do not claim executable metaplectic control.

## Relation to the bounded endpoint completion

The bounded Toeplitz-Cartan completion uses grade-normalized shifts. The
Bargmann completion uses unbounded raw creation operators. Although their
algebraic cores are related by grade rescaling, that rescaling is unbounded and
does not identify the completed operator systems.

The two completions answer different questions:

- Toeplitz completion controls bounded observation and spectral commutators;
- Bargmann completion controls unbounded metaplectic exponentiation.

Neither completion may inherit the other's authority by transport.

## Minimal source declaration

The remaining source declaration is

```text
BargmannMetaplecticLift
  grade_weights: constant relative to Bargmann factorial norms
  dense_core: even polynomials
  real_form: declared
  adjoint_rule: F_ij = -E_ij dagger
  mixed_generator_domains: common and invariant
  exponentiation_scope: declared
  relation_to_bounded_endpoint_ports: comparison map or none
```

Without this declaration, the analytic lift remains a unique candidate rather
than an executable endpoint capability.

## Evidence replay

The checker verifies the factorial adjoint identity, the weight recurrence,
uniqueness up to global scale, common-core invariance, analytic-vector ratios,
and inequivalence with uniformly bounded shifts through degree two hundred.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/bargmann_metaplectic_lift_uniqueness_checks.py
```

Machine-readable results are written to
`research/strominger/results/bargmann_metaplectic_lift_uniqueness_checks.json`.

