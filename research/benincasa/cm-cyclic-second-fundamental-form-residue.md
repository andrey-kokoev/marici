# The cyclic quadratic class is the first-normal transport residue

## Source-normal classes

Let

\[
L_i=\frac{\partial K}{\partial(P_i^2)},
\qquad
s_i=P_i^2.
\]

The physical first variation of the \(K^{-1/2}\) coefficient is represented,
up to a nonzero scalar, by

\[
\mathsf n_i=\frac{L_i}{K}K^{-1/2}.
\]

For \(D=\partial_{s_j}\), its covariant derivative is

\[
\nabla_D\mathsf n_i
=
\left(
\frac{D L_i}{K}
-\frac32\frac{L_i D K}{K^2}
\right)K^{-1/2}.
\]

This is the source-derived first-normal packet whose preservation must be
tested before forming a quotient.

## Rank result

The reducer automatically localizes labelled coefficient columns by one power
of \(K^{-1}\). Accordingly, the machine packet supplies bare \(L_i\) in those
columns; the displayed \(L_i/K\) classes are their reduced meanings. This
corrects an earlier extra-localization defect. The ranks below are from the
repaired packet.

At A, B, and HOMA, with independent-prime replication at A,

\[
\operatorname{rank}\langle\mathsf n_1,\mathsf n_2,\mathsf n_3\rangle=3.
\]

Adjoining the first ordered derivative already gives

\[
\operatorname{rank}
\langle\mathsf n_1,\mathsf n_2,\mathsf n_3,
\nabla_{s_1}\mathsf n_1\rangle=4.
\]

Every remaining labelled derivative stays in that rank-four closure. Thus the
rank-three first-normal span is not a subconnection, and its complete first
transport closure adds exactly one direction.

## Identification with the cyclic port

Let \(\mathsf A_{\rm cyc}^{(2)}\) be Entry 2591's cyclic quadratic class. The
three decisive ranks are

\[
\begin{aligned}
\operatorname{rank}\langle N_1,\mathsf A_{\rm cyc}^{(2)}\rangle&=4,\\
\operatorname{rank}\langle N_1,\nabla_{s_1}\mathsf n_1\rangle&=4,\\
\operatorname{rank}\langle N_1,\mathsf A_{\rm cyc}^{(2)},
\nabla_{s_1}\mathsf n_1\rangle&=4,
\end{aligned}
\]

where \(N_1=\langle\mathsf n_1,\mathsf n_2,\mathsf n_3\rangle\). Therefore the
cyclic class and the transport escape generate the same unique quotient
direction.

## Interpretation

The quadratic port is the second-fundamental-form residue of failed
first-normal transport. It is born canonically when legal continuation of the
rank-three normal packet leaves that packet.

This supplies a cosmological realization of the cross-sector mechanism
“failed legal continuation produces a new invariant record.” It does not yet
supply a physical pairing or observable activation.

## Rank-four closure

Entry 2610 adjoins the derivatives of all four generators

\[
\mathsf n_1,\quad\mathsf n_2,\quad\mathsf n_3,\quad
\mathsf A_{\rm cyc}^{(2)}.
\]

The complete sixteen-class packet—four generators, nine labelled derivatives
of the normal classes, and three derivatives of the cyclic class—still has
rank four in every tested fiber. Thus the first escape completes, rather than
starts, the finite transport closure in these models.

## Artifacts

- `research/benincasa/checkers/check_cm_first_normal_subconnection.py`
- `research/benincasa/results/cm-first-normal-subconnection.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`
