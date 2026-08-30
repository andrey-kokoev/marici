# Reflection-equivariant Tate propagation makes the divisor-free odd port dark

## Even and odd local sectors

Let reflection act on the local additive Tate carrier by

\[
(Rf)(x)=f(-x).
\]

The spherical vacuum is even:

\[
R\mathbf 1_{\mathbb Z_p}
=
\mathbf 1_{\mathbb Z_p}.
\]

The antisymmetric character pair

\[
f_\eta^{\mathrm{odd}}
=
\frac{
\psi_p(\eta x)-\psi_p(-\eta x)
}{2i}
\mathbf 1_{\mathbb Z_p}(x)
\]

is odd:

\[
Rf_\eta^{\mathrm{odd}}
=
-f_\eta^{\mathrm{odd}}.
\]

These parity types are source-derived.

## General darkness theorem

Let \(S\) be any propagator commuting with reflection:

\[
SR=RS.
\]

Then its resolvent also commutes with reflection wherever defined:

\[
(I-S)^{-1}R
=
R(I-S)^{-1}.
\]

Let \(U_{\mathrm{odd}}\) inject an odd boundary port and let \(V_{\mathrm{even}}^*\) be an even observer. The mixed return is

\[
G_{\mathrm{even},\mathrm{odd}}
=
V_{\mathrm{even}}^*
(I-S)^{-1}
U_{\mathrm{odd}}.
\]

Conjugating by reflection gives

\[
G_{\mathrm{even},\mathrm{odd}}
=
-G_{\mathrm{even},\mathrm{odd}}.
\]

Therefore

\[
G_{\mathrm{even},\mathrm{odd}}=0.
\]

This is exact parity selection, not an estimate.

## Application to the spherical Tate system

The standard local operations preserve reflection parity:

- multiplication by a radial function of \(|x|_p\);
- valuation projection and radial lift;
- spherical local Tate propagation;
- local Fourier transform, which preserves even and odd sectors;
- the unramified vacuum projector;
- every resolvent formed from these commuting operations.

Hence the divisor-free odd port is completely dark to the existing spherical wall–jump observers.

Its zero scalar Tate integral was not an accidental projection loss. It is the scalar shadow of a stronger operator parity decoupling.

## Consequence

The antisymmetric character pair solves the imported-divisor problem but does not by itself solve the mixed-return problem.

Adding it as a boundary coordinate produces a block-diagonal return:

\[
G_{\mathrm{full}}
=
\begin{pmatrix}
G_{\mathrm{even}}&0\\
0&G_{\mathrm{odd}}
\end{pmatrix}.
\]

If the odd determinant block is nowhere zero, it is spectrally irrelevant. If it has zeros, those zeros belong to an auxiliary odd system rather than to coupling with the zeta carrier.

## Required parity-changing incidence

A nonzero mixed return requires an operator \(P_{\mathrm{fin}}\) with odd reflection character:

\[
RP_{\mathrm{fin}}R=-P_{\mathrm{fin}}.
\]

Then \(P_{\mathrm{fin}}\) maps odd states to even states and even states to odd states, permitting a nonzero boundary pairing.

The finite additive Weyl carrier supplies a natural algebraic candidate:

\[
P_h=T_h-T_{-h}.
\]

Indeed,

\[
RT_hR=T_{-h},
\]

so

\[
RP_hR=-P_h.
\]

This is the finite-difference analogue of the archimedean derivative.

## Authority problem

The displacement \(h\) must be source-derived. Choosing \(h\) to make one mixed matrix element nonzero would fit the coupling.

A valid source law must determine:

- the additive displacement or its conductor class;
- its relation to the prime-power scale \(k\log p\);
- covariance under local Fourier transform;
- reciprocal orientation under \(h\mapsto-h\);
- compatibility with valuation projection after the parity-changing action;
- conductor-cutoff completion.

No canonical nonzero \(h\) is selected by the spherical vacuum alone.

## Minimal mixed return

Once \(P_h\) is authorized, the first relevant compression is

\[
G_{\mathrm{wj},\mathrm{odd}}(s)
=
V_{\mathrm{wj}}^*
(I-S_{\mathrm{even}}(s))^{-1}
P_h
U_{\mathrm{odd}}.
\]

Every factor now has a distinct role:

- \(U_{\mathrm{odd}}\): divisor-free finite phase port;
- \(P_h\): parity-changing source incidence;
- the resolvent: spherical propagation;
- \(V_{\mathrm{wj}}^*\): wall–jump observation.

Removing \(P_h\) forces the return to zero.

## Completion margin

Finite nonzero mixed returns are insufficient. If authorized displacements \(h_X\) tend to zero in a topology where

\[
T_{h_X}-T_{-h_X}\to0,
\]

then the odd observer margin collapses.

The completion theorem needs a fixed normalized parity-changing frame or a renormalized derivative limit with uniform graph control.

## Hostiles

1. Couple even and odd ports through a reflection-equivariant resolvent and claim a nonzero result.
2. Treat scalar Tate vanishing as the only darkness mechanism.
3. Insert \(T_h-T_{-h}\) with an arbitrary \(h\).
4. Let \(h_X\to0\) without derivative renormalization.
5. Attribute zeros of a decoupled odd determinant block to the completed zeta feedback.

## Verdict

The divisor-free antisymmetric character port remains dark under every existing spherical Tate propagator because those propagators preserve reflection parity.

The earliest missing constructor is now a source-authorized finite parity-changing incidence, naturally modeled by \(T_h-T_{-h}\), together with a completion-stable normalization.
