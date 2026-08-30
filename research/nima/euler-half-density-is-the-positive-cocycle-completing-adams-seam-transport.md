# Euler half-density is the positive cocycle completing Adams seam transport

## Geometric and weighted incidence

The unweighted prime-power cut atom at grade \(k\) is \(u_{p,k}\) in the cut fiber at

\[
a_{p,k}=k\log p.
\]

Moving-seam transport gives

\[
T_{r a\leftarrow a}u_{p,k}=u_{p,rk}.
\]

The physical incidence includes the Euler coefficient

\[
w_{p,k}=\frac1k p^{-k/2}.
\]

Therefore geometry alone does not intertwine the weighted atoms.

## Coefficient cocycle

Define

\[
\rho_r(p,k)
=
\frac{w_{p,rk}}{w_{p,k}}
=
\frac1r p^{-(r-1)k/2}.
\]

Then weighted incidence satisfies

\[
w_{p,rk}u_{p,rk}
=
\rho_r(p,k)
T_{r a\leftarrow a}
\left(w_{p,k}u_{p,k}\right).
\]

Thus the full Adams lift is the product of:

- unitary moving-seam transport;
- positive coefficient contraction;
- the declared type-fiber map from grade \(k\) to grade \(rk\).

## Cocycle law

For positive integers \(r,s\),

\[
\rho_s(p,k)\rho_r(p,sk)
=
\frac1s p^{-(s-1)k/2}
\frac1r p^{-(r-1)sk/2}
=
\rho_{rs}(p,k).
\]

Together with

\[
T_{rsa\leftarrow sa}T_{sa\leftarrow a}
=
T_{rsa\leftarrow a},
\]

this proves exact composition of the weighted geometric lift.

The coefficient law is a multiplicative cocycle for the Adams monoid action on prime-power labels.

## Additive action cost

Its negative logarithm is

\[
\mathcal E_r(p,k)
=
-\log\rho_r(p,k)
=
\log r+\frac{(r-1)k}{2}\log p.
\]

The cocycle law becomes

\[
\mathcal E_{rs}(p,k)
=
\mathcal E_s(p,k)
+
\mathcal E_r(p,sk).
\]

This is a source-derived additive cost attached to the scale lift. It is not physical time and not a fitted energy. It records loss of coefficient amplitude under passage to a higher prime-power grade.

## Positivity and irreversibility

For \(r>1\),

\[
0<\rho_r(p,k)<1.
\]

Hence Adams grade raising is geometrically unitary but coefficient-contracting. The full weighted lift is a semigroup action, not a group action. There is no source-authorized inverse Adams map on positive prime-power grades.

This distinguishes two structures that scalar Euler notation merges:

- reversible change of cut presentation;
- irreversible decay of Euler half-density.

## Type-fiber requirement

Let \(A_r:T_{p,k}\to T_{p,rk}\) be the Adams fiber map. Full naturality requires

\[
A_{rs}=A_r\!\mid_{(p,sk)}A_s
\]

with the appropriate source and target fibers, and compatibility with typed multiplication.

The scalar cocycle cannot supply \(A_r\). In particular, the transition from primitive to square or connected grade must preserve the declared arithmetic type rather than identify channels with equal scalar frequency.

## Hostile perturbations

A modified coefficient law

\[
\widetilde w_{p,k}
=
\varepsilon_{p,k}w_{p,k}
\]

has cocycle

\[
\widetilde\rho_r(p,k)
=
\frac{\varepsilon_{p,rk}}{\varepsilon_{p,k}}
\rho_r(p,k).
\]

Sign-changing or phase-valued \(\varepsilon\) introduces an additional torsor cocycle. It preserves scalar magnitude while changing orientation. Positive Fock source grammar excludes such a perturbation only when the sign frame and fiber maps are themselves source-authorized.

This provides a finite hostile gate: check whether the extra ratio is a trivial authorized coboundary. If not, the perturbed lift is a different constructor.

## Consequence

The grade-wise weighted Fourier–Poisson/Adams square now commutes at the scalar coefficient and moving-seam levels. The only remaining grade-local datum is the type-fiber Adams map.

Global completion still requires:

- summability of the assembled lift;
- endpoint and archimedean attachment;
- compatibility with the cross-channel Green blocks;
- the completed determinant or ordered-lens closure law.

## Verdict

Euler half-density is exactly the positive cocycle that completes geometric Adams transport. It supplies a source-local monotone law across prime powers, but it does not orient the completed endpoint–archimedean interaction.
