---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Radial Rees Lattice Regularizes the Nine-Master Cusp Corner

## Question

The exact bivariate connection of the nine-master
\(q_{\mathcal G_{12}}\)-residue module is logarithmic along the generic walls

\[
u=E_T=0,\qquad v=\ell_3=0,
\]

but its raw residue matrices do not have finite limits at \(u=v=0\).
The hard-to-vary claim tested here is

\[
\boxed{\text{the cusp corner requires an undeclared support divisor in the
nine-master connection.}}
\]

This entry tests the absolute rank-nine module. It does not include the three
marked relative generators of the rank-twelve extension.

## Frozen connection and radial pullback

Use the exact flat connection

\[
\nabla=d+A_u\,du+A_v\,dv
\]

in the source basis \((e_1,\ldots,e_9)\). On the first radial chart

\[
u=t,\qquad v=tr,
\]

the pulled-back coefficients are

\[
A_t=A_u+rA_v,qquad A_r=tA_v.
\]

The \(dt\)-coefficient has minimum \(t\)-valuation \(-1\), but the raw
\(dr\)-coefficient also has valuation \(-1\). Its leading term is rank one:

\[
tA_r\big|_{t=0}
=\frac1{r(r-1)}
\begin{pmatrix}
& & & & & & & &\\
& & & & & & & &\\
& & & & & & & &\\
& & & & & & & &\\
& & & & & & & &\\
& & & & & & & &\\
& & & & & & & &\\
& & & & & &1& &\\
& & & & & &-1& &
\end{pmatrix},
\qquad C^2=0.
\]

Thus the apparent irregularity is confined to the degeneration of the
\((e_8,e_9)\) frame toward \(e_7\).

## Frozen Rees lattice

Take the radial weights

\[
(w_1,\ldots,w_9)=(0,0,0,0,0,0,0,1,1),
\]

or equivalently

\[
f_i=e_i\ (i\le7),\qquad f_8=te_8,\qquad f_9=te_9.
\]

For both nonzero entries of \(C\),

\[
w_{\rm row}-w_{\rm column}=1.
\]

The transformed connection

\[
A'=GAG^{-1}+dG\,G^{-1}
\]

therefore has valuations

\[
\operatorname{ord}_t A'_t=-1,
\qquad
\operatorname{ord}_t A'_r=0.
\]

The companion chart \(v=t,\ u=tr\) gives the same pair \((-1,0)\).
Hence the radial connection is logarithmic and its exceptional tangent
connection is regular in this predeclared Rees lattice.

## Remaining exceptional-direction support

The nonconstant entries on the exceptional divisor have denominators dividing

\[
r(r-1).
\]

Here \(r=0\) is the strict transform of the other cusp wall, while \(r=1\)
is the strict transform of \(X_3=0\) in the frozen coordinates

\[
X_1=1,\quad X_2=\frac{u+v}{2}-1,\quad X_3=\frac{u-v}{2}.
\]

Both are existing energy/soft divisors.

## Verdict

The tested claim is falsified:

\[
\boxed{\text{the rank-nine cusp corner is logarithmic after the radial Rees
rescaling of }e_8,e_9,\text{ with no new support factor.}}
\]

The raw divergent corner residues were a frame-degeneration signal, not a new
carrier divisor. This strengthens H2 for the absolute nine-master coefficient
module at the two-cusp corner.

## Epistemic boundary and next falsifier

The exact bivariate source artifact has zero curvature and no generic higher
poles. The present calculation performs its two radial pullbacks and verifies
the Rees valuation change and exceptional support. It does not establish the
same result for \((\Omega_{111},\Omega_{101},\Omega_{110})\).

The remaining test is to reconstruct those three marked rows and columns in
both variables, apply the same radial lattice together with the known
\(e_6/(8E_T)\) shift, and check whether the complete rank-twelve tangent
connection is regular. A residual pole outside the strict transforms of the
frozen energy, soft, conductor, and Cut divisors would update H2 toward H3.

## Evidence

- `research/benincasa/bivariate_soft_gram_connection.json` (frozen exact input);
- `research/benincasa/marici-gm/src/bin/rank9_radial_rees_resolution.rs`;
- `research/benincasa/rank9-radial-rees-resolution-certificate.json`;
- Entries 300, 370, and 371.
