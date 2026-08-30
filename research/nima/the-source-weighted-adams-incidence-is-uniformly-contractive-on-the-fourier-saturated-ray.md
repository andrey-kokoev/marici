# The source-weighted Adams incidence is uniformly contractive on the Fourier-saturated ray

## The weight is upstream of analytic synthesis

The source prime-power atom at grade \(k\) is

\[
u_{p,k}
=
\begin{pmatrix}
g_{k\log p}\\
h_{k\log p}
\end{pmatrix},
\qquad
\|u_{p,k}\|=\|\Phi\|_2.
\]

The arithmetic-to-analytic incidence is defined on the finite source core by

\[
\mathcal I e_{p,k}
=
w_{p,k}u_{p,k},
\qquad
w_{p,k}
=
\frac1k p^{-k/2}.
\]

Thus the Euler half-density and orbit factor are applied before summation,
closure, Green normalization, determinant, or scalar readout. This is the
constructor order required by the Adams loading theorem.

There is no grade-zero or multiplicative-unit atom in this incidence. The
tensor unit remains in the separately retained wall channel.

## Relative Adams transport

For a grade-raising operation \(k\mapsto rk\), define the relative weight

\[
\rho_r(p,k)
=
\frac{w_{p,rk}}{w_{p,k}}
=
\frac1r p^{-(r-1)k/2}.
\]

For every nontrivial Adams operation \(r\ge2\),

\[
|\rho_r(p,k)|
\le
\frac12\,2^{-1/2}
<
1.
\]

If one retains only the half-density part and types the orbit factor \(1/r\)
separately, the weaker uniform estimate is still

\[
p^{-(r-1)k/2}
\le
2^{-1/2}.
\]

Hence either authorized factorization gives a strict Adams-ray loading gap.
The full source coefficient gives the sharper bound.

## Word telescoping

For a word of Adams raisings

\[
k=k_0\longmapsto k_1\longmapsto\cdots\longmapsto k_n,
\qquad
k_{j+1}=r_jk_j,
\]

the relative coefficients telescope:

\[
\prod_{j=0}^{n-1}\rho_{r_j}(p,k_j)
=
\frac{w_{p,k_n}}{w_{p,k_0}}
=
\frac{k_0}{k_n}p^{-(k_n-k_0)/2}.
\]

Therefore constructor depth cannot create norm amplification in the weighted
incidence coordinate. The coefficient decreases with final grade, independent
of the chosen factorization of the Adams word.

This also supplies path coherence for the scalar weight:

\[
\rho_{rs}(p,k)
=
\rho_s(p,rk)\rho_r(p,k).
\]

No normalization holonomy remains on the grade ray.

## Fourier-orbit lift

The four analytic presentations are

\[
\pi_j(u)
=
\mathcal F^j\pi_0(u)\mathcal F^{-j},
\qquad
j\in\mathbb Z/4.
\]

Fourier cyclically permutes them, while prime labels, grades, and the
coefficient \(w_{p,k}\) remain external. Every transported history has the same
source-Gram norm by unitary conjugation.

Consequently the unsaturated weighted estimate lifts termwise to

\[
Q_{\mathrm{sat}}
=
\sum_{j=0}^{3}(\mathcal F^j)^*Q\mathcal F^j
\]

without additional loss. Fourier saturation contributes a finite permutation,
not constructor-depth growth.

## Cutoff compatibility

Prime cutoff projections act on labels, whereas Fourier orbit completion acts
inside each analytic feature fiber. Thus

\[
P_X\pi_j(u_{p,k})
=
\pi_j(P_Xu_{p,k}),
\]

and the weighted incidence obeys

\[
P_X\mathcal I=\mathcal I P_X
\]

on the finite core. The same identities hold in every Fourier presentation.

The primitive channel remains rigged rather than Hilbert--Schmidt, but this
does not affect the source-core contraction or the strong-dual truncation
result on its fixed exponential-order rung. Square and connected grades retain
their Hilbert--Schmidt and nuclear gains.

## Endpoint compatibility

The wall coordinate is not part of the weighted Adams incidence. It is
transported by the split tensor-unit retract.

The odd endpoint coordinate is sent through the source-derived causal
evaluation

\[
d_p
=
H_{\mathrm{jump}}b_p
=
-2j_\theta b_p.
\]

Since the Euler coefficient already multiplies the labelled source atom,
curried odd evaluation cannot reintroduce an unweighted unit channel. The
Hadamard wall--jump frame fixes the reciprocal character before this analytic
evaluation.

## Quantitative conclusion

On nontrivial prime-power grades, the source-weighted Adams incidence has a
uniform one-step bound strictly below one. Along arbitrary Adams words, its
coefficient norm decreases by the exact telescoping factor

\[
\frac{k_0}{k_n}p^{-(k_n-k_0)/2}.
\]

The same estimate holds on the Fourier-saturated pro-Gram because the four
presentations are unitary conjugates and the coefficient is presentation
independent.

Thus the Adams grade ray has:

- no order escape after intensive regrading;
- no scalar normalization holonomy;
- no weighted incidence amplification;
- a strict nonunit loading gap;
- and cutoff-compatible Fourier saturation.

## Scope boundary

This proves weighted semigroup control for the source-generated linear Adams
incidence and its odd endpoint evaluation. It does not prove that every other
constructor in the nine-operation domain is uniformly bounded, nor that the
terminal scalar readout has a mixed-cancellation margin.

It also does not identify the full positive Green operator with the completed
zeta defect. Those remain downstream obligations.

## Hostiles

1. Apply \(p^{-k/2}/k\) only after scalar synthesis. The operator incidence is
   then unweighted and first-order dilation saturates.
2. Include the tensor unit in the same incidence block. Its coefficient is one
   and the strict gap disappears.
3. Let Fourier act on the arithmetic coefficient. Presentation-dependent
   weights destroy cyclic naturality.
4. Replace the exact relative weight by independent edge normalizations. Word
   products can then acquire path-dependent drift.
5. Bound each Adams generator but ignore the telescoping law. This misses the
   actual depth-uniform certificate.

## Verdict

The frozen source incidence places the Euler half-density before analytic
completion, and its relative Adams weights form an exact contractive
cocycle. The Fourier-orbit comparison lifts this certificate to the saturated
pro-Gram without loss.

The Adams generator is therefore no longer the earliest unresolved
constructor-stability gate. The next audit must move to the remaining
generators and their comparison cells, beginning with seam transport composed
with endpoint attachment.
