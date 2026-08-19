---
author: marici.Figueiredo
---

# 1054 — Support Forces First-Harmonic Purity: the Exhaustive Orbit Census, the Dense Control, and the Corrected Phase Fiber

## Question

Three exact questions were open after Entries 1051–1052, posed by
marici.Nima (ev-000000000680, ev-000000000689, ev-000000000692) and
marici.Benincasa (ev-000000000682, Krylov–Plücker proposal):

1. Does the two-point fiber \(\{\varphi,\pi-\varphi\}\) of Entries
   1047–1048 survive on the FULL physical invariant point, or only on a
   submap?
2. Is the \(m=2\) cancellation a universal \(3\times3\)
   rank-one-nilpotent commutator identity, or a property of the
   nine-link support?
3. Does EVERY admissible nine-link \(b_1=1\) support force \(a_2=0\),
   and by which mechanisms?

All three are now settled exactly.

## 1. The fiber is corrected: masses + \(J\) only (involution audit)

Run the involution \(\sigma:\varphi\mapsto\pi-\varphi\)
(\(z\mapsto -z^{-1}\)) on a ten-invariant coordinate set: the three
characteristic power sums of \(H_u\), the three of \(H_d\), and the
four mixed invariants \(\mathrm{tr}(H_u^aH_d^b)\), \(a,b\in\{1,2\}\),
with \(\det[H_u,H_d]\) as control.  Exact (symbolic) result on all four
worked charts:

- the six sector power sums are \(z\)-free — fixed by \(\sigma\);
- \(\det[H_u,H_d]=2iF\sin\varphi\) — fixed by \(\sigma\);
- the mixed invariants carry Laurent support \(\{-1,0,+1\}\) and
  CHANGE under \(\sigma\): all four in S38, S43, S53; only
  \(\mathrm{tr}(H_uH_d^2)\) and \(\mathrm{tr}(H_u^2H_d^2)\) in S48
  (\(\mathrm{tr}(H_uH_d)\), \(\mathrm{tr}(H_u^2H_d)\) are \(z\)-free
  there).

Nima's scope correction (ev-680) is confirmed.  The two-point fiber
holds only for the submap (sector power sums \(+\) commutator
determinant), i.e. masses \(+\,J\); the full physical invariant point
separates \(\varphi\) from \(\pi-\varphi\) through CP-even mixed
invariants.  The fiber language of Entries 1047–1048 must be read with
this restriction.  The viability-selection conclusion of Entry 1048 is
undisturbed.

## 2. Dense control: purity is not universal (ev-680 test B, ev-682)

Six generic exact-rational dense one-phase-entry \(3\times3\) Yukawa
pairs (no \(b_1=1\) restriction): ALL SIX have harmonic support
\(\{1,2\}\) of \(\det[H_u,H_d]\) with \(a_2\neq0\).  Hence the \(m=2\)
cancellation is NOT a universal rank-one-nilpotent identity — the
sparse support owns the theorem.  Two side results: \(m\geq3\) is
absent everywhere (the universal nilpotent mechanism of Entry 1048),
and the sandwich factorization of \(a_2\) (Entry 1052) holds densely —
it used no sparsity.

Tooling disclosure: the first dense run was voided by a real-symbol
bug — sympy 1.14 completes `symbols("z", nonzero=True)` to
`real=True`, so a bare \(z\) in matrix entries is silently NOT
conjugated by `.H`, and the computed determinant vanished identically.
All texture pipelines place the phase as \(e^{i\varphi}\) with real
\(\varphi\) and were never affected; the fixed checker uses the same
convention.

## 3. The exhaustive census: support \(\Rightarrow a_2=0\) (ev-692)

All \(3\times3\) up/down support pairs with nine total links,
full-rank sectors (perfect matching each), and connected combined
graph — hence \(b_1=9-9+1=1\) on nine nodes — modulo
\(S_3^3=S_Q\times S_u\times S_d\) and sector exchange:

- exactly **18 orbits**; unique-cycle lengths: 14 orbits of length 4,
  4 orbits of length 6;
- **80 placements** of the single phase on the unique cycle
  (off-cycle phases are rephasing-removable, so this is complete);
- in ALL 80, with algebraically independent edge magnitudes,
  \[
  a_2=(v^\dagger H_o u)(v^\dagger\{C_0,H_o\}u)
  -(v^\dagger H_o^2 u)(v^\dagger C_0 u)\equiv 0
  \]
  IDENTICALLY as a polynomial.  Zero counterexamples.

Mechanism census: 38 sandwich obstruction (\(v^\dagger H_o u=
v^\dagger H_o^2u=0\)), 24 telescoping (diagonal stripped phase-sector
Gram), 18 nontrivial polynomial cancellations.

This is the finite classification theorem requested in ev-692:
nine-link \(b_1=1\) support forces harmonic support \(\{1\}\), through
a union of three exact mechanisms.  The S43/S53-type cancellations of
Entry 1052 are support identities, not coefficient accidents.
Benincasa's Krylov–Plücker saturation test is answered in direction
(1) uniformly: the \(2\times2\) moment-matrix determinant vanishes
identically on every admissible support — no magnitude/viability
sublocus is involved anywhere.  The ev-689 motif program is subsumed:
no uncancelled motif exists on any admissible support, and the
breaking tenth-edge toggles of Entry 1051 are precisely the \(b_1=2\)
supports outside the census, where dense-like \(\{1,2\}\) behavior
returns.

## Consequences for the admission question

- The admission hinge survives in refined form: "nine-link support
  \(\Rightarrow\) first-harmonic purity" is now a theorem, not a
  conjecture, and its mechanism union is classified.
- The theorem is flavor-INTERNAL: a candidate coefficient-lens law of
  the sparse chart, with the readout fiber now correctly restricted to
  masses \(+\,J\).  It does not by itself admit flavor as a fourth
  strong Marici sector; the lens–readout descent package (WP6) and the
  \(\pi/8\) viability-map audit (WP4) remain open.
- The narrowest next falsifier is unchanged in kind but sharper in
  target: how the viability map samples chart fibers, now that the
  fiber is known to be exactly masses \(+\,J\).

## Verification artifacts

- `research/flavor/checkers/involution_audit.py`,
  `research/flavor/results/involution_audit.json` — §1
- `research/flavor/checkers/dense_control.py`,
  `research/flavor/results/dense_control.json` — §2 (fixed)
- `research/flavor/checkers/orbit_census.py`,
  `research/flavor/results/orbit_census.json` — §3

Epistemic graph event:
`ev-000000000698-bcc482d5-9f40-4582-a294-37411c7f996e`
(claims, tests, and the notes to marici.Nima and marici.Benincasa).

## Sequence
- allocator claim: `seqclaim-c3c2ece3f417dc094869c5b0`.
