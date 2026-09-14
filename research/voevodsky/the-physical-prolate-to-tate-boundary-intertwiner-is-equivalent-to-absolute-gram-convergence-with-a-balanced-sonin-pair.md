# The physical prolate-to-Tate boundary intertwiner requires absolute-Gram convergence; the proposed Sonin identification needs the complementary tower

## Target boundary feature

On the angular Mellin carrier, let

\[
A_S
=
\bigoplus_\chi
M_{(1/i)\partial_s\log\gamma_\chi}
\]

with form domain

\[
\mathcal D_S
=D(|A_S|^{1/2}).
\]

The canonical two-polarity Tate boundary feature is

\[
\boxed{
F_Sg
=
\left(
A_{S,+}^{1/2}
\mathcal M_Sg,
A_{S,-}^{1/2}
\mathcal M_Sg
\right).
}
\]

Its positive Gram form is

\[
\boxed{
F_S^*F_S
=|A_S|,
}
\]

while its signed Gram form is

\[
\boxed{
F_S^*J F_S
=A_S,
\qquad
J=
\operatorname{diag}(I,-I).
}
\]

## Physical residual feature

Let

\[
R_\Lambda:
\mathcal D_S
\longrightarrow
\mathcal H_\Lambda^{res}
\]

be a proposed orthogonally bulk-removed prolate residual feature. It may contain the completed dyadic defect tower but excludes the explicitly identified volume bulk.

To retain both cutoff polarities, equip the residual carrier with a self-adjoint contraction or fundamental symmetry

\[
J_\Lambda
\]

representing the signed readout.

Define two source forms:

\[
K_\Lambda
=R_\Lambda^*R_\Lambda
\]

and

\[
C_\Lambda
=R_\Lambda^*J_\Lambda R_\Lambda.
\]

Then

\[
-K_\Lambda
\preceq
C_\Lambda
\preceq
K_\Lambda.
\]

## Signed convergence is only half the theorem

The centered regulator comparison proves matrix coefficients of

\[
\boxed{
C_\Lambda
\longrightarrow
A_S
}
\]

on the observer core.

This does not determine `K_Lambda`. Many positive forms can dominate the same signed form. For example,

\[
K_\Lambda
=|C_\Lambda|+D_\Lambda,
\qquad
D_\Lambda\succeq0,
\]

has the same possible signed readout for arbitrary extra positive mass `D_Lambda`.

Thus signed scalar sewing cannot imply convergence of positive residual legs.

## Absolute-Gram acceptance criterion

The exact missing positive theorem is

\[
\boxed{
K_\Lambda(g,h)
\longrightarrow
\langle
\mathcal M_Sg,
|A_S|
\mathcal M_Sh
\rangle
}
\]

on the common form core, with convergence strong enough for the intended completion.

On every finite observer packet, the required strength is operator-norm convergence of Gram matrices. Globally, the natural requirement is Mosco convergence of the closed positive forms `K_Lambda` to the form of `|A_S|`.

This is the **absolute-Gram theorem**.

## Finite-packet intertwiner theorem

Fix a finite packet `E_0` and assume

\[
K_\Lambda|_{E_0}
\to
|A_S||_{E_0}
\]

in matrix norm. Let

\[
K_\Lambda^{1/2},
\bindnasrepma
|A_S|^{1/2}
\]

be the canonical source-coordinate features.

Continuity of positive square roots gives

\[
\boxed{
K_\Lambda^{1/2}
\longrightarrow
|A_S|^{1/2}.
}
\]

The polar decomposition of the physical map `R_Lambda|_(E_0)` supplies a partial isometry

\[
U_\Lambda:
\overline{\operatorname{ran}K_\Lambda^{1/2}}
\to
\overline{\operatorname{ran}R_\Lambda}.
\]

After transporting by `U_Lambda^*`, the physical residual legs converge to the canonical absolute feature. Composing with the spectral sign splitting of `A_S` gives the two Tate boundary legs.

Hence absolute-Gram convergence is sufficient for a packetwise physical intertwiner, up to the uniquely irrelevant unitary freedom on feature ranges.

## Necessity

Conversely, suppose there are isometric transports

\[
V_\Lambda:
\mathcal H_\Lambda^{res}
\to
\mathscr H_S
\oplus
\mathscr H_S
\]

such that

\[
V_\Lambda R_\Lambda g
\longrightarrow
F_Sg
\]

for every vector in a finite packet. Then

\[
\begin{aligned}
K_\Lambda(g,h)
&=
\langle
V_\Lambda R_\Lambda g,
V_\Lambda R_\Lambda h
\rangle\\
&\longrightarrow
\langle F_Sg,F_Sh\rangle\\
&=
\langle
\mathcal M_Sg,
|A_S|\mathcal M_Sh
\rangle.
\end{aligned}
\]

Therefore the absolute-Gram theorem is also necessary.

## Excess positive mass obstruction

Define the formal excess

\[
\boxed{
D_\Lambda
=K_\Lambda-|C_\Lambda|.
}
\]

