# Hadamard rotation separates the four-leg feature into common volume and trace-ideal difference rows

## Two projection features

For the Tate and reference projections, define

\[
F_Tx
=(Q^Tx,
(I-Q^T)x),
\]

\[
F_0x
=(Q^0x,
(I-Q^0)x).
\]

Both are isometries:

\[
F_T^*F_T
=F_0^*F_0
=I.
\]

The four-leg feature is

\[
\Psi x
=
\frac1{\sqrt2}
(F_Tx,
F_0x).
\]

Its signed involution is

\[
J_4
=
\operatorname{diag}(J_2,-J_2),

\qquad
J_2
=
\operatorname{diag}(I,-I).
\]

## Hadamard rotation

Apply the unitary Hadamard transform to the Tate/reference coordinate. Define

\[
\boxed{
C x
=
\frac12
(F_T+F_0)x,
}
\]

\[
\boxed{
D x
=
\frac12
(F_T-F_0)x.
}
\]

The rotated positive feature is

\[
\boxed{
\Psi^{rot}x
=(Cx,
Dx).
}
\]

Since the rotation is unitary,

\[
\boxed{
C^*C+D^*D
=I.
}
\]

Thus no positive mass is lost.

## Explicit common and difference rows

Let

\[
\Delta Q
=Q^T-Q^0.
\]

Then

\[
\boxed{
Dx
=
\frac12
(\Delta Qx,
-\Delta Qx).
}
\]

Hence

\[
\boxed{
D^*D
=
\frac12
(\Delta Q)^2.
}
\]

The common row is

\[
\boxed{
Cx
=
\frac12
((Q^T+Q^0)x,
(2I-Q^T-Q^0)x).
}
\]

It contains the shared source-volume component.

## Signed involution after rotation

Under the same Hadamard transform,

\[
J_4
\]

becomes off-diagonal:

\[
\boxed{
J_4^{rot}
=
\begin{pmatrix}
0&J_2\\
J_2&0
\end{pmatrix}.
}
\]

Therefore

\[
\begin{aligned}
(\Psi^{rot})^*
J_4^{rot}
\Psi^{rot}
&=
C^*J_2D
+D^*J_2C\\
&=
Q^T-Q^0.
\end{aligned}
\]

Thus

\[
\boxed{
C^*J_2D
+D^*J_2C
=
\Delta Q.
}
\]

The relative current is a cross pairing between common and difference rows.

## Difference row is observer-localized Hilbert--Schmidt

For an observer multiplier `M_m`,

\[
DM_m
=
\frac12
(\Delta Q M_m,
-\Delta Q M_m).
\]

The observer-localized relative projection block satisfies

\[
\Delta Q M_m
\in
\mathcal S_2
\]

under the characterwise divided-difference/Hankel estimate. Therefore

\[
\boxed{
DM_m
\in
\mathcal S_2,
}
\]

with

\[
\boxed{
\|DM_m\|_2^2
=
\frac12
\|\Delta Q M_m\|_2^2.
}
\]

This norm remains finite after removing the outer center-volume regulator for every fixed cutoff and Schwartz observer.

## Common row remains volume divergent

The common row is asymptotic to either projection feature and retains the identity Gram:

\[
C^*C
=I-
\frac12(\Delta Q)^2.
\]

For a non-Hilbert--Schmidt convolution observer,

\[
CM_m
\]

is not Hilbert--Schmidt on the full noncompact carrier. Its regulated norm diverges with source volume.

Thus the Hadamard rotation isolates divergence in `C` and finite relative variation in `D`.

## Relative pairing is finite

Although `C M_m` need not be Hilbert--Schmidt, the signed cross expression can be rearranged into observer-sandwiched relative operators:

\[
\boxed{
M_{m_h}^*
(C^*J_2D+D^*J_2C)
M_{m_g}
=
M_{m_h}^*
\Delta Q
M_{m_g}.
}
\]

The right side is trace class after two-sided Schwartz localization and endpoint separation.

Therefore the cross pairing is well defined as a relative trace even though the two common-row vectors do not individually have finite Hilbert--Schmidt norm.

## Relative Hilbert-module interpretation

The correct completion consists of:

