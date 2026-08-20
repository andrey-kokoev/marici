# Source and boundary packet: the sub-subleading triangle maps (marici.Strominger)

Companion to `subsubleading-triangle-conventions.md` (sources, grounding
ledger, gauge prescription G_CS2, hypotheses H-A..H-E, external inputs are
there). This packet exports the actual maps and the check items that
`checkers/subsubleading_triangle_exact_checks.py` (sympy) and
`marici-triangle/src/bin/subsubleading.rs` (Symbolica) verify, with
identical check IDs in both engines. Same rule as the rungs 1–2 packets:
nothing is proved by citing the correspondence; every link is a check item
with a declared left and right side, and every discrepancy is a typed
residual in the results JSONs.

Corners: sub-subleading soft factor [CS] = arXiv:1404.4091; the rung-3
Ward identity [CL16] = Campiglia–Laddha arXiv:1605.09094, with [CL15] =
arXiv:1502.02318 as the falsifiable smooth-charge baseline; memory
candidates [N18] (Nichols, CM memory) and [FGHN] (persistent observables,
abstract-level). Inherited from rungs 1–2: [HMLS] = arXiv:1401.7026,
[KLPS] = arXiv:1406.3312, [PSZ] = arXiv:1502.06120.

## 1. The maps and their grounded formulas

**Soft corner.** [CS (9)], tree level:
\(S^{(2)}=-\frac12\sum_a E_{\mu\nu}(q\cdot J_a)^\mu(q\cdot J_a)^\nu
/(q\cdot k_a)\), with \((q\cdot J_a)^\mu=q_\rho J_a^{\rho\mu}\).
CS state the per-leg gauge invariance holds "and not as a consequence of
any conservation law" — the mechanism is the antisymmetry of \(J_a\)
alone (CS lines 137–139): under the declared shift
\(\delta E_{\mu\nu}=q_\mu\Lambda_\nu+\Lambda_\mu q_\nu\) (G_CS2,
inherited from rung-2 G_CS) the per-leg variation is
\(2\Lambda_\mu(q\cdot J)^\mu{}_\nu(q\cdot J)^\nu\)-type and vanishes
because \(q_\mu(q\cdot J)^\mu=0\) identically. Spinor form [CS (20)]:
\(S^{(2)}=\frac12\sum_a\frac{[sa]}{\langle sa\rangle}
\tilde\lambda_s^{\dot a}\tilde\lambda_s^{\dot b}
\partial^2/\partial\tilde\lambda_a^{\dot a}\partial\tilde\lambda_a^{\dot b}\),
reference-spinor free. Holomorphic soft limit [CS (21)–(22), (28)]:
\(\lambda_s\to\varepsilon\lambda_s\), \(\tilde\lambda_s\) fixed, giving
the pole ladder \(\varepsilon^{-3}/\varepsilon^{-2}/\varepsilon^{-1}\)
for \(S^{(0)}\) [CS (17)], \(S^{(1)}\) [CS (18)], \(S^{(2)}\) [CS (20)].

