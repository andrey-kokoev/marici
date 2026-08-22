---
author: marici.Figueiredo
---

# First-Harmonic Universality: det[H_u, H_d] Over All One-Cycle Nine-Link Topologies (WP13)

## Question

WP12 (entry 1903) established \(\det[H_u,H_d] = 2iK_v\sin\phi\) exactly at the
61 *fitted* carrier-groupoid vertices. The operator asked for the
support-general theorem: does first-harmonic-only hold over **all** one-cycle
nine-link topologies, and what are the exact hypotheses? Equivalently: is the
Laurent support of \(\det[H_u,H_d]\) in \(z = e^{i\phi}\) contained in
\(\{-1,+1\}\) for every viable sparse Yukawa support, with the phase on the
unique cycle — and when exactly is the coefficient identically zero?

## Result

**Theorem (first-harmonic universality).** Let \(Y_u, Y_d\) be \(3\times3\)
matrices whose combined nine-node field graph has nine edges, is connected
(hence \(b_1 = E - V + 1 = 1\), a unique cycle \(\gamma\)), with each sector
admitting a perfect matching, all entries real positive except a single phase
\(z = e^{i\phi}\) on one edge of \(\gamma\). Then

\[
\det\nolimits[Y_uY_u^\dagger,\;Y_dY_d^\dagger]
= i\,A(\text{magnitudes})\sin\phi ,
\]

i.e. the Laurent support of the commutator determinant in \(z\) is contained
in \(\{-1,+1\}\) with exact antisymmetry \(a_{-m} = -a_m\) and \(a_0 = 0\).
Moreover \(A \equiv 0\) (as a polynomial in the magnitudes) **iff** \(\gamma\)
is a sector-pure 4-cycle on a quark-doublet pair \(\{a,b\}\) and the third
doublet node \(r\) has no derived H-link to one of \(\{a,b\}\) (one of the
pairs \((r,a),(r,b)\) is absent from the off-diagonal support of both
\(H_u\) and \(H_d\)). In every other case \(A\) is a nonzero polynomial.

Certificate: the support class contains **6552** viable one-cycle supports,
forming **18** orbits under \(S_3(Q)\times S_3(u^c)\times S_3(d^c)\) plus
\(u\leftrightarrow d\) swap (14 orbits with cycle length 4, 4 with length 6).
Testing every cycle edge of each orbit representative — **80** (support,
phase-edge) cases — with nine free magnitude symbols (exact symbolic Laurent
arithmetic) gives: 68 cases support exactly \(\{-1,+1\}\), 12 cases
identically zero, **zero higher-harmonic cases**, exact CP antisymmetry in
all 80, and the symbolic classification matches an independent exact rational
(Fraction) census case by case. Orbit invariance (row/column permutations
conjugate \(H_u,H_d\) by permutation matrices and leave \(\det C\) invariant;
swap maps case to case) extends the certificate to all 6552 supports. The 12
identically-zero cases are precisely the three orbits
\((\mathrm{mask}_u,\mathrm{mask}_d) \in \{(84,119), (85,118), (85,220)\}\)
satisfying the dichotomy condition; **no fitted WP9 chart lies in a zero
orbit** (checked: 0/61), and all 61 fitted charts regression-pass.

## Proof

Write the phase edge as \((q^*, c^*)\) with \(c^*\) an up-sector centre (the
\(u\leftrightarrow d\) swap covers the other choice). Then

\[
H_u(z) = H_0 + zE + z^{-1}E^\dagger,\qquad
E = m\,|s\rangle\langle q^*|,\quad
|s\rangle = \sum_{q \in N(c^*)\setminus q^*} m_q |q\rangle ,
\]

with \(E^2 = 0\) (since \(q^* \notin \mathrm{supp}\,s\)), and \(H_d\)
\(z\)-free. With \(C_0 = [H_0, H_d]\), \(P = [E, H_d]\), \(Q = [E^\dagger,
H_d]\), the exact identity \(\det C = \tfrac13\operatorname{tr} C^3\) for a
\(3\times3\) commutator (gated numerically in WP12) gives the coefficient
identities

\[
a_3 = \operatorname{tr} P^3,\qquad
a_2 = \operatorname{tr}(C_0 P^2),\qquad
a_1 = \operatorname{tr}(C_0^2 P) + \operatorname{tr}(P^2 Q).
\]

