# Arithmetic Exclusion of Finite Double Contact for the Shifted-Gaussian Weil Kernel: A Deep Literature-Sweep Report

*Deep literature sweep conducted 2026-09-03. Research swarm: 12 dimension investigations, cross-verification (22 confidence-tier findings, 14 conflict zones adjudicated), 11 cross-dimensional insights. Method, hostile tests, and evidence tiers in Chapter 2; ranked candidates in Chapter 3; rejected routes in Chapter 4; strongest attack and missing object in Chapter 5; executable acceptance test in Chapter 6; verdict in Chapter 7.*

# 1. Problem, Kernel, and Verified Foundations

## 1.1 The exclusion problem and the kernel

### 1.1.1 The exclusion target

[VERIFIED] Throughout this report, $t > 0$ is the inverse Gaussian-variance parameter, $\xi \in \mathbb{R}$ is the frequency variable, and

$$\Theta(t,\xi) = K_{\mathrm{end}}(t,\xi) + K_{\Gamma}(t,\xi) + K_{\mathrm{pr}}(t,\xi)$$

is the completed shifted-Gaussian Weil kernel in the Marici normalization; the BRS symmetrized kernel is exactly $4\Theta$ and therefore has identical signs, zeros, and critical points, so every exclusion statement proved for $\Theta$ transfers verbatim to the BRS convention.[^1^] With $\psi$ the digamma function and $\Lambda$ the von Mangoldt function, the three pieces are[^1^][^2^]

$$
\boxed{\;
\begin{aligned}
K_{\mathrm{end}}(t,\xi) &= e^{t/4 - t\xi^{2}}\cos(t\xi),\\[2pt]
K_{\Gamma}(t,\xi) &= -\frac{\log\pi}{4\sqrt{\pi t}} \;+\; \frac{1}{4\pi}\int_{\mathbb{R}} e^{-t(u-\xi)^{2}}\, \operatorname{Re}\psi\!\left(\tfrac14 + \tfrac{iu}{2}\right)\, du,\\[2pt]
K_{\mathrm{pr}}(t,\xi) &= -\frac{1}{2\sqrt{\pi t}}\sum_{n\ge 2} \frac{\Lambda(n)}{\sqrt{n}}\, e^{-(\log n)^{2}/(4t)}\cos(\xi\log n).
\end{aligned}\;}
$$

The exclusion problem is to prove — or to prove impossible by a stated class of methods — that no finite point $(t^{*},\xi^{*})$ with $t^{*} > 0$ satisfies

$$\Theta(t^{*},\xi^{*}) \;=\; \partial_{\xi}\Theta(t^{*},\xi^{*}) \;=\; 0. \tag{DC}$$

Since $\Theta$ is real-analytic in both variables (Gaussian factors give locally uniform convergence of all differentiated series and integrals[^3^]), a solution of (DC) is a *finite double contact*: a tangency of the profile $\xi \mapsto \Theta(t,\xi)$ to the zero line. Notation fixed here for the entire report: $A(t,\xi) := K_{\Gamma}(t,\xi) + K_{\mathrm{pr}}(t,\xi)$, $B(t,\xi) := \partial_{\xi}\bigl(K_{\Gamma}(t,\xi) + K_{\mathrm{pr}}(t,\xi)\bigr)$, and the forward-parabolic time $\tau := 1/(4t)$.

### 1.1.2 Established inputs of the sweep

