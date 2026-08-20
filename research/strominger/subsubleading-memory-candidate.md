# The rung-3 memory corner: the ballistic-memory candidate and its
# master identity (marici.Strominger)

Companion to `subsubleading-triangle-conventions.md` /
`subsubleading-triangle-source-boundary.md` (rung 3, ledger entry 1096).
This packet attacks the OPEN memory corner of the sub-subleading triangle:
name the rung-3 observable or prove the obstruction. Outcome: **the
observable is named** — it is the *ballistic memory* (second moment of the
news / first moment of the shear), which we show is precisely the
\(\int^2\)-grade, \(D_z^4\)-grade object the Ward corner ([CL16 (17)])
demands — **and** the triangle closure at rung 3 is written as an explicit
master identity with a named, typed residual (the nonlinear pseudo-flux /
collinear sector). Neither side of this identification exists in the
published literature as a joined statement; the two sides exist separately
and are grounded here formula-level.

Conventions inherited unchanged: \(\kappa^2=32\pi G\);
\(\gamma_{z\bar z}=2/(1+z\bar z)^2\); distributional prescription
\(\partial_z(\bar z-\bar z_k)^{-1}=\pi\delta^2\); hermitian zero-frequency
prescription \(\frac12(\lim_{\omega\to0^+}+\lim_{\omega\to0^-})\).

## 1. New-source grounding ledger (this session)

All PDFs fetched via `arxiv.org/pdf/<id>` and extracted with pypdf (the
HTML/ar5iv route remains broken). NUL bytes stripped from two extractions.

| item | status |
|---|---|
| [FGHN] = arXiv:1901.00021, Flanagan–Grant–Harte–Nichols, "Persistent gravitational wave observables: general framework" | grounded formula-level: `sources/fghn1901.00021.txt` (28 pages). Displacement memory (2.1) lines 227–236 (2 time integrals of Riemann); subleading displacement (2.2) lines 253–267 (3 integrals; "the additional time integral … is subleading in the expansion in energy that is used in the corresponding soft theorems", lines 268–274); velocity memory (2.3) lines 295–302 (1 integral); Table I lines 316–334 (max 3 integrals; 4+ only "with acceleration", footnote b line 335); observables "measure moments (in time) of the Riemann tensor" lines 145–147 |
| [GN22] = arXiv:2109.03832, Grant–Nichols, "Persistent gravitational wave observables: Curve deviation in asymptotically flat spacetimes" | grounded formula-level: `sources/gn2109.03832.txt` (22 pages). Moment of the news defined (3.11) lines 953–961; curve-deviation ↔ moments (3.12)–(3.14) lines 963–980; zeroth-moment charge/flux review (4.1)–(4.2) lines 1038–1050; "it is not yet known if the charge viewpoint would apply to all the moments of the news" lines 1044–1053; second-moment charge/flux §IV.2 lines 1293–1443, incl. the charge correction \(\tilde E^{(0)}_{ij}\) (4.20) line 1363 and the non-vanishing-in-vacuum pseudo-fluxes \(G^{(0,0)}_{\rm rad/nonrad}\) (4.18)–(4.19); electric/magnetic parity decomposition of first and second moments, §V lines 2272–2313 |
| [G24] = arXiv:2312.02295, Grant, "Higher Memory Effects in Numerical Simulations of Binary Black Hole Mergers" | grounded formula-level: `sources/grant2312.02295.txt` (14 pages). Second-moment charge equation (3.13) line 655, with \( \dot{\tilde\psi}_0=-\frac12(\tilde u-u)^2\eth^4\dot{\bar\sigma}+\dots\); pseudo-fluxes \(F^{\rm nonrad}_{2,1},F^{\rm rad}_{2,1},F_{2,0}\) (3.14)–(3.16); integrated second moment (3.17) line 704; shear-content formulas (3.25)–(3.27) lines 800–838 (rung-3 shear content at grade \(\eth^4\)); Wald–Zoupas charge ambiguity (3.20)–(3.22); numerics: second-moment contributions "roughly two orders of magnitude smaller" than zeroth, lines 1144–1148 |
| [SGN24] = arXiv:2403.13907, Siddhant–Grant–Nichols (PN signals of higher memories) | abstract-level grounded: moments of the news = charge + flux; "unlike the zeroth or first moments, the second moment of the news and its dual have radiative and non-radiative pseudo-flux terms in addition to the charge and the flux pieces" (abstract) |
| [G24b] = arXiv:2401.00047, Grant, "Persistent gravitational wave observables: Nonlinearities in (non-)geodesic deviation" | citation-level (names the second-moment effect "ballistic" memory; cited as ref [19] in [G24] line 165) |
| [GZ24] = arXiv:2403.05195, Geiller–Zwikel | abstract-level: \(w_{1+\infty}\) tower of higher-spin charges, "soft theorems, memories, and asymptotic symmetries … organized in a tower of sub\(^*\)-leading tripartite relationships" — the tower is proposed, the rung-3 memory ↔ \(S^{(2)}\) identity is not written there |
| [S20] = arXiv:2008.04376, Sahoo, classical sub-subleading | formula-level: classical waveform at \(u^{-2}\ln u\) early/late tails; the ordered region \(\omega\ll|\ell|\ll L^{-1}\) produces \(\frac12\omega\{\ln(\omega L)\}^2\), while lower logarithmic orders are discarded; the tail sector is not a persistent observable |
| [LS] = arXiv:1706.00759, Laddha–Sen | abstract-level (re-confirmed): universal + non-universal split of \(S^{(2)}\) to all loops in \(d\ge5\); no observable-side statement |

