# Global positive reference-edge removal is equivalent to relative lower semiboundedness of the Tate connection

## Idealized common-edge model

Let `H_0` be the positive observer source Hilbert space. Suppose the reference positive edge Gram at cutoff scale `L` is

\[
\boxed{
G_L^0
=LG_{edge},
}
\]

where `G_edge` is a fixed positive closed form.

Suppose the Tate-scattered positive Gram differs by the self-adjoint Tate connection form `A`:

\[
\boxed{
G_L^T
=LG_{edge}+A.
}
\]

Thus the signed relative form is

\[
D_L
=G_L^T-G_L^0
=A.
\]

This is the exact model suggested by a common Widom leading term and finite Tate relative correction.

## Jordan reference removal

The finite-packet common-edge formula gives

\[
C_L
=G_L^T-A_+
=G_L^0-A_-.
\]

Hence globally

\[
\boxed{
C_L
=LG_{edge}-A_-.
}
\]

Therefore a global common positive feature exists at cutoff `L` exactly when

\[
\boxed{
A_-
\preceq
LG_{edge}.
}
\]

This is a relative lower-semiboundedness condition on `A`.

## Plancherel edge

If

\[
G_{edge}=I
\]

in the Mellin--Plancherel carrier, the condition becomes

\[
\boxed{
A_-
\le
LI.
}
\]

Equivalently,

\[
\boxed{
A
\ge
-LI.
}
\]

Thus global positive reference removal at some finite cutoff is possible precisely when the Tate connection is bounded below.

If

\[
\inf\operatorname{spec}A
=-\infty,
\]

then for every finite `L` there are source vectors satisfying

\[
\langle g,
A_-g\rangle
>
L\|g\|^2,
\]

and consequently

\[
C_L(g,g)<0.
\]

No global common positive Gram can then be obtained by this orientation of Jordan edge removal.

## Opposite orientation

If the relative convention is reversed,

\[
G_L^0-G_L^T
=A,
\]

then the common Gram becomes

\[
C_L
=LG_{edge}-A_+.
\]

Global positivity requires an upper bound

\[
\boxed{
A_+
\preceq
LG_{edge}.
}
\]

Thus changing polarity exchanges lower-semiboundedness with upper-semiboundedness. It does not remove the global spectral issue.

## General relative form criterion

Let `q_edge` be a positive closed form with domain `D_edge`, and let `q_A` be a symmetric form on the same core. Write the Jordan forms `q_(A,+/-)` when they are defined by a self-adjoint operator in the `q_edge` carrier.

The exact criterion is

\[
\boxed{
q_{A,-}(g)
\le
Lq_{edge}(g)

\qquad
\text{for all }g\in D_{edge}.
}
\]

Equivalently, the negative part has relative bound at most `L` with no additive `L2` remainder.

If only

\[
q_{A,-}(g)
\le
aq_{edge}(g)
+b\|g\|^2
\]

is known, enlarge the reference feature by an additional Plancherel bulk `b I`; then positivity holds for `L>=a` in the augmented edge metric.

## Tate multiplication operator

For the semilocal Tate boundary,

\[
A_S
=
\bigoplus_\chi
M_{w_\chi},
\qquad
w_\chi(s)
=
\frac1i
\partial_s
\log\gamma_\chi(s).
\]

With Plancherel edge metric, the lower-semiboundedness test is concrete:

\[
\boxed{
\operatorname*{essinf}_{\chi,s}
w_\chi(s)
>-\infty.
}
\]

If the endpoint-normalized symbols satisfy

\[
w_\chi(s)
\ge
-C_S
\]

uniformly in all angular characters and spectral parameters, then

\[
A_{S,-}
\le
C_SI
\]

and every cutoff with `L>=C_S` admits the global common-edge decomposition.

If the essential infimum tends to `-infinity` along characters or spectral parameters, the Plancherel common-edge construction fails globally.

## Characterwise bounds are not enough without uniformity

For each fixed character `chi`, one may have

\[
w_\chi(s)
\ge
-C_\chi.
\]

