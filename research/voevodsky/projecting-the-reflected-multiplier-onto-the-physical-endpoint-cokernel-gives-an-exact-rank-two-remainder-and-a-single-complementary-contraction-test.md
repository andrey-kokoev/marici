# Projecting the reflected multiplier onto the physical endpoint cokernel gives an exact rank-two remainder and a single complementary contraction test

## Finite-window setting

Work first on a finite Paley--Wiener or regularized Hardy carrier `H_L`, where the reflected multiplier operator

\[
T_{S,L}=M_{\Theta_S}^*
\]

is bounded. The canonical signed kernel form is

\[
Q_{S,L}(f)
=
\|f\|^2-
\|T_{S,L}f\|^2.
\]

Let `E_L` be the physical endpoint harmonic space

\[
E_L=
\operatorname{span}
\{e^{x/2},e^{-x/2}\},
\]

transported into the target space of `T_S` by the fixed Fourier/Paley--Wiener identification. Let

\[
P_{end,L}:H_L\to E_L
\]

be its orthogonal projection and put

\[
P_{bulk,L}=I-P_{end,L}.
\]

## Exact orthogonal decomposition

Define

\[
R_{end,S,L}=P_{end,L}T_{S,L},
\]

\[
R_{bulk,S,L}=P_{bulk,L}T_{S,L}.
\]

Because the two target ranges are orthogonal,

\[
\boxed{
\|T_{S,L}f\|^2
=
\|R_{bulk,S,L}f\|^2
+
\|R_{end,S,L}f\|^2.
}
\]

Therefore

\[
\boxed{
Q_{S,L}(f)
=
G_{S,L}(f)
-
\|R_{end,S,L}f\|^2,
}
\]

where

\[
\boxed{
G_{S,L}(f)
=
\|f\|^2-
\|R_{bulk,S,L}f\|^2.
}
\]

The remainder has rank at most two because `ran R_end,S,L subset E_L`.

This is an exact Hilbert-space reduction of the full reflected feature to a bulk term plus the chosen physical endpoint subspace, with no cross term. Identifying its induced rank-two norm with the source swap-polarized endpoint form still requires the source normalization/intertwiner; the Hilbert projection alone does not supply the Krein signs.

## The single common-bulk condition

The bulk form `G_S,L` is positive if and only if

\[
\boxed{
\|P_{bulk,L}M_{\Theta_S}^*f\|
\le
\|f\|
\qquad
\text{for all }f\in H_L.
}
\]

Equivalently,

\[
\boxed{
M_{\Theta_S}
P_{bulk,L}
M_{\Theta_S}^*
\preceq I.
}
\]

Thus global Schur contractivity of `Theta_S` is stronger than necessary. The reflected multiplier may expand in the two endpoint directions; only its compression to the orthogonal endpoint complement must be contractive.

This is exactly the weaker, source-derived compression sought in the previous de Branges audit.

## Completed positivity criterion

Once `G_S,L>=0`, the full form is positive if and only if the endpoint observation is contractive relative to the bulk norm:

\[
\boxed{
\|R_{end,S,L}f\|^2
\le
G_{S,L}(f).
}
\]

Equivalently,

\[
T_{S,L}^*T_{S,L}
\preceq I.
\]

The latter is again full contractivity if required on every `f`. The conceptual gain is not a proof of positivity, but a two-stage localization of its failure:

1. prove unconditional contractivity on the endpoint complement;
2. control the remaining rank-two endpoint map by the positive bulk.

If stage 1 succeeds from semilocal analysis, only the physical endpoint obstruction remains.

## Endpoint parity

Diagonalize

\[
E_L=E_{even,L}
\oplus
E_{odd,L}.
\]

The source endpoint swap form assigns positive sign to the even line and negative sign to the odd line. Accordingly one may refine

\[
R_{end}=R_{even}

\oplus R_{odd}.
\]

The even component can be retained in the positive bulk, leaving only

