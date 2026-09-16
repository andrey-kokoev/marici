# The phase-increment contraction cannot be pointwise and must use nonlocal modular sewing

## Candidate local factorization

The first Laguerre identity reduces positivity to

\[
\|r_-(x)\|^2+
\|r_+(x)\|^2
\le
4M_0M_2,
\]

with

\[
r_-(u,v;x)=
\frac{u-v}{\sqrt2}
\sqrt{f(u)f(v)}
[1-e^{ix(u+v)}],
\]

\[
r_+(u,v;x)=
\frac{u+v}{\sqrt2}
\sqrt{f(u)f(v)}
[1-e^{ix(u-v)}].
\]

A first attempt would realize these features by a pointwise multiplier or fiberwise partial isometry acting on a bulk feature with density

\[
2(u^2+v^2)f(u)f(v).
\]

## Exact hostile fiber

Take

\[
xu=\pi,
\qquad
xv=0.
\]

Both phase increments then have squared modulus four. After removing the common factor \(\pi^2/x^2\),

\[
|r_-|^2=2,
\qquad
|r_+|^2=2.
\]

The combined residual density is therefore

\[
4.
\]

The available invariant bulk density is only

\[
2(u^2+v^2)=2.
\]

Hence the pointwise norm ratio is

\[
2>1.
\]

No fiberwise contraction exists.

## Durable check

Checker:

`research/voevodsky/checkers/check_phase_increment_pointwise_contraction_no_go.py`

Result:

`research/voevodsky/results/phase-increment-pointwise-contraction-no-go.json`

The fixture is exact and uses rational arithmetic after removing a common positive scale.

## Consequence

Any successful factorization

\[
(r_-,r_+)=P_xU_xb
\]

must mix different source fibers. It cannot be a pointwise phase multiplier, a local projection, or a direct integral of fiberwise partial isometries.

The required operator must use a nonlocal relation special to the completed theta source. The prior tail-flow packets already provide the relevant candidate architecture:

\[
I_z=rac{\Phi+G_z}{\sqrt2},
\qquad
O_z=rac{\Phi-G_z}{\sqrt2}.
\]

Their exact polarization identity is

\[
\langle I_w,I_z\rangle-
\langle O_w,O_z\rangle
=
\langle\Phi,G_z\rangle+
\langle G_w,\Phi\rangle.
\]

Combined with the tail Green identity, this produces a one-sided lurking isometry on the full tail feature. It does not collapse to a pointwise operation on \((u,v)\).

## Remaining gate

The one-sided isometry is already source-derived. The unresolved step is reciprocal sewing:

1. form the two incoming sum ports from the positive and negative sheets;
2. form the two outgoing endpoint-plus-difference ports;
3. apply the Tate/Fourier reciprocal sewing map to the complete ports;
4. prove equality of their Gram operators on the common rigged domain.

Finite-dimensional Fourier packets satisfy this full Gram equality. The infinite obstruction is domain typing: the connected tail is Hilbert, while primitive and endpoint currents can be distributional.

## Disposition

The requested partial-isometry construction has been narrowed decisively:

\[
\text{local phase partial isometry fails},
\]

while

\[
\text{nonlocal tail-flow lurking isometry remains admissible}.
\]

The next exact calculation should act on the complete reciprocal tail ports, not on individual two-copy phase fibers.
