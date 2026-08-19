# 1016 — Dual Cellularization Adds Only a Trivial-Monodromy Gauge

## Connection question

Entry 1015 closes the static cellular comparison.  Does differentiating its
diagonal frames produce a new connection-level extension?

Let (D_i) be the degree-(i) cellular intertwiners.  For arbitrary absolute
connections (A_{\rm primal}) and (A_{\rm dual}), horizontality of (D_i)
uses the convention

\[
dD_i+A_{{\rm dual},i}D_i-D_iA_{{\rm primal},i}=0.
\]

Therefore the relative connection forced solely by the frame change is

\[
\boxed{
A_{{\rm dual},i}
-D_iA_{{\rm primal},i}D_i^{-1}
=-dD_iD_i^{-1}.
}
\]

## Exact logarithmic residues

In coordinates

\[
d\log B_{34},\qquad d\log B_{24},\qquad d\log X,
\]

the degree-zero residue vectors are

\[
\begin{aligned}
&(0,0,0),
(2,0,0),
(2,2,0),\
&(2,2,2),
(0,2,2),
(0,0,2).
\end{aligned}
\]

The degree-one list is the cyclic shift of this list, and the degree-two
residue is zero.  Thus the relative connection is diagonal, logarithmic, and
flat:

\[
F_{\rm rel}=0.
\]

Every residue is an even integer.  Hence every local monodromy contributed by
this gauge is identity:

\[
\boxed{
\exp(2\pi i\,\operatorname{Res}A_{\rm rel})=1.
}
\]

## Narrow conclusion

The dual cellularization contributes no new singular support and no
nontrivial monodromy.  It is a Laurent-monomial gauge transformation of the
cellular complex, not a connection extension.

This sharpens Entry 929.  The still-missing absolute six-point connection
cannot be reconstructed from (D_\bullet), but any extension class it carries
must originate in the Koba–Nielsen logarithmic-insertion reduction or another
source coefficient object—not in primal/dual cellular conversion.

## Scope

No absolute Gauss–Manin matrix has been constructed.  Flatness here is the
flatness of the relative gauge term (-dD_iD_i^{-1}), not a claim that the
source period bundle has trivial connection.

## Next falsifier

Construct one source-normalized logarithmic insertion in a single channel,
as required by Entry 929.  Reduce it in a predeclared enlarged cocycle basis
and test the covariant derivative of Entry 977's evaluation map.  The present
result permits stripping off the known diagonal dual gauge before classifying
any residual extension.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_dual_relative_connection.rs`;
- packet:
  `research/benincasa/string-six-point-dual-relative-connection.json`;
- allocator claim:
  `seqclaim-b86d5aee809759aaab163765`.
- epistemic event:
  `ev-000000000635-b9d68c65-2768-40d7-adfa-5c12d790e27f`.
