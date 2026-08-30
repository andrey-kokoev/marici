# Theta tail and seam have one common source trace

## The split source atoms

For a positive scale label `q`, retain the two source-derived pieces

\[
 g_q(t)=\Phi(t+q),
 \qquad t\ge0,
\]

and

\[
 h_q(t)={\bf1}_{0\le t\le q}\Phi(q-t).
\]

The first is the translated source remaining in the positive tail.  The
second is the part which crosses the modular seam.  They are independent
state components after completion, but they arise by cutting one translated
bilateral source.

## Exact seam incidence

Their seam traces coincide:

\[
 \boxed{
 g_q(0)=h_q(0)=\Phi(q).}
\]

Their inward normal derivatives carry the reflection orientation:

\[
 g_q'(0)=\Phi'(q),
 \qquad
 h_q'(0)=-\Phi'(q).
\]

Thus the common value and the oriented normal jump are both fixed before any
Euler aggregation:

\[
 \operatorname{Tr}_0(g_q,h_q)
 =\bigl(\Phi(q),\,2\Phi'(q)\bigr).
\]

The seam is therefore not an arbitrary extra Hilbert summand.  It is an
independent completion coordinate with a source-fixed incidence to the tail.

## Finite labelled packets

For a finite label set `Q_X`, let

\[
 G_Xc=\sum_{q\in Q_X}c_qg_q,
 \qquad
 H_Xc=\sum_{q\in Q_X}c_qh_q.
\]

Endpoint evaluation gives one common row

\[
 \tau_X(c)=\sum_{q\in Q_X}c_q\Phi(q),
\]

with

\[
 \boxed{
 \operatorname{ev}_0G_X=\tau_X=\operatorname{ev}_0H_X.}
\]

Consequently

\[
 \ker(\operatorname{ev}_0G_X)
 =\ker(\operatorname{ev}_0H_X),
\]

so the operator well-definedness gate
`ker A_X subset ker B_X` closes exactly at the source-trace level.

## Kitaev projective slope

Before arithmetic aggregation into the anomaly line, the two incidence rows
are identical:

\[
 a_X=b_X=\tau_X.
\]

Hence the two-cutoff projective residual

\[
 \Delta_{X,Y}=a_Yb_X-b_Ya_X
\]

vanishes identically wherever both expressions are compared through the same
coefficient inclusion:

\[
 \boxed{\Delta_{X,Y}=0.}
\]

This is not a fitted parallelization.  Equality is forced by continuity of
the undecomposed source across the cut.  Any common line-frame change scales
both rows together and preserves their projective slope `1`.

## What remains undefined

The common trace takes values in the labelled seam-trace module, not yet in
the arithmetic anomaly line `L_X`.  A further source map

\[
 \lambda_X:\operatorname{Ran}\tau_X\longrightarrow L_X
\]

must assemble exact integer/prime-power labels with the primitive and square
transition cocycles.  Setting

\[
 A_X=\lambda_X\tau_X,
 \qquad
 B_X=\lambda_X\tau_X
\]

preserves the tail--seam slope automatically.  Both of Kitaev's coherence
cells then reduce to the single arithmetic equation

\[
 \boxed{
 \lambda_Y\tau_YV_{X,Y}
 =U_{X,Y}\lambda_X\tau_X.}
\]

Thus the missing source data are smaller than previously stated: there are
not two unrelated tail/seam incidence maps.  There is one common seam trace
and one arithmetic aggregation map into the anomaly line.

## Detector boundary

The equality of endpoint traces does not imply nonvanishing of their
arithmetic aggregation.  A nonzero coefficient packet may lie in
`ker tau_X`, and a completed detector may become orthogonal to the transported
source state.  The identity closes the projective compatibility gate, not the
detector-transversality gate exposed by Kitaev's `C^2` witness.

## Scope and falsifier

The theorem applies to the canonical translated tail/seam atoms above.  It
does not yet incorporate Clark differentiation, the full archimedean jet, or
the map `lambda_X` into the Tate anomaly line.

The next falsifier is one source-authorized arithmetic bonding for which

\[
 \lambda_Y\tau_YV_{X,Y}
 -U_{X,Y}\lambda_X\tau_X\ne0.
\]

Such a residual would live entirely in arithmetic aggregation; it could no
longer be blamed on tail--seam parallelization.
