# Cylinder-algebra intertwiner no-go

## Question

Can a nonzero bounded bulk--corona channel survive by intertwining only finite-conductor cylinder multiplication rather than the full measurable multiplication algebra?

## Claim boundary

No, if it intertwines the union of all finite-conductor cylinder multipliers. That union generates the full multiplication von Neumann algebra, so boundedness extends the intertwining relation to the strong closure; mutual singularity then forces the channel to vanish. This does not exclude an unbounded closable channel or a channel for a genuinely smaller nonseparating algebra.

## Setup

Let

\[
\pi_+:\mathcal A_{\rm cyl}\to B(L^2(\mu_+)),
\qquad
\pi_\times:\mathcal A_{\rm cyl}\to B(L^2(\mu_\times))
\]

be multiplication representations of the finite-coordinate cylinder algebra on the profinite conductor space. Suppose bounded \(C\) satisfies

\[
C\pi_+(a)=\pi_\times(a)C
\]

for every cylinder function \(a\).

## Strong-closure step

Cylinder functions generate the Borel sigma algebra. Their bounded multiplication operators are strongly dense in the generated multiplication von Neumann algebra. If bounded multipliers \(a_i\) converge strongly to \(a\), boundedness of \(C\) gives

\[
C\pi_+(a_i)f
\longrightarrow
C\pi_+(a)f
\]

and

\[
\pi_\times(a_i)Cf
\longrightarrow
\pi_\times(a)Cf.
\]

Thus the intertwining identity extends to every bounded measurable multiplier.

## Singular-support test

Mutual singularity supplies a measurable set \(A\) with

\[
\mu_+(A)=1,
\qquad
\mu_\times(A)=0.
\]

Hence

\[
\pi_+(\mathbf1_A)=I,
\qquad
\pi_\times(\mathbf1_A)=0.
\]

The extended intertwining identity yields

\[
C
=
C\pi_+(\mathbf1_A)
=
\pi_\times(\mathbf1_A)C
=0.
\]

## Consequence for the coherencer search

Replacing the full multiplication algebra by all finite-conductor observables does not evade the no-go. Although no single finite stage contains the singular support projection, the directed union recovers it in strong closure.

A surviving channel must violate at least one premise:

1. it is unbounded but closable, with an invariant common core;
2. it intertwines only a smaller algebra that does not strongly generate the support projection;
3. it satisfies a commutator relation rather than exact intertwining;
4. it is a correspondence or quadratic-form coupling rather than an operator;
5. its refinement residual is nonzero but controlled by higher coherence data.

The order--Mellin algebra is eligible only if its exact generated closure and differentiable domain are specified. Calling it smaller is insufficient; it must be shown not to reconstruct the separating projection.

## Disposition

The bounded all-cylinder intertwiner branch is closed. The next source question is to identify the smallest arithmetic algebra actually required by the explicit formula and compute whether its two representations are disjoint. If they are disjoint, only an unbounded/form-valued coherencer remains possible.

## Verification

- `research/voevodsky/checkers/check_cylinder_algebra_intertwiner.py`
- `research/voevodsky/results/cylinder_algebra_intertwiner.json`
