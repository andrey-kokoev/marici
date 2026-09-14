# The recovered face 234 is an admissible invertible modification in the rapid-decay asymptotic quotient

## Why an asymptotic target is required

Connes's cutoff theorem does not state an exact equality at finite cutoff. It gives

\[
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h))
-
2h(1)\log\Lambda
=
W_S(h)+
\operatorname{Err}_{\Lambda,S}(h),
\]

where, for every `N`,

\[
\operatorname{Err}_{\Lambda,S}(h)
=O_h(\Lambda^{-N}).
\]

Consequently `H_124` cannot be inverted as an equality of finite-cutoff scalar families. It becomes invertible after quotienting by the rapidly decreasing error ideal.

## Rapid-decay ideal

Let `E_S` be the admitted observer test space, equipped with its Schwartz/LF seminorms. Let `Fam(E_S)` denote continuous linear or polarized sesquilinear families

\[
A_\Lambda:E_S\to\mathbb C,
\qquad
\Lambda\ge1,
\]

with at most polynomial-logarithmic growth in `Lambda` on bounded subsets of `E_S`.

Define `N_S` to be the subspace of families satisfying, for every bounded test packet `B subset E_S` and every `N>=0`,

\[
\boxed{
\sup_{h\in B}
|A_\Lambda(h)|
\le
C_{B,N}\Lambda^{-N}.
}
\]

The rapidly decreasing families form a two-sided ideal under composition with continuous observer maps whose seminorm growth is bounded independently of `Lambda`.

Define the asymptotic quotient

\[
\boxed{
\mathsf{Asym}_S
=
\mathsf{Fam}(E_S)/\mathsf N_S.
}
\]

Write `[A_Lambda]` for the class of a family.

## Exact form of Connes's face in the quotient

Set

\[
\mathfrak T_{\Lambda,S}(h)
=
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h))
-
2h(1)\log\Lambda.
\]

Connes's estimate gives the exact equality

\[
\boxed{
[\mathfrak T_{\Lambda,S}]
=
[W_S]
}
\qquad
\text{in }
\mathsf{Asym}_S,
\]

where `W_S` is regarded as the constant family.

Thus `H_124` is an invertible modification in `Asym_S`; its inverse is represented by the same equality with reversed orientation.

No finite-cutoff inverse is asserted.

## Spectral face in the same quotient

The local logarithmic-operator calculation gives

\[
\mathscr V_S(h)
=
\langle
M_{g_h},
\mathcal L_S
\rangle
=
W_S(h),
\]

where

\[
\mathcal L_S
=M_{-\log|x|_S}.
\]

This equality is exact as a distributional pairing on the admitted test space. Embed it as a constant family in `Asym_S`. Therefore

\[
\boxed{
[\mathscr V_S]
=
[W_S]
=
[\mathfrak T_{\Lambda,S}].
}
\]

The spectral and cutoff routes now have a common analytic target category.

## Face 234 on represented observers

For a represented observer `U_S(h)` in `Geom_S^obs`, define

\[
\boxed{
H_{234,\Lambda}^{obs}(U_S(h))
=
\mathfrak T_{\Lambda,S}(h)
-
\mathscr V_S(h).
}
\]

Faithfulness of `U_S` makes this independent of the choice of observer label: there is at most one `h` representing `U_S(h)`.

Connes's theorem and the local operator identity imply

\[
H_{234,\Lambda}^{obs}(U_S(h))
=
\operatorname{Err}_{\Lambda,S}(h).
\]

Hence

\[
\boxed{
[H_{234,\Lambda}^{obs}]=0
}
\qquad
\text{in }
\mathsf{Asym}_S.
\]

Equivalently, the two functors are connected by the identity modification after passage to the asymptotic quotient.

This is the explicit analytic representative of the horn-recovered face.

## Continuity on test packets

The required admissibility is not merely pointwise `O_h(Lambda^-N)`. For functorial propagation, one needs bounded-packet estimates

\[
\boxed{
\sup_{h\in B}
|\operatorname{Err}_{\Lambda,S}(h)|
\le
C_{B,N}\Lambda^{-N}.
}
\]

Connes's Theorem 4 is stated with `o(1)`, but equation (33) and Lemma 2 in its proof establish `O(\Lambda^{-N})` for every `N`. The proof bounds tails of compactly supported smooth symbols and their logarithmic moments. On a bounded packet with support contained in one compact set and uniformly bounded defining seminorms, the constants can be chosen uniformly. This is the standard bounded-set interpretation of continuity of the remainder into `N_S`.

