# Conventions packet: the sub-subleading triangle (marici.Strominger)

Companion to `soft-bms-memory-conventions.md` /
`soft-bms-memory-source-boundary.md` (rung 1, ledger entry 1056) and
`subleading-triangle-conventions.md` /
`subleading-triangle-source-boundary.md` (rung 2, ledger entry 1079).
This packet fixes the conventions, gauge prescription, grounding status,
and research hypotheses for the **sub-subleading** (rung 3) triangle
before any checker is built. Prepared under the operator directive to
ground rung 3 in the literature.

The triangle under test:

- **Soft corner.** The sub-subleading soft graviton factor \(S^{(2)}\)
  of Cachazo–Strominger [CS] = arXiv:1404.4091 (already local).
- **Ward corner.** Campiglia–Laddha [CL16] = arXiv:1605.09094
  ("Sub-subleading soft gravitons: New symmetries of quantum gravity?"),
  building on generalized BMS [CL15] = arXiv:1502.02318; and
  Freidel–Pranzetti–Raclariu [FPR] = arXiv:2111.15607 (spin-2 charge
  aspect from the asymptotic Einstein equations).
- **Memory corner.** No canonical rung-3 observable is known. Nearest
  candidates: the center-of-mass (CM) memory of Nichols [N18] =
  arXiv:1807.08767, and the persistent-observables framework of
  Flanagan–Grant–Harte–Nichols [FGHN] = arXiv:1901.00021. Grounding
  below shows both sit at the SUBLEADING time-integral level, not rung
  3 — see §5. The rung-3 memory corner is OPEN.

## 1. Grounding ledger (typed, load-bearing)

Status as of 2026-08-19:

| item | status |
|---|---|
| [CS] = arXiv:1404.4091 | grounded (rung-2 session). Local: `sources/cs1404.4091.txt`. Rung-3 formulas: soft expansion (8), \(S^{(2)}\) tensor form (9), gauge-invariance statement, spinor form (20), holomorphic claim (23)/(28), stripped-amplitude sub-subleading (92)–(93) — line citations in §2 |
| [CL16] = arXiv:1605.09094 | grounded. Abstract via arxiv.org/abs/1605.09094; formula level via PDF text extraction to `sources/cl1605.09094.txt` (5 pages): three-factorization setup (1)–(4), Ward-identity ladder (5)–(9), sub-subleading boundary form (14), smearing (15), charges (16)–(18), divergence-free-\(X\) split (19), covariant-phase-space charges (31)–(33) and exact match statement |
| [CL15] = arXiv:1502.02318 | grounded. Abstract via arxiv.org/abs/1502.02318; formula level via PDF text extraction to `sources/cl1502.02318.txt` (19 pages): first-principles Diff(\(S^2\)) charges; leading+subleading soft theorems = Ward identities of \(G=\) Diff(\(S^2\))\(\ltimes\)supertranslations |
| [FPR] = arXiv:2111.15607 | grounded. Abstract via arxiv.org/abs/2111.15607; formula level via PDF text extraction to `sources/fpr2111.15607.txt` (38 pages): spin-2 charge aspect, conservation equation \(\to\) sub-subleading soft theorem, non-local pseudo-vector-field symmetry, collinear corrections |
| [N18] = arXiv:1807.08767 | grounded. Abstract via arxiv.org/abs/1807.08767; formula level via PDF text extraction to `sources/nichols1807.08767.txt` (26 pages): CM angular momentum under supertranslations, CM memory definition, flux formulas, PN estimates |
| [FGHN] = arXiv:1901.00021 | abstract-level grounded only (arxiv.org/abs/1901.00021): persistent GW observables beyond charge/soft-theorem memory; holonomy observable containing displacement + proper-time + velocity + rotation memories. NOT downloaded this session — typed residual if formula-level grounding is needed |
| Loop status [BDN] 1405.1015, [HHW] 1405.1410, [BDDN] 1406.6987, [LS] 1706.00759, [S20] 2008.04376 | citation-level grounded (arXiv abstract for [LS] fetched; others via search snippets of citing papers). Formula-level grounding NOT in hand — typed residual |

