# The translated theta history must remain bivariate until after Stokes descent

## The current mismatch

After two-ray restriction and half-density transport, a translated Gaussian
front has the form

\[
F_{n,\pm}(u,t)
=
\sqrt n\,e^{u/2}
e^{-\pi(ne^u\pm t)^2}.
\]

The centered theta Gaussian is only the slice

\[
F_{n,\pm}(u,0)
=
\sqrt n\,e^{u/2}e^{-\pi n^2e^{2u}}.
\]

The adjacent window boundary, however, depends on the full path
\(t\in[L,2L]\). Replacing the path by its centered slice before taking the
boundary erases the constructor that distinguishes \(W_L\) from \(W_{2L}\).

## Exact bivariate Stokes identity

Because the two-ray and half-density maps are independent of \(t\),

\[
\partial_t\mathcal T_nW_t
=
\mathcal T_n\partial_tW_t.
\]

Hence

\[
\mathcal T_n(W_{2L}-W_L)
=
\int_L^{2L}
\partial_t\mathcal T_nW_t\,dt.
\]

This is already the required linear Adams comparison, but it lives in a
bivariate history carrier with coordinates \((u,t)\).

Define

\[
\mathcal H_{n,L}
=
H^1\bigl([L,2L]_t;\mathcal K_n(u)\bigr),
\]

where \(\mathcal K_n\) is the appropriate half-density theta fiber. The
endpoint trace

\[
\Gamma_tF=(F(\cdot,L),F(\cdot,2L))
\]

and the oriented boundary

\[
\partial_t^{\mathrm{cell}}F
=
F(\cdot,2L)-F(\cdot,L)
\]

then preserve the source identity exactly.

## Centering does not commute with boundary

Let \(C_0F=F(\cdot,0)\) denote centered evaluation whenever it is defined.
For a cell with \(L>0\),

\[
C_0\partial_t^{\mathrm{cell}}F
\]

is not even typed as evaluation of the two endpoints, while

\[
\partial_t^{\mathrm{cell}}C_0F=0
\]

because \(C_0F\) has no remaining \(t\)-dependence.

Thus

\[
C_0\partial_t^{\mathrm{cell}}
\ne
\partial_t^{\mathrm{cell}}C_0.
\]

Any construction that centers first cannot recover the adjacent-cell
boundary.

## No rank-one centered compression

Suppose a linear compression

\[
C:\mathcal H_{n,L}\to\mathcal K_n
\]

factors through one centered theta channel and is independent of the
endpoints. If it annihilates every \(t\)-derivative after centering, then

\[
C\left(
F(\cdot,2L)-F(\cdot,L)
\right)=0.
\]

But the raw window disagreement is nonzero. Therefore no such rank-one
centered compression can intertwine the full Adams boundary.

The comparison needs either:

1. the full bivariate history until Stokes descent; or
2. a finite jet system rich enough to retain the endpoint difference.

The explicit prime-two computation shows that at least four Gaussian grades
occur, so the earlier three-grade centered packet is insufficient.

## Correct order of constructors

The source-authorized order is:

\[
\text{translated two-ray fronts}
\longrightarrow
\text{bivariate half-density history}
\longrightarrow
\text{oriented \(t\)-boundary}
\longrightarrow
\text{theta label sum}
\longrightarrow
\text{completion differential}
\longrightarrow
\text{relative Green quotient}.
\]

Centering may occur only after the oriented boundary has been represented in a
sufficient endpoint-jet carrier.

This removes the apparent need for an unexplained direct map from translated
fronts to a centered theta scalar.

## Green polarization

On the bivariate graph space, the natural form includes both derivatives:

\[
\|F\|_{\mathrm{bi}}^2
=
\int_L^{2L}
\left(
\|F(t)\|_{\mathcal K_n}^2
+
\|\partial_tF(t)\|_{\mathcal K_n}^2
+
\|\partial_uF(t)\|_{\mathcal K_n}^2
\right)\,dt,
\]

with the exact source weights still to be frozen.

The two-lift Green identity should first be proved here. The centered
Wronskian and tail/PV ports are then traces or Schur reductions of this
bivariate form, not replacements for it.

## Prime-two consequence

For \(p=2\), the source packet contains four grades

\[
\frac12,\quad
\frac32,\quad
\frac52,\quad
\frac72.
\]

These are the finite jet shadow of the translated \(t\)-history. The
\(f_3\) grade is precisely the first hostile to premature three-grade
centering.

The smallest executable checker should therefore compare:

- the exact bivariate endpoint difference;
- its four-grade jet at one label;
- the image after the completion differential;
- the relative Green boundary.

Agreement only after scalar integration is insufficient.

## Completion

Prime labels remain external and the half-density maps are isometric.
Consequently the bivariate enlargement does not by itself create cross-prime
mixing.

Completion needs:

- a common bivariate graph core;
- labelwise Stokes continuity;
- summability after Euler coefficients;
- preservation of the four-grade endpoint jet;
- a closed descent to the relative Green quotient.

The existing \(p^{-3/2-\sigma}\) mixed coefficient budget absorbs the
logarithmic history length.

## Hostiles

1. Evaluate at \(t=0\) before taking the adjacent boundary.
2. Replace the two translated rays by their sum and erase odd orientation.
3. Keep only three centered Gaussian grades at \(p=2\).
4. Match the scalar endpoint integral while losing a nonzero bivariate
   boundary vector.
5. Prove finite-label Stokes identities without a common completed graph
   domain.

## Verdict

The missing Adams comparison is not a mysterious map from translated windows
to one centered theta history. Such a rank-one compression cannot preserve the
adjacent boundary.

The correct common carrier is the bivariate translated theta history. On that
carrier the linear Stokes identity is exact. The next theorem is its fully
polarized Green closure and the source-authorized descent of its four-grade
endpoint jet to the completed relative boundary.
