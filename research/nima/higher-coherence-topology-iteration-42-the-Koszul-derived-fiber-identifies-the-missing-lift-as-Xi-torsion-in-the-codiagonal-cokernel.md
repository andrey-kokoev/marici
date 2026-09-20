# Higher-coherence topology iteration 42: the Koszul derived fiber identifies the missing lift as Xi-torsion in the codiagonal cokernel

## Candidate topology

Work in the local analytic ring

\[
O=\mathcal O_{U,z_0}
\]

at a zero `z_0` of `tau`. Let

\[
C:K\hookrightarrow H
\]

be the labelled Köthe incidence into the common-history germ module and put

\[
Q=\operatorname{coker}C.
\]

Instead of the ordinary divisor fiber, use the derived fiber computed by the
Koszul complex

\[
[O\xrightarrow{\tau}O].
\]

## Exact specialization obstruction

Tensoring

\[
0\to K\xrightarrow C H\to Q\to0
\]

with `O/(tau)` gives

\[
0\to
\operatorname{Tor}_1^O(Q,O/(\tau))
\to K/\tau K
\xrightarrow{\bar C}
H/\tau H.
\]

For a principal divisor,

\[
\operatorname{Tor}_1^O(Q,O/(\tau))
\cong
\{q\in Q:\tau q=0\}.
\]

Thus the failure of labelled incidence to remain injective at a Xi zero is
exactly `tau`-torsion in its cokernel.

## Apply the bordered identity

The known identity has the form

\[
C(R)=\tau H_{\rm border}.
\]

Let `[H_border]` denote the class of `H_border` in `Q`. Then

\[
\tau[H_{\rm border}]=0.
\]

Therefore the bordered comparison itself produces the candidate torsion class.
Its connecting image in `K/tau K` is precisely the specialized labelled
residual `[R]`.

This sharpens the earlier nonimplication: scalar Xi-divisibility may be evidence
of a nonzero derived specialization class rather than evidence that the
labelled residual vanishes.

## Exact criterion for success

Because `C` is injective on the projective source range, confinement follows if
one proves that `H_border` lifts through `C`:

\[
H_{\rm border}=C(S).
\]

Indeed,

\[
C(R-\tau S)=0
\]

then implies

\[
R=\tau S,
\]

so `R(z_0)=0` coordinatewise. Equivalently, it suffices to prove that `Q` has no
`tau`-torsion in the bordered source sector.

## Multiplicity

If `tau` has multiplicity `m` at `z_0`, write `tau=u^m v` with `v` a unit. The
derived fiber detects `u^m`-torsion and its filtration records the successive
multiplicity jets. The same lift criterion must hold through all `m` layers;
ordinary point evaluation sees only the bottom layer.

## Role of higher cones

An infinite simplex--prism--cone tower could now have a precise purpose: build
a projective resolution of `Q` and contract its `tau`-torsion. But adding a
formal free cell merely resolves the class; it does not prove the torsion class
zero. A source-derived lift of `H_border`, with all prime and Green
compatibilities, is still required.

## Verdict for topology 42

Derived Koszul topology does not erase the residual, but computes the exact
obstruction:

\[
[R]
\leftrightarrow
[H_{\rm border}]
\in Q[\tau].
\]

The next concrete gate is no longer vague codiagonal faithfulness. It is to
construct a labelled Köthe preimage of `H_border` or prove the relevant
cokernel is `tau`-torsion-free.

The next nonredundant topology to test is an `I`-adic/formal-neighborhood
topology along the Xi divisor, asking whether compatibility over every
`tau^n` thickening forces this torsion class to disappear.