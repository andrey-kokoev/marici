# Literature-search result

Search cut: **September 3, 2026**.

Under the standard Guinand–Weil normalization given below:

1. **Escape to infinity is excluded unconditionally at every finite positive heat threshold.**
2. **No located theorem excludes finite double contact.**
3. Gaussian total positivity, the parabolic zero-number theorem, and the strong maximum principle do not exclude contact because increasing \(t\) is backward heat evolution.
4. Exact interpolation on the zeta-zero set exists in a large entire-function class, but not in any fixed Paley–Wiener class.
5. The de Bruijn–Newman and Jensen-polynomial flows do not map their positivity or real-rootedness properties to \(\Theta\).
6. Compact-window Weil positivity provides a concrete conditional route: truncate the inverse Gaussian factors and compare the resulting explicit-formula error with a certified window margin.

## 1. Normalization

I used the Fourier convention

$$
\widehat f(\eta)=\int_{\mathbb R}f(u)e^{-2\pi iu\eta}\,du
$$

and the symmetrized shifted Gaussian

$$
h_{t,\xi}(u)
=
e^{-t(u-\xi)^2}+e^{-t(u+\xi)^2}.
$$

Bondarenko–Radchenko–Seip use the Guinand–Weil formula for functions analytic in a strip wider than \(|\Im z|\le \tfrac12\), with polynomial decay there. Every \(h_{t,\xi}\) satisfies those hypotheses. Their formula gives

$$
\Theta(t,\xi)
=
\sum_{\rho}
h_{t,\xi}\!\left(\frac{\rho-\frac12}{i}\right)
=
K_{\mathrm{end}}(t,\xi)
+
K_{\Gamma}(t,\xi)
+
K_{\mathrm{pr}}(t,\xi),
$$

where

$$
K_{\mathrm{end}}(t,\xi)
=
4e^{t/4-t\xi^2}\cos(t\xi),
$$

$$
K_{\Gamma}(t,\xi)
=
\frac1{2\pi}\int_{\mathbb R}
h_{t,\xi}(u)
\left[
\Re\psi\!\left(\frac14+\frac{iu}{2}\right)-\log\pi
\right]du,
$$

and

$$
K_{\mathrm{pr}}(t,\xi)
=
-\frac{2}{\sqrt{\pi t}}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
e^{-(\log n)^2/(4t)}
\cos(\xi\log n).
$$

The source’s class \(H_1\), Fourier convention, explicit formula (1.1), and zero-node convention \((\rho-\frac12)/i\) are stated immediately before its Theorem 1.1. ([arXiv][1])

**Citation.** Andriy Bondarenko, Danylo Radchenko, Kristian Seip, “Fourier Interpolation with Zeros of Zeta and \(L\)-Functions,” *Constructive Approximation* **57** (2023), 405–461. DOI: **10.1007/s00365-022-09599-w**. arXiv:**2005.02996**.

If the intended \(\Theta\) differs only by multiplication by a positive \(t\)-dependent scalar or by replacing \(t\) with a reciprocal variance parameter, the coercivity conclusion below is unchanged.

The standard heat parameter is

$$
s=\frac1{4t},
\qquad
U(s,\xi)=\sqrt{\frac{t}{\pi}}\,\Theta(t,\xi).
$$

Then

$$
\partial_s U=\partial_{\xi}^{\,2}U.
$$

Thus increasing \(t\), which narrows the Gaussian, is backward evolution in \(s\).

---

# 2. Escape to infinity

## 2.1 Uniform coercivity theorem

### Derived theorem

For every compact interval

$$
I=[t_0,T]\Subset(0,\infty),
$$

one has

$$
K_{\Gamma}(t,\xi)
=
\frac1{\sqrt{\pi t}}
\log\frac{|\xi|}{2\pi}
+
o_I(1),
\qquad |\xi|\to\infty,
$$

uniformly for \(t\in I\). Consequently,

$$
\boxed{
\lim_{R\to\infty}
\inf_{\substack{t\in I\\|\xi|\ge R}}
\Theta(t,\xi)=+\infty .
}
$$

### Source hypotheses

The digamma expansion used is

$$
\psi(z)
=
\log z-\frac1{2z}+O_\delta(|z|^{-2})
$$

uniformly in sectors \(|\arg z|\le\pi-\delta\). It is equation 5.11.2 of the NIST/DLMF gamma-function chapter. The corresponding printed reference is the *NIST Handbook of Mathematical Functions*, DOI **10.1017/CBO9780511920001**. ([NIST][2])

For real \(u\),

$$
q(u):=
\Re\psi\!\left(\frac14+\frac{iu}{2}\right)-\log\pi
=
\log|u|-\log(2\pi)+O(u^{-2}).
$$

The function \(q\) is real, even, smooth on \(\mathbb R\), and bounded below.

### Proof

Evenness of \(q\) gives

$$
K_\Gamma(t,\xi)
=
\frac1\pi
\int_{\mathbb R}e^{-t(u-\xi)^2}q(u)\,du.
$$

Put \(u=\xi+v\). On \(|v|\le|\xi|/2\),

$$
q(\xi+v)
=
\log|\xi|-\log(2\pi)
+
O\!\left(\frac{|v|+1}{|\xi|}\right).
$$

The Gaussian moments

$$
\int_{\mathbb R} e^{-tv^2}(1+|v|)\,dv
$$

are bounded uniformly for \(t\in[t_0,T]\). The complementary region contributes \(o_I(1)\), since it has Gaussian weight at most \(e^{-t_0\xi^2/4}\), while \(q(u)=O(\log(2+|u|))\). Therefore

$$
K_\Gamma(t,\xi)
=
\frac1\pi
\sqrt{\frac{\pi}{t}}
\left(\log|\xi|-\log(2\pi)\right)
+
o_I(1).
$$

The endpoint term satisfies