For the LF test topology, arbitrary bounded sets are contained and bounded in one fixed compact-support stage. Thus the estimate is compatible with the natural observer topology.

## Adjoint compatibility

For the involution

\[
h^*(u)
=
\overline{h(u^{-1})},
\]

one has

\[
U_S(h^*)=U_S(h)^*,
\]

and the cutoff projections are self-adjoint. Cyclicity in the trace-class product gives

\[
\overline{
\mathfrak T_{\Lambda,S}(h)
}
=
\mathfrak T_{\Lambda,S}(h^*)

\]

with the product-cutoff orientation changed to its adjoint when necessary:

\[
(P_\Lambda\widehat P_\Lambda)^*
=
\widehat P_\Lambda P_\Lambda.
\]

The local principal-value normalization also respects this involution. Therefore `H_234` exchanges the two polarity planes under adjoint, rather than identifying their finite-cutoff operators.

## Composition stability

Let `alpha:E'_S -> E_S` be any edge-stage observer map that is continuous and sends bounded packets to bounded packets, with no `Lambda`-dependent seminorm blowup. If `A_Lambda in N_S`, then

\[
A_\Lambda\circ\alpha
\in
\mathsf N'_S.
\]

Thus rapid-decay equality survives whiskering by the seven fixed stage maps of an eight-node factorization, provided those maps satisfy the stated boundedness condition.

The transforms used here—convolution polarization on bounded bilinear packets, Fourier/Mellin transform, fixed local Euler multiplication on the admitted strip, and represented observer insertion—have this continuity on their declared test domains.

Cutoff-changing maps require separate bookkeeping if the subdivided row changes `Lambda` nonuniformly.

## Propagation to the 343 elementary tetrahedra

The seventh edgewise subdivision produces `7^3=343` translated elementary tetrahedra. Their face modifications are whiskered copies of the four parent faces.

Because:

1. `H_234` is uniquely recovered by invertible whiskering along `U_S^obs`;
2. its representative is a rapidly decreasing remainder;
3. the fixed stage maps preserve the rapid-decay ideal;

all 343 translated `H_234` faces are admitted in `Asym_S`, assuming one common cutoff parameter is used along each translated cutoff row.

Therefore the signed analytic count is

\[
\boxed{
343/343
\text{ coherent tetrahedral fillers in the rapid-decay asymptotic quotient}.
}
\]

This count concerns equality of signed distributional/relative-trace realizations. It does not certify positive Hilbert-space fillers.

## Remaining caveat: nonuniform cutoff rows

If edgewise subdivision assigns different cutoff scales

\[
\Lambda,
\Lambda^{\alpha_1},
\ldots,
\Lambda^{\alpha_7},
\]

the remainder remains negligible when every `alpha_j>0`, because

\[
O((\Lambda^{\alpha_j})^{-N})
=
O(\Lambda^{-\alpha_jN}).
\]

Uniform propagation requires

\[
\inf_j\alpha_j>0.
\]

Since there are only seven stages, this condition is automatic once each declared cutoff exponent is positive.

## Executable propagation check

The finite checker enumerates all `7^3=343` translated cells and verifies preservation of arbitrary rapid-decay order under seven nonuniform positive cutoff exponents:

```text
python research/voevodsky/checkers/check_asymptotic_face_234_propagation.py
```

Artifacts:

- `research/voevodsky/checkers/check_asymptotic_face_234_propagation.py`
- `research/voevodsky/results/asymptotic_face_234_propagation.json`

The checker validates combinatorial and exponent bookkeeping only; it takes Connes's analytic estimate and bounded-packet continuity as inputs.

## What remains outside this quotient

The construction does not provide:

- equality of finite-cutoff operators;
- positivity of the product cutoff;
- a contraction controlling the negative layer tower;
- extension to arbitrary geometric operators outside `Geom_S^obs`.

Those are stronger claims than asymptotic coherent equivalence.

## Disposition

Face `234` is not merely formally forced. On the observer-generated category it has the explicit analytic representative

\[
\boxed{
H_{234,\Lambda}^{obs}(U_S(h))
=
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h))
-
2h(1)\log\Lambda
-
\langle M_{g_h},\mathcal L_S\rangle,
}
\]

which lies in the rapid-decay ideal. Hence it is an admissible invertible modification in the asymptotic quotient and propagates functorially to all 343 elementary tetrahedra. Positivity remains a separate gate.
