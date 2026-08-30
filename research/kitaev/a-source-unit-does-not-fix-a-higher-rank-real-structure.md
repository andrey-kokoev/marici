# A Source Unit Does Not Fix a Higher-Rank Real Structure

## Real structures and transport

A real structure on a complex Hilbert space (H) is an antiunitary
involution (J). In a fixed complex basis it has the form

\[
J_S(v)=S\overline v,
\qquad
S\overline S=I.
\]

For source and target structures (J_{S_+}) and (J_{S_-}), a complex-linear
transport (D:H_+\to H_-) preserves the real forms exactly when

\[
D S_+=S_-\overline D.
\]

The typed residual

\[
\mathcal R(D;S_+,S_-)=D S_+-S_-\overline D
\]

must vanish before any scalar readout. A scalar gamma or phase can repair this
residual only if its value is independently derived from the source transport;
choosing it to force a desired scalar sign is circular.

## The one-dimensional torsor

Every real structure on (\mathbb C) is

\[
J_\theta(z)=e^{2i\theta}\overline z,
\]

whose fixed real line is (e^{i\theta}\mathbb R). Thus real lines form a
(U(1)/\{\pm1\}) torsor. Multiplication by
(d=re^{i\phi}), with (r>0), intertwines (J_{\theta_+}) and
(J_{\theta_-}) exactly when

\[
\phi=\theta_- -\theta_+\pmod\pi.
\]

The transport phase is therefore a coherence cell, not dispensable scalar
normalization.

## A unit fixes too little in higher rank

A nonzero unit or vacuum (u) may specify a positive ray inside one real form.
In complex dimension at least two it does not determine the full conjugation.
For example, on (\mathbb C^2), both

\[
J_0(z_1,z_2)=(\overline z_1,\overline z_2)
\]

and

\[
J_1(z_1,z_2)=(\overline z_1,-\overline z_2)
\]

fix (u=e_1), but their fixed real forms differ in the second direction:

\[
\operatorname{Fix}(J_0)=\mathbb R e_1\oplus\mathbb R e_2,
\qquad
\operatorname{Fix}(J_1)=\mathbb R e_1\oplus\mathbb R(i e_2).
\]

The identity map preserves the unit and every scalar probe supported on it,
yet fails the real-structure transport equation. The residual freedom after
fixing one unit is the family of real structures on its orthogonal complement;
in rank (n) this has the homogeneous type (U(n-1)/O(n-1)).

Therefore the tensor unit can orient a one-dimensional reference channel but
cannot by itself authorize a higher-rank positive cone or all interference
phases.

## Minimal source signature

The real-frame route requires the source to provide:

1. antiunitary involutions (J_{+,X}) and (J_{-,X}), not merely preferred
   vectors;
2. a transport (D_X) satisfying
   (D_XJ_{+,X}=J_{-,X}D_X);
3. compatibility of units and positive rays inside the fixed real forms;
4. compatibility with the sheet involution and admitted arithmetic
   constructors;
5. a cutoff-independent bound controlling the transport residual and the gap
   between completed real subspaces.

If exact intertwining is weakened at finite cutoff, the residual norm must tend
to zero in the source topology. Strong convergence on a preferred unit alone
does not control the complementary real frame.

## Falsifiers

- The transport preserves the unit but not the conjugation.
- Two distinct real structures fix every declared scalar reference probe.
- A gamma phase is selected after inspecting the desired scalar sign.
- The real frame is declared only on the one-dimensional trace image while the
  arithmetic correspondence is higher rank.
- Residuals vanish on the unit but not on its orthogonal complement.
- Cutoff real forms drift without a uniform graph or gap bound.

## Claim boundary

This is a finite real-structure compiler theorem. It does not identify the
theta/Tate conjugations, derive the gamma factor, prove completion stability,
or prove RH.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. One-dimensional line transport, higher-rank conjugation transport,
unit-fixed residual frames, and completion stability were frozen branches.
Incompatible real lines and two conjugations fixing one vacuum were the exact
hostiles.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The transport law became the explicit antilinear intertwiner residual.
A unit was proved sufficient only to orient its own ray, leaving a
(U(n-1)/O(n-1))-type family on the complement. The missing theta/Tate datum is
therefore a full transported conjugation, not another scalar normalization.