$$
|K_{\mathrm{end}}(t,\xi)|
\le
4e^{T/4-t_0\xi^2}.
$$

The prime term satisfies

$$
|K_{\mathrm{pr}}(t,\xi)|
\le
M_I,
$$

where

$$
M_I:=
\frac{2}{\sqrt{\pi t_0}}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
e^{-(\log n)^2/(4T)}
<\infty .
$$

The convergence is elementary: the Gaussian in \(\log n\) eventually dominates every negative power of \(n\). Hence the archimedean logarithm dominates both remaining terms uniformly on \(I\).

### Consequence for a first threshold

If \(t_j\to t_*\in(0,\infty)\), then choose \(I\Subset(0,\infty)\) containing all sufficiently large \(t_j\). The preceding theorem makes

$$
|\xi_j|\to\infty,
\qquad
\Theta(t_j,\xi_j)\to0
$$

impossible. Therefore any first loss of positivity at a finite \(t_*\) is attained at a finite \(\xi_*\).

**Missing step discharged:** escape to infinity at a finite positive threshold.

**Unmet hypotheses:** only verification that the intended \(K_{\mathrm{end}},K_\Gamma,K_{\mathrm{pr}}\) use the displayed normalization, or an equivalent positive rescaling.

**RH dependence:** none.

**Classification:** `applicable`.

**Cheapest test:** term-by-term symbolic comparison with the intended kernel definition. An effective compact radius can then be obtained by computing a rigorous uniform remainder bound for \(q(u)-\log(|u|/2\pi)\) and the convergent number \(M_I\).

---

## 2.2 Prime almost-periodicity gives an obstruction, not an escape mechanism

For distinct primes \(p_1,\ldots,p_m\), the numbers

$$
\log p_1,\ldots,\log p_m
$$

are linearly independent over \(\mathbb Q\). Kronecker–Weyl approximation therefore gives, for positive coefficients \(a_{p,k}\),

$$
\sup_{\xi\in\mathbb R}
\sum_{p\le P}\sum_{k\le K_p}
a_{p,k}\cos(k\xi\log p)
=
\sum_{p\le P}\sum_{k\le K_p}a_{p,k}.
$$

Absolute and locally uniform convergence of the Gaussian-weighted full prime-power series then implies

$$
\sup_{\xi}
\sum_{p}\sum_{k\ge1}
\frac{\log p}{p^{k/2}}
e^{-k^2(\log p)^2/(4t)}
\cos(k\xi\log p)
=
\sum_{p}\sum_{k\ge1}
\frac{\log p}{p^{k/2}}
e^{-k^2(\log p)^2/(4t)}.
$$

Thus no pointwise estimate can replace the absolute prime mass by a fixed smaller multiple uniformly in \(\xi\). The current version of Zhu’s Lemma 3.2 proves the analogous exact supremum statement for the finite prime comb; Theorem 1.4 derives the resulting barrier for pointwise-envelope certificates. ([arXiv][3])

**Citation.** Xuefeng Zhu, “Weil Positivity in Compact Windows: a Finite Reduction, Certified Two-Sided Bounds, and a Landau–Widom Decay Law,” arXiv:**2608.24827v2**, September 2, 2026. DOI: **10.48550/arXiv.2608.24827**. This is an unrefereed preprint. ([arXiv][3])

**Missing step discharged:** it rules out a proposed uniform-cancellation shortcut for \(K_{\mathrm{pr}}\).

**Unmet hypotheses:** none for the finite comb; passage to the infinite Gaussian comb uses the displayed absolute convergence.

**RH dependence:** none.

**Classification:** `applicable`.

**Cheapest test:** none. The alignment obstruction follows from unique factorization and Kronecker approximation.

---

# 3. Finite zero contact

## 3.1 Angenent’s zero-number theorem

**Citation.** Sigurd Angenent, “The Zero Set of a Solution of a Parabolic Equation,” *Journal für die reine und angewandte Mathematik* **390** (1988), 79–96. DOI: **10.1515/crll.1988.390.79**.

### Exact results

Angenent considers

$$
u_s=a(s,x)u_{xx}+b(s,x)u_x+c(s,x)u,
\qquad a>0,
$$

under boundedness and regularity assumptions on the coefficients and their indicated derivatives.

* **Theorem A:** a finite-order zero has a locally finite parabolic zero-set structure unless the solution is identically zero.
* **Theorem B:** on a finite spatial interval, with nonvanishing boundary traces and finite initial zero count, the number of spatial zeros is nonincreasing in forward time and drops strictly when a multiple zero occurs.

### Map to \(\Theta\)

Take

$$
u(s,x)=U(s,\xi),
\qquad
a=1,\quad b=c=0,\quad x=\xi.
$$

The coercivity theorem permits restriction to \([-R,R]\) around a candidate finite threshold, with nonzero positive boundary values for \(R\) sufficiently large.

### What it proves

A finite multiple contact has the standard local zero-annihilation topology. If a zero has multiplicity greater than one, forward heat evolution reduces the zero number.

### Why it does not exclude contact

Positivity is known on the broad side \(s>s_*\). The contact lies at the initial-time boundary \(s=s_*\) of that forward-positive region. For \(s<s_*\), which corresponds to larger \(t\), the solution may be negative. Angenent’s theorem allows two zeros to merge at \(s_*\) and disappear for \(s>s_*\); it does not prohibit this event.

The whole-line and finite-zero hypotheses also require coercive localization and a proof that the zero count in the selected interval is finite, although analyticity supplies local finiteness.

**Missing step discharged:** local classification and forward zero-count monotonicity, not exclusion.

**Unmet hypotheses:** finite interval, nonzero boundary traces, finite zero count, and the wrong temporal direction for the desired inference.

**RH dependence:** none.

**Classification:** `inapplicable` for exclusion; locally applicable after coercive localization.

**Cheapest test:** choose a compact \(t\)-interval around a proposed \(t_*\), compute a certified \(R\) from the coercivity estimate, and verify \(U(s,\pm R)>0\). The theorem will then classify any observed contact but will not rule it out.

