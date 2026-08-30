# Higgs-mass-calibrated common-clock portal

## Calibration role

WP471 treats the WP467 Higgs-portal stiffness `eta` as a detector-calibrated
nuisance coordinate. It is not promoted to source-selection authority. The
vacuum equations and

\[
{g_Ff\over v}=\sqrt3g_F
\]

at `y=a=1` do not depend on `eta`, so this calibration does not move the target
clock ratio.

The physical input is the PDG 2025 central Higgs mass `125.20 GeV`, with
`v=246.22 GeV`. In units of `w^2=v^2/2`, the required curvature is

\[
L_H={2m_H^2\over v^2}={78375200\over151560721}.
\]

## Unique exact calibration

After the WP469 radial lift, the exact radial Hessian for variable `eta` is

\[
R(\eta)=\begin{pmatrix}
106&2\sqrt6&-98\sqrt3\\
2\sqrt6&4\eta+4&(-4\eta+2)\sqrt2\\
-98\sqrt3&(-4\eta+2)\sqrt2&302+8\eta
\end{pmatrix}.
\]

The pole equation `det(R(eta)-L_H I)=0` is linear in `eta` and gives the unique
positive solution

\[
\eta_H={1186324514058160\over13746755484562347}
\simeq0.0862985.
\]

At this value the exact radial spectrum is

\[
L_H,qquad12,qquad{12109182640\over30233769}.
\]

Together with WP468's orthogonal modes, all physical curvatures remain
positive and the only zeros are the eleven gauge Goldstones.

## Frozen calibrated residues

Polynomial spectral projectors give the Higgs-radial diagonal residues:

\[
Z_H={45822595065274178\over68734007773010799}
\simeq0.66666555,
\]

for the 125.20-GeV pole,

\[
Z_D={1\over3}
\]

for the lifted `12` pole, and approximately `1.12 times 10^-6` for the heavy
radial pole. The complete flavor-radial and singlet-radial residues are frozen
in the generated JSON.

The mass input fixes only `eta`; it does not fit these residues. They are
therefore withheld physical predictions of this calibrated conditional model.

## Classification and next instrument

- Selector: the common-clock source operation still conditionally selects
  `g_F f/v`; Higgs mass calibration neither selects nor changes it.
- Instrument: reconstructed Higgs mass, with declared detector units.
- Calibration map: rank one and unique in `eta` at the frozen point.
- Rigidifier: the mass instrument fixes one response coordinate, not a texture
  presentation.
- Smallest next falsifier: the predicted Higgs signal-strength residue near
  `2/3` is incompatible with independently measured Higgs rates after complete
  production and decay normalization.
- Remaining gate: attach the full Higgs rate/width likelihood without refitting
  `eta`, then derive scalar and flavor-vector widths in the same threshold
  domain.

