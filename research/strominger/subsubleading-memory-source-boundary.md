# Source and boundary packet: the rung-3 (ballistic) memory checks (marici.Strominger)

Companion to `subsubleading-memory-candidate.md` (candidate derivation
M1–M4, hypotheses C1–C6, obstruction O1, residuals R1–R5 — sources,
grounding ledger, and external inputs are there) and to
`subsubleading-triangle-source-boundary.md` (rung-3 soft/Ward triangle).
This packet exports the check items that
`checkers/subsubleading_memory_exact_checks.py` (sympy, 65 checks) and
`marici-triangle/src/bin/subsubleading_memory.rs` (Symbolica, 65 checks)
verify, with **identical check IDs and pass/fail semantics in both
engines**, differed by `checkers/diff_subsubleading_memory_results.py`
(identical ID sets, identical verdict per ID, zero mismatches). Same rule
as the rungs 1–3 packets: nothing is proved by citing the correspondence;
every link is a check item with a declared left and right side, and every
discrepancy is a typed residual in the results JSONs.

Sources: PSZ = Pate–Sharma–Zimmerman arXiv:1502.06120; CL16 =
Campiglia–Laddha arXiv:1605.09094; G24 = Grant arXiv:2312.02295; GN22 =
Grant–Nichols arXiv:2109.03832; FPR = arXiv:2111.15607; S20 = Sahoo
arXiv:2008.04376. Grounding ledger with line citations:
`subsubleading-memory-candidate.md` §1.

## 1. Engine-equivalence ledger (how the Symbolica port computes)

The sympy suite calls `sp.integrate`, `sp.limit`, and `sp.series` on
witnesses containing `atan`, `log`, and `exp`. Symbolica carries no
transcendental calculus, so the port performs the **equivalent exact
computation** — never a weakened one:

- `atan(u)`, `log(u)`, `log(mu)` are exact symbols (`ata`, `lg`/`lgUt`,
  `lmuT`) with the **declared derivative rules**
  \(d\,\mathrm{ata}=du/(1+u^2)\), \(d\,\mathrm{lg}=du/u\). Every
  antiderivative the sympy suite gets from `sp.integrate` is instead
  **certified**: the derivative of the candidate primitive is checked
  symbolically against the integrand (M1.1, M1.2, M1.9, M1.10, M1.11,
  M1.12 certificates).
