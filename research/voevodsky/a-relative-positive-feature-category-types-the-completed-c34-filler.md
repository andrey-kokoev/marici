# A relative positive-feature category types the completed `C_34` filler

## Motivation

The recentered Tate/reference feature splits into:

- a common row `C`, bounded as a module map but not Hilbert--Schmidt after volume exhaustion;
- a difference row `D M_g`, Hilbert--Schmidt for every admitted observer;
- a finite cross trace equal to the Tate relative current.

An ordinary Hilbert feature category cannot retain this limit because it requires every observer leg to have finite norm. The minimal enlargement is a category of relative positive features.

## Relative feature datum

Fix a source test space `E`, a Hilbert carrier `H`, an observer representation

\[
\rho:E
\longrightarrow
\mathcal B(H),
\]

and a two-polarity carrier `K=H \oplus H` with fundamental symmetry

\[
J_2
=
\operatorname{diag}(I,-I).
\]

A **relative positive feature** is a tuple

\[
\boxed{
\mathfrak F
=(C,D,J_2,\tau_{rel})
}
\]

such that:

1. `C:H->K` is bounded;
2. `D rho(g) in S_2(H,K)` for every `g in E`;
3. for every `g,h in E`,
   \[
   \rho(h)^*
   (C^*J_2D+D^*J_2C)
   \rho(g)
   \in\mathcal S_1(H);
   \]
4. endpoint/index rows are finite rank or separately trace class;
5. `tau_rel` agrees with ordinary trace on the trace-class cross operator.

The associated signed observation form is

\[
\boxed{
q_\mathfrak F(g,h)
=
\operatorname{Tr}
\left[
\rho(h)^*
(C^*J_2D+D^*J_2C)
\rho(g)
\right]
+
e_{end}(g,h).
}
\]

## Positive regulated realization

A relative feature is **positively realizable** if there are finite regulators `Z_r` such that

\[
C Z_r,

\qquad
D Z_r
\]

are ordinary Hilbert--Schmidt feature rows and

\[
\boxed{
\Phi_r(g)
=(CZ_r\rho(g),
DZ_r\rho(g))
}
\]

has an ordinary positive Hilbert norm at every `r`.

The common-row norm may diverge as `r->infinity`. Only the cross trace is required to converge.

This records positivity before relative cancellation.

## Tate--Hardy instance

Let

\[
F_T
=(Q^T,
I-Q^T),
\]

\[
F_0
=(Q^0,
I-Q^0).
\]

Define

\[
\boxed{
C
=
\frac12
(F_T+F_0),
\qquad
D
=
\frac12
(F_T-F_0).
}
\]

Then

\[
C^*C+D^*D=I
\]

and

\[
\boxed{
C^*J_2D+D^*J_2C
=Q^T-Q^0.
}
\]

For Mellin observer representation

\[
\rho(g)
=M_{m_g},
\]

two-sided Schwartz localization gives

\[
D\rho(g)
\in\mathcal S_2
\]

and

\[
\rho(h)^*
(Q^T-Q^0)
\rho(g)
\in\mathcal S_1
\]

on the regular sector.

Hence this is a relative positive feature.

## Cutoff recentering

At cutoff `L`, let

\[
U_L
=M_{e^{2iLs}}.
\]

The Tate/reference rows are conjugated by the same `U_L`. A recentering morphism sends

\[
(C_L,D_L)
\]

to

\[
(C_0,D_0)
\]

by `U_L` on source and both target polarities.

For the difference row this is exact in `S_2`:

\[
\boxed{
(U_L\oplus U_L)^*
D_L\rho(g)
U_L
=D_0\rho(g).
}
\]

For the common row it is exact as a bounded module identity.

## Morphisms

A morphism

