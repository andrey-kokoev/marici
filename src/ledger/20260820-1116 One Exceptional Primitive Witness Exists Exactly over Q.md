---
author: marici.Benincasa
---

# 1116 — One Exceptional Primitive Witness Exists Exactly over Q

## Frozen problem

At the exceptional center

\[
(u,v)=(0,2),
\]

Entry 1098 constructed a two-chart glued rank-four quotient object only after
finite-field reduction.  Entry 1115 bounded a pilot source primitive in the
\(p\)-chart by

\[
(\deg N,\deg D)=(6,4).
\]

The present entry tests one quotient generator and one chart exactly over
\(\mathbb Q\).

## Source-normalized identity

The source system contains 372 columns: twelve marked-relative class columns
and 360 degree-eight exact columns.  A deterministic lexicographic convention
was used only to choose one primitive representative.  It is not asserted to
be canonical.

Two-prime reconstruction gives 218 nonzero scalar coefficients, assembling
into only 47 nonzero numerator polynomials.  The common denominator is

\[
\boxed{
D_p(s)=s(s-1)(s^2+6s+1),
\qquad s=q/p.
}
\]

Substitution into the complete symbolic source identity gives

\[
\boxed{
\sum_{j=1}^{372}N_j(s)M_j(s,a,b)
-D_p(s)r_0(s,a,b)=0
}
\]

as a polynomial in \(\mathbb Q[s,a,b]\).  The residual has zero terms.

## Narrow result

\[
\boxed{
\text{One pilot exceptional primitive exists exactly over }\mathbb Q
\text{ in the }p\text{-chart}.}
\]

Thus the modular rank-four quotient at this center is not merely an artifact
of the two tested characteristics.

## Remaining descent obstruction

The analogous lexicographic \(q\)-chart representative is a poor rational
lattice: even four-prime CRT reconstruction leaves 191 coefficients beyond a
74-digit modulus.  This is not evidence that no rational \(q\)-chart
primitive exists.  It shows that independently choosing modular pivot
sections is not a viable chart-gluing convention.

The remaining problem is therefore typed as primitive-gauge transport:

\[
\boxed{
\text{transport the exact }p\text{-chart primitive across }r=s^{-1}
\text{ and compare modulo the exact submodule}.}
\]

## Scope

This entry does not establish:

- exact characteristic-zero primitives for the other three quotient classes;
- a characteristic-zero primitive in the independently reduced \(q\)-chart;
- an exact overlap cocycle for primitive representatives;
- canonicity of the lexicographic primitive;
- a global rank-twelve connection or physical relative-chain pairing.

## Durable verification

Witness:

`research/benincasa/rank12-u0-v2-exceptional-pilot-rational-witness.json`.

Checker:

`research/benincasa/checkers/rank12_u0_v2_exact_primitive_witness.py`.

Result:

`research/benincasa/results/rank12-u0-v2-exceptional-pilot-rational-witness.json`.

Ledger claim: `seqclaim-e6b19811fc941654980d3531`.

Epistemic event:

`ev-000000000815-181e3516-a016-4cf2-8857-267be17a8426`.

## Next falsifier

Derive the overlap transport of the 372 source columns under

\[
r=s^{-1},\qquad A_q=rA_p,\qquad B_q=rB_p,
\]

including derivative variance.  Transport the exact \(p\)-chart witness and
test whether its difference from a \(q\)-chart lift lies in the exact
submodule.  Failure after source-derived transport would be a genuine
coefficient-descent obstruction; failure of another fitted pivot convention
would not.
