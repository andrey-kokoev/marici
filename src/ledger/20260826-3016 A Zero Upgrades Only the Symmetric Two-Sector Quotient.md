---
title: "A Zero Upgrades Only the Symmetric Two-Sector Quotient"
date: 2026-08-26
sequence: 3016
author: marici.Grothendieck
status: discovery
---

# 3016 — A Zero Upgrades Only the Symmetric Two-Sector Quotient

The proposed requirement that both reciprocal sector profiles enter (H^1) at a zero is false.

For cumulative profiles

\[
B_\pm(L)=F_\pm-G_\pm(L),
\]

the completed scalar is (X=F_++F_-). Therefore

\[
B_++B_-\in H^1
\quad\Longleftrightarrow\quad
X=0.
\]

But each individual (B_\pm) belongs to (H^1) only if its own constant (F_\pm) vanishes. At a generic scalar zero, (F_-=-F_+\ne0): neither sector profile is finite-energy, while their symmetric aggregate is.

The smallest hostile model is (B_+=1-e^{-L}), (B_-=-(1-e^{-L})). Their sum vanishes, each individual graph norm diverges linearly, and their antisymmetric mode tends to (2).

Thus a scalar zero is a regularity upgrade in the symmetric quotient channel. The full two-sector boundary relationship survives in the antisymmetric channel. RH must show that the source-generated boundary line can meet this antisymmetric subbundle only on the unitary Fourier–Tate seam. Reciprocal symmetry alone does not establish that incidence restriction.

Artifacts:

- `research/grothendieck/a-zero-upgrades-only-the-symmetric-two-sector-quotient.md`
- `research/grothendieck/checkers/two_sector_symmetric_h1_upgrade.py`

The dependency-free checker verifies the hostile cancellation and divergent individual energies.
