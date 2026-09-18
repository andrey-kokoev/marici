# A canonical pre-G4 tail edge and positive Green face

## Orientation correction

The positive-face orientation asserted below is conditional on a consistent tail-flow convention. The subsequently discovered mismatch between the published integral and differential equation is recorded in `correction-the-published-tail-integral-solves-the-opposite-signed-flow-equation.md`; until repaired, only the algebraic forcing Gram factorization is certified.

## Purpose

This packet defines the strongest coherence edge that can be formed from the currently source-derived analytic data. It does not rename that edge `U_G4` and does not assign the missing arithmetic labels by fiat.

## Analytic carrier

Let

\[
H=L^2(0,\infty),\qquad D=H^1(0,\infty)\cap H.
\]

For each spectral parameter \(z\), define the doubled tail-history fiber

\[
\mathcal S_z^{\rm tail}
=\{(f^+,f^-,G^+,G^-)\in H^2\oplus D^2:
(\partial_q+z)G^\pm=-f^\pm\}.
\]

Endpoint evaluation \(D\to\mathbb C\) is bounded in the graph norm, so every coordinate below is analytic and typed on this fiber.

## Boundary coordinates

For each sign set

\[
I_z^\pm=\frac{f_z^\pm+G_z^\pm}{\sqrt2},
\qquad
O_z^\pm=\frac{f_z^\pm-G_z^\pm}{\sqrt2}.
\]

Define the incoming and outgoing spaces

\[
\mathcal B_{\rm in}=H\oplus H,
\qquad
\mathcal B_{\rm out}=\mathbb C^2\oplus H\oplus H,
\]

and the source-derived boundary maps

\[
B_z(f^+,f^-,G^+,G^-)=(I_z^+,I_z^-),
\]

\[
A_z(f^+,f^-,G^+,G^-)
=(G^+(0),G^-(0),O_z^+,O_z^-).
\]

The canonical pre-G4 edge is the graph map

\[
R_z^{\rm tail}:\mathcal S_z^{\rm tail}
\longrightarrow
\mathcal B_{\rm in}\oplus\mathcal B_{\rm out},
\qquad
s\longmapsto(B_zs,A_zs).
\]

Retaining both coordinates makes this map source-faithful. No inverse or scattering operator \(B_zs\mapsto A_zs\) is asserted without a uniqueness theorem for the source boundary problem.

## Positive Green face

Give the boundary sum the Krein form

\[
J=\begin{pmatrix}-I_{\mathcal B_{\rm in}}&0\\0&I_{\mathcal B_{\rm out}}\end{pmatrix}.
\]

For histories \(s_z\in\mathcal S_z^{\rm tail}\) and \(s_w\in\mathcal S_w^{\rm tail}\), integration of the two tail equations gives

\[
\langle R_w^{\rm tail}s_w,
J R_z^{\rm tail}s_z\rangle
=(z+\bar w)
\left(
\langle G_w^+,G_z^+\rangle_H+
\langle G_w^-,G_z^-\rangle_H
\right).
\]

Thus

\[
K_{\rm tail}(w,z)=
\langle G_w^+,G_z^+\rangle_H+
\langle G_w^-,G_z^-\rangle_H
\]

is the analytically formed positive shape. It is strictly positive on every nonzero doubled tail state.

## Lattice placement

Introduce the distinct predicates

- \(t\): the doubled tail carrier and graph map \(R_z^{\rm tail}\) exist;
- \(g\): the polarized Green face above holds;
- \(a\): a source-authorized arithmetic labelling/sewing map from these boundary coordinates to the declared G4 ports exists;
- \(u\): the authoritative `U_G4` exists in that same labelled target;
- \(c\): the comparison with `T_PB` is formed and coherent.

The present construction establishes

\[
(t,g,a,u,c)=(1,1,0,0,\bot).
\]

The old three-coordinate projection remains \((u,r,c)=(0,0,\bot)\), because \(R_z^{\rm tail}\) has target \(\mathcal B_{\rm in}\oplus\mathcal B_{\rm out}\), not the undeclared `U_G4` target.

## Exact remaining extension

**Refinement.** The idelic Fourier sewing core `J0` already exists algebraically; see `correction-the-arithmetic-sewing-core-exists-and-the-missing-edge-is-the-tail-to-idelic-trace-interface.md`. What is absent is the typed tail-to-trace interface and the authoritative G4 readout. The following direct map notation abbreviates that composite.

A future arithmetic sewing map must have the explicit type

\[
S_{\rm ar}:\mathcal B_{\rm in}\oplus\mathcal B_{\rm out}
\longrightarrow U_{G4},
\]

with declared primitive, square, seam, archimedean, reciprocal, and linking coordinates, pairings, and basis order. Only then may one define

\[
R_z=S_{\rm ar}\circ R_z^{\rm tail}
\]

and test the comparison face against `T_PB`.

## Claim boundary

This packet analytically forms the tail-level coherence edge and its positive Green face. It does not construct the arithmetic sewing map, authorize `U_G4`, prove complete-port conservation at Xi zeros, or imply RH.
