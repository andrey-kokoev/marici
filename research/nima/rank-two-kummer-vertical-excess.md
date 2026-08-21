# The Rank-Two Kummer Line Is a Gram-Supported Vertical Excess

The algebraic line \(w^2=-R\) does not arise as an ordinary restriction of
the generic physical degree-32 marked cover. It appears through a nonflat
rank-drop specialization.

Consider the exact family

\[
a=(1,0,0),\qquad
b=(0,1,0),\qquad
c=(1,1,e).
\]

The first two bisector equations fix

\[
\ell=(1/2,1/2,z).
\]

The third bisector and null equations become

\[
e(z-e/2)=0,
\qquad
z^2+1/2=0.
\]

Eliminating \(z\) gives

\[
\boxed{
\operatorname{Res}_z
\left(e(z-e/2),z^2+1/2\right)
=
\frac14e^2(e^2+2).
}
\]

The two factors have different meanings:

- \(e^2=0\) is the external-Gram rank-drop component;
- \(e^2+2=0\) is the ordinary nondegenerate zero-radius discriminant.

Near \(e=0\), every nonzero fiber is empty, while the special fiber is

\[
z^2+1/2=0,
\]

with two reduced complex points. Hence this two-sheeted Kummer line is a
vertical excess supported on the Gram divisor, not a flat continuation of a
generic fourfold intersection.

This reconciles the result with Benincasa Entries 1216--1217:

- the physical measure carries the external-Gram Kummer density;
- the generic marked coefficient object is the degree-32 \(C_2^5\) cover;
- the \(w\)-line is an additional algebraic special-fiber object created by
  the rank-drop totalization.

Therefore it must be typed through a supported nearby-cycle, Tor, or excess
intersection complex before it can contribute physically. Ordinary
restriction of the degree-32 local system is insufficient.

Artifacts:

- `research/nima/check_rank_two_kummer_vertical_excess.py`
- `research/nima/results/rank-two-kummer-vertical-excess.json`
