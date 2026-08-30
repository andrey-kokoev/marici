# Charged-cycle Standard Model interference

## Bounded question

Can an independently existing Standard Model neutral-current amplitude make
the WP640 contact response linearly visible, and can that interference recover
the source-current sign or phase lost when \(\chi\) was eliminated?

## Exact Fierz channel

The Dirac completeness identity and one Grassmann interchange give

\[
(\bar d_Ru_L)(\bar u_Ld_R)
=-{1\over2}(\bar d_R\gamma^\mu d_R)
(\bar u_L\gamma_\mu u_L).
\]

Therefore the WP640 interaction

\[
-G(\bar d_Ru_L)(\bar u_Ld_R)
\]

is equivalent to a chiral neutral-current contact with coefficient \(G/2\).
Photon and \(Z\) exchange already supply source-authorized amplitudes in this
external quark channel. No fitted reference port is needed to establish the
existence of interference.

## Abstract calibrated-background slice

Let \(B\) denote a real Standard Model helicity amplitude in a fixed kinematic
bin, in the same normalization as the contact amplitude. The response factor
is

\[
R(B,G)=(B+G/2)^2,
\]

and its background-subtracted value is

\[
\Delta R=BG+G^2/4.
\]

The term linear in \(G\) means a nonzero Standard Model background can improve
sensitivity to the contact coefficient. On the exact slice \(B=1\), the
constructive, destructive, and mass-two WP640 contexts give total responses
\(9,1,9/4\), respectively.

This use of \(B=1\) is a normalization test, not detector calibration. A real
analysis must derive \(B\), its phase, and its uncertainty from the Standard
Model plus the admitted bin definition.

## Irreversible source kernel

The interference does not recover the sign or phase of the pre-contact source
current. Charged-scalar elimination has already applied

\[
J\longmapsto G={|J|^2\over m_\chi^2}.
\]

For every phase \(e^{i\alpha}\), the currents \(J\) and
\(e^{i\alpha}J\) give the same \(G\), hence the same interference response for
every \(B\). The first nonfaithful arrow is charged-scalar elimination, not the
later detector projection. No family of downstream probes that factors only
through \(G\) can repair this kernel.

## Classification and remaining gate

Standard Model interference makes the added contact coefficient linearly
probeable at source level. It is still neither a selector nor a texture
rigidifier and does not descend to a selector on the original `physical16`
family. Detector authority requires a named collider dataset and binning,
PDF convolution, electroweak helicity amplitudes, operator running, flavor
tagging, cuts, response matrices, backgrounds, uncertainties, and likelihood.

## Reproduction

Run:

    uv run --with sympy python research/flavor/checkers/wp641_charged_cycle_sm_interference.py

The generated result is
`research/flavor/results/wp641_charged_cycle_sm_interference.json`.