(The identity \(a_1 = \operatorname{tr}(C_0^2P) + \operatorname{tr}(P^2Q)\)
was verified exactly: for orbit representative \((85,122)\),
\(\operatorname{tr}(C_0^2P) = 91\,980\,016\,128\) and
\(\operatorname{tr}(P^2Q) = 62\,597\,510\,976\) sum to the \(\det C\)
coefficient \(154\,577\,527\,104\).)

**Step 1: \(a_3 = 0\) for any single-phase-entry \(H_u\).** With
\(A = |s\rangle\langle q^*|H_d\), \(B = H_d|s\rangle\langle q^*|\),
\(\alpha = \langle q^*|H_d|s\rangle\), one computes \(A^2 = \alpha A\),
\(B^2 = \alpha B\), \(AB = \langle q^*|H_d^2|s\rangle\,|s\rangle\langle q^*|\),
\(BA = 0\), hence \(P^3 = m^2\alpha^2 P\) and
\(\operatorname{tr} P^3 = m^2\alpha^2 \operatorname{tr} P = 0\) since \(P\) is
a commutator. No sparsity is used.

**Step 2: derived labelled multigraph and the unicyclic classification.**
Contract each centre (a \(u^c\) or \(d^c\) node) \(c\) to a clique on its
doublet neighbourhood \(N(c)\), labelled \(c\), producing a labelled
multigraph on the three \(Q\) nodes. Field-graph cycles are exactly closed
derived walks with pairwise distinct labels, so \(b_1 = 1\) forces one of:

- **Type I (4-cycle):** one pair \(\{a,b\}\) carries exactly two labels
  \(\{c^*, c_2\}\); every other pair carries at most one label; and the third
  node \(r\) attaches to **at most one** of \(a, b\) (a label \(x\) on both
  \((r,a)\) and \((r,b)\) would force \(x\) to be a degree-3 centre also
  labelling \((a,b)\), raising \(b_1\); two distinct such labels create a
  distinct-label triangle).
- **Type II (6-cycle):** all three pairs carry exactly one label, all
  distinct (labels \(\{a,b,a\}\)-style repetitions force a shared centre,
  contradicting multiplicity one).

**Step 3: \(a_2 = 0\) by the bichromatic obstruction.** Expanding
\(P^2 = m^2(\alpha(A+B) - \beta |s\rangle\langle q^*|)\) with
\(\beta = \langle q^*|H_d^2|s\rangle\) and using
\(\{H_d, [H_0,H_d]\} = [H_0, H_d^2]\),

\[
a_2 = m^2\big[\alpha\,\langle q^*|[H_0, H_d^2]|s\rangle
- \beta\,\langle q^*|C_0|s\rangle\big].
\]

Every monomial in this expansion is a walk product in which some \(Q\)-\(Q\)
pair would have to carry both a \(u\)-label \(\neq c^*\) and a \(d\)-label,
or a second independent cycle would have to exist. Case analysis:

- *Type II:* \(\deg c^* = 2\), the pair \((q^*,q')\) is \(u\)-only, so
  \(\alpha = 0\). Then \(\beta \neq 0\) requires both remaining pairs
  \(d\)-labelled, in which case \(\langle q^*|C_0|q'\rangle = 0\) (no
  \(u\)-links remain); if exactly one remaining pair is \(d\)-labelled,
  \(\beta = 0\); if none, both factors vanish.
- *Type I, \(\deg c^* = 2\), \(c_2\) up-type:* \(H_d^{ab} = 0\) gives
  \(\alpha = 0\), and \(\beta\) needs \(d\)-paths \(a\)-\(x\)-\(b\), forcing
  links to both sides of the cycle — excluded — so \(\beta = 0\).
- *Type I, \(\deg c^* = 2\), \(c_2\) down-type:* the expansion reduces to
  \(-m^2 m_b^2 (H_d^{ab})^2\,(H_d^{rx} H_0^{rx})\)-type terms (\(x\) the
  side where \(r\) attaches), each needing pair \((r,x)\) to be both up- and
  down-labelled — zero.
- *Type I, \(\deg c^* = 3\):* \(c^*\) labels all three pairs, so \(H_0\) is
  diagonal; then \(\langle a|C_0|s\rangle = m_b(h_a - h_b)H_d^{ab}\),
  \(\langle a|[H_0,H_d^2]|s\rangle = m_b(h_a - h_b)(H_d^2)^{ab}\),
  \(\beta = m_b (H_d^2)^{ab}\), and the two terms cancel identically.

**Step 4: antisymmetry.** \(z \leftrightarrow z^{-1}\) is complex
conjugation; \(\det C\) is anti-Hermitian-valued with real coefficients,
hence \(a_{-m} = -a_m\) and \(a_0 = 0\). This is structural, not
combinatorial.

**Step 5: the zero dichotomy.** For the coefficient \(A = a_1/i\): in the
three zero orbits the cycle is a sector-pure 4-cycle on \(\{a,b\}\) and one
of the pairs \((r,a),(r,b)\) is entirely absent; every closed walk
contributing to \(\operatorname{tr}(C_0^2P) + \operatorname{tr}(P^2Q)\) then
requires the absent pair or a second cycle. The mechanism is transparent when
one sector is monomial (\(H_u\) diagonal): \(\det C\) is proportional to the
difference of the two oriented triangle products
\(H_d^{01}H_d^{12}H_d^{20} - \mathrm{c.c.}\), which vanishes identically when
a pair is absent. Exhaustion over the 18 orbits (symbolic certificate) proves
both directions: exactly the orbits \((84,119), (85,118), (85,220)\) and all
their members have \(A \equiv 0\).

Steps 1–4 are exact symbolic manipulations verified by the checkers; Step 5
and the per-orbit nonvanishing of \(A\) are certified by the symbolic
confirmation over all 80 cases with nine free magnitude symbols — no
polynomial-identity-testing gap remains.

## Interpretation

- The WP12 sine form was not an accident of the fitted sample: it is a
  theorem on the whole one-cycle nine-link class. The only \(\phi\)-channel
  from loop data into weak-basis invariants is \(\sin\phi\), universally.
- The unoriented pushforward of WP12 is thereby promoted: on every viable
  topology, \(\{\phi,-\phi\} \mapsto \{J,-J\}\) with
  \(\det[H_u,H_d] = -2i\,\hat J \prod_q m_q^2\); the orientation ambiguity of
  the chart is exactly the sign ambiguity of \(J\).
- The zero dichotomy has physical content: \(A \equiv 0\) topologies force
  \(J = 0\) for all \(\phi\) — they are CP-conserving charts, invisible to
  the CKM phase. All 61 fitted charts lie in the nonzero class, as they must
  to fit \(J \neq 0\).
- For the Marici admission question: the flavor lens datum survives chart
  descent only through the sine image. The theorem fixes the exact
  topological domain on which any future "loop-holonomy to observable" map
  must be defined, and the exact exceptional locus where it degenerates.
- Process note: the first census run reported 16 zero cases; four were an
  artifact of an order-dependent cycle-edge decode that silently dropped the
  phase (the assertion now gates this). The corrected count is 12, and the
  purity cross-tab hypothesis was revised accordingly — recorded here for
  audit honesty.

## Verification

- `research/flavor/checkers/wp13_all_topology_census.py` — exhaustive
  enumeration (6552 supports, 18 orbits, 80 phase cases), exact Fraction
  arithmetic, two generic magnitude assignments per case; 61/61 fitted-chart
  regression pass; output `results/wp13_all_topology_census.json`.
- `research/flavor/checkers/wp13_symbolic_confirmation.py` — exact symbolic
  (nine free magnitude symbols) Laurent support for all 80 cases; zero
  higher harmonics, zero mismatches against the rational census; output
  `results/wp13_symbolic_confirmation.json`.
- `research/flavor/checkers/wp13_zero_case_probe.py` — structural probe
  isolating the zero-dichotomy condition.
- Coefficient identities verified against direct \(\det C\) evaluation at
  exact rational points (example above).

## Relations

- Strengthens entry 1903 (WP12: fitted-vertex sine form) to the
  support-general theorem.
- Answers the remaining harmonic-support question attached to the WP11/WP12
  line: the Laurent dependence of \(\det[H_u,H_d]\) in \(z\) is
  first-harmonic-only on the entire one-cycle class, not only on S38/S43/
  S48/S53.
- Consistent with WP11 (entry on chart vs physical invariance): nothing here
  promotes \(\phi\) itself to a weak-basis invariant; the theorem constrains
  the *form* of its descent.