- Definite integrals over \((-\infty,\infty)\) or \([0,1]\) are exact
  endpoint evaluations of the certified primitives: rational limits at
  \(u\to\pm\infty\) by the \(u\to 1/t\) substitution (divergence detected
  through Symbolica's unsigned-infinity atom), polynomial integrals by
  exact coefficient extraction \(c_k=A^{(k)}(0)/k!\).
- Limits involving `atan`/`log` at \(+\infty\) use the exact identities
  \(\mathrm{atan}(u)=\pi/2-\mathrm{atan}(1/u)\) with the truncated atan
  series \(t-t^3/3+t^5/5-t^7/7\) (far beyond the order any check
  inspects) and \(\log(u)=-\log(1/u)\); a surviving `log t` term or a
  negative \(t\)-power is exactly the divergent case (M1.11a).
- M1.14's `sp.series(..., eps, 0, 4).removeO()` is the exact truncated
  series of \(\log(1+a\varepsilon)\) and \((1+a\varepsilon)^{-2/-3}\)
  through \(\varepsilon^3\), coefficient-extracted after expansion.
- M2's Gaussian moments use the exact integration-by-parts recurrence
  \(G_k=\frac{k-1}{2}G_{k-2}\) with \(G_1=0\) (odd symmetry); \(G_0
  =\sqrt\pi\) is a **declared external exact input** carried as the
  symbol `sqpi`. The Fourier side uses the exp series truncated at
  exactly the order the check inspects (\(\omega^5\)).
- M5's formal sift \(u\,\delta(u-u_k)=u_k\delta(u-u_k)\) is applied per
  delta channel by exact coefficient extraction (each expanded term
  carries a single \(d_k\) factor).
- \(\sqrt2\) is carried as the symbol `sq2` reduced by \(sq2^2=2\)
  (exponents \(\pm2,\pm3,\pm4,\pm6,\pm8\)), as in the rung-2 port.

No check was dropped, renumbered, or weakened; pass/fail semantics are
identical, and the differ enforces it.

## 2. Check items (checker specification; IDs shared by both engines)

### M1 — C1 port: CL16 double-u integral structure (23 checks)

Left side: the double retarded primitive \(I_2(U)=\int^U\!\int^u F\) and
the moments \(I_1,M_1\) of the \(u^{-3}\)-tail witness
\(F=(2+u)/(1+u^2)^2\) (CL16 footnote-2 borderline class,
`cl1605.09094.txt` lines 259–260). Right side: the ramp identity
\(I_2=UI_1-M_1\), the drift \(-M_1(\infty)\), and the CL16 (30)
finite-part subtraction \(Q=\lim(tQ^{(1)}+Q^{(0)})\) (lines 431–436;
double-u charge (17), lines 223–252).

- M1.1/M1.2: antiderivative certificates \(I_1'=F\), \(M_1'=uF\).
  GROUNDED + verified both engines.
- M1.3/M1.4: \(I_1(\infty)=\pi\), \(M_1(\infty)=\pi/2\). Verified.
- M1.5: \(I_2(U)=UI_1(U)-M_1(U)\) identically (FPR repeated-primitive vs
  CL16 moment bridge). Verified.
- M1.6 (obstruction O1): \(I_2(U)-UI_1(\infty)\to-\pi/2\) — nonzero
  finite part; the linear drift is the rung-2 content removed by CL16
  (30). Verified.
- M1.7: falloff class \(u^3F\to 1\) forces the drift. Verified.
- M1.8–M1.10: all-rational drift-free control
  \(F_0=\frac{d}{du}[2u/(1+u^2)^2]\): \(\int F_0=0\),
  \(\int u^2F_0=-2\pi\), bounded double primitive. Verified.
- M1.11/M1.11a (residual R5): the classical log tail \(C\sim u^{-2}\log
  u\) (S20) gives ballistic moment \((\log U)^2/2\), unbounded — outside
  the strict CL16/FPR class. Verified as a typed obstruction.
- M1.12–M1.12d: two-grade log finite part
  (\(\frac A2\log^2U+B\log U\) counterterms), running coefficient
  \(B_\mu=B+A\log\mu\), unavoidable scale ambiguity, one-cocycle
  composition, affine scale torsor independent of the \(D/u^3\) control.
  Verified; the *prescription* (choice of \(\mu\)) remains undeclared by
  the sources — typed residual (log-tail finite-part data).
- M1.13–M1.13a: retarded-time translation
  \(\mathcal M_3\mapsto\mathcal M_3-a\mathcal M_2\), additive second
  affine action. Verified.
- M1.14–M1.14c: minimal translation-closed tail jet \((A,B,E,D)\) with
  \(E'=E-2aA\), \(D'=D+aA-2aB\); \((A,B,D)\) truncation not closed
  (M1.14a, typed); scale and time-origin actions commute and compose.
  Verified.

### M2 — C1 flux side: Fourier ↔ moment, projector ladder (6 checks)

Left side: moments \(\mu_n\) of the Gaussian witness \(F=ue^{-u^2}\).
Right side: \(\hat F=i\omega\sqrt\pi/2\,e^{-\omega^2/4}\) and the
zero-frequency projectors \((2+\omega\partial_\omega)
(1+\omega\partial_\omega)\) (packet; rung-3 T4.4 heritage) and FPR
\(\partial_\omega(1+\omega\partial_\omega)\) (`fpr2111.15607.txt` lines
1414–1428).

- M2.1/M2.2: \(\mu_1=\sqrt\pi/2,\ \mu_3=3\sqrt\pi/4,\ \mu_5=15\sqrt\pi/8\);
  even moments vanish. Verified (declared input \(G_0=\sqrt\pi\), §1).
- M2.3: moment/Fourier series match through \(\omega^5\). Verified.
- M2.4–M2.6: packet projector kills \(\omega^{-2},\omega^{-1}\) poles
  (\(\mapsto 2c_0+6c_1\omega\)); FPR projector extracts \(2c_1\);
  composite extracts \(12c_1\). Verified.

### M3 — C3 burst: compact-support shear, candidate \(\mathcal M_3\) identity (5 checks)

Left side: news moments of the bump shear \(C=u^3(1-u)^3\) on \([0,1]\).
Right side: the news/shear ladder
\(N^{(2)}=\frac12\int u^2\dot C\,du=-\int uC\,du=-1/280\) (packet §3;
GN22 (3.11), lines 953–961) and the curve-deviation observable GN22
(3.14) at \(n=0\) (lines 1001–1011).

- M3.1/M3.2: the candidate identity and bump moments
  (\(\int C=1/140\), \(N^{(1)}=-1/140\)). Verified.
- M3.3: \(\Delta\alpha^{(0)}=\frac1{2r}[3N^{(2)}-N^{(1)}]=-1/(560r)\).
  Verified.
- M3.4/M3.5: double shear primitive \(I_3(1)=1/280\), ramp continuation
  \(I_3(U)=U/140-1/280\); CL16 (30) finite part
  \(\mathrm{FP}[I_3-UI_2(1)]=-1/280=N^{(2)}\). Verified.

### M4 — C3 parity doubling (6 checks)

Left side: \(X^A=\epsilon^{AB}\partial_B\chi\),
\(\epsilon^{z\bar z}=-i/\gamma\) (candidate convention). Right side:
divergence-free condition, reality, and the electric (\(\sigma\)-even) vs
magnetic (\(\sigma\)-odd) decomposition of the second moment (GN22 §V,
lines 2272–2313; CL16 (19) split).

- M4.1/M4.2: \(D_AX^A=0\), \(\sigma(X^z)=X^{\bar z}\), both witnesses.
  Verified.
- M4.3: \(\sigma(\eth_s f)=\bar\eth_{-s}\sigma(f)\). Verified.
- M4.4/M4.5: electric/magnetic parity of \(D_zX_z\) and
  \(iD_zX'_z\). Verified.
- M4.6: \(l\)-degeneracy (\(\eth^2\,{}_0Y_{1m}=0\) grade) and
  nontriviality at \(l=2\). Verified.

### M5 — C2 burst: formal delta/Theta sifting (3 checks)

Left side: formal burst \(F=\sum_k c_k\,\delta(u-u_k)\) at exact rational
kinematics (\(c=(2,-3,5)\), \(u_k=(\frac14,\frac12,\frac34)\)). Right
side: PSZ (5.10) burst moments (grounded for \(T_{uz}\), not for the
burst shear — candidate packet C2) and the ramp/double-primitive
identity.

- M5.1: sift moments \(\int u^mF\,du=\sum c_ku_k^m\), \(m=0,1,2\).
  Verified under the declared formal rules.
- M5.2: Heaviside ramp \(I_2(U)=\sum c_k(U-u_k)\Theta(U-u_k)
  =UI_1(U)-M_1(U)\) at \(U=0,\frac38,2\); sift rule
  \((u-u_k)\delta(u-u_k)=0\). Verified.
- M5.3 (typed residual R-C2): full \(D_z^4\)-grade shear-response closure
  NOT grounded; single-outgoing-insertion coefficient \(-3\pi/E_k\sum
  c_ku_k\) is half the printed CL16 (15) \(-6\pi/E_k\sum c_ku_k\) (the
  T3.5c half-drift; crossing doubling resolved separately in M8.5).
  Verified as a typed obstruction.

### M6 — C4 pseudo-fluxes: G24 (3.14)–(3.16) (8 checks)

Left side: \(F^{\rm rad}_{2,1}=-3i\frac{d}{du}(\sigma\,\mathrm{Im}
[\eth^2\bar\sigma])\), \(F^{\rm nonrad}_{2,1}=-3\frac{d}{du}(m\sigma)\),
\(F_{2,0}=-3\sigma^2\dot{\bar\sigma}\) under \((m,\sigma)\to\varepsilon
(m,\sigma)\) (G24 (3.14)–(3.16), `grant2312.02295.txt` lines 633–716).
Right side: \(\varepsilon\)-degree typing vs the FPR cubic collinear
block \(t^C\) (FPR after (87); FPR (132) nonlocal action).

- M6.1: \(\mathrm{Im}[\eth^2\bar\sigma]\) \(\sigma\)-real, nonzero.
  Verified.
- M6.2–M6.4: \(F^{\rm rad/nonrad}_{2,1}\) quadratic, \(F_{2,0}\) CUBIC.
  Verified.
- M6.5: radiative/non-radiative split in \(m\). Verified.
- M6.6: total-derivative structure, \(\int_0^1F^{\rm rad/nonrad}=0\)
  (boundary evaluation on the compact-support witness). Verified.
- M6.7 (anti-test): the quadratic pseudo-fluxes cannot be the collinear
  block. Verified — prior identification withdrawn (candidate packet C4).
- M6.8 (typed): the local cubic functional is not proportional to FPR
  (132)'s nonlocal \(\partial_u(C\partial_u^{-1}C)\) action; full
  corrected charge + symplectic transgression required. Verified as a
  typed obstruction.

### M7 — C5 spin calculus: eth ladder and grade (4 checks)

Left side: G24 (2.15a/b) raising/lowering on \(l=1,2,3\) harmonic
witnesses; \(\eth^4\) at spin \(\pm2\). Right side: eigenvalues
\(-\frac12(l-s)(l+s+1)\) family, the \(\eth^4\) eigenvalue
\((l-1)l(l+1)(l+2)/4\) (GN22 (4.58); G24 spin calculus (2.14)–(2.16)),
and the \(D_z^4=P^6\eth^4P^{-2}\) identity.

- M7.1: G24 (2.15a/b) eigenvalue identities. Verified.
- M7.2: \(\eth^4:\) spin \(-2\to+2\) with the (4.58) eigenvalue.
  Verified.
- M7.3: \(D_z^4T_{zz}=P^6\eth^4(P^{-2}T_{zz})\) on a generic rational
  spin-2 witness. Verified.
- M7.4: FPR repeated-primitive bracket differentiates to \(u^2N/2\).
  Verified.

### M8 — C6 normalization boundary (10 checks)

Left side: \(\kappa^2=32\pi G\) chain, FPR (103),(106),(129), CL16 (30),
PSZ (5.2),(2.1), FPR (2c),(36),(119). Right side: the linear
normalization \(\mathcal M_3=\frac{3\kappa^2}{4}t^S\) and the augmented
angular-momentum-aspect flux map.

- M8.1: \(1/(8\pi G)=4/\kappa^2\). Verified.
- M8.2/M8.2b/M8.2c: \(\mathcal M_3=\frac{3\kappa^2}{4}t^S\);
  \(t^S=-4Q^{\rm FP}_{\rm soft}/(3\kappa^2)\); outgoing-insertion
  coefficient \(-\kappa/(8\pi)\). Verified.
- M8.3/M8.4: \(u\)-weighted PSZ (5.2) closes only with the
  angular-momentum-aspect principal/corner cell; same-flux anti-test
  (\(T_{uz}=0\) admits nonzero first shear moment). Verified.
- M8.5: FPR crossing factor 2 converts the T3.5c insertion coefficient
  \(-3\pi\) to CL16's charge coefficient \(-6\pi\) exactly. Verified —
  residual R1 resolved.
- M8.6: PSZ↔FPR metric dictionary \(P_A=N_A+\frac34C_{AB}D_CC^{CB}
  -\frac{3}{32}\partial_A(C_{BC}C^{BC})\) (PSZ (2.1) vs FPR (2c)).
  Verified.
- M8.7/M8.7a: operator-level angular \(u\)-weighted PSZ (5.2) square;
  \(\partial_{\bar z}\) commutes with the time integral; the endpoint
  aspect cell completes the flux map; witness nontrivial. Verified.

## 3. Typed residuals (none absorbed)

1. **T3.5c half-drift** — RESOLVED at linear order: the computed
   single-outgoing-insertion plain-\(\delta\) coefficient is half the
   printed CL16 (15) charge value because the charge contains both
   crossed insertions [FPR after (119)]; M8.5 reproduces the factor
   exactly. M5.3 retains the underlying typing: the full \(D_z^4\)-grade
   burst shear response is not grounded by PSZ (5.10) alone.
2. **Magnetic half underived** (R3): no first-principles derivation of
   \(\tilde Q_{rX}\) (CL16 lines 115–120); the magnetic second moment
   exists memory-side (GN22 §V) but its Ward-side partner is incomplete.
   Not checked; M4 verifies only the parity typing.
3. **FPR collinear sector** (R2): the quadratic G24/GN22 pseudo-fluxes
   lie outside the tree-level Ward identity and cannot be FPR's cubic
   collinear block (M6.7); the cubic \(F_{2,0}\) is degree-compatible
   but not equal to the FPR (132) nonlocal action (M6.8). Open.
4. **Loop non-universality** of \(S^{(2)}\) (BDN/HHW/BDDN; LS salvage,
   arXiv:1706.00759) — citation-level only, typed residual; not checked.
5. **Log-tail finite-part data** (R5): the ballistic-memory functional is
   defined only on the strict CL16/FPR falloff class (M1.11/M1.11a
   obstruction proved). The two-grade log finite part is verified
   (M1.12), but its scale \(\mu\) is an affine-torsor ambiguity
   (M1.12a–d) with no source-derived preferred section; S20 fixes the
   universal \(\omega\ln^2\omega\) coefficient but not the finite-part
   scale. The retarded-time origin is a second independent torsor
   (M1.13–M1.13a); the natural datum is the four-grade jet
   \((A,B,E,D)\) (M1.14–M1.14c).
6. **Corner matching** (R4): antipodal matching for the \(O(r)\) /
   pseudo-vector-field generators is assumed, not established
   (conventions packet §9; FPR (127) assumes the same). Not checked.

## 4. Declared prescriptions (load-bearing, identical in both engines)

1. **CL16 (30) finite part** \(Q=\lim_{t\to\infty}(tQ^{(1)}+Q^{(0)})\):
   the linear drift \(UI_1(\infty)\) (rung-2 content) is subtracted;
   \(\mathrm{FP}\,Q^{\rm soft}_Y=-M_1(\infty)=-\mathcal M_3[Y]\).
2. **Distributional prescription** \(\partial_z(\bar z-\bar z_k)^{-1}
   =\pi\delta^2\) (rung-1 declared, inherited unchanged).
3. **Fold weight sequence** \((-1,0,1,2)\) for the \(D_z^4\) smearing
   (rung-3 boundary packet §2, inherited; uniqueness witnessed by T3.4b
   in the triangle suite).
4. **Formal burst rules** (M5): \(u\,\delta(u-u_k)=u_k\delta(u-u_k)\),
   \(\int\delta(u-u_k)du=1\), \(\Theta\) sampling at the nodes.
5. **Engine-level declared inputs** (Symbolica port, §1): derivative
   rules for `ata`/`lg`/`lmuT`; \(G_0=\sqrt\pi\) Gaussian integral;
   \(\log(1)=0\); the hermitian zero-frequency prescription inherited
   from the candidate packet.

## 5. Dual-engine status

- sympy: `checkers/subsubleading_memory_exact_checks.py` →
  `results/subsubleading_memory_exact_checks.json`, 65/65.
- Symbolica: `marici-triangle/src/bin/subsubleading_memory.rs` →
  `results/subsubleading_memory_symbolica_checks.json`, 65/65, 65/65
  agreement.
- differ: `checkers/diff_subsubleading_memory_results.py` → identical
  check-ID sets, identical verdict per ID, 0 mismatches (exit 0).

No other input. The soft–BMS–memory correspondence is nowhere invoked as
proof; each link above is a check item executed identically by both
engines, with the typed residuals of §3 reported, never absorbed.
