# The Endpoint Has Two Weyl Pairs but sp4 Execution Needs an Unbounded Domain Constructor

## Independence-versus-polarization test

The spinor presentation uses two algebraically independent homogeneous
coordinates \(u,v\). Their differential operators satisfy

\[
[\partial_u,u]=1,
\qquad
[\partial_v,v]=1,
\qquad
[\partial_u,v]=[\partial_v,u]=0.
\]

The Weyl form therefore has rank four: there are two independent canonical
pairs

\[
(u,\partial_u)
\qquad\text{and}\qquad
(v,\partial_v).
\]

They are not two polarizations of one canonical pair. Spinor exchange
\(u\leftrightarrow v\) swaps the pairs, while Fourier reciprocity acts inside
one pair by exchanging multiplication and differentiation. These operations
have different variance.

## Projective typing

The projective conic is obtained from nonzero spinors by common scalar
identification. This removes the shared radial scale but does not impose a Weyl
relation identifying \(v\) with \(\partial_u\). The homogeneous coordinate
ring retains both variables and its complete grade tower.

Thus the four mixed quadratic generators are genuine algebraic operators on
the endpoint section ring. They are not justified by duplicating one
polarization.

This does not yet make all four mixed controls physically executable. The
projective quotient and the endpoint instrument contract must still authorize
their domains and readouts.

## Bounded-operator no-go

The Toeplitz-Cartan spectral triple uses bounded normalized shifts. The exact
metaplectic algebra uses raw quadratic creation and second differentiation.
These cannot be the same operator family on the completed Hilbert space.

Indeed, if both \(E\) and \(F\) were bounded, then their commutator would be
bounded. But the oscillator relation requires

\[
[E,F]=H,
\]

and \(H\) has eigenvalues \(n+1/2\), which are unbounded. Therefore every
nontrivial Hilbert realization of the exact oscillator algebra requires
unbounded generators.

In the Bargmann normalization, multiplication by \(u^2/2\) has coefficient

\[
\frac12\sqrt{(n+1)(n+2)}
\]

on the normalized degree-\(n\) monomial. It grows linearly. By contrast, the
normalized Cartan shifts are contractions. Their algebraic conjugacy uses an
unbounded grade rescaling and is not a bounded or unitary equivalence of the
completed representations.

## Missing constructor

To promote the algebraic \(\mathfrak{sp}_4\) action to executable analytic
control, the source must supply:

```text
UnboundedMetaplecticDomain
  common_dense_core
  graph_norms_for_all_ten_generators
  adjoint_relations
  essential_self_adjointness_or_closability
  invariant_domain_under_mixed_controls
  exponentiation_authority
  projective_or_gauge_compatibility
```

The polynomial ring is a common algebraic core, but a core alone does not
authorize exponentiation or physical execution.

## Consequence for the two preceding theorems

Two structures coexist without contradiction:

- the bounded Toeplitz-Cartan spectral triple, whose shifts are admissible
  observables with bounded commutators;
- the unbounded algebraic metaplectic \(\mathfrak{sp}_4\), whose generators
  encode exact oscillator control on a common polynomial core.

Passing from the first to the second is a domain-bearing completion step, not
a change of notation.

## Theta comparison

The endpoint passes Grothendieck's algebraic independence gate: its two spinor
coordinates yield two independent Weyl pairs and a legitimate four-dimensional
mixed complement. Whether theta plus/minus sectors supply the same independence
is a separate source question. A comparison map cannot be inferred from the
common \(\mathfrak{sp}_4\) presentation.

## Evidence replay

The checker verifies rank-four canonical commutators, the distinction between
pair exchange and Fourier reflection, unbounded oscillator coefficients,
bounded normalized Cartan coefficients, and the bounded-commutator no-go
through degree two hundred.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/endpoint_weyl_independence_and_unbounded_sp4_checks.py
```

Machine-readable results are written to
`research/strominger/results/endpoint_weyl_independence_and_unbounded_sp4_checks.json`.

