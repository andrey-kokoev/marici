# 1606 — The Exact One-Loop QED Amplitude Has a Sub-Threshold Bell Crossing

Date: 2026-08-21

Sequence claim: `seqclaim-e2e1fa9ba6ffb7ecfb48cdfd`

## Result

Entry 1602's EFT prediction survives its decisive falsifier. The exact
massive-fermion one-loop helicity amplitudes, evaluated at the transverse
angle with the below-threshold analytic continuation, give a Bell crossing in
the bracket

\[
0.4201576087391004
<\frac{s}{m_e^2}<
0.4201576087623835.
\]

Thus

\[
\boxed{
\frac{\sqrt{s}}{m_e}=0.6481956562\ldots
}
\]

is the exact one-loop transverse onset for the frozen maximally entangled
input and fixed analyzer settings.

The implementation passed a source-normalization gate before the root was
accepted. At (s/m_e^2=0.01), the three stripped channels reproduce

\[
\mathcal M_{--++}\sim\frac{11}{360}y^2,
\qquad
\mathcal M_{++++}\sim-\frac1{80}y^2,
\qquad
\mathcal M_{-+++}\sim-\frac1{10080}y^3
\]

to better than (0.2\%), thereby checking the (g_2,f_2,h_3) conventions
and the mixed-helicity normalization independently.

The dimension-ten and dimension-twelve truncated-amplitude onsets were
(0.46803) and (0.42369); the latter is already within one percent of the
exact value. Hence the physical crossing is not an EFT-truncation artifact.

This establishes a transverse fixed-analyzer Bell violation below pair
production. A subsequent bounded angular census is recorded separately; this
entry alone does not establish violation at every angle and does not include
two-loop radiative corrections.

## Evidence

- Ajjath et al., arXiv:2312.16966v2, equations 50 and 53--55.
- `research/nima/check_exact_qed_bell_onset.py`
- `research/nima/results/exact-qed-bell-onset.json`
- `research/nima/exact-qed-bell-onset.md`
- epistemic-graph event:
  `ev-000000001791-21b898f6-e293-4394-8db4-6212be4aea15`.
