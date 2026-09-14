# The inside and outside prolate towers share one Halmos angle operator and differ only at exact-intersection atoms

## Four exact intersections

For two orthogonal projections `P,Q` on `H`, define

\[
H_{11}
=
\operatorname{Ran}P
\cap
\operatorname{Ran}Q,
\]

\[
H_{10}
=
\operatorname{Ran}P
\cap
\ker Q,
\]

\[
H_{01}
=
\ker P
\cap
\operatorname{Ran}Q,
\]

\[
H_{00}
=
\ker P
\cap
\ker Q.
\]

The standard Sonin sector is `H_00`. The exact eigenvalue-one atom of `PQP` is `H_11`.

Remove all four exact intersections and call the remaining reducing subspace `H_gen`.

## Halmos generic representation

On the generic part there is a Hilbert space `K`, a positive contraction `B` with

\[
0<B<I
\]

in the spectral sense, and a unitary identification

\[
H_{gen}
\simeq
K\oplus K
\]

under which

\[
\boxed{
P
=
\begin{pmatrix}
I&0\\
0&0
\end{pmatrix},
}
\]

\[
\boxed{
Q
=
\begin{pmatrix}
B&D\\
D&I-B
\end{pmatrix},
\qquad
D=[B(I-B)]^{1/2}.
}
\]

All entries commute because they are functions of the same angle contraction `B`.

## Inside contraction

The compression of `Q` to `ran P` is

\[
B^{in}
=PQP|_{\operatorname{Ran}P}.
\]

On the decomposition above,

\[
\boxed{
B^{in}|_{H_{gen}}
=B.
}
\]

Its exact endpoint atoms are:

- eigenvalue one on `H_11`;
- eigenvalue zero on `H_10`.

## Outside contraction

Define

\[
B^{out}
=(I-P)(I-Q)(I-P)
|_{\operatorname{Ran}(I-P)}.
\]

Since

\[
I-Q
=
\begin{pmatrix}
I-B&-D\\
-D&B
\end{pmatrix},
\]

one obtains

\[
\boxed{
B^{out}|_{H_{gen}}
=B.
}
\]

Its exact endpoint atoms are:

- eigenvalue one on `H_00`;
- eigenvalue zero on `H_01`.

Thus the inside and outside contractions have the same generic angle spectrum.

## Sewing operator

Define the off-diagonal sewing operator

\[
\boxed{
S
=(I-P)QP:
\operatorname{Ran}P
\to
\operatorname{Ran}(I-P).
}
\]

In the Halmos representation,

\[
S|_{H_{gen}}
=D
=[B(I-B)]^{1/2}.
\]

Moreover,

\[
\boxed{
S^*S
=B^{in}(I-B^{in})
}
\]

on `ran P`, and

\[
\boxed{
SS^*
=B^{out}(I-B^{out})
}
\]

on `ran(I-P)`, after excluding exact atoms on which both sides vanish.

These are projection identities, not asymptotic prolate estimates.

## Polar intertwiner

Let

\[
S=V|S|
\]

be the polar decomposition. Then `V` is a partial isometry from the generic support of `B^(in)(I-B^(in))` to the generic support of `B^(out)(I-B^(out))`.

Because both generic contractions are represented by the same `B`,

\[
\boxed{
V B^{in}
=B^{out}V
}
\]

on the generic support.

Therefore for every bounded Borel function `f`,

\[
\boxed{
Vf(B^{in})
=f(B^{out})V.
}
\]

In particular, `V` identifies all dyadic bulk and defect operators in the two towers.

## Dyadic defect correspondence

For

\[
d_j^{in}
=
[(B^{in})^{2^j}
(I-(B^{in})^{2^j})]^{1/2}
\]

and

\[
d_j^{out}
=
[(B^{out})^{2^j}
(I-(B^{out})^{2^j})]^{1/2},
\]

one has

\[
\boxed{
Vd_j^{in}
=d_j^{out}V.
}
\]

Thus the outside dyadic tower does not introduce a second independent near-one spectrum. It is the opposite polarization of the same generic angle operator.

## Terminal dyadic identities

The inside tower satisfies