---

## 3.2 Generic signed-data counterexample

Let

$$
G_\sigma(x)=\frac1{\sqrt{4\pi\sigma}}e^{-x^2/(4\sigma)}
$$

and choose \(A>B>0\), \(s_*>0\), and

$$
c=\sqrt{\frac{B+s_*}{A+s_*}}.
$$

Define

$$
u(s,x)=G_{A+s}(x)-c\,G_{B+s}(x).
$$

Then \(u_s=u_{xx}\), and

$$
\frac{G_{A+s}(x)}{G_{B+s}(x)}
=
\sqrt{\frac{B+s}{A+s}}
\exp\!\left(
\frac{(A-B)x^2}{4(A+s)(B+s)}
\right).
$$

This ratio is minimized at \(x=0\). Its minimum increases strictly with \(s\). Consequently,

$$
u(s,x)>0\quad(s>s_*),
$$

$$
u(s_*,x)\ge0,
\qquad
u(s_*,0)=u_x(s_*,0)=0,
\qquad
u_{xx}(s_*,0)>0,
$$

and

$$
u(s,0)<0\quad(s<s_*).
$$

This is an exact double contact separating a positive broader Gaussian scale from a negative narrower scale.

**Result:** no theorem depending only on “signed initial distribution + Gaussian convolution + positivity at one scale” can exclude the required contact. Additional arithmetic structure is necessary.

**Classification:** `applicable` obstruction.

---

## 3.3 Total positivity and variation diminution

**Classical citation.** I. J. Schoenberg, “On Variation-Diminishing Integral Operators of the Convolution Type,” *Proceedings of the National Academy of Sciences* **34** (1948), 164–169. DOI: **10.1073/pnas.34.4.164**.

**Exact modern statement.** Karlheinz Gröchenig, “Infinite Totally Positive Matrices: Some Open Problems,” *Acta Scientiarum Mathematicarum* (2026). DOI: **10.1007/s44146-026-00264-3**.

* Definition 2.5 identifies the Gaussian \(e^{-\pi\gamma x^2}\), \(\gamma>0\), as a Pólya-frequency/totally positive kernel.
* Theorem 4.9 states that if \(g\) is totally positive and \(f\) is locally Riemann-integrable, then

$$
S(f*g)\le S(f),
$$

where \(S\) is the number of sign changes when finite. The paper explicitly observes that the statement becomes vacuous when the input has infinitely many sign changes. ([Springer][4])

### Map

For \(s_2>s_1\),

$$
U(s_2,\cdot)
=
G_{s_2-s_1}*U(s_1,\cdot).
$$

Therefore

$$
S(U(s_2,\cdot))
\le
S(U(s_1,\cdot)).
$$

### Failure

The inequality runs from narrower to broader scales. It permits sign changes and a negative interval to appear when the evolution is reversed. The explicit counterexample above shows that this possibility is realized even by a difference of two Gaussians.

The underlying arithmetic distribution also has no known finite-sign-variation representation. The theorem becomes noninformative if the sign count is infinite.

**Missing step discharged:** none for contact exclusion; it restricts forward evolution only.

**Unmet hypotheses:** finite or otherwise quantitatively controlled sign variation and a theorem relating that variation to the arithmetic distribution.

**RH dependence:** none. Proving that the underlying Weil distribution is nonnegative would itself contain the desired zero-location information.

**Classification:** `inapplicable` in its present form.

**Cheapest test:** search for a finite signed-measure or finite-sign-change representation of one narrower profile. Without such a representation, total positivity supplies no additional inequality.

---

# 4. Weil positivity and promotion from compact tests

## 4.1 Weil’s criterion in a precise test space

**Classical citation.** André Weil, “Sur les ‘formules explicites’ de la théorie des nombres premiers,” *Communications du Séminaire Mathématique de l’Université de Lund*, volume dedicated to Marcel Riesz (1952), 252–265. DOI: none. ([CERN Document Server][5])

A modern exact formulation is Wong’s Theorem 2.3.

**Citation.** Tian An Wong, “Explicit Formulas for the Spectral Side of the Trace Formula of \(\mathrm{SL}(2)\),” *Acta Arithmetica* **195** (2020), 149–175. DOI: **10.4064/aa190115-9-10**. arXiv:**1608.02296**. ([Mathematical Institute PAN][6])

### Theorem 2.3

The typed test space is

$$
C_c^\infty(\mathbb R_+^\times)
$$

with multiplicative convolution and Mellin transform. With the multiplicative involution chosen so that

$$
\widehat{g^\tau}(s)=\widehat g(1-s),
$$

the theorem states that RH is equivalent to

$$
W(g*\overline{g}^{\,\tau})\ge0
$$

for every compactly supported smooth \(g\), with equality only for \(g=0\). On the zero side,

$$
W(g*\overline{g}^{\,\tau})
=
\sum_\rho
\widehat g(\rho)\,
\overline{\widehat g(1-\bar\rho)}.
$$

The theorem and its convolution/Mellin conventions are given in Section 2. ([arXiv][7])

### Map to the shifted Gaussian

Set

$$
F_\pm(z)=e^{-\frac t2(z\mp\xi)^2}.
$$