\[
R_{odd,S,L}=P_{odd,L}T_{S,L}
\]

as the hostile rank-one feature. In the source Krein metric the target form should therefore be organized as

\[
Q_{S,L}
=
G_{even+bulk,S,L}
-
\|R_{odd,S,L}f\|^2.
\]

The exact coefficient must be adjusted by the endpoint Gram eigenvalue

\[
2(\sinh L-L).
\]

Thus functional-equation parity potentially reduces the final obstruction from rank two to rank one.

## Prime transition

For adjoining `q`,

\[
T_{S\cup\{q\},L}
=
M_{\varphi_q}^*T_{S,L},
\qquad
\varphi_q=
\frac{m_q^\#}{m_q},
\]

up to the fixed multiplication-order convention. Therefore

\[
R_{bulk,S\cup\{q\},L}
=
P_{bulk,L}M_{\varphi_q}^*T_{S,L},
\]

and similarly for `R_end`.

The endpoint projection is held fixed while every prime modifies both bulk and endpoint components coherently. This prevents the creation of a new endpoint coordinate for each prime.

## Leakage operator

Define the complementary leakage

\[
L_{S,L}
=P_{bulk,L}M_{\Theta_S}^*.
\]

Then the first gate is simply

\[
\boxed{
\|L_{S,L}
\|
\le1.
}
\]

Its defect operator is

\[
D_{S,L}
=
(I-L_{S,L}^*L_{S,L})^{1/2}.
\]

If the gate holds, the positive common bulk is realized by

\[
G_{S,L}(f)=
\|D_{S,L}f\|^2.
\]

The remaining endpoint inequality becomes a Douglas factorization condition:

\[
\boxed{
R_{end,S,L}^*R_{end,S,L}
\preceq
D_{S,L}^2.
}
\]

Equivalently, there exists a contraction `C_S,L` such that

\[
R_{end,S,L}=C_{S,L}D_{S,L}.
\]

This is the exact rank-two Douglas problem requested previously.

## Noncircularity audit

The decomposition itself is unconditional. The two inequalities are not.

If one defines `E_L` as the span of singular vectors of `T_S` with singular value greater than one, then complementary contractivity holds tautologically, but the endpoint identification becomes fitted and circular.

The only admissible projection is the source-fixed harmonic endpoint space

\[
E_L=
\ker(\partial_x^2-\tfrac14)^*.
\]

Proving

\[
\|P_{bulk,L}M_{\Theta_S}^*\|
\le1
\]

for this fixed projection is a genuine theorem. It says that every expansive direction of the reflected multiplier is physically endpoint-harmonic.

## Relation to Suzuki

Suzuki's conjugate-Toeplitz leakage has a cokernel `ker L*`. The present endpoint projection gives a concrete candidate intertwining equation

\[
\boxed{
\ker L_{S,L}^*

\cong
E_L
=
\operatorname{span}\{e^{x/2},e^{-x/2}\},
}
\]

or its parity-reduced odd line. Equality cannot be inferred from dimensions alone; the source must supply the intertwiner.

## Uniform limit

A global result requires:

\[
\sup_{S,L}
\|P_{bulk,L}M_{\Theta_S}^*\|
\le1,
\]

plus compatible convergence of

\[
D_{S,L},
\qquad
R_{end,S,L},
\qquad
C_{S,L}
\]

under prime and support enlargement. Because endpoint evaluation norms grow exponentially, these operators must be renormalized jointly; separate norm limits need not exist.

## Disposition

The full negative reflected feature now has an exact orthogonal split relative to the source-motivated endpoint projection:

\[
\boxed{
M_{\Theta_S}^*
=
P_{bulk}M_{\Theta_S}^*
+
P_{end}M_{\Theta_S}^*.
}
\]

The first summand yields a positive common bulk precisely when its norm is at most one. The second has rank at most two and is exactly the physical endpoint channel. If complementary contractivity is proved, rung-four positivity reduces to one Douglas domination inequality, rank one after parity reduction.