1. a common multiplier/module row `C` retained only relatively;
2. a Hilbert--Schmidt difference row `D M_m`;
3. the bounded off-diagonal involution `J_4^(rot)`;
4. a trace-class cross contraction.

Symbolically,

\[
\boxed{
\text{common module}
\overset{J_2}{\longleftrightarrow}
\text{Hilbert--Schmidt relative difference}.
}
\]

This is not an ordinary direct-sum Hilbert vector after regulator removal, but it is a well-defined relative correspondence.

## Ordered eight-leg version

The eight-leg feature adds the observer-placement coordinate `PA` versus `A`. Apply the Hadamard rotation independently in both four-leg blocks.

This produces:

- common rows `C(PA)` and `C(A)`;
- difference rows `D(PA)` and `D(A)`;
- off-diagonal pairings in both Tate/reference and placement coordinates.

The Hermitian readout remains

\[
\frac12
(P\Delta Q+
\Delta QP),
\]

and the skew readout remains

\[
\frac1{2i}
[P,
\Delta Q].
\]

All finite identities are preserved because the rotation is unitary.

## Dyadic refinement

Dyadic Halmos refinement may be applied before or after Hadamard rotation. Before rotation it refines each projection/complement row. After rotation, it refines the corresponding common/difference combinations.

Since both operations are isometries on the finite regulated carrier, the two routes are unitarily equivalent and all signed readouts agree.

Thus the relative-module decomposition is compatible with the countable prolate refinement.

## Minimal positive relative norm

The positive norm of the difference row is

\[
\boxed{
q_D(g)
=
\frac12
\|\Delta Q M_{m_g}\|_2^2.
}
\]

This is an unconditional positive relative quantity. It measures the Hilbert--Schmidt distance between the Tate and reference projection features.

It is not the absolute Weil form `|A_S|`. The Tate current is the cross pairing with the common row, not the norm square of `D` alone.

Cauchy--Schwarz in a valid localized factorization gives bounds on the relative trace in terms of `q_D` and an observer boundary norm, but does not force Weil positivity.

## Regulator convergence

At finite outer regulator, both `C` and `D` are ordinary Hilbert--Schmidt feature rows. As the regulator is removed:

- `D` converges in Hilbert--Schmidt norm when the localized relative projection estimate is uniform;
- `C` does not converge in Hilbert--Schmidt norm;
- the cross trace converges by trace-class localization;
- the signed boundary form converges to the Tate logarithmic derivative.

This is the precise relative convergence pattern sought by the earlier raw-leg divergence audit.

## Endpoint/index component

If

\[
\Delta Q
=
\Delta Q^{regular}
+
\Delta Q^{index},
\]

then the difference row splits correspondingly. The index part is finite rank and belongs to the finite Hilbert difference sector. Its cross pairing with the common row produces the endpoint/winding contribution.

Thus endpoint data are retained without forcing the entire common row into Hilbert--Schmidt class.

## Categorical object

The Hadamard-rotated filler is naturally an arrow in a relative correspondence category:

\[
\boxed{
(C,D,
J_4^{rot},
\operatorname{Tr}_{rel}).
}
\]

Composition retains the common module label and composes trace-ideal differences. It should not be collapsed to the difference row alone, because doing so loses the linear Tate current.

## Comparison with common-Gram subtraction

The finite-packet Jordan construction removes a common positive Gram and leaves minimal positive/negative legs. The Hadamard rotation instead keeps the common feature formally and isolates a trace-ideal difference.

Advantages of the relative version:

- exact at every regulator;
- no finite-packet coercivity threshold;
- no semiboundedness assumption;
- packet and conductor compatibility inherited from the global projections.

Cost:

- no ordinary finite norm for the common row;
- the boundary is a cross form, not a standalone positive Gram.

## Disposition

The four-leg feature has the exact common/difference decomposition

\[
\boxed{
C
=
\frac12(F_T+F_0),
\qquad
D
=
\frac12(F_T-F_0),
}
\]

with

\[
\boxed{
C^*C+D^*D=I,
\qquad
C^*J_2D+D^*J_2C
=Q^T-Q^0.
}
\]

After observer localization, `D` is Hilbert--Schmidt while `C` retains divergent common volume. The Tate boundary is their finite relative cross pairing. This supplies the concrete regulator-relative positive completion required when raw positive legs cannot converge.