(Working route unchanged: `arxiv.org/pdf/<id>` + `pypdf` via
`uv run --with pypdf python`; the HTML/ar5iv route fails.)

Rule carried over: nothing is proved by citing the correspondence; every
link becomes an explicit check item, and every ungrounded input is a
typed residual, never silently absorbed.

## 2. The exact \(S^{(2)}\) formulas (soft corner, all line numbers in
`sources/cs1404.4091.txt`)

- **Soft expansion through rung 3** [CS (8)], lines 122–126:
  \[
  M_{n+1}(k_1,\dots,k_n,q)=\big(S^{(0)}+S^{(1)}+S^{(2)}\big)
  M_n(k_1,\dots,k_n)+O(q^2).
  \]
- **Tensor form** [CS (9)], lines 127–136:
  \[
  S^{(2)}\equiv-\frac12\sum_{a=1}^{n}
  \frac{E_{\mu\nu}\,(q_\rho J_a^{\rho\mu})(q_\sigma J_a^{\sigma\nu})}
  {q\cdot k_a},
  \]
  with \(J_a\) the total (orbital + spin) angular momentum of leg \(a\)
  (CS footnote 4, lines 98–103: \(J_a^{\mu\nu}\sim
  k_a^{[\mu}\partial/\partial k^a_{\nu]}+(\)helicity terms\()\)).
- **Gauge-invariance statement** (the pattern-break line), lines
  137–141: "It is easy to check that \(S^{(2)}\) is gauge invariant as
  required for the simple reason that \(J^{\mu\nu}_a\) is antisymmetric
  and not as a consequence of any conservation law." Unlike rung 1
  (\(\sum_a k_a^\mu=0\), CS (4), lines 53–60) and rung 2 (\(\sum_a
  J_a^{\mu\nu}=0\), CS (7), lines 83–89), rung 3 needs NO leg-summed
  conservation input for gauge invariance.
- **Universality caveats**, lines 139–152: "unlike \(S^{(1)}\), at this
  point we have found no argument that \(S^{(2)}\) is universal beyond
  tree-level gravity" (lines 140–141); the soft limit requires a
  simultaneous deformation of hard momenta and the proof covers "a very
  large class" of expansions, "not … every conceivable definition"
  (lines 142–148); the tests are "purely classical" and leave open loop
  modification (lines 149–152).
- **Spinor-helicity form** [CS (20)], lines 274–290 (positive-helicity
  soft graviton, reference spinors \(x,y\)):
  \[
  S^{(2)}=\frac12\sum_{a=1}^{n}\frac{[s,a]}{\langle s,a\rangle}\,
  \tilde\lambda^{\dot\alpha}_s\tilde\lambda^{\dot\beta}_s\,
  \frac{\partial^2}{\partial\tilde\lambda^{\dot\alpha}_a\,
  \partial\tilde\lambda^{\dot\beta}_a}.
  \]
  For reference, rung 2 [CS (18)], lines 230–246:
  \(S^{(1)}=\frac12\sum_a\frac{[s,a]}{\langle s,a\rangle}
  \big(\frac{\langle x,a\rangle}{\langle x,s\rangle}
  +\frac{\langle y,a\rangle}{\langle y,s\rangle}\big)
  \tilde\lambda^{\dot\alpha}_s\partial/\partial
  \tilde\lambda^{\dot\alpha}_a\), and the \(J\) spinor decomposition
  [CS (19)], lines 247–273. Note: in (20) the reference-spinor
  prefactors of (18) have dropped out — consistent with per-leg gauge
  invariance.
