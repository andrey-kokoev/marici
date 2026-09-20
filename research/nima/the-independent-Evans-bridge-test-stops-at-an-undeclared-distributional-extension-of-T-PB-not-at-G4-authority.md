# The independent Evans bridge test stops at an undeclared distributional extension of T_PB, not at G4 authority

## Audit target

For the source-derived candidate

\[
\epsilon_{\rm Ev}^{(j)}(v)
=(v\otimes\Phi)\oplus(v\otimes F^jK_1),
\qquad
K_1=-\frac12|q|+\delta_0,
\]

the decisive expression is

\[
T_{PB}\epsilon_{\rm Ev}^{(j)}(u_z).
\]

Version 17 authorizes `T_PB` as the analytical G4. No external owner or legacy
comparison is involved.

## What the current T_PB contract declares

The crossing is specified as

\[
T_{PB}
=\mathcal L\circ(\rho_0,e,w,\rho)
\circ\operatorname{Loc}_{[a,b]}
\circ\operatorname{HD}_{\rm ord}
\]

on the projective ordered-pair kernel carrier. It declares continuity,
orientation, shell naturality, and all-jet compatibility. It also fixes

\[
\partial_t\rho=e-\frac12w,
\qquad
R+2E=\frac{\rho(0)+E-W/2}{z}+2E.
\]

## Exact missing operation

The contracts do not define the shell-localization and four bordered coordinate
maps on pair tensors whose second leg is a distribution in

\[
\operatorname{span}(\delta_0,\mathbf1,|q|,V).
\]

In particular, none supplies the four values

\[
(\rho_0,e,w,\rho)(u_z\otimes\delta_0),
\quad
(\rho_0,e,w,\rho)(u_z\otimes\mathbf1),
\]

\[
(\rho_0,e,w,\rho)(u_z\otimes|q|),
\quad
(\rho_0,e,w,\rho)(u_z\otimes V).
\]

The five-cell representation fixes their finite linear labels and Fourier
orbits, but explicitly does not identify that representation with the analytic
Tate action or its quadratic Green lift. Therefore it cannot be substituted
for these analytic values.

## Consequence

The expression `T_PB epsilon_Ev(u_z)` is presently well motivated but not
well typed on the declared domain. Neither tau divisibility nor failure of tau
divisibility can be computed from the current crossing contract.

This is not an authority gate. It is a concrete domain-extension theorem:
construct

\[
T_{PB}^{\rm rig}:
P_{\rm pair}^{\rm rig}
\longrightarrow B_{\rm border}^{\rm rig}
\]

on the strong-dual pair carrier containing the four distributional second
legs, and prove it restricts to the existing `T_PB` on regular pair kernels.

## Acceptance tests for the extension

A valid extension must:

1. derive the four displayed coordinate packets by duality, not by desired Xi
   cancellation;
2. intertwine the Fourier orbit
   `delta_0 <-> one`, `K -> V -> -K`;
3. preserve the fixed wall and odd columns
   `w_theta=(1/2,1/2)` and `j_theta=(1/4,-1/4)`;
4. commute with moving seams, prime cutoffs, and parameter jets;
5. retain the source identity `partial K_1=D_1`;
6. produce a transverse defect that is tested for tau divisibility and
   nonidentity only after the extension is frozen.

## Disposition

The mythical-owner blocker is removed. The live executable gate is the
rigged/distributional extension of the already admitted canonical crossing.
Assigning the four missing coordinate packets from the desired Evans result
would be circular.