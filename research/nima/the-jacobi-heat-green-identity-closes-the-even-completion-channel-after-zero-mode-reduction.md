# The Jacobi heat Green identity closes the even completion channel after zero-mode reduction

The Jacobi comparison has a canonical positive Green form. On the even
completed channel, closability and radical descent follow directly from the
heat equation.

## Periodic Jacobi rigging

Work on the \(z\)-circle with Fourier series

\[
F(z)=\sum_{k\in\mathbb Z}F_ke^{2\pi ikz}.
\]

For \(s>9/2\), use the Sobolev rigging

\[
H^s(\mathbb T)\subset L^2(\mathbb T)\subset H^{-s}(\mathbb T).
\]

The threshold \(s>9/2\) makes evaluation of derivatives through order four
continuous:

\[
F\longmapsto F^{(j)}(0),
\qquad
0\le j\le4.
\]

The theta sections lie in every such rung for each \(r>0\).

## Heat propagation

Let

\[
P_\rho
=
e^{\frac{\rho}{4\pi}\partial_z^2},
\qquad
\rho\ge0.
\]

On Fourier modes,

\[
(P_\rho F)_k=e^{-\pi\rho k^2}F_k.
\]

Hence \(P_\rho\) is a contraction on every \(H^s\), preserves the constant
mode, and is smoothing for \(\rho>0\).

For the direct sector \(r\ge r_0>0\),

\[
F(r)=P_{r-r_0}F(r_0).
\]

The reciprocal sector is treated after Poisson sewing in the variable \(1/r\);
no backward heat operator is used.

## Polarized heat Green identity

For two heat solutions \(F,G\),

\[
\partial_rF=\frac1{4\pi}\partial_z^2F,
\qquad
\partial_rG=\frac1{4\pi}\partial_z^2G.
\]

Integration by parts on the circle gives

\[
\frac{d}{dr}\langle F(r),G(r)\rangle
=
-\frac1{2\pi}
\langle\partial_zF(r),\partial_zG(r)\rangle.
\]

In particular,

\[
\|F(r_1)\|^2-\|F(r_0)\|^2
=
-\frac1{2\pi}
\int_{r_0}^{r_1}
\|\partial_zF(r)\|^2\,dr.
\]

Thus the heat history has a source-derived positive bulk energy

\[
\mathfrak e_{[r_0,r_1]}(F,G)
=
\frac1{2\pi}
\int_{r_0}^{r_1}
\langle\partial_zF(r),\partial_zG(r)\rangle\,dr.
\]

## Radical

The energy radical consists exactly of the constant Fourier mode:

\[
\mathfrak e(F,F)=0
\quad\Longleftrightarrow\quad
F(z,r)=c.
\]

This is the Jacobi zero mode, hence the precursor wall.

The completed even-jet observer is

\[
\mathcal J_rF
=
\frac{r^2}{4\pi^2}F^{(4)}(0)
+
\frac{3r}{2\pi}F^{(2)}(0).
\]

Since derivatives annihilate constants,

\[
\ker\mathfrak e
\subseteq
\ker\mathcal J_r.
\]

Therefore radical annihilation is automatic on the even completed channel.
The observer descends to the reduced heat-energy quotient before any
pseudoinverse or Schur complement is formed.

## Boundedness of the completed observer

For \(s>9/2\), Sobolev trace bounds give

\[
|\mathcal J_rF|
\le
C_s(r^2+r)\|F\|_{H^s}.
\]

On each compact heat interval \(r\in[r_0,r_1]\subset(0,\infty)\),

\[
\sup_r|\mathcal J_rF|
\le
C_{s,r_0,r_1}\|F\|_{H^s}.
\]

Composed with heat propagation, \(\mathcal J_rP_{r-r_0}\) is continuous on
the common dense core and extends continuously to the declared Sobolev rung.
Its graph is therefore closed there.

Uniformity is correctly restricted to compact \(r\)-regions. Near \(r=0\),
one changes to the reciprocal Poisson chart rather than claiming a uniform
direct-chart bound.

## Relative wall channel

The reduced energy quotient removes the constant mode from the bulk form, but
the mapping-cone object retains it as a separate wall coordinate. Its
coupling to the completed image is the Wronskian connecting morphism

\[
\partial_{\mathcal C}:
\operatorname{Ran}\mathcal C
\to
(\ker\mathcal C)^*.
\]

Thus bulk radical reduction and wall retention are compatible rather than
contradictory.

## What is now closed

For the reciprocal-even completed theta channel, the Jacobi square now has:

- a common dense Sobolev core;
- contractive heat propagation;
- an exact polarized Green identity;
- a positive bulk energy;
- an explicitly identified radical;
- automatic radical annihilation by the completion jet;
- continuous fourth-order endpoint observation;
- a closed represented graph on compact scale regions;
- a separate relative wall connecting map.

This closes the analytic Green polarization of the even Jacobi comparison.

## Remaining channels

The full Adams mixed form is not yet constructed. Still required are:

1. the reciprocal-odd oriented-front channel;
2. its pairing with the even completion jet;
3. prime and grade incidence into the Jacobi carrier;
4. compatibility of direct and reciprocal Sobolev metrics under Poisson;
5. assembly of the primitive dual and square Hilbert coefficients;
6. the source boundary sign of the resulting mixed block.

Thus only the even analytic comparison cell is promoted, not the Adams edge
or global coercivity theorem.

## Source locators

- research/nima/the-heat-equation-turns-the-completed-theta-source-into-an-even-window-jet.md
- research/nima/the-jacobi-heat-kernel-is-the-first-common-carrier-for-window-shift-and-theta-scale.md
- research/nima/the-wronskian-lagrange-boundary-map-is-the-relative-connecting-morphism-for-the-killed-wall.md
- research/nima/the-completion-differential-annihilates-the-wall-so-the-common-carrier-must-be-relative.md