**Ward corner.** [CL16 (14)]: the sub-subleading soft insertion as a
boundary operator,
\(S^{(2)-}=\frac{1}{2\omega}\sum_i\frac{1}{q\cdot k_i}
(\varepsilon^-_\mu q_\nu J_i^{\mu\nu})^2\) (our normalization; see the
typed residual T2.3c). The smearing identity [CL16 (15)]:
\(\frac{1}{2\pi}D_z^4 S^{(2)-}
=-3\sum_i E_i^{-1}\delta^{(2)}(z,z_i)\partial^2_{z_i}+\dots\)
— all terms proportional to (derivatives of) \(\delta^2\). The charges
[CL16 (17)–(18)]: \(O(r)\) large diffeomorphisms \(rX^A\partial_A\) with
divergence-free \(X^A\), electric parity \(Q_{rX}\) with the DOUBLE
retarded-time integral \(\int du\int^u du'\), magnetic half
\(\tilde Q_{rX}\) added as "+ c.c." [CL16 (17)] — no first-principles
derivation (CL16 lines 115–120, open sub-item).

**Memory corner.** No rung-3 observable is formula-grounded. The
nearest grounded candidates are rung-2 grade: the CM memory [N18] is a
SINGLE retarded-time integral (grade \(D_z^3\)); the rung-3 candidate
(H-mem) is a DOUBLE integral at grade \(D_z^4\), structurally the
first-moment observable \(\int^u u' F(u') du' = u\int^u F-\int\int^u F\)
with \(F\) playing \(D_z^4 C_{zz}\) [CL16 (17) structure; FGHN
framework abstract-level only]. Existence as a measurable persistent
observable remains OPEN.

## 2. The declared distributional fold (load-bearing prescription)

The Ward-corner checks use one declared prescription, stated here once:

- \(P=(\bar z-\bar z_k)^{-1}\) is antiholomorphic: its regular
  \(z\)-derivative vanishes and
  \(\partial_z P=\pi\delta^2(z-z_k)\) (rung-1 declared prescription,
  inherited; rung-2 used the conjugate statement).
- The strike delta carries weight one higher than the factor it struck:
  the fold of \(D_z^n(G\cdot P)\) runs over the weight sequence
  \((w_0,w_0+1,\dots,w_0+n-1)\) with \(w_0=-1\) (P itself), so the
  plain-\(\delta\) term has weight 0, \(\partial_z\delta\) weight 1,
  \(\partial_z^2\delta\) weight 2.
- The weight-0 start is FORCED, not arbitrary: with the naive sequence
  \((0,1,2,3)\) the regular part of \(D_z^4(GP)\) does not vanish
  (check T3.4b pins the obstruction exactly); the scan over
  \(w_0\in\{-3..3\}\) selects \(w_0=-1\) uniquely (scratch scan,
  conventions packet development notes; the checker witnesses the two
  adjacent cases).
- Products \(f\,\partial_z^j\delta^2\) are reduced at the pole by
  Leibniz: \(f\,\partial^j\delta=\sum_i(-1)^i\binom{j}{i}
  (\partial_z^i f)|_{z=z_k}\,\partial^{j-i}\delta\).

This is the rung-2 fold of the KLPS (6.7)/(6.12) scaffold extended by
one grade; cross-rung consistency is check T4.1.

## 3. Check items (checker specification; IDs shared by both engines)

- **T1 (soft-corner gauge).** T1.1: \(q_\mu q_\nu J^{\mu\nu}=0\)
  identically for antisymmetric \(J\) (CS lines 137–139 mechanism).
  T1.2: per-leg gauge variation of [CS (9)] under G_CS2 vanishes
  IDENTICALLY — no conservation law, no \(\Sigma\)-constraint. T1.3:
  the two-leg sum with independent generic \(J_1,J_2\) vanishes
  leg-by-leg, no inter-leg cancellation. T1.4 (deliberate failure):
  with the symmetric mutation \(J\to S\) the variation is nonzero — the
  antisymmetry is load-bearing. T1.5 (pattern break): the RUNG-2-grade
  contraction \(\Lambda_\mu q_\nu J^{\mu\nu}\) is nonzero per leg
  without \(\sum_a J_a=0\) — the \(\mathcal P\to\mathcal J\) escalation
  terminates at rung 3. T1.6: operator form on the sphere,
  \(\mathrm{op}(q)=0\) (the \(\varepsilon\to\varepsilon+\alpha q\)
  freedom leaves \(C=(\varepsilon\cdot q\cdot J)\) invariant per leg).
- **T2 (spinor corner).** T2.1: [CS (20)] on bracket monomials,
  \(\tilde\lambda_s^2\partial^2_{\tilde\lambda_a}[a,b]^m
  =m(m-1)[s,b]^2[a,b]^{m-2}\), \(m=2,3,4\). T2.2: the [CS (28)] pole
  ladder \(\varepsilon^{-3/-2/-1}\) under \(\lambda_s\to
  \varepsilon\lambda_s\). T2.3: [CS (9)] vs [CL16 (14)] normalization —
  T2.3a contraction identity, T2.3b the per-leg ratio is exactly
  \(-\omega\), T2.3c typed residual: the ratio is \(-\omega\), not 1
  (same family as the rung-2 \(\kappa\) residual S3).
- **T3 (Ward fold).** T3.1: per-leg
  \(C=(\varepsilon^-\cdot q\cdot J)\) operator
  \((c_{z_k},c_{\bar z_k},c_{E_k})
  =(-\sqrt2\,\omega(z-z_k)^2/(1+z\bar z),\ 0,\
  -\sqrt2\,E_k\omega(z-z_k)(1+z\bar z_k)/((1+z\bar z)(1+z_k\bar z_k)))\)
  — regular in \(\bar z\) (the antiholomorphic pole of [KLPS (6.6)] is
  cancelled by \(q\cdot k\)). T3.2: the \(S^{(2)-}\) channels of
  \(\omega^{-1}(2q\cdot k)^{-1}C^2\):
  \(A_{\partial_z^2}=-(z-z_k)^3(1+z_k\bar z_k)/(2E_k(\bar z-\bar z_k)
  (1+z\bar z))\),
  \(A_{\partial_z\partial_E}=-(z-z_k)^2(1+z\bar z_k)/((\bar z-\bar z_k)
  (1+z\bar z))\),
  \(A_{\partial_E^2}=-E_k(z-z_k)(1+z\bar z_k)^2/(2(\bar z-\bar z_k)
  (1+z\bar z)(1+z_k\bar z_k))\),
  \(A_{\partial_z}=(z-z_k)^2(1+z_k\bar z_k)/(E_k(\bar z-\bar z_k)
  (1+z\bar z))\),
  \(A_{\partial_E}=0\) identically; \(\omega\) cancels throughout.
  T3.3: single-pole structure — every channel is \(G\cdot(\bar z-\bar
  z_k)^{-1}\) with \(G\) finite at \(\bar z=\bar z_k\). T3.4a: [CL16
  (15)] structural core — with the declared weight sequence
  \((-1,0,1,2)\) the regular part of \(D_z^4 S^{(2)-}\) vanishes in ALL
  channels ("all terms proportional to deltas" holds exactly). T3.4b:
  the weight choice is forced (naive \((0,1,2,3)\) leaves a nonzero
  regular part, pinned). T3.5: the \(\partial_z^2\) channel is PURE
  plain-\(\delta\) (T3.5a) with coefficient exactly \(-3\pi/E_k\)
  (T3.5b); T3.5c typed residual: printed [CL16 (15)] gives \(-6\pi/E_k\)
  in our normalization — the computed delta is uniformly HALF the
  printed one (candidate \(\delta^2\)-normalization drift, same family
  as rung-2 S10.2/S10.3e). T3.6: the unprinted "\(\dots\)" content of
  [CL16 (15)] named exactly — \(\partial_z\partial_E\) channel:
  \(-8\pi\bar z_k/(1+z_k\bar z_k)\,\delta-2\pi\,\partial\delta\);
  \(\partial_E^2\) channel: \(-6\pi E_k\bar z_k^2/(1+z_k\bar z_k)^2\,
  \delta-3\pi E_k\bar z_k/(1+z_k\bar z_k)\,\partial\delta
  -(\pi E_k/2)\,\partial^2\delta\); \(\partial_z\) channel:
  \(2\pi\bar z_k/(E_k(1+z_k\bar z_k))\,\delta+(2\pi/E_k)\,
  \partial\delta\). T3.7: electric/magnetic doubling — \(C^+\) is the
  exact \(\sigma\)-conjugate of \(C^-\) at operator level (the "+ c.c."
  of [CL16 (17)/(18)] is exact).
- **T4 (cross-rung ladder).** T4.1: the fold recursion at \(n=3\),
  sequence \((0,1,2)\), reproduces rung-2's declared fold coefficients
  exactly on a test function with NONZERO \(c_P\) (non-vacuous). T4.2:
  the derivative-grade ladder as one recursion — \(D_z^2=d^2-\Gamma d\),
  \(D_z^3=d^3-3\Gamma d^2+(2\Gamma^2-\Gamma')d\),
  \(D_z^4=d^4-6\Gamma d^3+(11\Gamma^2-4\Gamma')d^2
  +(7\Gamma\Gamma'-\Gamma''-6\Gamma^3)d\) on weight-0 scalars. T4.3:
  the time-integral ladder — T4.3a the double retarded primitive is the
  first-moment observable \((uA-S)'=uF\) with \(A=S'\), \(F=S''\);
  T4.3b boundary terms vanish in the [CL16 footnote 2] falloff class;
  T4.3c the \(\int^2\) and \(\int^1\) grades are distinct (CM memory
  sits at \(\int^1\), rung 2). T4.4: the zero-frequency projector
  ladder — \((1+\omega\partial_\omega)\) kills \(a/\omega\) [KLPS
  (5.33), rung 2]; \((2+\omega\partial_\omega)(1+\omega\partial_\omega)\)
  kills \(a/\omega^2\) and \(b/\omega\) and acts as \(2\times\) on the
  finite part (finite-part prescription for the \(\omega^{-1}\) moment
  of [CL16 (14)]).
- **T5 (deliberate-failure controls, INVERTED relative to rung 2).**
  T5.1: H-A anti-test — removing every \(\Sigma\)-constraint changes
  NOTHING at the rung-3 gauge step (backed by T1.2/T1.3 zero vs T1.5
  nonzero). T5.2: H-B baseline obstruction — the rung-2-grade \(D_z^3\)
  smearing (sequence \((-1,0,1)\)) applied to the rung-3
  \(\partial_z^2\) channel leaves a nonzero regular part, pinned exactly
  as \(-3(1+\bar z z_k)^3(1+z_k\bar z_k)/(E_k(1+z\bar z)^4
  (\bar z-\bar z_k))\); the \(D_z^4\) grade is forced. T5.3:
  genuinely-wrong mutation — polluting [CS (20)] with a leg spinor
  (\(\tilde\lambda_s\tilde\lambda_a\partial^2\)) breaks the bracket
  identity; residual \(-15136/2205\) at the exact rational point.
- **T6 (verdict record).** Synthesis of T1–T5 over H-A..H-E (below).

## 4. Hypothesis verdicts (both engines agree)

- **H-A SUPPORTED** for the checkable core: per-leg gauge invariance
  needs no conservation law (T1.2/T1.3/T1.6), and the smeared identity
  closes with no \(\Sigma\)-input (T3.4a) — closure is kinematic, the
  \(\mathcal P\to\mathcal J\) escalation terminates (T1.5).
- **H-B FALSIFIED as baseline** (T5.2): no smooth generalized-BMS
  (single-\(u\)-integral) charge class reproduces the rung-3
  distributional identity.
- **H-C SUPPORTED up to the uniform factor-\(\tfrac12\) delta drift**
  (T3.5c, same family as rung-2 S10); the "\(\dots\)" channels named
  exactly (T3.6); electric/magnetic doubling exact at operator level
  (T3.7). The magnetic half \(\tilde Q_{rX}\) first-principles
  derivation remains an open sub-item (CL16 lines 115–120).
- **H-D SUPPORTED at tree level** (T4.1/T4.2/T4.4); FPR collinear/
  nonlinear corrections are a typed residual beyond tree level.
- **H-mem: structural content verified** (T4.3: double retarded-time
  integral = first-moment observable, distinct from the rung-2 CM
  grade); existence of a measurable rung-3 persistent observable remains
  OPEN (FGHN abstract-level only).
- **H-E: the named residual of this rung is the half-strength delta
  drift (T3.5c), not a closure failure.**

## 5. Typed residuals (none absorbed)

1. **T2.3c**: [CS (9)]/[CL16 (14)] per-leg ratio is exactly
   \(-\omega\) (the \(\omega^{-1}\) and \((2k\cdot q)^{-1}\) vs overall
   \(-\tfrac12\) conventions; same family as the rung-2 \(\kappa\)
   residual S3).
2. **T3.5c**: computed plain-\(\delta\) coefficient \(-3\pi/E_k\) is
   uniformly HALF the printed [CL16 (15)] value \(-6\pi/E_k\) (candidate
   \(\delta^2\)-normalization drift, same family as rung-2
   S10.2/S10.3e).
3. Magnetic half \(\tilde Q_{rX}\): no first-principles derivation
   (CL16 lines 115–120) — open sub-item, not checked.
4. FPR collinear/nonlinear corrections to \(S^{(2)}\) beyond tree
   level — typed residual, not checked.
5. Loop-level non-universality of \(S^{(2)}\) (BDN/HHW/BDDN; LS
   salvage) — citation-level only, typed residual.
6. FGHN persistent-observable framework is abstract-level grounded
   only; the rung-3 memory observable (H-mem) is a hypothesis, not a
   citation.

## 6. External inputs ledger (final for this triangle)

1. Tree-level restriction of \(S^{(2)}\) (CS lines 139–152; conventions
   packet §7).
2. The holomorphic soft path \(\lambda_s\to\varepsilon\lambda_s\),
   \(\tilde\lambda_s\) fixed (CS (21)–(22), (28); packet §3).
3. Declared gauge shift \(\delta E_{\mu\nu}=q_\mu\Lambda_\nu
   +\Lambda_\mu q_\nu\) (rung-2 G_CS, inherited; packet §3 G_CS2).
4. Distributional prescription \(\partial_z(\bar z-\bar z_k)^{-1}
   =\pi\delta^2\) (rung-1 declared prescription, inherited; §2).
5. Declared fold weight sequence \((-1,0,1,2)\) for the stripped
   \(S^{(2)-}\) operator coefficients — fixed by the
   vanishing-regular-part requirement, uniqueness witnessed by T3.4b.
6. Antipodal matching at \(i^0\) [HMLS 3.1–3.3], inherited; corner
   matching for the \(O(r)\) rung-3 generators is OPEN (packet §9).

No other input. The soft–BMS–memory correspondence is nowhere invoked
as proof; each link above is a check item executed identically by both
engines, with the typed residuals of §5 reported, never absorbed.
