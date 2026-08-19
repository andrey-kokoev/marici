# 889 — The Parke–Taylor Period Circuit Closes at Associated Grade

## Record

Date: 2026-08-18

Status: exact field-theory-leading/associated-grade period-intertwining theorem for two cycle and two Parke--Taylor cocycle labels. This does **not** establish the finite-\(\alpha'\) hypergeometric period identity.

## Frozen cocycles and cycles

Use the Parke--Taylor cocycle basis

\[
\Phi=igl(\operatorname{PT}(12345),\operatorname{PT}(12435)\bigr),
\]

the source cycle basis

\[
\mathcal C=(13254,14253),
\]

and Entry 888's target basis

\[
\mathcal D'=(12354,12453).
\]

The source states that, after removing the common \(\alpha'^{-2}\) normalization, the leading string periods reduce to bi-adjoint double-partial amplitudes.

## Source period grade

The common-vertex calculation of Entry 883 gives

\[
\operatorname{gr}P_{\mathcal C,\Phi}
=
\begin{pmatrix}
\dfrac1{s_{23}s_{45}}&0\\[2mm]
0&\dfrac1{s_{24}s_{35}}
\end{pmatrix}.
\]

The zero entries are cocycle selections: the corresponding Parke--Taylor forms select no common trivalent vertex.

## Circuit grade

Entry 888 has field-theory grade

\[
\operatorname{gr}M_{\mathcal D'\leftarrow\mathcal C}
=
-\frac1{s_{12}}
\begin{pmatrix}
s_{12}+s_{23}&s_{24}\\
s_{23}&s_{12}+s_{24}
\end{pmatrix}.
\]

Multiplication yields

\[
\operatorname{gr}M\operatorname{gr}P_{\mathcal C,\Phi}
=
\begin{pmatrix}
-\dfrac1{s_{12}s_{45}}-\dfrac1{s_{23}s_{45}}
&-\dfrac1{s_{12}s_{35}}\\[3mm]
-\dfrac1{s_{12}s_{45}}
&-\dfrac1{s_{12}s_{35}}-\dfrac1{s_{24}s_{35}}
\end{pmatrix}.
\]

Every entry is independently the common-triangulation sum for the target cycle and the corresponding Parke--Taylor cocycle. Therefore

\[
\boxed{
\operatorname{gr}P_{\mathcal D',\Phi}
=
\operatorname{gr}M_{\mathcal D'\leftarrow\mathcal C}
\operatorname{gr}P_{\mathcal C,\Phi}.
}
\]

At

\[
(s_{12},s_{23},s_{24},s_{35},s_{45})=(2,3,9,-14,11),
\]

the exact target matrix is

\[
\begin{pmatrix}
-5/66&1/28\\
-1/22&11/252
\end{pmatrix},
\]

and the Rust checker verifies the matrix identity over \(\mathbb Q\).

## Typed conclusion

This is the first tested string comparison containing both:

- a change of twisted-cycle basis;
- two independently labelled logarithmic Parke--Taylor cocycles.

It closes using the same labelled face/circuit calculus at associated grade. No extra contact term or carrier cell is needed.

But the type boundary is essential:

\[
\boxed{
\text{associated-grade period intertwining}
\not\Rightarrow
\text{finite-}\alpha'\text{ period theorem}.
}
\]

The latter still requires the actual Koba--Nielsen periods and their branch-normalized analytic continuation.

## Next falsifier

Compute one finite-\(\alpha'\) Parke--Taylor period column by source-normalized hypergeometric continuation in both cycle bases. Test the circuit identity numerically at generic nonresonant kinematics, preserving branch phases. Failure after source normalization would locate the first coefficient-level obstruction beyond associated grade.

## Certificate

Run:

```text
cargo run --quiet --bin string_five_point_pt_associated_grade
```

Artifacts:

- `research/benincasa/marici-gm/src/bin/string_five_point_pt_associated_grade.rs`
- `research/benincasa/string-five-point-pt-associated-grade.json`

## Sources

- Sebastian Mizera, *Combinatorics and Topology of Kawai--Lewellen--Tye Relations*, arXiv:1706.08527, Sections 3.2--3.4 and Appendix B.
- Sebastian Mizera, *Inverse of the String Theory KLT Kernel*, arXiv:1610.04230, equation (5.4).