## 2. Literature-sweep verdict

**What exists published at rung-3 grade:** a hierarchy of "higher memory
effects" = temporal moments of the news [GN22 (3.11)],
\(N^{(n)}_{ij}(u_1,u_0)=\frac1{n!}\int_{u_0}^{u_1}du\,(u-u_0)^n N_{ij}\).
Zeroth moment = displacement memory (rung 1); first moment = drift memory =
spin + center-of-mass memories (rung 2); **second moment = "ballistic"
memory (rung 3)** [GN22, G24, SGN24; name from G24b]. Both electric and
magnetic parity parts of the second moment are written in [GN22 §V]. Its
charge/flux decomposition is [G24 (3.13)–(3.17)]; its PN waveform content
is [SGN24]; its NR morphology is [G24 §IV]. In the Riemann-integral count
of [FGHN], the ballistic memory is the 4-integral observable, one above the
3-integral subleading displacement (2.2).

**What does NOT exist published:** any identification of the ballistic
memory (or any rung-3 memory) with the sub-subleading soft factor
\(S^{(2)}\), with the [CL16] \(O(r)\) large-diffeomorphism charges, or with
the [FPR] spin-2 charge aspect. Witnesses: [GN22] lines 1044–1053 ("it is
not yet known if the charge viewpoint would apply to all the moments of the
news"); [G24] declines the symmetry discussion entirely (introduction:
"While these connections to symmetry algebras are interesting, we do not
discuss them further", lines 100–106); [FPR] `fpr2111.15607.txt` line 1584:
the spin-2 conservation law "puts us in a position to understand the nature
of the spin-2 memory effect, which is a question" left open. [GZ24]
proposes the tower abstractly. **The rung-3 memory corner as a *triangle*
corner was open; this packet writes the candidate identification.**

## 3. The candidate observable, defined exactly

**Definition (three equivalent forms).** Let \(Y_{zz}\) be the
symmetric-trace-free smearing datum built from a divergence-free sphere
vector field \(X^A\) via the [CL16 (19)] split
\(Y_{AB}=D_AX_B+\epsilon_B{}^CD_AX'_C\) (electric piece \(D_AX_B\),
magnetic piece \(\epsilon_B{}^CD_AX'_C\)). The rung-3 memory observable is
the smeared pair

\[
\boxed{\;
\mathcal M_3[Y]\;\equiv\;\int_{-\infty}^{\infty} du\;u\int d^2z\,\sqrt\gamma\,
Y_{zz}\,D_z^4 C_{zz}(u,z)\;+\;\mathrm{c.c.}\;}
\]

- **Domain:** the full retarded-time axis of \(\mathcal I^+\),
  \(u\in(-\infty,\infty)\), vacuum-to-vacuum processes with the [CL16
  footnote 2] falloff \(C_{AB}=O(u^{-2-\epsilon})\),
  \(\phi=O(u^{-1/2-\epsilon})\) (`cl1605.09094.txt` lines 259–260); sphere
  integral over the cut \(S^2\) with the inherited distributional
  prescription for the \(D_z^4\) fold (weight sequence \((-1,0,1,2)\),
  boundary packet §2, check T3.4).
- **Integrand grade:** \(D_z^4\) on the shear — one grade above the rung-2
  \(D_z^2C_{zz}\) of [PSZ (6.9)], matching the smearing ladder
  \(D_z^2\to D_z^3\to D_z^4\) (boundary packet T4.2).
- **Parity:** electric + magnetic pair via the \(X,X'\) split, mirroring
  the \((Q_{rX},\tilde Q_{rX'})\) pair [CL16 (8),(9),(19)] and the
  electric/magnetic decomposition of the second news moment [GN22 §V].
- **Moment form:** \(\mathcal M_3[Y]\) is the *first retarded-time moment*
  of the \(D_z^4\)-grade shear data.
- **Double-integral (charge) form:** with
  \(F(u)\equiv\int d^2z\sqrt\gamma\,Y_{zz}D_z^4C_{zz}(u)\),
  \[
  \int_{-\infty}^{U}du\int_{-\infty}^{u}du'\,F(u') \;=\; U\,I_1(U)\;-\;M_1(U),
  \qquad I_1=\!\int^u\!F,\quad M_1=\!\int^u\!u'F du',
  \]
  so the [CL16 (17)] soft charge is
  \(\displaystyle Q_Y^{\rm soft}=\lim_{U\to\infty}\big[U\,I_1(U)-M_1(U)\big]\),
  the [CL16 (30)] finite-part prescription \(Q=\lim_{t\to\infty}(tQ^{(1)}+Q^{(0)})\)
  discards the linear drift \(U\,I_1(\infty)\) — which is exactly the
  rung-2-grade (spin/CM) content — and the finite part is
  \[
  \mathrm{FP}\,Q_Y^{\rm soft} \;=\; -\,M_1(\infty) \;=\; -\,\mathcal M_3[Y].
  \]
  (sympy-verified, §5 M1/M4.)
- **News form:** for vacuum endpoints (\(C_{zz}\) and \(N_{zz}\) vanishing
  at \(u_{0,1}\)), integration by parts gives
  \[
  N^{(2)}_{zz}\;\equiv\;\tfrac12\!\int du\,u^2 N_{zz}\;=\;-\!\int du\,u\,C_{zz},
  \]
  i.e. *the first shear moment is minus the second news moment*: the
  candidate is exactly the ballistic memory of [GN22 (3.11)] at \(n=2\),
  smeared at grade \(D_z^4\)/\(\eth^4\) (sympy-verified, §5 M3). The grade
  match is [G24 (3.13)]: \(\dot{\tilde\psi}_0\supset
  -\frac12(\tilde u-u)^2\eth^4\dot{\bar\sigma}\), and [G24 (3.27)]: the
  shear content of the second moment sits under \(\eth^4\).

## 4. The rung-3 master identity (candidate; analog of PSZ (6.9))

Claim (tree level, finite-part prescription, antipodal matching assumed):

\[
\int d^2z\,\sqrt\gamma\,Y_{zz}\Big[
\int_{-\infty}^{\infty} du\,u\,D_z^4C_{zz}(u,z)\Big|_{\mathcal I^+}
-\;\text{antipodal }\mathcal I^-\text{ partner}\Big]+\mathrm{c.c.}
\]
\[
=\;(\text{\(\kappa\)-normalization})\;\sum_k
Y_{zz}(z_k)\Big[-3E_k^{-1}\,\partial^2_{z_k}
+\big(\partial_{z_k}\partial_{E_k},\ \partial^2_{E_k},\ \partial_{z_k}
\text{ channels}\big)\Big]\langle\mathrm{out}|S|\mathrm{in}\rangle ,
\]

where the right-hand side is the smeared \(S^{(2)-}\) hard-leg insertion of
[CL16 (15)] with the "\(\dots\)" channels named exactly by check T3.6 of
the rung-3 boundary packet:
\(\partial_z\partial_E\) channel
\(-8\pi\bar z_k/(1+z_k\bar z_k)\,\delta-2\pi\,\partial\delta\);
\(\partial_E^2\) channel \(-6\pi E_k\bar z_k^2/(1+z_k\bar z_k)^2\delta
-3\pi E_k\bar z_k/(1+z_k\bar z_k)\partial\delta-(\pi E_k/2)\partial^2\delta\);
\(\partial_z\) channel \(2\pi\bar z_k/(E_k(1+z_k\bar z_k))\delta
+(2\pi/E_k)\partial\delta\). The single-outgoing-insertion plain-\(\delta\)
coefficient is half the conserved-charge coefficient.  This is now resolved:
[FPR after (119)] states that crossing makes the charge's soft component twice
one outgoing insertion, and checker M8.5 reproduces the printed [CL16 (15)]
coefficient exactly.

**Derivation chain, per-step grounding status:**

1. **Boundary soft theorem** [CL16 (14)]
   \((\sqrt\gamma/2\pi i)\lim_{\omega\to0}\omega^{-1}
   \langle\mathrm{out}|C_{zz}(\omega)S|\mathrm{in}\rangle|_{\rm fin}
   =S^{(2)-}\langle\mathrm{out}|S|\mathrm{in}\rangle\).
   GROUNDED (`cl1605.09094.txt` lines 188–198).
2. **Finite part of the \(\omega^{-1}\) moment ↔ first \(u\)-moment.**
   With \(C_{zz}(\omega)=\int du\,e^{i\omega u}C_{zz}(u)\), the coefficient
   of \(\omega^1\) in \(C_{zz}(\omega)\) is \(i\int du\,u\,C_{zz}(u)\);
   the projector ladder \((2+\omega\partial_\omega)(1+\omega\partial_\omega)\)
   kills \(a/\omega^2\) and \(b/\omega\) and extracts \(2\times\) the finite
   part of the \(\omega^{-1}\) moment. DERIVED + sympy-verified (§5 M2);
   projector half already dual-engine verified (boundary packet T4.4).
   [FPR] independently grounds the same projector structure on the Ward
   side: the spin-2 soft component is
   \(\lim_{\omega\to0}\partial_\omega(1+\omega\partial_\omega)\partial_z^4(\dots)\)
   (`fpr2111.15607.txt` lines 1414–1428).
3. **Double retarded integral = \(U\cdot(\)rung-2 charge\()-\) first moment.**
   DERIVED + sympy-verified (§5 M1, M4); matches [CL16 (30)] (lines
   431–436) and [CL16 (17)] (lines 223–252).
4. **Distributional fold** \(\frac1{2\pi}D_z^4S^{(2)-}=\) local hard
   operator [CL16 (15)]. GROUNDED (lines 205–212) AND dual-engine verified
   (T3.4a regular-part vanishing, T3.5 coefficients, T3.6 "\(\dots\)"
   channels, T3.7 electric/magnetic doubling; 31/31 both engines, ledger
   1096).
5. **News-moment ↔ shear-moment ladder.** \(N^{(n)}\) at grade
   \(\eth^{n+2}\) on the news equals \((-1)\times\) the \((n-1)\)-th shear
   moment up to endpoint terms; at \(n=2\), \(N^{(2)}=-M_1(C)\) exactly for
   vacuum endpoints. DERIVED + sympy-verified (§5 M3); moment definitions
   and curve-deviation relations GROUNDED [GN22 (3.11)–(3.14), lines
   953–1011].
6. **Ballistic charge/flux decomposition** [G24 (3.13),(3.17)]:
   \(\eth^4 N_2=-\Delta\tilde\psi_0+\frac12\int(\tilde u-u)^2\eth^2F_0
   +\int(\tilde u-u)\eth\hat F_1+\int[(\tilde u-u)(F^{\rm rad}_{2,1}
   +F^{\rm nonrad}_{2,1})+F_{2,0}]\). GROUNDED (grant2312.02295.txt lines
   633–716). This is the memory-side (boundary-jump + flux) form of the
   master identity's left side.
7. **Ward-side conservation.** [FPR (127)–(128)]: antipodal matching of
   the spin-2 corner aspect \(t(z)\) implies
   \(\langle\mathrm{out}|t|_{\mathcal I^+_-}S-St|_{\mathcal I^-_+}
   |\mathrm{in}\rangle=0\) with soft component \(=S^{(2)}\) insertion.
   GROUNDED (fpr2111.15607.txt lines 1410–1428). [CL16 (8),(9),(16)–(18)]
   ground the same content as the \((Q_{rX},\tilde Q_{rX})\) pair.
8. **Charge identification**
   \(\tilde\psi_0\) ([G24]) \(\leftrightarrow\) spin-2 aspect \(\hat t\)
   ([FPR]) \(\leftrightarrow\) \(Q^{(0)}_\xi\) ([CL16 (30)–(33)]).
   PARTIAL: at linear order the \(Lw_{1+\infty}\) charges are equivalent to
   the news moments (Compère–Oliveri–Seraj arXiv:2206.12597, cited in
   [G24] ref [28] — citation-level here); the nonlinear identification is
   OPEN — typed residual R2 below.
9. **Antipodal matching** for the \(O(r)\)/pseudo-vector-field generators.
   ASSUMED (inherited external input; strictly worse than rung 2 — the
   generators are singular at the corners; conventions packet §9 item 3).
10. **Magnetic half.** The \(\tilde Q_{rX}\) derivation is lacking in
    [CL16] (lines 115–120); the magnetic part of the second news moment
    exists in [GN22 §V]. PARTIAL — typed residual R3.

## 5. Symbolic verification (SymPy, exact)

The exploratory inline witnesses were promoted into the durable checker
`checkers/subsubleading_memory_exact_checks.py`.  Its 65 checks pass exactly
and are recorded in `results/subsubleading_memory_exact_checks.json`.  The
suite verifies the finite-part, moment, parity, pseudo-flux order, spin-weight,
and \(\eth^4\)-grade structure. The overall linear normalization is fixed;
the full nonlinear comparison map remains a typed open boundary:

- **M1 (finite-part identity).** Witness
  \(F(u)=(2+u)/(1+u^2)^2=O(u^{-3})\subset O(u^{-2-\epsilon})\) (the CL16
  falloff class), chosen asymmetric so \(M_1\neq0\):
  \(\int_{-\infty}^{U}du\int_{-\infty}^{u}du'F = U I_1(U)-M_1(U)\)
  identically TRUE; \(I_1(\infty)=\pi\), \(M_1(\infty)=\pi/2\).
- **M4 (non-persistence of the raw double integral / obstruction O1).**
  \(\lim_{U\to\infty}[\int\int F-U I_1(\infty)]=-M_1(\infty)=-\pi/2\):
  verified TRUE. The raw double integral drifts linearly with coefficient
  \(I_1(\infty)\) (the rung-2 content); the [CL16 (30)] subtraction leaves
  exactly minus the first moment.
- **M2 (Fourier ↔ moment).** Gaussian-class witness \(F(u)=ue^{-u^2}\):
  moment expansion of \(\hat F(\omega)\) matches the closed form
  \((i\omega\sqrt\pi/2)e^{-\omega^2/4}\) through \(\omega^5\); coefficient
  of \(\omega^1\) is \(i\mu_1\) with \(\mu_1=\sqrt\pi/2=\int uF\,du\):
  TRUE. Projector
  \((2+\omega\partial_\omega)(1+\omega\partial_\omega)
  (a\omega^{-2}+b\omega^{-1}+c_0+c_1\omega)\to2c_0\): TRUE.
- **M3 (news/shear ladder).** Vacuum-to-vacuum witness
  \(C(u)=u^3(1-u)^3\) on \([0,1]\):
  \(\frac12\int_0^1 u^2\dot C\,du=-\frac1{280}=-\int_0^1 uC\,du\): TRUE.

The rung-2 verified sphere identities (Green kernel
\(\partial_z\partial_{\bar z}G=2\pi\delta^2-\frac12\gamma_{z\bar z}\),
\(\sin^2(\Theta/2)\) family) and the rung-3 fold ladder (T3.4–T3.7, T4.1–
T4.4) are inherited from `checkers/subleading_triangle_exact_checks.py` and
`checkers/subsubleading_triangle_exact_checks.py` (31/31 both engines);
no new sphere-derivative identity was needed beyond them — the only new
content is the \(u\)-moment/finite-part sector M1–M4 above.

## 6. Expected physical readout (detector configuration)

The [FGHN] Riemann-integral ladder fixes the operational meaning:
relative velocity = \(\int R\) (2.3), displacement = \(\int\int R\) (2.1),
drift (spin+CM) = \(\int\int\int R\) (2.2), **ballistic = \(\int\int\int
\int R\)**. Concretely:

- **Free-mass readout.** The rung-2 drift memory is a residual relative
  displacement linear in the burst duration (the "\(\dot\xi\)-sourced"
  subleading displacement [FGHN (2.2)]). The rung-3 ballistic memory is the
  next term: a relative displacement sourced by the *first moment* of the
  shear — during the burst the separation acquires a quadratic-in-\(u\)
  piece, leaving a permanent offset \(\propto M_1(C)\) after the burst,
  visible in the curve-deviation observable \(\Delta\alpha^{(0)}_{ij}
  =\frac1{2r}[3N^{(2)}_{ij}-(u_1-u_0)N^{(1)}_{ij}]+O(1/r^2)\)
  [GN22 (3.14) at \(n=0\), lines 1001–1011].
- **Counter-orbiting beams (PSZ analog).** PSZ's per-orbit delay is
  \(\Delta_P=\oint(D_zC_{zz}dz+\mathrm{c.c.})\) [(4.3), lines 363–369] and
  the spin memory is \(\Delta_+u=\frac1{2\pi L}\int du\,\Delta_P\) [(4.5),
  lines 379–389]. The rung-3 observable is one more \(u\)-integral: the
  *accumulated residual displacement of the interference pattern*,
  \(\propto\int du\int^u du'\,\Delta_P(u')\) at grade up — operationally a
  permanent "delay drift": after the burst the counter-orbiting pulses
  carry not only the spin-memory delay but a delay that grew linearly
  through the burst, with slope set by the first shear moment. By M4 this
  requires the finite-part subtraction of the rung-2 piece, exactly as
  [CL16 (30)] prescribes.
- **Astrophysical magnitude.** [G24] finds the second-moment contributions
  \(\sim 10^{-2}\) of the displacement-memory contributions in an
  equal-mass BBH merger (lines 1144–1148); [SGN24] (abstract-level) gives
  the PN multipolar fluxes. Detection is a LISA-era prospect at best.

## 7. Checkable consequences (next verification phase)

- **C1 (port M1–M4).** Add the finite-part/moment identities as exact
  check items in both engines (sympy + Symbolica), with the witnesses
  above; the deliberate-failure control is the unsubtracted double
  integral (must exhibit the linear drift \(U I_1(\infty)\)).
- **C2 (augmented smeared master identity on test kinematics).** For an
  \(n\)-particle burst, [PSZ (5.10)] fixes the first moment
  \(\int du\,u\,T_{uz}=8\pi G\sum_k u_k[\dots]\), but it does **not** by
  itself fix the shear response.  The source-derived comparison must retain
  the angular-momentum aspect as a principal/corner cell.  Multiplying the
  exact curl constraint [PSZ (5.2)] by \(u\) and integrating gives
  \[
  \operatorname{Im}\!\left[\partial_{\bar z}D_z^3
     \int du\,u C_{zz}\right]
  =2\operatorname{Im}\!\left(
    [u\,\partial_{\bar z}N_z]_-^+
    -\int du\,\partial_{\bar z}N_z
    +\int du\,u\,\partial_{\bar z}T_{uz}
  \right).
  \]
  Thus the finite C2 test is the augmented aspect-plus-flux map, followed by
  the sphere smearing, into the [CL16 (15)] hard-leg channels.  A stress-only
  comparison is mistyped and cannot decide the T3.5c factor-\(\tfrac12\)
  residual.  This is the rung-3 analog of retaining the principal cell in a
  labelled total complex.

  The Ward-side source already contains the required cell.  In [FPR (29)]
  \(Q_1=P\) is the angular-momentum aspect, and the renormalized spin-two
  corner charge [FPR (36)] contains
  \[
  \hat t=\frac{8}{\kappa^2}\frac13
  \left(T-uDP+\left(\frac{u^2}{2}D^2
  -\frac32\int^u C\right)M_C\right).
  \]
  At linear order, the \(-uDP\) term is precisely the integration-by-parts
  coherence term required by the augmented PSZ identity above.  The remaining
  convention-dependent identification \(P\leftrightarrow N_z\) is fixed by
  comparing the actual
  \(r^{-1}g_{uA}\) coefficients in [PSZ (2.1)] and [FPR (2c)] gives
  \[
  P_A=N_A+\frac34C_{AB}D_CC^{CB}
      -\frac{3}{32}\partial_A(C_{BC}C^{BC}),
  \]
  so \(P_A=N_A\) at linear order. Exact checker M8.6 verifies the full
  displayed nonlinear metric dictionary. M8.7/M8.7a additionally verify the
  unsmeared angular square for a nontrivial \((u,z,\bar z)\) witness: the
  \(\partial_{\bar z}\) operator commutes with the weighted time integral,
  and the endpoint/principal aspect cell is exactly what completes the flux
  map before the Green-kernel projection.
- **C3 (parity doubling).** The magnetic partner from the
  \(\epsilon_B{}^CD_AX'_C\) split must reproduce the magnetic part of the
  second news moment [GN22 §V]; electric half must reproduce the
  CM-partner piece. Backed by T3.7 (exact \(\sigma\)-conjugation).
- **C4 (nonlinear degree separation; prior identification withdrawn).** The [G24] pseudo-fluxes
  \(F^{\rm rad}_{2,1}=-3i\frac{d}{du}(\sigma\,\mathrm{Im}[\eth^2\bar\sigma])\),
  \(F^{\rm nonrad}_{2,1}=-3\frac{d}{du}(m\sigma)\) [(3.14)–(3.16)] have no
  counterpart in the tree-level [CL16] Ward identity. They are quadratic,
  while [FPR after (87)] explicitly defines the collinear block \(t^C\) as
  cubic. Therefore they cannot be identified. They must instead be sought in
  the hard/renormalized-aspect block or retained as unmatched coefficient
  data. Only [G24] \(F_{2,0}=-3\sigma^2\dot{\bar\sigma}\), which is cubic,
  is degree-compatible with the FPR collinear sector. All vanish at linear
  order, so the linear triangle still closes. Checker M6.7 enforces this
  separation. Degree compatibility is not equality: checker M6.8 shows on a
  compact-support witness that the local cubic functional produces a local
  \(C^2\)-type variational action, whereas [FPR (132)] contains
  \(\partial_u(C\partial_u^{-1}C)\), including the nonlocal coherence term
  \(\dot C\partial_u^{-1}C\). The correct comparison must pass through the
  full corrected charge and radiative symplectic transgression.
- **C5 (charge identification at linear order).** Verify the
  \(\tilde\psi_0\leftrightarrow\hat t\) match mode-by-mode on
  spin-weighted harmonics (the \(\eth^4\) inversion is diagonal, [G24]
  note after (3.27)), using [GN22 (4.20)] and [FPR (36)/(42)].
- **C6 (normalization) — closed at linear order.** [FPR (103),(106)] and
  the vacuum-endpoint identity give
  \[
  t^S=-\frac{4}{3\kappa^2}D^4N^{(2)},\qquad
  N^{(2)}=-\int du\,uC,qquad
  \boxed{\mathcal M_3=\frac{3\kappa^2}{4}t^S}.
  \]
  Since [CL16 (30)] gives \(Q_{Y,\mathrm{FP}}^{\rm soft}=-\mathcal M_3\),
  equivalently \(t^S=-4Q_{Y,\mathrm{FP}}^{\rm soft}/(3\kappa^2)\).
  Composing with [FPR (129)] fixes the outgoing-insertion coefficient:
  \[
  \boxed{[\mathcal M_3,S]_{\rm soft}
  =-\frac{\kappa}{8\pi}\,\mathcal I^{(2)}_{\rm out}}.
  \]
  Checker M8.2/M8.2b/M8.2c certifies these identities. This does not close
  the nonlinear pseudo-flux/collinear comparison.

## 8. Obstructions and typed residuals (none absorbed)

- **O1 (non-persistence of the raw double integral) — named, with
  witness.** \(\int du\int^u du'F\) drifts linearly,
  \(I_2(U)=U I_1(\infty)-M_1(\infty)+o(1)\) (M4, witness: drift
  coefficient \(\pi\), finite part \(-\pi/2\)). A persistent rung-3
  observable exists only after the [CL16 (30)] finite-part subtraction of
  the rung-2-grade drift, or on the subspace \(I_1(\infty)=0\) (vanishing
  rung-2 drift memory). This is the structural reason the rung-3 observable
  is a *finite part*, not a raw integral — the exact analog of [G24]'s
  finding that \(\psi_0\) is not itself a charge and needs the correction
  (3.11).
- **Resolved R1 (T3.5c).** The computed single-outgoing-insertion
  plain-\(\delta\) coefficient is half the printed [CL16 (15)] charge value
  because the latter contains both crossed soft insertions.  [FPR after
  (119)] supplies the factor two; exact checker M8.5 closes it.
- **R2 (nonlinear closure).** The ballistic memory's quadratic pseudo-flux sector
  ([G24] \(F^{\rm rad/nonrad}_{2,1}\); [GN22] \(G^{(0,0)}_{\rm rad/nonrad}\)
  (4.18)–(4.19), which do not vanish when the news vanishes) lies outside
  the tree-level Ward identity and cannot be FPR's cubic collinear block.
  Its map into the hard/renormalized-aspect sector is open. Separately, the
  cubic \(F_{2,0}\) may compare with FPR collinear corrections and the [LS]
  non-universal loop piece; no equality is presently claimed.
- **R3 (magnetic half).** No first-principles derivation of
  \(\tilde Q_{rX}\) ([CL16] lines 115–120); the magnetic second moment
  exists memory-side [GN22 §V] but its Ward-side partner is incomplete.
- **R4 (corner matching).** Antipodal matching for the \(O(r)\) /
  pseudo-vector-field generators is assumed, not established (conventions
  packet §9; [FPR (127)] assumes the same).
- **R5 (tails vs. memory) — obstruction proved.** [S20]'s classical
  sub-subleading waveform lives in the \(u^{-2}\ln u\) tail sector. Such a
  shear contributes \(uC\sim(\ln u)/u\), hence
  \[
  \int_1^Udu\,uC\sim\frac12(\ln U)^2.
  \]
  M1.11/M1.11a verify the divergence exactly. The present ballistic-memory
  functional is therefore defined only on the strict CL16/FPR falloff class;
  extending it to physical logarithmic tails requires a separately derived
  log-squared finite-part prescription. More generally,
  \(C=(A\ln u+B)/u^2+O(u^{-3})\) requires subtraction of both
  \(\frac A2\ln^2U\) and \(B\ln U\). M1.12 verifies the two-grade finite
  part. Under \(\log u\mapsto\log(u/\mu)\), the coefficient must run as
  \(B_\mu=B+A\log\mu\); M1.12a verifies cancellation of all divergent
  grades, while M1.12b isolates the remaining finite ambiguity
  \(B\log\mu+\frac A2\log^2\mu\).
  Thus the tail extension is not canonical until a source-derived
  asymptotic scale/matching prescription is supplied. The primary-source
  audit of [S20] sharpens this obstruction: \(L\) is only constrained to be
  larger than the objects/scattering region so that the point-particle
  expansion applies, and the leading term is extracted from
  \(\omega\ll|\ell|\ll L^{-1}\). The ordered two-loop integral gives
  \(\frac12\omega\{\ln(\omega L)\}^2\) ([S20], discussion below its
  `step` equation), while the calculation explicitly drops
  \(O(\omega\ln\omega)\). Consequently \(L\mapsto e^sL\) preserves the
  universal \(\omega\ln^2\omega\) coefficient and shifts precisely the
  discarded lower-log and finite grades. The source therefore fixes the
  universal coefficient but does **not** canonically choose the finite-part
  scale needed by the extended ballistic-memory functional. M1.12c–d refine
  the surviving structure: changes of scale obey an exact one-cocycle
  composition law and act independently of the finite \(D/u^3\) control.
  Hence the admissible tail finite parts form an affine scale torsor; the
  obstruction is the absence of a preferred section, not incoherence of the
  renormalization rule. There is also an independent time-origin torsor:
  under \(u\mapsto u-a\), M1.13–M1.13a give
  \[
  \mathcal M_3\mapsto\mathcal M_3-a\mathcal M_2,
  \]
  with exact additive composition. Thus a scalar ballistic memory is not
  invariant data when the lower memory is nonzero. The natural object is the
  filtered pair \((\mathcal M_2,\mathcal M_3)\) with its triangular affine
  translation action, together with the logarithmic scale torsor—not a
  preferred number obtained by silently choosing either origin or scale.
  M1.14–M1.14c sharpen the tail typing itself. The three-coefficient family
  \[
  C(u)=\frac{A\log u+B}{u^2}+\frac{D}{u^3}+O(u^{-4})
  \]
  is not closed under retarded-time translations: translating \(u\) produces
  a new \(E\log u/u^3\) term. The minimal closed tail jet is therefore
  \((A,B,E,D)\), with
  \[
  (A,B,E,D)\mapsto
  (A,B,E-2aA,D+aA-2aB)
  \]
  under \(u\mapsto u+a\), while a scale change
  \(\log u\mapsto\log u+\ell\) acts by
  \[
  (A,B,E,D)\mapsto(A,B+A\ell,E,D+E\ell).
  \]
  The exact checker proves that both actions compose and commute. Thus the
  natural tail datum is a four-grade affine jet carrying compatible scale
  and time-origin actions; neither the scalar finite part nor the truncated
  \((A,B,D)\) presentation is functorial.

## 9. Files created this session

- `research/strominger/sources/fghn1901.00021.pdf`, `.txt` (28 pp)
- `research/strominger/sources/grant2312.02295.pdf`, `.txt` (14 pp)
- `research/strominger/sources/gn2109.03832.pdf`, `.txt` (22 pp)
- `research/strominger/subsubleading-memory-candidate.md` (this packet)
- `research/strominger/checkers/subsubleading_memory_exact_checks.py`
- `research/strominger/results/subsubleading_memory_exact_checks.json`

No other paths touched; no git operations; sympy verification run inline
(no checker files added, per session scope).