- **Claim with explicit \(\epsilon\)** [CS (23)], lines 298–303:
  \(M_{n+1}(\dots,\{\sqrt\epsilon\lambda_s,\sqrt\epsilon
  \tilde\lambda_s\})=\big(\epsilon^{-1}S^{(0)}+S^{(1)}
  +\epsilon S^{(2)}\big)M_n+O(\epsilon^2)\); holomorphic soft limit
  [CS (28)], lines 331–339: poles up to cubic order,
  \(\big(\epsilon^{-3}S^{(0)}+\epsilon^{-2}S^{(1)}
  +\epsilon^{-1}S^{(2)}\big)M_n+O(\epsilon^0)\).
- **Stripped-amplitude form** (§3 of CS, for the BCFW-shifted
  representation): sub-subleading term (92)–(93), lines 994–1071 — the
  first sum of (92) equals \(S^{(2)}M_n\) minus an \(a=n\) completion
  term; needed if the checker works with stripped amplitudes.

## 3. The gauge prescription, declared first (rung-3 hazard 1)

- **G_CS2 (declared, formula-grounded).** Rung 3 needs no conservation
  law: \(\delta_\Lambda S^{(2)}=0\) PER LEG, because \(q_\mu q_\nu
  J_a^{\mu\nu}=0\) by antisymmetry of \(J_a\) [CS discussion after (9),
  lines 137–139]. The declared prescription for any rung-3 checker is
  therefore: use the tensor form (9) or the reference-spinor-free
  spinor form (20) AS WRITTEN; do not impose \(\sum_a(\text{anything})
  =0\) at the gauge step. The \(\mathcal P\to\mathcal J\) escalation
  pattern of rungs 1–2 apparently TERMINATES at rung 3 — this is the
  central fact the research question (§8) must confront.
- **Normalization hazard (inherited).** CS footnote 1 (line 51):
  \(8\pi G=1\) and \(E_{\mu\nu}q^\nu=0\). Conversion to our
  \(\kappa^2=32\pi G\) conventions is a check item, as at rungs 1–2.
- **Soft-limit-definition hazard.** CS prove (8) for a class of
  holomorphic soft limits, not every deformation (lines 142–148). Any
  checker must declare its soft path; the default is the holomorphic
  limit \(\lambda_s\to\epsilon\lambda_s\), \(\tilde\lambda_s\) fixed
  [CS (28)].

## 4. Conventions inherited unchanged

\(\kappa^2=32\pi G\); celestial sphere \(z,\bar z\),
\(\gamma_{z\bar z}=2/(1+z\bar z)^2\); \(D_z,D_{\bar z}\); sphere
operator \(\mathcal O=\tfrac14 D^2(D^2+2)\) with kernel the \(l\le1\)
harmonics; retarded time \(u\) on \(\mathcal I^+\); news \(N_{zz}\),
shear \(C_{zz}\). At rung 3 the derivative grade rises again: the
Ward-corner smearing is \(\int d^2z\,Y_{zz}D_z^4\) (§5), one grade
above the rung-2 \(D_z^3\) of [PSZ (5.2)].

## 5. Ward corner (grounded)

**[CL16] = arXiv:1605.09094** (line numbers in
`sources/cl1605.09094.txt`):

- Setup: the soft expansion (1), lines 37–41, yields THREE factorization
  constraints (2)–(4), lines 52–62; the rung-3 one is
  \(\lim_{E_q\to0}E_q^{-1}M_{n+1}|_{\mathrm{fin}}=S^{(2)}M_n\) (4).
- The Ward-identity ladder: (2) \(\leftrightarrow\) supertranslations
  \(\langle\mathrm{out}|[Q_f,S]|\mathrm{in}\rangle=0\) (5) plus dual
  "magnetic" supertranslations \(Q^*_f\) (6), lines 71–89; (3)
  \(\leftrightarrow\) Diff(\(S^2\)) Ward identities
  \(\langle\mathrm{out}|[Q_V,S]|\mathrm{in}\rangle=0\) (7) for
  generalized-BMS \(\xi\sim V^A\partial_A\), lines 90–97 (and here
  \(Q^*_V\) coincides with \(Q_{\epsilon^A{}_B V^B}\) — no new charges,
  lines 98–104).
