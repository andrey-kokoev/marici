# Gaussian positivity promotes to Weil positivity

## Question

Does positivity of every translated Gaussian evaluation of the completed Weil distribution imply the full Weil criterion rather than only positivity on a restricted family?

## Claim boundary

Let `S(R)` be the Schwartz space and let

\[
\mathcal W\in\mathcal S'(\mathbb R)
\]

be the source-side completed Weil tempered distribution in the centered spectral coordinate. For `s>0`, set

\[
G_s(x)=\frac1{\sqrt{4\pi s}}e^{-x^2/(4s)}.
\]

Assume that the shifted-Gaussian kernel is the distributional convolution

\[
U(s,\xi)=(\mathcal W*G_s)(\xi)
=\langle\mathcal W,G_s(\xi-\cdot)\rangle
\]

and that

\[
U(s,\xi)\ge0
\qquad\text{for every }s>0,\ \xi\in\mathbb R.
\]

Then `W` is a positive tempered distribution. Consequently it pairs nonnegatively with every nonnegative Schwartz test. If the quadratic tests in the cited Weil criterion restrict on the centered real axis to nonnegative Schwartz functions and their Weil functional equals this pairing, the Riemann hypothesis follows.

The theorem does not prove Gaussian positivity. It proves the promotion arrow from all-scale, all-translate Gaussian positivity to the full criterion, conditional on the stated interface identification.

## The approximate-identity theorem

### Theorem

Let `T` be a tempered distribution. If

\[
(T*G_s)(x)\ge0
\]

for every `s>0` and every real `x`, then `T` is a positive distribution.

### Proof

Take a nonnegative compactly supported smooth function `phi`. Since `T*G_s` is a smooth function of polynomial growth,

\[
I_s=\int_{\mathbb R}(T*G_s)(x)\phi(x)\,dx
\]

is defined and nonnegative. Distributional Fubini and the evenness of `G_s` give

\[
I_s=\langle T,G_s*\phi\rangle.
\]

The Gaussian family is an approximate identity on the Schwartz space:

\[
G_s*\phi\longrightarrow\phi
\qquad\text{in }\mathcal S(\mathbb R)
\]

as `s` decreases to zero. Continuity of `T` therefore yields

\[
\langle T,\phi\rangle
=\lim_{s\downarrow0}I_s\ge0.
\]

Thus `T` is positive on every nonnegative compactly supported smooth test, which is the definition of a positive distribution.

### Extension to nonnegative Schwartz tests

A positive distribution is a positive Radon measure. Because `T` is also tempered, that measure has polynomial growth. For any nonnegative Schwartz function `h`, choose nonnegative compactly supported smooth cutoffs `chi_R` increasing pointwise to one. Then

\[
\langle T,\chi_R h\rangle\ge0.
\]

Polynomial growth of the measure and rapid decay of `h` permit passage to the limit, giving

\[
\langle T,h\rangle\ge0.
\]

No finite cutoff is promoted by itself: the limit uses the tempered positive-measure theorem and Schwartz decay.

## Interface with multiplicative Weil tests

Let

\[
g\in C_c^\infty(\mathbb R_+^\times).
\]

Pass to logarithmic coordinates and include the standard half-density normalization. Its centered Mellin transform has the form

\[
F_g(u)=\widehat g\!\left(\frac12+iu\right).
\]

For the multiplicative involution appearing in Weil's criterion, the quadratic test restricts on the real centered line to

\[
h_g(u)=F_g(u)\overline{F_g(u)}=|F_g(u)|^2\ge0.
\]

Compact smooth support of `g` gives rapid decay of `F_g` on the real line by repeated integration by parts, hence `h_g` is Schwartz. If the source-side explicit formula identifies

\[
W(g*\overline g^{\,\tau})=\langle\mathcal W,h_g\rangle,
\]

positivity of `W` implies

\[
W(g*\overline g^{\,\tau})\ge0
\]

for every such `g`. This is the nonnegativity condition in Weil's criterion.

## Parameter map

The prior Gaussian uses

\[
e^{-t(u-\xi)^2}.
\]

The normalized heat kernel has exponent `-(u-xi)^2/(4s)`, so

\[
s=\frac1{4t}.
\]

Multiplication by the positive scalar `sqrt(t/pi)` converts the unnormalized Gaussian to `G_s`. Therefore positivity of `Theta(t,xi)` for every positive `t` and real `xi` is equivalent to positivity of `(W*G_s)(xi)` for every positive `s` and real `xi`. The factor-four symmetrization convention is also positive and has no effect on this implication.

## Potential failure modes and their resolution

1. **Only one Gaussian scale.** Positivity at one `s` does not determine the sign of `W`; the theorem requires every `s>0`.
2. **Only the zero character.** Positivity at `xi=0` does not test arbitrary translates; every real `xi` is required.
3. **Backward heat inference.** No backward maximum principle is used. The proof takes the assumed nonnegative convolutions directly to the distributional limit.
4. **Pointwise positivity of an autocorrelation.** A multiplicative autocorrelation need not be pointwise nonnegative before transformation. The relevant centered spectral restriction is `|F_g|^2`, which is nonnegative.
5. **Unsupported test-space extension.** Compact tests enter first. Extension to Schwartz tests uses positivity plus the tempered-measure representation, not an unproved uniform finite cutoff.
6. **Complex zero nodes.** The proof is source-side. It does not represent off-line zero evaluations as a real measure. Weil's criterion supplies the separately reviewed arrow from source functional positivity to zero location.

## Direct verification of the Weil-criterion interface

The source archive for Wong, arXiv:1608.02296, has SHA-256 `d348ce724aaa7013d0d8d06cafb42a5a5cd54b01831cce2577828c099cd2e87e`. Source lines 221--240 define `g in C_c^infty(R_+^times)`,

\[
g^*(x)=x^{-1}g(x^{-1}),
\qquad
\widehat g(s)=\int_0^\infty g(x)x^{s-1}\,dx,
\]

and the completed explicit functional. Lines 340--360 state the Weil criterion for `g*bar(g)^*`. Direct calculation from Wong's convolution at lines 342--346 gives

\[
\widehat{g*\overline g^{\,*}}(s)
=\widehat g(s)\,\overline{\widehat g(1-\overline s)}.
\]

On the critical line `s=1/2+iu`, this is exactly

\[
\left|\widehat g\!\left(\frac12+iu\right)\right|^2.
\]

Wong states the condition as nonnegativity with equality only for zero `g`. The converse argument at line 360 says that an off-line zero produces a test with negative functional value. Therefore nonnegativity alone already excludes off-line zeros; strictness is not needed for the implication used here. Once RH follows, the stronger equality statement can be treated separately.

The BRS formula and Wong's first explicit formula both define their functional by the completed zero sum. Their test presentations differ, but on the centered line the logarithmic-coordinate pullback above supplies the required nonnegative Schwartz restriction. A publication version should cite both formulas and display this pullback; no unverified sign or half-divisor conversion remains in the promotion arrow.

## Disposition

Item 5 is closed at theorem level: proving `Theta(t,xi)>=0` for every positive `t` and real `xi` makes the completed source distribution positive, hence makes Wong's quadratic functional nonnegative and implies RH. The unresolved mathematical core remains all-scale Gaussian positivity, equivalently finite double-contact exclusion after broad positivity and character coercivity.
