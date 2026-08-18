---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Algebraic Quartic Is Not Fitting Support of the Conic Limit Line

## Question

Entry 525 constructed the canonical coefficient line

\[
\mathcal L_{\rm fit}=G_{C_{\rm fit}}/G_{\rm lim}
\]

on

\[
C_{\rm fit}:\qquad X_1X_2-E_T^2=0.
\]

Test the narrow claim

\[
\boxed{\mathcal Q=0\text{ is rank or Fitting support of }
\mathcal L_{\rm fit}.}
\]

This is only a support test. It does not test the induced connection or the
extension to the elliptic quotient.

## Frozen restriction

On the \(X_1=1\) patch put

\[
u=E_T,\qquad X_2=u^2.
\]

The source quartic restricts exactly to

\[
\boxed{
\mathcal Q|_{C_{\rm fit}}
=u^3(8u^2-29u+8).
}
\]

The factor \(u^3\) is soft/total-energy support. The two nonzero roots of

\[
8u^2-29u+8
\]

are the generic algebraic-quartic intersections with the fitting conic.

## Exact finite-field test

Over \(\mathbf F_{2305843009213693951}\), the discriminant is \(585\), with
chosen square root

\[
\sqrt{585}=1010164894911838578.
\]

The two roots are

\[
u_+=2224863127069827992,
\qquad
u_-=1522131762902424682.
\]

At each root and at exact-form degrees \(8\) and \(10\), compute the full
homogeneous exact-lift rank and the projected special-fiber gauge plane.
Compare with the two neighboring conic fibers \(u\pm1\).

The results are constant:

\[
\begin{array}{c|c|c|c}
\text{degree}&\operatorname{rank}&
\operatorname{rank}G_{C_{\rm fit}}&
\text{pivot mask}\\
\hline
8&116&3&280\\
10&151&3&280
\end{array}
\]

at both quartic roots and all four neighboring fibers. The canonical extra
row retains support mask \(3328\), namely

\[
\langle e_6,e_8,e_9\rangle.
\]

No rank drop, rank enhancement, pivot change, or disappearance of the
canonical quotient line occurs at either nonsoft root.

## Verdict

The tested claim is falsified:

\[
\boxed{
\mathcal Q=0
\text{ is not Fitting/rank support of }
\mathcal L_{\rm fit}
\text{ in the frozen exact-lift presentation.}
}
\]

Consequently, if \(\mathcal Q\) belongs to this mechanism, it must enter
through one of the structures not measured by fiber rank:

\[
\text{the induced connection on }\mathcal L_{\rm fit},
\qquad
\text{the algebraic--elliptic extension class},
\qquad
\text{or physical relative-chain data}.
\]

## Classification

| Datum | Classification |
|---|---|
| \(C_{\rm fit}\) | internal coefficient Fitting divisor |
| \(\mathcal Q\cap C_{\rm fit}\), away from \(u=0\) | not support of the conic rank-one quotient |
| \(u=0\) factor | existing total-energy/soft support |
| possible \(\mathcal Q\) connection pole | untested coefficient data |
| possible \(\mathcal Q\) extension support | untested coefficient data |
| new carrier datum | none |

## Epistemic boundary

This finite-field fiber census does not compute tangent transport, a
Gauss--Manin connection, extension data, integral normalization, or the
physical relative chain. Constancy at the two finite-field roots is evidence
against Fitting support in the tested model; it is not a characteristic-zero
proof of regularity of the full connection.

## Next falsifier

Differentiate the complete homogeneous relation

\[
A(u)r(u)=0
\]

along \(C_{\rm fit}\), retaining primitive exact-lift coordinates. Solve

\[
A(u)r'(u)=-A'(u)r(u)
\]

modulo the persistent limit plane, rather than differentiating a chosen RREF
representative. Determine whether the induced rank-one transport exists. If
it exists, factor its nonintegral pole divisor and test whether
\(8u^2-29u+8\) occurs. If it does not, classify the failure as extension
data. No carrier modification is admissible.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`;
- `research/benincasa/gauge-fitting-conic-q-fibers.json`;
- Entries 390 and 525.