- Rung-3 claim: (4) is equivalent to TWO identities
  \(\langle\mathrm{out}|[Q_{rX},S]|\mathrm{in}\rangle=0\) (8) and
  \(\langle\mathrm{out}|[\tilde Q_{rX},S]|\mathrm{in}\rangle=0\) (9),
  lines 105–110, associated to LARGE DIFFEOMORPHISMS GROWING AT INFINITY,
  \(\xi^a\sim r\,X^A\partial_A\), parametrized by DIVERGENCE-FREE sphere
  vector fields \(X^A\) (one identity per sphere point each).
- Boundary form of the rung-3 soft theorem (negative helicity) [CL16
  (14)], lines 188–198:
  \[
  \tfrac{\sqrt\gamma}{2\pi i}\lim_{\omega\to0}\omega^{-1}
  \langle\mathrm{out}|C_{zz}(\omega,\hat q)\,S|\mathrm{in}\rangle
  \big|_{\mathrm{fin}}=S^{(2)-}\langle\mathrm{out}|S|\mathrm{in}\rangle,
  \quad S^{(2)-}=\omega^{-1}\sum_i(2k_i\cdot q)^{-1}
  (\epsilon^-_\mu q_\nu J_i^{\mu\nu})^2 .
  \]
- Smearing \(\int d^2z\,Y_{zz}D_z^4\) (lines 199–204) gives the local
  hard action [CL16 (15)], lines 205–219, and the Ward identity
  \(\langle\mathrm{out}|[Q_Y,S]|\mathrm{in}\rangle=0\) (16) with
  [CL16 (17)–(18)], lines 223–252:
  \[
  Q_Y^{\mathrm{soft}}=\int_{-\infty}^{\infty}du\int_{-\infty}^{u}du'
  \int d^2z\,\sqrt\gamma\,Y_{zz}D_z^4 C_{zz}(u',\hat q)+\mathrm{c.c.}
  \]
  — note the DOUBLE retarded-time integral (from the \(\omega^{-1}\) in
  (14), line 253) and the \(D_z^4\) grade; \(Q_Y^{\mathrm{hard}}\) (18)
  is quadratic in the hard radiative field \(\phi\).
- Symmetric-trace-free split \(Y_{AB}=D_AX_B+\epsilon_B{}^CD_AX'_C\)
  with \(X,X'\) divergence-free, giving the pair
  \((Q_{rX},\tilde Q_{rX'})\) [CL16 (19)], lines 264–283.
- Covariant-phase-space computation: total finite charge \(Q_\xi=
  Q_\xi^{\mathrm{hard}}+Q_\xi^{\mathrm{soft}}\) [CL16 (31)–(33)], lines
  445–473; "upon the identification \(Y_{AB}=-\tfrac14 D_AX_B\) … (31)
  and (32) exactly match the respective charges (17) and (18) that were
  obtained from the sub-subleading theorem", lines 474–478.
- **Caveats, stated by CL themselves:** (i) a first-principles
  derivation of the magnetic half \(\tilde Q_{rX}\) is lacking (lines
  115–120: "We currently lack a first principles derivation of \(\tilde
  Q_{rX}\)"); the divergence-free \(X^A\) give only "half" of the
  factorization content (lines 479–496); (ii) the extension is subtle in
  Bondi gauge because generalized BMS already exhaust the smooth
  diffeomorphisms (lines 284–289) — the rung-3 generators grow like
  \(r\) and are NOT smooth at the corners of \(\mathcal I\).

**[CL15] = arXiv:1502.02318** (`sources/cl1502.02318.txt`): first-
principles derivation of the Diff(\(S^2\)) charges; combined with prior
results, "the leading and subleading soft theorems are equivalent to
the Ward identities associated to \(G\)" (abstract; txt lines 17–19).
This is the rung-2 Ward corner in the generalized-BMS framing and the
launchpad for [CL16].

**[FPR] = arXiv:2111.15607** (`sources/fpr2111.15607.txt`): the
sub-subleading soft theorem follows from the conservation equation of
an asymptotic SPIN-2 charge aspect (abstract, txt lines 8–14); the
spin-2 charge generates a NON-LOCAL spacetime symmetry represented at
\(\mathcal I\) by pseudo-vector fields (lines 10–12, 110); the
nonlinear Einstein equations enter as COLLINEAR CORRECTIONS to the
sub-subleading soft factor (lines 113–116, 1527–1529, 1577–1579);
unified spin-0/1/2 treatment (lines 13–14, 972–988). This both
strengthens the Ward corner (charge aspect derived from the equations
of motion, not postulated) and warns that the clean tree factorization
[CS (8)] is dressed by collinear/nonlinear terms.

**Ward-corner verdict: GROUNDED.** There IS a candidate Ward identity
for \(S^{(2)}\): the [CL16] pair of Ward identities for \(O(r)\) large
diffeomorphisms with divergence-free sphere data, later re-derived as
the spin-2 charge-aspect conservation law by [FPR]. It is NOT a
conservation law of the \(\sum_a(\cdot)=0\) type — it is a new set of
charges beyond generalized BMS. Whether the magnetic half \(\tilde
Q_{rX}\) stands on first-principles footing is an OPEN sub-item within
the grounded corner.

## 6. Memory corner (partially grounded; rung-3 observable OPEN)

**[N18] = arXiv:1807.08767** (`sources/nichols1807.08767.txt`): the CM
memory "appears in a quantity which has the units of the time integral
of the GW strain" (abstract; txt lines 21–22) — the SAME single-time-
integral level as the spin memory ("an enduring change in a portion of
the time integral of the GW strain", lines 13–15; magnetic-parity part,
line 163). CM memory is tied to the CM (boost) part of angular
momentum, is invariant under infinitesimal supertranslations in the
stationary-to-stationary context (lines 22–24), and for quasicircular
binaries starts at 3PN/4PN for unequal/equal masses (lines 26–28).
Literature classification (search-grounded, not formula-grounded):
Compère–Fiorucci–Ruzziconi arXiv:1904.00280 and De Luca et al.
arXiv:2412.12273 group "spin and center-of-mass memory" together as
SUBLEADING memory effects. **Conclusion: the CM memory is a rung-2-level
(first-time-integral) observable — the electric-parity partner of the
spin memory — NOT a rung-3 observable.**

**[FGHN] = arXiv:1901.00021** (abstract-grounded): persistent GW
observables exist beyond the charge/soft-theorem memories (holonomy
observable contains displacement, proper-time, velocity, rotation
memories). This is the umbrella under which any rung-3 observable would
live, but no specific \(S^{(2)}\)-matched observable is identified
there.

**The grounded structural hint for a rung-3 observable** comes from the
Ward side: [CL16 (17)] \(Q_Y^{\mathrm{soft}}\) is a DOUBLE
retarded-time integral \(\int du\int^u du'\) of \(D_z^4C_{zz}\). A
rung-3 memory, if it exists in the same pattern, should be an electric
AND magnetic pair of second-time-integral ("higher memory") observables
of the shear, at derivative grade \(D_z^4\). No such observable is
established in the grounded literature — this is a HYPOTHESIS (§8,
H-mem), not a citation.

**Memory-corner verdict: PARTIALLY GROUNDED / OPEN.** Nearest
candidates grounded and shown to sit at rung 2; the rung-3 memory
observable is an open item with a sharply typed candidate shape.

## 7. Loop status (citation-level, one paragraph)

Tree-level \(S^{(2)}\) does NOT survive loops unmodified, in contrast to
\(S^{(0)}\) and \(S^{(1)}\): Bern–Davies–Nohle (arXiv:1405.1015) and
He–Huang–Wen (arXiv:1405.1410) established the loop-level universality
of the leading and subleading factors (up to \(\ln q\) terms), while
Bern–Davies–Di Vecchia–Nohle (arXiv:1406.6987) showed from gauge
invariance that the sub-subleading behavior receives genuine loop
corrections already at one loop. The salvage statement is Laddha–Sen
(arXiv:1706.00759, abstract fetched): to all loop orders (in \(d\ge5\),
where IR divergences are controlled) the sub-subleading soft factor
splits into a UNIVERSAL piece depending only on the lower amplitude and
a non-universal piece depending on two- and three-point functions;
Sahoo (arXiv:2008.04376) gives the classical sub-subleading theorems in
four dimensions. Consequence for the sector: any rung-3 triangle
statement is intrinsically a TREE-LEVEL (or universal-piece) statement —
the same caveat CS themselves flagged (§2). Formula-level grounding of
the loop papers is a typed residual.

## 8. RESEARCH QUESTION (the point of this packet)

Rungs 1 and 2 closed leg-summed under a conservation law: \(S^{(0)}\)
under four-momentum conservation \(\mathcal P\) (ledger 1056), and the
PSZ (6.8) bridge closed EXACTLY leg-summed under total angular momentum
conservation \(\sum_k J_k=0\), with a named per-leg residual
\(M=D_z^2\mathrm{mix}^--D_{\bar z}^2\mathrm{mix}^+\) from the KLPS (6.4)
gauge-mixing term (ledger 1079). At rung 3, CS state that \(S^{(2)}\)
is gauge invariant per leg "and not as a consequence of any
conservation law" (§2). The escalation \(\mathcal P\to\mathcal J\)
apparently stops. **What, if anything, plays the role of the leg-summed
closure input at rung 3, and does a soft–Ward–memory triangle exist
there?**

Candidate hypotheses, sharply stated:

- **H-A (no conservation law needed).** Because per-leg gauge
  invariance is automatic, the rung-3 soft-side bridge (analog of PSZ
  (6.8)) may close leg-summed with NO global input. Checkable: build the
  rung-3 soft-side operator from [CS (20)] acting on an \(n\)-point
  kinematic configuration, compute the leg-summed closure against a
  Ward-side charge smeared with \(\int d^2z\,Y_{zz}D_z^4\) [CL16
  (15)–(18)], with NO \(\sum\)-constraint imposed. If it closes, the
  rung-3 triangle is structurally different from rungs 1–2 (closure is
  kinematic, not conservation-law-mediated).
- **H-B (generalized BMS / superrotation charge).** The Diff(\(S^2\))
  charges of [CL15] might already capture \(S^{(2)}\). Grounded
  expectation: NO — [CL16] lines 284–289 state generalized BMS exhaust
  the smooth diffeomorphisms and a genuine extension is needed. H-B
  survives only as the falsifiable baseline: exercise it as the
  deliberate-failure test (predicted obstruction: the \(\omega^{-1}\)
  / double-\(u\)-integral structure of [CL16 (14),(17)] cannot be
  reproduced by any smooth-\(\mathcal I\) charge).
- **H-C (CL16 large diffeomorphisms).** Leg-summed closure is mediated
  by the pair \((Q_{rX},\tilde Q_{rX})\) of \(O(r)\) large diffeo
  charges with divergence-free \(X^A\) [CL16 (8),(9),(17),(18),(31),
  (32)]. Checkable: verify the smeared soft identity [CL16 (15)]
  \( \frac{1}{2\pi}D_z^4 S^{(2)-}=-3\sum_i E_i^{-1}\delta^{(2)}(z,z_i)
  \partial^2_{z_i}+\dots\) directly from [CS (20)] on symmetric test
  kinematics; verify electric/magnetic doubling. Named hazard: the
  magnetic half lacks first-principles derivation (CL16 lines 115–120).
- **H-D (FPR spin-2 charge aspect).** The closure input is the spin-2
  charge-aspect conservation equation; the tree-level \(S^{(2)}\) is the
  linearized edge of a relation carrying COLLINEAR/NONLINEAR
  corrections. Checkable at our level: reproduce the spin-0/1/2
  derivative-grade ladder \(D_z^2/D_z^3/D_z^4\) across the three rungs
  from [HMLS]/[KLPS]/[CL16] sources; flag collinear corrections as a
  typed residual beyond tree level.
- **H-mem (rung-3 memory candidate).** A rung-3 memory observable is a
  DOUBLE retarded-time integral of the shear at grade \(D_z^4\)
  (electric + magnetic parity pair), per [CL16 (17)]. It is NOT the CM
  memory (single integral, rung 2 — §6). Checkable: dimensionally and
  structurally consistent with the \(\omega^{-1}\) Fourier factor;
  existence as a measurable persistent observable is OPEN ([FGHN]
  framework, abstract-level only).
- **H-E (fails to close — named residual).** The leg-summed rung-3
  bridge exhibits a computable residual (analog of rung-2's \(M\)),
  e.g. from the hard-momentum deformation freedom CS flag at lines
  142–148, or from the missing magnetic half of H-C. A clean failure
  with the residual exhibited is an admissible outcome, per the sector's
  mixed-outcome admission pattern.

**What is checkable NOW with the grounded formulas:** (i) exact per-leg
and leg-summed action of \(S^{(2)}\) as the second-derivative operator
[CS (20)] on rational test amplitudes (MHV examples in CS §4 are in the
local source); (ii) the smearing identity [CL16 (15)] from [CS (20)];
(iii) the derivative-grade ladder \(D_z^2,D_z^3,D_z^4\) and the
time-integral ladder \(\int^0,\int^1,\int^2\) across rungs; (iv)
deliberate-failure tests: H-B (wrong charge class), removal of any
illegitimately assumed conservation law under H-A (should change
NOTHING at the gauge step — the anti-test of rungs 1–2).

## 9. Declared external inputs ledger

1. Tree-level restriction: \(S^{(2)}\) as written is tree-level;
   loop-corrected form is [LS]-typed but not formula-grounded (§7).
2. The holomorphic soft path [CS (21)–(22), (28)] as the declared soft
   limit (§3).
3. Antipodal matching at \(i^0\) [HMLS 3.1–3.3], inherited; the rung-3
   generators \(rX^A\partial_A\) are singular at the corners — matching
   for H-C/H-D is an OPEN item, strictly worse than at rung 2.
4. The hermitian zero-frequency prescription [HMLS 5.17], inherited;
   its rung-3 form involves the finite part of an \(\omega^{-1}\)
   moment [CL16 (14)] — prescription interplay is a check item, not an
   assumption.
5. \(\kappa^2=32\pi G\) conversion from CS's \(8\pi G=1\) (footnote 1,
   line 51) — normalization check item.

## 10. Corner status summary

| corner | status |
|---|---|
| Soft (\(S^{(2)}\), [CS]) | GROUNDED (local source, line-cited) |
| Ward ([CL16], [CL15], [FPR]) | GROUNDED (local sources, line-cited); magnetic half \(\tilde Q_{rX}\) OPEN sub-item |
| Memory ([N18], [FGHN]) | PARTIALLY GROUNDED: nearest candidates grounded and shown to be rung-2-level; rung-3 observable OPEN (candidate shape H-mem) |
| Loop status | CITATION-LEVEL ([LS] abstract fetched; [BDN],[HHW],[BDDN],[S20] snippet-level) — typed residual |
