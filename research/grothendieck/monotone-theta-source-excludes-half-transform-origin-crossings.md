# Monotone theta source excludes half-transform origin crossings

## Question

The phase-transversality reduction had two gates: exclude a zero of the
one-sided half-transform itself, and exclude a stationary crossing of its
imaginary axis.  Does completed-theta monotonicity close the first gate?

## Truncated monotone-source measure

Earlier theta source work proves

\[
\Phi'(u)<0
\qquad
(u>0).
\]

For fixed \(L>0\), define the positive measure

\[
d\mu_L(t)
=-Phi'(t)\,dt+Phi(L)\delta_L(dt)
\]

on \((0,L]\).  Its total mass is

\[
\mu_L((0,L])=\Phi(0).
\]

The layer-cake identity is exact:

\[
\Phi(u)=\mu_L([u,L]).
\]

For

\[
H_L(z)=\int_0^L\Phi(u)e^{izu}\,du,
\]

Fubini therefore gives

\[
izH_L(z)
=
\int_{(0,L]}(e^{izt}-1)\,d\mu_L(t).
\]

The endpoint atom is essential.  It retains the support boundary current that
would be lost by replacing the truncated source with \(-\Phi'(t)dt\) alone.

## Upper-half-plane zero exclusion

If \(\operatorname{Im}z>0\), then

\[
\left|
\int_{(0,L]}e^{izt}\,d\mu_L(t)
\right|
<
\mu_L((0,L]).
\]

Strictness follows because the measure has positive mass away from zero.
Hence the right side of the factorization cannot vanish, and

\[
H_L(z)\ne0
\qquad
(\operatorname{Im}z>0).
\]

## Real-axis sine orientation

For real \(x>0\), take real parts of the factorization:

\[
-xS_L(x)
=
\int_{(0,L]}(\cos(xt)-1)\,d\mu_L(t).
\]

Because \(-\Phi'(t)dt\) has positive density throughout \((0,L)\), equality
cannot occur for \(x>0\).  Therefore

\[
S_L(x)>0
\qquad
(x>0).
\]

In particular,

\[
H_L(x)\ne0
\qquad
(x\in\mathbb R).
\]

The half-transform curve remains strictly in the open upper half-plane for
positive frequency.  Every zero of the physical cosine readout is therefore a
genuine crossing of the imaginary axis, never a passage through the origin.

## Corrected collision gate

At a cosine zero,

\[
\theta_L'(x)
=
\frac{M_L(x)}{S_L(x)},
\qquad
M_L(x)=\int_0^L u\Phi(u)\sin(xu)\,du.
\]

Since \(S_L(x)>0\) for \(x>0\), the double-zero condition reduces exactly to

\[
C_L(x)=0,
\qquad
M_L(x)=0.
\]

No common sign for \(M_L\) is possible or required.  As successive simple
zeros of the real cosine transform alternate crossing direction, the sign of
\(M_L=-C_L'\) normally alternates as well.

Thus monotone theta transport closes the origin-crossing gate and leaves one
scalar transversality problem: the position-weighted sine integral must not
vanish on the cosine-zero locus.

## Relation to minimum phase

The factorization makes the one-sided theta carrier minimum-phase in the upper
half-plane.  This is a genuine source theorem, but it does not orient the
comparison with the reflected sheet strongly enough to prove simplicity of
the cosine readout.  A curve can remain in the upper half-plane while touching
the imaginary axis tangentially.

This explains precisely why causal-sheet zero-freeness was previously useful
but insufficient for RH.

## Remaining falsifier

The sole finite collision witness is now a pair \((L,x)\), with \(L>0\) and
\(x>0\), such that

\[
\int_0^L\Phi(u)\cos(xu)\,du=0,
\qquad
\int_0^L u\Phi(u)\sin(xu)\,du=0.
\]

The denominator and origin-crossing cases no longer require separate audits.

## Result

Strict decrease of the completed theta source gives an exact positive
layer-cake factorization for every finite support truncation.  It proves that
the half-transform is zero-free in the upper half-plane, has strictly positive
sine part on the positive real axis, and never crosses the origin.  The RH
support-flow programme is reduced to nonstationarity of its imaginary-axis
crossings.
