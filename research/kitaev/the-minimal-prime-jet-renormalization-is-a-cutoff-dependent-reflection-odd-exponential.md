# The minimal prime-jet renormalization is a cutoff-dependent reflection-odd exponential

## Question

What is the minimal reflection-compatible counterterm that cancels the
divergent central first jet of the finite-prime Fourier–Tate transition?

## Divergent connection coefficient

Let

\[
c_X=
\frac{\gamma_X'}{\gamma_X}(1/2)
=
\sum_{p\le X}
\frac{2(\log p)p^{-1/2}}{1-p^{-1/2}}.
\]

Then

\[
c_X\longrightarrow+\infty.
\]

Every cutoff nevertheless satisfies

\[
\gamma_X(1/2)=1.
\]

## No fixed multiplier can repair the jet

Let (a(s)) be a fixed holomorphic nonzero archimedean or polar multiplier
regular at (s=1/2). Then

\[
\frac{(a\gamma_X)'}{a\gamma_X}(1/2)
=
\frac{a'}a(1/2)+c_X.
\]

The first term is cutoff-independent and finite, so the sum still diverges.

Therefore no fixed regular multiplier cancels the naive finite-prime jet
escape. Any successful completion must alter the cutoff transition itself or
introduce a cutoff-dependent normalization derived from the global source.

## Minimal first-order counterterm

Define

\[
\rho_X(s)
=
\exp\left[-c_X(s-1/2)\right].
\]

It obeys

\[
\rho_X(1-s)=\rho_X(s)^{-1},
\qquad
\rho_X(1/2)=1.
\]

For

\[
\Gamma_X=\rho_X\gamma_X,
\]

one has

\[
\Gamma_X(1/2)=1,
\qquad
\frac{\Gamma_X'}{\Gamma_X}(1/2)=0.
\]

This is the unique linear logarithmic correction at the fixed point.

## Odd-jet normal form

Write

\[
u=s-1/2.
\]

For any normalized nonzero counterterm satisfying reflection inversion,

\[
\rho_X(-u)=\rho_X(u)^{-1},
\qquad
\rho_X(0)=1.
\]

On a local logarithm branch,

\[
\log\rho_X(-u)=-\log\rho_X(u).
\]

Therefore its logarithm has only odd powers:

\[
\log\rho_X(u)
=
-c_Xu+d_{3,X}u^3+d_{5,X}u^5+\cdots.
\]

The divergent first-jet cancellation fixes the linear coefficient. Higher
freedom begins at cubic order and must be fixed by higher-jet completion laws,
not by first-order data.

This predicts an odd renormalization tower for every reflection-compatible
completed transition.

## Source-authority boundary

The exponential above proves algebraic sufficiency and identifies the
minimal coefficient. It does not authorize inserting that factor into the
theta/Tate source.

A valid counterterm must be derived from one of:

1. a completed Hadamard or determinant normalization;
2. the archimedean and polar source package together with its cutoff law;
3. a restricted-product renormalization functor;
4. a vacuum or tensor-unit frame transported coherently across cutoffs.

Choosing (ho_X) merely because it cancels (c_X) would be fitted
subtraction.

## Completion criterion

The renormalized transitions must satisfy more than the central first-jet
condition. They require:

- cutoff cocycle compatibility;
- convergence on compact off-seam sets;
- bounded action and inverse on the completed carrier;
- preservation of the finite valuation grades;
- compatibility with the Real structure;
- convergence of every jet order used by downstream constructors.

The first-order counterterm is necessary for a Clark-jet completion but not
sufficient for the completed operator lift.

## Relation to experimental reset

Aspect's unrestricted transition-memory hostile has the same authority
boundary. A fitted subtraction can always move signal into a transition
memory term. Only an independently certified reset or full transition
calibration identifies the logical effect.

Here (ho_X) is the algebraic subtraction. The analogue of the certified
reset is a source-derived global normalization that fixes (ho_X) before
observing the divergent jet.

## Falsifier certificate

    {
      "code": "prime_jet_counterterm_not_source_authorized",
      "required_linear_coefficient": "-c_X",
      "reflection_odd": true,
      "fixed_multiplier_sufficient": false,
      "higher_odd_coefficients_source_fixed": false,
      "completion_bounds_proved": false
    }

## Disposition

The minimal algebraic repair of the divergent finite-prime first jet is a
cutoff-dependent reflection-odd exponential with forced linear coefficient
(-c_X). A fixed archimedean factor cannot supply it. The remaining theorem
is source derivation and completion coherence of the full odd counterterm
tower.

## Claim boundary

This packet constructs and classifies the local first-order counterterm. It
does not claim that the proposed exponential is the canonical Tate
renormalization, nor that it converges or preserves the admitted arithmetic
constructor family.