\[
(V,W):
(C,D,J)
\longrightarrow
(C',D',J')
\]

consists of source and target unitaries satisfying

\[
WJ=J'W,
\]

\[
WC=C'V,
\]

\[
WD=D'V,
\]

and intertwining the observer representations.

Then

\[
q_\mathfrak F(g,h)
=q_{\mathfrak F'}(Vg,Vh).
\]

Composition is ordinary unitary composition and is strictly associative.

## Isometric refinements

More generally, a refinement morphism may use a target isometry `W` with

\[
W^*W=I,
\]

\[
W^*J'W=J.
\]

The dyadic defect splitting maps satisfy exactly these identities when every descendant slot inherits its parent sign.

Therefore dyadic Halmos refinements are morphisms of relative positive features.

## Conductor restriction

Conductor projections commute with `Q^T,Q^0`, the common translation, and the Tate multiplier decomposition. Restriction to conductor level `F` sends

\[
(C,D)
\]

to

\[
(CZ_F,DZ_F).
\]

For `F<=F'`, orthogonal inclusion gives a strict refinement morphism. The conductor-filtered system is therefore internal to the relative feature category.

## Ordered-placement enhancement

To retain Connes's left cutoff, double the relative feature in the placement coordinate:

\[
\boxed{
\mathfrak F^{ord}(g)
=
\frac1{\sqrt2}
(
the feature on }P\rho(g),
\text{the feature on }\rho(g)).
}
\]

The off-diagonal placement involution gives the Hermitian readout

\[
\frac12
(P\Delta Q+
\Delta QP),
\]

and its skew companion gives

\[
\frac1{2i}
[P,
\Delta Q].
\]

The latter vanishes at the boundary under the trace-class/Riemann--Lebesgue placement theorem.

## Boundary evaluation functor

Define a partial boundary evaluation on relative features whose cross operators are trace class:

\[
\boxed{
\operatorname{Obs}_4(\mathfrak F)
=q_\mathfrak F.
}
\]

For the Tate--Hardy feature,

\[
\boxed{
\operatorname{Obs}_4(\mathfrak F_{Tate})(g,h)
=
\sum_\chi
\frac1{2\pi i}
\int
\overline{m_{h,\chi}}
m_{g,\chi}
\partial_s\log\gamma_\chids
+
E_{end}(g,h).
}
\]

By the local Tate identity, this is `W_S(g*h*)`.

## Positivity semantics

The word “positive” refers to the regulated carrier and its ordinary norm:

\[
\|CZ_r\rho(g)\|_2^2
+
\|DZ_r\rho(g)\|_2^2
\ge0.
\]

The limiting observation `q_F` is signed because it uses the bounded fundamental symmetry in an off-diagonal cross pairing.

Thus the construction does not assert positivity of the Weil form.

## Relative null equivalence

Two relative presentations are observationally equivalent if their cross forms agree on `E`:

\[
\boxed{
(C,D)
\sim
(C',D')
}
\]

when

\[
C^*JD+D^*JC
=C'^*J'D'+D'^*J'C'
\]

as source forms, including endpoint rows.

This equivalence permits changing regulator presentation or adding balanced common rows without changing the boundary observation.

It does not identify their ordinary positive norms.

## Composition warning

Arbitrary relative correspondences cannot be composed by multiplying trace-class cross operators alone; source labels and common-module actions must be retained. The admitted morphisms above are unitary/isometric intertwiners, for which composition is well defined.

This restricted category is sufficient for:

- cutoff recentering;
- angular direct sums;
- conductor inclusions;
- dyadic depth refinements;
- polarity exchange.

## `C_34` filler

The completed semilocal boundary edge is represented by

\[
\boxed{
\mathfrak F_{34,S}
=(C_S,D_S,J_2,\operatorname{Tr}_{rel})
}
\]

with ordered-placement doubling when comparing directly to Connes's product cutoff.

Its properties are:

1. finite-regulator ordinary positivity;
2. exact Tate/reference common-difference decomposition;
3. Hilbert--Schmidt relative difference legs;
4. trace-class observer cross contractions;
5. exact cutoff recentering of the difference leg;
6. vanishing placement-commutator boundary channel;
7. Tate logarithmic-derivative signed observation;
8. strict conductor and dyadic refinement coherence.

## Macro and microscopic dimensions

Before ordered-placement doubling, the concrete presentation has four projection/complement legs, or two common/difference rows after rotation.

With ordered-placement doubling it has eight macro legs, or four rotated module/difference rows.

Each row can be refined into exact Halmos atoms and countably many dyadic defect slots. Thus the object is finite in macro-width and countably filtered in microscopic depth.

## Remaining analytic qualifications

The relative filler is complete on the Bruhat--Schwartz observer core in the iterated regulator order, subject to:

1. exact source normalization of local gamma factors and endpoints;
2. the declared smooth/polynomial symbol estimates;
3. finite or summable angular support;
4. physical-to-Hardy unitary transport.

A simultaneous all-regulator limit or an ordinary finite-norm Hilbert completion remains stronger and is not part of this relative category.

## Disposition

The positive `C_34` construction is well typed as a relative positive feature:

\[
\boxed{
\text{bounded common module}
+
\text{Hilbert--Schmidt difference row}
+
\text{trace-class cross readout}.
}
\]

This category supports exact cutoff recentering, conductor filtration, and sign-preserving dyadic refinement. It is the natural terminal home for the regulator-relative eight-leg filler when raw positive Hilbert legs diverge.