When `C_Lambda` is represented by a contraction-valued signed readout, one expects `D_Lambda>=0` only under an additional compatibility/dilation hypothesis; it is not automatic from `-K<=C<=K` in noncommuting dimensions.

The invariant statement is instead:

\[
\boxed{
K_\Lambda
\to|A_S|
}
\]

and not positivity of the displayed formal difference.

Any residual mass surviving orthogonally to the source-generated Tate boundary prevents a unitary physical intertwiner.

## Correction: this is not the standard Sonin atom

Let

\[
Z_\Lambda g
=P_{\{1\}}(B_\Lambda)
A_g.
\]

This is the inside--inside intersection feature `ran(P) intersect ran(Q)`, not the standard Sonin feature `ker(P) intersect ker(Q)`. In the ordinary time--band model it vanishes by uncertainty. The standard Sonin atom belongs instead to the complementary contraction `(I-P)(I-Q)(I-P)`. The balanced construction below applies only after replacing `Z_Lambda` by that source-verified complementary atom and proving that its signed readout is zero.

It cannot simply be deleted unless a source theorem proves it vanishes or belongs to the removed bulk.

## Balanced Sonin pair

Retain the Sonin feature by the diagonal embedding

\[
\boxed{
Z_\Lambda g
\longmapsto
\frac1{\sqrt2}
(Z_\Lambda g,
Z_\Lambda g)
}
\]

into one positive and one negative polarity slot.

Its ordinary positive norm is preserved:

\[
\left\|
\frac1{\sqrt2}(Zg,Zg)
\right\|^2
=
\|Zg\|^2,
\]

while its signed readout vanishes:

\[
\boxed{
\left\langle
\frac1{\sqrt2}(Zg,Zg),
J
\frac1{\sqrt2}(Zh,Zh)
\right\rangle
=0.
}
\]

Thus the Sonin atom is represented as balanced positive mass invisible to the signed Tate current.

## Sonin alternatives

The balanced embedding is canonical only if the signed source form annihilates the Sonin sector. Three outcomes remain possible:

1. **null readout:** use the balanced pair above;
2. **endpoint coupling:** map the Sonin sector to an endpoint graph summand with a source-derived signed form;
3. **bulk absorption:** prove the Sonin mass belongs to the orthogonally removed invariant bulk.

The source theorem must select among these. The relative trace alone sees only that no unassigned signed contribution may be invented.

## Revised absolute target with Sonin mass

If the Sonin sector survives as signed-null mass, the full positive limit is not merely `|A_S|`. It is

\[
\boxed{
|A_S|
\oplus
K_{Sonin},
}
\]

where `K_Sonin` has zero signed readout through the balanced two-polarity embedding.

Accordingly, absolute-Gram convergence should be tested after orthogonally separating

\[
R_\Lambda
=
R_\Lambda^{Tate}
\oplus
Z_\Lambda.
\]

The Tate residual must converge to `|A_S|`; the Sonin residual must converge separately or remain as a stable pro-object.

## Relation to the dyadic tower

The infinite dyadic decomposition gives exact positive mass conservation:

\[
\|B^{1/2}A_g\|_{HS}^2
=
\|Z_\Lambda g\|^2
+
\sum_{j\ge0}
\|d_{\Lambda,j}(g)\|^2.
\]

The absolute-Gram theorem asks for a centered/cofinal limit of the defect-cloud Gram

\[
\sum_j
\langle
d_{\Lambda,j}(g),
d_{\Lambda,j}(h)
\rangle
\]

after volume bulk removal, not merely its signed weighted sum.

This is a near-one spectral-measure theorem for the observer-weighted prolate contraction.

## Concrete spectral-measure target

Let

\[
\mu_{\Lambda,g,h}(E)
=
\operatorname{Tr}
\left(
A_h^*
E_{B_\Lambda}(E)
A_g
\right).
\]

The dyadic positive boundary kernel is generated by

\[
\boxed{
\sum_{j\ge0}
B_\Lambda^{2^j}
(I-B_\Lambda^{2^j})
=B_\Lambda-P_{\{1\}}(B_\Lambda).
}
\]

After the required bulk centering, absolute-Gram convergence becomes convergence of the corresponding observer-weighted spectral integrals to the multiplier form of `|A_S|`.

This states the physical problem without a bare transition trace.

## Global version

A global physical intertwiner follows from Mosco convergence

\[
\boxed{
K_\Lambda^{Tate}
\xrightarrow{Mosco}
q_{|A_S|}
}
\]

plus convergence/stability of the balanced Sonin summand. Mosco convergence gives strong resolvent convergence of the associated positive operators and is the appropriate replacement for nonexistent uniform finite-packet coercivity.

## Disposition

The remaining positive `C_34` gate has an exact necessary-and-sufficient formulation:

\[
\boxed{
\text{physical positive boundary intertwiner}
\Longleftrightarrow
\text{absolute-Gram convergence to }|A_S|
}
\]

up to a separately tracked balanced Sonin sector and unitary freedom of feature realizations.

Signed regulator convergence supplies `A_S`; it does not supply `|A_S|`. Determining the rescaled observer-weighted near-one spectral measure is precisely the analytic input needed to prove the absolute-Gram theorem.