Since \(F_\pm^\#(z):=\overline{F_\pm(\bar z)}=F_\pm(z)\),

$$
h_{t,\xi}(z)
=
F_+(z)F_+^\#(z)+F_-(z)F_-^\#(z).
$$

This is the required algebraic quadratic-factor form. The obstruction is analytic: \(F_\pm\) are entire of order two, not finite exponential type. Their inverse Fourier transforms are Gaussians, not compactly supported functions.

### Required missing theorem

One needs compactly supported factors \(g_{\pm,L}\) with transforms \(F_{\pm,L}\) such that

$$
W\!\left(
h_{t,\xi}
-
F_{+,L}F_{+,L}^\#
-
F_{-,L}F_{-,L}^\#
\right)
$$

is controlled uniformly and is smaller than an unconditional compact-window positivity margin.

Ordinary \(L^1(\mathbb R)\), uniform real-axis, or pointwise positive approximation does not suffice: off RH, \(W\) samples entire functions at nonreal points.

**RH dependence:** the criterion is equivalent to RH. The required approximation/error theorem would not itself assume RH.

**Classification:** `conditionally applicable`.

**Cheapest test:** truncate the inverse Fourier Gaussians to \([-L,L]\), calculate the three explicit-formula components of the resulting error separately, and compare them with a known lower bound for the localized Weil form.

---

## 4.2 Burnol’s compact-support positivity

**Citation.** Jean-François Burnol, “Sur les Formules Explicites I: analyse invariante,” *Comptes Rendus de l’Académie des Sciences de Paris, Série I* **331** (2000), 423–428. DOI: none located. arXiv:**math/0101068**. ([arXiv][8])

### Theorem 3.7

Let \(g\in C_c^\infty(0,\infty)\),

$$
g^\tau(u)=\frac1u g(1/u),
\qquad
k=g*g^\tau
$$

under multiplicative convolution. Then

$$
Z(k)=\sum_\rho \widehat g(\rho)\widehat g(1-\rho).
$$

Theorem 3.7 states that there exists \(c>1\) such that

$$
Z(k)\ge0
$$

whenever

$$
\operatorname{supp}g\subset[1/c,c].
$$

The proof chooses \(c=e^{\varepsilon/2}\) for sufficiently small \(\varepsilon\). It explicitly says that an additional idea is needed to reach \(c=\sqrt2\). ([arXiv][9])

### Map

With \(x=\log u\), the support becomes

$$
x\in[-\log c,\log c].
$$

The inverse Fourier Gaussian factor has full support, so it is not covered directly.

**Missing step discharged:** unconditional positivity on a nonzero compact window.

**Unmet hypotheses:** compact support of the factor, not merely rapid decay.

**RH dependence:** none for the small window. Positivity for every \(c\) is equivalent to RH.

**Classification:** `conditionally applicable` to \(\Theta\).

**Cheapest test:** truncate each inverse Gaussian factor inside \([-\log c,\log c]\) and estimate the explicit-formula truncation error.

---

## 4.3 Yoshida’s localized Hermitian forms

**Citation.** Hiroyuki Yoshida, “On Hermitian Forms Attached to Zeta Functions,” in *Zeta Functions in Geometry*, Advanced Studies in Pure Mathematics **21** (1992), 281–325. DOI: **10.2969/aspm/02110281**. ([Project Euclid][10])

The results relevant here are:

* **Proposition 1:** strict positivity on all nonzero odd compactly supported smooth tests implies RH; strict positivity on all nonzero even tests implies RH apart from possible real zeros.
* **Lemma 2:** the infimum of the localized Rayleigh quotient on Yoshida’s space \(K(a)\) is positive for sufficiently small \(a\).
* **Theorem 2:** nondegeneracy of the completed localized form for every \(a>0\) is equivalent to RH.

Suzuki gives the test-space definitions and identifies these exact theorem numbers. Yoshida’s \(K(a)\) consists of restrictions to \([-a,a]\) of smooth \(2a\)-periodic functions. ([arXiv][11])

### Map

The physical/logarithmic support parameter is \(a\). The Gaussian factor must be truncated or approximated by members of \(K(a)\).

**Missing step discharged:** small-window positivity and an RH-equivalent exhaustion by compact windows.

**Unmet hypotheses:** a quantitative approximation theorem in the Weil form norm, including the off-real zero evaluations.

**RH dependence:** Lemma 2 is unconditional. The all-\(a\) nondegeneracy statement is equivalent to RH.

**Classification:** `conditionally applicable`.

**Cheapest test:** calculate the localized Rayleigh quotient of a truncated Gaussian factor and bound the cross-term between its compact part and tail.

---

## 4.4 Bombieri’s variational formulation

**Citation.** Enrico Bombieri, “Remarks on Weil’s Quadratic Functional in the Theory of Prime Numbers. I,” *Rendiconti Lincei. Matematica e Applicazioni* **11** no. 3 (2000), 183–233. DOI: none located. Stable journal records are available through EuDML and BDim. ([European Digital Mathematics Library][12])

Relevant numbered results:

* **Theorem 3:** existence of a minimizer for the localized lower bound on \(L^2(E)\), with \(E\) a finite union of intervals.
* **Theorem 5:** continuity of parity-restricted lower bounds as the interval changes is asserted.
* **Theorem 12:** small-support positivity.

Suzuki notes that the proof details for the continuity assertion in Theorem 5 are not fully supplied and proves an unconditional continuity theorem by another method. ([arXiv][11])

### Map

Bombieri’s minimizer theorem can handle compactly supported approximants to the inverse Gaussian factors. It does not identify the Gaussian itself as a localized minimizer.

**Missing step discharged:** attainment of a compact-window variational infimum.

**Unmet hypotheses:** comparison between the Gaussian family and the localized ground state; quantitative continuity/error control.

**RH dependence:** compact-window statements are unconditional; nonnegativity on all windows is RH-equivalent.

**Classification:** `conditionally applicable`.

**Cheapest test:** prove form convergence for truncated inverse Gaussians independently of Bombieri’s asserted continuity step.

---

## 4.5 Suzuki’s 2026 continuity theorem

**Citation.** Masatoshi Suzuki, “Weil’s Quadratic Form via the Screw Function,” arXiv:**2606.09096v1** (June 2026). DOI: **10.48550/arXiv.2606.09096**. ([arXiv][13])

Let \(Q_W^a\) be the closed localized Weil form on \(L^2(-a,a)\), \(A_a\) its associated self-adjoint operator, and

$$
\lambda_a
=
\inf_{v\ne0}
\frac{Q_W^a(v)}{\|v\|_2^2}.
$$

* **Theorem 1.1:** \(A_a\) is the Friedrichs extension of \(B_a=D^*G_aD\) initially defined on \(H_0^1(-a,a)\).
* **Corollary 1.2:** \(\lambda_a\) is the infimum over \(C_c^\infty(-a,a)\).
* **Theorem 1.3:** \(a\mapsto\lambda_a\) is continuous.
* **Theorem 1.4:** for sufficiently small \(a\), \(\lambda_a\) is positive and simple, its ground state is even, and

$$
\lambda_a
=
\log\frac1a+\mu_1-\log(2\pi)+\psi(2)-1+O(a),
\qquad \mu_1>0.
$$

All these results are stated without assuming RH. Failure of RH implies \(\lambda_a<0\) for some \(a\); continuity and small-\(a\) positivity then force a degenerate window with \(\lambda_a=0\). ([arXiv][11])

### Map

The parameter \(a\) is physical/logarithmic support width, not Gaussian inverse variance \(t\). The theorem produces a zero of a window ground-state eigenvalue, not a pointwise zero of \(\Theta(t,\xi)\).

**Missing step discharged:** rigorous support-parameter continuity and attainment for the complete localized Weil form.

**Unmet hypotheses:** a comparison inequality of the form

$$
\inf_\xi\Theta(t,\xi)
\ge
C(t)\lambda_{a(t)}-\varepsilon(t).
$$

**RH dependence:** none in the theorems. The statement \(\lambda_a\ge0\) for all \(a\) is RH-equivalent.

**Classification:** `conditionally applicable`.

**Cheapest test:** calculate \(Q_W^a\) on truncated translated Gaussian factors and compare their Rayleigh quotient to \(\lambda_a\).

---

## 4.6 Zhu’s certified compact-window theorem

**Citation.** Xuefeng Zhu, “Weil Positivity in Compact Windows: a Finite Reduction, Certified Two-Sided Bounds, and a Landau–Widom Decay Law,” arXiv:**2608.24827v2**, September 2, 2026. DOI: **10.48550/arXiv.2608.24827**. Unrefereed preprint. ([arXiv][3])

### Exact results

For real even \(f\) supported in \([-L,L]\), let \(F=\widehat f\), and let \(Q(f)\) denote the Weil form evaluated on \(f*\tilde f\).

* **Theorem 1.1:** an explicit frequency split and finite Legendre-matrix criterion imply a global lower bound for every \(f\) in the full infinite-dimensional window space. The hypotheses include \(T^\sharp>0\) such that

$$
\beta^*
=
\log\frac{T^\sharp}{2\pi}
-\frac1{T^\sharp}
-A_L
>0,
$$

with \(A_L\) the mass of the finite prime comb. All matrix-tail and coupling errors are explicit.

* **Theorem 1.2:**

$$
Q(f)\ge
8.9\times10^{-18}\|f\|_2^2
$$

for every real even \(f\) supported in \([-0.8,0.8]\); the paper also treats the odd sector.

* **Theorem 1.4:** any certificate based on a pointwise envelope for the prime comb requires a cutoff growing doubly exponentially with \(L\), and Lemma 3.2 proves the exact prime-comb supremum used in that obstruction. ([arXiv][3])

### Map

Truncate the inverse Fourier Gaussian factors \(F_\pm\) to \([-0.8,0.8]\). The theorem supplies a numerical but rigorously certified lower margin for their compact portions. One must then show that their tails change the Weil form by less than that margin.

### Unmet hypotheses

The Gaussian factors are not compactly supported. The certified margin is very small, so an ordinary \(L^2\)-tail estimate is insufficient unless accompanied by a sharp explicit-formula continuity bound.

**RH dependence:** none for Theorems 1.1–1.2. The paper’s Theorem 1.3 explicitly assumes RH and is not usable here.

**Classification:** `conditionally applicable`.

**Cheapest test:** perform one interval-arithmetic evaluation of

$$
\left|
W(F_\pm F_\pm^\#-F_{\pm,L}F_{\pm,L}^\#)
\right|
$$

for \(L=0.8\), keeping endpoint, gamma, and prime errors separate, and compare with \(8.9\times10^{-18}\|f_L\|_2^2\).

---

## 4.7 Gaussian Beurling–Selberg approximation

**Citation.** Emanuel Carneiro, Friedrich Littmann, Jeffrey D. Vaaler, “Gaussian Subordination for the Beurling–Selberg Extremal Problem,” *Transactions of the American Mathematical Society* **365** (2013), 3493–3534. DOI: **10.1090/S0002-9947-2012-05687-4**. arXiv:**1008.4969**. ([arXiv][14])

For

$$
G_\lambda(x)=e^{-\pi\lambda x^2},
$$

the relevant results are:

* **Theorem 1:** unique optimal \(L^1\) entire approximation of exponential type \(\pi\).
* **Theorem 2:** unique optimal entire minorant of exponential type \(2\pi\).
* **Theorem 3:** unique optimal entire majorant of exponential type \(2\pi\).

Their Fourier transforms have compact support determined by the exponential type. ([arXiv][14])

### Map

Scaling and translation produce bandlimited entire majorants, minorants, and approximants for each shifted Gaussian component of \(h_{t,\xi}\).

### Failure of direct application

Real-axis inequalities

$$
L(x)\le h_{t,\xi}(x)\le M(x)
$$

do not imply

$$
W(L)\le W(h_{t,\xi})\le W(M)
$$

unless the Weil distribution is already known to be a positive distribution. Off RH, this order-preservation is unavailable and would contain the desired conclusion.

The optimal \(L^1\) error is useful only after proving continuity of \(W\) in a norm controlled by that error and by complex-strip growth.

**RH dependence:** the extremal theorems are unconditional. Order transfer through \(W\) is circular.

**Classification:** `inapplicable` as an order argument; `conditionally applicable` as a quantitative signed-error approximation.

**Cheapest test:** evaluate \(W(h-L)\) directly using the arithmetic side instead of using \(h-L\ge0\).

---

# 5. Strict-peak interpolation

## 5.1 Exact cardinal interpolation on the zeta-zero set

**Citation.** Bondarenko, Radchenko, Seip, “Fourier Interpolation with Zeros of Zeta and \(L\)-Functions,” cited above.

### Theorem 1.1

The theorem constructs rapidly decreasing even entire functions

$$
U_n,\qquad V_{\rho,j},
$$

where \(\rho\) runs over nontrivial zeta zeros and \(0\le j<m_\rho\). They satisfy cardinal conditions at the zero nodes

$$
\lambda_\rho=\frac{\rho-\frac12}{i}:
$$

$$
V_{\rho,j}^{(j')}(\lambda_{\rho'})
=
\delta_{\rho,\rho'}\delta_{j,j'},
$$

with the appropriate multiplicity indexing, while their Fourier transforms vanish at the logarithmic prime sampling nodes. No RH or zero-simplicity hypothesis is imposed. ([arXiv][1])

### Map to a reciprocal pair

For a simple off-line reciprocal pair

$$
\rho,\qquad 1-\bar\rho,
$$

a finite linear combination of the corresponding cardinal functions can be assigned arbitrary values at those nodes and zero at every other zeta node. Choosing values \(1\) and \(-1\), or the phases required by the Weil pairing, gives a stronger discrete interpolation property than “strict modulus below one at all other zeros.”

### Unmet hypotheses

The constructed functions are not asserted to have finite exponential type. They are therefore not automatically Mellin/Fourier transforms of compactly supported Weil factors.

One must also prove that the quadratic product

$$
F(z)F^\#(z)
$$

belongs to a test class on which the explicit formula and the required limiting operations are valid. The cardinal theorem is linear; the Weil test is quadratic.

**RH dependence:** none.

**Classification:** `applicable` for bare entire interpolation; `conditionally applicable` for strict-peak Weil tests.

**Cheapest test:** determine the vertical growth/order of one orbit-symmetrized cardinal function and verify directly that \(F F^\#\) satisfies the \(H_1\) strip-decay conditions and can be approximated in the Weil-form topology by compactly supported factors.

---

## 5.2 Burnol’s Sonine/de Branges evaluator systems

**Citation.** Jean-François Burnol, “Two Complete and Minimal Systems Associated with the Zeros of the Riemann Zeta Function,” *Journal de Théorie des Nombres de Bordeaux* **16** (2004), 65–94. DOI: **10.5802/jtnb.434**. arXiv:**math/0203120**.

Let \(K_a\) be Burnol’s Sonine space, consisting of \(L^2\)-functions with simultaneous gaps for the function and its cosine transform. The completed Mellin transform is the relevant entire-function model.

* **Theorem 2.1:** completed Mellin transforms of elements of \(K_a\) are entire, and point/derivative evaluation is continuous.
* **Theorem 3.1:** the evaluator system indexed by zeta zeros is minimal exactly for \(a\le1\) and complete exactly for \(a\ge1\), with the stated boundary behavior at \(a=1\).
* **Theorem 3.2:** gives the corresponding complementary-system statements.
* **Theorem 3.3:** the functions built from

$$
\frac{\zeta(s)}{(s-\rho)^l}
$$

form complete/minimal systems in the critical Sonine space, with a dual system consisting of triangular combinations of zero-evaluation vectors. ([arXiv][15])

Minimality provides biorthogonal vectors, hence exact cardinal evaluation in this Hilbert-space model.

### Map

A dual evaluator associated with one reciprocal zero orbit is the natural candidate strict-peak factor.

### Unmet hypotheses

The Sonine-gap space is not the same as the compact-support Paley–Wiener factor space used in Weil’s criterion. Minimality gives exact evaluation but no raw bound

$$
|F(\lambda_{\rho'})|<1
$$

outside the selected orbit unless the biorthogonal normalization is analyzed. Closure under \(F\mapsto FF^\#\) is also not supplied.

**RH dependence:** none.

**Classification:** `conditionally applicable`.

**Cheapest test:** compute the selected dual vector’s inverse Mellin transform and determine whether it lies in, or can be approximated in, the compact-factor Weil domain.

---

## 5.3 Paley–Wiener density obstruction

**Citation.** H. J. Landau, “Necessary Density Conditions for Sampling and Interpolation of Certain Entire Functions,” *Acta Mathematica* **117** (1967), 37–52. DOI: **10.1007/BF02395039**.

Landau’s **Theorem 4** gives an upper-density restriction for interpolation sets in Paley–Wiener spaces. In a modern Fourier normalization, Olevskii–Ulanovskii’s Theorem 3 states that if a uniformly discrete real set \(\Lambda\) is an interpolation set for \(PW_S\), then

$$
D^+(\Lambda)\le\frac{\operatorname{mes}S}{\pi}
$$

in their convention. ([arXiv][16])

### Failure of the direct map

To regard all zeta nodes as a real interpolation set requires

$$
\frac{\rho-\frac12}{i}\in\mathbb R
$$

for every \(\rho\), which is RH. Uniform separation of all ordinates is also unproved. Thus Landau’s real interpolation theorem cannot noncircularly establish the requested peak.

**Classification:** `circular` for the full zeta node set.

### Stronger unconditional obstruction for exact cardinal Paley–Wiener functions

Suppose a nonzero entire function \(F\) of finite exponential type vanished at every zeta node except finitely many. Jensen’s formula gives

$$
n_F(R)=O(R),
$$

where \(n_F(R)\) is the number of zeros of \(F\) in \(|z|\le R\), counted with multiplicity. The Riemann–von Mangoldt formula gives

$$
\#\left\{\rho:
\left|\frac{\rho-\frac12}{i}\right|\le R
\right\}
\asymp R\log R.
$$

Therefore no nonzero finite-exponential-type entire function can satisfy the exact BRS cardinal conditions on all zeta zeros.

This proves that the BRS cardinal functions necessarily lie outside every fixed Paley–Wiener space.

It does **not** rule out the weaker requirement

$$
F(\lambda_{\rho_0})=1,
\qquad
|F(\lambda_\rho)|<1
\quad(\rho\ne\rho_0),
$$

because those inequalities do not create zeros and may have no uniform gap below one.

**Classification:** `applicable` obstruction to exact finite-type cardinal interpolation.

**Cheapest test for the weaker problem:** formulate the selected zero orbit as a multiplier or extremal interpolation problem with a prescribed exponential type and solve the finite truncations with a proof of uniform convergence on the full complex zero multiset.

---

## 5.4 Reproducing-kernel limitation

In a reproducing-kernel Hilbert space,

$$
|K(z,w)|^2\le K(z,z)K(w,w),
$$

with strict inequality when the evaluation vectors are noncollinear. This controls the normalized correlation

$$
\frac{|K(z,w)|}{\sqrt{K(z,z)K(w,w)}},
$$

not the raw candidate peak

$$
\left|\frac{K(z,w)}{K(w,w)}\right|.
$$

The latter is below one only if a separate diagonal estimate \(K(z,z)\le K(w,w)\) is available on every other zero. Standard de Branges kernel arguments do not provide this ordering for the zeta nodes. Constructions that first place every zeta zero on the real spectral axis assume the zero-location statement being sought.

**Classification:** `conditionally applicable`; `circular` when the de Branges spectral sequence is assumed real.

**Cheapest test:** calculate the diagonal kernel \(K(\lambda_\rho,\lambda_\rho)\) on a non-RH-dependent candidate space and prove that the selected orbit uniquely maximizes it.

---

# 6. Other heat-flow and Laguerre–Pólya formulations

## 6.1 de Bruijn–Newman flow

**Citation.** Brad Rodgers, Terence Tao, “The de Bruijn–Newman Constant Is Non-Negative,” *Forum of Mathematics, Pi* **8** (2020), e6. DOI: **10.1017/fmp.2020.6**. arXiv:**1801.05914**. ([arXiv][17])

They study

$$
H_\tau(z)
=
\int_0^\infty e^{\tau u^2}\Phi(u)\cos(zu)\,du,
$$

which satisfies

$$
\partial_\tau H_\tau=-\partial_z^2H_\tau.
$$

The de Bruijn–Newman theorem supplies a finite constant \(\Lambda\) such that \(H_\tau\) has only real zeros exactly when \(\tau\ge\Lambda\). RH is equivalent to \(\Lambda\le0\). Rodgers–Tao’s **Theorem 1** proves

$$
\Lambda\ge0.
$$

The definitions and equivalence are stated at the beginning of the paper. ([arXiv][18])

### Failure of the map

The propagated property is **real-rootedness of an entire function**. The property required here is **pointwise nonnegativity of a translated Gaussian convolution**. There is no identity

$$
\Theta(t,\xi)=A(t,\xi)H_\tau(z)
$$

or positive transform relating the two, and no theorem converting real-rootedness of \(H_\tau\) into positivity of \(\Theta\).

The PDE sign resemblance is insufficient: its state variable, initial kernel, and invariant property differ.

**RH dependence:** the flow and threshold theorem are unconditional; real-rootedness at \(\tau=0\) is RH-equivalent.

**Classification:** `inapplicable`.

**Cheapest test:** exhibit an explicit intertwining operator taking \(H_\tau\) to \(\Theta(t,\cdot)\) and prove it preserves the relevant cone. No such operator was found.

---

## 6.2 Jensen polynomials

**Citation.** Michael Griffin, Ken Ono, Larry Rolen, Don Zagier, “Jensen Polynomials for the Riemann Zeta Function and Other Sequences,” *Proceedings of the National Academy of Sciences* **116** (2019), 11103–11110. DOI: **10.1073/pnas.1902572116**. arXiv:**1902.07321**. ([arXiv][19])

Their principal asymptotic theorem says that for each fixed degree \(d\), suitably shifted and rescaled Jensen polynomials formed from sufficiently high derivatives converge locally uniformly to the Hermite polynomial \(H_d\), hence are eventually hyperbolic.

**Negative-result citation.** David W. Farmer, “Jensen Polynomials Are Not a Plausible Route to Proving the Riemann Hypothesis,” *Advances in Mathematics* **411** (2022), 108781. DOI: **10.1016/j.aim.2022.108781**. arXiv:**2008.07206**.

Farmer’s Theorem 3.1 restates the Hermite convergence, and Sections 4–5 exhibit entire functions with deliberately displaced nonreal zeros whose high derivative/Jensen behavior has the same Hermite universality. Thus eventual Jensen hyperbolicity can coexist with off-axis zeros of the original function. ([arXiv][20])

### Failure of the map

The parameters are derivative index \(n\) and polynomial degree \(d\), not Gaussian variance \(t\) and translation \(\xi\). The propagated property is polynomial hyperbolicity, not pointwise positivity. Repeated differentiation can erase information about finitely or sparsely displaced off-axis zeros.

**Classification:** `inapplicable`; Farmer supplies a documented negative near-match.

**Cheapest test:** none within the existing Jensen formulation. A new identity tying a Jensen determinant directly to \(\Theta(t,\xi)\) would be required.

---

# 7. Result ledger

| Route                                              | Classification                  | Result for the present problem                                                    |
| -------------------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------- |
| Digamma asymptotic + absolute Gaussian prime bound | `applicable`                    | Excludes escape to infinity uniformly near every finite \(t_*>0\)                 |
| Prime almost-periodicity                           | `applicable` obstruction        | Rules out uniform cancellation below absolute prime mass                          |
| Angenent zero-number theorem                       | `inapplicable` for exclusion    | Classifies contact; permits the required double zero                              |
| Gaussian total positivity                          | `inapplicable` in reverse time  | Sign variation decreases only toward broader variance                             |
| Generic signed heat flow                           | `applicable` obstruction        | Explicitly realizes broad-scale positivity with a double-contact threshold        |
| Weil/Wong criterion                                | `conditionally applicable`      | Requires compact-factor approximation in the Weil-form topology                   |
| Burnol/Yoshida small-window positivity             | `conditionally applicable`      | Supplies unconditional compact windows, not noncompact Gaussian factors           |
| Suzuki support-flow continuity                     | `conditionally applicable`      | Gives an attained degeneracy in support parameter, not pointwise Gaussian contact |
| Zhu certified support \(1.6\)                      | `conditionally applicable`      | Supplies an explicit margin against which Gaussian truncation error can be tested |
| Gaussian Beurling–Selberg extremals                | `circular` as an order argument | Real-axis majorization does not order the Weil functional off RH                  |
| BRS cardinal interpolation                         | `conditionally applicable`      | Exact interpolation exists, but outside fixed Paley–Wiener type                   |
| Burnol Sonine evaluator system                     | `conditionally applicable`      | Biorthogonal zero evaluators exist in a different Hilbert space                   |
| Landau density theorem                             | `circular` on zeta nodes        | Real-node map assumes RH; separation is unproved                                  |
| Finite-type exact cardinal interpolation           | `inapplicable` by obstruction   | Impossible because \(R\log R\) nodes exceed \(O(R)\) zero capacity                |
| de Bruijn–Newman                                   | `inapplicable`                  | Real-rootedness flow does not map to pointwise positivity                         |
| Jensen/Laguerre–Pólya asymptotics                  | `inapplicable`                  | Hyperbolicity can persist despite displaced nonreal zeros                         |

# 8. Remaining finite problem

The escape theorem reduces a finite-threshold failure to

$$
t_*\in(0,\infty),\qquad \xi_*\in[-R,R],
$$

with

$$
\Theta(t_*,\xi_*)=0,
\qquad
\partial_\xi\Theta(t_*,\xi_*)=0.
$$

At \(t=t_*\), analyticity and nonnegativity imply that the zero has even multiplicity. Angenent’s theorem supplies its local parabolic topology but permits it.

The smallest currently supported reduction is therefore one of the following:

$$
\partial_\xi\Theta(t,\xi)=0
\quad\Longrightarrow\quad
\Theta(t,\xi)>0,
$$

proved directly on compact \(t,\xi\) regions with analytic tail bounds; or

$$
\left|
W(h_{t,\xi}-h_{t,\xi}^{(L)})
\right|
<
m_L\,
\|g_{t,\xi}^{(L)}\|_2^2,
$$

where \(h^{(L)}\) is constructed from compactly truncated inverse Gaussian factors and \(m_L\) is a certified localized Weil margin. Zhu’s current \(L=0.8\) result supplies one explicit value of \(m_L\). No located theorem completes either inequality globally.

[1]: https://arxiv.org/html/2005.02996 "https://arxiv.org/html/2005.02996"
[2]: https://www.nist.gov/publications/nist-handbook-mathematical-functions "https://www.nist.gov/publications/nist-handbook-mathematical-functions"
[3]: https://arxiv.org/html/2608.24827v2 "https://arxiv.org/html/2608.24827v2"
[4]: https://link.springer.com/article/10.1007/s44146-026-00264-3 "https://link.springer.com/article/10.1007/s44146-026-00264-3"
[5]: https://cds.cern.ch/record/471308?ln=sk "https://cds.cern.ch/record/471308?ln=sk"
[6]: https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/195/2/113609/explicit-formulas-for-the-spectral-side-of-the-trace-formula-of-rm-sl-2 "https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/195/2/113609/explicit-formulas-for-the-spectral-side-of-the-trace-formula-of-rm-sl-2"
[7]: https://arxiv.org/html/1608.02296 "https://arxiv.org/html/1608.02296"
[8]: https://arxiv.org/abs/math/0101068 "https://arxiv.org/abs/math/0101068"
[9]: https://arxiv.org/pdf/math.NT/0101068 "https://arxiv.org/pdf/math.NT/0101068"
[10]: https://projecteuclid.org/proceedings/advanced-studies-in-pure-mathematics/Zeta-Functions-in-Geometry/Chapter/On-Hermitian-Forms-attached-to-Zeta-Functions/10.2969/aspm/02110281 "https://projecteuclid.org/proceedings/advanced-studies-in-pure-mathematics/Zeta-Functions-in-Geometry/Chapter/On-Hermitian-Forms-attached-to-Zeta-Functions/10.2969/aspm/02110281"
[11]: https://arxiv.org/html/2606.09096v1 "https://arxiv.org/html/2606.09096v1"
[12]: https://eudml.org/doc/252338?utm_source=chatgpt.com "Remarks on Weil's quadratic functional in the theory of ..."
[13]: https://arxiv.org/abs/2606.09096?utm_source=chatgpt.com "Weil's quadratic form via the screw function"
[14]: https://arxiv.org/html/1008.4969 "https://arxiv.org/html/1008.4969"
[15]: https://arxiv.org/html/math/0203120 "https://arxiv.org/html/math/0203120"
[16]: https://arxiv.org/pdf/1512.01437 "https://arxiv.org/pdf/1512.01437"
[17]: https://arxiv.org/pdf/1801.05914 "https://arxiv.org/pdf/1801.05914"
[18]: https://arxiv.org/html/1801.05914 "https://arxiv.org/html/1801.05914"
[19]: https://arxiv.org/pdf/1902.07321 "https://arxiv.org/pdf/1902.07321"
[20]: https://arxiv.org/html/2008.07206v2 "https://arxiv.org/html/2008.07206v2"
