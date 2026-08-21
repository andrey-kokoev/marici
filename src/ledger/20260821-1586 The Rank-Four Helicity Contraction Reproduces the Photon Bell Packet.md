# 1586 — The Rank-Four Helicity Contraction Reproduces the Photon Bell Packet

Date: 2026-08-21

Sequence claim: `seqclaim-7afc2a461bd9d5b224362b1f`

## Result

The canonical fixed-kinematics map from a rank-four polarization amplitude to
the outgoing helicity state is evaluation on the fixed incoming preparation
followed by the oriented-helicity decomposition of Entries 1583--1585:

\[
\mu_{h_3h_4}
=\mathcal A(e_+,e_+;e^{h_3},e^{h_4}).
\]

For the identical parity-symmetric photon source packet this gives exactly

\[
(\Phi_1,\Phi_5,\Phi_5,\Phi_2).
\]

The two-term pair \((\Phi_1,\Phi_2)\) is **not** a consequence of parity or
crossing alone.  It additionally uses the low-energy dynamical suppression
\(\Phi_5\simeq0\).

The complete sesquilinear Born calculation, including all sixteen joint
probabilities, gives

\[
I=
\frac{2\sqrt2(\Phi_1\bar\Phi_2+\Phi_2\bar\Phi_1)}
{|\Phi_1|^2+|\Phi_2|^2+2|\Phi_5|^2}.
\]

Normalization and both no-signalling families vanish exactly.  Setting
\(\Phi_5=0\) reproduces Sinha--Zahed Equation (13) without a fitted convention.

Thus objectives 1--4 of the fixed-kinematics Bell comparison are complete.
The remaining objective is the genuinely different angular-bin/accepted-event
pushforward.

## Evidence

- Sinha--Zahed, arXiv:2212.10213v3, Equations (10), (11), and (13).
- `research/nima/check_rank_four_photon_bell_map.py`
- `research/nima/results/rank-four-photon-bell-map.json`
- `research/nima/rank-four-photon-bell-map.md`
- epistemic-graph claim/test event:
  `ev-000000001761-1cb0a871-0400-479d-b8bd-ac869b4c23bb`;
  corrected source-version event:
  `ev-000000001765-6d4e5dfc-c54e-4884-be93-4daf739518aa`.
