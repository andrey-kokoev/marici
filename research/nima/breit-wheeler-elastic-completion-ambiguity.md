# Elastic completion is a phase problem after the Cut is fixed

Owner: `marici.Nima`

Status: retained as the inclusive-effect theorem.  The continuous phase is
removed in the exact one-loop problem once the complete oriented Cut and the
source-normalized boundary jet are supplied; see
`qed-oriented-cut-uniqueness.md`.

Let (K) denote the exposed pair-production branch, normalized so that

\[
K^\dagger K=E,qquad 0\le E\le I.
\]

Any elastic branch (S_{\rm el}) completing it to an isometry must satisfy

\[
S_{\rm el}^\dagger S_{\rm el}=I-E.
\]

Its polar form is therefore

\[
\boxed{
S_{\rm el}=U\sqrt{I-E},
}
\]

where (U) is a partial isometry, unitary when (I-E) is nonsingular.  The
Cut determines the positive factor and leaves the coherent phase (U)
undetermined.

## Symmetry does not remove the ambiguity

At the forward planar Breit--Wheeler sample, the Cut effect can be represented
as a real symmetric matrix.  For every real (\theta),

\[
U_\theta
=\exp\!\left(i\theta\frac{E}{\lambda_{\max}(E)}\right)
\]

commutes with (E), is unitary, and is symmetric.  Hence

\[
S_\theta=U_\theta\sqrt{I-E}
\]

obeys the same unitarity equation and the same planar reciprocity symmetry
for a continuous family of distinct phases.  Positivity, unitarity, and this
time-reversal gate do not select one completion.

## Analyticity narrows but does not automatically select

Knowing the absorptive Cut at all energies is analogous to knowing a boundary
modulus.  Analytic reconstruction still requires subtraction data,
asymptotics, and pole/zero information.  Multiplication by an allowed inner
or CDD factor preserves the physical-boundary modulus while changing the
phase.

Therefore the source-derived elastic completion has two logically separate
requirements:

1. a dispersion relation reconstructing the outer part from the Cut;
2. source conditions fixing subtraction constants and excluding or
   classifying inner/CDD factors.

Crossing is vector-valued in the helicity system, so this audit must be
performed on the full crossing representation rather than independently on
three scalar helicity functions.

## Sharp next test

Use the exact one-loop light-by-light amplitude as a hostile control:

1. reconstruct its real part from the established electron Cut with the
   declared vector-valued crossing map;
2. compute the smallest subtraction polynomial allowed by gauge invariance,
   crossing, and low-energy softness;
3. divide the exact amplitude by the reconstructed outer completion;
4. test whether the residual is the identity, a fixed source phase, or a
   nontrivial inner/CDD factor.

The outcomes have distinct meanings:

- identity: the Cut plus declared boundary conditions selects the instrument;
- fixed phase/polynomial: a finite source boundary packet is additionally
  required;
- nontrivial inner factor: absorptive data is intrinsically insufficient.

## Falsifiers

- Two completions with the same Cut and admitted symmetries cannot be
  constructed.
- The polar family changes the Cut effect.
- Scalar dispersion is applied before the helicity crossing representation is
  retained.
- A subtraction or CDD choice is called source-derived without independent
  source authority.
