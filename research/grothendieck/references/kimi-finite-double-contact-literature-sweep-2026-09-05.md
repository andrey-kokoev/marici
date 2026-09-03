# Literature Search: Excluding First Contact in the Shifted-Gaussian Weil Kernel

**Date:** 2026-09-03
**Scope:** Final synthesis of a ten-dimension parallel literature search (`research/weilkernel_dim01.md`–`dim10.md`), corrected per the independent cross-verification report (`research/weilkernel_cross_verification.md`) and organized around the cross-dimension insights I1–I8 (`research/weilkernel_insight.md`). All corrections mandated by the verification pass are applied in this report and override the raw dimension files wherever they conflict.

## Executive summary

The search asked whether the mathematical literature contains results capable of proving, refuting, or materially reducing global positivity of the completed shifted-Gaussian Weil kernel $\Theta(t,\xi) = K_{\mathrm{end}}(t,\xi) + K_{\Gamma}(t,\xi) + K_{\mathrm{pr}}(t,\xi)$, $t>0$, $\xi \in \mathbb{R}$ — specifically, whether **finite double contact** $\Theta(t_*,\xi_*) = \partial_\xi\Theta(t_*,\xi_*) = 0$ and **escape to infinity** (loss of positivity as $|\xi|\to\infty$) can be excluded by known theorems, or whether the obstruction can be reduced to a strictly smaller testable condition, or whether one of the proposed routes is rigorously impossible. **Headline verdict:** the search succeeds on three of the four acceptance criteria. (i) At each *fixed* $t>0$, escape to infinity is excluded by verified unconditional results — Bohr–Kronecker almost-periodicity of the prime cosine sum (with the sharp lim-inf formula corrected by the verifier: the minimum runs over completely multiplicative unimodular characters, not the naive $-\sum a_n$) together with exponential dominance of the pole term $2e^{t/8}\cosh(\xi/2)$. (ii) Finite double contact is excluded *modulo a single structural check*: if $\partial_t\Theta = \partial_{\xi\xi}\Theta$ holds termwise for the completed explicit formula, then Angenent's zero-number Theorem B (1988, with the theorem lettering corrected: the strict zero-number drop at multiple zeros is Theorem B, not Theorem A), Widder's 1944 representation theorem, and Escauriaza–Seregin–Šverák backward uniqueness jointly exclude the contact. (iii) Two proposed routes are rigorously obstructed: the de Bruijn–Newman heat flow does **not** map to $\Theta(t,\xi)$ (the Weil Gaussian is Fourier-dual with the opposite sign, $t' = -1/(4t)$; the only honest correspondence is at the threshold $t'=0$, i.e. RH itself), and exact bandlimited strict-peak interpolation at the zeta ordinates is **unconditionally impossible** (infinite Beurling–Malliavin density by Cartwright–Levin and $N(T)\sim (T/2\pi)\log T$). The genuinely open core — uniformity of positivity as $t \to 0^+$ — is not discharged by any located theorem, but is reduced to four concrete testable conditions T1–T4. No proof route free of circularity was found that establishes global positivity; all RH-equivalent criteria are quarantined in Section 4.

---

## 1. Problem statement

Let
$$
\Theta(t,\xi) \;=\; K_{\mathrm{end}}(t,\xi) \,+\, K_{\Gamma}(t,\xi) \,+\, K_{\mathrm{pr}}(t,\xi), \qquad t>0,\ \xi\in\mathbb{R},
$$
be the completed shifted-Gaussian Weil kernel: the Weil explicit formula evaluated on the Gaussian test function $h(r) = e^{-t(r-\xi)^2}$, written on the arithmetic side as the sum of an archimedean/end term $K_{\mathrm{end}}$ (pole terms $2\operatorname{Re} e^{-t(i/2-\xi)^2} = 2e^{t/4 - t\xi^2}\cos(t\xi)$, equivalently expressed in the $\cosh(\xi/2)$ gauge), the Gamma/digamma kernel $K_{\Gamma}$, and the prime sum $K_{\mathrm{pr}}(t,\xi) = \sum_n a_n(t)\cos(\xi\log n)$ with $a_n(t)\ge 0$, $\sum_n a_n(t) < \infty$. On the zero side, $\Theta(t,\xi) = \sum_\rho m_\rho\, e^{-t(\gamma_\rho - \xi)^2}$, where $\rho = \tfrac12 + i\gamma_\rho$ runs over the non-trivial zeros of $\zeta$ with multiplicity, and $\gamma_\rho$ is possibly non-real with $|\operatorname{Im}\gamma_\rho| = |\operatorname{Re}\rho - \tfrac12| < \tfrac12$.

**Broad smoothing** (heat-semigroup regularization of the Weil distribution) already gives $\Theta(t,\xi) > 0$ for all sufficiently small $t$, uniformly in $\xi$ on compact sets. If a finite positive threshold $t_*$ existed at which positivity first fails, real-analyticity in $\xi$ and the parabolic maximum principle force a **double contact**
$$
\Theta(t_*,\xi_*) = 0, \qquad \partial_\xi\Theta(t_*,\xi_*) = 0,
$$
i.e. a zero of multiplicity $\ge 2$ in the spatial variable at the first contact time. The two unresolved tasks posed to the literature search are therefore:

- **(a) Zero-contact exclusion:** exclude all finite double contacts $(t_*,\xi_*)$;
- **(b) Escape to infinity:** exclude loss of positivity through $|\xi|\to\infty$ as $t$ varies, in particular uniformly as $t\to 0^+$.

The five search questions (Q1–Q5) target, respectively: parabolic zero-number/variation-diminishing machinery for signed initial data; uniform-in-$\xi$ lower bounds for translated Gaussian convolutions of digamma and von Mangoldt sums; arithmetic proofs of Weil positivity for Gaussian tests and promotion to the full admissible test space; Paley–Wiener/de Branges/Beurling–Malliavin interpolation with a strict peak at one zero pair; and Newman/de Bruijn heat-flow, Laguerre–Pólya and Jensen-polynomial equivalences, with the explicit demand to check whether the heat parameter and positivity property actually map to $\Theta(t,\xi)$ rather than merely resemble it.

## 2. Method

**Design.** Ten search dimensions were executed in parallel, each assigned a distinct source class and question cluster:

| Dim | Focus | Feeds |
|---|---|---|
| 01 | Parabolic zero-number theory; total positivity; bell-shaped kernels | Q1 |
| 02 | Variation-diminishing convolution, Pólya frequency functions, sign changes | Q1 |
| 03 | Strong maximum principle, Widder-type theorems, backward uniqueness, almost-periodic heat flows | Q1 |
| 04 | Uniform archimedean bounds; explicit coercive lower bounds for Weil sums | Q2 |
| 05 | Almost-periodic cosine sums, Bohr/Kronecker, universality methods | Q2 |
| 06 | Weil positivity literature (Weil, Bombieri, Li, Yoshida, Suzuki, Connes–Consani) | Q3 |
| 07 | de Branges/Sonine spaces, screw functions, Hilbert-space completions of the Weil distribution | Q3 |
| 08 | Bandlimited interpolation, extremal problems, Gaussian subordination | Q4 |
| 09 | Beurling–Malliavin density, completeness, interpolation with derivatives, Jensen/Laguerre–Pólya | Q4 |
| 10 | de Bruijn–Newman constant, heat flow, Pólya–Jensen, Laguerre–Pólya class | Q5 |

**Source classes.** Journal papers (Crossref/Project Euclid/EuDML/Göttingen GDZ scans), books and published proceedings, and arXiv preprints with traceable metadata. Numerical positivity, finitely many verified zeros, and finite parameter scans were excluded as global theorems per the brief's exclusion rules.

**Schema.** Every potentially useful result was recorded with a nine-field schema: (1) full citation + DOI/arXiv + stable link; (2) exact theorem number and transcribed hypotheses; (3) typed objects and parameter conventions; (4) proposed map to $\Theta(t,\xi)$; (5) which missing step it would discharge; (6) every unmet hypothesis; (7) RH-equivalence / zero-location-assumption check; (8) classification (`applicable` / `conditionally applicable` / `inapplicable` / `circular`); (9) cheapest concrete test to settle conditional applicability.

