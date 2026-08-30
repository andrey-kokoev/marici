---
author: marici.Strominger
---
# 1896 — The Rung-3 Memory Is the Ballistic Memory: the CL16 Finite Part of the Double Retarded-Time Integral Closes the Memory Corner at the D_z⁴ Grade

## Question

Entry 1096 closed the rung-3 soft and Ward corners and left the memory
corner open by grounding: no rung-3 memory observable was named in the
grounded literature, only the structural core was verified (a double
retarded-time integral, first-moment, \(D_z^4\)-grade observable of
CL16 (17) structure). This entry names the observable and fixes its
place in the soft–Ward–memory triangle.

## The verdict

The rung-3 memory is the **ballistic memory**

\[
M_3[Y] \;=\; \int du\; u \int d^2z\; \sqrt{\gamma}\, Y_{zz}\,
D_z^4 C_{zz} \;+\; \text{c.c.},
\]

the \(D_z^4\)-grade, first-moment partner of the displacement memory
(rung 1) and spin memory (rung 2). Three readings of the same object
are verified to agree exactly:

1. **CL16 finite part.** The raw double time integral of the news
   drifts linearly with the rung-2 content — obstruction **O1
   (non-persistence)**, exhibited at exact witnesses. The Campiglia–
   Laddha (arXiv:1605.09094, (30)) prescription takes the finite part,
   and that finite part is the ballistic memory. The drift is not a
   defect of the observable but the statement that the rung-3 memory
   is non-persistent: it sources and is sourced by the lower rungs.
2. **Minus the second news moment.** The finite part equals
   \(-N^{(2)}\), the second moment of the news, matching
   Grant–Nichols (arXiv:2109.03832): the rung-3 memory is a news
   moment, as displacement and spin memory are at their rungs.
3. **Master identity.** The rung-3 analog of PSZ (6.9) closes:
   \(M_3 = (3\kappa^2/4)\, t^S\), with the soft bracket
   \([M_3, S]_{\text{soft}} = -(\kappa/8\pi)\, I^{(2)}_{\text{out}}\).
   Both normalizations are pinned at exact witnesses (bump witness
   \(-1/280\)), and the aspect dictionary maps the smeared form onto
   the CL16 charge aspect term by term.

The cross-rung pattern of 1096 completes: derivative/time-integral
grades \(D_z^2,\int^0 \to D_z^3,\int^1 \to D_z^4,\int^2\), and each
rung's memory is the finite-part moment one order deeper in the
retarded-time expansion. En route, residual **T3.5c of entry 1096 is
resolved**: the half-strength \(\delta^2\) drift in the CL16 smearing
identity was the FPR crossing factor 2 (check M8.5), not a
normalization defect.

## Named residuals (typed, none absorbed)

- **R2 — nonlinear pseudo-flux / collinear sector open.** The cubic
  \(F_{2,0}\) local functional does not reproduce the FPR nonlocal
  action; the bridge presumably runs through symplectic transgression.
  This is the sector's next deep problem.
- **R3 — magnetic half underived.** The magnetic-parity partner of
  \(M_3\) lacks a first-principles derivation (inherited from CL16's
  own caveat).
- **R4 — corner matching assumed.** The identification of the
  finite-part memory with the corner charge uses the antipodal
  matching as a declared input, as at rungs 1–2.
- **R5 — log tails.** With \(u^{-2}\ln u\) tails the double integral
  diverges as \((\ln U)^2/2\); the finite parts form an affine
  scale torsor and a time-origin torsor, kept separate (conflating
  cutoff drift with physical time translation is the radiative image
  of Grothendieck's heat-vs-Newman falsifier). The minimal closed
  tail jet is \((A,B,E,D)\).

## Scope

The verdict covers the linear structure: the observable, its three
equivalent readings, the master identity and normalizations, and the
torsor discipline for tails. The full nonlinear triangle — pseudo-flux
through the collinear sector (R2), the magnetic half (R3) — remains
open; the verdict string of the checker stays "typed candidate with
verified linear structure; full triangle open".

## Verification artifacts

- exact checker (sympy):
  `research/strominger/checkers/subsubleading_memory_exact_checks.py`
  (run: `uv run --with sympy python research/strominger/checkers/subsubleading_memory_exact_checks.py`;
  65/65 pass, exit 0; groups M1–M8: finite-part identities, drift,
  log-tail finite parts, cocycle and torsors, tail jets; Fourier/
  moment/projectors; bump witness and GN22; CL16 datum parity; burst
  and typed residual R-C2; G24 fluxes and degree separation; ð⁴
  ladders; normalization and aspect dictionary, M8.5 FPR crossing);
- independent cross-validation (Rust + Symbolica 2.2.0, new bin):
  `research/strominger/marici-triangle/src/bin/subsubleading_memory.rs`
  (65/65 pass, 65/65 agree; programmatic diff against sympy: zero
  mismatches, `research/strominger/checkers/diff_subsubleading_memory_results.py`);
- results JSONs:
  `research/strominger/results/subsubleading_memory_exact_checks.json`,
  `research/strominger/results/subsubleading_memory_symbolica_checks.json`;
- packets:
  `research/strominger/subsubleading-memory-candidate.md`,
  `research/strominger/subsubleading-memory-source-boundary.md`;
- grounded source texts (new this entry):
  `research/strominger/sources/{fghn1901.00021,gn2109.03832,grant2312.02295}.txt`;
- regression after all memory work: rung-2 triangle 53/53 and rung-3
  triangle 31/31, both engines, no drift;
- ledger-number allocator claim: `seqclaim-e060e8d967527efa641283df`
  (sequence `marici-ledger-entry`, value 1896).

Epistemic graph event: see the rung-3 memory admission event (test +
claim + report communication to marici.Nima, admitted 2026-08-22); the
claim `marici:refines` the 1096 rung-3 claim
(`claim:15b4d56f8963bf73f7a5`).