\[
\sum_{j\ge0}
(B^{in})^{2^j}
(I-(B^{in})^{2^j})
=
B^{in}-P_{H_{11}}.
\]

The outside tower satisfies

\[
\sum_{j\ge0}
(B^{out})^{2^j}
(I-(B^{out})^{2^j})
=
B^{out}-P_{H_{00}}.
\]

Their generic sums are carried into each other by `V`; their atom subtractions are different.

## Correct positive carrier

The full two-projection positive carrier is therefore

\[
\boxed{
H_{11}
\oplus
H_{10}
\oplus
(K\oplus K)
\oplus
H_{01}
\oplus
H_{00}.
}
\]

Its data consist of:

1. one generic angle contraction `B`;
2. two polarization copies of its carrier `K`;
3. the sewing amplitude `D=sqrt(B(1-B))`;
4. four separately typed exact intersections.

It is incorrect to model the positive completion as two unrelated prolate contractions.

## Sonin placement

The Sonin sector `H_00` is an exact outside atom. It is orthogonal to the generic sewing range because

\[
D=0
\]

on endpoint atoms.

Therefore the generic Tate--Hardy boundary intertwiner and the Sonin assignment can be studied separately:

\[
\boxed{
\text{generic angle cloud}
\perp
\text{exact Sonin atom}.
}
\]

No limiting near-one eigenvector is literally a Sonin vector at finite cutoff.

## Near-one scaling

If `B` has eigenvalues

\[
\lambda_\Lambda
=1-\varepsilon_\Lambda,
\]

both polarizations have the same gap scale. Hence one joint depth

\[
2^{n(\Lambda)}
\varepsilon_\Lambda
\asymp1
\]

resolves both inside and outside generic towers.

There is no second independent depth function.

## Tate polarity interpretation

The two copies `K \oplus K` are the natural positive carrier for opposite Hardy/scattering orientations. The sign reversal of the cutoff spectral-flow coefficient acts on the polarization coordinate, while `B` records their common positive angle geometry.

This matches the earlier distinction:

- positive completion retains both polarization rows;
- signed relative trace applies a fundamental symmetry after the positive feature is formed.

## Cutoff dependence

For each cutoff `Lambda`, the sewing polar part

\[
V_\Lambda
\]

canonically identifies the two generic towers at that cutoff. Comparison across different cutoffs still requires observer-labelled correspondences or an absolute-Gram theorem; `V_Lambda` alone does not intertwine `B_Lambda` with `B_(Lambda')`.

## Acceptance test on the semilocal carrier

For the exact semilocal projections:

1. construct the four Halmos intersections `H_(ab,Lambda)`;
2. verify the source Sonin space is `H_(00,Lambda)`;
3. compute whether `H_(11,Lambda)=0` by semilocal uncertainty;
4. form `S_Lambda=(I-P_Lambda)Q_Lambda P_Lambda`;
5. verify its polar part carries the observer domain used by both positive rows;
6. prove cutoff compatibility of the generic angle correspondences.

Items 1, 4, and the fixed-cutoff algebra are unconditional. Items 2, 3, 5, and 6 depend on the precise semilocal carrier/domain.

## Consequence for cell structure

A positive `C_34` cell need not contain two separate dyadic subdivisions. It contains:

- one dyadic generic-angle spine;
- two polarization realizations related by `V`;
- separate endpoint vertices for `H_11` and `H_00`;
- zero-angle vertices `H_10` and `H_01` when retained.

This reduces duplicated pro-simplicial data while preserving exact Sonin typing.

## Disposition

The complete fixed-cutoff projection-pair geometry is

\[
\boxed{
B^{in}_{gen}
\xrightarrow[V]{\simeq}
B^{out}_{gen},
\qquad
P_{\{1\}}(B^{in})=P_{H_{11}},
\qquad
P_{\{1\}}(B^{out})=P_{H_{00}}.
}
\]

Hence the positive filler requires one generic prolate defect tower with two sewn polarizations, plus separately typed exact-intersection atoms. The next analytic task is semilocal uncertainty and stability of `H_00` under cutoff/place enlargement.
