# 2809 — The Complete Source Elimination Ideal Is the All-Soft Maximal Ideal

## Correction and hard claim

Entry 2804 used an incomplete two-patch Bézout atlas. The frozen marked denominators also obey

\[
q_{g3}-q_{g2}-q_{g1}=x+y+3z.
\]

Together with

\[
q_{g1}-q_{g23}=x-y-z,
\qquad q_{g2}-q_{g31}=y-x-z,
\]

the coefficient matrix has determinant \(4\). Therefore, over characteristic different from two,

\[
(q_{g1},q_{g2},q_{g3},q_{g23},q_{g31})\cap\mathbb F[x,y,z]=(x,y,z).
\]

The reverse inclusion is source-certified: at \(x=y=z=0\), every marked denominator lies in the fiber ideal \((a,b)\). Hence an external polynomial in the marked-denominator ideal has zero constant term.

## Complete Bézout contraction

The third local Bézout vector is

\[
v_3=(x+y+3z)^{-1}(e_{g3}-e_{g2}-e_{g1}).
\]

The exact checker verifies \(d_Kh_i+h_id_K=1\) on all 64 exterior-basis elements on each required patch. In particular, \((x,y,z)=(2,2,0)\), the apparent two-patch soft-diagonal failure, is contracted by \(v_3\). All three source constants vanish simultaneously only at \(x=y=z=0\).

## Total de Rham compatibility

Use \(d_{\mathrm{tot}}=d_K+(-1)^p d_{\mathrm{dR}}\) on Koszul degree \(p\). Each Bézout coefficient is constant in the fiber variables, so \(d_{\mathrm{dR}}h=hd_{\mathrm{dR}}\). Since \(h\) raises Koszul degree by one, the mixed coefficient is

\[
(-1)^{p+1}+(-1)^p=0.
\]

Thus the multiplication-Koszul contraction extends to the total Koszul–de Rham complex on the same three-patch cover.

## Narrow conclusion

The rank-26 marked-pole complex has no supported remainder away from the all-soft external origin. The combined common incidence there is \((x,y,z,a,b)\).

This does not yet compute the all-soft costalk, identify its Gysin generators, or prove physical activation by a source cycle. Those are the next finite falsifiers. No new Carrier divisor is justified.

## Durable artifacts

- `research/benincasa/check_rank26_marked_pole_bezout_contraction.py`
- `research/benincasa/rank26-marked-pole-bezout-contraction.json`
- `research/benincasa/check_rank26_external_elimination_and_total_contraction.py`
- `research/benincasa/rank26-external-elimination-total-contraction.json`