This only proves positivity on finite angular truncations. Global removal requires

\[
\boxed{
\sup_\chi
C_\chi
<\infty
}
\]

or a stronger edge metric carrying angular weights that dominate `C_chi`.

Rapid decay of each fixed smooth observer does not create one global positive Gram on the completed Plancherel space; it merely places that observer in the form domain.

## Why finite packets always succeed eventually

On a finite packet `E_0`, the compression

\[
A|_{E_0}
\]

is a bounded matrix. Therefore

\[
(A|_{E_0})_-
\le
C(E_0)G_{edge}|_{E_0}
\]

whenever the compressed edge form is nondegenerate.

Choosing

\[
L>C(E_0)
\]

makes the common Gram positive. The threshold depends on the packet and may diverge as packets explore increasingly negative spectral regions.

This explains exactly why packetwise positive fillers do not automatically globalize.

## Weighted edge repair

If `A_S` is not bounded below in Plancherel norm, define a stronger positive edge metric

\[
\boxed{
G_{edge}^{weighted}
=I+A_{S,-}.
}
\]

Then

\[
A_{S,-}
\preceq
G_{edge}^{weighted}.
\]

A common positive decomposition exists for `L>=1` in this graph carrier.

However, this repair is valid physically only if the observer-weighted Widom leading Gram actually converges to the same weighted edge form. One cannot choose the stronger metric solely to force positivity; it must be produced by the cutoff asymptotic.

## Endpoint sector

If `w_chi` has negative singularities caused by a branch/pole convention, first separate the finite-dimensional or graph endpoint channel prescribed by the local Tate identity. The semiboundedness test should be applied to the regular multiplication part after endpoint extraction.

Failure to separate endpoints can falsely report an unbounded negative spectral tail that belongs to a distinct boundary summand.

## Global feature when the criterion holds

Assume

\[
A_-
\preceq
LG_{edge}.
\]

Then define the common edge form

\[
C_L
=LG_{edge}-A_-
\succeq0.
\]

The two positive feature Grams decompose as

\[
\boxed{
G_L^T
=C_L+A_+,
}
\]

\[
\boxed{
G_L^0
=C_L+A_-.
}
\]

Removing the common feature `C_L^(1/2)` leaves the global coherent Tate boundary legs

\[
\boxed{
(A_+^{1/2},
A_-^{1/2}).
}
\]

Because the construction uses global spectral calculus before packet restriction, all packet-successor cells commute exactly.

## Approximate asymptotics

For actual regulators, write

\[
G_\Lambda^T
=L_\Lambda G_{edge}
+A
+R_\Lambda^T,
\]

\[
G_\Lambda^0
=L_\Lambda G_{edge}
+R_\Lambda^0.
\]

A global positive decomposition requires remainder bounds in the same form order, not merely pointwise convergence:

\[
\boxed{
\pm R_\Lambda^{T,0}
\preceq
\epsilon_\Lambda
(G_{edge}+|A|),

\qquad
\epsilon_\Lambda
\to0.
}
\]

Scalar matrix-coefficient convergence on each observer does not imply these inequalities.

## Exact analytic acceptance test

For the semilocal Tate symbols, determine:

1. the regularized real multiplier `w_chi(s)` in the exact Connes normalization;
2. its essential lower bound after endpoint extraction;
3. whether the bound is uniform in `chi`;
4. the actual operator-valued Widom edge metric;
5. form-order control of regulator remainders.

Then:

- a uniform lower bound closes the global positive reference-removal gate in the displayed orientation;
- an unbounded negative tail proves that only packetwise/filtered positive fillers exist for a Plancherel edge;
- a weighted physical edge law may repair the latter case.

## Disposition

The global common-edge condition is

\[
\boxed{
A_{S,-}
\preceq
L_\LambdaG_{edge}.
}
\]

For a Plancherel edge, this is exactly uniform lower-semiboundedness of the Tate logarithmic derivative. The next computation is therefore not another abstract coherence argument: it is the characterwise lower-bound analysis of `(1/i) partial_s log gamma_chi` with endpoint terms separated.
