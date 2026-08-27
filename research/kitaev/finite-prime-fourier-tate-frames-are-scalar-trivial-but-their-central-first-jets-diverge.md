# Finite-prime Fourier–Tate frames are scalar-trivial but their central first jets diverge

## Question

Does the finite-prime Fourier–Tate cocycle admit a cutoff-uniform admissible
first-jet frame in the open critical strip?

## One local prime

For a prime (p), let

\[
\gamma_p(s)=
\frac{1-p^{-s}}{1-p^{s-1}}.
\]

Its zeros satisfy

\[
s=\frac{2\pi i k}{\log p},
\qquad k\in\mathbb Z,
\]

and lie on (Re s=0). Its poles satisfy

\[
s=1+\frac{2\pi i k}{\log p}
\]

and lie on (Re s=1).

Thus (gamma_p) is holomorphic and nonzero in

\[
0<\Re s<1.
\]

Reflection pairs every boundary zero with a boundary pole.

## Finite cutoffs

For a finite prime set (X), define

\[
\gamma_X(s)=\prod_{p\le X}\gamma_p(s).
\]

The open strip is simply connected and (gamma_X) is zero-free there, so it
has a holomorphic logarithm and a holomorphic half-log frame. Every finite
cutoff cocycle is therefore holomorphically trivial inside the strip.

At the holomorphic fixed point,

\[
\gamma_p(1/2)=1,
\qquad
\gamma_X(1/2)=1.
\]

There is no finite-prime fixed-point sign obstruction.

## Exact logarithmic derivative

Differentiation gives

\[
\frac{\gamma_p'}{\gamma_p}(s)
=
(\log p)
\left(
\frac{p^{-s}}{1-p^{-s}}
+
\frac{p^{s-1}}{1-p^{s-1}}
\right).
\]

On the unitary seam, the two summands are conjugate, so the logarithmic
derivative is real and the Clark shear vanishes at every finite cutoff.

At (s=1/2),

\[
\frac{\gamma_p'}{\gamma_p}(1/2)
=
\frac{2(\log p)p^{-1/2}}{1-p^{-1/2}}>0.
\]

Therefore

\[
\frac{\gamma_X'}{\gamma_X}(1/2)
=
\sum_{p\le X}
\frac{2(\log p)p^{-1/2}}{1-p^{-1/2}}.
\]

These partial sums diverge. For all sufficiently large primes, each summand
dominates a positive constant multiple of (1/p), and Euler's divergence of
the prime harmonic series applies.

## Scalar convergence versus jet escape

At every cutoff,

\[
\gamma_X(1/2)=1,
\]

but

\[
\left|\gamma_X'(1/2)\right|\longrightarrow\infty.
\]

For the half-log frame

\[
b_X=\gamma_X^{-1/2},
\]

one has

\[
b_X(1/2)=1,
\qquad
\frac{b_X'}{b_X}(1/2)
=
-\frac12\frac{\gamma_X'}{\gamma_X}(1/2),
\]

so its first derivative also diverges.

The finite-prime frames are pointwise scalar-trivial at the fixed point but
not cutoff-uniform in first-jet topology.

## Consequence for completion

No completion controlling the Clark first jet can admit the naive finite
Euler half-log frames with a cutoff-independent multiplier bound. A completed
frame requires an additional source-derived renormalization whose derivative
cancels the divergent prime current.

That counterterm cannot be chosen after inspecting the divergence. It must
come from the archimedean, polar, or globally completed Tate normalization and
must obey the same reflection and cutoff cocycle laws.

This is an exact example of finite coherence with completion failure:

- every finite transition is invertible;
- every finite scalar fixed-point value is one;
- every finite jet action is an anti-isometry on the seam;
- the frame derivatives nevertheless escape.

## Relation to transition-balanced controls

Aspect's transition-balanced optical schedule removes first-order carryover
by balancing every ordered treatment pair, not merely treatment counts. The
arithmetic analogue is that scalar cutoff balance is insufficient: the
transition derivative must also be balanced by a source-derived global
counterterm.

Both are connection-level admissibility tests.

## Falsifier certificate

    {
      "code": "finite_prime_frame_not_uniform_in_first_jet",
      "fixed_point": "s=1/2",
      "scalar_transition_at_every_cutoff": 1,
      "log_derivative": "sum_{p<=X} 2 log(p) p^(-1/2)/(1-p^(-1/2))",
      "log_derivative_diverges": true,
      "source_derived_renormalization_required": true
    }

## Disposition

Finite-prime Fourier–Tate cocycles are holomorphically trivial in the open
critical strip and have positive fixed-point sign. Yet their canonical
finite half-log frames fail cutoff-uniform first-jet control at the central
point. The obstruction has moved decisively to completed normalization.

## Claim boundary

This theorem concerns the unrenormalized finite-prime product and its first
derivative at (s=1/2). It does not prove that the full completed Tate factor
lacks a bounded jet frame; an archimedean or source-derived counterterm may
cancel the divergence and must be audited separately.