**Verification pass.** An independent adversarial pass (Crossref, arXiv API, GDZ OCR of the original Crelle scans, Numdam/AIF PDFs, direct computation) checked the load-bearing items. Outcome: one mathematical claim **REFUTED** (dim05's sharp lim-inf identity; corrected statement in §3.2); one attribution **MISMATCH** (arXiv:2405.04869 is Nicol Leong solo; HLY = arXiv:2306.13289); corrected DOIs (Widder 10.1090/S0002-9947-1944-0009795-2; Bohr 10.1007/BF01457178); corrected journal data (Lou: Appl. Math. Lett. **95** (2019), 41–47, DOI 10.1016/j.aml.2019.03.016); theorem-numbering correction (Angenent: discreteness = Theorem A; strict zero-number drop = Theorem B; the (a)–(d) composite is Lou's restatement); transcription error fixed (Lagarias's $C_1(\pi)$ needs the factor $N/2$); convention trap confirmed (Ki–Kim–Lee $\Lambda = 4\lambda^{(0)}$). This synthesis additionally resolved, via doi.org/Crossref/arXiv checks: Csordas–Smith–Varga DOI 10.1007/BF01205170; Bombieri 2003 DOI 10.1002/cpa.10089; Gonçalves DOI 10.1090/tran6672 (Trans. AMS 369 (2017), no. 2); Suzuki Canad. J. Math. DOI 10.4153/S0008414X25101739; Burnol JTNB pages 65–94; Polymath15 arXiv:1904.12438; Kwaśnicki pages 2255–2280. All other load-bearing items were verified.


---

## 3. Results by search question

### 3.1 Q1 — Zero-contact exclusion (Dimensions 01–03)

#### (a) Narrative assessment

The double-contact condition $\Theta(t_*,\xi_*) = \partial_\xi\Theta(t_*,\xi_*) = 0$ is, verbatim, a **multiple zero** of the spatial slice of a 1D parabolic solution, and the classical Sturmian/parabolic literature addresses exactly this object. Three independent, mutually reinforcing, verified toolkits were located:

1. **Widder's representation theorem** (1944) [^1^]: a nonnegative classical solution of the heat equation on a strip $\mathbb{R}\times(0,c)$ is a Poisson–Gauss–Stieltjes integral of a positive measure, hence **strictly positive everywhere unless identically zero**. If $\Theta \ge 0$ on $(0,t_*]\times\mathbb{R}$ (which holds by definition of a first-violation time $t_*$, by continuity), then $\Theta(t_*,\xi) > 0$ for every finite $\xi$ — no zero at all, double or otherwise. This discharges task (a) and the finite-$\xi$ part of task (b) in one stroke, subject to one structural check (below).
2. **Angenent's zero-number theory** (1988) [^2^] — with the verifier's numbering correction: **Theorem A** is discreteness of the zero set; **Theorem B** is the strict drop of the zero number $Z(t)$ across any time at which a multiple zero exists; the frequently-quoted composite "(a)–(d)" statement is Lou's 2019 restatement [^3^]. Theorem B implies that a double contact at the *first* violation time is impossible: positivity for $t<t_*$ gives $Z(t)=0$ on every window, while a multiple zero at $t_*$ forces $Z(t_1) > Z(t_2)$ for $t_1<t_*<t_2$, a contradiction. Zero-number theory does **not** exclude double contacts in general — it *predicts* them as the unique mechanism by which the zero count changes — but it kills the first-violation scenario.
3. **Backward uniqueness** (Lions–Malgrange [^4^]; Escauriaza–Seregin–Šverák [^5^][^6^]; Dardé–Ervedoza for distributional data [^7^]) kills the residual case $\Theta(t_*,\cdot)\equiv 0$.

The **single structural hypothesis** on which every one of these tools rests is that $\Theta(t,\xi)$ is a classical solution of an exact uniformly parabolic equation — concretely $\partial_t\Theta = c\,\partial_{\xi\xi}\Theta$ up to a smooth strictly increasing reparametrization of $t$ — with Tychonoff-class growth $|\Theta(t,\xi)| \le A(t)e^{B(t)\xi^2}$. The prime-sum side satisfies the heat equation termwise for $t>0$ (each $e^{-t\gamma^2}\cos(\gamma\xi)$ does); the completed $K_{\mathrm{end}} + K_\Gamma$ terms must be checked from the exact definition used. No located hypothesis is RH-equivalent or assumes zero locations: this route is **non-circular**. Caveat: Angenent's theorem is stated on bounded intervals, so its use on $\mathbb{R}$ entangles (a) with (b) via boundary control on windows $[-L,L]$ (generic $L$ exists by analyticity of $t\mapsto\Theta(t,\pm L)$).

Two further findings frame the limits of this approach. The **Karlin oscillation theorem** [^8^][^9^] would exclude double zeros for *all* $t$ at once, but its key hypothesis — one-signedness of the unsmoothed Weil data $\Theta(0^+,\cdot)$ — is very likely RH-equivalent, so that route is quarantined (Section 4). Conversely, **de Bruijn's 1950 theorem** [^10^] explains *why* zero counting alone cannot exclude double contacts: under Gaussian smoothing, real zeros of trigonometric integrals are created and annihilated pairwise through double zeros — double contacts are the generic mechanism, not a pathology.

#### (b) Top theorems (9-field schema)

**T-Q1.1 Widder 1944 — representation of positive temperatures.**
1. *Citation.* D. V. Widder, "Positive temperatures on an infinite rod", *Trans. Amer. Math. Soc.* **55** (1944), no. 1, 85–95. DOI 10.1090/S0002-9947-1944-0009795-2 (corrected per verifier; dim01's 0009704-9 is wrong). JSTOR 1990141. Book form: *The Heat Equation*, Academic Press, 1975, Ch. VIII [^1^][^11^].
2. *Theorem (main representation theorem, faithfully transcribed).* "$u(x,t)$, of class $C^2$ on $-\infty<x<\infty$, $0<t<c$, satisfies $\partial_x^2 u = \partial_t u$ and $u(x,t)\ge 0$ there if and only if $u(x,t) = \int_{-\infty}^{\infty} k(x-y,t)\,d\alpha(y)$, $k(x,t) = (4\pi t)^{-1/2}e^{-x^2/4t}$, with $\alpha$ non-decreasing and the integral absolutely convergent on $0<t<c$." Corollary (strict positivity): $k>0$ everywhere, so $u>0$ unless $\alpha$ is constant ($u\equiv 0$); also uniqueness for nonnegative solutions with no growth restriction.
3. *Typed objects.* Real classical $C^2$ solutions; $\alpha$ a non-decreasing function (positive Stieltjes measure); no Tychonoff growth hypothesis needed — that is the point of the theorem.
4. *Map to $\Theta$.* $u(t,x) \leftrightarrow \Theta(t,\xi)$ verbatim (diffusivity/variance conventions differ by an affine rescaling of $t$ only). On the strip $(0,t_*]\times\mathbb{R}$ with $\Theta\ge 0$, $\Theta\not\equiv 0$: $\Theta(t_*,\xi) = \int k(\xi-y,t_*)\,d\alpha(y) > 0$ for all $\xi$.
5. *Step discharged.* Double-contact exclusion (a), forward direction, and the finite-$\xi$ part of escape-to-infinity (b): a first violation at finite $\xi_*$ contradicts the representation.
6. *Unmet hypotheses.* (i) Exact heat equation $\partial_t\Theta = c\,\partial_{\xi\xi}\Theta$ for the *completed* kernel, including $K_{\mathrm{end}} + K_\Gamma$; (ii) nonnegativity on the strip up to $t_*$ (the definition of first violation); (iii) $\Theta\not\equiv 0$.
7. *Circularity.* None: pure PDE, no $\zeta$-zero input. Caveat: "$\Theta\ge 0$ for all $t$" is RH-equivalent globally, so Widder is a closure lemma, not a proof of RH.
8. *Classification.* `conditionally applicable` — the strongest single tool located; the only condition is the standing heat-equation check.
9. *Cheapest test.* Compute $\partial_t\Theta - \partial_{\xi\xi}\Theta$ termwise from the completed explicit formula (symbolically $0$ on the prime side; check the archimedean terms); then Widder applies verbatim.

**T-Q1.2 Angenent 1988 — zero-number theory (Theorems A and B).**
1. *Citation.* S. B. Angenent, "The zero set of a solution of a parabolic equation", *J. Reine Angew. Math.* **390** (1988), 79–96. DOI 10.1515/crll.1988.390.79. EuDML doc 153060; MR953678 [^2^].
2. *Theorem (verbatim from the GDZ OCR of the original, pp. 79–80, per verifier).* **Theorem A.** "For each $t\in(0,T)$ the zero set $Z(t) = \{x\in M : u(x,t)=0\}$ is a discrete subset of $M$." **Theorem B.** "If at $(x_0,t_0)$ both $u$ and $u_x$ vanish, then … $u(\cdot,t+\delta)$ has at most one zero … $u(\cdot,t-\delta)$ has at least two zeroes." (Equation $u_t = a(x,t)u_{xx} + b(x,t)u_x + c(x,t)u$ with $a>0$, coefficients bounded with the stated regularity; bounded interval with separated boundary conditions. Non-increase of $Z(t)$ follows by the Matano/Nickel comparison argument [^12^][^13^].)
3. *Typed objects.* Scalar classical solutions of linear 1D parabolic equations on bounded intervals; zeros counted without multiplicity; multiple zero $=$ simultaneous vanishing of $u$ and $u_x$.
4. *Map to $\Theta$.* $u(t,x) = \Theta(t,\xi)$ on windows $I = [-L,L]$; the double-contact hypothesis is verbatim Angenent's multiple zero. First violation at $t_*$ with $\Theta>0$ for $t<t_*$ gives $Z_I(t)=0$ for $t<t_*$; Theorem B forces a strict drop across $t_*$, i.e. zeros before $t_*$ — contradiction.
5. *Step discharged.* Task (a) in the strongest local form; also the mechanism statement: any change of the zero count passes through exactly the double contact.
6. *Unmet hypotheses.* (i) Standing heat-equation check; (ii) bounded-interval formulation — boundary signs $\Theta(t,\pm L)\neq 0$ near $t_*$, arranged by generic choice of $L$ via analyticity of $t\mapsto\Theta(t,\pm L)$; whole-line use would require excluding zero influx from $\xi=\pm\infty$, which is precisely task (b); (iii) $\Theta(t_*,\cdot)\not\equiv 0$ (residual case handled by backward uniqueness, T-Q1.4).
7. *Circularity.* None whatsoever — hypotheses concern coefficients and boundary behavior only.
8. *Classification.* `conditionally applicable` (only the heat-equation structure needs confirmation; bounded-window version suffices).
9. *Cheapest test.* Verify $\partial_t\Theta = c\,\partial_{\xi\xi}\Theta$ and $|\Theta(t,\xi)|\le A(t)e^{B(t)\xi^2}$ from the explicit formula; numerically confirm $\Theta(t,\pm L)\neq 0$ near a candidate $t_*$ for one large $L$.

**T-Q1.3 Lou 2019 — zero-number diminishing under general boundary conditions.**
1. *Citation.* B. Lou, "The zero number diminishing property under general boundary conditions", *Appl. Math. Lett.* **95** (2019), 41–47. DOI 10.1016/j.aml.2019.03.016 (journal data corrected per verifier; dim03's "97 (2019) 78–83" is wrong). arXiv:1809.00309 [^3^].
2. *Theorem.* Theorem 1.1: for bounded classical solutions of $u_t = a u_{xx} + b u_x + c u$ on $(0,1)\times(0,T)$, $a>0$, $b,c$ bounded, under general separated Robin conditions $u_x(i,t) = \beta_i(t)u(i,t)$, $\beta_i\in L^\infty_{\mathrm{loc}}$, the zero number is finite for $t>0$, nonincreasing, and strictly decreases through any time with a multiple zero. Theorem 1.2 extends (a)–(c) to *moving* intervals $(\xi_1(t),\xi_2(t))$ with zero/nonzero Dirichlet or isolated-boundary-zero patterns. Lou's (a)–(d) composite is the standard modern restatement of Angenent's Theorems A+B (the "(a)–(d) Theorem A" label in the raw dimension files is Lou's restatement, not Angenent's numbering).
3. *Typed objects.* As T-Q1.2 plus Robin/moving-boundary data.
4. *Map to $\Theta$.* On $[-L,L]$ impose induced Robin data $\beta_\pm(t) = \partial_\xi\Theta(t,\pm L)/\Theta(t,\pm L)$ wherever nonzero; the moving-interval version rigorizes the maximal positivity region around $\xi_*$ when zeros approach from the sides.
5. *Step discharged.* Technical closure of T-Q1.2's boundary conditions on windows and on the maximal positivity interval $(\xi_1(t),\xi_2(t))$.
6. *Unmet hypotheses.* $\beta_i\in L^\infty_{\mathrm{loc}}$ fails at boundary-zero times — handled by generic $L$; $C^1$ zero curves, OK by the implicit function theorem away from multiple zeros.
7. *Circularity.* None.
8. *Classification.* `conditionally applicable` (same single condition).
9. *Cheapest test.* As T-Q1.2.

**T-Q1.4 Backward uniqueness: Lions–Malgrange 1960; Escauriaza–Seregin–Šverák 2003; Dardé–Ervedoza 2019.**
1. *Citations.* J.-L. Lions, B. Malgrange, "Sur l'unicité rétrograde dans les problèmes mixtes paraboliques", *Math. Scand.* **8** (1960), 277–286 [^4^]. L. Escauriaza, G. Seregin, V. Šverák, "Backward uniqueness for parabolic equations", *Arch. Ration. Mech. Anal.* **169** (2003), 147–157, DOI 10.1007/s00205-003-0263-8 [^5^]; and "Backward uniqueness for the heat operator in a half-space", *Algebra i Analiz* **15** (2003), 201–214 = *St. Petersburg Math. J.* **15** (2004), 139–148 [^6^]. J. Dardé, S. Ervedoza, "Backward uniqueness results for some parabolic equations in an infinite rod", *Math. Control Relat. Fields* **9** (2019), 673–696, DOI 10.3934/mcrf.2019046 [^7^].
2. *Theorem (ESS 2003, faithfully).* If $|\partial_t u + \Delta u| \le c(|\nabla u| + |u|)$ in $(\mathbb{R}^n\setminus B_R)\times(0,1)$, $|u(x,t)|\le M e^{M|x|^2}$, and $u(x,1)=0$, then $u\equiv 0$ — backward uniqueness in exterior domains with no boundary condition on the sphere; the half-space version needs no boundary control at all. Dardé–Ervedoza prove BU on the half-line for tempered-distribution initial data with Fourier growth $|\mathcal{F}(y_0)(\xi)|\le M e^{M|\xi|^\rho}$, $\rho<2$ — the best match to $\Theta$'s regularity level.
3. *Typed objects.* Perturbed backward heat inequalities in exterior/half-space domains; $e^{M|x|^2}$ growth class.
4. *Map to $\Theta$.* $u(s,\xi) = \Theta(t_*-s,\xi)$ run backward: $\Theta(t_*,\cdot)\equiv 0$ on a ray $\{\xi>R\}$ (or globally) implies $\Theta\equiv 0$ for earlier times — contradiction with $\Theta>0$ for $t<t_*$.
5. *Step discharged.* Residual case of T-Q1.1/T-Q1.2 ($\Theta(t_*,\cdot)\equiv 0$, or simultaneous vanishing on a whole ray — an extreme escape-to-infinity scenario).
6. *Unmet hypotheses.* The growth bound $|\Theta(t,\xi)|\le M(t)e^{M(t)\xi^2}$ from the explicit formula (prime sum fine; archimedean terms to be checked); Sobolev membership for the Lions–Malgrange form may require renormalization by $e^{-a\xi^2}$.
7. *Circularity.* None.
8. *Classification.* `conditionally applicable`.
9. *Cheapest test.* Establish the $e^{M\xi^2}$ bound for the completed kernel on compact $t$-intervals; or check $e^{-a\xi^2}\Theta\in L^2_t H^2_\xi$.

**T-Q1.5 Schoenberg 1950 (PF II) / Karlin 1968 — variation-diminishing Gaussian convolution.**
1. *Citations.* I. J. Schoenberg, "On Pólya frequency functions. II. Variation-diminishing integral operators of the convolution type", *Acta Sci. Math. (Szeged)* **12** (1950), 97–106 (résumé: *Proc. Natl. Acad. Sci. USA* **34** (1948), 164–169, DOI 10.1073/pnas.34.4.164) [^14^]; classification theorem: "On Pólya frequency functions. I", *J. Analyse Math.* **1** (1951), 331–374, DOI 10.1007/BF02790092 [^15^]. S. Karlin, *Total Positivity, Vol. I*, Stanford Univ. Press, 1968, Ch. 5, Thm 3.1 and oscillation theorem [^8^]; S. Karlin, Z. Ziegler, "Chebyshevian spline functions", *SIAM J. Numer. Anal.* **3** (1966), 514–543, DOI 10.1137/0703043 [^9^]. Modern restatement (verifier-confirmed): M. Kwaśnicki, "A new class of bell-shaped functions", *Trans. Amer. Math. Soc.* **373** (2020), 2255–2280 (pages corrected per verifier; dim01's 3245–3282 wrong), DOI 10.1090/tran/7825, arXiv:1710.11023, Thm 4.3 (Schoenberg): "An integrable function is a variation diminishing convolution kernel if and only if it is a Pólya frequency function, up to multiplication by a constant" [^16^]. Strict-positivity companion: Schoenberg–Whitney, *Trans. Amer. Math. Soc.* **74** (1953), 246–259, DOI 10.1090/S0002-9947-1953-0055298-4 [^17^].
2. *Theorem (transcribed).* Schoenberg II, Thm 1: for $\Lambda\in L^1(\mathbb{R})$, $\Lambda\not\equiv 0$, convolution $f\mapsto \Lambda*f$ satisfies $S^-(\Lambda*f)\le S^-(f)$ for all bounded measurable $f$ **iff** $\Lambda$ is a Pólya frequency function (up to sign). Karlin Ch. 5 Thm 3.1(ii): for strictly sign-regular kernels, $S^+(Tf)\le S^-(f)$. Karlin's oscillation theorem (ETP form): for a strictly totally positive differentiable kernel $p$ and input $\xi$ with $S(\xi)=n$ sign changes, $\Xi(x) = \int \xi(y)p(x,y)\,d\mu(y)$ has zero count with multiplicity $N(\Xi)\le n$ or $\Xi\equiv 0$. The Gaussian is PF$_\infty$/STP/ETP$_\infty$ unconditionally.
3. *Typed objects.* Sign-change counts $S^-, S^+$ (Karlin conventions); PF functions; zeros counted with multiplicity in the oscillation theorem.
4. *Map to $\Theta$.* $\Lambda = g_t$ (Gaussian), $f = \Theta(0^+,\cdot)$: $S^-(\Theta(t,\cdot))\le S^-(\Theta(0^+,\cdot))$ on the whole line, no windowing needed. Oscillation theorem: if $S^-(\Theta(0^+,\cdot))=0$ then $N(\Theta(t,\cdot))=0$ — no zero of any multiplicity, double contacts excluded for all $t$ at once.
5. *Step discharged.* Sign-change control (applicable); the strong form would discharge (a) completely — but see 7.
6. *Unmet hypotheses.* $\Theta(0^+,\cdot)$ must exist as a signed measure/function with finite $S^-$; the strong form needs $S^-(\Theta(0^+,\cdot))=0$, i.e. pointwise one-signedness of the unsmoothed Weil data; $S^-$ counts sign changes, so a tangency zero of a nonnegative function is invisible ($S^+=0$) — the VDP alone is blind to double contacts.
7. *Circularity.* The unconditional weak form: none. The strong form's hypothesis (pointwise positivity of unsmoothed Weil data) is plausibly RH-equivalent — **high circularity risk**; quarantined in Section 4.
8. *Classification.* Weak form: `applicable` (qualitatively, once $S^-(\Theta(0^+,\cdot))$ is known). Strong (oscillation) form: `conditionally applicable` with high circularity risk.
9. *Cheapest test.* Estimate $S^-$ of the truncated explicit-formula data numerically and check stability under truncation; if the continuous parts are not one-signed, the strong application is dead.

#### (c) Documented near-misses (Q1)

| Near-miss | Reason it fails |
|---|---|
| Strong maximum principle for signed data (Nirenberg [^18^]; Friedman [^19^]) | Propagates an attained extremum only when the sign is already known; vacuous for sign-changing data; never creates positivity. PDE-side closure lemma strictly weaker than Widder (T-Q1.1). |
| Parabolic Harnack inequalities (Moser [^20^]; Li–Yau [^21^]) | Require $u\ge 0$ (resp. $u>0$ for $\log u$) throughout — logically circular as positivity proofs; constants degrade with cylinder size, so no uniform-in-$\xi$ bound. |
| Aronson Gaussian bounds / nonnegative-solution representation [^22^][^23^] | Exhausts nonnegative solutions by Poisson integrals (Widder in $n$ dimensions); as a proof device it presumes $\Theta\ge 0$ — structure theorem only. |
| Nash 1958 Hölder regularity | Regularity tool; no sign information. |
| Nodal-set measure estimates (Lin 1991 [^24^]; Han–Lin 1994 [^25^]; Huang–Jiang 2024, arXiv:2406.05877) | The critical set $\{u=\nabla u=0\}$ is measure-small but not empty — does not exclude a double contact. |
| Vertical-line rigidity (Lees–Protter [^26^]; ESS §4 [^5^]) | Needs a double contact *persisting at fixed $\xi_*$ over a time interval*; the problem's contact is instantaneous with moving $\xi_*$. |
| Almost-periodic heat semigroups (Giga–Inui–Mahalov–Matsui [^27^]; Cannone–Karch [^28^]) | $\Theta$ is not demonstrably Bohr-almost-periodic in $\xi$ (Gaussian envelope breaks recurrence); a.p. theory does not exclude $\inf=0$ without attained zero. |
| Scale-space fingerprint theorems (Yuille–Poggio [^29^]; Babaud et al., IEEE TPAMI 8 (1986), 26–33) | Correct line-version of "no interior zero creation", strictly weaker than Angenent; engineering-level hypotheses; in dimension $\ge 2$ zero creation occurs — a warning against overgeneralization. |
| Matano lap-number [^12^]; Nickel [^13^]; Sturm 1836 via Bérard–Helffer [^30^][^31^] | Historical/priority core of T-Q1.2; bounded intervals, Neumann/periodic data; subsumed by Angenent. |
| Ancient-solution rigidity (Lin–Zhang 2019 [^32^]) | Requires an ancient ($t<0$) extension of $\Theta$, which the Gaussian Weil test does not admit. |
| Karlin oscillation theorem, strong form [^8^][^9^] | Would exclude double zeros for all $t$, but the hypothesis $S^-(\Theta(0^+,\cdot))=0$ is plausibly RH-equivalent — circular; quarantined. |
| Pólya-frequency route for $\Theta(t,\cdot)$ itself [^15^][^16^] | PF would give strict positivity outright, but the natural $\zeta$-kernel fails PF at order 5 (certified, arXiv:2602.20313 [^33^]); verifying PF$_\infty$ is harder than positivity. Route blocked. |
| Gröchenig–Romero–Stöckler 2018 (Invent. Math. 211, 1119–1148); Weinberger PF$_3$; Karlin–Proschan 1960; Gantmacher–Krein | No theorem on zeros/positivity of the convolved function; order-3 TP too weak; no zero control; bounded-interval eigenfunction theory — none applies. |
| Chen 1998 strong unique continuation [^34^] | Infinite-order (flat) contacts excluded outright unless $\Theta\equiv 0$ (`applicable` for that); a mere double contact is order 2, so SUCP does not exclude it. |
| de Bruijn 1950 mechanism [^10^][^35^][^36^] | Unconditional strip law $|\operatorname{Im}z|^2 \le \max(\Delta^2-2\lambda,0)$: real zeros of Gaussian-smoothed cosine transforms annihilate *pairwise through double zeros* — double contacts are the generic mechanism, so zero counting alone cannot exclude them (negative result for Q1). |
| Turán / Laguerre–Pólya hierarchies tied to $\zeta$-coefficients [^37^][^38^][^39^][^40^][^41^][^42^] | Every full-hierarchy statement is RH-equivalent — circular; quarantined (Section 4). |

**Bottom line (Q1).** Double contact at finite $\xi_*$ is excluded modulo the single structural check $\partial_t\Theta = c\,\partial_{\xi\xi}\Theta$ plus Tychonoff-class growth, via Widder (T-Q1.1) or Angenent (T-Q1.2) + backward uniqueness (T-Q1.4). No located theorem is circular on this route. What the literature does *not* give: exclusion of escape-to-infinity by parabolic tools (zero-number theory is a bounded-window counting theory), and any unconditional statement about the $t\to 0^+$ uniform regime.

### 3.2 Q2 — Escape to infinity (Dimensions 04–05)

#### (a) Narrative assessment

The escape-to-infinity question splits into two regimes with sharply different literature coverage.

**Fixed $t>0$: settled, unconditionally.** The prime part $K_{\mathrm{pr}}(t,\xi) = \sum_{n\ge 2} a_n(t)\cos(\xi\log n)$, $a_n(t)\ge 0$, $\sum_n a_n(t) < \infty$, is a Bohr (uniformly) almost-periodic function of $\xi$. Kronecker's simultaneous approximation theorem (the frequencies $\{\log p\}$ over primes are $\mathbb{Q}$-linearly independent by unique factorization) plus Bohr's theory give complete control of its infimum. **The verifier refuted the raw dim05 sharp identity** $\inf = \liminf = -\sum_n a_n(t)$: because $\{\log n\}$ over *all* $n$ are not $\mathbb{Q}$-linearly independent ($\log 4 = 2\log 2$), the closure of $\xi \mapsto (n^{-i\xi})$ on the Bohr compactification is the set of *completely multiplicative* unimodular characters, and $\chi(p) = -1$ forces $\chi(n) = (-1)^{\Omega(n)}$, not $-1$ (counterexample: $\min_\xi[\cos(\xi\log 2) + \cos(\xi\log 4)] = -9/8 \neq -2$). The corrected sharp statement is
$$
\inf_\xi K_{\mathrm{pr}}(t,\xi) \;=\; \min_{\substack{\chi\ \text{completely multiplicative}\\ |\chi|=1}} \sum_n a_n(t)\,\operatorname{Re}\chi(n),
$$
which factors over primes as $\sum_p \min_{|z|=1}\sum_m a_{p^m}(t)\operatorname{Re}(z^m)$ and is **strictly** $> -\sum_n a_n$ whenever coefficients occur at even prime powers (as the $\Lambda$-weighted $K_{\mathrm{pr}}$ always has). The qualitative conclusion survives intact: $K_{\mathrm{pr}}(t,\cdot)$ takes negative values on relatively dense sets of $\xi$ ($\liminf \le \sum_n a_n(t)(-1)^{\Omega(n)} < 0$), its $\liminf$ is a finite explicit computable quantity, and there is no silent escape at infinity for the prime part. Meanwhile the pole term in $K_{\mathrm{end}}$, $2e^{t/8}\cosh(\xi/2)$, grows like $e^{|\xi|/2}$ and dominates the bounded oscillation: **at fixed $t$, positivity cannot be lost through $|\xi|\to\infty$**, and the task reduces to the one-variable comparison between $K_{\mathrm{end}}(t)+K_\Gamma(t)$ and the corrected $\liminf$ of the prime sum.

**Uniformity as $t\to 0^+$: open, and provably the hard core.** As $t\downarrow 0$, the $\ell^1$ content $A(t) = \sum_n a_n(t) \uparrow \infty$ (of order $\sqrt{2\pi/t}\,e^{1/(8t)}$-type, dominated by primes near $e^{1/(2t)}$), while the pole term grows like $\sqrt{2\pi/t}\,e^{1/(2t)}$; the comparison is not discharged by any located theorem. Two verified *obstructions* mark the boundary of what is provable: **Turán's criterion** — uniform-in-$\xi$ cancellation bounds for $\sum \Lambda(n) n^{i\xi}$ stronger than Korobov–Vinogradov strength imply new zero-free regions, i.e. are RH-strength — and **Wintner's theorem** that the zeros-side trigonometric series is B²-almost-periodic *if and only if* RH. Both are quarantined as circular (Section 4). Useful unconditional infrastructure exists: explicit uniform-in-$\xi$ bounds for $-\zeta'/\zeta$ on and near the 1-line (Trudgian; Cully-Hugill–Leong; Leong), Landau–Gonek-type explicit identities with Gaussian log-weights, and explicit zero-density estimates — these make the *smoothed* prime sum tame but provably cannot close the full criterion (zero-density bounds are strictly weaker than RH).

**Archimedean side: well understood.** Lagarias's Theorem 5.1 gives the unconditional coercive growth of the archimedean (digamma) contribution in the Li normalization, $S_\infty(n,\pi) = \frac{N}{2}n\log n + C_1(\pi)n + O(N(K(\pi)+1))$ with $C_1(\pi) = \frac{N}{2}(\gamma - 1 - \log 2\pi) + \frac12\log Q(\pi)$ (the $N/2$ factor restored per verifier; raw dim04 dropped it); Bombieri's Theorem 12 gives an explicit coercive lower bound $\big(\log(1/|I|) - \log^+\log(1/|I|) - O(1)\big)\|F\|^2$ for narrow-support tests; Connes–Consani give an unconditional positivity lower bound with explicit defect constant $c = 4\gamma/\log 2$ for the archimedean Weil distribution on convolution squares supported in $[2^{-1/2},2^{1/2}]$. All quadratic-form results in this area are structurally **$\xi$-blind** (translation multiplies $\hat g$ by $e^{i\xi\cdot}$ and leaves $|\hat g|^2$ invariant) — they support the coercivity half of the comparison but cannot see the pointwise-in-$\xi$ question directly (insight I4).

#### (b) Top theorems (9-field schema)

**T-Q2.1 Kronecker 1884 / Bohr 1918 — sharp infimum of absolutely convergent prime cosine sums (corrected).**
1. *Citation.* Kronecker's simultaneous approximation theorem, standard source: T. M. Apostol, *Modular Functions and Dirichlet Series in Number Theory*, 2nd ed., GTM 41, Springer, 1990, Thm 7.11, DOI 10.1007/978-1-4612-0999-7 [^43^]. H. Bohr, "Zur Theorie der allgemeinen Dirichletschen Reihen", *Math. Ann.* **79** (1918), 136–156, DOI 10.1007/BF01457178 (corrected per verifier; dim05's BF01457180 resolves to a different article) [^44^]; H. Bohr, *Almost Periodic Functions*, Chelsea, 1947 [^45^]; modern restatement: A. Defant, I. Schoolmann, "On Bohr's theorem for general Dirichlet series", *Math. Nachr.* **293** (2020), 1591–1612, arXiv:1812.04925 [^46^].
2. *Theorem (corrected sharp form; the raw dim05 identity was REFUTED by the verifier).* (i) Kronecker: $\mathbb{Q}$-linearly independent $\theta_1,\dots,\theta_N$ give density of $\{t(\theta_1,\dots,\theta_N)\}$ in $\mathbb{T}^N$; $\{\log p\}$ are $\mathbb{Q}$-linearly independent. (ii) Bohr: uniform limits of generalized trigonometric polynomials are uniformly almost periodic; for UAP $f$, $\inf$ over any half-line equals $\inf$ over $\mathbb{R}$, approached on relatively dense sets. (iii) For $c_n\ge 0$, $\sum c_n < \infty$, $f(\xi) = \sum_n c_n\cos(\xi\log n)$: $\inf_\xi f(\xi) = \min_{\chi} \sum_n c_n\operatorname{Re}\chi(n)$ over **completely multiplicative unimodular** $\chi$ ($= \sum_p \min_{|z|=1}\sum_m c_{p^m}\operatorname{Re}(z^m)$ for prime-power-supported coefficients), in general strictly $> -\sum_n c_n$; and $\liminf_{\xi\to\infty} f(\xi) \le \sum_n c_n(-1)^{\Omega(n)} < 0$, approached on a relatively dense set.
3. *Typed objects.* Continuous UAP $f:\mathbb{R}\to\mathbb{R}$; frequencies $\log n$; coefficients $a_n(t)\in\mathbb{R}_{\ge 0}$, $\ell^1$ for each fixed $t>0$ via the Gaussian factor.
4. *Map to $\Theta$.* Direct: $K_{\mathrm{pr}}(t,\xi)$ has exactly this shape. Hence $\inf_\xi \Theta(t,\xi) = K_{\mathrm{end}}(t) + K_\Gamma(t) + \inf_\xi K_{\mathrm{pr}}(t,\cdot)$ (non-oscillating parts) and loss of positivity at infinity occurs iff the archimedean/end terms fall below the (corrected) prime infimum; the failure set is then relatively dense, not an escaping sequence.
5. *Step discharged.* Escape-to-infinity, fully, for every fixed $t>0$, unconditionally; converts the task into the one-variable comparison $K_{\mathrm{end}}(t)+K_\Gamma(t)$ vs. $-\inf_\xi K_{\mathrm{pr}}(t,\xi)$.
6. *Unmet hypotheses.* No uniformity in $t$ as $t\to 0^+$; exact coefficient convention of $K_{\mathrm{pr}}$ (prime-power weights) must be matched; signed coefficients would replace the character-min by the corresponding signed variant.
7. *Circularity.* None — 1884/1918 mathematics, no zero information. Note the converse flavor: the sharpness means no slack exists; the one-variable inequality is exactly as hard as the full pointwise statement.
8. *Classification.* `applicable` (central result of the dimension; corrected constant).
9. *Cheapest test.* Compute $A(t) = \sum_n \Lambda(n)n^{-1/2}e^{-t(\log n)^2/2}$ and the corrected $\inf$ $\sum_p \min_{|z|=1}\sum_m a_{p^m}(t)\operatorname{Re}(z^m)$ numerically against $K_{\mathrm{end}}(t)+K_\Gamma(t)$ on a $t$-grid; the margin and its $t\to 0^+$ asymptotics follow by quadrature.

**T-Q2.2 Lagarias 2007 — unconditional archimedean growth (Theorem 5.1).**
1. *Citation.* J. C. Lagarias, "Li coefficients for automorphic L-functions", *Ann. Inst. Fourier (Grenoble)* **57** (2007), no. 5, 1689–1740, DOI 10.5802/aif.2311 [^47^].
2. *Theorem (Theorem 5.1, verified verbatim from the published PDF; constant corrected per verifier).* With $K(\pi) := \max_j |\kappa_j(\pi)|^2$,
$$
S_\infty(n,\pi) \;=\; \frac{N}{2}\,n\log n \;+\; C_1(\pi)\,n \;+\; O\big(N(K(\pi)+1)\big), \qquad n \ge K(\pi),
$$
with **absolute** implied constant and $C_1(\pi) = \frac{N}{2}(\gamma - 1 - \log 2\pi) + \frac12\log Q(\pi)$ (the factor $N/2$ on the first term was missing in raw dim04). Theorem 1.1: $\lambda_n(\pi) = \frac{N}{2}n\log n + C_1(\pi)n - \lambda_n(\sqrt{n},\pi) + O(\sqrt{n}\log n)$ unconditionally.
3. *Typed objects.* Li coefficients $\lambda_n(\pi) = \sum_\rho [1-(1-1/\rho)^n]$ for cuspidal automorphic $\pi$ on $GL(N)$; $S_\infty$ the archimedean (digamma/Hurwitz-zeta) part, entering via $\psi(s+1) = -\gamma + \sum_{m\ge1}(1/m - 1/(s+m))$.
4. *Map to $\Theta$.* Discrete analogue ($n \leftrightarrow 1/t$) of the digamma kernel's coercive growth: the archimedean main term $\frac{N}{2}n\log n$ is unconditionally large and positive, while the potentially negative part is only the truncated Li sum $\lambda_n(\sqrt n,\pi)$.
5. *Step discharged.* Supports the coercivity half of (b): the archimedean contribution grows linearly in $n$ (i.e. $\sim \frac1t\log\frac1t$ in Gaussian normalization) and must be compared against the zero/prime oscillation.
6. *Unmet hypotheses.* Li kernel $(1+1/s)^n - 1$ rather than the translated Gaussian; no $\xi$ parameter — translation uniformity must be re-derived; the clean asymptotic for the remainder assumes RH (that half is circular).
7. *Circularity.* Theorem 5.1 itself is unconditional (pure digamma analysis).
8. *Classification.* `conditionally applicable`.
9. *Cheapest test.* Replicate the Theorem 5.1 computation with the Gaussian kernel $k(s) = e^{t(s-1/2)^2}e^{i\xi(s-1/2)}$: does an analogous unconditional asymptotic for the archimedean piece hold with error uniform in $\xi$? A one-page saddle-point computation on $\psi(1/4+ir/2)$.

**T-Q2.3 Connes–Consani 2021 — unconditional archimedean positivity with explicit defect.**
1. *Citation.* A. Connes, C. Consani, "Weil positivity and trace formula, the archimedean place", *Selecta Math. (N.S.)* **27** (2021), Art. 77, DOI 10.1007/s00029-021-00689-4, arXiv:2006.13771 [^48^].
2. *Theorem (Theorem 6.11, verbatim from the arXiv PDF, verifier-confirmed).* For $g\in C_c^\infty(\mathbb{R}_+^*)$ with $\operatorname{supp} g \subset [2^{-1/2},2^{1/2}]$ and $\hat g(-i/2)=0$,
$$
W_\infty(g*g^*) \;\ge\; \operatorname{Tr}(\vartheta(g)S\vartheta(g)^*) \;-\; c\,|\hat g(0)|^2, \qquad c = \frac{4\gamma}{\log 2},
$$
with $\operatorname{Tr}\ge 0$; background: for smooth positive-definite $f$ supported in $(1/2,2)$ with $\hat f(\pm i/2)=0$, $W_\infty(f)\ge 0$ (Yoshida's Theorem 1, T-Q3.2).
3. *Typed objects.* $W_\infty = -W_{\mathbb{R}}$ the archimedean Weil distribution on $\mathbb{R}_+^*$; $\vartheta(g)$ the scaling action on $L^2(\mathbb{R})_{\mathrm{ev}}$; $S$ the projection onto the Sonin-space complement.
4. *Map to $\Theta$.* $W_\infty(g*g^*)$ is $K_\Gamma$ (plus its cosh term) at the autocorrelation level; the inequality is a uniform, explicit, unconditional lower bound for the archimedean contribution — exactly the "uniform lower bound for Gaussian convolutions involving digamma terms" sought — modulo the explicit defect $c|\hat g(0)|^2$.
5. *Step discharged.* Archimedean-side coercivity relevant to (b); does not touch the prime oscillation in $\xi$.
6. *Unmet hypotheses.* Support in $[2^{-1/2},2^{1/2}]$ (log-scale width $<\log 2$ — the Gaussian's log-scale support is all of $\mathbb{R}$, so it fails verbatim for every $t$); vanishing conditions; multiplicative rather than additive translation; quadratic-form (autocorrelation) level, hence $\xi$-blind.
7. *Circularity.* None — proved unconditionally via operator theory (prolate spheroidal functions, Sonin spaces).
8. *Classification.* `conditionally applicable`.
9. *Cheapest test.* Numerically evaluate $W_\infty(g*g^*)$, $\operatorname{Tr}(\vartheta(g)S\vartheta(g)^*)$, $c|\hat g(0)|^2$ for the specific Gaussian $g_{t,\xi}$ at several $(t,\xi)$ — does the inequality survive outside the support hypothesis? If yes, attempt removal of the support restriction via the decomposition $W_\infty = S - E$.

**T-Q2.4 Bombieri 2000 — explicit coercive lower bound for the Weil functional (Theorem 12).**
1. *Citation.* E. Bombieri, "Remarks on Weil's quadratic functional in the theory of prime numbers, I", *Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl.* **11** (2000), no. 3, 183–233, MR1838532, EUDML doc 252338 [^49^].
2. *Theorem (Theorem 12, verbatim).* "If $F(x)$ has compact support in an interval $I$ of length $|I| < \log 2$ we have $T[F(x)*F(-x)] = \sum_\gamma |\hat F(\gamma)|^2 \ge \big(\log(1/|I|) - \log^+\log(1/|I|) - O(1)\big)\|F\|^2$", the $O$-constant absolute. Also Lemma 3: for $f\in L^2$ supported in $[M^{-1},M]$, $T[f*f^*] = \frac{1}{2\pi}\int \operatorname{Re}\frac{\Gamma'}{\Gamma}(\frac14+\frac{iv}{2})\,|\hat f(\frac12+iv)|^2\,dv + O(M)\|f\|^2$.
3. *Typed objects.* Additive normalization of the explicit-formula distribution $T$; $F$ compactly supported; $\gamma$ the zeta ordinates.
4. *Map to $\Theta$.* $T$ is $K_{\mathrm{end}}+K_\Gamma+K_{\mathrm{pr}}$ on the arithmetic side; translation $F\mapsto F(\cdot+c)$ leaves $T[F*F(-\cdot)]$ invariant, and the bound depends only on $|I|$ — the strongest explicit-constant statement found that is uniform under test-function translation. It proves archimedean coercive dominance for narrow tests (prime terms vanish for $|I|<\log 2$).
5. *Step discharged.* Neither directly; it is unconditional archimedean coercivity with explicit structure, an ingredient for the $K_{\mathrm{end}}+K_\Gamma$ side of the fixed-$t$ comparison.
6. *Unmet hypotheses.* Compact support $|I|<\log 2$ — the Gaussian has full support; truncation reintroduces prime terms; $L^2$-quadratic-form bound, not pointwise-in-$\xi$.
7. *Circularity.* None for the small-support statement (the equality $T[F*\bar F(-\cdot)] = \sum_\gamma |\hat F(\gamma)|^2$ is the unconditional explicit formula).
8. *Classification.* `conditionally applicable`.
9. *Cheapest test.* Decompose the Gaussian $g = g_{\mathrm{small}} + g_{\mathrm{tail}}$ with $g_{\mathrm{small}}$ supported in length $<\log 2$ carrying most of the $L^2$ mass; bound the tail's prime-sum contribution explicitly (finite computation in $t$).

**T-Q2.5 Turán's criterion — circularity detector (obstruction theorem).**
1. *Citation.* P. Turán, "On some approximative Dirichlet-polynomials in the theory of the zeta-function of Riemann", *Danske Vid. Selsk. Mat.-Fys. Medd.* **24** (1948), no. 17 [^50^]; P. Turán, *On a New Method of Analysis and Its Applications*, Wiley-Interscience, 1984 [^51^]; secondary source with full discussion: G. Halász, "The number-theoretic work of Paul Turán", *Acta Arith.* **37** (1980), 9–31 [^52^].
2. *Theorem (faithfully transcribed from Halász, pp. 10–11).* "Suppose that with positive numbers $a,b,c$ we have, for all $t$ large enough, $\big|\sum_{N<n\le N'} \Lambda(n)e^{it\log n}\big| \le cN\log^2 N/|t|^a$ whenever $|t|^b\le N<N'\le 2N$. Then $\zeta(\sigma+it)\neq 0$ for $\sigma > 1 - c'(\text{function of }a,b)$, with an absolute constant $c'>0$."
3. *Typed objects.* Dyadic von Mangoldt sums with multiplicative oscillation $n^{it} = e^{it\log n}$ — precisely the object of this question.
4. *Map to $\Theta$.* Any proposed uniform-in-$\xi$ bound $|\sum_{N<n\le 2N}\Lambda(n)e^{i\xi\log n}| \ll N\log^2 N/|\xi|^a$ is, by Turán, equivalent in strength to a zero-free region; for strong enough $(a,b)$ it implies quasi-RH.
5. *Step discharged.* None — a *negative* metatheorem marking exactly which uniform estimates are RH-strength before one attempts them.
6. *Unmet hypotheses.* The hypothesis itself is unproven and RH-strength; that is the point.
7. *Circularity.* Fails as a tool; essential as a circularity detector. Any lemma of the shape "$\sum\Lambda(n)n^{i\xi}\ll\dots$ uniformly in $\xi$" must be benchmarked against it.
8. *Classification.* `circular` (as a bound) / indispensable obstruction.
9. *Cheapest test.* Substitute a proposed estimate's exponents into Turán's implication; if the resulting zero-free region beats Korobov–Vinogradov, the estimate is unprovable without RH.

#### (c) Documented near-misses (Q2)

| Near-miss | Reason |
|---|---|
| Explicit uniform-in-$\xi$ bounds for $-\zeta'/\zeta$ (Trudgian [^53^]; Cully-Hugill–Leong [^54^]; Leong [^55^]; Yang [^56^]) | `applicable` infrastructure: explicit $O(\log t)$-type bounds, uniform in the ordinate, feed the Gaussian–Mellin contour for $K_{\mathrm{pr}}$; but show no cancellation beyond zero-free-region strength, hence cannot close the criterion. Cheapest test: plug Trudgian's constants at $\sigma = 1+1/\log(|\xi|+2)$. |
| Omega theorems (Yang [^57^]; Li–Zhao [^58^]; Aistleitner–Mahatab–Munsch [^59^]; Bondarenko–Seip [^60^]) | `applicable` obstruction side: $\max_{T^\beta\le t\le T}(-\operatorname{Re}\zeta'/\zeta(1+it)) \ge \log_2 T + \log_3 T + O(1)$ via resonators — quantifies how deep the prime dips go as $t\to 0^+$; Yang's resonator is itself Gaussian-weighted, so the method transfers to $K_{\mathrm{pr}}$ but the published weights are $n^{-1}$, not the Weil weight. |
| Jacobi triple product / lattice theta uniform positivity (Montgomery [^61^]; Faulhuber–Steinerberger [^62^]; Janssen [^63^]; Biane–Pitman–Yor [^64^]) | `conditionally applicable` model: $\vartheta_3>0$ uniformly via the product formula — but $K_{\mathrm{pr}}$ has incommensurate frequencies $\log p$ and no product structure, so the argument does not transfer. |
| Weil 1952 positivity criterion [^65^] | RH-equivalent; quadratic-form level, $\xi$-blind. Quarantined (Section 4). |
| Wintner 1935/1941/1943 (zeros-side series B²-almost-periodic) [^66^][^67^] | The B²-AP property of the PNT remainder is *equivalent* to RH (Wintner's 1943 converse) — circular; heuristic value only. |
| Li criterion [^68^] / Bombieri–Lagarias / Omar–Mazhouda [^69^][^70^] | RH equivalences; $\xi$-free positivity. Quarantined. |
| Yoshida 1992 Prop. 1 / Thm 2 [^71^] | RH-equivalences (Lemma 2, unconditional small-support positivity, is the usable fragment — see Q3). |
| Positive cosine-sum theorems (Young 1913 [^72^]; Vietoris 1958 [^73^]; Brown–Dai–Wang 2007 [^74^]) | Require commensurate frequencies $k\theta$ or orthogonal-polynomial structure; $\sum c_p\cos(\xi\log p)$ is outside their scope and provably changes sign in general. |
| Katkova–Lobova–Vishnyakova partial-theta Laguerre–Pólya threshold [^75^] | Laguerre–Pólya membership concerns zeros in $z$, not positivity on $|z|=1$ where $\xi$ lives; wrong slice of the plane. |
| Vinogradov/Vaughan-type additive-character prime sums (Vinogradov 1954; Vaughan 1977; Daboussi–Rivat 2001; Vaughan L¹ 1988; Bazin 2025, arXiv:2508.18394; Srivastav 2025, arXiv:2505.07803; Montgomery–Vaughan 1977, Invent. Math. 43, 69–82) | Wrong oscillation: additive twist $e(\alpha n)$, not multiplicative $n^{i\xi}$. No Vinogradov-type bound for $n^{i\xi}$ beyond zero-free-region strength can exist (Turán, T-Q2.5). Vaughan's identity transfers as *method* only. |
| Turán–Knapowski power-sum machinery [^76^][^77^][^78^] | Oscillation in the $x$-variable (center of the Gaussian window), not in the translation $\xi$; relevant method if one needs to prove failure of positivity from a hypothetical off-line zero (effective sign-change localization). |
| Explicit Riemann–von Mangoldt error bounds (Cully-Hugill–Johnston et al., arXiv:2111.10001) | Control $\psi(x)$ with constants; no positivity, no translated-Gaussian/digamma balance. |
| Landau–Gonek explicit formulas [^79^][^80^], Aryan extension [^81^], Balanzario–Cárdenas–Chacón smooth version (arXiv:2311.04347, Thm 1 only; Thm 2 assumes RH), Montgomery–Vaughan Gaussian log-kernel identity [^82^] | Unconditional exact identities, useful infrastructure; note the mapping subtlety: the log-Gaussian kernel dualizes to $e^{+a^2\rho^2/2}$ over zeros (divergent) — the Weil kernel's Gaussian is in the Fourier coordinate with $e^{-\gamma^2/(2t)}$, convergent for fixed $t>0$. Identities discharge no bound by themselves. |
| Zero-density estimates (Ingham [^83^]; Huxley [^84^]; Guth–Maynard, arXiv:2405.20552 [^85^]; Kadiri–Lumley–Ng [^86^]; Bellotti [^87^]) with explicit zero-free regions (Mossinghoff–Trudgian–Yang [^88^]; Ford [^89^]) | Make zeros-side estimates $\xi$-uniform and unconditional, but are strictly weaker than RH: the $\sigma\to 1/2^+$ limit is trivial ($\asymp T\log T$), so this route provably cannot close the full criterion; Bellotti's explicit estimate covers only $T \le \exp(6.7\times10^{12})$. |
| de Bruijn–Newman heat-flow results (Rodgers–Tao [^42^]; Csordas–Norfolk–Varga 1988 [^90^]; Polymath15 [^91^]) | Zero-location results about $H_t$, not pointwise positivity in $\xi$; $H_t$ heats ($e^{+tu^2}$) where $\Theta$ cools ($e^{-t\gamma^2}$) — see Q5 for the sign obstruction. `inapplicable` to (b). |
| Suzuki's screw-function framework [^92^][^93^] | Gives the explicit digamma-kernel form $Q_W^a(v) = \frac{1}{2\pi}\int(\log|z|-\log 2\pi)|\hat v|^2 dz + O(a)\|v\|^2$ — the archimedean coercive weight with exact constants — but is $\xi$-blind (depends on $|\hat v|^2$); the pointwise criterion $g(t)\le 0 \iff$ RH is circular. |
| Groskin 2026 archimedean tail theorem (arXiv:2607.02828) [^94^]; Connes–Consani–Moscovici (arXiv:2511.22755) [^95^]; Connes–van Suijlekom (arXiv:2511.23257) [^96^] | Total positivity of truncated archimedean tail matrices with explicit budgets — unconditional but Galerkin/matrix-level, no translation parameter, 2026 preprints not yet refereed. |

**Bottom line (Q2).** Fixed-$t$ escape-to-infinity is excluded by verified 1884–1918 mathematics (T-Q2.1, corrected) plus pole-term dominance; the uniform $t\to 0^+$ regime is reduced to the explicit one-variable comparison between $K_{\mathrm{end}}+K_\Gamma$ and the corrected prime-sum infimum, with archimedean coercivity supplied by Lagarias/Bombieri/Connes–Consani (T-Q2.2–T-Q2.4). Uniform-in-$\xi$ estimates beyond Korobov–Vinogradov strength are provably RH-strength (T-Q2.5) — a rigorous obstruction, not a gap of diligence.

### 3.3 Q3 — Weil positivity (Dimensions 06–07)

#### (a) Narrative assessment

This dimension pair asked two things: (i) does the classical Weil-positivity literature contain an unconditional, direct arithmetic proof of positivity for Gaussian tests, or a theorem promoting positivity on the Gaussian family to the full Weil criterion; (ii) what exactly is circular. The answers are sharp and mostly negative, but the negative answers are themselves decisive structure:

- **The target equivalence is fully documented.** RH ⟺ $\sum_v W_v(g*g^*) \le 0$ for all admissible $g$ with $\hat g(\pm i/2) = 0$ (Weil 1952 [^65^]; Bombieri Theorem 2 [^49^]; modern transcription in Connes–Consani [^48^] and Connes's 2026 survey [^97^]). $\Theta(t,\xi)\ge 0$ for all $(t,\xi)$ is the Gaussian specialization. By definition this cannot be a proof tool — it is the goal.
- **Analytic legitimacy of Gaussian tests is unconditional** (Barner's admissibility class, (B1)–(B3) [^98^][^99^]): $\Theta(t,\xi)$ is rigorously well-defined via the explicit formula for all $(t,\xi)$.
- **Unconditional positivity exists only in compact windows.** Yoshida's Theorem 1 [^71^] ($W_\infty(f)\ge 0$ for positive-definite $f$ supported in $(1/2,2)$ with $\hat f(\pm i/2)=0$), Bombieri's variational small-$t$ positivity [^49^][^100^], Connes–Consani's archimedean trace-form positivity [^48^], Suzuki's small-interval screw-function positivity [^92^][^93^], and the certified-window preprint [^101^] all require compact support with at most finitely many primes entering. The Gaussian has full position-side support — every prime power contributes to $K_{\mathrm{pr}}$ — so none applies verbatim (insight I2).
- **The promotion machinery now exists in print (2021–2026) and is unconditional, but the Gaussian-density hypothesis is missing.** Yoshida's localization (RH ⟺ windowed positivity for every $a>0$), Connes–Consani's lower-boundedness/lower-semicontinuity with trigonometric-polynomial core [^102^], and Suzuki's Corollary 1.2 (infimum of the Rayleigh quotient over the form domain equals the infimum over $C_c^\infty(-a,a)$ — positivity on a form-norm-dense subset suffices) [^92^] together give: *positivity on any form-norm-dense subset of $C_c^\infty(-a,a)$, for all $a$, is equivalent to the full criterion*. Wiener's theorems [^103^] give density of Gaussian translates in $L^1/L^2$, but the Weil form's continuity scale is windowed $H^{\log}$-type, not $L^1/L^2$ — **no published theorem states that (truncated) Gaussian mixtures are dense in the form norm, and no theorem states that the two-parameter Gaussian family detects positivity**. This pair of statements is precisely the gap the $\Theta$-project must fill itself (dim07's synthesis; insight I6).
- **A structural wrinkle:** for the *quadratic* form, $\gamma_{t,\xi}*\tilde\gamma_{t,\xi} = \gamma_{2t,0}$ is $\xi$-independent, so on autocorrelations the Gaussian family collapses to the one-parameter dilation family $\{W(\gamma_{2t,0})\}$ — visibly not positivity-detecting. The $\xi$-translations only act on the *linear* evaluation $\Theta(t,\xi) = W(\gamma_{t,\xi})$; any promotion must therefore run through mixtures $\sum_j c_j \gamma_{t_j,\xi_j}$ and positive-type combinations (insight I4).
- **One unconditional sign trick ignores zero locations entirely:** Poitou–Odlyzko [^104^][^105^] — if the test function's Mellin transform $\Phi(s)$ is pointwise nonnegative on the whole critical strip, the zero side contributes nonnegatively with no RH input. The shifted-Gaussian transform $\exp(-t(s-\frac12)^2)$ takes both signs off the line, so the trick fails verbatim for $\Theta$, but it isolates the exact property (strip-nonnegative Mellin transform) that would make zero-side positivity unconditional.

#### (b) Top theorems (9-field schema)

**T-Q3.1 Weil 1952 — the positivity criterion (circular benchmark).**
1. *Citation.* A. Weil, "Sur les 'formules explicites' de la théorie des nombres premiers", Comm. Sém. Math. Univ. Lund, Tome Suppl. (M. Riesz volume), 1952, 252–265; Œuvres II, 48–62 [^65^]. Distributional/local form: Weil 1972 [^106^].
2. *Theorem.* No numbered theorems; final pages: RH ⟺ $\sum_v W_v(g*g^*) \le 0$ for all $g\in C_c^\infty(\mathbb{R}_+^*)$ with $\hat g(\pm i/2)=0$ (Hecke-Grössencharakter version: GRH ⟺ positivity).
3. *Typed objects.* Autocorrelation class $f = g*g^*$ on $\mathbb{R}_+^*$; zeros with multiplicity.
4. *Map to $\Theta$.* $\Theta(t,\xi)\ge 0$ for all $(t,\xi)$ is the Gaussian specialization (up to the global sign convention between $\Theta$ and $\sum_v W_v$).
5. *Step discharged.* None — it is the statement being reduced to, not a tool.
6. *Unmet hypotheses.* n/a.
7. *Circularity.* Yes, by definition RH-equivalent.
8. *Classification.* `circular` (foundational benchmark).
9. *Cheapest test.* n/a.

**T-Q3.2 Yoshida 1992 — localization, unconditional window positivity, form continuity.**
1. *Citation.* H. Yoshida, "On Hermitian forms attached to zeta functions", Adv. Stud. Pure Math. 21, Kinokuniya, 1992, 281–325. DOI 10.2969/aspm/02110281 [^71^].
2. *Theorems (faithful).* Theorem 1 (verbatim via Connes's 2026 survey §4.1, verifier-confirmed): "For any smooth, positive definite function $f$ with support in the interval $(1/2, 2)$ and whose Fourier transform vanishes at $\pm i/2$ one has: $W_\infty(f)\ge 0$" ($W_\infty := -W_{\mathbb{R}}$). Localization: RH ⟺ positive definiteness of the form on $C(a)$ for every $a>0$. Lemma 2: positivity on small windows $a\le a_0$. Lemma 3: coercivity $(\varphi,\varphi)\ge\mu\|\varphi\|^2$ on a finite-codimension subspace. Lemmas 4–5: sup/$C^1$-continuity and bilinear $L^2$-continuity of the form on fixed windows. Proposition 2: nondegeneracy on every $C(a)$.
3. *Typed objects.* Hermitian form $(\varphi_1,\varphi_2) = T(\varphi_1*\tilde\varphi_2)$; support $(1/2,2)$ multiplicatively ⟺ no prime power contributes (2 is the first prime).
4. *Map to $\Theta$.* Archetype of "positivity for small $t$": in the regime where the Gaussian autocorrelation is effectively supported inside $(1/2,2)$, $\Theta \approx W_\infty$ part only. Lemmas 4–5 are the published continuity scale of the Weil functional — the norm in which Gaussian density would have to be proved.
5. *Step discharged.* Localization (full criterion ⟺ window-by-window positivity) and unconditional archimedean-window positivity; continuity estimates for the promotion argument. Does not discharge double-contact or escape-to-infinity.
6. *Unmet hypotheses.* Compact support in $(1/2,2)$ — fails for Gaussians; $\hat f(\pm i/2)=0$ must be enforced; positive definiteness (true for autocorrelations); Lemma 5's constant $c_a$ unquantified as $a\to\infty$.
7. *Circularity.* None in the unconditional fragments (proof is numerical-analytic, no zero locations).
8. *Classification.* `applicable` (regime-restricted); `conditionally applicable` to $\Theta$.
9. *Cheapest test.* Compute the Toeplitz eigenvalues for the Gaussian autocorrelation truncated to $(1/2,2)$ and quantify tail error against the smallest eigenvalue; re-run Lemma 5 with explicit $a$-dependence.

**T-Q3.3 Bombieri 2000 — variational attainment and countable reduction.**
1. *Citation.* E. Bombieri, "Remarks on Weil's quadratic functional in the theory of prime numbers, I", Atti Accad. Naz. Lincei Rend. Lincei (9) Mat. Appl. 11 (2000), 183–233, EUDML 252338 [^49^].
2. *Theorems (quoted).* Theorem 2: $T[f*f^*]\ge 0$ on $C_0^\infty((0,\infty))$ ⟺ RH. Countable reduction: positivity ⟺ $T[g_{n,\varepsilon}]>0$ for an explicit countable two-parameter family. Variational theorem: the functional attains its minimum on the unit $L^2$-ball of functions supported in $[-t,t]$, and is positive definite for $t$ small (reproving Yoshida's value $t=(\log 2)/2$, extended to $t=\log 2$). Truncated-eigenvalue theorem: if RH fails with finitely many off-line zeros, the number of negative eigenvalues of large truncations equals half the number of violating zeros.
3. *Typed objects.* $T$ on $C_0^\infty(\mathbb{R}_+^*)$; $L^2$ variational problem; finite truncations of the infinite quadratic form.
4. *Map to $\Theta$.* The Gaussian family is a two-parameter subfamily of the admissible tests; the minimum-attainment theorem is exactly the variational setup behind the "first violation = minimizer touches zero" picture; the eigenvalue-counting theorem is the truncated-matrix analogue of double-contact exclusion.
5. *Step discharged.* Variational machinery for the first-violation picture; the only published "restricted countable class ⟺ full criterion" results (with Bombieri–Lagarias, T-Q3.7).
6. *Unmet hypotheses.* Positivity statements are RH-equivalent (circular as tools); unconditional positivity only for $t\le\log 2$ compact windows — violated by the Gaussian family.
7. *Circularity.* Theorem 2 and the $g_{n,\varepsilon}$ reduction: RH-equivalent → circular. Variational attainment and small-window positivity: unconditional.
8. *Classification.* Mixed: `circular` (Thm 2, countable reduction) / `conditionally applicable` (variational attainment, eigenvalue counting).
9. *Cheapest test.* Approximate the Gaussian by compactly supported autocorrelations, bound the induced error in $T$ (Gaussian tails are explicit), and check whether minimum-attainment applies on the approximating subspace.

**T-Q3.4 Connes–Consani 2021 + 2023 — unconditional archimedean positivity and form-core results.**
1. *Citations.* [^48^] (Selecta 27 (2021), Paper 77); "Spectral triples and ζ-cycles", Enseign. Math. 69 (2023), 93–148, arXiv:2106.01715 [^102^].
2. *Theorems.* Corollary 2.3: $L(f) = \int f(\rho^{-1})(\delta(\rho)-\tau(\rho))\,d^*\rho$ is positive on the convolution algebra $C_c^\infty(\mathbb{R}_+^*)$ (trace of positive operators), $2\theta'(t) + \hat\delta(t)\ge 0$ — unconditional. Corollary 2 + Theorem 6.11: explicit archimedean lower bound with defect $c = 4\gamma/\log 2$ (see T-Q2.3). Proposition 2.1 (2023): $Q_W^a$ is lower bounded and lower semicontinuous in $L^2(-a,a)$, hence closable. Proposition 2.3: trigonometric polynomials are a form core.
3. *Typed objects.* Semi-local trace-formula Hilbert space; cutoff projections; Sonin spaces; prolate spheroidal functions.
4. *Map to $\Theta$.* Strongest known *conceptual* proof of the small-window positivity underlying the broad-smoothing regime; Props 2.1/2.3 are the continuity half of any density-promotion argument for $\Theta$.
5. *Step discharged.* Unconditional foundation of the small-window region; the closability/core properties needed for promotion. Does not extend past the first prime.
6. *Unmet hypotheses.* Support $[2^{-1/2},2^{1/2}]$, vanishing conditions; Gaussian fails both literally.
7. *Circularity.* None in the proved directions.
8. *Classification.* `applicable` (archimedean window) / `conditionally applicable` to $\Theta$.
9. *Cheapest test.* Check whether the compression estimate (Lemma 6.10) survives Gaussian multipliers replacing indicator cutoffs — precisely the $\Theta$ setting.

**T-Q3.5 Suzuki 2023–2026 — screw function, form closability, dense-subset sufficiency.**
1. *Citations.* M. Suzuki, "Aspects of the screw function corresponding to the Riemann zeta function", J. Lond. Math. Soc. 108 (2023), 1448–1487, DOI 10.1112/jlms.12785, arXiv:2206.03682 [^93^]; "Weil's quadratic form via the screw function", arXiv:2606.09096 (2026, preprint) [^92^]; "On the Hilbert space derived from the Weil distribution", Canad. J. Math. (2025), DOI 10.4153/S0008414X25101739, arXiv:2301.00421 [^107^].
2. *Theorems (faithful).* Theorem 1.1 (arXiv:2606.09096): $Q_W^a$ on $C_c^\infty(-a,a)$ is lower bounded, closable; its closure is the Friedrichs form of a self-adjoint operator with compact resolvent. **Corollary 1.2:** $C_c^\infty(-a,a)$ is form-norm dense in the form domain; hence positivity of $Q_W^a$ on any dense subspace is equivalent to positivity on the full domain. Theorem 1.3: lowest eigenvalue continuous in $a$. Also: continuous screw function $G_a$ replacing the distributional kernel; RH ⟺ $-g(t)\ge 0$ for all $t$ (one-variable target); unconditional small-interval positivity recovering the Yoshida window; all stated "without assuming the Riemann Hypothesis" for the structural results. The CJM paper constructs the de Branges space from the Weil distribution **under RH** — circular for proof purposes (quarantined).
3. *Typed objects.* Kreĭn screw functions; continuous-kernel hermitian forms on $L^2(-a,a)$; Rayleigh-quotient infima.
4. *Map to $\Theta$.* $Q_W(v)$ with $v$ a mixture of shifted Gaussians is a quadratic expression in values $\Theta(2t_{ij}, \xi_i - \xi_j)$: the *only* located result that makes "positivity on a dense subset ⇒ positivity everywhere" rigorous for the Weil functional — in windowed form-norm topology.
5. *Step discharged.* The "dense subset ⇒ full space" implication, per window, unconditionally. The Gaussian-density hypothesis itself is NOT in the paper.
6. *Unmet hypotheses.* (a) truncation to $(-a,a)$; (b) form-norm density of truncated Gaussian mixtures; (c) uniformity as $a\to\infty$ — none proved anywhere.
7. *Circularity.* Corollary 1.2 package: clean. The RH-equivalences and the CJM Hilbert-space construction: circular as tools.
8. *Classification.* `conditionally applicable` (Cor. 1.2, form machinery); `circular` (CJM RH-assuming construction).
9. *Cheapest test.* Fix $a=1$: is the form-norm closure of span of smoothed truncated Gaussians equal to the form domain? Fourier-side reduction: density of bandlimited truncations of $e^{-tz^2/2}\times$(plane waves) in $L^2(\mathbb{R}, (1+\log^+|z|)\,dz)$; finite Gram-matrix computations already give strong evidence.

**T-Q3.6 Li 1997 / Bombieri–Lagarias 1999 — restricted countable families suffice (paradigm; circular as tool).**
1. *Citations.* X.-J. Li, J. Number Theory 65 (1997), 325–333, DOI 10.1006/jnth.1997.2137 [^68^]; E. Bombieri, J. C. Lagarias, J. Number Theory 77 (1999), 274–287, DOI 10.1006/jnth.1999.2392 [^69^].
2. *Theorem.* RH ⟺ $\lambda_n = \sum_\rho (1-(1-1/\rho)^n) \ge 0$ for all $n\ge 1$; Bombieri–Lagarias show the $\lambda_n$ are Weil-functional evaluations on a countable test family — sparse families can capture full Weil positivity.
3. *Typed objects.* Li coefficients; discrete one-parameter test family.
4. *Map to $\Theta$.* Proof of concept that restricted families can be positivity-detecting; the Gaussian family is NOT known to be (no density theorem), unlike the Li family.
5. *Step discharged.* None (RH-equivalent by construction).
6. *Unmet hypotheses.* The $\lambda_n$ encode all zeros by construction.
7. *Circularity.* Yes — RH-equivalent.
8. *Classification.* `circular` as tool; structural paradigm.
9. *Cheapest test.* n/a.

**T-Q3.7 Poitou–Odlyzko — strip-nonnegative Mellin transforms (the one unconditional zero-side sign trick).**
1. *Citations.* G. Poitou, Sém. DPP 1976/77, exp. 6, Numdam [^104^]; A. M. Odlyzko, J. Théor. Nombres Bordeaux 2 (1990), 119–141, DOI 10.5802/jtnb.22 [^105^].
2. *Theorem (technique).* Choose $F$ with $\Phi(s)\ge 0$ on the whole strip $0\le\operatorname{Re} s\le 1$; then $\sum_\rho \Phi(\rho)\ge 0$ unconditionally, since every zero in the strip contributes nonnegatively. This yields unconditional discriminant bounds.
3. *Typed objects.* Explicit formula for Dedekind zeta functions; test Mellin transforms engineered for strip positivity.
4. *Map to $\Theta$.* The shifted-Gaussian transform $\exp(-t(s-\frac12)^2)e^{\xi(s-1/2)}$ takes both signs off the line, so the trick fails verbatim; but it isolates the exact property needed: **any test whose Mellin transform is $\ge 0$ on the strip gives unconditional zero-side positivity**.
5. *Step discharged.* None directly; defines the design constraint for any unconditional zero-side argument.
6. *Unmet hypotheses.* Strip-nonnegativity of the transform — fails for the shifted Gaussian.
7. *Circularity.* None — never assumes RH in the unconditional form.
8. *Classification.* `applicable` as technique; `inapplicable` verbatim to $\Theta$.
9. *Cheapest test.* For $\xi=0$: can $\exp(t(s-\frac12)^2)$ be dominated by a strip-nonnegative transform (one-line numerical check)?

#### (c) Documented near-misses (Q3)

| Near-miss | Reason |
|---|---|
| Weil 1972 local explicit formula [^106^] | The canonical local decomposition $W = \sum_v W_v$; formula only, no positivity. `applicable` as reference. |
| Haran 1990 Riesz potentials [^108^] | Potential-theoretic rewriting of explicit sums; suggests sign structure of local terms but contains no unconditional positivity theorem for the zeta functional. |
| Lagarias 1999 ($\operatorname{Re}(\xi'/\xi)(s) > 0$ for $\operatorname{Re} s>1/2$ ⟺ RH) [^109^] | RH-equivalent pointwise (not quadratic-form) positivity — circular; a genuinely pointwise statement, though, worth noting as a model. |
| Connes 1999 adele-class trace formula [^110^] | Global trace formula ⟺ RH — circular; semilocal pieces unconditional. Prototype of the "dense subset" argument (test functions in $L^2_\delta$), completed rigorously only in [^102^][^92^]. |
| Bombieri–Hejhal 1995 [^111^] | Assumes GRH and a density hypothesis; output is zero statistics, not positivity — `inapplicable` and circular. |
| Suzuki CJM 2025 (Hilbert space from the Weil distribution) [^107^] | Whole construction assumes RH — circular for proof purposes (natural habitat for a global density statement if it existed unconditionally). |
| Nyman–Beurling–Báez-Duarte density criterion [^112^] | The paradigm "restricted family suffices for RH", but density is Mellin-dual to RH by construction — circular as proof ingredient. |
| Krein–Langer hpd-continuation theory [^113^] | Correct abstract framework under the screw-function results; no statement about the Weil functional itself. |
| Burnol's complete/minimal zero-attached systems [^114^] | Density statements on the spectral side, tied to zero locations — circularity risk. |
| Wiener Tauberian density [^103^]; Hermite completeness [^115^] | Genuine density of Gaussian translates/mixtures, but in $L^1/L^2$ norms where the Weil form is not known to be continuous — near-miss alone; `conditionally applicable` combined with [^102^][^92^][^71^]. |
| Beurling–Selberg extremals / Gaussian subordination [^116^][^117^][^118^] | Canonical bandlimited majorants/minorants of the Gaussian with explicit $L^1$ error — the bridge from Gaussian tests to compactly supported Weil tests; $L^1$ kernel error still must be converted to form-norm error. Caution: headline applications to $\zeta$ bounds (Carneiro–Chandee–Milinovich et al.) assume RH — circular. |
| Bombieri 2003 Hilbert-space variational reformulation [^100^] | Recasts Weil positivity as Hilbert-space minimization (attainment, sign of the infimum); equivalence core RH-circular, and Suzuki [^92^] cautions the global form-continuity assertion there is not fully justified — rigorous version is [^102^][^92^]. `conditionally applicable` with caveat. |
| Barner admissibility [^98^]; Büthe–Franke–Jost–Kleinjung [^99^]; Avdispahić–Smajlović [^119^] | Legitimizes evaluation of $\Theta$ (`applicable`); contains no density or continuity statement for the quadratic form — near-miss for promotion. |
| Connes–Consani–Moscovici "Zeta spectral triples" [^95^]; Connes–van Suijlekom [^96^] | Finite-dimensional Carathéodory–Fejér truncated forms; semi-local restricted-family positivity; 2025–26, monitor. |
| Zhu, certified compact-window positivity, arXiv:2608.24827 [^101^] | Certified positivity up to autocorrelation support 1.6 with Landau–Widom decay; argues the windowed route "cannot reach RH unassisted" (frequency-resolution threshold $\sim 2\pi e^{A_L}$, $A_L\sim 4e^L$). Unrefereed preprint; `conditionally applicable`. |
| Wong's transcription [^120^] | Secondary checkpoint for exact normalizations (Theorems 2.1–2.3); itself circular on positivity. |
| Gaussian-mixture density in statistics (Norets, Ann. Statist. 38 (2010), 1733–1766) | KL/$L^1$ probabilistic metrics, unrelated to the Weil form. |
| Explicit search for "Gaussian family suffices" theorems | **Not found.** No published theorem states positivity on the two-parameter shifted-Gaussian family implies the full Weil criterion. This is a genuine literature gap, not a search failure (dims 06–07 both searched exhaustively). |

**Bottom line (Q3).** Unconditional Weil positivity exists in the literature only in compact windows (Yoshida; Bombieri; Connes–Consani; Suzuki; certified-window preprint); the promotion principle "dense subset ⇒ full space" now exists rigorously in windowed form-norm topology (Suzuki Cor. 1.2; Connes–Consani Props 2.1/2.3; Yoshida Lemmas 4–5); what is missing from all of mathematics in print is form-norm density of Gaussian mixtures and its $a\to\infty$ uniformity. Every global positivity criterion located is RH-equivalent and quarantined.

### 3.4 Q4 — Strict-peak interpolation (Dimensions 08–09)

#### (a) Narrative assessment

The strict-peak problem asks for an entire/Paley–Wiener transform $F$ with $|F|=1$ at one reciprocal zero pair $\frac12 \pm i\gamma_0$ and $|F|<1$ at all other zeta zeros (or an exact Kronecker-delta peak, or a value+derivative prescription), with the intended use being a contradiction-with-nonpositivity argument. The literature splits the problem cleanly into three regimes, and produces one of the search's two rigorous obstructions:

1. **Unconditional interpolation at the zeros exists — outside the Paley–Wiener class.** Bondarenko–Radchenko–Seip (2023, Thm 1.1) [^121^] construct, with no unproven hypothesis, rapidly decaying even entire functions $V_{\rho,j}$ interpolating arbitrary data (including derivatives up to multiplicity) at *all* nontrivial zeros with $\gamma'>0$, off-line zeros included. Burnol (2004, Thms 3.1–3.3, 5.2) [^114^] constructs unconditional dual/interpolation systems in Sonine (de Branges) spaces. Neither family is bounded bandlimited (no compact Fourier support, no global modulus control). Trivially, $F(z) \propto \xi(\frac12-iz)/(z-z_{\rho_0})$ is a strict peak on the zero set for free — confirming the difficulty is *entirely* the function-class constraint, not interpolation per se.
2. **Every RKHS route whose nodes are exactly the zeta zeros is RH-circular or disproved.** For $E(z) = \xi(1-iz)$, Hermite–Biehler holds unconditionally, but the zeta zeros lie on the symmetry axis iff RH, and at an on-axis zero $w$ of $E$ the reproducing kernel degenerates ($K(w,w)=0$): under RH *every* element of $\mathcal H(E)$ vanishes at every shifted zero — no strict-peak function can live in that space. de Branges' positivity conditions [^122^] imply RH but were **disproved** for $\xi$ by Conrey–Li [^123^] (the sign condition fails at the 34th zero, unconditionally). Suzuki's inner-function criterion [^124^] is RH-equivalent at the critical parameter; the RH-assuming Hamiltonian/model-space constructions [^125^][^126^][^127^] are all quarantined.
3. **Bandlimited interpolation at the zero ordinates is unconditionally obstructed — this is the search's rigorous obstruction (insight I5).** Riemann–von Mangoldt ($N(T)\sim \frac{T}{2\pi}\log\frac{T}{2\pi e}$ [^128^]) gives the ordinate sequence superlinear counting $n(r)\asymp r\log r$, hence infinite Beurling–Malliavin density, infinite upper/lower uniform densities, and zero separation. Consequences, all unconditional: (i) the punctured system $\{e^{i\gamma t}:\gamma\neq\gamma_0\}$ is complete in $L^2(-\sigma,\sigma)$ for **every** $\sigma$ (Beurling–Malliavin 1967), so the **exact peak does not exist in any $PW_\sigma$ at any bandwidth**; (ii) independently, Cartwright–Levin zero-density theory forbids a bounded exponential-type function from vanishing on a superlinear set; (iii) $\{\gamma\}$ is never interpolating (Landau 1967; Ortega-Cerdà–Seip), so no biorthogonal peak-function machinery exists; (iv) Beurling's sampling theorem gives the *quantitative* strict-peak obstruction $1 \le K\,\sup_{\gamma\neq\gamma_0}|f(\gamma)|$, i.e. the dip is bounded below by the reciprocal of a sampling constant; (v) Ortega-Cerdà–Seip's Fourier-frame theorem shows the coefficient functionals are unbounded — approximate peaks force $L^2$-norm blow-up. The one-point strict (nonzero) peak itself is **not literally excluded** by any located theorem; deciding it is a quantitative sampling-constant problem at infinite density (open sub-problem, T-Q4.4 below).

**Net assessment:** the interpolation step can be discharged unconditionally (T-Q4.1, T-Q4.2) but only outside the PW/Gaussian-test class; the RKHS shortcut is circular or disproved; exact bandlimited peaks are unconditionally impossible; strict bandlimited peaks are quantitatively obstructed and undecided. If the intended argument needs a *bandlimited* strict peak, the route is dead in the exact version and must be replaced by the envelope-localization construction of the BM multiplier theorem (T-Q4.5), which cannot enforce a strict dip at the *nearest* zeros (Lehmer-type pairs with gaps $\to 0$) — precisely where the obstruction lives.

#### (b) Top theorems (9-field schema)

**T-Q4.1 Bondarenko–Radchenko–Seip 2023 — unconditional interpolation at zeta zeros.**
1. *Citation.* A. Bondarenko, D. Radchenko, K. Seip, "Fourier interpolation with zeros of zeta and L-functions", Constr. Approx. 57 (2023), 405–461. DOI 10.1007/s00365-022-09599-w. arXiv:2005.02996 [^121^].
2. *Theorem (Theorem 1.1, transcribed).* For every nontrivial zero $\rho=\beta+i\gamma$ ($\gamma>0$) of multiplicity $m_\rho$ and each $0\le j<m_\rho$, there exist rapidly decaying even entire functions $V_{\rho,j}$ with $V_{\rho,j}^{(j')}((\rho'-1/2)/i) = \delta_{\rho\rho'}\delta_{jj'}$ for all nontrivial zeros $\rho'$ with $\gamma'>0$, and $\widehat{V_{\rho,j}}(\pm\log n/4\pi)=0$; every $f$ in the strip class $\mathcal H_1$ admits the Fourier interpolation formula $f = \sum_{\rho,j} f^{(j)}(z_\rho)V_{\rho,j} + \sum_n \hat f(\pm\log n/4\pi)W_n$. **No RH, no simplicity assumption.**
3. *Typed objects.* Even entire functions, rapidly decaying in a strip; nodes $z_\rho = (\rho-1/2)/i$.
4. *Map to $\Theta$/strict-peak.* $F = V_{\rho_0,0}$: $F(z_{\rho_0})=1$, $F=0$ at all other upper-half-plane zeros (off-line included); evenness gives the conjugate pair. Strict peak on the zero set, unconditionally.
5. *Step discharged.* Construction of the interpolant on the zero set (nothing asserted about $|F|$ between zeros).
6. *Unmet hypotheses.* $V_{\rho,0}$ is not shown to be of finite exponential type, bounded on $\mathbb{R}$ in the PW sense, or a transform of a compactly supported (let alone Gaussian-shifted) test function; $\widehat V$ vanishes at $\log n/4\pi$ but is not compactly supported.
7. *Circularity.* Clean — contour-integral construction, works for arbitrary zero locations. Flag: feeding the peaks back into an RH proof via Weil positivity would risk circularity in spirit (the duality derives from the functional equation).
8. *Classification.* `applicable` (construction step) with class-mismatch caveat; `inapplicable` to the bandlimited strict-peak problem proper.
9. *Cheapest test.* Estimate the exponential type and $L^\infty(\mathbb{R})$ growth of $V_{\rho_0,0}$ from its defining contour integral: if order 1 finite type, it is a PW function and strict peak is solved outright; else quantify the mismatch.

**T-Q4.2 Burnol 2004 — complete/minimal systems and Sonine-space interpolation at the zeros.**
1. *Citation.* J.-F. Burnol, "Two complete and minimal systems associated with the zeros of the Riemann zeta function", J. Théor. Nombres Bordeaux 16 (2004), no. 1, 65–94 (pages corrected; dim08's 65–99 wrong). DOI 10.5802/jtnb.434. arXiv:math/0203120 [^114^]. Context: Burnol, "On Fourier and Zeta(s)", Forum Math. 16 (2004), 789–840, arXiv:math/0112254 [^129^].
2. *Theorems.* Thm 3.1: in each extended Sonine space $L_a$ the zero-evaluators $Y_{\rho,\nu}^a$ form a complete system. Thm 3.2: they are minimal. Thm 3.3: dual elements $g_\rho$ (completed Mellin transform $\zeta(s)/((s-\rho)\zeta'(\rho)\cdot(\text{Gamma/conductor factors}))$, simple zeros) lie in $L_1$ with $\delta_{\rho\rho'}$ pairing. Thm 5.2: residue interpolation series. Explicitly no hypothesis on multiplicities; RH never assumed.
3. *Typed objects.* $L_a \subset L^2(0,\infty;dt)$, cosine-transform self-dual; bilinear Sonine pairing.
4. *Map to strict-peak.* $g_{\rho_0}$ has completed Mellin transform $1$ at $\rho_0$ and $0$ at all other zeros — a strict-peak interpolant in a de Branges-flavored Hilbert space.
5. *Step discharged.* Construction of interpolants (Sonine/Mellin category).
6. *Unmet hypotheses.* Interpolants are $L^2$-Mellin objects (meromorphic after completion), not bounded entire functions of exponential type; bilinear pairing, so "modulus 1" has no norm meaning; no PW/Gaussian structure.
7. *Circularity.* Clean.
8. *Classification.* `applicable` (construction), class-mismatch caveat.
9. *Cheapest test.* Check whether the Sonine isometry transports $g_{\rho_0}$ into a de Branges space $\mathcal H(E)$ with $E$ of Pólya class; if yes, test boundedness of its Mellin transform on the critical line numerically for low zeros.

**T-Q4.3 Beurling–Malliavin 1967 — completeness radius; exact-peak impossibility.**
1. *Citation.* A. Beurling, P. Malliavin, "On the closure of characters and the zeros of entire functions", Acta Math. 118 (1967), 79–93. DOI 10.1007/BF02392477 [^130^]. Modern statements: Seip–Ulanovskii 1997 [^131^]; Koosis [^132^]; Belov–Havin [^133^]. Density computation: Giuliano–Grekos, arXiv:2311.04762 [^134^]; superlinear counting from Riemann–von Mangoldt [^128^].
2. *Theorem (verified against the original).* The closure radius satisfies $\varrho(\Lambda) = \pi A_e(dN_{\Lambda^*})$ (exterior/BM density of the symmetrized counting measure); Theorem II: entire functions of type $\le\pi k$ (Poisson-summable $\log|f|$) vanishing on $\Lambda$ exist iff $k > a := A_e$, and "$\varrho(\Lambda)$ does not change if a finite number of points are removed from or adjoined to $\Lambda$." For superlinear $\Lambda$ ($n(r)\asymp r\log r$), $D_{BM}(\Lambda) = \infty$ unconditionally (Giuliano–Grekos/Koosis direction).
3. *Typed objects.* Discrete real (or strip-bounded) sequences; completeness of exponentials in $L^2(-a,a)$; duality completeness ⟺ no nonzero $PW_a$ function vanishes on $\Lambda$.
4. *Map to strict-peak.* $\Lambda = \{\pm\gamma_n\}$: $D_{BM} = \infty$ ⟹ $\{e^{i\gamma t}\}$ complete in $L^2(-\sigma,\sigma)$ for every $\sigma$, unchanged after deleting $\gamma_0$. An exact peak $f\in PW_\sigma$, $f(\gamma_0)=1$, $f(\gamma)=0$ otherwise, would be a nonzero $PW_\sigma$ function vanishing on $\Lambda\setminus\{\gamma_0\}$ — contradiction.
5. *Step discharged.* **Impossibility of the exact Kronecker-delta peak in any Paley–Wiener space, at any bandwidth — unconditional.**
6. *Unmet hypotheses.* None (discreteness and strip condition hold regardless of RH).
7. *Circularity.* None — uses only the unconditional zero count.
8. *Classification.* `applicable` (impossibility side).
9. *Cheapest test.* None needed; chain Riemann–von Mangoldt ⟹ $D_{BM}=\infty$ ⟹ completeness at all bandwidths is unconditional.

**T-Q4.4 Beurling's sampling theorem + Blank–Ulanovskii Cartwright sets — the quantitative strict-peak obstruction.**
1. *Citation.* A. Beurling, 1966 lecture notes / Collected Works [^135^]; N. Blank, A. Ulanovskii, "On Cartwright's theorem", arXiv:1603.09585 [^136^]; interpolation-side characterization: Ortega-Cerdà–Seip 1999 [^137^].
2. *Theorem.* $\Lambda$ is sampling for the Bernstein space $B_\sigma$ ($\sup_{\mathbb{R}}|f| \le K\sup_\Lambda|f|$) iff it contains a uniformly discrete subset with $D^- > \sigma/\pi$; uniqueness holds iff $\Lambda$ is a Cartwright set (Blank–Ulanovskii characterization).
3. *Typed objects.* Bernstein space $B_\sigma \supset PW_\sigma$; uniformly discrete subsets; lower uniform density.
4. *Map to strict-peak.* $D^-(\{\gamma\}) = \infty$ ⟹ sampling for every $B_\sigma$, and likewise for the punctured set. Hence every candidate obeys $1 = |f(\gamma_0)| \le K\sup_{\gamma\neq\gamma_0}|f(\gamma)|$: **no bandlimited strict peak can be arbitrarily good**; the optimal dip is $1/K$ for the punctured zero set's sampling constant.
5. *Step discharged.* Quantitative obstruction to strict peaks (dip bounded below); the remaining open sub-problem is whether $K(\sigma, \Lambda\setminus\{\gamma_0\}) > 1$ (expected, since $K\to\infty$ along density-$\to\infty$ exhaustions).
6. *Unmet hypotheses.* None for the obstruction direction; no construction.
7. *Circularity.* None.
8. *Classification.* `applicable` (obstruction).
9. *Cheapest test.* Estimate Beurling's sampling constant for a greedy maximal $\delta$-separated subset of Odlyzko's zero tables and track $K$ as $\delta\downarrow 0$; if $K>1$ at the optimal subset, the strict peak is excluded in $B_\sigma$.

**T-Q4.5 Beurling–Malliavin 1962 multiplier theorem — the sole serious construction tool.**
1. *Citation.* A. Beurling, P. Malliavin, "On Fourier transforms of measures with compact support", Acta Math. 107 (1962), 291–309, DOI 10.1007/BF02545792 [^138^]; seventh proof: Mashreghi–Nazarov–Havin 2005/06 [^139^]; de Branges analogs: Belov–Havin [^133^]; Lipschitz habitat: Lyubarskii–Ortega-Cerdà 2014 [^140^].
2. *Theorem.* For Lipschitz $\omega\ge 1$ with $\int \log\omega(x)/(1+x^2)\,dx < \infty$ and every $\varepsilon>0$, there is a nonzero entire $f$ of type $\le\varepsilon$ with $\omega f$ bounded on $\mathbb{R}$ (arrange $\omega|f|\le 1$).
3. *Typed objects.* Majorants; multipliers of arbitrarily small type.
4. *Map to strict-peak.* With $\omega$ growing like $|x-\gamma_0|^{\eta}$ away from $\gamma_0$: $f$ of arbitrarily small type with $|f(\gamma)| \le (1+|\gamma-\gamma_0|)^{-\eta}$ at distant zeros — envelope localization compatible with the Gaussian test class after mollification. The catch: at near-neighbor zeros (gaps $\to 0$, Lehmer pairs) $\omega(\gamma)\approx 1$, so no dip where the obstruction lives; prescribed values at points are not delivered.
5. *Step discharged.* Partial construction: strong localization at $\gamma_0$ with small values in the bulk of the zero set at arbitrarily small bandwidth.
6. *Unmet hypotheses.* No point-value prescription; no strict dip at nearest zeros; compact support rather than Gaussian decay on the Fourier side (combine with mollification).
7. *Circularity.* None.
8. *Classification.* `conditionally applicable` — discharges envelope localization, not the strict peak.
9. *Cheapest test.* Run the MNH construction near the first Lehmer pair $\gamma_{6709}\approx 7005.0629$, $\gamma_{6710}\approx 7005.1006$ (gap $\approx 0.04$): the obstruction is exactly at such pairs.

**T-Q4.6 Conrey–Li 2000 — de Branges' positivity conditions fail for $\xi$ (route killer).**
1. *Citation.* J. B. Conrey, X.-J. Li, Int. Math. Res. Not. 2000, no. 18, 929–935, DOI 10.1155/S1073792800000489, arXiv:math/9812166 [^123^].
2. *Theorems.* Thm 1 (de Branges): for $E(z) = \xi(1-iz)$ (HB unconditionally), positivity $\operatorname{Re}\langle F(z), F(z+i)\rangle_{\mathcal H(E)} \ge 0$ for all $F$ implies the zeros lie on the axis (implies RH). Thm 2 + counterexample: at $F = K(w,\cdot)$ the positivity reduces to a sign condition on $\operatorname{Re}\{\xi'(\rho)\xi(1+\rho)\}$, which **fails at the 34th zero** — so the positivity condition fails unconditionally for $\xi$.
3. *Map to strict-peak/positivity.* The de Branges route "Hilbert-space positivity ⟹ RH" cannot be run; the natural kernel objects lack the required positivity.
4. *Step discharged.* None — authoritative negative assessment (impossibility of the positivity route, not of interpolation).
5. *Circularity.* The disproof itself is unconditional (uses a verified on-line zero).
6. *Classification.* `inapplicable` (hypothesis disproved); essential negative evidence.
7. *Cheapest test.* n/a (settled).

#### (c) Documented near-misses (Q4)

| Near-miss | Reason |
|---|---|
| Cartwright–Levin zero-density theory [^141^][^142^] | `applicable` second impossibility proof for the *exact* peak: bounded exponential-type functions have $n(r)=O(r)$ zeros, while $\Lambda\setminus\{\gamma_0\}$ has $n(r)\asymp r\log r$. Does not touch the strict (nonzero) peak: bounded Cartwright functions can be small on superlinear sets. |
| Landau 1967 interpolation obstruction [^143^]; Ortega-Cerdà–Seip $D^+$ bound [^137^]; complete-interpolation characterization (Lyubarskii–Seip [^144^]; Pavlov [^145^]; Hruščëv–Nikol'skiĭ–Pavlov [^146^]) | `applicable` negative: $D^+(\{\gamma\})=\infty$ and zero separation ⟹ never interpolating; no biorthogonal peak machinery exists at the zeta zeros. |
| Ortega-Cerdà–Seip Fourier frames [^147^] | `applicable` obstruction: $\{\gamma\}$ is sampling but not a finite union of separated sequences, so no frame; coefficient functionals unbounded; $PW_\sigma$ peak with dip $\downarrow$ forces $L^2$-norm blow-up (since $\operatorname{dist}(e^{i\gamma_0 t},\overline{\operatorname{span}}\{e^{i\gamma t}\})=0$ by T-Q4.3). |
| de Branges $\mathcal H(\xi(1-iz))$ orthogonal kernel bases [^148^] | At an on-axis zero $w$, $K(w,w)=0$: under RH every element vanishes at every zeta zero — the strict-peak function cannot live in this space; nodes-on-axis ⟺ RH. `circular`. |
| de Branges 1986/1994 RH programme [^122^] | Positivity hypothesis disproved (Conrey–Li); `inapplicable`. |
| Suzuki $\Theta_\omega$ inner-function criterion [^124^] | Inner property at $\omega<1/2$ ⟺ zero-freeness in $\operatorname{Re}s>1-\omega$; at $\omega\to 0$ exactly RH. `circular`. |
| Suzuki Hamiltonians/integral operators [^125^]; model-space Li norms [^126^]; Carneiro–Chandee–Littmann–Milinovich [^127^] | All assume RH (+simplicity). `circular`. |
| Gonçalves 2017 Hermite interpolation in de Branges spaces [^149^] | Node sequences need lattice-like separation/linear density; impossible at superlinear density (already killed by T-Q4.3). `inapplicable` at $\{\gamma\}$. |
| Lyubarskii–Seip/Pavlov complete interpolating sequences [^144^][^145^] | Require separation + finite density; fail at $\{\gamma\}$. |
| Kadec 1/4 / Avdonin "in the mean" [^150^] | Bounded perturbation of a lattice; $\gamma_n \sim 2\pi n/\log n$ drifts unboundedly. `inapplicable`. |
| Radchenko–Viazovska 2019 [^151^]; Kulikov 2021 [^152^] | Subcritical-density ($\sqrt n$) Fourier interpolation — opposite regime; delineates the criticality threshold. |
| Kulikov–Nazarov–Sodin uniqueness pairs [^153^] | Finite density thresholds; our density is infinite; interpolation formulas live in the borderline/tempered regime, not bandlimited. `inapplicable` for bandlimited peaks. |
| Levinson 1940 [^154^]; Redheffer 1977 [^155^] (complex-node completeness) | RH-free strengthening of T-Q4.3 for sampling at the full complex zeros $\beta+i\gamma$; conclusion unchanged. |
| Poltoratski 2012 (Acta Math. 208, 151–209); Makarov–Poltoratski 2010 (Invent. Math. 180, 443–480) | Measure-level/Toeplitz BM theory; the discrete-set case is already covered by T-Q4.3 without gap structure. |
| Ortega-Cerdà–Seip, $\bar\partial$ multipliers (Rev. Mat. Iberoamericana 18 (2002), 355–377) | Several-variables sampling constructions; 1-D bandlimited case subsumed by T-Q4.5. |
| Lagarias, "Hilbert spaces of entire functions and Dirichlet L-functions" (Springer 2006, 365–377); Lagarias, Ann. Inst. Fourier 56 (2006), 1–52 | RH/GRH-equivalent conditions throughout — `circular`. |
| Vu Kim Tuan / Boumenir PW-sampling item | Could not be traced to a verified bibliographic record; treated as unverified near-miss. |

**Bottom line (Q4).** Exact bandlimited peak interpolation at the zeta ordinates is **unconditionally impossible** (two independent proofs: BM completeness of the punctured system; Cartwright–Levin zero density). Strict bandlimited peaks are quantitatively obstructed (sampling constant; Fourier-frame ill-posedness) but not literally excluded — an open quantitative sub-problem. Unconditional strict-peak interpolants exist only outside the PW class (BRS, Burnol). The RKHS shortcut is circular (nodes on the axis ⟺ RH; kernel degeneracy) or disproved (Conrey–Li). This is acceptance-criterion obstruction (ii) of Section 6.

### 3.5 Q5 — Equivalent heat-flow formulations (Dimension 10)

#### (a) Narrative assessment

The question was whether the de Bruijn–Newman heat parameter and zero-reality property of $H_t(z) = \int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du$ map, by an explicit change of variables, onto $\Theta(t,\xi)$, and whether positivity of $\Theta(t,\cdot)$ corresponds to reality of zeros of $H_{t'}$ for some $t'$. The verified answer (dim10, §4, derived there; no literature source found for the map itself) is the search's **first rigorous obstruction** (insight I3):

**The two Gaussian parameters are Fourier-dual with opposite signs.** The Weil Gaussian $h_{t,\xi}(r) = e^{-t(r-\xi)^2}$ has $u$-space partner $\hat h \propto e^{-u^2/(4t)}e^{-i\xi u}$ (decaying); the de Bruijn evolution multiplies $\Phi(u)$ by the *growing* Gaussian $e^{+t'u^2}$. Formal matching gives $t' = -1/(4t)$: the Weil smoothing is the backward (wrong-sign) heat flow applied to the test function, not the forward flow applied to $\Phi$. The monotonicities are opposite: increasing $t'$ *creates* zero-reality (de Bruijn strip shrinking, width² $\mapsto$ width² $-2t'$); increasing $t$ *exposes* off-line zeros in $\Theta$ (a zero quartet with deviation $b = |\operatorname{Re}\rho - \frac12|>0$ contributes $4e^{tb^2 - t(\xi-a)^2}\cos(2tb(\xi-a))$, detectable once $t \gtrsim \pi/(2b^2)$, numerically verified in dim10 §4.3).

**The only honest correspondence is at the threshold $t' = 0$:**
$$
\Theta(t,\xi)\ge 0\ \ \forall t>0,\ \forall\xi \quad\Longleftrightarrow\quad \mathrm{RH} \quad\Longleftrightarrow\quad H_0\ \text{has only real zeros} \quad\Longleftrightarrow\quad \Lambda \le 0,
$$
and by Rodgers–Tao ($\Lambda \ge 0$ [^42^]) this is $\Lambda = 0$. **No monotone map $t \mapsto t'$ with $t' \neq 0$ can work**: $H_{t'}$ has only real zeros for all $t' \ge 0.22$ unconditionally (Polymath15 [^91^]), so any such equivalence would prove RH. Single-scale positivity $\Theta(t,\cdot)\ge 0$ for all $\xi$ excludes off-line zeros with $b \gtrsim \sqrt{\pi/(2t)}$ — a quantitative weaker-than-RH statement, converging to RH as $t\to\infty$.

What the heat-flow literature *does* supply: the exact threshold structure (Newman's half-line theorem), the mechanism theorems (de Bruijn strip-shrinking; Pólya universal factors), the strongest double-contact analysis anywhere (the zero-repulsion ODE $\partial_t x_k = 2\sum'_{j\neq k} 1/(x_k - x_j)$; Csordas–Smith–Varga's Lehmer-pair collision criterion; Rodgers–Tao's local-equilibrium contradiction), and heat-side escape-to-infinity exclusion (Ki–Kim–Lee: all but finitely many zeros of $H_\lambda$ are real and simple for each $\lambda>0$). None of it transfers to $\Theta$ because of the sign obstruction — but it is the correct model of what the $\Theta$-side theory would have to prove.

**Convention trap (verified, mandatory correction 6).** Ki–Kim–Lee 2009 [^156^] define $\Lambda = 4\lambda^{(0)}$ where $\Xi_\lambda = \int e^{\lambda u^2}\Phi(u)e^{izu}du$: a **factor of 4** against the Rodgers–Tao/Polymath convention $H_t = \int e^{tu^2}\Phi(u)\cos(zu)du$. In KKL, de Bruijn's bound reads $\lambda^{(0)} \le 1/8$ and their main theorem is $\Lambda < 1/2$ in the $\Lambda$-scale (i.e. $\lambda^{(0)} < 1/8$); Newman's 1976 bound $b_0 \ge -1/8$ corresponds to $\Lambda \le 1/2$. Any transcription mixing the two scales is off by 4.

**No peer-reviewed paper writes the Weil explicit formula with Gaussian test as a de Bruijn-type integral** (22+ searches). Closest: Polymath15's effective approximation $H_t(z) \approx \frac18 B_t(z)(f_t(\cdots) + \text{conj})$ with $f_t$ a theta-derived Dirichlet series [^91^]; the Newman–Wu survey places the explicit formula and $H_{f,\lambda}$ side by side [^35^]. 2025–26 non-refereed preprints claiming a "heat-flow ↔ windowed Weil positivity dictionary" are logged as near-misses.

#### (b) Top theorems (9-field schema)

**T-Q5.1 de Bruijn 1950 — strip-shrinking and universal factors.**
1. *Citation.* N. G. de Bruijn, "The roots of trigonometric integrals", Duke Math. J. 17 (1950), 197–226, DOI 10.1215/S0012-7094-50-01720-0 [^10^]; verbatim modern restatement: Newman–Wu survey [^35^].
2. *Theorem (as restated in [^35^], Thms 7 and 13).* For $f(z) = \int F(t)e^{izt}\,dt$ real entire of order $<2$ with $F(t) = O(e^{-|t|^b})$, $b>2$: if the zeros lie in $|\operatorname{Im}z|\le\Delta$, those of the $e^{\lambda t^2}$-evolved transform lie in $|\operatorname{Im}z| \le [\max(\Delta^2 - 2\lambda, 0)]^{1/2}$ — real for $\lambda \ge \Delta^2/2$. Corollary: zeros of $H_0$ lie in $|\operatorname{Im}z|\le 1$ (zero-free region of $\zeta$), hence $\Lambda \le 1/2$.
3. *Typed objects.* Even real transforms of super-exponentially decaying densities; Gaussian-parameter family $\lambda =$ negative heat time.
4. *Map to $\Theta$.* No direct map (sign obstruction). The strip law width² $\mapsto$ width² $-2t'$ is the heat-side dual of the $\Theta$-side detectivity law $b_{\mathrm{detectable}}^2 \approx \pi/(2t)$; formally $t' \leftrightarrow \pi/(4t)$ in magnitude, opposite sign.
5. *Step discharged.* Heat-side escape-to-infinity exclusion: zeros cannot enter the strip from infinity; width² decreases linearly.
6. *Unmet hypotheses.* All verified for $\Phi$ (even, super-exponential decay, order $1<2$); not applicable to $\Theta$'s two-variable positivity.
7. *Circularity.* None (uses only the zero-free region).
8. *Classification.* `applicable` (mechanism theorem for the heat flow); `inapplicable` as a positivity theorem for $\Theta$.
9. *Cheapest test.* n/a.

**T-Q5.2 Newman 1976 — threshold structure.**
1. *Citation.* C. M. Newman, "Fourier transforms with only real zeros", Proc. Amer. Math. Soc. 61 (1976), 245–251, DOI 10.1090/S0002-9939-1976-0434982-5 [^157^]; transcription via Dimitrov–Rusev [^158^].
2. *Theorem (Theorem 3, verbatim substance).* There exists $b_0$ with $-1/8 \le b_0 < \infty$ such that $\Xi_b(z) = \int e^{izt - bt^2}\Phi(t)\,dt$ has only real zeros when $b \le b_0$ but non-real zeros when $b > b_0$. Remark 2: "The Riemann hypothesis is the statement that $b_0 \ge 0$; we make the complementary conjecture that $b_0 \le 0$" (Newman's conjecture, proved by Rodgers–Tao). Class-$\mathcal R$ characterization theorem: even measures all of whose Gaussian smoothings have real-zero transforms are exactly the $\varphi^4$/Laguerre–Pólya-type class $Ke^{-\beta t^2 - \alpha t^4}\prod_j(1 + t^2/a_j^4)\cdot(\text{cosh factors})$.
3. *Typed objects.* Even finite measures with $\int e^{bt^2}\,d\rho < \infty$; entire characteristic functions.
4. *Map to $\Theta$.* Establishes that the good set $\{t : H_t \text{ real zeros}\}$ is a half-line $[\Lambda,\infty)$ — the prerequisite for any threshold formulation.
5. *Step discharged.* Threshold structure underlying the equivalence.
6. *Unmet hypotheses.* None for $\Phi$.
7. *Circularity.* None.
8. *Classification.* `applicable` (structural).
9. *Cheapest test.* n/a.

**T-Q5.3 Csordas–Smith–Varga 1994 — Lehmer-pair collision criterion (double contact, heat side).**
1. *Citation.* G. Csordas, W. Smith, R. S. Varga, "Lehmer pairs of zeros, the de Bruijn–Newman constant $\Lambda$, and the Riemann hypothesis", Constr. Approx. 10 (1994), 107–129, DOI 10.1007/BF01205170 (verified; dim02's BF01212570 is wrong) [^159^]. Restatement: Odlyzko [^160^].
2. *Theorem (Theorem 1, transcribed via Odlyzko).* For a Lehmer pair $\{x_k(0), x_{k+1}(0)\}$ of zeros of $H_0$, define $g_k(0) := \sum'_{j\ne k,k+1}\{1/(x_k - x_j)^2 + 1/(x_{k+1}-x_j)^2\}$. If $g_k(0)\le 0$ then $\Lambda>0$ (RH false); if $g_k(0)>0$, $\lambda_k := [(1 - \frac54\Delta_k^2 g_k(0))^{4/5}-1]/(8g_k(0)) \le \Lambda$. Underlying dynamics: zeros satisfy the repulsion ODE $\partial_t x_k = 2\sum'_{j\neq k} 1/(x_k - x_j)$ under the backward heat equation $\partial_t H_t = -\partial_z^2 H_t$ [^161^].
3. *Typed objects.* Real zeros of $H_0$ ordered; close pairs; $\Delta_k$ normalized gap. Framed "assume RH in the region" — legitimate since $\neg$RH gives $\Lambda>0$ anyway.
4. *Map to $\Theta$.* None direct; the canonical *double-contact* statement: a too-close pair forces a collision (double zero) at some $t<0$, bounding $\Lambda$ below. Zeros leave the axis only via collisions — the heat-side analogue of the double-contact mechanism.
5. *Step discharged.* Heat-side double-contact exclusion/quantification: collisions are the only way zeros leave the axis; collision times estimated from gap data.
6. *Unmet hypotheses.* Verified numerical zero locations (e.g. the Lehmer pair at zeros 6709–6710 gives $\Lambda > -4.379\times 10^{-6}$).
7. *Circularity.* None (numerical zero locations are computed, not assumed on the line; the "assume RH" framing is legitimate casework).
8. *Classification.* `applicable` (heat-side dynamics); `inapplicable` to $\Theta$-positivity directly.
9. *Cheapest test.* n/a.

**T-Q5.4 Ki–Kim–Lee 2009 — escape-to-infinity exclusion, heat side (strongest known form).**
1. *Citation.* H. Ki, Y.-O. Kim, J. Lee, "On the de Bruijn–Newman constant", Adv. Math. 222 (2009), 281–306, DOI 10.1016/j.aim.2009.04.003 [^156^]. Companion: Ki–Kim, J. Anal. Math. 91 (2003), 369–387 (de Bruijn's question on strong universal factors) [^162^].
2. *Theorem (verbatim substance from the published abstract).* With $\lambda^{(0)} := \inf\{\lambda : \Xi_\lambda = \int e^{\lambda u^2}\Phi(u)e^{izu}du \text{ has only real zeros}\}$ and $\Lambda = 4\lambda^{(0)}$ (**factor-of-4 convention vs Rodgers–Tao**): RH ⟺ $\Lambda \le 0$; de Bruijn gives $\Lambda \le 1/2$; the paper proves **all but finitely many zeros of $\Xi_\lambda$ are real and simple for each $\lambda > 0$**, hence $\Lambda < 1/2$.
3. *Typed objects.* Same de Bruijn class; saddle-point asymptotics of $H_\lambda$.
4. *Map to $\Theta$.* None direct (sign obstruction); this is the heat-side statement that off-axis zeros neither accumulate nor drift in from $\infty$.
5. *Step discharged.* Escape-to-infinity exclusion on the heat side: for every $t'>0$ the non-real zeros of $H_{t'}$ are confined and finite in number (non-effective; Polymath15 makes finite regions effective).
6. *Unmet hypotheses.* None (unconditional).
7. *Circularity.* None.
8. *Classification.* `applicable` (heat side); `inapplicable` to $\Theta$.
9. *Cheapest test.* n/a. (Note: no theorem labeled "D4" exists in this literature, despite the task brief's reference; the closest matches are de Bruijn's Theorem 13 and KKL's main theorem.)

**T-Q5.5 Rodgers–Tao 2020 — $\Lambda \ge 0$ (the threshold equals RH).**
1. *Citation.* B. Rodgers, T. Tao, "The de Bruijn–Newman constant is non-negative", Forum Math. Pi 8 (2020), e6, DOI 10.1017/fmp.2020.6, arXiv:1801.05914 [^42^].
2. *Theorem (Theorem 1.1).* $\Lambda \ge 0$. Method: assume $\Lambda<0$, analyze the zero dynamics of $H_t$ on $\Lambda<t\le 0$ (building on Csordas–Smith–Varga), deduce local equilibrium (zeros locally equally spaced), contradicting Montgomery pair correlation.
3. *Map to $\Theta$.* Yields the two-sided statement RH ⟺ $\Lambda = 0$: the heat threshold *is* RH. It gives no $t'>0$ handle on $\Theta$.
4. *Step discharged.* The full heat-flow threshold side of the equivalence; the strongest collision analysis.
5. *Unmet hypotheses.* None (uses proved zero-distribution results).
6. *Circularity.* None.
7. *Classification.* `applicable` as the statement that the $\Theta$-positivity target ($\equiv$ RH) equals $\Lambda \le 0$, hence $\Lambda = 0$.
8. *Cheapest test.* n/a.

**T-Q5.6 Polymath15 2019 — effective heat flow, $\Lambda \le 0.22$.**
1. *Citation.* D. H. J. Polymath, "Effective approximation of heat flow evolution of the Riemann $\xi$ function, and a new upper bound for the de Bruijn–Newman constant", Res. Math. Sci. 6 (2019), Art. 31, DOI 10.1007/s40687-019-0193-1, arXiv:1904.12438 (id verified via arXiv API; dim07's 1810.05120 is an unrelated QCD paper) [^91^].
2. *Theorems.* Theorem 1.4: $\Lambda \le 0.22$ unconditionally (verified RH to height $X/2$ with $X\approx 6\times 10^{10}$ via Platt; barrier method + interval arithmetic). Theorem 1.2: explicit criterion $\Lambda \le t_0 + y_0^2/2$ from final-time clearance plus a barrier region. Effective approximation $H_t(z) \approx \frac18 B_t(z)f_t(\cdots)$ with $f_t$ a theta/Mellin-derived Dirichlet series — **the closest published object to "the explicit formula written as a de Bruijn-type integral"**.
3. *Map to $\Theta$.* The $A_t + B_t$ approximation is the natural bridge object (same Dirichlet series as the prime side), but the correspondence is $H_t$-value ↔ prime sum, not $\Theta$-positivity ↔ zero-reality.
4. *Step discharged.* Makes Ki–Kim–Lee's finiteness effective in finite regions; supplies the bridge object.
5. *Unmet hypotheses.* Hypothesis (i) is verified computation, not RH.
6. *Circularity.* None.
7. *Classification.* `applicable` (heat-side, effective); near-miss for the $\Theta$ bridge.
8. *Cheapest test.* n/a.

#### (c) Documented near-misses (Q5)

| Near-miss | Reason |
|---|---|
| Pólya 1926–27 universal factors and Pólya–Jensen criterion [^163^] | Reality persists under forward heat (monotonicity backbone of the half-line threshold); RH ⟺ hyperbolicity of all Jensen polynomials — `circular` as a proof route, `conditionally applicable` as the correct positivity-analogue template. |
| Griffin–Ono–Rolen–Zagier 2019 [^41^]; effective follow-up [^164^] | Asymptotics of $\zeta^{(2n)}(1/2)$ give hyperbolicity of a density-1 subset of Jensen polynomials per degree and all $d\le 8$; the $d$-uniformity gap is provably the whole difficulty. `inapplicable` to $\Theta$-positivity; evidence machinery only. |
| Gröchenig 2020 (Schoenberg PF functions and $\xi$) [^165^] | RH ⟺ existence of a PF function $\Lambda$ with $1/\Xi_1(s)=\int_0^\infty\Lambda(x)e^{-sx}dx$; conceptual equivalence, `circular` as a route; cf. the certified PF-order-5 failure [^33^]. |
| Csordas–Norfolk–Varga 1986 Turán inequalities [^37^]; Csordas–Varga 1988 [^38^]/1990 [^39^]; Csordas survey [^166^] | Necessary conditions (verified) or infinite hierarchies ⟺ RH; `circular` as proof route, `applicable` as finite necessary conditions. |
| Newman–Wu survey [^35^] | Baseline reference for all statements/conventions (de Bruijn Thms 7/8/13, Newman Thms 9–10, KKL Thm 14 verbatim); not itself a new tool. `applicable` as reference. |
| Cardon 2005 [^167^] (+ Cardon–Nielsen, Cardon–de Gaston sequels) | de Bruijn–Newman constants for general kernels; structural, kernel-flexible; no explicit-formula link. |
| Odlyzko 2000 [^160^] | Numerical improvement of $\Lambda$ bounds via CSV machinery; numerical, not a global theorem for $\Theta$. |
| Ismail 2026, "Heat-flow lifetimes and windowed Weil positivity: a quantitative dictionary" (ResearchGate) | Claims exactly the mission's dictionary, but non-refereed, full text not retrievable; unverified. |
| Perišić 2025, "The de Bruijn–Newman constant from the Helson–Blur" (Zenodo) | Assumes RH inside a private platform; circular by construction; files restricted. |
| Planat 2026 and sequels [^168^] | A *different* positivity problem (modulus-growth criterion RH ⟺ $\partial_y|D(x+iy)|^2>0$); structurally adjacent; non-peer-reviewed; its own bridge admitted open. |
| "Certified PF-order-5 failure of the de Bruijn–Newman kernel", arXiv:2602.20313 (2026) [^33^] | Relevant negative evidence for PF-based positivity routes; not a positivity theorem; non-refereed. |
| Gershon, "The De Bruijn–Newman Constant Is Zero" (preprints.org 202604.1513) | Unverified claimed RH proof; excluded per protocol. |
| Csordas–Yang, "Finite Fourier transforms and the zeros of the Riemann xi-function" | Kernel criteria without the explicit-formula link. |
| Burnol's distributional explicit formulas (arXiv:math/9810169, math/9809119, math/0101068) | Propagator forms of the explicit formula; no de Bruijn connection. |

**Bottom line (Q5).** The equivalence $\Theta$-positivity ⟺ RH ⟺ $H_0$ real zeros ⟺ $\Lambda=0$ is exact but passes through RH — circular as a proof route, exact as a dictionary. The requested map to a *nonzero* heat parameter is rigorously obstructed (Fourier-dual opposite sign, $t' = -1/(4t)$; insight I3). The heat-flow literature supplies the model for the $\Theta$-side theory: threshold structure (Newman), mechanism (de Bruijn), collision/double-contact analysis (CSV, Rodgers–Tao), and escape-to-infinity exclusion (KKL) — all non-circular, none transferable to $\Theta$ by any located theorem.

## 4. Circularity quarantine (insight I7)

The following results are **RH-equivalent or assume zero locations**. They are legitimate as benchmarks, dictionaries, and heuristics — and several are the strongest statements in their area — but must not be used as proof tools for the $\Theta$-positivity target. (Conditional fragments that are unconditional are listed in the second table.)

| Result | What it asserts | Circularity mechanism |
|---|---|---|
| Weil 1952 positivity criterion [^65^]; Weil 1972 local form [^106^] | RH ⟺ Weil positivity on all admissible tests | By definition the target |
| Bombieri 2000, Theorem 2 [^49^]; Bombieri–Lagarias 1999 [^69^]; Omar–Mazhouda 2007 [^70^] | RH ⟺ $T[f*f^*]\ge 0$; restricted countable families | RH-equivalent by construction |
| Li criterion [^68^] ($\lambda_n\ge 0$) | RH ⟺ positivity of the Li sequence | Encodes all zeros by construction |
| Turán's criterion [^50^][^51^] | Uniform-in-$\xi$ estimates stronger than Korobov–Vinogradov ⟹ zero-free regions / quasi-RH | The *estimate itself* is RH-strength |
| Wintner 1935/1941/1943 [^66^][^67^] | Zeros-side series is B²-almost-periodic ⟺ RH | Converse theorem: the property is RH |
| Katkova 2007 multiply-positive sequences [^40^]; Csordas–Norfolk–Varga 1986/1988/1990 Turán/Laguerre–Pólya hierarchies [^37^][^38^][^39^]; GORZ 2019 full Jensen hierarchy [^41^] | "For all $k$"/full-hierarchy statements ⟺ RH | Each full hierarchy is RH-equivalent |
| Rodgers–Tao $\Lambda\ge 0$ as a positivity proof [^42^] | RH ⟺ $\Lambda\le 0$ and $\Lambda\ge 0$ ⟹ $\Lambda=0$ | The equivalence passes through RH |
| Lagarias 1999 [^109^] ($\operatorname{Re}(\xi'/\xi)>0$) | Pointwise positivity ⟺ RH | RH-equivalent pointwise criterion |
| Connes 1999 global trace-formula positivity [^110^] | Global positivity ⟺ RH | Global version is RH-equivalent (semilocal pieces are not — see below) |
| Suzuki CJM 2025 Hilbert space from the Weil distribution [^107^] | de Branges completion of the Weil form | Construction assumes RH |
| Suzuki $\Theta_\omega$ inner-function criterion at the critical parameter [^124^] | Inner property at $\omega\to 0$ ⟺ RH | RH-equivalent |
| de Branges $\mathcal H(\xi(1-iz))$ node scheme [^148^][^122^]; Suzuki Hamiltonians/model spaces [^125^][^126^]; Carneiro–Chandee–Littmann–Milinovich [^127^]; Burnol zero-attached complete systems on the spectral side [^114^]; Lagarias Hilbert-space RH equivalences (Springer 2006 chapter; Ann. Inst. Fourier 56 (2006), 1–52) | Hilbert-space/realization criteria | Assume RH (nodes on the axis; zero locations) or are disproved (Conrey–Li [^123^]) |
| Karlin oscillation theorem in the strong form applied to $\Theta$ [^8^][^9^] | One-signed unsmoothed Weil data ⟹ no zeros of $\Theta$ at all | The hypothesis $S^-(\Theta(0^+,\cdot))=0$ is plausibly RH-equivalent |
| Bombieri–Hejhal 1995 [^111^] | Zero statistics of linear combinations of Euler products | Assumes GRH + density hypothesis; output not positivity |
| Yoshida 1992 Prop. 1 / Thm 2 [^71^]; Poitou–Odlyzko trick if used with a strip-signed transform | RH-equivalences / engineered sign conditions | Equivalences, not tools |
| 2025–26 claimed RH proofs/dictionaries (Perišić; Gershon; Ismail; Planat sequels [^168^]) | Various | Non-refereed; assume or claim RH; excluded per protocol |

**Usable unconditional tools** (confirmed non-circular by construction of their hypotheses — no zero-location input): Widder 1944 [^1^]; Angenent 1988 [^2^]; Lou 2019 [^3^]; backward uniqueness (Lions–Malgrange [^4^], ESS [^5^][^6^], Dardé–Ervedoza [^7^]); Chen SUCP [^34^]; Schoenberg/Karlin/Kwaśnicki variation-diminishing weak form [^14^][^15^][^8^][^16^]; Kronecker–Bohr almost-periodicity [^43^][^44^][^45^]; Lagarias Theorem 5.1 [^47^]; Bombieri Theorem 12 and variational attainment [^49^]; Yoshida Theorem 1 and Lemmas 2–5 [^71^]; Connes–Consani Corollary 2.3/Theorem 6.11/Propositions 2.1–2.3 [^48^][^102^]; Suzuki Corollary 1.2/form closability [^92^][^93^]; Barner admissibility [^98^]; explicit $\zeta'/\zeta$ bounds [^53^][^54^][^55^]; omega theorems [^57^][^58^][^59^][^60^]; zero-density estimates [^83^]–[^88^]; Beurling–Malliavin [^130^][^138^]; Cartwright–Levin [^141^]; Landau [^143^]; Ortega-Cerdà–Seip [^137^][^147^]; BRS construction [^121^]; Burnol's Sonine-space systems [^114^]; de Bruijn 1950 [^10^]; Newman 1976 [^157^]; CSV 1994 [^159^]; KKL 2009 [^156^]; Polymath15 [^91^]; Jacobi/theta uniform positivity [^61^][^62^][^63^][^64^]; Beurling–Selberg extremals [^116^][^117^][^118^]; Poitou–Odlyzko unconditional strip trick [^104^][^105^].

## 5. Cross-dimension insights (I1–I8)

**I1. Task (a) is nearly settled by classical parabolic theory (Dims 01–03).** Angenent Theorem B (numbering corrected: strict zero-number drop at multiple zeros) + Widder 1944 (positive heat solutions are strictly positive unless $\equiv 0$) + Escauriaza–Seregin–Šverák backward uniqueness jointly reduce double-contact exclusion to one structural check: $\partial_t\Theta = c\,\partial_{\xi\xi}\Theta$ with Tychonoff-class growth. No candidate on this route carries an RH-equivalent hypothesis. Bounded-interval formulations entangle (a) with boundary control on windows $[-L,L]$. *Confidence: high.*

**I2. Task (b) is settled at fixed $t>0$; the hard regime is $t\to 0^+$ (Dims 04–05).** $K_{\mathrm{pr}}$ is Bohr almost-periodic; the corrected sharp infimum is $\min_\chi \sum_n a_n\operatorname{Re}\chi(n)$ over completely multiplicative unimodular $\chi$ (verifier refuted the naive $-\sum a_n$; counterexample $\min[\cos(\xi\log 2)+\cos(\xi\log 4)] = -9/8 \neq -2$). Negative values occur on relatively dense sets; the pole term $2e^{t/8}\cosh(\xi/2)$ dominates at fixed $t$. The uniform $t\to 0^+$ question is not covered by any located theorem. *Confidence: high (with corrected constant).*

**I3. The de Bruijn–Newman heat flow does not map to $\Theta(t,\xi)$ (Dim 10, verifier item 13).** $\hat h_{t,\xi}(u) = \sqrt{\pi/t}\,e^{-u^2/(4t)}e^{-i\xi u}$ decays; de Bruijn multiplies by growing $e^{+t'u^2}$; formal matching forces $t' = -1/(4t) < 0$ — the backward, zero-destroying direction. Only $t'=0$ corresponds ($\Theta$-positivity $\forall t$ ⟺ RH ⟺ $\Lambda\le 0$, and $\Lambda=0$ by Rodgers–Tao); any equivalence at $t'>0$ would falsely prove RH given Polymath15's $\Lambda\le 0.22$. Nuance: $e^{t'u^2}\hat h$ stays integrable for $t'<1/(4t)$, so a small-forward map exists at $L^1/L^2$ level — the obstruction is the direction and the function-class mismatch. *Confidence: high.*

**I4. The Weil quadratic functional is structurally $\xi$-blind (Dims 04, 06, 07).** All rigorous quadratic-form positivity statements depend only on $|\hat g|^2$; translation multiplies $\hat g$ by $e^{i\xi\cdot}$, and on autocorrelations $\gamma_{t,\xi}*\tilde\gamma_{t,\xi} = \gamma_{2t,0}$, collapsing the two-parameter family to one parameter. $\xi$-information survives only in the *linear* evaluation $\Theta(t,\xi) = W(\gamma_{t,\xi})$. No published quadratic-form theorem can discharge the pointwise-in-$\xi$ tasks directly. *Confidence: high.*

**I5. Strict-peak interpolation: unconditional impossibility in PW classes; existence outside them (Dims 08–09).** Superlinear zero counting ⟹ infinite Beurling–Malliavin density, zero separation ⟹ not interpolating for any $PW_\sigma$; exact bandlimited peak interpolation is unconditionally impossible (BM completeness + Cartwright–Levin, two independent routes). BRS 2023 construct value-1-at-one-zero interpolants unconditionally in non-bandlimited strip classes. The strict bandlimited peak is quantitatively obstructed (dip $\ge 1/K$, $K$ = sampling constant of the punctured zero set) and its existence reduces to a sampling-constant estimate — apparently open. *Confidence: high.*

**I6. Promotion route (Gaussian tests → full Weil criterion): machinery exists, one density gap (Dims 06–07).** Suzuki 2026 Corollary 1.2 + Connes–Consani 2023 Proposition 2.1 give: the windowed Weil form is lower bounded, lower semicontinuous, and positivity on a form-norm-dense subset suffices per window. Missing step: form-norm density of truncated shifted/dilated Gaussians in the Friedrichs form domain — Fourier-side, density in $L^2((1+\log^+|z|)\,dz)$ among type-$\le a$ entire functions; numerically decidable per window. Zhu 2026 argues window positivity alone cannot reach RH without extra input. *Confidence: high.*

**I7. Circularity quarantine (cross-dimension, confirmed).** The quarantine and usable-tool lists are Section 4. *Confidence: high.*

**I8. Cheapest concrete tests to close the remaining gaps (aggregated).**
- **T1.** Verify $\partial_t\Theta = \partial_{\xi\xi}\Theta$ termwise from the completed explicit formula → unlocks Widder + Angenent + ESS for task (a). [Dims 01–03]
- **T2.** Form-norm density of truncated shifted Gaussians in the windowed form domain → promotion route per window. [Dim 07]
- **T3.** Exponential type of the BRS interpolant $V_{\rho_0,0}$ → settles feasibility of unconditional strict-peak interpolation. [Dim 08]
- **T4.** Growth comparison $K_{\mathrm{end}} + K_\Gamma$ vs the $\ell^1$-norm/corrected infimum of the prime coefficients, uniform as $t\to 0^+$ → settles task (b) uniformity. [Dims 04–05]

## 6. Acceptance-criterion verdict

**(1) Verified theorem excluding finite double contact or escape to infinity — PARTIAL.** Escape-to-infinity at each fixed $t>0$ is excluded by verified unconditional results: corrected Kronecker–Bohr almost-periodicity (T-Q2.1: sharp prime-sum infimum over completely multiplicative characters, negative dips on relatively dense sets) plus exponential pole-term dominance $2e^{t/8}\cosh(\xi/2)$. Finite double contact is excluded **modulo the single structural check** $\partial_t\Theta = \partial_{\xi\xi}\Theta$ (plus Tychonoff growth): then Widder's representation theorem (T-Q1.1) or Angenent's Theorem B (T-Q1.2, numbering corrected) with backward uniqueness (T-Q1.4) and strong unique continuation (Chen, near-miss row below) jointly forbid the first-violation contact. No located theorem discharges the **uniform $t\to 0^+$ regime**, which remains the genuinely open core.

**(2) Reduction to a strictly smaller testable condition — YES.** The problem reduces to four concrete, independently checkable conditions T1–T4 (insight I8, listed in Section 5): the termwise heat-equation check (T1); form-norm density of truncated shifted Gaussians per window (T2, numerically decidable); the exponential type of the BRS interpolant (T3); and the uniform-in-$t$ growth comparison between $K_{\mathrm{end}}+K_\Gamma$ and the corrected prime-sum infimum (T4, quadrature-decidable on a $t$-grid).

**(3) Rigorous obstruction — YES, on two routes.** (i) The de Bruijn–Newman heat flow does not map to $\Theta(t,\xi)$: the Weil Gaussian is Fourier-dual with the opposite sign, $t' = -1/(4t)$; the only honest correspondence is the threshold $t'=0$, i.e. RH itself, and any $t'>0$ equivalence would falsely prove RH given $\Lambda\le 0.22$ (Polymath15) — insight I3, verified by direct Fourier computation. (ii) Exact bandlimited strict-peak interpolation at the zeta ordinates is **unconditionally impossible**: infinite Beurling–Malliavin density (completeness of the punctured exponential system at every bandwidth) and Cartwright–Levin zero-density bounds give two independent proofs; the strict (nonzero) peak is quantitatively obstructed via sampling constants (dip $\ge 1/K$) and Fourier-frame ill-posedness — insight I5.

**(4) Documented negative results and near-misses — YES.** Catalogued per question in Sections 3.1(c)–3.5(c): the strong maximum principle and Harnack inequalities are vacuous/circular for signed data; nodal-set measure estimates do not exclude contacts; the Karlin oscillation strong form has an RH-equivalent hypothesis; the Pólya-frequency route for $\Theta$ is blocked at PF order 5 (certified); Turán's criterion proves uniform-in-$\xi$ prime-sum estimates beyond Korobov–Vinogradov strength are RH-strength; all global Weil-positivity criteria are RH-equivalent; de Branges' positivity conditions fail unconditionally for $\xi$ (Conrey–Li, at the 34th zero); the $\mathcal H(\xi(1-iz))$ reproducing kernel degenerates at on-axis zeros; the Gaussian family is not known to be positivity-detecting (a genuine literature gap, documented by exhaustive search in dims 06–07); and the claimed 2025–26 heat-flow dictionaries are unverified or circular.

**Summary classification tally** (29 full-schema theorem entries, Sections 3.1–3.5; primary classification where an entry is mixed):

| Classification | Count | Entries |
|---|---|---|
| `applicable` | 13 | T-Q1.5 (weak form); T-Q2.1; T-Q3.2 (window regime); T-Q4.1, T-Q4.2, T-Q4.3, T-Q4.4; T-Q5.1–T-Q5.6 (heat-flow side) |
| `conditionally applicable` | 10 | T-Q1.1, T-Q1.2, T-Q1.3, T-Q1.4; T-Q2.2, T-Q2.3, T-Q2.4; T-Q3.4, T-Q3.5; T-Q4.5 |
| `inapplicable` | 2 | T-Q3.7 (verbatim to $\Theta$); T-Q4.6 (hypothesis disproved by Conrey–Li) |
| `circular` | 4 | T-Q2.5 (as a bound); T-Q3.1; T-Q3.3 (Theorem 2 and countable reduction; its variational-attainment fragment is `conditionally applicable`); T-Q3.6 |

In addition, 12 demoted entries documented in the near-miss tables carry explicit classifications: Chen's SUCP and de Bruijn's mechanism (Q1); explicit $\zeta'/\zeta$ bounds, omega theorems, the Jacobi model (Q2); Bombieri 2003 (Q3); Cartwright–Levin, the Landau/interpolation obstructions, Fourier frames (Q4); Pólya–Jensen, GORZ, Gröchenig (Q5). Of these: 6 are `applicable` as obstruction/infrastructure results, 4 `conditionally applicable`, and 3 are `circular` or quarantined as RH routes (Pólya–Jensen full hierarchy, GORZ, Gröchenig), with GORZ additionally `inapplicable` to $\Theta$-positivity proper.

## 7. References

[^1^] D. V. Widder, "Positive temperatures on an infinite rod", Trans. Amer. Math. Soc. 55 (1944), no. 1, 85–95. DOI 10.1090/S0002-9947-1944-0009795-2 (verified; replaces erroneous 0009704-9). JSTOR 1990141

[^2^] S. B. Angenent, "The zero set of a solution of a parabolic equation", J. Reine Angew. Math. 390 (1988), 79–96. DOI 10.1515/crll.1988.390.79. EuDML 153060

[^3^] B. Lou, "The zero number diminishing property under general boundary conditions", Appl. Math. Lett. 95 (2019), 41–47. DOI 10.1016/j.aml.2019.03.016 (journal data corrected per verification). arXiv:1809.00309..00309

[^4^] J.-L. Lions, B. Malgrange, "Sur l'unicité rétrograde dans les problèmes mixtes paraboliques", Math. Scand. 8 (1960), 277–286. DOI 10.7146/math.scand.a-10602.

[^5^] L. Escauriaza, G. Seregin, V. Šverák, "Backward uniqueness for parabolic equations", Arch. Ration. Mech. Anal. 169 (2003), 147–157. DOI 10.1007/s00205-003-0263-8.

[^6^] L. Escauriaza, G. Seregin, V. Šverák, "Backward uniqueness for the heat operator in a half-space", Algebra i Analiz 15 (2003), 201–214 = St. Petersburg Math. J. 15 (2004), 139–148.

[^7^] J. Dardé, S. Ervedoza, "Backward uniqueness results for some parabolic equations in an infinite rod", Math. Control Relat. Fields 9 (2019), 673–696. DOI 10.3934/mcrf.2019046.

[^8^] S. Karlin, Total Positivity, Vol. I, Stanford University Press, 1968, Ch. 5.

[^9^] S. Karlin, Z. Ziegler, "Chebyshevian spline functions", SIAM J. Numer. Anal. 3 (1966), 514–543. DOI 10.1137/0703043.

[^10^] N. G. de Bruijn, "The roots of trigonometric integrals", Duke Math. J. 17 (1950), 197–226. DOI 10.1215/S0012-7094-50-01720-0.

[^11^] D. V. Widder, The Heat Equation, Academic Press, 1975, Ch. VIII.

[^12^] H. Matano, "Nonincrease of the lap-number of a solution for a one-dimensional semilinear parabolic equation", J. Fac. Sci. Univ. Tokyo Sect. IA Math. 29 (1982), 401–441. https://repository.dl.itc.u-tokyo.ac.jp/records/39956

[^13^] K. Nickel, "Gestaltaussagen über Lösungen parabolischer Differentialgleichungen", J. Reine Angew. Math. 211 (1962), 78–94. DOI 10.1515/crll.1962.211.78.

[^14^] I. J. Schoenberg, "On Pólya frequency functions. II. Variation-diminishing integral operators of the convolution type", Acta Sci. Math. (Szeged) 12 (1950), 97–106; résumé Proc. Natl. Acad. Sci. USA 34 (1948), 164–169. DOI 10.1073/pnas.34.4.164.

[^15^] I. J. Schoenberg, "On Pólya frequency functions. I. The totally positive functions and their Laplace transforms", J. Analyse Math. 1 (1951), 331–374. DOI 10.1007/BF02790092.

[^16^] M. Kwaśnicki, "A new class of bell-shaped functions", Trans. Amer. Math. Soc. 373 (2020), 2255–2280 (pages per verification). DOI 10.1090/tran/7825. arXiv:1710.11023..11023

[^17^] I. J. Schoenberg, A. Whitney, "On Pólya frequency functions. III", Trans. Amer. Math. Soc. 74 (1953), 246–259. DOI 10.1090/S0002-9947-1953-0055298-4.

[^18^] L. Nirenberg, "A strong maximum principle for parabolic equations", Comm. Pure Appl. Math. 6 (1953), 167–177. DOI 10.1002/cpa.3160060202.

[^19^] A. Friedman, "Remarks on the maximum principle for parabolic equations and its applications", Pacific J. Math. 8 (1958), 201–211. DOI 10.2140/pjm.1958.8.201.

[^20^] J. Moser, "A Harnack inequality for parabolic differential equations", Comm. Pure Appl. Math. 17 (1964), 101–134. DOI 10.1002/cpa.3160170106.

[^21^] P. Li, S.-T. Yau, "On the parabolic kernel of the Schrödinger operator", Acta Math. 156 (1986), 153–201. DOI 10.1007/BF02399203.

[^22^] D. G. Aronson, "Non-negative solutions of linear parabolic equations", Ann. Scuola Norm. Sup. Pisa 22 (1968), 607–694.

[^23^] D. G. Aronson, "Bounds for the fundamental solution of a parabolic equation", Bull. Amer. Math. Soc. 73 (1967), 890–896. DOI 10.1090/S0002-9904-1967-11830-5.

[^24^] F.-H. Lin, "Nodal sets of solutions of elliptic and parabolic equations", Comm. Pure Appl. Math. 44 (1991), 287–308. DOI 10.1002/cpa.3160440303.

[^25^] Q. Han, F.-H. Lin, "Nodal sets of solutions of parabolic equations II", Comm. Pure Appl. Math. 47 (1994), 1219–1238. DOI 10.1002/cpa.3160470904.

[^26^] M. Lees, M. H. Protter, "Unique continuation for parabolic differential equations and inequalities", Duke Math. J. 28 (1961), 369–382. DOI 10.1215/S0012-7094-61-02834-4.

[^27^] Y. Giga, K. Inui, A. Mahalov, S. Matsui, "Navier–Stokes equations in a rotating frame in R3 with initial data nondecreasing at infinity", Hokkaido Math. J. 35 (2006), 321–364.

[^28^] P. Cannone, G. Karch, "Smooth or singular solutions to the Navier–Stokes system?", J. Differential Equations 197 (2004), 247–274. DOI 10.1016/j.jde.2003.10.009.

[^29^] A. L. Yuille, T. A. Poggio, "Scaling theorems for zero crossings", IEEE Trans. Pattern Anal. Mach. Intell. 8 (1986), 15–25. DOI 10.1109/TPAMI.1986.4767748.

[^30^] P. Bérard, B. Helffer, "Sturm's theorem on zeros of linear combinations of eigenfunctions", Expo. Math. 38 (2020), 27–50. DOI 10.1016/j.exmath.2018.10.002. arXiv:1706.08247.

[^31^] C. Sturm, "Mémoire sur les équations différentielles linéaires du second ordre", J. Math. Pures Appl. 1 (1836), 106–186.

[^32^] F. Lin, Z. Zhang, "Liouville theorems of parabolic equations on the upper half space", Comm. Pure Appl. Math. 72 (2019), 2006–2028. arXiv:1712.04091.

[^33^] M. Michałowski (et al.), preprint on failure of PF order 5 for zeta kernels, arXiv:2602.20313 (2026)..20313

[^34^] X.-Y. Chen, "A strong unique continuation theorem for parabolic equations", Math. Ann. 311 (1998), 603–630. DOI 10.1007/s002080050202.

[^35^] C. M. Newman, W. Wu, "Constants of de Bruijn–Newman type in analytic number theory and statistical physics", Bull. Amer. Math. Soc. 57 (2020), 595–614. DOI 10.1090/bull/1668. arXiv:1901.06596.

[^36^] H. Ki, Y.-O. Kim, "On the number of nonreal zeros of real entire functions and the Fourier–Pólya conjecture", Duke Math. J. 104 (2000), 45–73. DOI 10.1215/S0012-7094-00-10413-9.

[^37^] G. Csordas, T. S. Norfolk, R. S. Varga, "The Riemann hypothesis and the Turán inequalities", Trans. Amer. Math. Soc. 296 (1986), 521–541. DOI 10.1090/S0002-9947-1986-0846596-X.

[^38^] G. Csordas, R. S. Varga, "Moment inequalities and the Riemann hypothesis", Constr. Approx. 4 (1988), 175–198. DOI 10.1007/BF02075455.

[^39^] G. Csordas, R. S. Varga, "Integral transforms and the Laguerre–Pólya class", Adv. in Appl. Math. 11 (1990), 328–357.

[^40^] O. Katkova, "Multiple positivity and the Riemann zeta-function", Comput. Methods Funct. Theory 7 (2007), 13–31. DOI 10.1007/BF03321628. arXiv:math/0505174.

[^41^] A. Griffin, K. Ono, L. Rolen, D. Zagier, "Jensen polynomials for the Riemann zeta function and other sequences", Proc. Natl. Acad. Sci. USA 116 (2019), 11103–11110. DOI 10.1073/pnas.1902572116. arXiv:1902.07321.

[^42^] B. Rodgers, T. Tao, "The de Bruijn–Newman constant is non-negative", Forum Math. Pi 8 (2020), e6. DOI 10.1017/fmp.2020.6. arXiv:1801.05914.

[^43^] T. M. Apostol, Modular Functions and Dirichlet Series in Number Theory, 2nd ed., GTM 41, Springer, 1990, Thm 7.11. DOI 10.1007/978-1-4612-0999-7.

[^44^] H. Bohr, "Zur Theorie der allgemeinen Dirichletschen Reihen", Math. Ann. 79 (1918), 136–156. DOI 10.1007/BF01457178 (corrected per verification).

[^45^] H. Bohr, Almost Periodic Functions, Chelsea, New York, 1947.

[^46^] A. Defant, I. Schoolmann, "On Bohr's theorem for general Dirichlet series", Math. Nachr. 293 (2020), 1591–1612. arXiv:1812.04925.

[^47^] J. C. Lagarias, "Li coefficients for automorphic L-functions", Ann. Inst. Fourier (Grenoble) 57 (2007), no. 5, 1689–1740. DOI 10.5802/aif.2311.

[^48^] A. Connes, C. Consani, "Weil positivity and trace formula, the archimedean place", Selecta Math. (N.S.) 27 (2021), Paper No. 77. DOI 10.1007/s00029-021-00689-4. arXiv:2006.13771.

[^49^] E. Bombieri, "Remarks on Weil's quadratic functional in the theory of prime numbers, I", Atti Accad. Naz. Lincei Rend. Lincei (9) Mat. Appl. 11 (2000), 183–233. EUDML doc 252338

[^50^] P. Turán, "On some approximative Dirichlet-polynomials in the theory of the zeta-function of Riemann", Danske Vid. Selsk. Mat.-Fys. Medd. 24 (1948), no. 17.

[^51^] P. Turán, On a New Method of Analysis and Its Applications, Wiley-Interscience, 1984.

[^52^] G. Halász, "The number-theoretic work of Paul Turán", Acta Arith. 37 (1980), 9–31. https://matwbn.icm.edu.pl/ksiazki/aa/aa37/aa3713.pdf

[^53^] T. Trudgian, "Explicit bounds on the logarithmic derivative and the reciprocal of the Riemann zeta-function", Funct. Approx. Comment. Math. 52 (2015), 253–261. DOI 10.7169/facm/2015.52.2.5.

[^54^] M. Cully-Hugill, N. Leong, "Explicit estimates for the Riemann zeta function close to the 1-line", arXiv:2312.09412 (2023).

[^55^] N. Leong, "Explicit estimates for the logarithmic derivative and the reciprocal of the Riemann zeta function", arXiv:2405.04869 (2024) — sole author (attribution corrected per verification)..04869

[^56^] A. Yang, "Explicit bounds on ζ(s) in the critical strip and a zero-free region", J. Math. Anal. Appl. 534 (2024), 128124. DOI 10.1016/j.jmaa.2024.128124.

[^57^] D. Yang, "Omega theorems for logarithmic derivatives of zeta and L-functions", arXiv:2311.16371 (2023).

[^58^] Z. Li, S. Zhao, "Omega theorems for logarithmic derivatives of zeta and L-functions near the 1-line", arXiv:2404.17250 (2024).

[^59^] C. Aistleitner, K. Mahatab, M. Munsch, "Extreme values of the Riemann zeta function on the 1-line", Int. Math. Res. Not. 2019, no. 22, 6924–6932. DOI 10.1093/imrn/rnx331.

[^60^] A. Bondarenko, K. Seip, "Large greatest common divisor sums and extreme values of the Riemann zeta function", Duke Math. J. 166 (2017), 1685–1701. DOI 10.1215/00127094-0000005X.

[^61^] H. L. Montgomery, "Minimal theta functions", Glasgow Math. J. 30 (1988), 75–85. DOI 10.1017/S0017089500007042.

[^62^] M. Faulhuber, S. Steinerberger, "Optimal Gabor frame bounds for separable lattices and estimates for Jacobi theta functions", J. Math. Anal. Appl. 445 (2017), 407–422. DOI 10.1016/j.jmaa.2016.07.074.

[^63^] A. J. E. M. Janssen, "Some Weyl–Heisenberg frame bound calculations", Indag. Math. 7 (1996), 165–183.

[^64^] P. Biane, J. Pitman, M. Yor, "Probability laws related to the Jacobi theta and Riemann zeta functions", Bull. Amer. Math. Soc. 38 (2001), 435–465. DOI 10.1090/S0273-0979-01-00912-0.

[^65^] A. Weil, "Sur les 'formules explicites' de la théorie des nombres premiers", Comm. Sém. Math. Univ. Lund, Tome Suppl. (M. Riesz volume), 1952, 252–265; Œuvres II, 48–62.

[^66^] A. Wintner, "On the distribution function of the remainder term of the prime number theorem", Amer. J. Math. 63 (1941), 233–248. DOI 10.2307/2371519; companion: Amer. J. Math. 57 (1935), 534–538, DOI 10.2307/2371183.

[^67^] A. Wintner, "Riemann's hypothesis and harmonic analysis", Duke Math. J. 10 (1943), 99–105. DOI 10.1215/S0012-7094-43-01010-5.

[^68^] X.-J. Li, "The positivity of a sequence of numbers and the Riemann hypothesis", J. Number Theory 65 (1997), 325–333. DOI 10.1006/jnth.1997.2137.

[^69^] E. Bombieri, J. C. Lagarias, "Complements to Li's criterion for the Riemann hypothesis", J. Number Theory 77 (1999), 274–287. DOI 10.1006/jnth.1999.2392.

[^70^] S. Omar, K. Mazhouda, "Le critère de Li et l'hypothèse de Riemann pour la classe de Selberg", J. Number Theory 125 (2007), 50–58.

[^71^] H. Yoshida, "On Hermitian forms attached to zeta functions", in Zeta Functions in Geometry (Tokyo, 1990), Adv. Stud. Pure Math. 21, Kinokuniya, 1992, 281–325. DOI 10.2969/aspm/02110281.

[^72^] W. H. Young, "On the Fourier series of bounded functions", Proc. London Math. Soc. 11 (1913), 357–366.

[^73^] L. Vietoris, "Über das Vorzeichen gewisser trigonometrischer Summen", Sitzungsber. Österr. Akad. Wiss. 167 (1958), 125–135.

[^74^] G. Brown, F. Dai, K. Wang, "Extensions of Vietoris's inequalities", Ramanujan J. 14 (2007), 471–505.

[^75^] O. Katkova, T. Lobova, A. Vishnyakova, "On power series having sections with only real zeros", Comput. Methods Funct. Theory 3 (2003), 425–441.

[^76^] P. Turán, "On the remainder-term of the prime-number formula. I", Acta Math. Acad. Sci. Hungar. 1 (1950), 48–63. DOI 10.1007/BF02022552.

[^77^] S. Knapowski, P. Turán, "Comparative prime-number theory I–VIII", Acta Math. Acad. Sci. Hungar. 13–14 (1962–1963).

[^78^] J. Pintz, "On the remainder term of the prime number formula and the zeros of Riemann's zeta function", in Number Theory Noordwijkerhout 1983, LNM 1068, Springer, 1984, 186–197. DOI 10.1007/BFb0099450.

[^79^] E. Landau, "Über die Nullstellen der Zetafunktion", Math. Ann. 71 (1912), 548–564. DOI 10.1007/BF01456856.

[^80^] S. M. Gonek, "An explicit formula of Landau and its applications to the theory of the zeta function", in The Rademacher Legacy to Mathematics, Contemp. Math. 143, AMS, 1993, 395–413. DOI 10.1090/conm/143.

[^81^] F. Aryan, "On an extension of the Landau–Gonek formula", J. Number Theory 233 (2022), 389–404. arXiv:1902.05473.

[^82^] H. L. Montgomery, R. C. Vaughan, Multiplicative Number Theory I: Classical Theory, Cambridge Stud. Adv. Math. 97, CUP, 2007, p. 410.

[^83^] A. E. Ingham, "On the estimation of N(σ,T)", Quart. J. Math. Oxford 11 (1940), 291–292. DOI 10.1093/qmath/os-11.1.291.

[^84^] M. N. Huxley, "On the difference between consecutive primes", Invent. Math. 15 (1972), 164–170. DOI 10.1007/BF01404114.

[^85^] L. Guth, J. Maynard, "New large value estimates for Dirichlet polynomials", arXiv:2405.20552 (2024).

[^86^] H. Kadiri, A. Lumley, N. Ng, "Explicit zero density for the Riemann zeta function", J. Math. Anal. Appl. 465 (2018), 22–46. DOI 10.1016/j.jmaa.2018.02.033.

[^87^] C. Bellotti, "An explicit log-free zero density estimate for the Riemann zeta-function", J. Number Theory 269 (2025), 37–77. arXiv:2405.12545.

[^88^] M. J. Mossinghoff, T. S. Trudgian, A. Yang, "Explicit zero-free regions for the Riemann zeta-function", Res. Number Theory 10 (2024), art. 11. DOI 10.1007/s40993-023-00506-9.

[^89^] K. Ford, "Vinogradov's integral and bounds for the Riemann zeta function", Proc. London Math. Soc. 85 (2002), 565–630. DOI 10.1112/S0024611502013655.

[^90^] G. Csordas, T. S. Norfolk, R. S. Varga, "A lower bound for the de Bruijn–Newman constant Λ", Numer. Math. 52 (1988), 483–497. DOI 10.1007/BF01400887.

[^91^] D. H. J. Polymath, "Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant", Res. Math. Sci. 6 (2019), no. 3, Art. 31. DOI 10.1007/s40687-019-0193-1. arXiv:1904.12438 (verified via arXiv API; dim07's 1810.05120 is an unrelated QCD paper).

[^92^] M. Suzuki, "Weil's quadratic form via the screw function", arXiv:2606.09096 (2026)..09096

[^93^] M. Suzuki, "Aspects of the screw function corresponding to the Riemann zeta function", J. Lond. Math. Soc. (2) 108 (2023), 1448–1487. DOI 10.1112/jlms.12785. arXiv:2206.03682.

[^94^] A. Groskin, preprint on archimedean Weil tails, arXiv:2607.02828 (2026)..02828

[^95^] A. Connes, C. Consani, H. Moscovici, "Zeta spectral triples", arXiv:2511.22755 (2025)..22755

[^96^] A. Connes, W. van Suijlekom, "Quadratic forms, real zeros and echoes of the spectral action", Comm. Math. Phys. 406 (2025), 312. arXiv:2511.23257.

[^97^] A. Connes, "The Riemann Hypothesis: Past, Present and a Letter Through Time", arXiv:2602.04022 (2026), §4.1.

[^98^] K. Barner, "On A. Weil's explicit formula", J. Reine Angew. Math. 323 (1981), 139–152. DOI 10.1515/crll.1981.323.139.

[^99^] J. Büthe, J. Franke, A. Jost, T. Kleinjung, "Some applications of the Weil–Barner explicit formula", Math. Nachr. 286 (2013), 536–549; J. Büthe, arXiv:1410.7008, §2.

[^100^] E. Bombieri, "A variational approach to the explicit formula", Comm. Pure Appl. Math. 56 (2003), no. 8, 1151–1164. DOI 10.1002/cpa.10089 (verified; replaces erroneous cpa.10077).

[^101^] X. Zhu, "Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law", arXiv:2608.24827 (2026, preprint)..24827

[^102^] A. Connes, C. Consani, "Spectral triples and ζ-cycles", Enseign. Math. 69 (2023), no. 1–2, 93–148. DOI 10.4171/lem/1049 (per verification; the arXiv HTML header carries a stale unrelated DOI template). arXiv:2106.01715.

[^103^] N. Wiener, "Tauberian theorems", Ann. of Math. (2) 33 (1932), 1–100. DOI 10.2307/1968102; L2 version: The Fourier Integral and Certain of Its Applications, CUP, 1933, Ch. II.

[^104^] G. Poitou, "Sur les petits discriminants", Sém. Delange-Pisot-Poitou 18 (1976/77), exp. 6. Numdam SDPP_1976-1977__18_1_A6_0.

[^105^] A. M. Odlyzko, "Bounds for discriminants and related estimates for class numbers, regulators and zeros of zeta functions: a survey of recent results", J. Théor. Nombres Bordeaux 2 (1990), 119–141. DOI 10.5802/jtnb.22.

[^106^] A. Weil, "Sur les formules explicites de la théorie des nombres", Izv. Akad. Nauk SSSR Ser. Mat. 36 (1972), 3–18; Math. USSR-Izv. 6 (1972), 1–17. DOI 10.1070/IM1972v006n01ABEH001866. https://www.mathnet.ru/eng/im2289

[^107^] M. Suzuki, "On the Hilbert space derived from the Weil distribution", Canad. J. Math. (2025). DOI 10.4153/S0008414X25101739 (verified via Crossref; dim07's S0008414X25000327 does not resolve). arXiv:2301.00421.

[^108^] S. Haran, "Riesz potentials and explicit sums in arithmetic", Invent. Math. 101 (1990), 697–703. DOI 10.1007/BF01231521.

[^109^] J. C. Lagarias, "On a positivity property of the Riemann ξ-function", Acta Arith. 89 (1999), 217–234. DOI 10.4064/aa-89-3-217-234.

[^110^] A. Connes, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function", Selecta Math. (N.S.) 5 (1999), 29–106. DOI 10.1007/s000290050042. arXiv:math/9811068.

[^111^] E. Bombieri, D. A. Hejhal, "On the distribution of zeros of linear combinations of Euler products", Duke Math. J. 80 (1995), 821–862. DOI 10.1215/S0012-7094-95-08028-4.

[^112^] B. Nyman, On some groups and semigroups of translations, Thesis, Uppsala, 1950; A. Beurling, "A closure problem related to the Riemann zeta-function", Proc. Natl. Acad. Sci. USA 41 (1955), 312–314, DOI 10.1073/pnas.41.5.312; L. Báez-Duarte, "A strengthening of the Nyman–Beurling criterion", Atti Accad. Naz. Lincei (9) 14 (2003), 5–11, arXiv:math/0202141.

[^113^] M. G. Krein, H. Langer, "Continuation of hermitian positive definite functions and related questions", Integral Equations Operator Theory 78 (2014), 1–69.

[^114^] J.-F. Burnol, "Two complete and minimal systems associated with the zeros of the Riemann zeta function", J. Théor. Nombres Bordeaux 16 (2004), no. 1, 65–94. DOI 10.5802/jtnb.434. arXiv:math/0203120.

[^115^] G. Szegő, Orthogonal Polynomials, AMS Colloquium Publ. 23, 4th ed., AMS, 1975, §5.7.

[^116^] J. J. Holt, J. D. Vaaler, "The Beurling–Selberg extremal functions for a ball in Euclidean space", Duke Math. J. 83 (1996), 202–248. DOI 10.1215/S0012-7094-96-08309-X.

[^117^] J. D. Vaaler, "Some extremal functions in Fourier analysis", Bull. Amer. Math. Soc. 12 (1985), 183–216. DOI 10.1090/S0273-0979-1985-15349-2.

[^118^] E. Carneiro, F. Littmann, J. D. Vaaler, "Gaussian subordination for the Beurling–Selberg extremal problem", Trans. Amer. Math. Soc. 365 (2013), 3493–3534. DOI 10.1090/S0002-9947-2013-05716-9. arXiv:1008.4969.

[^119^] M. Avdispahić, L. Smajlović, "Explicit formula for a fundamental class of functions", Bull. Belg. Math. Soc. Simon Stevin 12 (2005), 569–587.

[^120^] T. A. Wong, "Explicit formulas for the spectral side of the trace formula of SL(2)", arXiv:1608.02296 (2016).

[^121^] A. Bondarenko, D. Radchenko, K. Seip, "Fourier interpolation with zeros of zeta and L-functions", Constr. Approx. 57 (2023), 405–461. DOI 10.1007/s00365-022-09599-w. arXiv:2005.02996.

[^122^] L. de Branges, "The Riemann hypothesis for Hilbert spaces of entire functions", Bull. Amer. Math. Soc. (N.S.) 15 (1986), 1–17; "A conjecture which implies the Riemann hypothesis", J. Funct. Anal. 121 (1994), 117–184. DOI 10.1006/jfan.1994.1047.

[^123^] J. B. Conrey, X.-J. Li, "A note on some positivity conditions related to zeta and L-functions", Int. Math. Res. Not. 2000, no. 18, 929–935. DOI 10.1155/S1073792800000489. arXiv:math/9812166.

[^124^] M. Suzuki, "A canonical system of differential equations arising from the Riemann zeta-function", arXiv:1204.1827 (2012, v2 2016).

[^125^] M. Suzuki, "Hamiltonians arising from L-functions in the Selberg class", J. Math. Anal. Appl. (2021), DOI 10.1016/j.jmaa.2021.125198; "Integral operators arising from the Riemann zeta function", arXiv:1907.07302.

[^126^] M. Suzuki, "Li coefficients as norms of functions in a model space", arXiv:2301.05779 (2023), to appear in J. Number Theory.

[^127^] E. Carneiro, V. Chandee, F. Littmann, M. B. Milinovich, "Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function", J. Reine Angew. Math. 725 (2017), 143–182. DOI 10.1515/crelle-2014-0081. arXiv:1406.5462.

[^128^] E. C. Titchmarsh, The Theory of the Riemann Zeta-Function, 2nd ed. (rev. D. R. Heath-Brown), Oxford Univ. Press, 1986; Theorem 9.4 (Riemann–von Mangoldt).

[^129^] J.-F. Burnol, "On Fourier and Zeta(s)", Forum Math. 16 (2004), 789–840. arXiv:math/0112254.

[^130^] A. Beurling, P. Malliavin, "On the closure of characters and the zeros of entire functions", Acta Math. 118 (1967), 79–93. DOI 10.1007/BF02392477.

[^131^] K. Seip, A. Ulanovskii, "The Beurling–Malliavin density of a random sequence", Proc. Amer. Math. Soc. 125 (1997), 1749–1754.

[^132^] P. Koosis, The Logarithmic Integral I–II, Cambridge Stud. Adv. Math. 12 & 21, CUP, 1988/1992.

[^133^] Yu. Belov, V. Havin, "The Beurling–Malliavin multiplier theorem and its analogs for the de Branges spaces", in Operator Theory (D. Alpay, ed.), Springer, 2015, vol. 1, 581–609. arXiv:1309.7130.

[^134^] R. Giuliano, G. Grekos, "On the connection between the Beurling–Malliavin density and the asymptotic density", arXiv:2311.04762 (2023).

[^135^] A. Beurling, "Local harmonic analysis with some applications to differential operators", in Some Recent Advances in the Basic Sciences vol. 1, Belfer Graduate School, 1966, 109–125; Collected Works vol. 2, Birkhäuser, 1989.

[^136^] N. Blank, A. Ulanovskii, "On Cartwright's theorem", arXiv:1603.09585 (2016).

[^137^] J. Ortega-Cerdà, K. Seip, "Beurling-type density theorems for weighted Lp interpolation in Bernstein's space", J. Funct. Anal. 162 (1999), 400–415. arXiv:math/0005092.

[^138^] A. Beurling, P. Malliavin, "On Fourier transforms of measures with compact support", Acta Math. 107 (1962), 291–309. DOI 10.1007/BF02545792.

[^139^] J. Mashreghi, F. L. Nazarov, V. P. Havin, "The Beurling–Malliavin multiplier theorem: the seventh proof", Algebra i Analiz 17 (2005), 3–68 = St. Petersburg Math. J. 17 (2006), 699–744.

[^140^] Yu. Lyubarskii, J. Ortega-Cerdà, "Bandlimited Lipschitz functions", Appl. Comput. Harmon. Anal. 37 (2014), 307–324. arXiv:1307.7359.

[^141^] B. Ya. Levin, Distribution of Zeros of Entire Functions, Transl. Math. Monographs 5, AMS, rev. ed. 1980; Lectures on Entire Functions, Transl. Math. Monographs 150, AMS, 1996.

[^142^] M. Cartwright, "On certain integral functions of order one", Quart. J. Math. 7 (1936), 46–55; classical Cartwright-class theory (1935–36), see [Levin].

[^143^] H. J. Landau, "Necessary density conditions for sampling and interpolation of certain entire functions", Acta Math. 117 (1967), 37–52. DOI 10.1007/BF02395039.

[^144^] Yu. I. Lyubarskii, K. Seip, "Complete interpolating sequences for Paley–Wiener spaces and Muckenhoupt's (Ap) condition", Rev. Mat. Iberoamericana 13 (1997), 361–376. arXiv:math/9511212.

[^145^] B. S. Pavlov, "The basis property of a system of exponentials and the condition of Muckenhoupt", Dokl. Akad. Nauk SSSR 247 (1979), 37–40 = Soviet Math. Dokl. 20 (1979), 655–659.

[^146^] S. V. Hruščëv, N. K. Nikol'skiĭ, B. S. Pavlov, "Unconditional bases of exponentials and of reproducing kernels", LNM 864, Springer, 1981, 214–335.

[^147^] J. Ortega-Cerdà, K. Seip, "Fourier frames", Ann. of Math. (2) 155 (2002), 789–806.

[^148^] L. de Branges, Hilbert Spaces of Entire Functions, Prentice-Hall, 1968; D. N. Clark, "One dimensional perturbations of restricted shifts", J. Analyse Math. 25 (1972), 169–191.

[^149^] F. Gonçalves, "Interpolation formulas with derivatives in de Branges spaces", Trans. Amer. Math. Soc. 369 (2017), no. 2, 805–832. DOI 10.1090/tran6672 (issue/DOI corrected via Crossref; both dim files' DOIs tran/6714, tran/6861 point to other papers). arXiv:1503.01412; Part II (with F. Littmann): J. Math. Anal. Appl. 458 (2018), 1091–1114.

[^150^] S. A. Avdonin, "On the question of Riesz bases of exponential functions in L2", Vestnik Leningrad Univ. 13 (1974), 5–12 = Vestnik Leningrad Univ. Math. 7 (1979), 203–211.

[^151^] D. Radchenko, M. Viazovska, "Fourier interpolation on the real line", Publ. Math. Inst. Hautes Études Sci. 129 (2019), 51–81. DOI 10.1007/s10240-018-0101-z.

[^152^] A. Kulikov, "Fourier interpolation and time-frequency localization", J. Fourier Anal. Appl. 27 (2021), Paper 58. DOI 10.1007/s00041-021-09861-y.

[^153^] A. Kulikov, F. Nazarov, M. Sodin, "Fourier uniqueness and non-uniqueness pairs", J. Math. Phys. Anal. Geom. 21 (2025), no. 1, 84–130. DOI 10.15407/mag21.01.04. arXiv:2306.14013.

[^154^] N. Levinson, Gap and Density Theorems, AMS Colloquium Publ. 26, 1940.

[^155^] R. M. Redheffer, "Completeness of sets of complex exponentials", Adv. Math. 24 (1977), 1–62.

[^156^] H. Ki, Y.-O. Kim, J. Lee, "On the de Bruijn–Newman constant", Adv. Math. 222 (2009), 281–306. DOI 10.1016/j.aim.2009.04.003. Convention warning: their Λ = 4λ(0), a factor of 4 against Rodgers–Tao.

[^157^] C. M. Newman, "Fourier transforms with only real zeros", Proc. Amer. Math. Soc. 61 (1976), 245–251. DOI 10.1090/S0002-9939-1976-0434982-5.

[^158^] D. K. Dimitrov, P. K. Rusev, "Zeros of entire Fourier transforms", East J. Approx. 17 (2011), 1–108.

[^159^] G. Csordas, W. Smith, R. S. Varga, "Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis", Constr. Approx. 10 (1994), 107–129. DOI 10.1007/BF01205170 (verified; replaces erroneous BF01212570).

[^160^] A. M. Odlyzko, "An improved bound for the de Bruijn–Newman constant", Numer. Algorithms 25 (2000), 293–303.

[^161^] MathOverflow 115447, "The Riemann zeros and the heat equation". https://mathoverflow.net/questions/115447/

[^162^] H. Ki, Y.-O. Kim, "De Bruijn's question on the zeros of Fourier transforms", J. Anal. Math. 91 (2003), 369–387.

[^163^] G. Pólya, "Über trigonometrische Integrale mit nur reellen Nullstellen", J. Reine Angew. Math. 158 (1927), 6–18, DOI 10.1515/crll.1927.158.6; "Über die algebraisch-funktionentheoretischen Untersuchungen von J. L. W. V. Jensen", Kgl. Danske Vid. Sel. Math.-Fys. Medd. 7 (1927), no. 17, 1–33; "Bemerkung über die Integraldarstellung der Riemannschen ξ-Funktion", Acta Math. 48 (1926), 305–317, DOI 10.1007/BF02565336.

[^164^] M. Griffin, K. Ono, L. Rolen, J. Thorner, Z. Tripp, I. Wagner, "Jensen polynomials for the Riemann xi-function", Adv. Math. 397 (2022), 108186. arXiv:1910.01227.

[^165^] K. Gröchenig, "Schoenberg's theory of totally positive functions and the Riemann zeta function", arXiv:2007.12889 (2020).

[^166^] G. Csordas, survey on Fourier transforms and the Laguerre–Pólya class, arXiv:1309.0055, §4.

[^167^] D. A. Cardon, "Fourier transforms having only real zeros", Proc. Amer. Math. Soc. 133 (2005), 1349–1356. DOI 10.1090/S0002-9939-04-07655-9.

[^168^] M. Planat, "The theta-kernel positivity problem for the Riemann Xi function", Preprints 2026, 202604.1239, DOI 10.20944/preprints202604.1239.v1, and sequels (202606.0062, 202606.1957).
