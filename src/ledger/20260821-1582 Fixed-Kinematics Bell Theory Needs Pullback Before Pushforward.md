# 1582 — Fixed-Kinematics Bell Theory Needs Pullback Before Pushforward

Date: 2026-08-21

Sequence claim: `seqclaim-4d4e9ea21e4f92c07edf6be1`

## Result

The source Bell construction and an accepted-event experiment require two
different base operations.  Sinha and Zahed define the massless outgoing
helicity qubits **at fixed momenta**.  Their theoretical Bell function is thus

\[
\text{kinematic fiber pullback}
\longrightarrow
\text{Born normalization/readout}.
\]

It does not require a momentum-base pushforward.  Such a positive relative
pushforward becomes necessary only for angular bins, inclusive observables, or
postselected detector samples.

On an exact two-fiber packet, evaluation commutes with every pointwise fiber
map, while equal-weight pushforward changes the Bell value from the individual
fiber values.  Hence Entries 1580–1581 remain the correct support theorem, but
their missing pushforward is not a blocker for the pointwise theoretical test.

The next smallest Marici construction is the fixed-kinematics helicity fiber
and its sesquilinear Born readout.  The experimental support problem is a
strictly later layer.

## Evidence

- Sinha–Zahed, arXiv:2212.10213v3, basic setup and fixed-momenta qubits.
- `research/nima/check_fixed_kinematics_bell_pullback.py`
- `research/nima/results/fixed-kinematics-bell-pullback.json`
- `research/nima/fixed-kinematics-bell-pullback.md`
- epistemic-graph event: `ev-000000001755-6c9deadf-95ab-40d0-a530-6611f8e10696`.