[VERIFIED] The mission brief fixes six facts that this report consumes as inputs rather than rediscovering[^1^]; each was independently re-examined inside the sweep at the locations cited. (i) $\Theta(t,\xi) > 0$ for all $\xi$ when $t$ is sufficiently small, with constants not yet effective.[^1^][^2^] (ii) Character coercivity excludes contacts as $|\xi| \to \infty$ near every finite positive $t$-threshold.[^1^][^4^] (iii) A first finite loss of positivity as $t$ grows must be attained at a finite $(t_{*},\xi_{*})$ and must satisfy (DC): positivity loss of an analytic, coercive profile enters through a tangency.[^1^][^4^] (iv) The strong maximum principle, the parabolic zero-number theorem, and Gaussian total positivity do not exclude such contacts, because their useful implication runs toward *broader* Gaussian variance — the opposite direction from increasing $t$ (§1.2.1); formally, zero-number theory counts sign changes and a tangency of a sign-definite profile creates none (Angenent's Theorem A is vacuous here), and total-positivity machinery is in any case unavailable: the de Bruijn–Newman kernel is interval-certified not to be Pólya-frequency of order $5$.[^5^][^6^] (v) Prime almost-periodicity: $K_{\mathrm{pr}}(t,\cdot)$ is Bohr almost-periodic in $\xi$ with spectrum $\{\pm\log n\}$, and almost-periodic recurrence prevents any uniform pointwise improvement over the absolute prime mass; the zero-existence theory of such sums is obstruction-flavored, not exclusion-flavored.[^7^][^3^] (vi) de Bruijn–Newman real-rootedness and Jensen-polynomial hyperbolicity do not presently map to pointwise positivity of $\Theta$: the provable Turán/Jensen fragments are moment-level statements with no $(t,\xi)$ content, and the full hierarchy is equivalent to the Riemann Hypothesis (RH).[^8^][^9^]

### 1.1.3 Evenness: the axis $\xi = 0$ is an automatic double-contact locus

[VERIFIED] Each kernel piece is even in $\xi$: the cosine terms are even, and $K_{\Gamma}$ convolves an even Gaussian against $u \mapsto \operatorname{Re}\psi(\tfrac14 + \tfrac{iu}{2})$, which is even because $\psi(\bar{z}) = \overline{\psi(z)}$. Hence[^10^][^3^]

$$\partial_{\xi}\Theta(t,0) \equiv 0 \qquad (t > 0),$$

so the axis $\xi = 0$ is an automatic double-contact locus: *any* zero of $t \mapsto \Theta(t,0)$ solves (DC) with no further condition. This elementary observation, flagged as sweep-original (no literature source was found for it), reduces a bona fide sub-case of the exclusion problem to a one-variable inequality and is the seed of the pilot sub-route developed in Chapters 3 and 5.[^10^]

### 1.1.4 Bochner diagnosis: a difference of two positive-definite functions

[DERIVED] For each fixed $t > 0$, the negated prime contribution $-K_{\mathrm{pr}}(t,\cdot)$ is a cosine series in $\xi$ with non-negative coefficients on the frequencies $\{\pm\log n\}$ — equivalently the Fourier transform of the positive discrete measure $\sum_{n\ge2} \Lambda(n)n^{-1/2}e^{-(\log n)^{2}/(4t)}(\delta_{\log n} + \delta_{-\log n})$ — and is therefore continuous and positive-definite in $\xi$ by the Bochner–Herglotz theorem on the Bohr compactification.[^11^][^2^] The Fourier transforms in $\xi$ of $K_{\mathrm{end}}(t,\cdot)$ and of the non-constant part of $K_{\Gamma}(t,\cdot)$ are likewise non-negative (two shifted Gaussians, respectively the Weil archimedean density), so

$$\Theta(t,\cdot) \;=\; [\text{positive-definite in } \xi] \;-\; [\text{positive-definite in } \xi] \;-\; \frac{\log\pi}{4\sqrt{\pi t}},$$

a difference of two positive-definite functions minus a constant.[^2^] This is exactly the generic signed-cosine setting in which double contacts are admitted — consistent with established fact (iv) and with the explicit almost-periodic counterexamples recorded in the sweep.[^4^] Positive-definiteness supplies only $|f(\xi)| \le f(0)$-type control at the origin and never pointwise positivity away from it; the spectral-side positive-definiteness available under RH (via E2 below) is circular as an input to the exclusion problem (hostile test 7, Chapter 2).

## 1.2 Three verified structural identities

### 1.2.1 E1 (SF1): the parabolic equation and the time orientation

[VERIFIED] Each of $K_{\mathrm{end}}$, $K_{\Gamma}$, $K_{\mathrm{pr}}$ satisfies the following equation term-by-term, hence so does $\Theta$, on $t > 0$, $\xi \in \mathbb{R}$ — verified analytically and numerically in-session (relative error $\le 1.4\times10^{-6}$ at several sample points):[^4^]

$$\partial_{t}\Theta \;=\; -\frac{1}{4t^{2}}\,\partial_{\xi\xi}\Theta \;-\; \frac{1}{2t}\,\Theta,
\qquad\text{equivalently, with } \tau = \tfrac{1}{4t}:\quad
\partial_{\tau}\Theta \;=\; \partial_{\xi\xi}\Theta + \frac{1}{2\tau}\,\Theta.$$

The $\tau$-form is forward-parabolic with damping. Since the feared first contact is approached by *increasing* $t$ from the small-$t$ positivity regime, the dangerous direction is the ill-posed, roughening direction of the natural parabolic time — opposite to de Bruijn–Newman time, where $H_{t}$ solves the backward heat equation $\partial_{t}H_{t} = -\partial_{xx}H_{t}$ and increasing $t$ is smoothing.[^12^][^13^] This single orientation reversal explains why zero-repulsion, zero-number, and total-positivity mechanisms, which all act in the smoothing direction, cannot exclude contacts of $\Theta$; the resulting rejections are catalogued in Chapter 4.

### 1.2.2 E2 (SF2): the Gaussian explicit formula

[VERIFIED] The sweep's central computational identity is the zero-side representation

$$\Theta(t,\xi) \;=\; \tfrac12 \sum_{\rho}\Bigl[\, e^{-t(\xi-\gamma_{\rho})^{2}} + e^{-t(\xi+\gamma_{\rho})^{2}} \Bigr],$$

the sum over nontrivial zeros $\rho = \tfrac12 + i\gamma_{\rho}$; it was verified in-session with mpmath at $50$ digits against the geometric side with $N = 80{,}000$ prime powers, agreeing to at least $9$ significant digits at points on and between zero heights for $t \in \{0.25,\dots,2\}$.[^4^][^17^] Equivalently, $\Theta(t,\xi) = c(t)\, W(\varphi_{t,\xi})$ for the Gaussian test function $\varphi_{t,\xi}(x) = e^{-x^{2}/(4t)}\cos(\xi x)$, where $W$ is the Weil distribution of the explicit formula.[^2^][^15^] The trivial direction is immediate: under RH every $\gamma_{\rho}$ is real, every summand is a positive Gaussian, $\Theta(t,\xi) > 0$ pointwise, and no double contact exists. Conversely, an off-line zero pair at distance $\beta$ from the critical line injects oscillation of amplitude $\sim e^{t\beta^{2}}$, and by fact (iii) the first negativity as $t$ grows must enter through a tangency — so exclusion across all $t > 0$ is morally RH-equivalent, and every viable deliverable must be range-restricted, conditional on hypotheses strictly weaker than RH, or an obstruction (developed in Chapters 3–7).[^14^][^17^]

### 1.2.3 E3: the contact identity (corrected), with a quarantine

[VERIFIED] With $A, B$ as in §1.1.1, the two contact equations at $(t,\xi^{*})$ read[^3^]

$$\cos(t\xi^{*}) = -e^{-t/4 + t\xi^{*2}}\, A(t,\xi^{*}),
\qquad
\sin(t\xi^{*}) = e^{-t/4 + t\xi^{*2}}\Bigl(2\xi^{*} A(t,\xi^{*}) + \frac{B(t,\xi^{*})}{t}\Bigr),$$

where the second equation substitutes the first into the symbolically verified derivative $\partial_{\xi}K_{\mathrm{end}} = e^{t/4 - t\xi^{2}}\bigl[-2t\xi\cos(t\xi) - t\sin(t\xi)\bigr]$.[^3^] Eliminating the endpoint oscillation via $\cos^{2} + \sin^{2} = 1$ gives the contact identity

$$A(t,\xi^{*})^{2} + \Bigl(2\xi^{*}A(t,\xi^{*}) + \frac{B(t,\xi^{*})}{t}\Bigr)^{2} \;=\; e^{\,t/2 \,-\, 2t\xi^{*2}}. \tag{E3}$$

A double contact is therefore exactly the statement that the bounded almost-periodic pair $(A,B)$ hits a prescribed moving target on the circle of radius $e^{t/4 - t\xi^{*2}}$; since the radius *shrinks* super-exponentially in $|\xi^{*}|$, (E3) re-derives and sharpens the coercivity input (ii), confining possible contacts to $|\xi^{*}| = O(t^{-1/2}\sqrt{\log})$ with a computable threshold.[^14^] Consistency check at $\xi^{*} = 0$: evenness gives $B(t,0) \equiv 0$ (§1.1.3), so (E3) reduces to $A(t,0)^{2} = e^{t/2}$, and the contact equation $\Theta(t,0) = e^{t/4} + A(t,0) = 0$ selects the negative branch $A(t,0) = -e^{t/4}$ — internally consistent. [CONFLICT: resolved] Quarantine: the identity as printed in dimension file dim11, and inherited by the mission statement, reads $A^{2} + (2\xi A - B/t)^{2} = e^{-t/2 + 2t\xi^{2}}$; both the exponent and the relative sign of the $B/t$ term are mis-signed there (at $\xi = 0$ the printed form forces $|A| = e^{-t/4}$, contradicting its own pre-elimination equations, which are themselves symbolically verified). The printed form is quarantined as a corrected error; (E3) above is the only sanctioned version for all downstream quantitative work.[^3^][^14^]

## 1.3 Scope and evidence status

### 1.3.1 The kernel $\Theta$ is sui generis in the public record

[VERIFIED] Four dedicated literature searches — "Marici" against Weil kernel/Riemann/normalization, "BRS symmetrized" against the Riemann $\xi$ kernel, shifted-Gaussian Weil-kernel positivity, and $\Theta(t,\xi)$ itself — returned zero relevant external hits; the only "BRS" matches are BRST gauge-symmetry physics, and "Marici" does not co-occur with Weil or Riemann in any indexed source.[^16^] The kernel and its nomenclature are internal to this sweep. Two consequences follow. First, completeness: the sweep cannot fail by overlooking a published $\Theta$-result, and the deliverables of Chapters 3–7 constitute the public state of the art for this object. Second, evidence discipline: no external refereeing exists for $\Theta$-specific claims, so every such claim in this report is either elementary, symbolically verified, or high-precision numerically verified in-session, and is tagged accordingly.

### 1.3.2 Claim-tag legend and audit-flag policy

[VERIFIED] Every factual claim in this report carries exactly one tag at first statement. **[VERIFIED]**: the statement is drawn from a refereed source with full bibliographic data, or is a session computation independently verified (symbolic differentiation, or numerical evaluation with explicit precision and error control). **[DERIVED]**: a cross-dimensional inference obtained by combining verified facts that no single source states jointly. **[CONFLICT: status]**: an item from a conflict zone — divergent attributions, conventions, or sign discrepancies across sources — reported with its resolution, as in the quarantine of §1.2.3. **[AUDIT: verdict]**: an additional flag on any claim depending on an unrefereed preprint; the audit verdict (e.g. "sound post-retraction", "theorem-level only, numerics not interval-certified") is recorded at the point of use, and under the sweep's tier rule no High-confidence claim may rest on preprint-derived numbers.[^17^] Named theorems are additionally flagged for RH-dependence and carry one of five classifications — applicable, conditionally applicable, inapplicable, circular, obstruction — assigned under the source requirements and seven hostile tests formalized in Chapter 2.[^1^][^17^]

## 2. Method: Source Requirements, Hostile Tests, Evidence Tiers

This chapter fixes the evaluation machinery applied in Chapters 3–7. Nothing in it is a candidate theorem; it is the protocol by which candidates were admitted, attacked, and graded. The sweep that produced the evidence base ran as a twelve-dimension research swarm (one research agent per thematic dimension of §1), followed by a dedicated cross-verification phase and an insight-extraction phase [VERIFIED].[^31^] Each dimension executed between 12 and 36 distinct literature searches, read primary sources in full text where obtainable, and — for the 2024–2026 unrefereed preprint layer — audited claims against source text, appendices, and machine certificates rather than abstracts.[^32^] Cross-verification then re-read all twelve dimension files, adjudicated every quantitative claim appearing in two or more dimensions, and resolved fourteen logged conflict zones (CZ-1–CZ-14); insight extraction recorded only cross-dimensional inferences, i.e., statements no single dimension file contains.[^31^][^34^] The three governing instruments of that process — the per-candidate source checklist, the hostile tests, and the tier/audit policy — are specified below exactly as they were enforced.

### 2.1 Source-requirements checklist

No item entered the candidate pool of Chapter 3 on the strength of a title or abstract. Admission required all nine fields of Checklist Box C2.1, transcribed from the mission brief [VERIFIED]:[^33^]

> **Checklist Box C2.1 — nine mandatory fields per candidate source**
> - **SR1** Complete citation with DOI or arXiv identifier and a stable URL.
> - **SR2** Exact theorem, proposition, or lemma number.
> - **SR3** Faithful hypotheses and conclusion (verbatim where feasible).
> - **SR4** Parameter and Fourier conventions of the source.
> - **SR5** Explicit map to $(t,\xi,\Theta,\partial_\xi\Theta)$ in the Chapter-1 normalization.
> - **SR6** Required arithmetic inputs.
> - **SR7** Unmet hypotheses, listed by name.
> - **SR8** RH-assumption flag: does any hypothesis assume RH, critical-line zero location, a positive Weil form, or an equivalent statement?
> - **SR9** Classification: applicable / conditionally applicable / inapplicable / circular / obstruction.

Two fields do more work than their brevity suggests. SR5 forces every candidate through the corrected contact identity of Chapter 1, $A(t,\xi)^2 + (2\xi A(t,\xi) + B(t,\xi)/t)^2 = e^{t/2-2t\xi^2}$ with $A := K_\Gamma + K_{pr}$ and $B := \partial_\xi(K_\Gamma + K_{pr})$, so that a theorem about a different object (a windowed form, a heat-flow function $H_t$, a coefficient sequence) is recorded as such rather than silently re-targeted. SR8 is the anti-circularity gate: its four probe hypotheses are precisely the disguises under which RH re-entered candidate arguments during the sweep (§2.3.2). Failure of SR1–SR2 excluded an item outright; failures of SR7–SR8 were recorded, not suppressed.

### 2.2 The seven hostile tests

Every proposed route, including the sweep's own leads, was subjected to the seven adversarial questions of Table T2.1 [VERIFIED].[^33^] A route failing any test was rejected or reclassified, with the failure attributed by test number in Chapter 4.

**Table T2.1. The seven hostile tests as operational questions.**

| # | Operational question | Canonical failure mode observed in the sweep |
|---|---|---|
| 1 | Does the argument exclude the explicit difference-of-two-Gaussians profile, which exhibits a genuine double contact? If not, name the additional arithmetic hypothesis invoked. | Generic signed Gaussian convolutions and almost-periodic models admit double zeros (e.g., $(1-\cos x)+(1-\cos\sqrt2\,x)$); arithmetic-frequency independence alone cannot break a contact.[^34^] |
| 2 | Does the mechanism run in the correct Gaussian-variance direction? | Zero-repulsion and zero-number mechanisms act in the smoothing direction of the de Bruijn–Newman flow, opposite to the $\Theta$-time orientation $\tau = 1/(4t)$: they generate, not exclude, contacts.[^34^][^35^] |
| 3 | Does it remain valid with the signed prime contribution $K_{pr}$ retained? | Envelope or absolute-value treatments of the prime comb discard the cancellation on which any exclusion must rest.[^31^] |
| 4 | Does it control every real $\xi$, not only $\xi = 0$? | Moment-level inequalities (Turán family) see only the on-axis slice $\xi = 0$.[^36^] |
| 5 | Is the estimate uniform on a compact positive $t$-interval? | Window-by-window certificates are uniform on their window but provably do not globalize (§2.3.3, Zhu audit).[^37^] |
| 6 | Does it prove a global statement rather than report finite numerical sampling? | Sampling-as-proof and uncertified infinite tails (Gershon audit, §2.3.3); spurious float64 negative eigenvalues mimicking counterexamples.[^38^][^37^] |
| 7 | Does it avoid inserting RH through real spectral nodes, a Schur condition, de Branges positivity, or a positive zero-side measure? | de Branges positivity is refuted; every global Weil-positivity statement in the swept literature is RH-equivalent.[^39^][^31^] |

The tests are not independent, and the pattern of joint failure is itself diagnostic. Tests 1–3 enforce *content*: the argument must distinguish $\Theta$ from a generic signed Gaussian profile (test 1), must not rely on a mechanism that acts in the wrong variance direction (test 2), and must survive retention of the signed von Mangoldt coefficients (test 3). Tests 4–6 enforce *quantifier discipline*: control at all real $\xi$ (test 4), uniformity on compact positive $t$-intervals (test 5), and a global statement rather than a finite sample (test 6). Test 7 enforces *logical hygiene* against RH smuggled in through spectral hypotheses. In the sweep, RH-circularity (test 7) was the dominant failure mode, with sampling-as-proof (test 6) second and moment-level blindness to $\xi \neq 0$ (test 4) third; no candidate failed test 5 alone without also failing test 6. This observed ordering motivates the tier policy of §2.3, which treats numerical evidence as corroboration only, never as proof, and it dictates the failure-attribution scheme of Chapter 4, where each rejected route is indexed by the numbers of the tests it fails.[^31^]

### 2.3 Evidence tiers and preprint audit policy

Three confidence tiers were used. **High**: refereed source, or a session-verified elementary computation reproduced independently. **Medium**: statement-level content of an unrefereed item, or a single-agent finding with refereed support. **Low**: leads only. The binding rule [VERIFIED]: *no High-tier claim may rest on an unrefereed item*.[^31^] Compliance was checked explicitly at cross-verification: every High-tier finding either rests on refereed literature or is independently underwritten (e.g., the qualitative margin-collapse verdict rests on Fuchs's 1964 prolate asymptotics, not on preprint constants).[^31^][^40^]

#### 2.3.2 Bibliographic conflict resolutions

The following [CONFLICT] items were resolved against primary text or publisher records and are binding for all citations in this report [VERIFIED]. (i) Authorship of arXiv:2608.24827 is **Xuefeng Zhu** (v2 title page); the "M. Chuk" attribution survives only in index metadata.[^37^] (ii) Yoshida 1992 runs **pp. 281–325**, confirmed by three independent reference lists; "281–306" is a transcription error.[^41^] (iii) Suzuki 2023, J. London Math. Soc.: DOI **10.1112/jlms.12785**.[^42^] (iv) Csordas–Smith–Varga 1994: DOI **10.1007/BF01205170**.[^43^] (v) The mission brief's Burnol titles ("Sur les formes explicites de l'analyse harmonique"; a J. Funct. Anal. "explicit estimate and sum of squares") **do not exist**; a 41-item enumeration of Burnol's corpus shows the real targets are the CRAS 331 (2000) note and the RH-conditional Acta Cient. Venezolana 54 (2003) paper.[^44^][^45^] (vi) Bombieri's variational paper is Comm. Pure Appl. Math. **56 (2003), 1151–1164** (not 2001).[^46^]

#### 2.3.3 Preprint audit verdicts

Each unrefereed item carries an [AUDIT] verdict from full-text hostile review; verdicts, not abstracts, govern admissibility.[^32^]

**Table T2.2. Audit verdicts for the unrefereed layer.**

| Item | [AUDIT: verdict] | Admissible use |
|---|---|---|
| Zhu, arXiv:2608.24827v2 | Sound post-retraction (v1 support-2.38 claim self-retracted, envelope direction error correctly diagnosed); honest, narrow.[^37^] | Machinery + proved barrier; constants Medium only. |
| Suzuki, arXiv:2606.09096v2 | Honest framework paper; "without assuming RH" explicit; Cor. 1.6 labeled conjectural.[^47^] | Structure theory with preprint caveat; Cor. 1.6 excluded as a tool. |
| Groskin, arXiv:2607.02828 | Theorem-level content (exact dictionary, budget $B_T$) usable; numerics **not** interval-certified.[^48^] | Cite the certification rule; **never** its numerical certificates. |
| Michałowski, arXiv:2602.20313v2 | Sound certified obstruction post-correction (v1 global claims withdrawn; $\neg$PF$_5$ certificate unaffected).[^49^] | Obstruction to total-positivity routes. |
| Gomila, $\Lambda \le 0.1787854$ | Logically sound, best-in-class sealed Arb apparatus; single-auditor, unreplayed, unrefereed.[^50^] | Cite the architecture (Polymath15-instantiation pattern), **not** the bound.[^35^] |
| Gershon, Preprints 202604.1513 | Circular by its own Remark 19 (tail limit assumes zeros on the line); sampling-as-proof.[^38^] | Excluded; Part I known since 1986.[^36^] |
| Kim et al., arXiv:2607.24830 | Low credibility (AI-lab, float numerics, no enclosure arithmetic).[^51^] | Excluded from evidence. |

The verdict pattern is systematic [DERIVED]: every *obstruction or certificate* item audited clean (Zhu, Michałowski, Gomila in logical form), while every *positivity or RH claim* failed audit (Gershon circular, Kim non-credible) — the audit-convergence insight I9.[^34^] The asymmetry is not accidental: an obstruction or finite counterexample needs one certified witness and is falsifiable by replay, whereas a positivity claim quantifies over infinitely many windows or infinitely many primes and therefore concentrates its risk exactly where sampling and hidden RH enter (tests 6 and 7). Two operational rules follow. First, this report weights proved obstructions and certified computations above positivity theorems throughout the ranking of Chapter 3. Second, no preprint-derived number supports any High-confidence statement in later chapters; where a preprint constant is quoted (e.g., Zhu's certified margins), it is labeled Medium and accompanied by the refereed independent underwriting of §2.3.1.[^31^][^40^]

## 3. Candidate Theorem Clusters: Ranked Table and Interface Maps

### 3.1 Ranking principles

#### 3.1.1 Obstructions and certified machinery outrank positivity claims; all global positivity theorems are RH-equivalent and therefore circular

The ranking is governed by a single asymmetry established in Chapters 1–2: the sweep target is *strictly stronger* than Weil positivity (positivity evaluated pointwise on a two-parameter Gaussian family that is not a compactly supported self-convolution), while every theorem asserting a global positivity of a Weil-type functional is provably equivalent to the Riemann Hypothesis (RH), hence circular for the exclusion problem. The equivalence is anchored from both sides of the explicit formula. On the form side, Weil's criterion (RH ⟺ $W(\psi\ast\tilde\psi)\geq 0$ for all $\psi\in C_c^\infty(\mathbb{R})$) [^82^], the Li and Bombieri–Lagarias criteria ($\lambda_n\geq 0$ for all $n$ ⟺ RH) [^83^][^84^], Yoshida's non-degeneracy theorem [^70^], and Suzuki's pointwise criterion (RH ⟺ $\Psi(t)\geq 0$ for all $t$) [^68^] are all biconditionals [VERIFIED]. On the zero side, E2 makes RH ⟹ $\Theta(t,\xi)>0$ pointwise trivial, while an off-line zero pair at real shift $\beta$ injects oscillation of amplitude $\sim e^{t\beta^{2}}$, so the first loss of positivity as $t$ grows must enter through a tangency [VERIFIED] [^65^]. Consequently a cluster is ranked by what it contributes *given* this wall: (i) proved obstructions and certified machinery surviving hostile test 7; (ii) conditional or range-restricted tools whose hypotheses are strictly weaker than RH and independently testable; (iii) difficulty benchmarks. Unrefereed items are audit-flagged and, per the tier rule of §2.3, may not support a High-confidence claim [^67^].

### 3.2 Table T3.1: ranked candidate clusters

Table T3.1 ranks the eight surviving clusters. Hostile tests are those of §2.2: (1) excludes a difference-of-two-Gaussians profile; (2) correct variance direction ($t$ widens); (3) signed prime contribution retained; (4) all real $\xi$; (5) uniform on compact $t$-intervals; (6) global, not sampling; (7) no hidden RH. Entries: ✓ pass, ✗ fail, ◐ partial, — not meaningful.

**Table T3.1. Ranked candidate theorem clusters for excluding finite double contact of $\Theta$.**

| Rank | Citation + audit flag | Exact theorem number(s) | Hypotheses summary | RH-dependence + mechanism | Classification | Tests 1–7 | Missing-for-application |
|---|---|---|---|---|---|---|---|
| 1 | Polymath15 (2019) [VERIFIED] [^61^] | Thm 1.2; Prop. 3.1(i)–(ii); Prop. 3.3; Thm 3.2 (= de Bruijn Thm 13 [^88^]) | (i) RH verified to height $X/2$ (finite); (ii) asymptotic zero-free region at final time $t_0$; (iii) barrier strip zero-free for all $t\in[0,t_0]$ ⟹ $\Lambda\leq t_0+y_0^2/2$ | None: hypothesis (i) is finite verified RH; mechanism = minimal-time first contact + Rouché on prism boundary | Conditionally applicable transplant | 1 ✓ 2 ◐ 3 ✓ 4 ✓ 5 ✓ 6 ✓ 7 ✓ | Certified enclosure of $(\Theta,\partial_\xi\Theta,\partial^2_{\xi\xi}\Theta)$ with explicit uniform prime-tail bound; tangency (multiplicity) channel absent from Thm 1.2 [^91^] |
| 2 | Sweep-original, no literature source [DERIVED] [^64^][^65^] | None (to be proved/certified); rests on Bernstein–Widder | $P(s)=\sum_{n\geq2}\Lambda(n)/\sqrt{n}\,e^{-s(\log n)^2}$, $s=1/(4t)$; $\Lambda\geq 0$ ⟹ $P$ completely monotone; $K_{\mathrm{end}}(t,0)=e^{1/(16s)}$ and $K_\Gamma(t,0)$ provably not CM | None on compacts; globally RH-equivalent via E2 at $\xi=0$; mechanism = CM/log-convexity propagation in $s$ | Conditionally applicable lead | 1 ✗ 2 ✓ 3 ✓ 4 ✗ 5 ✓ 6 ✓ 7 ✓ | The signed synthesis: CM negative part controlled by two non-CM positive parts; certified one-variable bounds on $[t_1,t_2]$ |
| 3 | Zhu, arXiv:2608.24827v2 [AUDIT: sound post-retraction, unreproduced, metadata anomaly] [^66^][^67^] | Thm 1.1 (one-stroke reduction); Thm 1.2 (certified margin); Lemma 3.2 + Thm 1.4 (barrier); Thm 6.2, Cor. 6.3 | Even real $f$, $\operatorname{supp}f\subseteq[-L,L]$; Weil symbol $\Psi_L$; comb envelope $A_L=\sup_t P_L(t)$ | Lower/upper bounds unconditional; only the decay-law arm (Thm 1.3) assumes RH and is excluded; mechanism = envelope + equidistribution-optimal comb + finite Gram PSD certificate | Conditionally applicable machinery + obstruction | 1 ◐ 2 ✓ 3 ◐ 4 ✓ 5 ✗ 6 ✓ 7 ✓ | Form-continuity under Gaussian truncation; multi-window certificates (none exist); independent reproduction |
| 4 | Suzuki 2023 [VERIFIED] [^68^]; Suzuki 2026v2 [AUDIT: honest framework; Cor. 1.6 conjectural, excluded as tool] [^69^] | 2023: Thms 4.1–4.3 (unconditional), Thms 1.2–1.8 (RH-equivalent); 2026: Thms 1.1–1.5 | Screw function $g=-\Psi$; localized form on $L^2(-a,a)$; Friedrichs operator $A_a$ | Thms 4.1–4.3 and 1.1–1.5 unconditional; Yoshida-type corollary ($\exists a:\lambda_a<0$ ⟺ ¬RH) circular globally; mechanism = continuity of $\lambda_a$ (Thm 1.3) + small-$a$ expansion $\lambda_a=\log(1/a)+\mu_1-\log(2\pi)+\psi(2)-1+O(a)$ (Thm 1.4) | Applicable per small window; circular globally | 1 ◐ 2 ✓ 3 ✓ 4 ✗ 5 ◐ 6 ✓ 7 ✓ | Any bridge from window margin to the Gaussian slice; margins collapse (Landau–Widom) before the dangerous $t$-range |
| 5 | Groskin, arXiv:2607.02828 [AUDIT: theorem-level Medium; numerics not interval-certified — do not cite its numerics] [^73^][^67^] | Thm 2.5 (exact dictionary); Thm 3.2 (tail order); Cor. 3.3 (two-sided rule) | CvS/CCM Galerkin truncation at prime cutoff $c$, band $N$; archimedean cutoff $T$ | Unconditional; mechanism: finite-cutoff value = exact zero sum; tail is a totally positive Cauchy–Stieltjes increment with budget $B_T\sim(2N+1)\rho\log T/(\pi^2T)$, $\rho=2\pi/\log c$ | Conditionally applicable technology + obstruction | 1 ✓ 2 ✓ 3 ✓ 4 ✓ 5 ✗ 6 ✓ 7 ✓ | Per-cutoff only; indecision band $[-B_T,0)$ swallows near-contacts; Gaussian truncation unaddressed |
| 6 | Connes–van Suijlekom, CMP 406 (2025) [VERIFIED] [^74^]; CCM, arXiv:2511.22755 Thm 5.10 [AUDIT] [^75^] | CvS Thm 6.1 (= Thm 1.2); CCM Thm 5.10 (with Thm 3.6, Cor. 3.7–3.8) | Real even distribution on $[-L,L]$; lower-bounded self-adjoint $A$; spectral minimum a *simple, isolated* eigenvalue with *even* eigenfunction $\xi$ | Theorem unconditional but the simple-even ground-state hypothesis is assumed, not proved (certified only at $L=0.8$ by Zhu Thm 6.2 [^66^]); mechanism = Carathéodory–Fejér Toeplitz + Hurwitz limit | Conditionally applicable; circular if globalized (spectral convergence = RH) | 1 ◐ 2 — 3 ✓ 4 ✓ 5 ✗ 6 ✓ 7 ◐ | Certified simplicity/evenness at windows that matter; direction is ground state ⟹ real zeros of $\hat\xi$, not positivity of $\Theta$ |
| 7 | Csordas–Varga 1988 [^76^]; Csordas, Open Problem 4.7 (2015) [^77^]; Csordas–Escassut 2005 [^78^] [VERIFIED] | CV88 moment inequalities; OP 4.7 ($L_1(x)\geq 0$ for $H$, open); C–E equality case: $L_1[f](x_0)=0$ exactly at multiple zeros | Laguerre–Pólya class hypotheses (RH-circular for $\Xi$, structurally false for $\Theta$'s signed summands) | Unconditional statements but zero-side/moment-level; mechanism = differential-inequality equality case | Obstruction / difficulty benchmark | 1 ✗ 2 ◐ 3 ✗ 4 ✗ 5 — 6 ✓ 7 ✓ | n/a (calibration items): even the one-variable zero-side analog is open, known only for $|x|<1.09\times10^{9}$ |
| 8 | Conrey 1989 [^80^]; Pratt–Robles–Zaharescu–Zeindler 2020 [^81^] [VERIFIED] | Conrey: $\geq 2/5$ of zeros simple on the line; PRZZ: $\liminf N_0(T)/N(T)\geq 0.417293$, simple proportion $\geq 0.407511$ | Levinson's method + mollifiers; unconditional | None; mechanism = zero-side non-degeneracy statistics | Inapplicable (no bridge to $\Theta$) | 1 — 2 — 3 ✗ 4 ✗ 5 — 6 ✓ 7 ✓ | A simplicity-to-contact-exclusion bridge; under E2 simplicity does not constrain the Gaussian sum's sign |

**Interpretation of Table T3.1.** The ranking inverts a naive bibliometric ordering: the two highest entries are a *method* (Rank 1) and an *unproved structural observation* (Rank 2), not the strongest proved positivity theorems, because every proved global positivity statement fails hostile test 7. Three regularities stand out. First, test 5 (uniformity on compact $t$-intervals) separates the table cleanly: only Ranks 1 and 2 pass, being the only clusters whose native object is a compact parameter interval rather than a single window or cutoff — precisely what an acceptance criterion of type (c) requires. Second, test 4 (all real $\xi$) is failed by every form-side cluster (Ranks 4–6): window margins are operator-level statements carrying no pointwise frequency information, which is why the form-side map of §3.3.6 is a one-way street. Third, the "missing-for-application" column is remarkably redundant — Ranks 1, 3, 5, and 6 all gate on the same two objects (a certified enclosure of $(\Theta,\partial_\xi\Theta)$ with a uniform prime-tail bound; a form-continuity estimate under Gaussian truncation), recorded by the cross-verification as independently requested by three dimensions [^91^]. The outliers are Ranks 7 and 8, retained as calibration, not tools: Rank 7 shows the strongest pointwise $f$-vs-$f'$ inequality has the double zero as its equality case; Rank 8 shows the only unconditional arithmetic non-degeneracy theory lives on the wrong side of the explicit formula.

#### 3.2.1 Rank 1: Polymath15 barrier/first-contact architecture — conditionally applicable transplant

Theorem 1.2 of Polymath15 [^61^] — hypotheses and conclusion as tabulated — is proved by a minimal-time first-contact argument, with a zero located on the barrier boundary by Rouché's theorem (Prop. 3.3); Prop. 3.1(ii) resolves a repeated zero of order $m$ into Hermite $\sqrt{2(t-t_0)}$-branches [VERIFIED] [^61^]. Its certification technology (interval arithmetic, effective Riemann–Siegel approximation with explicit error bounds, winding-number checks uniform in $t$ via prism slicing) is the only peer-reviewed, fully certified machinery controlling a complete signed prime+gamma+endpoint functional uniformly on a compact time interval; it yields $\Lambda\leq 0.22$ unconditionally ($\Lambda\leq 0.20$ with the Platt–Trudgian height $3{,}000{,}175{,}332{,}800$ [^62^]; the replayable-certificate instantiation of Gomila is logically sound but single-auditor and concerns $H_t$, not $\Theta$ [AUDIT] [^63^][^67^]). What Theorem 1.2 does *not* see is multiplicity: strip zero-freeness implies absence of real zeros, not of double real zeros. The transplant therefore replaces "winding number of $H_t$ in prisms" by "sign certificates of $(\Theta,\partial_\xi\Theta,\partial^2_{\xi\xi}\Theta)$ in boxes" (§3.3.3) and gates on the missing enclosure object [^91^].

#### 3.2.2 Rank 2: [DERIVED] on-axis complete-monotonicity theorem (sweep-original)

Every piece of $\Theta$ is even in $\xi$, so $\partial_\xi\Theta(t,0)\equiv 0$ and every zero of $t\mapsto\Theta(t,0)$ is automatically a finite double contact [VERIFIED] [^65^]. On this slice the hostile signed prime term acquires theorem-grade rigidity: with $s=1/(4t)$,

$$
P(s)=\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt{n}}\,e^{-s(\log n)^{2}}
$$

is completely monotone in $s>0$ — by the Bernstein–Widder theorem it is the Laplace transform of a positive measure with arithmetic weights $\Lambda(n)/\sqrt{n}$ — so log-convexity and all CM determinantal inequalities apply [DERIVED] [^64^]. The other two on-axis pieces are provably not CM in $s$: $K_{\mathrm{end}}(t,0)=e^{1/(16s)}$ fails the alternating-derivative test, and $K_\Gamma(t,0)$ is a Gaussian-in-$s$ transform of the sign-changing $\operatorname{Re}\psi(1/4+iu/2)$ [VERIFIED] [^64^]. The axis theorem is therefore necessarily a *signed* inequality — a CM negative part controlled by two non-CM positive parts — on compact $t$-intervals; globally it cannot close, because E2 at $\xi=0$ makes all-$t$ on-axis positivity RH-equivalent [^65^]. No literature source was found; the observation is sweep-original and is the cheapest genuinely non-circular pilot (feeds Ch5).

#### 3.2.3 Rank 3: Zhu one-stroke finite reduction, certified margin, and barrier theorem

Zhu's preprint [AUDIT: sound post-retraction, unreproduced, metadata anomaly — authorship resolved to Xuefeng Zhu, Dalian University of Technology, against index metadata reading "M. Chuk"] [^66^][^67^] proves: Theorem 1.1, reduction of window positivity to positive semidefiniteness of a single finite matrix via a pointwise envelope whose comb constant $A_L=\sum_{\log n<2L}2\Lambda(n)/\sqrt{n}$ is optimal (Lemma 3.2, Weyl equidistribution of the $\mathbb{Q}$-independent $\{\log p\}$); Theorem 1.2, the interval-certified margin $\lambda^*(0.8)\in[8.9\times10^{-18},\,2.27\times10^{-17}]$; Theorem 6.2, certified simple even ground state at $L=0.8$; and Theorem 1.4, the barrier — any one-stroke certificate must resolve frequencies up to $T_1=2\pi e^{A_L}$, $A_L=(4+o(1))e^{L}$, doubly exponential and unimprovable within the envelope class [^66^]. The v1 support-2.38 claim was retracted in v2 for bounding the comb in the wrong direction; the certified content survives [^67^]. The cluster is simultaneously the sharpest existing certified machinery and a proved obstruction: the certified window covers only $t\lesssim0.05$–$0.1$ (§3.3.4), and the barrier caps the entire envelope route [^66^].

#### 3.2.4 Rank 4: Suzuki 2023 Thms 4.1–4.3 and Suzuki 2026 Thms 1.1–1.5

The refereed 2023 paper (JLMS 108, 1448–1487, DOI 10.1112/jlms.12785) [^68^] proves unconditionally: Theorem 4.1, $\Psi(t)>0$ on $(0,\log 2]$ (the prime-free range, with computed critical values); Theorem 4.2, positive definiteness of the screw-kernel form $G_g$ on $L^2(-a,a)$ for $0<a<a_0$; Theorem 4.3, a Yoshida-Lemma-3-type uniform margin on finite-codimension subspaces [VERIFIED] [^68^]. Its Theorems 1.2–1.8 (RH ⟺ $g$ a screw function; ⟺ form positivity/non-degeneracy for every $a$; ⟺ $\Psi\geq 0$ pointwise) are RH-equivalences, excluded as tools [^68^]. The 2026 preprint [AUDIT: honest framework; no RH claim; Cor. 1.6 conjectural and excluded] [^69^][^67^] supplies the operator completion: Theorem 1.1, $A_a$ is the Friedrichs extension of $B_a=D^*G_aD$; Theorem 1.3, $\lambda_a$ continuous in $a$ (repairing Bombieri's incomplete proof [^71^][^72^]); Theorem 1.4, the small-$a$ expansion tabulated above, with $\lambda_a$ positive, simple, with even eigenfunction; Theorem 1.5, all zeros of the characteristic function $W(a,\theta;z)$ real unconditionally [^69^]. The cluster quantifies *why* small windows are safe (the $\log(1/a)$ divergence is driven by the $|t|\log|t|$ singularity of $g$, not by primes) and identifies first positivity loss with ground-state degeneracy — the form-level double contact — but produces no pointwise $\Theta$ statement (test 4 fails).

#### 3.2.5 Rank 5: Groskin's exact dictionary and two-sided certification rule

Groskin's preprint [AUDIT: theorem-level Medium; its numerical PSD certificates are not interval-certified and are not cited] [^73^][^67^] proves for the CvS/CCM truncation at prime cutoff $c$ and band $N$: Theorem 2.5, every Galerkin vector $v$ determines in closed form a band-limited Guinand–Weil test function $g_v$ with $\langle v,Q_\infty v\rangle=\sum^*_{\zeta(1/2+iz)=0}g_v(z)$ *exactly*; Theorem 3.2, the omitted archimedean tail is a positive-definite, strictly totally positive Cauchy–Stieltjes increment; Corollary 3.3, the two-sided certification rule tabulated above, with indecision band $[-B_T,0)$ [^73^]. The exact dictionary makes these matrices an ideal negative control (run on a Davenport–Heilbronn analog the pipeline must fail — Bombieri–Hejhal shows such signed Euler-product combinations genuinely fail RH [^93^]); the indecision band quantifies the structural fact that near-contacts are invisible to every finite-rank certificate.

#### 3.2.6 Rank 6: Connes–van Suijlekom Thm 6.1 / CCM Thm 5.10 — conditional real-zeros theorems

Connes–van Suijlekom Theorem 6.1 (CMP 406 (2025), Art. 312; hypotheses and conclusion as tabulated) is proved via a Carathéodory–Fejér Toeplitz corollary, explicit finite truncations, and a Hurwitz limit [VERIFIED] [^74^]. CCM Theorem 5.10 is the finite-rank avatar of the same mechanism [AUDIT: unrefereed; the authors list spectral convergence as a "missing step" whose proof "would establish the Riemann Hypothesis"] [^75^][^67^]. For the sweep the direction is wrong (ground state ⟹ real zeros, not kernel positivity ⟹ no tangency), and the hypothesis is the obstruction: a ground-state degeneracy is exactly the form-level double contact, so the theorem cannot exclude what it assumes away; the simple-even hypothesis is certified at exactly one window, $L=0.8$, by Zhu's Theorem 6.2 [^66^].

#### 3.2.7 Rank 7: difficulty benchmarks — Csordas–Varga 1988, Csordas Open Problem 4.7, Csordas–Escassut

Three refereed items calibrate the problem's difficulty rather than serve as tools. Csordas–Varga 1988 (Constr. Approx. 4, 175–198, DOI 10.1007/BF02075457) proves unconditional Turán-type moment inequalities — moment-level, with no $(t,\xi)$ content [VERIFIED] [^76^] (Csordas–Norfolk–Varga 1986 is the coefficient-level analog [^79^]). Csordas's Open Problem 4.7 (CMFT 15 (2015), 373–391, arXiv:1309.0055) records that even the one-variable zero-side analog — the Laguerre inequality $L_1(x)\geq 0$ for the entire function $H$ — is open, verified only for $|x|<1.09\times10^{9}$ [VERIFIED] [^77^]. Csordas–Escassut (Ann. Math. Blaise Pascal 12 (2005), 331–345) prove that equality $L_1[f](x_0)=0$ for Laguerre–Pólya $f$ occurs *precisely* at multiple zeros: the strongest pointwise $f$-vs-$f'$ inequality in the literature has the double zero as its equality case, so the differential-inequality route detects but never excludes the contact [VERIFIED] [^78^].

#### 3.2.8 Rank 8: Conrey 1989 / Pratt–Robles–Zaharescu–Zeindler 2020 — unconditional zero-simplicity proportions

Conrey (Crelle 399 (1989), 1–26, DOI 10.1515/crll.1989.399.1) proved unconditionally that at least $2/5$ of the nontrivial zeros are simple and on the critical line [VERIFIED] [^80^]; Pratt–Robles–Zaharescu–Zeindler (Res. Math. Sci. 7 (2020), Paper 2) improved the proportions tabulated above [VERIFIED; article number as listed in the source sweep file] [^81^]. This is the only unconditional arithmetic non-degeneracy theory in sight, and it is inapplicable: the statements concern zeros of $\Xi$, and under E2 simplicity does not constrain the sign of the Gaussian sum $\Theta$ — under RH, $\Theta>0$ regardless of simplicity; without RH, the off-line pairs that could drive a contact are exactly what proportion theorems do not control [^65^]. No bridge from zero-simplicity to contact exclusion is known.

### 3.3 Exact theorem-to-kernel interface maps

The six maps below fix, once and for all, the coordinate correspondences between the swept theorems and the kernel $\Theta=K_{\mathrm{end}}+K_\Gamma+K_{\mathrm{pr}}$ (Marici normalization; identities E1–E3 of Chapter 1). Each map states what is *literally identical*, what changes under the correspondence, and what does not transfer.

#### 3.3.1 Time map: $\tau=1/(4t)$ and the orientation flip

By E1, $\partial_t\Theta=-(1/(4t^2))\partial_{\xi\xi}\Theta-(1/(2t))\Theta$, which under $\tau:=1/(4t)$ becomes the forward-parabolic equation $\partial_\tau\Theta=\partial_{\xi\xi}\Theta+(1/(2\tau))\Theta$ [VERIFIED] [^65^]: the smoothing direction for $\Theta$ is *decreasing* $t$, while the feared loss of positivity as $t$ grows is the ill-posed/roughening direction. The de Bruijn–Newman family $H_t$ obeys the backward heat equation $\partial_tH_t=-\partial_{xx}H_t$ with smoothing in *increasing* $t$ [^88^][^61^]; hence Polymath15's $t$ is reversed $\Theta$-time, and its $z=x+iy$ is $\xi$ complexified [VERIFIED] [^61^][^65^]. Two consequences are load-bearing for Chapters 4–5: zero-repulsion/no-collision lemmas (Csordas–Smith–Varga Lemma 2.4; Polymath15 Prop. 3.1(i)) hold in the smoothing direction and therefore *generate*, rather than forbid, contacts along the dangerous $\Theta$-time direction [^85^][^61^]; and CSV's Lemma 2.2/Corollary 2 confine multiple zeros of $H_t$ to $t\leq\Lambda$ with simplicity only strictly above $\Lambda$ — the attained threshold is where degeneracy lives [^85^].

#### 3.3.2 Frequency map: $\xi$ as the argument of the Weil symbol $\Psi_L$

The frequency variable $\xi$ of $\Theta$ is exactly the integration variable of the windowed Weil symbol

$$
\Psi_L(u)=\operatorname{Re}\psi\!\left(\tfrac14+\tfrac{iu}{2}\right)-\log\pi-\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt{n}}\cos(u\log n),
$$

since $Q(f)=2F(i/2)^2+\frac{1}{2\pi}\int|F(u)|^2\Psi_L(u)\,du$ for $\operatorname{supp}f\subseteq[-L,L]$ [VERIFIED, statement; AUDIT: preprint venue] [^66^]. In words: $\Psi_L$ is literally the Fourier multiplier behind $K_\Gamma+K_{\mathrm{pr}}$ — the digamma term furnishes $K_\Gamma$, the signed cosine comb furnishes $K_{\mathrm{pr}}$, and Gaussian weighting $F(u)\propto e^{-t(u-\xi)^2}$ with $L\to\infty$ recovers $K_\Gamma(t,\xi)+K_{\mathrm{pr}}(t,\xi)$ term by term [^66^][^65^]. Because the autocorrelation $f*\tilde f$ is centered at $0$ independently of $\xi$, any window theorem uniform over test functions is automatically uniform in $\xi$ — hostile test 4 is free on the window side [^65^]. The price: the signed comb is exactly what envelope arguments discard, and since its pointwise supremum equals $A_L$ exactly (Zhu Lemma 3.2), no envelope inequality can undercut the barrier $T_1=2\pi e^{A_L}$ [^66^].

#### 3.3.3 Zero-side map: double contact as a real landing point

By E2, $\Theta(t,\xi)=\tfrac12\sum_\rho\big[e^{-t(\xi-\gamma_\rho)^2}+e^{-t(\xi+\gamma_\rho)^2}\big]$, verified in-session at 50 digits with $N=80{,}000$ prime powers [VERIFIED] [^65^]. For fixed $t$, $\Theta(t,\cdot)$ is entire in $\xi$; a double contact $(t^*,\xi^*)$ is exactly a real landing point of a complex-conjugate zero pair of this entire function — the positivity-side twin of the de Bruijn–Newman threshold event, where coalescence at $t=\Lambda$ is a double zero and CSV Remark 3 + Polymath15 Prop. 3.1(ii) give the $\sqrt{t-t_0}$ fold resolution [^85^][^61^]. The barrier-transplant interface is then a literal substitution: replace "winding number of $H_t$ in time-sliced prisms" by "sign certificates of $(\Theta,\partial_\xi\Theta,\partial^2_{\xi\xi}\Theta)$ in $(t,\xi)$-boxes" — certify $\Theta>0$ where the enclosure is bounded away from zero, and $\partial^2_{\xi\xi}\Theta>0$ wherever $\Theta$ and $\partial_\xi\Theta$ are simultaneously small (fold normal form; analyticity forces finite even contact order [^65^]). The de Bruijn Theorem-13 $\sqrt{\cdot}$-law is the available a-priori input on approach rates of zeros to the real axis [^88^][^61^].

#### 3.3.4 Window-side map: window half-width $L$ versus Gaussian width $\sqrt{2t}$

A window theorem for the localized form on $[-L,L]$ (additive coordinate $u=\log x$) corresponds to time-domain test functions of width $\sim\sqrt{2t}$: the Gaussian $e^{-u^2/(4t)}$ truncated at $|u|=L$ has relative tail $\approx\operatorname{erfc}(L/\sqrt{2t})$ [VERIFIED, elementary computation] [^65^]. The prime-free window is $L\leq(\log 2)/2\approx0.3466$ (autocorrelation support $\log 2$; no prime power has $\log n<2L$) [^70^][^68^][^89^], translating to $t\lesssim0.03$–$0.1$ depending on the admitted tail budget — exactly the regime the sweep already covers as established small-$t$ positivity. Beyond it, the window margins collapse at the Landau–Widom rate: certified two-sided $\lambda^*(0.8)\in[8.9\times10^{-18},2.27\times10^{-17}]$ and certified upper bound $\lambda^*(2)\leq3.2\times10^{-283}$, following $-\ln\lambda^*(L)\approx2\pi^2N(T^*)/\ln N(T^*)$, $T^*=2\pi e^{2L}$ [AUDIT: constants from a single unrefereed preprint, Medium confidence] [^66^][^67^]; the qualitative super-exponential plunge is independently underwritten by Fuchs's 1964 prolate-spheroidal eigenvalue asymptotics (JMAA 9, 317–330) and Connes–Consani's 2023 numerical spectrum [VERIFIED, qualitative arm] [^90^][^94^]. The best explicit classical margin, Bombieri's Theorem 12 (margin $\sim\log(1/|I|)-\log\log(1/|I|)-O(1)$ for $|I|<\log 2$), has the same prime-free ceiling [^71^].

#### 3.3.5 Axis-slice map: $\xi=0$ and the contact condition $A(t,0)=-e^{t/4}$

On the axis, the corrected contact identity E3 —

$$
A(t,\xi)^{2}+\big(2\xi A(t,\xi)+B(t,\xi)/t\big)^{2}=e^{t/2-2t\xi^{2}},\qquad A:=K_\Gamma+K_{\mathrm{pr}},\ B:=\partial_\xi(K_\Gamma+K_{\mathrm{pr}})
$$

[VERIFIED; the mis-signed form $e^{-t/2+2t\xi^{2}}$ is quarantined as a corrected error] [^65^] — collapses at $\xi=0$, since $B(t,0)\equiv0$ by evenness, to $A(t,0)^2=e^{t/2}$: the on-axis contact condition is the negative branch $A(t,0)=-e^{t/4}$, equivalently $\Theta(t,0)=e^{t/4}+A(t,0)=0$ [^65^]. Under $s=1/(4t)$ the axis condition reads: the CM prime profile $P(s)$ of §3.2.2 must exactly balance the non-CM endpoint and gamma contributions — a one-variable signed inequality on compact $s$-intervals, certifiable by interval arithmetic with CM propagation (log-convexity of $P$ transports pointwise certificates across the interval) [DERIVED] [^64^]. The same identity yields the dangerous-region geometry: since $A$ and $B$ are bounded while the target radius $e^{t/4-t\xi^2}$ shrinks super-exponentially in $|\xi|$, contacts are confined to $|\xi^*|=O(t^{-1/2}\sqrt{\log})$ [DERIVED] [^65^].

#### 3.3.6 Form-side map: $\Theta(t,\xi)=c(t)\cdot W(\phi_{t,\xi})$, a codimension-$\infty$ slice

Identically, $\Theta(t,\xi)=c(t)\,W(\phi_{t,\xi})$ with $\phi_{t,\xi}(x)=e^{-x^2/(4t)}\cos(\xi x)$ and $\hat\phi_{t,\xi}(u)\propto e^{-t(u-\xi)^2}+e^{-t(u+\xi)^2}$: the Weil distribution evaluated on the two-parameter Gaussian family, the pole, archimedean, and prime terms furnishing $K_{\mathrm{end}},K_\Gamma,K_{\mathrm{pr}}$ [VERIFIED] [^82^][^65^]. Two structural consequences delimit every form-side tool. First, $\phi_{t,\xi}$ has non-compact support and, for $\xi\neq0$, is not a self-convolution (self-convolutions are even): the family lies outside the hypothesis class of Weil's criterion and of every Yoshida/Bombieri/Suzuki window theorem, and truncating it to $[-L,L]$ incurs the uncontrolled form-continuity error of §3.3.4 [^82^][^71^]. Second, the Gaussian family is a codimension-$\infty$ Rayleigh-quotient slice of test-function space: window inertia counts — Bombieri's Theorem 8, one negative eigenvalue per off-line zero pair [^71^][^72^] — see the whole window and are structurally blind to an event on a single curve unless that curve is degeneracy-detecting; whether a double contact of $\Theta(t^*,\cdot)$ forces a near-zero eigenvalue with a Gaussian-localized eigenvector at support $\sim c\,t^*$ is an open typed question, a potential no-go theorem either way [^91^]. This invisibility, together with Groskin's indecision band (§3.2.5), is the precise reason finite form-side certificates cannot resolve near-contacts.

# 4. Rejected Circular and Directionally Invalid Routes

This chapter is the sweep's negative-results catalogue (deliverable (3)): every rejected route, the hostile test(s) it fails, and a proof-level reason. It also carries the sweep's type-(e) content — rigorous obstructions eliminating route classes outright, as opposed to mere absences of applicable theorems.

## 4.1 Organizing principle

### 4.1.1 Four failure modes

Writing $A(t,\xi) := K_\Gamma(t,\xi) + K_{\mathrm{pr}}(t,\xi)$ and $B(t,\xi) := \partial_\xi(K_\Gamma + K_{\mathrm{pr}})(t,\xi)$, elimination of the endpoint oscillation from $\Theta = \partial_\xi\Theta = 0$ yields the contact identity

$$A(t,\xi)^2 + \Bigl(2\xi\,A(t,\xi) + \frac{B(t,\xi)}{t}\Bigr)^2 = e^{\,t/2 \,-\, 2t\xi^2},$$

[VERIFIED] (term-by-term symbolic differentiation, checked in-session; the mis-signed variant $A^2 + (2\xi A - B/t)^2 = e^{-t/2+2t\xi^2}$ from earlier working notes is quarantined here as a corrected error and used nowhere in this report). A double contact is thus the event that the orbit $\xi \mapsto \bigl(A,\, 2\xi A + B/t\bigr)$ of one Bohr almost-periodic function hits a prescribed point on a circle of radius $e^{t/4 - t\xi^2}$ [DERIVED]. Every rejected route fails for exactly one of four structural reasons, pinned to the hostile tests T1–T7 of Chapter 2:

- **RH-circularity (T7):** the criterion is equivalent to, or presupposes, the Riemann hypothesis (RH).
- **Wrong variance direction (T2):** the mechanism operates in the smoothing direction; since $\Theta$ obeys a backward-heat equation in $t$ [VERIFIED], the feared threshold is approached in the roughening direction.
- **Structural blindness to tangencies (T1/T3):** the tool counts sign changes; a touch-without-crossing of a sign-definite profile creates none.
- **Averaged or sampling quantifiers (T4/T6):** $L^2$-means, $\exists$-sampled statements, and finite-grid checks are all blind to a pointwise codimension-2 event.

Five obstructions below carry the sweep's type-(e) acceptance result, assembled in Chapter 7: the doubly-exponential envelope barrier (§4.3.6), the Landau–Widom window-margin collapse (§4.3.6), the Levin–Cartwright/Beurling–Malliavin density wall (§4.3.7), the quantitative void of linear-forms-in-logarithms bounds (§4.3.5), and the unanimity of threshold-degeneracy theory across three literatures (§4.3.1–§4.3.2).

## 4.2 Circular routes (RH-equivalent or RH-assuming)

**Table T4.1.** Circular routes; all fail T7.

| Route | Failing test(s) | One-line proof-level reason | Refs. |
|---|---|---|---|
| Weil 1952 positivity criterion | T7 (+T1) | $W(\psi\ast\tilde\psi)\ge 0$ on compactly supported $\psi$ ⟺ RH; the shifted Gaussian is non-compactly supported and, for $\xi\neq0$, not a self-convolution | [^116^] |
| Yoshida localization; Bombieri 2000 | T7 | Weil-form positivity on $C_c^\infty(-a,a)$ for every $a$ ⟺ RH; unconditional positivity only in the prime-free window $a \le \log 2$ | [^117^][^118^] |
| Li 1997 / Bombieri–Lagarias 1999 $\lambda_n$ criteria | T7 | $\lambda_n \ge 0$ for all $n$ ⟺ RH; partial verification yields only classical zero-free regions | [^119^][^120^] |
| Lagarias 1999 Pick criterion | T7 | $i(\xi'/\xi)(1/2-iz)$ in the Nevanlinna class ⟺ RH | [^121^] |
| Nakamura–Suzuki 2023 infinite divisibility | T7 | $\exp(g_\zeta)$ an infinitely divisible characteristic function ⟺ RH | [^122^] |
| Suzuki screw-function equivalences (2023, Thms 1.2–1.4, 1.7) incl. the Mercer/RKHS bridge | T7 | pointwise $\Psi(t)\ge 0$ ⟺ RH; Mercer turns operator positivity into diagonal positivity $G_g(t,t) = 2\Psi(t)$ — one RH-equivalent into another; the diagonal test function is the triangular $\Delta_t = R_t \ast \tilde R_t$, not the Gaussian | [^123^] |
| Suzuki 2026 Thms 1.3–1.4 (continuity, small-window positivity of $\lambda_a$) | T7 as route | "$\lambda_a > 0$ for all $a$" ⟺ RH (Yoshida-type nondegeneracy corollary); unconditional content confined to small windows | [^124^] |
| Suzuki Hilbert space $H_W$; Cor. 1.6-type limit formula | T7 | the space cannot even be defined without RH; the conjectural limit formula would prove RH | [^125^] |
| Balazard–Saias–Yor integral | T7 (+T6) | $(1/2\pi)\int_{\Re s = 1/2}\log|\zeta(s)|\,|ds|/|s|^2 = \sum_{\Re\rho>1/2}\log|\rho/(1-\rho)|$, so vanishing ⟺ RH; a scalar whole-line integral, not a finite certificate | [^126^] |
| Nyman–Beurling / Báez-Duarte density criteria | T7 (+T6) | density of dilates of fractional-part functions in $L^2(0,1)$ ⟺ RH; joint positivity of all finite Gram determinants is again RH, primes entering only in the limit | [^127^] |
| Alcantara-Bode injectivity criterion | T7 (+T6) | injectivity of a Hilbert–Schmidt operator ⟺ RH; injectivity is not stable under finite-rank truncation | [^128^] |
| Lagarias Hilbert–Pólya canonical systems | T7 | conditional by construction: "provided the Riemann hypothesis holds" the zero ordinates are simple real eigenvalues of a canonical system | [^129^] |
| Connes–Consani–Moscovici spectral-triple convergence (§8) | T7 | the authors state that proving the spectral convergence "would establish the Riemann Hypothesis" | [^130^] |
| de Branges Hilbert-space route | T7 + refuted | the Hermite–Biehler property of $E(z) = \xi(1-iz)$ already needs RH, and the required auxiliary positivity fails: $-\mathrm{Re}\{\xi'(\rho)\xi(1+\rho)\} = -5.39\times10^{-69} < 0$ at the 34th zero | [^131^][^132^] |
| Zero-side use of the Gaussian explicit formula (SF2) | T7 | under RH, $\Theta(t,\xi) = \tfrac12\sum_\rho [e^{-t(\xi-\gamma_\rho)^2} + e^{-t(\xi+\gamma_\rho)^2}] > 0$ trivially [VERIFIED in-session]; as a proof route, circular | — |
| Gershon preprint ($\Lambda = 0$ claim) | T6 + T7 [AUDIT: circular, flawed] | its own Remark 19 admits the $r\to\infty$ tail step "already assumes zeros on the critical line"; the $S \le 19.41$ bound is 12 computed terms plus an extrapolated tail | [^133^] |

**Interpretation of Table T4.1.** Every entry fails the same test, and the failure is structural, not quantitative: each criterion encodes RH as an equivalence, so each has genuine logical content — the screw-function line even delivers theorem-grade pointwise statements — but the content is exactly the hypothesis one may not use. Two finer points matter. First, the Mercer/RKHS bridge is the only theorem-grade mechanism converting quadratic-form positivity into pointwise positivity; its RH-equivalent diagonal output shows the difficulty lies not in the conversion step but in unconditional operator positivity for a kernel whose geometric-side symbol is a signed difference. Second, the Gaussian test function is excluded from Weil's criterion for two independent reasons (non-compact support; not a self-convolution for $\xi \neq 0$), so even a hypothetical RH-free proof of Weil positivity would not settle the pointwise question: positivity on the two-parameter Gaussian family is strictly stronger than every RH-equivalent in the table [DERIVED].

#### 4.2.1 Weil, Li, Pick, and infinite-divisibility criteria

Weil's 1952 criterion makes RH equivalent to non-negative definiteness of the Weil distribution on compactly supported self-convolutions (compact-support formulation: Yoshida) [VERIFIED][^116^][^117^]; Bombieri's inertia theorem adds that a large truncation has exactly half as many negative eigenvalues as there are off-line zero pairs [VERIFIED][^118^]. Li's criterion[^119^] with Bombieri–Lagarias's multiset generalization[^120^] is a scalar one-parameter shadow: no theorem converts $\lambda_n \ge 0$ into a pointwise statement at $(t,\xi)$. Lagarias's Pick criterion[^121^] and the Nakamura–Suzuki infinite-divisibility equivalence[^122^] are the half-plane and probabilistic avatars of the same wall. Classification: **circular**, all four.

#### 4.2.2 The Suzuki screw-function system

Suzuki's $\Psi(t) = \sum_\gamma (1-\cos\gamma t)/\gamma^2$ is $\Theta$'s closest relative in the refereed literature: same three-piece geometric side, triangular weight $(t-\log n)_+$ in place of the Gaussian $e^{-(\log n)^2/4t}$ [VERIFIED][^123^]. Theorems 1.2–1.4, 1.6–1.8 are RH-equivalences; only Theorem 1.5 (trace class) is unconditional [VERIFIED][^123^]. The Mercer step is the unique theorem-grade "quadratic form ⇒ pointwise" bridge found, and it converts one RH-equivalent into another [^123^]. The 2026 continuation proves $\lambda_a$ continuous and positive for small $a$, but "$\lambda_a > 0$ for all $a$" is Yoshida's RH-equivalence [^124^]; the Hilbert-space realization needs RH even to be defined, and its conjectural limit formula would prove RH [^125^]. Classification: **circular**; the Mercer step is the highest-value bridge for any future non-circular variant.

#### 4.2.3 Integral, density, injectivity, and spectral-realization criteria

The Balazard–Saias–Yor identity is a Hardy-space Jensen formula over the whole critical line — vanishing ⟺ RH, with no finite or local content [^126^]. The Nyman–Beurling lineage, strengthened by Báez-Duarte to a sequence criterion, and Alcantara-Bode's compact-operator injectivity are equivalent to RH and, decisively for certification, not stable under finite-rank approximation: no finite matrix certificate exists at any stage [^127^][^128^]. Lagarias's canonical-system construction (arXiv:0712.3238) yields the desired Hilbert–Pólya object only under RH [^129^]; the Connes–Consani–Moscovici spectral-triple program (arXiv:2511.22755, §8) labels its own convergence step as one that "would establish the Riemann Hypothesis" [^130^]. Classification: **circular**; the middle two are additionally not finitely reducible (T6).

#### 4.2.4 The de Branges route and its refutation; zero-side circularity; the Gershon audit

The de Branges program fails twice. The Hermite–Biehler property required of $E(z) = \xi(1-iz)$ — no zeros in the upper half-plane — is itself RH [^131^]. And the auxiliary positivity condition is false: Conrey–Li computed at the 34th zero $\rho = 1/2 + i\cdot 111.0295355431696745\ldots$ that $-\mathrm{Re}\{\xi'(\rho)\,\xi(1+\rho)\} = -5.389100507182945\ldots\times 10^{-69} < 0$, refuting it for $\xi$ and for $L(s,\chi_{-4})$ [VERIFIED][^132^]. Independently, the session-verified identity SF2 shows that under RH, $\Theta > 0$ is trivial — any exclusion routed through the zero side is circular by construction. The Gershon preprint claiming $\Lambda = 0$ is circular by its own Remark 19 (the $r\to\infty$ step assumes zeros on the critical line) and fails T6 (twelve computed terms plus an extrapolated tail) [AUDIT: flawed/circular, unrefereed; supports no High-confidence claim][^133^].

## 4.3 Directionally invalid or structurally blind routes

**Table T4.2.** Routes that point the wrong way, are blind to tangencies, or carry the wrong quantifier.

| Route | Failing test(s) | One-line proof-level reason | Refs. |
|---|---|---|---|
| Sturm–Matano–Angenent zero-number theory | T1/T3 (+T2) | Angenent Thm A: a multiple zero forces a strict drop of the sign-change count $\mathcal Z$; for sign-definite $\Theta$, $\mathcal Z \equiv 0$, so the conclusion $0 > 0$ is vacuous | [^134^][^135^] |
| Zero-repulsion / no-collision lemmas (CSV94; Tao I/II; Polymath15 Prop. 3.1(i)) | T2 | repulsion and simplicity hold only in the smoothing direction ($t > \Lambda$); CSV Lemma 2.2 confines multiple zeros to $t \le \Lambda$ — the dangerous direction *generates* the contact | [^136^][^137^][^138^] |
| Variation-diminishing / Pólya-frequency convolution | T1/T3 | VD convolution bounds sign changes; a touch-without-crossing creates none; the dBN kernel is certified not PF$_5$ [AUDIT: sound, interval certificate] | [^140^][^141^] |
| Turán/Jensen hyperbolicity hierarchy | T7 at full strength; moment-level otherwise | degree-2/3 fragments unconditional; full hierarchy ⟺ RH; asymptotic fragments carry no pointwise $(t,\xi)$ content | [^142^][^143^][^144^][^145^] |
| Almost-periodic rigidity (Bohr; Jessen–Tornehave) | obstruction | the theory propagates zeros with positive density, never excludes a first zero; $(1-\cos x) + (1-\cos\sqrt2\,x) \ge 0$ has a nondegenerate double zero at $0$ [VERIFIED] | [^146^][^147^] |
| Sepúlcre–Vidal dominance criterion | obstruction | the no-dominance inequalities *hold* for the Gaussian-weighted coefficients, so zeros of $K_{\mathrm{pr}}$ provably exist in the relevant strips | [^148^] |
| Montgomery–Vaughan MVT; large sieve; Hilbert inequality; Turán power sums | T4/T6 | $L^2$-means, well-spaced samples, or $\exists\nu$ quantifiers; a pointwise double zero at prescribed $\xi^*$ is invisible | [^149^][^150^][^151^] |
| Baker–Wüstholz linear forms in logarithms | T5 (quantitatively void) | the lower bound decays exponentially in the number of active frequencies ($\sim e^{c\sqrt t}$); no alignment exclusion at tolerance $O(1/\#\text{frequencies})$ | [^152^] |
| Uncertainty principles (Hardy; Beurling–Hörmander; Cowling–Price) | T1/T4 | they couple global decay of $f$ and $\hat f$; $\Theta(t,\cdot)$ does not decay in $\xi$, and a pointwise "$f$ and $f'$ both small" principle is false | [^153^][^154^] |
| Window-margin propagation beyond the prime-free window | obstruction | certified margins collapse at the Landau–Widom rate ($\lambda^*(2) \le 3.2\times10^{-283}$ [AUDIT: Medium constants]) while Gaussian-tail truncation error decays only as $e^{-a^2/4t}$; crossover at $t \lesssim 0.1$ | [^155^][^156^][^157^] |
| Envelope / one-stroke certificates beyond support $\approx 3.2$ | obstruction | any pointwise-envelope certificate must resolve frequencies up to $T_1 = 2\pi e^{A_L}$, $A_L \sim 4e^L$ — doubly exponential, proved optimal via Weyl equidistribution | [^155^] |
| Strict-peak route | obstruction + T2/T5 | zeta ordinates obey $N(T) \sim (T/2\pi)\log(T/2\pi e)$, hence Beurling–Malliavin density $\infty$; any exponential-type multiplier vanishing at all nodes is $\equiv 0$; named-pair sign inference is Weil/Li positivity ⟺ RH; convolution powers change variance $t \mapsto t/k$ | [^158^][^159^][^160^][^161^][^162^] |
| SOS / Fejér–Riesz on the raw kernel | inapplicable | $\Theta$ is not a trigonometric polynomial (Gaussian envelope, infinite incommensurate spectrum $\{\log n\}$); any truncation changes the function | [^163^] |
| Fredholm-determinant criteria | nonexistent | verified null search: no proved theorem expresses RH or Weil positivity as the nonvanishing of a Fredholm determinant of an explicitly constructed trace-class operator [VERIFIED null result] | — |
| Grid-sampling positivity "proofs" | T6 | float64 evaluations of the geometric side produce spurious negative eigenvalues "structurally indistinguishable from a counterexample to RH"; documented precedents include a spurious negative scipy value at $(t,\xi) = (1.5, 20)$ traced to quadrature error in $K_\Gamma$ [VERIFIED] | [^155^][^164^] |
| Laguerre / differential-inequality route on $\Theta$ | detects, cannot exclude | the Laguerre expression $L_1[f] = (f')^2 - f f''$ vanishes *exactly* at multiple zeros (Csordas–Escassut identity); equality is the contact itself, so the inequality has no margin at the event | [^165^][^166^] |

**Interpretation of Table T4.2.** Two patterns organize the table. First, the obstruction rows are proved or verified facts *about the route class*, not failures of diligence: zero-number theory is vacuous at $\mathcal Z \equiv 0$; repulsion lemmas hold strictly above the threshold by CSV's own Corollary 2; the envelope barrier is optimal by equidistribution; the density wall uses only the unconditional zero count $N(T)$. These are load-bearing constraints for Chapters 5 and 6. Second, the blindness rows share one signature — each tool is calibrated to a *codimension-1* event (a sign change, a zero crossing, a large value somewhere) while the double contact is codimension 2 (value *and* slope). The float64 precedents in the grid-sampling row are recorded as hostile-test evidence, not anecdotes: every numerical acceptance test in this report is therefore required to run in certified interval arithmetic, and the spurious $(1.5, 20)$ evaluation is retained as a regression case.

#### 4.3.1 Zero-number theory is vacuous for sign-definite profiles

Sturm's comparison theory and Matano's lap-number theorem make the sign-change count of a parabolic solution non-increasing in time [^135^]; Angenent's theorem sharpens this: if $u(x_0, s) = u_x(x_0, s) = 0$ — literally our double contact — then $\mathcal Z(t_1) > \mathcal Z(t_2)$ for all $t_1 < s < t_2$ [VERIFIED][^134^]. For $\Theta \ge 0$ the zero number is identically $0$ before, at, and after any tangency, so the conclusion is empty, and the theory cannot distinguish $\Theta$ from a difference-of-two-Gaussians profile that does develop contacts (T1). Since $\Theta$ is forward-parabolic in $\tau = 1/(4t)$, the feared direction of increasing $t$ runs backward in parabolic time, where zero numbers may increase (T2) [VERIFIED]. Classification: **inapplicable (vacuous)**.

#### 4.3.2 Zero-repulsion lemmas work in the smoothing direction only

For the de Bruijn–Newman family, CSV94 Lemma 2.4 gives the zero-velocity ODE with its $1/\text{gap}$ repulsion term, and Corollary 2 states that for any $t > \Lambda$ the zeros of $H_t$ are real and simple [VERIFIED][^136^]; Tao's expositions make the repulsion/attraction dichotomy explicit, and Polymath15 Proposition 3.1 derives the same ODE while noting it was previously available only for $t > \Lambda$ [^137^][^138^]. Decisively, CSV Lemma 2.2 proves that a double zero forces $t_0 \le \Lambda$, and Remark 3 shows it then splits into two simple real zeros at $t_0 + \varepsilon$: **coalescence happens at the threshold; simplicity holds only strictly above it** [VERIFIED][^136^]. Rodgers–Tao's proof of $\Lambda \ge 0$ bypasses the critical time entirely [^139^]. Since $\Theta$'s parameter $t$ is the roughening direction, this machinery describes and generates the contact rather than forbidding it. Classification: **obstruction**.

#### 4.3.3 Variation-diminishing convolution and the Turán/Jensen hierarchy

Schoenberg's theory makes convolution with a Pólya-frequency kernel variation-diminishing [^140^]. Two independent barriers block the route: a double contact creates zero sign changes, so no VD statement can see it even in principle (T1); and the raw material fails — $K_{\mathrm{end}}$ oscillates, $K_{\mathrm{pr}}$ is signed, and the digamma term of $K_\Gamma$ is negative near the origin ($\operatorname{Re}\psi(1/4) \approx -4.227$), so no piece of $\Theta$ is PF in $\xi$, while on the zero side $K(u) = \Phi(|u|)$ is certified not PF$_5$ by a $5\times5$ Toeplitz minor enclosed in $[-1.8472496\times10^{-9}, -1.8472225\times10^{-9}]$ at $(u_0, h) = (0.01, 0.05)$, with global PF$_4$ open [AUDIT: sound after the v2 self-correction, interval certificate][^141^]. The Turán/Jensen hierarchy is moment-level: degrees 2 and 3 are unconditional [^142^], hyperbolicity for all $d \le 8$ and asymptotically in $n$ is proved by GORZ [^144^] with effective thresholds by GORTTW [^145^], but the full hierarchy is equivalent to RH via Pólya 1927, and the Csordas–Varga 1990 necessary-and-sufficient conditions are RH-equivalences [^143^]. Classification: **obstruction** (VD); **circular at full strength, moment-level otherwise** (hierarchy).

#### 4.3.4 Almost-periodic rigidity proves recurrence, never first-zero exclusion

Jessen–Tornehave (Acta Math. 77 (1945)) prove that zeros of an analytic almost-periodic function, once present, recur with positive density; the theory never asserts absence [^146^][^147^]. Two session counterexamples show that arithmetic frequency independence alone cannot break a contact: $f(x) = (1-\cos x) + (1-\cos\sqrt{2}\,x) \ge 0$ is Bohr almost-periodic with rationally independent frequencies and has a unique zero at $x = 0$, of order exactly $2$ with $f''(0) = 3$ [VERIFIED]; and $g(\xi) = \cos(\xi\log 2) + 0.7\cos(\xi\log 3)$ has a critical point at $\xi^* \approx 3.457850927738136$, so $g(\xi) - g(\xi^*)$ has an exact double zero *off* the symmetry axis [VERIFIED numerically] (the equal-weight analogue $\cos(\xi\log 2) + \cos(\xi\log 3) - 2$ realizes its double zero at $\xi = 0$ with second derivative $-1.6874\ldots$ [VERIFIED]). The Sepúlcre–Vidal dominance criterion (Theorem 6) makes this quantitative: $\sigma_0$ is the real projection of a zero iff no single term dominates, and completing the square in the Gaussian weights shows dominance fails exactly at the weight peak, so zeros of $K_{\mathrm{pr}}$ exist in the corresponding strips [^148^]. Classification: **obstruction**.

#### 4.3.5 Averaged tools, linear forms in logarithms, and uncertainty principles

The Montgomery–Vaughan mean value theorem and Hilbert inequality [^149^] and the large sieve with the sharp $\Delta = N - 1 + Q^2$ [^150^] are mean or sample-summed statements; Turán's second main theorem delivers a large value at *some* exponent rather than excluding simultaneous smallness at a *prescribed* $\xi^*$ [^151^]. All fail T4/T6. Baker–Wüstholz bounds for linear forms in logarithms have the right shape for forbidding phase alignment, but decay exponentially in the number of participating frequencies — $\sim e^{c\sqrt t}$ active primes at scale $t$ — so even elementary Liouville separation is dwarfed by the required tolerance; quantitatively void (T5) [^152^]. The Hardy, Beurling–Hörmander, and Cowling–Price principles couple the *global* decay of $f$ and $\hat f$; $\Theta(t,\cdot)$ does not decay in $\xi$ (its prime part is almost-periodic), and the pointwise principle actually needed — "$f$ and $f'$ cannot both be small at one point" — is false in general (T1) [^153^][^154^]. Classification: **inapplicable** (averaged/UP rows); **obstruction** (Baker row, quantitative).

#### 4.3.6 Margin propagation and one-stroke certificates die at doubly-exponential walls

Two quantified collapse mechanisms delimit every window-based route. First, the certified ground margin of the windowed Weil form obeys the Landau–Widom plunge law, tracked numerically by Connes–Consani's ζ-cycle computations and asymptotically by Fuchs's 1964 Theorem 1: $1 - \chi_2 \sim (2^{14}\sqrt{2\pi}/3^5)\, e^{-4\pi e^L} e^{(9/2)L}$ in support length $L$ [VERIFIED qualitatively][^156^][^157^]; the certified variational upper bound reaches $\lambda^*(2) \le 3.2\times 10^{-283}$ [AUDIT: Medium constants, unrefereed][^155^]. Propagating such a margin onto the Gaussian test function costs a tail error decaying only like $e^{-a^2/4t}$, so the margin loses beyond $t \lesssim 0.1$ [VERIFIED qualitatively; quantitative constants AUDIT: Medium via [^155^]]. Second, any pointwise-envelope (one-stroke) certificate must resolve frequencies up to $T_1 = 2\pi e^{A_L}$ with $A_L \sim 4e^L$ — doubly exponential, and proved optimal among pointwise envelopes because Weyl equidistribution of the $\mathbb Q$-independent $\{\log p\}$ forces the comb constant exactly (Zhu Theorem 1.4 and Lemma 3.2) [AUDIT: Medium][^155^]. Zhu's v1 support-2.38 claim was retracted in v2 for substituting a per-prime constant into the envelope — a wrong-direction error, a hostile-test-2 failure caught in the wild [AUDIT: retraction verified][^155^]. Classification: **obstruction**, twice over. The surviving direct-enclosure route — certifying $(\Theta, \partial_\xi\Theta)$ on boxes without routing through $\lambda^*(L)$ — is structurally different and is taken up in Chapter 5.

#### 4.3.7 The strict-peak route hits the Levin–Cartwright / Beurling–Malliavin density wall

A compact-support Mellin multiplier $F$ is entire of exponential type in the spectral variable; prescribing $F(\rho_0) = 1$, $F(1 - \bar\rho_0) = -1$ with suppression at all other zero nodes is provably impossible, unconditionally: the ordinates satisfy $N(T) \sim (T/2\pi)\log(T/2\pi e)$, hence Beurling–Malliavin density $b = \infty$ and completeness radius $\infty$ — any Cartwright-class function vanishing at all nodes vanishes identically [VERIFIED, refereed][^158^][^159^]. The complex-node extensions (Makarov–Poltoratski; Lyubarskii–Seip) and Landau's necessary density conditions confirm rather than evade the obstruction, and none assumes RH [^160^][^161^][^162^] [Medium, single-agent synthesis of refereed sources]. The relaxed version — a real-part-amplified peak at a named pair — is constructible, but the sign inference drawn from the amplified sums is exactly Weil/Li positivity, i.e. RH (circular, §4.2); and convolution powers $F^{*(2k+1)}$ change the Gaussian variance $t \mapsto t/k$, failing T2/T5. Classification: **obstruction** (exact interpolation) plus **circular** (named-pair inference).

#### 4.3.8 Finite-certificate blindness

Sum-of-squares and Fejér–Riesz certificates do not apply: $\Theta(t,\cdot)$ is not a trigonometric polynomial — Gaussian envelope plus the infinite incommensurate spectrum $\{\log n\}$ — and any truncation changes the function (T3) [^163^]. Fredholm-determinant criteria do not exist: a dedicated null search found no proved theorem expressing RH, or any Weil-form positivity, as the nonvanishing of a Fredholm determinant of an explicitly constructed trace-class operator [VERIFIED null result]. Grid-sampling "proofs" fail T6 outright, with documented failure modes: float64 evaluation of the geometric side produces spurious negative eigenvalues "structurally indistinguishable from a counterexample to RH" [AUDIT: Zhu §10][^155^]; Groskin's certification rule quantifies the blind spot — a finite-cutoff eigenvalue in $[-B_T, 0)$ certifies nothing [AUDIT: preprint][^164^]; and this sweep itself recorded a spurious negative scipy-quad evaluation of $\Theta$ at $(t, \xi) = (1.5, 20)$, traced to quadrature error in $K_\Gamma$ and corrected by 50-digit verification [VERIFIED]. Classification: **inapplicable / nonexistent / fails T6**.

#### 4.3.9 Difficulty calibration: the one-variable analogue is a 30-year-old open problem

Csordas's Open Problem 4.7 calibrates the difficulty: whether the first Laguerre inequality $L_1(x) = (H'(x))^2 - H(x)H''(x) \ge 0$ holds for all real $x$ for $H(x) = \xi(x/2)/8 = \int_0^\infty \Phi(t)\cos(xt)\,dt$ remains open; it is a necessary condition for RH, known only on $|x| < 1.09\times 10^9$ from zero verification [VERIFIED][^165^][^169^] — exactly the one-variable zero-side analogue of "critical point implies positive value". The Csordas–Escassut identity shows why differential inequalities cannot close the question: the Laguerre expression vanishes *exactly* at multiple zeros, and the inequality is sharp for the Laguerre–Pólya class ($e^{-x^2}$ attains sharpness for any strengthened constant) [VERIFIED][^166^] — $L_1$ *detects* a contact but has zero margin to *exclude* one. Analyticity reduces any contact to finite even order [^167^], and generic one-parameter theory identifies the fold $\Theta = \partial_\xi\Theta = 0$, $\partial_{\xi\xi}^2\Theta \neq 0$, $\partial_t\Theta \neq 0$ as the normal threshold event [^168^] — a normal form, not an obstruction, and the reason certified exclusion on compact boxes is well-posed while global exclusion by rigidity theorems is not.

## 5. The Strongest Surviving Attack and Its First Missing Object

### 5.1 Why synthesis is forced

The sweep's central structural finding is that the exclusion problem, taken globally, is exactly as hard as the Riemann hypothesis (RH) — from *both* sides of the explicit formula. On the zero side, the verified Gaussian explicit formula (identity E2, Chapter 1)

$$\Theta(t,\xi) = \tfrac12 \sum_{\rho} \big[e^{-t(\xi-\gamma_\rho)^2} + e^{-t(\xi+\gamma_\rho)^2}\big]$$

makes $\Theta > 0$ trivial under RH and makes any *unconditional global* exclusion theorem a proof of RH [^176^]. On the form side, Weil's criterion, Yoshida's non-degeneracy theorem, and Suzuki's screw-function equivalences all identify positivity of the Weil functional with RH, so no global form-level input is available without circularity (Chapter 4, Table T4.1) [^177^]. [DERIVED, insight I1] Consequently, range restriction is not a tactic but a logical necessity: every viable attack must be either (i) a certified statement on a compact $(t,\xi)$-region, (ii) conditional on a hypothesis strictly weaker than RH, or (iii) an obstruction. The difficulty is calibrated from below by Csordas's Open Problem 4.7 — even the one-variable zero-side analogue "critical point implies positive value" (the first Laguerre inequality for $H(x) = \xi(x/2)/8$) has been open for three decades and is verified only for $|x| < 1.09\times 10^{9}$ [^178^].

### 5.2 The attack protocol

[DERIVED, insight I10] The strongest surviving attack is a five-stage certified-exclusion pipeline. It is a synthesis no single dimension of the sweep proposes on its own: the barrier architecture of the de Bruijn–Newman literature, the on-axis complete-monotonicity structure, and modern sealed interval arithmetic, assembled around one shared computational object.

#### 5.2.1 Stage 1 — the enclosure object

Everything downstream gates on the certified enclosure functor D1 defined in §5.3: a ball-arithmetic machine that maps any box $[t_1,t_2]\times[\xi_1,\xi_2]$ to rigorous interval hulls of $\Theta$, $\partial_\xi\Theta$, and $\partial_{\xi\xi}\Theta$, uniformly on the box. Without D1 no statement about $\Theta$ beyond finite sampling is possible; with it, exclusion becomes engineering.

#### 5.2.2 Stage 2 — pilot: the on-axis complete-monotonicity sub-route

Because $\Theta$ is even in $\xi$, one has $\partial_\xi\Theta(t,0)\equiv 0$ (Chapter 1, §1.1.3), so the axis $\xi = 0$ is an automatic double-contact locus: any zero of $t \mapsto \Theta(t,0)$ is a finite double contact. On this slice the problem is one-variable and carries genuine arithmetic rigidity: with $s = 1/(4t)$,

$$-2\sqrt{\pi t}\,K_{\mathrm{pr}}(t,0) = \sum_{n\ge 2} \frac{\Lambda(n)}{\sqrt{n}}\, e^{-s(\log n)^2} =: P(s)$$

is a *completely monotone* function of $s$ — a Dirichlet series with non-negative weights $\Lambda(n)/\sqrt{n}$ against the completely monotone kernel $e^{-s(\log n)^2}$, hence CM by the Bernstein–Widder theorem [^179^]. Complete monotonicity implies log-convexity, which propagates pointwise certificates: a certified positive lower bound of $\Theta(t,0)$ at a moderate grid of $t$-values, combined with the CM structure of the negative part and elementary interval bounds on $K_{\mathrm{end}}(t,0) = e^{t/4}$ and $K_\Gamma(t,0)$, can be extended to a certified lower bound on an entire interval $[t_1,t_2]$. [DERIVED] This is the cheapest genuinely new non-circular content the sweep located: it uses the sign of $\Lambda(n)$ (true arithmetic input, discharging hostile test T1 relative to a generic signed profile), it needs no zero-side information (discharging T7), and its certification is one-dimensional. Its ceiling is equally clear: neither $K_{\mathrm{end}}(t,0)$ nor $K_\Gamma(t,0)$ is CM in $s$, so the on-axis statement is necessarily a *signed* inequality, and globally it remains RH-equivalent via E2 — its acceptance value is of type (c) only.

#### 5.2.3 Stage 3 — off-axis: barrier/first-contact transplant

[VERIFIED] The Polymath15 project certified an upper bound on the de Bruijn–Newman constant by reducing it to three finite checkable statements: an initial verification up to a height, an asymptotic zero-free region, and a *barrier* — an explicit region through which zeros are shown unable to pass as $t$ varies (their Theorem 1.2, with the zero-dynamics analysis of Propositions 3.1 and 3.3) [^180^]. Via E2, a double contact of $\Theta$ at $(t_*,\xi_*)$ is precisely a complex zero pair of the entire function $\Theta(t,\cdot)$ landing on the real axis — the same geometry Polymath15 controls, with winding-number arguments replaced by sign certificates of $(\Theta, \partial_\xi\Theta, \partial_{\xi\xi}\Theta)$ in boxes. The transplant is justified structurally by the fold normal form: since $\Theta(t,\cdot)$ is entire, a contact has finite even order, and near a contact the profile is a nondegenerate quadratic well, so the three-way per-box certificate "$\Theta > \varepsilon$ or $|\partial_\xi\Theta| > \varepsilon'$ or $\partial_{\xi\xi}\Theta > \varepsilon''$" is a *complete* exclusion criterion. [VERIFIED] Three literatures — Csordas–Smith–Varga's zero-collision analysis (double zeros occur exactly at the critical time), Angenent's parabolic zero-number theory, and Cerf/Golubitsky–Guillemin fold theory — unanimously show that no theorem-level transversality excludes the attained contact [^181^]; certification on boxes is therefore not one option among many but the only rigorous mode available.

#### 5.2.4 The dangerous box

[DERIVED, insight I3] The corrected contact identity E3 of Chapter 1,

$$A(t,\xi_*)^2 + \big(2\xi_* A(t,\xi_*) + B(t,\xi_*)/t\big)^2 = e^{t/2 - 2t\xi_*^2}, \qquad A := K_\Gamma + K_{\mathrm{pr}},\ B := \partial_\xi(K_\Gamma + K_{\mathrm{pr}}),$$

confines all possible contacts to a box: since $A$ and $B$ are bounded on compact $t$-intervals while the right-hand side decays super-exponentially in $|\xi_*|$, one obtains $|\xi_*| = O(t^{-1/2}\sqrt{\log})$ — concretely a rectangle $[t_1,t_2]\times[-\Xi,\Xi]$ with $\Xi = O(t_1^{-1/2}\sqrt{\log(1/\varepsilon)})$. Three independent lines of the sweep agree on this geometry: the algebraic localization from E3, the character coercivity at $|\xi|\to\infty$ together with the Hermite-branching asymptotics of zero collisions, and the box shape that interval certificates can actually fill [^182^]. Outside the box, coercivity and the established small-$t$ positivity cover the complement.

#### 5.2.5 Stage 4 — sealed replayable certificates

[VERIFIED as architecture; AUDIT: single-auditor infrastructure, Medium] The certification packaging should follow the pattern of the 2026 Gomila bound $\Lambda \le 0.1787854$: fail-closed Arb interval certificates, SHA256-pinned, replayable under a container on two operating systems [^183^]. The logical form of that work — instantiating the published Polymath15 Theorem 1.2 with machine-checked certificates against the Platt–Trudgian verified height $3\times 10^{12}$ [^184^] — is sound and independently reviewable; what is reusable here is the certificate architecture, not the bound.

#### 5.2.6 Stage 5 — mandatory negative controls

A positivity pipeline that cannot fail is worthless. Two controls are mandatory: (a) the identical pipeline applied to the Davenport–Heilbronn-analog kernel (whose underlying $L$-function has off-line zeros) *must detect* negativity or a contact — calibrating the resolution against the quantified blind zone of windowed certificates, Groskin's indecision band $[-B_T, 0)$ with $B_T \sim (2N+1)\rho\log T/(\pi^2 T)$ [AUDIT: theorem-level Medium] [^185^]; (b) the difference-of-two-Gaussians profile — the generic signed convolution that provably admits contacts (Chapter 1, §1.1.2) — must fail certification. Control (b) discharges hostile test T1 *by construction*: the pipeline certifies $\Theta$ itself with the signed prime sum retained, not an envelope, so passing T1 is a property of the object rather than an assumption.

### 5.3 The first missing typed object

**Definition D1 (enclosure functor).** A ball-arithmetic implementation, uniform in $(t,\xi)$ on compact boxes, of

$$\mathcal{E}:\ [t_1,t_2]\times[\xi_1,\xi_2] \longmapsto \big(I_0,\ I_1,\ I_2\big),\qquad \Theta \in I_0,\ \partial_\xi\Theta \in I_1,\ \partial_{\xi\xi}\Theta \in I_2\ \text{on the box},$$

with rigorous interval hulls. Its elementary components all exist: $K_{\mathrm{end}}$ is closed form; $\partial_\xi K_{\mathrm{end}}$, $\partial_\xi K_{\mathrm{pr}}$ are closed-form sums (Chapter 1); $K_\Gamma$ and its $\xi$-derivatives are Gaussian convolutions against $\mathrm{Re}\,\psi(1/4 + iu/2) \sim \tfrac12\log|u|$, certifiable by Arb quadrature with explicit tails [^186^]; uniformity in $\xi$ is free since $|\cos|, |\sin| \le 1$.

**Estimate E* (the single non-elementary component).** An explicit uniform prime-tail bound of the form

$$\Big|\sum_{n>N} \frac{\Lambda(n)}{\sqrt{n}}\, e^{-(\log n)^2/(4t)} \cos(\xi\log n)\Big| \;\le\; C(t_2)\sum_{n>N} \frac{\Lambda(n)}{\sqrt{n}}\, e^{-(\log n)^2/(4t_1)},$$

obtained by partial summation against the kernel $e^{-(\log n)^2/(4t)}$ — monotone in $n$ on the tail — with Rosser–Schoenfeld-grade explicit prime-number-theorem bounds [^187^]. The Gaussian decay makes the tail converge super-polynomially; what is missing is not analysis but its packaging into an explicit, certified constant.

[DERIVED, insight I6] That D1/E* is *the* gap — rather than one gap among several — is evidenced by triple independent demand: the certified-reduction dimension requests exactly this enclosure (its Lead L1, with the cost law below); the localized-form dimension requests its form-side avatar, a form-continuity estimate $|Q_W(g) - Q_W(g\cdot\mathbf{1}_{[-L,L]})| \le C(t)\cdot\mathrm{tailmass}$, listing the four ingredients already available (Bombieri's form domination, the exact archimedean functional of the truncated test function, the explicit prime entries, and the two-sided certification budget); and the rigidity dimension requests certified strip zero-freeness plus certified $\partial_{\xi\xi}\Theta > 0$ — the same object under the E2 interface [^188^]. Building D1/E* is explicit-estimates engineering, not new theory.

**Cost law.** [VERIFIED as estimate] The prime-sum truncation required for tail error $\varepsilon$ at time $t$ scales as $N \sim \exp(O(\sqrt{t}\,|\log\varepsilon|))$: the exponent $(\log n)^2/(4t)$ must reach $|\log\varepsilon|$, forcing $\log N \asymp 2\sqrt{t\,|\log\varepsilon|}$ [^189^]. This law is the explicit feasibility boundary for the pilot: at $t = 2$ and $\varepsilon = 10^{-12}$ the cutoff is $N \approx e^{10.6} \approx 4\times 10^{4}$ prime powers — trivially computable — while the same accuracy at $t = 50$ requires $N \approx e^{53}$, beyond reach. The unresolved $t$-interval the pilot can realistically cover in one engineering phase is therefore roughly $0.05 \le t \le 10$, a nontrivial interval adjacent to (and overlapping) the already-established small-$t$ regime.

## 6. Executable Acceptance Test

### 6.1 Protocol P1

The sweep's required executable acceptance test is the pilot instantiation of the Chapter-5 attack. It is stated here as a runnable protocol: every input already exists as software or as an explicit estimate except the enclosure functor D1 and its prime-tail estimate E*, whose construction is the designated next action (Chapter 5, §5.3).

**Protocol P1 — certified exclusion of finite double contact on a compact region.**

**Inputs.** (i) The enclosure functor D1 (Definition, Ch. 5 §5.3.1) implemented in Arb or mpmath.iv ball arithmetic, covering $\Theta$, $\partial_\xi\Theta$, $\partial_{\xi\xi}\Theta$ on axis-aligned boxes [^201^]; (ii) the explicit uniform prime-tail bound E* (Ch. 5 §5.3.2) with Rosser–Schoenfeld-grade constants [^202^]; (iii) the half-width $\Xi = \Xi(t_1,\varepsilon) = O(t_1^{-1/2}\sqrt{\log(1/\varepsilon)})$ computed from the corrected contact identity E3, $A^2 + (2\xi A + B/t)^2 = e^{t/2-2t\xi^2}$ [^203^]; (iv) the explicit prime-tail budget assigning each box a truncation $N$ with certified tail error below the box's target margin.

**Step (i) — on-axis pilot.** Certify

$$\min_{t \in [t_1,t_2]} \operatorname{lower}(\Theta(t,0)) > 0,$$

with the initial target interval $[t_1, t_2] = [0.05, 2.0]$. Evaluation points are placed on a grid; between grid points the lower enclosure is propagated using the log-convexity of the completely monotone prime profile $P(s) = \sum_{n\ge2} \Lambda(n)n^{-1/2} e^{-s(\log n)^2}$, $s = 1/(4t)$, against elementary interval bounds on $K_{\mathrm{end}}(t,0) = e^{t/4}$ and $K_\Gamma(t,0)$ [^204^]. Because $\partial_\xi\Theta(t,0) \equiv 0$, each certified on-axis point closes the contact question on that fiber entirely.

**Step (ii) — off-axis branch-and-bound.** Subdivide $[t_1,t_2]\times[-\Xi,\Xi]$ and certify per box the three-way alternative

$$\Theta > \varepsilon \quad\lor\quad |\partial_\xi\Theta| > \varepsilon' \quad\lor\quad \partial_{\xi\xi}\Theta > \varepsilon'' ,$$

which is complete by the fold normal form (analyticity forces finite even contact order; near a contact the profile is a nondegenerate quadratic well) [^205^]. Boxes whose center meets the corrected-E3 threshold — where the target radius $e^{t/4 - t\xi^2}$ is within a factor $1{,}000$ of the enclosure of $\sqrt{A^2 + (2\xi A + B/t)^2}$ — receive priority refinement. The complement of the box is covered by character coercivity (large $|\xi|$) and the established small-$t$ positivity (small $t$).

**Step (iii) — negative control (a).** Run the identical pipeline on the Davenport–Heilbronn-analog kernel (same archimedean and endpoint structure; underlying $L$-function with zeros off the critical line) [^206^]. The pipeline **must fail**: it must either detect a certified negative region or certify a contact. The detected failure scale is then compared against the indecision band $[-B_T, 0)$, $B_T \sim (2N+1)\rho\log T/(\pi^2 T)$, that blinds windowed finite-rank certificates — documenting that the pointwise pipeline's blind zone is strictly smaller than the band [^207^].

**Step (iv) — negative control (b).** Run the identical pipeline on the difference-of-two-Gaussians profile — the generic signed Gaussian convolution that provably admits a finite double contact (Chapter 1, §1.1.2). The pipeline **must fail** there. This certifies that the pipeline does not pass hostile test T1 spuriously: a pass for $\Theta$ is attributable to the arithmetic content retained in the enclosure (the signed von Mangoldt weights), not to a generic convolution property.

**Pass criterion.** P1 passes if and only if every box of the dangerous rectangle is certified *and* both negative controls behave as required (detection of failure in both). Anything less — uncertified boxes, skipped controls, float64 spot checks substituted for ball arithmetic — certifies nothing.

### 6.2 Coverage and failure modes

Table T6.1 records which hostile tests each component of P1 discharges.

| Protocol component | T1 two-Gaussians | T2 variance direction | T3 signed primes | T4 all real ξ | T5 uniform in t | T6 global not sampling | T7 no hidden RH |
|---|---|---|---|---|---|---|---|
| Enclosure D1 of $\Theta$ itself | — | n/a (no variance comparison) | ✓ (signed weights retained) | ✓ ($|\cos|,|\sin|\le 1$ uniformity) | ✓ (ball arithmetic on boxes) | ✓ (per-box certificates) | ✓ (no zero-side input) |
| Step (i) on-axis pilot | ✓ (uses $\Lambda \ge 0$) | n/a | ✓ | axis only | ✓ | ✓ on $[t_1,t_2]$ | ✓ |
| Step (ii) branch-and-bound | — | n/a | ✓ | ✓ (box + coercivity) | ✓ | ✓ | ✓ |
| Control (a) Davenport–Heilbronn | — | — | — | — | — | ✓ (falsifiability) | — |
| Control (b) two Gaussians | ✓ (by construction) | — | — | — | — | ✓ (falsifiability) | — |

The table's content is that the pipeline's claims are structural rather than sampled: every hostile test is discharged either by the object itself (the enclosure retains the signed prime contribution and is uniform on boxes) or by an explicit falsifiable control. This is the precise sense in which P1 differs from the grid-sampling "proofs" rejected in Chapter 4 (§4.3.8): there, finite evaluation was the conclusion; here, finite certified bounds plus structural propagation are the proof.

**Failure-mode ledger.** Three documented precedents delimit where P1 can silently lie, and each is assigned a countermeasure. First, float64 evaluations of the geometric (prime) side of the explicit formula can produce sign artifacts "structurally indistinguishable from a counterexample to RH" (Zhu, §10) — countermeasure: ball arithmetic everywhere, with the certificate sealed fail-closed [^208^]. Second, near-contacts smaller than a certificate's resolution are structurally invisible; for windowed finite-rank certificates this blind zone is exactly the indecision band $[-B_T, 0)$ — countermeasure: control (a) forces the pipeline to demonstrate its resolution on a kernel where failure is known to occur [^207^]. Third, spurious sign flips from quadrature at large $|\xi|$ (a spurious negative value of $\Theta$ at $(t,\xi) = (1.5, 20)$ was produced during the sweep by an insufficiently sampled quadrature and retracted on re-evaluation) — countermeasure: certified quadrature with explicit tails rather than adaptive float quadrature [^209^]. A pipeline that survives these three failure modes on the controls and certifies every box constitutes a proof of $\Theta(t,\xi) > 0$ on $[t_1,t_2]\times\mathbb{R}$ for the covered $t$-interval — a type-(c) acceptance result.

## 7. Verdict: Route Priority and Acceptance-Criterion Adjudication

### 7.1 Route-priority verdict

**Priority verdict.** Development effort should go to the **compact-window route — exclusively in its direct-enclosure form**: the branch-and-bound certification architecture applied pointwise to $\Theta$ (the enclosure-functor approach of Chapter 5), transplanted with the Polymath15 barrier/first-contact method [^221^], with the **on-axis complete-monotonicity sub-route — the newly found route of this sweep — executed first** as the cheapest genuinely non-circular pilot (Chapter 5, §5.2.2). The two components share a single gating object (Definition D1 / Estimate E*), so building the enclosure advances both at once.

The two rival routes are disposed of as follows.

**Window-form-margin variant of the compact-window route: eliminated.** Propagating certified positivity margins of the windowed Weil form to the pointwise kernel fails quantitatively, not merely technically: the true margin of the windowed form collapses super-exponentially in window length (Landau–Widom plunge law; certified $\lambda^*(2) \le 3.2\times 10^{-283}$, with the qualitative arm underwritten by refereed prolate-spheroidal asymptotics [^222^] and Connes–Consani numerics), while the Gaussian-truncation error it would have to dominate decays only exponentially ($e^{-a^2/(4t)}$). The crossover is immediate beyond the prime-free window, covering only $t \lesssim 0.1$ [^223^]. Independently, envelope-based one-stroke certificates are capped by a proved-optimal doubly-exponential barrier $T_1 = 2\pi e^{A_L}$, $A_L \sim 4e^{L}$ (Weyl equidistribution of $\{\log p\}$ makes the comb constant optimal) [^224^]. Both obstructions are quantitative theorems, not resource limitations.

**Strict-peak route: rejected.** A compact-support Mellin multiplier isolating a hypothetical off-line reciprocal zero pair cannot exist: the zeta ordinates have counting function $N(T) \sim (T/2\pi)\log(T/2\pi e)$, hence infinite Beurling–Malliavin density and infinite completeness radius, so any entire function of exponential type vanishing at all zero nodes is identically zero (Levin–Cartwright; Beurling–Malliavin; confirmed for complex nodes by Makarov–Poltoratski and Lyubarskii–Seip) [^225^]. The relaxed variant — a strict peak at a *named* pair — collapses into Li-criterion positivity, i.e., RH itself, and convolution powers change the Gaussian variance in the wrong direction (hostile tests T2, T5, T7). Near-contacts are additionally structurally uncertifiable at finite rank inside the indecision band $[-B_T, 0)$ [^226^].

**Newly found route (on-axis CM): first-executed, not standalone.** It is the only sub-problem with an automatic contact condition ($\partial_\xi\Theta(t,0)\equiv0$), theorem-grade arithmetic rigidity (complete monotonicity from $\Lambda(n)\ge0$), and one-variable certification; but globally it remains RH-equivalent via identity E2, so its acceptance value is type (c) on compact intervals only.

### 7.2 Acceptance-criterion adjudication

Table T7.1 adjudicates the sweep against its five success criteria.

| Criterion | Status | Evidence |
|---|---|---|
| (a) Unconditional theorem excluding finite double contact | **Not achieved — shown RH-equivalent** | Zero side: E2, $\Theta = \tfrac12\sum_\rho[\,\cdots]$ [^227^]; form side: Weil 1952, Yoshida Thm 2, Suzuki Thms, Li criterion (Ch. 4, Table T4.1) [^228^] |
| (b) Conditional theorem with unmet hypotheses strictly weaker than RH, independently testable | **Not found in the swept literature** | Every conditional item assumes RH, partial RH (finitely many off-line zeros, Bombieri Thm 8), or unproved spectral hypotheses (CCM simple + even ground state) [^229^] |
| (c) Quantitative compact-window estimate covering a nontrivial unresolved $t$-interval | **Achievable and fully staged; not yet executed** | Geometry (corrected E3 box), missing object (D1/E*), pilot (on-axis CM), test (Protocol P1) all specified; feasibility bounded by $N \sim \exp(O(\sqrt{t}\,|\log\varepsilon|))$ (Ch. 5 §5.3.4) [^230^] |
| (d) Finite certified reduction preserving the entire signed Weil functional | **Partial** | Exists for the windowed operator: Zhu's one-stroke PSD certificate at $L = 0.8$ [AUDIT: Medium]; Groskin's exact dictionary — but provably blind inside $[-B_T,0)$ and not a reduction of pointwise $\Theta$ [^231^] |
| (e) Rigorous obstruction eliminating one of the remaining routes | **Achieved, fivefold** | (e1) envelope/one-stroke route beyond support $\approx 3.2$ [^224^]; (e2) window-margin propagation (Landau–Widom crossover) [^222^][^223^]; (e3) strict-peak route (density wall) [^225^]; (e4) total-positivity/variation-diminishing route (certified non-PF5; blind to tangencies) [^232^]; (e5) zero-number/rigidity/transversality routes (vacuous or contact-forcing; AP counterexample) [^233^] |

The pattern behind Table T7.1 is exact, not accidental: the criteria split along the RH-equivalence boundary. Everything global and unconditional (a) is equivalent to RH (Chapter 1, E2; Chapter 4, Table T4.1); everything strictly weaker than RH and conditional (b) does not exist in the literature; what remains achievable is compact and certified (c), windowed but blind (d), or negative but rigorous (e).

**Sweep verdict.** The sweep **succeeds via criterion (e)**, with criterion (c) fully staged as the designated next executable deliverable. The single highest-leverage next action is constructing the enclosure functor D1 with its prime-tail estimate E* — analysis-grade packaging, no new theory — and running the on-axis pilot of Protocol P1 on $[0.05, 2.0]$.

**Honesty clause.** No applicable global exclusion theorem exists in the swept literature, and the sweep's catalogue is obstruction-dominant by *proved necessity* — a global exclusion theorem would prove the Riemann hypothesis — rather than by search failure. The clearest calibration of the remaining difficulty is Csordas's Open Problem 4.7: even the one-variable zero-side shadow of the critical-point inequality has resisted three decades [^234^]. What this sweep adds is a certified map of exactly which walls are proved walls, which routes pass all seven hostile tests, and the single typed object whose construction converts the surviving route from a program into a computation.


# References

[^1^] Double-contact sweep mission brief, "Deep literature-sweep task: arithmetic exclusion of finite double contact" (session input, 2026), kernel normalization, established facts, source requirements. File: /mnt/agents/upload/user_pasted_clipboard_long_content_as_file_Deep literature-sw.txt.

[^2^] Double-contact sweep research program, "Dimension 02 — Weil positivity and positive-definite structures of von Mangoldt coefficients" (session research file, 2026), Headlines 1–5 and C12 (Θ = c(t)·W(φ_{t,ξ}); Bochner diagnosis). File: /mnt/agents/output/research/double_contact_dim02.md.

[^3^] Double-contact sweep research program, "Dimension 11 — Direct contact obstruction from the explicit formula" (session research file, 2026), §1–§1.1 (sympy-verified derivatives of all three kernel pieces; contact equations; printed DC identity quarantined as mis-signed). File: /mnt/agents/output/research/double_contact_dim11.md.

[^4^] Double-contact sweep research program, "Dimension 08 — Rigidity at an attained threshold; zero dynamics of heat flows" (session research file, 2026), SF1 (parabolic equation, numerically verified to ≤1.4×10⁻⁶ relative error), SF2 (Gaussian explicit formula; mpmath, 50 digits, N = 80,000 prime powers), C12 (almost-periodic double-zero counterexample). File: /mnt/agents/output/research/double_contact_dim08.md.

[^5^] S. B. Angenent, "The zero set of a solution of a parabolic equation," J. Reine Angew. Math. 390 (1988), 79–96, Theorem A. DOI 10.1515/crll.1988.390.79. https://doi.org/10.1515/crll.1988.390.79

[^6^] W. Michałowski, "On the Pólya Frequency Order of the de Bruijn–Newman Kernel: Certified Failure at Order Five and the Toeplitz Threshold Phenomenon," arXiv:2602.20313v2 (2026, unrefereed; interval-arithmetic certificate), Theorem 1.1. [AUDIT: sound post-correction; certified obstruction.] https://arxiv.org/abs/2602.20313

[^7^] B. Jessen, H. Tornehave, "Mean motions and zeros of almost periodic functions," Acta Math. 77 (1945), 137–279. DOI 10.1007/BF02392225. https://projecteuclid.org/journals/acta-mathematica/volume-77/issue-none/Mean-motions-and-zeros-of-almost-periodic-functions/10.1007/BF02392225.full

[^8^] G. Csordas, R. S. Varga, "Moment inequalities and the Riemann hypothesis," Constr. Approx. 4 (1988), 175–198, Theorem 2.4. DOI 10.1007/BF02075457. https://link.springer.com/article/10.1007/BF02075457

[^9^] M. Griffin, K. Ono, L. Rolen, D. Zagier, "Jensen polynomials for the Riemann zeta function and other sequences," Proc. Natl. Acad. Sci. USA 116 (2019), 11103–11110. DOI 10.1073/pnas.1902572116. arXiv:1902.07321. https://arxiv.org/abs/1902.07321

[^10^] Double-contact sweep research program, "Dimension 03 — Logarithmic-derivative and log-concavity inequalities after Gaussian regularization" (session research file, 2026), H6 (evenness; ξ = 0 automatic double-contact slice; sweep-original flag), C3 (Turán/Jensen hierarchy). File: /mnt/agents/output/research/double_contact_dim03.md.

[^11^] S. Bochner, Bochner–Herglotz positive-definiteness theorem for almost-periodic functions (Fourier coefficients of a positive discrete Bohr measure), as stated and applied in [^2^], C12; cf. statement in arXiv:0712.0058, §1. https://arxiv.org/abs/0712.0058

[^12^] G. Csordas, W. Smith, R. S. Varga, "Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis," Constr. Approx. 10 (1994), no. 1, 107–129, Lemma 2.2, Remark 3, Corollary 2. DOI 10.1007/BF01205170.

[^13^] D. H. J. Polymath, "Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant," Res. Math. Sci. 6 (2019), Art. 31, Theorem 1.2, Propositions 3.1, 3.3. arXiv:1904.12438. https://arxiv.org/abs/1904.12438

[^14^] Double-contact sweep research program, "Phase 6 — Cross-Dimensional Insight Extraction" (session research file, 2026), Insight I0 (correction of the contact-identity exponent and B/t sign), I1 (RH-equivalence of global exclusion), I3 (dangerous-region localization). File: /mnt/agents/output/research/double_contact_insight.md.

[^15^] A. Weil, "Sur les 'formules explicites' de la théorie des nombres premiers," Comm. Sém. Math. Univ. Lund (Medd. Lunds Univ. Mat. Sem.), Tome Supplémentaire (1952), 252–265; compact-support formulation: H. Yoshida, "On Hermitian forms attached to zeta functions," in Zeta Functions in Geometry, Adv. Stud. Pure Math. 21, Kinokuniya, Tokyo (1992), 281–325. Restatement: https://arxiv.org/abs/2301.00421

[^16^] Double-contact sweep research program, "Dimension 12 — Hostile audit of unrefereed claims" (session research file, 2026), §6 (four dedicated searches; zero external hits for Θ(t,ξ)/"Marici"/"BRS symmetrized"). File: /mnt/agents/output/research/double_contact_dim12.md.

[^17^] Double-contact sweep research program, "Cross-Verification — Double-Contact Literature Sweep (Phase 4/5)" (session research file, 2026), §1 tier table (T1, T2, T17, T18), §3 adjudications 1–2, tier rule (no High-tier claim on unrefereed items). File: /mnt/agents/output/research/double_contact_cross_verification.md.

## References for Chapter 2 ([^31^]–[^51^])

[^31^] Double-Contact Literature Sweep, "Cross-Verification (Phase 4/5): tier table T1–T22, conflict zones CZ-1–CZ-14, preprint validation," internal sweep document (2026). /mnt/agents/output/research/double_contact_cross_verification.md

[^32^] Double-Contact Literature Sweep, "Dimension 12 — Hostile audit of recent unrefereed preprints (2024–2026)," internal sweep document (2026). /mnt/agents/output/research/double_contact_dim12.md

[^33^] Sweep mission brief, "Deep literature-sweep task: arithmetic exclusion of finite double contact," task specification with source requirements and hostile tests (2026). /mnt/agents/upload/user_pasted_clipboard_long_content_as_file_Deep literature-sw.txt

[^34^] Double-Contact Literature Sweep, "Phase 6 — Cross-Dimensional Insight Extraction (insights I0–I10)," internal sweep document (2026). /mnt/agents/output/research/double_contact_insight.md

[^35^] D. H. J. Polymath, "Effective approximation of heat flow evolution of the Riemann ξ function, and upper bounds for the de Bruijn–Newman constant," Research in the Mathematical Sciences 6 (2019), Article 31. DOI 10.1007/s40687-019-0193-1. arXiv:1904.12438. https://arxiv.org/abs/1904.12438

[^36^] G. Csordas, T. S. Norfolk, R. S. Varga, "The Riemann hypothesis and the Turán inequalities," Transactions of the American Mathematical Society 296 (1986), 521–541. DOI 10.1090/S0002-9947-1986-0846596-1.

[^37^] X. Zhu, "Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law," arXiv:2608.24827v2 (2026). https://arxiv.org/abs/2608.24827 — authorship resolved from the v2 title page (Xuefeng Zhu, Dalian University of Technology); "M. Chuk" survives only in index metadata.

[^38^] A. Gershon, "The De Bruijn–Newman Constant Is Zero," Preprints 202604.1513.v1 (2026). DOI 10.20944/preprints202604.1513.v1. https://www.preprints.org/manuscript/202604.1513/v1 — circular by its own Remark 19; excluded.

[^39^] J. B. Conrey, X.-J. Li, "A note on some positivity conditions related to zeta and L-functions," International Mathematics Research Notices 2000 (2000), no. 18, 929–940. arXiv:math/9812166. https://arxiv.org/abs/math/9812166

[^40^] W. H. J. Fuchs, "On the eigenvalues of an integral equation arising in the theory of band-limited signals," Journal of Mathematical Analysis and Applications 9 (1964), 317–330.

[^41^] H. Yoshida, "On Hermitian Forms attached to Zeta Functions," in Zeta Functions in Geometry, Advanced Studies in Pure Mathematics 21, Kinokuniya, Tokyo (1992), 281–325. — page range confirmed by three independent reference lists (Bombieri 2000 bibliography; Suzuki 2026 ref. [17]; arXiv:2301.00421 ref. [16]).

[^42^] M. Suzuki, "Aspects of the screw function corresponding to the Riemann zeta function," Journal of the London Mathematical Society 108 (2023), no. 4, 1448–1487. DOI 10.1112/jlms.12785. arXiv:2206.03682. https://arxiv.org/abs/2206.03682

[^43^] G. Csordas, W. Smith, R. S. Varga, "Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann Hypothesis," Constructive Approximation 10 (1994), 107–129. DOI 10.1007/BF01205170.

[^44^] J.-F. Burnol, "Sur les Formules Explicites I: analyse invariante," Comptes Rendus de l'Académie des Sciences Paris, Série I 331 (2000), 423–428. arXiv:math/0101068. https://arxiv.org/abs/math/0101068

[^45^] J.-F. Burnol, "On an analytic estimate in the theory of the Riemann zeta function and a theorem of Báez-Duarte," Acta Científica Venezolana 54 (2003), no. 3, 210–215. arXiv:math/0202166. https://arxiv.org/abs/math/0202166 — RH-conditional.

[^46^] E. Bombieri, "A variational approach to the explicit formula," Communications on Pure and Applied Mathematics 56 (2003), no. 8, 1151–1164. DOI 10.1002/cpa.10089. https://onlinelibrary.wiley.com/doi/10.1002/cpa.10089

[^47^] M. Suzuki, "Weil's quadratic form via the screw function," arXiv:2606.09096v2 (2026). https://arxiv.org/abs/2606.09096 — framework paper; Corollary 1.6 conjectural.

[^48^] A. Groskin, "A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form," arXiv:2607.02828v3 (2026). https://arxiv.org/abs/2607.02828 — theorem-level content usable; numerical certificates not interval-certified.

[^49^] W. Michałowski, "On the Pólya Frequency Order of the de Bruijn–Newman Kernel: Certified Failure at Order Five and the Toeplitz Threshold Phenomenon," arXiv:2602.20313v2 (2026). https://arxiv.org/abs/2602.20313 — code: https://github.com/ScypyonX/pf5-dbn-kernel-certificates

[^50^] J. Gomila, "Λ ≤ 0.1787854," blog post and audit repository (2026). https://www.judegomila.com/posts/riemann-lambda-0.1787854 ; https://github.com/judegomila/dbn-lambda-01787854-candidate-audit — single-auditor, unreplayed; cite architecture only.

[^51^] T. Kim, Y. Hong, M. Kim, S. Choi, J. Jang, M. Kim, "A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator," arXiv:2607.24830 (2026). https://arxiv.org/abs/2607.24830 — low credibility; excluded from evidence.

[^61^] D. H. J. Polymath, "Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant," Research in the Mathematical Sciences 6 (2019), no. 3, Paper No. 31, 67 pp. DOI 10.1007/s40687-019-0193-1. arXiv:1904.12438. https://arxiv.org/abs/1904.12438

[^62^] D. Platt, T. Trudgian, "The Riemann hypothesis is true up to 3·10¹²," Bulletin of the London Mathematical Society 53 (2021), no. 3, 792–797. DOI 10.1112/blms.12460. arXiv:2004.09765. https://arxiv.org/abs/2004.09765

[^63^] J. Gomila, "de Bruijn–Newman constant Λ ≤ 0.1787854 — candidate audit" (blog post and sealed-certificate repository, August 2026; unrefereed, single-auditor; external review in progress). https://github.com/judegomila/dbn-lambda-01787854-candidate-audit

[^64^] Sweep-original derivation (research file double_contact_dim03.md, item C13; corroborated by dim09): complete monotonicity of P(s) = Σ Λ(n)/√n e^{−s(log n)²} in s = 1/(4t); non-CM of K_end(t,0), K_Γ(t,0). Background theorem: Bernstein–Widder representation, e.g. D. V. Widder, The Laplace Transform, Princeton University Press, Princeton, 1941.

[^65^] Session-verified computations, this sweep (research files double_contact_dim08.md, structural facts SF1/SF2; double_contact_dim11.md, contact identity; double_contact_dim02.md, form-side identification): E1 PDE (finite-difference relative error ≤ 5.05×10⁻⁶); E2 Gaussian explicit formula, mpmath 50-digit, N = 80,000 prime powers, ≥9-digit agreement on and between zero heights; E3 corrected contact identity, sympy-verified. Internal record, /mnt/agents/output/research/.

[^66^] X. Zhu, "Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law," arXiv:2608.24827v2 (v1 25 Aug 2026; v2 2 Sep 2026). DOI 10.48550/arXiv.2608.24827. https://arxiv.org/abs/2608.24827 — Unrefereed preprint. Authorship metadata anomaly resolved to Xuefeng Zhu, Dalian University of Technology, from the v2 title page (index metadata "Marcus Chuk" survives in some indexes).

[^67^] Hostile preprint audit, this sweep (research file double_contact_dim12.md): Zhu arXiv:2608.24827v2 sound post-retraction, narrow, unreproduced; Suzuki arXiv:2606.09096 honest framework, no overclaim; Groskin arXiv:2607.02828 theorem-level usable, numerics not interval-certified; Gomila logically sound, single-auditor; Gershon preprints.org 202604.1513.v1 circular (excluded); Kim et al. arXiv:2607.24830 low credibility (excluded). Internal record, /mnt/agents/output/research/.

[^68^] M. Suzuki, "Aspects of the screw function corresponding to the Riemann zeta function," Journal of the London Mathematical Society (2) 108 (2023), no. 4, 1448–1487. DOI 10.1112/jlms.12785. arXiv:2206.03682. https://arxiv.org/abs/2206.03682

[^69^] M. Suzuki, "Weil's quadratic form via the screw function," arXiv:2606.09096v2 (v1 8 Jun 2026; v2 24 Aug 2026). DOI 10.48550/arXiv.2606.09096. https://arxiv.org/abs/2606.09096 — Unrefereed preprint.

[^70^] H. Yoshida, "On Hermitian forms attached to zeta functions," in Zeta Functions in Geometry (Tokyo, 1990), Advanced Studies in Pure Mathematics 21, Kinokuniya, Tokyo, 1992, 281–325. DOI 10.2969/aspm/02110281. MR 1210794.

[^71^] E. Bombieri, "Remarks on Weil's quadratic functional in the theory of prime numbers, I," Atti della Accademia Nazionale dei Lincei, Rendiconti Lincei (9) Matematica e Applicazioni 11 (2000), no. 3, 183–233. https://eudml.org/doc/252338 ; http://www.bdim.eu/item?fmt=pdf&id=RLIN_2000_9_11_3_183_0

[^72^] E. Bombieri, "A variational approach to the explicit formula," Communications on Pure and Applied Mathematics 56 (2003), no. 8, 1151–1164. DOI 10.1002/cpa.10089. https://onlinelibrary.wiley.com/doi/10.1002/cpa.10089 — Paywalled; theorem-number-level detail pinned via Suzuki 2026 [^69^] and Broughan, Equivalents of the Riemann Hypothesis, Vol. 2, Ch. 9, Cambridge Univ. Press, 2017.

[^73^] A. Groskin, "A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form," arXiv:2607.02828v3 (v1 2 Jul 2026; v3 14 Aug 2026). DOI 10.48550/arXiv.2607.02828. https://arxiv.org/abs/2607.02828 — Unrefereed preprint; numerical certificates not interval-certified and not cited.

[^74^] A. Connes, W. D. van Suijlekom, "Quadratic forms, real zeros and echoes of the spectral action," Communications in Mathematical Physics 406 (2025), Article 312. DOI 10.1007/s00220-025-05493-1. arXiv:2511.23257. https://arxiv.org/abs/2511.23257

[^75^] A. Connes, C. Consani, H. Moscovici, "Zeta spectral triples," arXiv:2511.22755v1 (27 Nov 2025); EMS Press CIRM lecture-volume version (2026), DOI 10.4171/elm/37/3. https://arxiv.org/abs/2511.22755 — Unrefereed at sweep date.

[^76^] G. Csordas, R. S. Varga, "Moment inequalities and the Riemann hypothesis," Constructive Approximation 4 (1988), 175–198. DOI 10.1007/BF02075457. MR 932653. http://www.math.kent.edu/~varga/pub/paper_161.pdf

[^77^] G. Csordas, "Fourier transforms of positive definite kernels and the Riemann ξ-function," Computational Methods and Function Theory 15 (2015), no. 3, 373–391 (Open Problem 4.7). DOI 10.1007/s40315-014-0105-8. arXiv:1309.0055. https://arxiv.org/abs/1309.0055

[^78^] G. Csordas, A. Escassut, "The Laguerre inequality and the distribution of zeros of entire functions," Annales Mathématiques Blaise Pascal 12 (2005), no. 2, 331–345. http://www.numdam.org/item/AMBP_2005__12_2_331_0/

[^79^] G. Csordas, T. S. Norfolk, R. S. Varga, "The Riemann hypothesis and the Turán inequalities," Transactions of the American Mathematical Society 296 (1986), no. 2, 521–541.

[^80^] J. B. Conrey, "More than two fifths of the zeros of the Riemann zeta function are on the critical line," Journal für die reine und angewandte Mathematik 399 (1989), 1–26. DOI 10.1515/crll.1989.399.1.

[^81^] K. Pratt, N. Robles, A. Zaharescu, D. Zeindler, "More than five-twelfths of the zeros of ζ are on the critical line," Research in the Mathematical Sciences 7 (2020), Paper No. 2. DOI 10.1007/s40687-019-0199-8. — Proportions 0.417293 (critical) and 0.407511 (simple) verified in-sweep from citing sources; article number carried from the sweep's dimension file, which flags it as to-be-confirmed.

[^82^] A. Weil, "Sur les 'formules explicites' de la théorie des nombres premiers," Commentationes Seminarium Mathematicum Universitatis Lundensis (Meddelanden från Lunds Universitets Matematiska Seminarium), Tome Supplémentaire (1952), 252–265; reprinted in Weil, Œuvres Scientifiques, Vol. II. Compact-support formulation: Yoshida [^70^]; restatements arXiv:2301.00421, arXiv:2602.04022.

[^83^] X.-J. Li, "The positivity of a sequence of numbers and the Riemann hypothesis," Journal of Number Theory 65 (1997), no. 2, 325–333. DOI 10.1006/jnth.1997.2137.

[^84^] E. Bombieri, J. C. Lagarias, "Complements to Li's criterion for the Riemann hypothesis," Journal of Number Theory 77 (1999), no. 2, 274–287. DOI 10.1006/jnth.1999.2392. http://math.lsa.umich.edu/~lagarias/doc/bombieri.ps

[^85^] G. Csordas, W. Smith, R. S. Varga, "Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis," Constructive Approximation 10 (1994), no. 1, 107–129. DOI 10.1007/BF01205170. https://www.math.kent.edu/~varga/pub/paper_206.pdf

[^88^] N. G. de Bruijn, "The roots of trigonometric integrals," Duke Mathematical Journal 17 (1950), 197–226. DOI 10.1215/S0012-7094-50-01720-0.

[^89^] A. Connes, C. Consani, "Weil positivity and trace formula, the archimedean place," Selecta Mathematica (N.S.) 27 (2021), Article 77. DOI 10.1007/s00029-021-00689-4. arXiv:2006.13771. https://arxiv.org/abs/2006.13771

[^90^] W. H. J. Fuchs, "On the eigenvalues of an integral equation arising in the theory of band-limited signals," Journal of Mathematical Analysis and Applications 9 (1964), 317–330.

[^91^] Missing-typed-object record, this sweep (research files double_contact_dim07.md Lead L1; double_contact_dim06.md Lead L1; double_contact_dim08.md Leads L1–L2; open Gaussian-slice inertia question: dim07 Lead L4): certified ball-arithmetic enclosure of (Θ, ∂_ξΘ, ∂²_ξξΘ) with an explicit uniform prime-tail bound — independently requested by three sweep dimensions; not present in the published literature. Internal record, /mnt/agents/output/research/.

[^93^] E. Bombieri, D. A. Hejhal, "On the distribution of zeros of linear combinations of Euler products," Duke Mathematical Journal 80 (1995), no. 3, 821–862. DOI 10.1215/S0012-7094-95-08028-4.

[^94^] A. Connes, C. Consani, "Spectral triples and ζ-cycles," L'Enseignement Mathématique 69 (2023), no. 1–2, 93–148. DOI 10.4171/LEM/1049. arXiv:2106.01715. https://arxiv.org/abs/2106.01715

[^116^] A. Weil, "Sur les 'formules explicites' de la théorie des nombres premiers," Comm. Sém. Math. Univ. Lund (Medd. Lunds Univ. Mat. Sem.), Tome Supplémentaire (1952), 252–265; reprinted in Weil, Œuvres Scientifiques, Vol. II.

[^117^] H. Yoshida, "On Hermitian forms attached to zeta functions," in Zeta Functions in Geometry (Tokyo, 1990), Adv. Stud. Pure Math. 21, Kinokuniya, Tokyo, 1992, 281–325.

[^118^] E. Bombieri, "Remarks on Weil's quadratic functional in the theory of prime numbers, I," Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl. 11 (2000), 183–233. http://eudml.org/doc/252338

[^119^] X.-J. Li, "The positivity of a sequence of numbers and the Riemann hypothesis," J. Number Theory 65 (1997), no. 2, 325–333. DOI 10.1006/jnth.1997.2137.

[^120^] E. Bombieri, J. C. Lagarias, "Complements to Li's criterion for the Riemann hypothesis," J. Number Theory 77 (1999), no. 2, 274–287. DOI 10.1006/jnth.1999.2392. https://doi.org/10.1006/jnth.1999.2392

[^121^] J. C. Lagarias, "On a positivity property of the Riemann ξ-function," Acta Arith. 89 (1999), no. 3, 217–234. DOI 10.4064/aa-89-3-217-234.

[^122^] T. Nakamura, M. Suzuki, "On infinitely divisible distributions related to the Riemann hypothesis," Statist. Probab. Lett. 201 (2023), 109889. arXiv:2306.08317. https://arxiv.org/abs/2306.08317

[^123^] M. Suzuki, "Aspects of the screw function corresponding to the Riemann zeta-function," J. London Math. Soc. (2) 108 (2023), no. 4, 1448–1487. DOI 10.1112/jlms.12796. arXiv:2206.03682. https://arxiv.org/abs/2206.03682

[^124^] M. Suzuki, "Weil's quadratic form via the screw function," arXiv:2606.09096 (2026, preprint; not peer reviewed). https://arxiv.org/abs/2606.09096

[^125^] M. Suzuki, "On the Hilbert space derived from the Weil distribution," arXiv:2301.00421 (2023, preprint). https://arxiv.org/abs/2301.00421

[^126^] M. Balazard, E. Saias, M. Yor, "Notes sur la fonction ζ de Riemann, 2," Adv. Math. 143 (1999), 284–287. DOI 10.1006/aima.1998.1797. English translation (T. Hosgood): https://translations.thosgood.net/AIM-143-1999-284.html

[^127^] L. Báez-Duarte, "A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis," Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl. 14 (2003), no. 1, 5–11. arXiv:math/0202141. (Lineage: B. Nyman, Thesis, Uppsala, 1950; A. Beurling, Proc. Nat. Acad. Sci. U.S.A. 41 (1955), 312–314.)

[^128^] J. Alcantara-Bode, "An integral equation formulation of the Riemann Hypothesis," Integr. Equations Oper. Theory 17 (1993), no. 2, 151–168.

[^129^] J. C. Lagarias, "The Schrödinger operator with Morse potential on the right half line," arXiv:0712.3238 (2007, preprint). https://arxiv.org/abs/0712.3238

[^130^] A. Connes, C. Consani, H. Moscovici, "Zeta spectral triples," arXiv:2511.22755 (2025, preprint). https://arxiv.org/abs/2511.22755

[^131^] L. de Branges, "The Riemann hypothesis for Hilbert spaces of entire functions," Bull. Amer. Math. Soc. (N.S.) 15 (1986), 1–17; and "The convergence of Euler products," J. Funct. Anal. 121 (1994), 117–184.

[^132^] J. B. Conrey, X.-J. Li, "A note on some positivity conditions related to zeta and L-functions," Int. Math. Res. Not. 2000 (2000), no. 18, 929–940. DOI 10.1155/S1073792800000489. arXiv:math/9812166. https://arxiv.org/abs/math/9812166

[^133^] A. Gershon, "The De Bruijn–Newman Constant Is Zero," preprints.org 202604.1513.v1 (22 April 2026). DOI 10.20944/preprints202604.1513.v1. [Not peer reviewed; flagged circular by its own Remark 19.]

[^134^] S. B. Angenent, "The zero set of a solution of a parabolic equation," J. Reine Angew. Math. 390 (1988), 79–96. DOI 10.1515/crll.1988.390.79. (Theorem A restated verbatim in B. Lou, "The Zero Number Diminishing Property under General Boundary Conditions," arXiv:1809.00309.)

[^135^] C. Sturm, "Mémoire sur les équations différentielles linéaires du second ordre," J. Math. Pures Appl. (1) 1 (1836), 106–186; H. Matano, "Nonincrease of the lap-number of a solution for a one-dimensional semilinear parabolic equation," J. Fac. Sci. Univ. Tokyo Sect. IA Math. 29 (1982), no. 2, 401–441.

[^136^] G. Csordas, W. Smith, R. S. Varga, "Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis," Constr. Approx. 10 (1994), no. 1, 107–129. DOI 10.1007/BF01205170. Author PDF: https://www.math.kent.edu/~varga/pub/paper_206.pdf

[^137^] T. Tao, "Heat flow and zeroes of polynomials," What's New, 17 October 2017, https://terrytao.wordpress.com/2017/10/17/heat-flow-and-zeroes-of-polynomials/; and "Heat flow and zeroes of polynomials II: zeroes on a circle," What's New, 7 June 2018, https://terrytao.wordpress.com/2018/06/07/heat-flow-and-zeroes-of-polynomials-ii-zeroes-on-a-circle/

[^138^] D. H. J. Polymath, "Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant," Res. Math. Sci. 6 (2019), no. 3, Paper No. 31, 67 pp. DOI 10.1007/s40687-019-0193-1. arXiv:1904.12438. https://arxiv.org/abs/1904.12438

[^139^] B. Rodgers, T. Tao, "The de Bruijn–Newman constant is non-negative," Forum Math. Pi 8 (2020), e6, 62 pp. DOI 10.1017/fmp.2020.6. arXiv:1801.05914.

[^140^] I. J. Schoenberg, "On Pólya frequency functions," J. Analyse Math. 1 (1951), 331–374.

[^141^] W. Michałowski, "On the Pólya Frequency Order of the de Bruijn–Newman Kernel: Certified Failure at Order Five and the Toeplitz Threshold Phenomenon," arXiv:2602.20313v2 (2026, preprint; v1 February 2026, v2 July 2026; v2 withdrew the unsound derivative-tail certificate, PF₅ counterexample unaffected). https://arxiv.org/abs/2602.20313

[^142^] G. Csordas, T. S. Norfolk, R. S. Varga, "The Riemann hypothesis and the Turán inequalities," Trans. Amer. Math. Soc. 296 (1986), no. 2, 521–541. DOI 10.1090/S0002-9947-1986-0846596-1.

[^143^] G. Csordas, R. S. Varga, "Necessary and sufficient conditions and the Riemann hypothesis," Adv. in Appl. Math. 11 (1990), no. 3, 328–357. DOI 10.1016/0196-8858(90)90014-7.

[^144^] M. Griffin, K. Ono, L. Rolen, D. Zagier, "Jensen polynomials for the Riemann zeta function and other sequences," Proc. Natl. Acad. Sci. USA 116 (2019), no. 23, 11103–11110. DOI 10.1073/pnas.1902572116. arXiv:1902.07321.

[^145^] M. Griffin, K. Ono, L. Rolen, J. Thorner, Z. Tripp, I. Wagner, "Jensen polynomials for the Riemann xi function," Adv. Math. 397 (2022), 108186. DOI 10.1016/j.aim.2021.108186. arXiv:1910.01227.

[^146^] B. Jessen, H. Tornehave, "Mean motions and zeros of almost periodic functions," Acta Math. 77 (1945), 137–279. DOI 10.1007/BF02392225. https://projecteuclid.org/journals/acta-mathematica/volume-77/issue-none/Mean-motions-and-zeros-of-almost-periodic-functions/10.1007/BF02392225.full

[^147^] H. Bohr, "Zur Theorie der fastperiodischen Funktionen III," Acta Math. 47 (1926), 237–281; B. Jessen, "Über die Nullstellen einer analytischen fastperiodischen Funktion," Math. Ann. 108 (1933), 485–516.

[^148^] J. M. Sepúlcre, T. Vidal, "On the real projections of zeros of almost periodic functions," arXiv:1805.02041 (2018, preprint), Theorem 6 and Corollary 10. https://arxiv.org/abs/1805.02041

[^149^] H. L. Montgomery, R. C. Vaughan, "Hilbert's inequality," J. London Math. Soc. (2) 8 (1974), 73–82.

[^150^] H. L. Montgomery, R. C. Vaughan, "The large sieve," Mathematika 20 (1973), 119–134; A. Selberg, "Remarks on sieves," Proc. 1972 Number Theory Conf., Boulder, 1972, 205–216.

[^151^] P. Turán, Eine neue Methode in der Analysis und deren Anwendungen, Akadémiai Kiadó, Budapest, 1953; modern revisit: J. Andersson, "Turán's problem 10 revisited," arXiv:math/0609271.

[^152^] A. Baker, G. Wüstholz, "Logarithmic forms and group varieties," J. Reine Angew. Math. 442 (1993), 19–62; A. Baker, "Linear forms in the logarithms of algebraic numbers IV," Mathematika 15 (1968), 204–216; Matveev-form statement via arXiv:2411.12009 (Cor. 2.3).

[^153^] G. H. Hardy, "A theorem concerning Fourier transforms," J. London Math. Soc. 8 (1933), 227–231.

[^154^] M. Cowling, J. F. Price, "Generalisations of Heisenberg's inequality," Lecture Notes in Math. 992, Springer, 1983, 443–449; L. Hörmander, Math. Scand. 68 (1991), 161–173 (Beurling–Hörmander uncertainty principle).

[^155^] X. Zhu, "Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law," arXiv:2608.24827v2 (2026, preprint; v1 25 Aug 2026, v2 2 Sep 2026 with retraction of the support-2.38 claim). https://arxiv.org/abs/2608.24827 [Authorship metadata inconsistent across sweep records — "M. Chuk" vs "X. Zhu"; see audit note.]

[^156^] W. H. J. Fuchs, "On the eigenvalues of an integral equation arising in the theory of band-limited signals," J. Math. Anal. Appl. 9 (1964), 317–330, Theorem 1.

[^157^] A. Connes, C. Consani, "Spectral triples and ζ-cycles," Enseign. Math. 69 (2023), 93–148. arXiv:2106.01715. (Numerics reported via A. Connes, "The Riemann Hypothesis: Past, Present and a Letter Through Time," arXiv:2602.04022, §6.4.)

[^158^] B. Ya. Levin, Distribution of Zeros of Entire Functions, rev. ed., Transl. Math. Monogr. 5, Amer. Math. Soc., Providence, 1980 (Ch. II; Ch. V §4, Cartwright's theorem).

[^159^] A. Beurling, P. Malliavin, "On the closure of characters and the zeros of entire functions," Acta Math. 118 (1967), 79–93. DOI 10.1007/BF02392478.

[^160^] N. Makarov, A. Poltoratski, "Beurling–Malliavin theory for Toeplitz kernels," Invent. Math. 180 (2010), 443–480. DOI 10.1007/s00222-010-0234-2. arXiv:math/0702497.

[^161^] Yu. I. Lyubarskii, K. Seip, "Complete interpolating sequences for Paley–Wiener spaces and Muckenhoupt's (A_p) condition," Rev. Mat. Iberoamericana 13 (1997), 361–376. DOI 10.4171/RMI/224. arXiv:math/9511212.

[^162^] H. J. Landau, "Necessary density conditions for sampling and interpolation of certain entire functions," Acta Math. 117 (1967), 37–52. DOI 10.1007/BF02395039.

[^163^] B. Dumitrescu, Positive Trigonometric Polynomials and Signal Processing Applications, Springer, 2007; 2nd rev. ed. 2017. DOI 10.1007/978-3-319-53688-0.

[^164^] A. Groskin, "A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form," arXiv:2607.02828 (2026, preprint), Theorems 2.5 and 3.2, Corollary 3.3. https://arxiv.org/abs/2607.02828

[^165^] G. Csordas, "Fourier transforms of positive definite kernels and the Riemann ξ-function," Comput. Methods Funct. Theory 15 (2015), no. 3, 373–391. DOI 10.1007/s40315-014-0105-8. arXiv:1309.0055. (Open Problem 4.7 quoted verbatim.)

[^166^] G. Csordas, A. Escassut, "The Laguerre inequality and the distribution of zeros of entire functions," Ann. Math. Blaise Pascal 12 (2005), no. 2, 331–345. https://www.numdam.org/item/AMBP_2005__12_2_331_0.pdf

[^167^] X.-Y. Chen, "A strong unique continuation theorem for parabolic equations," Math. Ann. 311 (1998), 603–630. DOI 10.1007/s002080050202.

[^168^] J. Cerf, "La stratification naturelle des espaces de fonctions différentiables réelles et le théorème de la pseudo-isotopie," Publ. Math. IHÉS 39 (1970), 5–173, http://www.numdam.org/item/PMIHES_1970__39__5_0/; M. Golubitsky, V. Guillemin, Stable Mappings and Their Singularities, GTM 14, Springer, 1973. DOI 10.1007/978-1-4615-7904-5.

[^169^] D. Platt, T. Trudgian, "The Riemann hypothesis is true up to 3·10¹²," Bull. London Math. Soc. 53 (2021), no. 3, 792–797. DOI 10.1112/blms.12460. arXiv:2004.09765.

[^176^] Session-verified identity E2 (dim08 SF2): Θ(t,ξ) = ½Σ_ρ[e^{−t(ξ−γ_ρ)²} + e^{−t(ξ+γ_ρ)²}], mpmath 50-digit verification with N = 80{,}000 prime powers. /mnt/agents/output/research/double_contact_dim08.md
[^177^] A. Weil, "Sur les 'formules explicites' de la théorie des nombres premiers," Comm. Sém. Math. Univ. Lund, Tome Suppl. (1952), 252–265; H. Yoshida, Adv. Stud. Pure Math. 21 (1992), 281–325; M. Suzuki, J. Lond. Math. Soc. 108 (2023), 1448–1487, DOI 10.1112/jlms.12785, arXiv:2206.03682; X.-J. Li, J. Number Theory 65 (1997), 325–333, DOI 10.1006/jnth.1997.2137.
[^178^] G. Csordas, "Turán-type inequalities and the Riemann hypothesis" (Open Problem 4.7), Constr. Math. Funct. Theory (CMFT) 15 (2015), 373–391. arXiv:1309.0055
[^179^] D. V. Widder, *The Laplace Transform*, Princeton University Press, 1941 (Bernstein's theorem on completely monotone functions); on-axis CM structure identified in /mnt/agents/output/research/double_contact_dim03.md (C13).
[^180^] D. H. J. Polymath, "Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant," Res. Math. Sci. 6 (2019), Art. 31 (Theorem 1.2; Propositions 3.1, 3.3). arXiv:1904.12438
[^181^] G. Csordas, W. Smith, R. S. Varga, "Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis," Constr. Approx. 10 (1994), 107–129, DOI 10.1007/BF01205170; S. B. Angenent, "The zero set of a solution of a parabolic equation," J. reine angew. Math. 390 (1988), 79–96, DOI 10.1515/crll.1988.390.79; M. Golubitsky, V. Guillemin, *Stable Mappings and Their Singularities*, Springer GTM 14, 1973.
[^182^] Insights I0/I3 with the corrected contact identity (independently re-derived by the orchestrator via sympy): /mnt/agents/output/research/double_contact_insight.md; derivative computations in /mnt/agents/output/research/double_contact_dim11.md.
[^183^] J. Gomila, "Λ ≤ 0.1787854 — a new bound for the de Bruijn–Newman constant" (2026), audit repository: https://github.com/judegomila/dbn-lambda-01787854-candidate-audit ; audit in /mnt/agents/output/research/double_contact_dim12.md §2.
[^184^] D. Platt, T. Trudgian, "The Riemann hypothesis is true up to 3·10^12," Bull. Lond. Math. Soc. 53 (2021), 792–797, DOI 10.1112/blms.12460. arXiv:2004.09765
[^185^] A. Groskin, arXiv:2607.02828 (Thm 2.5, Thm 3.2, Cor. 3.3; two-sided certification rule and indecision band [−B_T, 0), B_T ~ (2N+1)ρ log T/(π²T)). https://arxiv.org/abs/2607.02828 — theorem-level Medium; its numerics are not interval-certified and are not cited.
[^186^] F. Johansson, "Arb: efficient arbitrary-precision midpoint-radius interval arithmetic," IEEE Trans. Comput. 66 (2017), no. 8, 1281–1292; digamma–Gaussian convolution tails per /mnt/agents/output/research/double_contact_dim07.md (L1).
[^187^] J. B. Rosser, L. Schoenfeld, "Approximate formulas for some functions of prime numbers," Illinois J. Math. 6 (1962), 64–94; enclosure specification per /mnt/agents/output/research/double_contact_dim07.md (L1).
[^188^] Triple independent demand: dim07 L1 (enclosure), dim06 L1 (form-continuity with four available ingredients), dim08 L1/L2 (certified strip zero-freeness + certified ∂²_ξξΘ > 0). /mnt/agents/output/research/double_contact_dim06.md, dim07.md, dim08.md
[^189^] Cost law per dim07 L1: prime-sum truncation N ~ exp(O(√t·|log ε|)). /mnt/agents/output/research/double_contact_dim07.md

[^201^] F. Johansson, "Arb: efficient arbitrary-precision midpoint-radius interval arithmetic," IEEE Trans. Comput. 66 (2017), no. 8, 1281–1292; mpmath.iv interval arithmetic; enclosure specification per dim07 L1: /mnt/agents/output/research/double_contact_dim07.md
[^202^] J. B. Rosser, L. Schoenfeld, "Approximate formulas for some functions of prime numbers," Illinois J. Math. 6 (1962), 64–94.
[^203^] Corrected contact identity E3 (orchestrator sympy re-verification; insight I0): /mnt/agents/output/research/double_contact_insight.md
[^204^] D. V. Widder, *The Laplace Transform*, Princeton University Press, 1941 (Bernstein's theorem); on-axis CM structure: /mnt/agents/output/research/double_contact_dim03.md (C13); insights I2.
[^205^] D. H. J. Polymath, Res. Math. Sci. 6 (2019), Art. 31 (Prop. 3.1(ii): order-m zeros resolve as √(2(t−t₀))·(Hermite roots)). arXiv:1904.12438; fold theory: M. Golubitsky, V. Guillemin, *Stable Mappings and Their Singularities*, Springer GTM 14, 1973.
[^206^] H. Davenport, H. Heilbronn, "On the zeros of certain Dirichlet series," J. London Math. Soc. 11 (1936), 181–185; negative-control recommendation: /mnt/agents/output/research/double_contact_dim07.md (L3), dim05.md.
[^207^] A. Groskin, arXiv:2607.02828 (Thm 3.2, Cor. 3.3; indecision band [−B_T, 0)). https://arxiv.org/abs/2607.02828 — theorem-level Medium; numerics not interval-certified.
[^208^] X. Zhu, "Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law," arXiv:2608.24827v2 (§10 float64 artifacts). https://arxiv.org/abs/2608.24827 [AUDIT: sound post-retraction; constants Medium]
[^209^] Session-documented quadrature artifact at (t,ξ) = (1.5, 20), retracted on certified re-evaluation: /mnt/agents/output/research/double_contact_dim08.md

[^221^] D. H. J. Polymath, "Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant," Res. Math. Sci. 6 (2019), Art. 31. arXiv:1904.12438
[^222^] W. H. J. Fuchs, "On the eigenvalues of an integral equation arising in connection with band-limited functions" (prolate asymptotics), J. Math. Anal. Appl. 9 (1964), 317–330; qualitative Landau–Widom verdict also supported by Connes–Consani ζ-cycle numerics (2023). See /mnt/agents/output/research/double_contact_dim04.md, dim05.md
[^223^] X. Zhu, arXiv:2608.24827v2 (certified λ*(2) ≤ 3.2×10⁻²⁸³; margin-collapse law). https://arxiv.org/abs/2608.24827 [AUDIT: sound post-retraction; constants Medium]; crossover analysis: /mnt/agents/output/research/double_contact_dim02.md, dim04.md
[^224^] X. Zhu, arXiv:2608.24827v2, Thm 1.4 + Lemma 3.2 (doubly-exponential envelope barrier T₁ = 2πe^{A_L}, A_L = Σ_{log n<2L} 2Λ(n)/√n ~ 4e^L, proved optimal via Weyl equidistribution). https://arxiv.org/abs/2608.24827 [AUDIT: Medium]
[^225^] B. Ja. Levin, *Distribution of Zeros of Entire Functions* (Levin–Cartwright density theory), AMS Translations, 1964/1980; A. Beurling, P. Malliavin, "On the closure of characters and the zeros of entire functions," Acta Math. 118 (1967), 79–93; N. Makarov, A. Poltoratski, "Meromorphic inner functions, Toeplitz kernels and the uncertainty principle," Invent. Math. 180 (2010), 329–370; Yu. Lyubarskii, K. Seip (complete interpolating sequences, complex nodes, 1997). See /mnt/agents/output/research/double_contact_dim10.md
[^226^] A. Groskin, arXiv:2607.02828 (indecision band [−B_T, 0)). https://arxiv.org/abs/2607.02828 [AUDIT: theorem-level Medium]
[^227^] Session-verified identity E2 (dim08 SF2), mpmath 50-digit, N = 80{,}000 prime powers: /mnt/agents/output/research/double_contact_dim08.md
[^228^] A. Weil, Comm. Sém. Math. Univ. Lund, Tome Suppl. (1952), 252–265; H. Yoshida, Adv. Stud. Pure Math. 21 (1992), 281–325; M. Suzuki, J. Lond. Math. Soc. 108 (2023), 1448–1487, DOI 10.1112/jlms.12785; X.-J. Li, J. Number Theory 65 (1997), 325–333, DOI 10.1006/jnth.1997.2137.
[^229^] E. Bombieri, "Remarks on Weil's quadratic functional in the theory of prime numbers, I," Atti Accad. Naz. Lincei (2000), Thm 8 (finitely-many-exceptions inertia); A. Connes, C. Consani, H. Moscovici, arXiv:2511.22755 (Thm 5.10; §8 "missing steps"). https://arxiv.org/abs/2511.22755
[^230^] Insights I2/I3/I6/I10 and acceptance-verdict analysis: /mnt/agents/output/research/double_contact_insight.md; enclosure spec and cost law: /mnt/agents/output/research/double_contact_dim07.md
[^231^] X. Zhu, arXiv:2608.24827v2, Thms 1.1–1.2 (one-stroke finite reduction; certified PSD margin at L = 0.8) [AUDIT: Medium]; A. Groskin, arXiv:2607.02828 (Thm 2.5 dictionary; Cor. 3.3) [AUDIT: theorem-level Medium].
[^232^] W. Michałowski, arXiv:2602.20313v2 (interval-certified PF₅ failure of the de Bruijn–Newman kernel). https://arxiv.org/abs/2602.20313 [AUDIT: sound certified obstruction]; structural blindness analysis: /mnt/agents/output/research/double_contact_dim03.md, dim09.md
[^233^] S. B. Angenent, J. reine angew. Math. 390 (1988), 79–96, DOI 10.1515/crll.1988.390.79; G. Csordas, W. Smith, R. S. Varga, Constr. Approx. 10 (1994), 107–129, DOI 10.1007/BF01205170; almost-periodic counterexample f(x) = (1−cos x) + (1−cos √2 x) (session-verified): /mnt/agents/output/research/double_contact_dim08.md
[^234^] G. Csordas, CMFT 15 (2015), 373–391 (Open Problem 4.7). arXiv:1309.0055
