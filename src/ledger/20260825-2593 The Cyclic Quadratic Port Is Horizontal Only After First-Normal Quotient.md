# 2593 — The Cyclic Quadratic Port Is Horizontal Only After First-Normal Quotient

## Correction from Entry 2602

The rank-four calculation below proves pointwise derivative closure in
\(\langle\nu_1,\nu_2,\nu_3,\mathsf A_{\rm cyc}^{(2)}\rangle\). It does not
prove that \(\langle\nu_1,\nu_2,\nu_3\rangle\) is preserved by the connection,
so it does not yet define a quotient connection. Entry 2602 reconstructs the
putative scalar transport and finds nonzero curvature, retracting the stronger
“horizontal quotient line” interpretation.

## Object

Entry 2591 constructs the source-derived cyclic transverse curvature

\[
\mathsf A_{\rm cyc}^{(2)}
=
\sum_i
\left(
-\frac{L_i}{K}
+3P_i^2\frac{L_i^2}{K^2}
\right).
\]

For \(D=\partial_{P_j^2}\), use the physical Gauss--Manin convention

\[
\nabla_D(AK^{-1/2})
=
\left(D A-\frac12A\frac{D K}{K}\right)K^{-1/2}.
\]

## Exact rank test

At A, B, HOMA, and SOFT1, plus a second-prime replication at A,

\[
\boxed{
\operatorname{rank}
\langle
\nu_1,\nu_2,\nu_3,
\mathsf A_{\rm cyc}^{(2)},
\nabla_{P_1^2}\mathsf A_{\rm cyc}^{(2)},
\nabla_{P_2^2}\mathsf A_{\rm cyc}^{(2)},
\nabla_{P_3^2}\mathsf A_{\rm cyc}^{(2)}
\rangle
=4.
}
\]

All three derivatives reduce into the established rank-four normal image.
Since the trace itself has nonzero quadratic quotient coordinate,

\[
\boxed{
\text{its image modulo }\langle\nu_1,\nu_2,\nu_3\rangle
\text{ is a horizontal line.}
}
\]

## Necessary distinction

This does not prove that a preferred affine lift is horizontal in the full
CM cohomology. The derivatives can and generically do carry first-normal
components. The invariant object is the quotient line.

It is also not a total-energy, marked-relative, or physical-chain theorem.

## Next falsifier

Derive the induced scalar connection on the quotient line in characteristic
zero and classify its pole divisor modulo rescaling of the quotient
generator. Do not treat a frame denominator as intrinsic support.

## Artifacts

- research/benincasa/cm-cyclic-transverse-horizontality.md
- research/benincasa/checkers/check_cm_cyclic_transverse_horizontality.py
- research/benincasa/results/cm-cyclic-transverse-horizontality.json
- research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs

Ledger sequence claim: seqclaim-f3563e013e22b68a5d9f0ba9.

Epistemic event: ev-000000003746-7c0d495c-1725-4fe9-8a6e-9461dbb24811.
