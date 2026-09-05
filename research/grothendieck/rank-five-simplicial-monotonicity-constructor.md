# Rank-five monotonicity needs a source constructor before simplicial composition

## Question

Can the rank-five Newton–`LDL*` pivot be transported from the certified
endpoint to every ordered configuration by constructive monotonicity arrows?

## Claim boundary

Let

\[
 \Delta_5=\{0\le x_1\le\cdots\le x_5\le0.01\}
\]

and let `d5(x)` be the fifth pivot of the normalized divided-difference
matrix already implemented by the rank-five checkers. The target theorem is

\[
 x\le y\quad\Longrightarrow\quad d_5(x)\ge d_5(y),
\]

where the order is coordinatewise and both points lie in `Delta_5`. Combined
with the certified endpoint value, this would prove `d5>0` throughout the
ordered simplex. It would not prove arbitrary-rank positivity, positivity
outside the declared interval, Weil positivity, or RH.

The endpoint cell supplies a first generating-arrow constructor. On its inner
radius `0.0005`, all five derivative uppers are negative after including the
analytic source and rational inversion remainders. The first four are below
`-1.4096e-28`; the fifth is below `-1.2239e-27`.

## Bold conjecture

The fifth pivot is coordinatewise decreasing on `Delta_5`, and its derivative
admits a source-derived nonpositive factorization compatible with Newton
elimination. Such a factorization supplies generating monotonicity arrows;
Rzk may then verify composition and coherence without being asked to invent
the analytic sign.

## Named rivals

1. No global sign factorization exists, but directed small-cell derivative
   certificates form a finite cover of `Delta_5`.
2. The pivot is positive on `Delta_5` but not coordinatewise monotone; value
   certificates can close positivity while endpoint transport cannot.
3. A negative derivative or pivot occurs between the tested anchors, refuting
   the monotonicity or positivity claim respectively.
4. A Gram-contraction identity supplies finite-step arrows directly, making a
   derivative factorization unnecessary.

## Risky consequences and falsification

A structural proof must derive one of the following without assuming the
required sign:

- `partial_i d5 = -N_i` with source-derived `N_i>=0`;
- a finite-step comparison `d5(x+delta e_i)<=d5(x)` on every admitted step;
- a Gram contraction whose residual squared norm is exactly `d5`.

The strongest immediate falsifier is a directed cell with a strictly positive
lower bound for one coordinate derivative, or a negative upper bound for the
pivot. An interval containing zero is a representation residual, not a
counterexample.

For a derivative proof, the checker must include source-tail and rational
inversion remainders. For a finite-cover proof, it must verify coverage,
boundary cells, collision strata, and denominator separation. For an Rzk
encoding, generating arrows must carry one of these admitted analytic
witnesses; Segal composition alone has no sign authority.

## Disposition

Active. First derive and simplify the differentiated Schur-complement/Newton
pivot formula, then test whether its numerator has a source-positive or
sum-of-squares factorization. Use directed small-cell certificates as hostile
falsifiers and as a fallback finite-cover constructor. Do not begin Rzk
composition until a generating analytic witness exists.

## Schur derivative decomposition

Writing the normalized Newton matrix in block form

\[
 M=\begin{pmatrix}A&b\\ b^{\mathsf T}&a_{55}\end{pmatrix},
 \qquad c=A^{-1}b,
\]

the fifth pivot is `d5=a55-b^T A^-1 b`. Stationarity of the Schur
complement gives the exact generating formula

\[
 \partial_i d_5=\partial_i a_{55}
 -2(\partial_i b)^{\mathsf T}c
 +c^{\mathsf T}(\partial_i A)c.
\]

The directed checker verifies this identity against the differentiated `LDL*`
recursion at the endpoint for all five coordinates. Every resulting enclosure
is strictly negative. However, the three displayed terms have scale about
`1e-22` and cancel to a derivative of scale `1e-28`. Their individual signs
therefore do not prove monotonicity. The next structural step must factor this
six-order cancellation before interval transport; treating the three terms as
independent boxes would discard the sign.

- Checker: `checkers/central_rank_five_schur_derivative.py`
- Result: `results/central-rank-five-schur-derivative.json`

The same cancellation can be retained invariantly by the determinant ratio

\[
 d_5=\frac{\det M_5}{\det M_4},\qquad
 \partial_i d_5=
 \frac{\det(M_4)\,\partial_i\det(M_5)
 -\det(M_5)\,\partial_i\det(M_4)}{\det(M_4)^2}.
\]

At the endpoint, direct Leibniz interval evaluation certifies the numerator
negative for all five coordinates and encloses the differentiated `LDL*`
answer. For the first coordinate the numerator lies near
`-1.3037846766e-105`. This packages the cancellation into one source-invariant
minor expression. It does not yet explain its sign throughout `Delta_5`; the
next target is a total-positivity or compound-matrix identity making this
numerator nonpositive without determinant expansion.

- Checker: `checkers/central_rank_five_determinant_ratio_derivative.py`
- Result: `results/central-rank-five-determinant-ratio-derivative.json`

## Moment-carrier test

The raw coefficient sequence is not a Stieltjes moment sequence: among Hankel
minors of ranks one through five and shifts zero through nine, 13 are directed
negative, beginning with the rank-one shift-one coefficient. Therefore raw
Hankel total positivity cannot explain the sign.

For the alternating sequence `g_n=(-1)^(n-1) f_n`, direct Leibniz boxes
initially made 45 of the same 50 minors positive and left five unresolved.
Directed `LDL*` preserves the Hankel correlations. Raising the independently
controlled eta-series source depth from 300 to 500 narrows the high-order
coefficient intervals and resolves every former residual: all 50 tested
alternating Hankel minors are directed positive. This remains a finite test
through rank five and shift nine, not a positive-measure construction.

An extended `LDL*` sweep used every Hankel matrix supported by coefficients
through degree 49, with ranks through ten. At 90-digit directed arithmetic, 136 of 400 cases are positive and 264 are
unresolved, with the first unresolved rank-one coefficient at shift 27.
Including `B18` explicitly and bounding omitted `B20` does not move that
boundary. Raising directed arithmetic to 160 digits certifies 207 cases and
moves the first unresolved rank-one coefficient to shift 34; 193 cases remain
unresolved and none is negative. This confirms arithmetic precision as a real
axis of the finite residual, while supplying no finite-to-global promotion. This is finite evidence for, but not construction of,
a positive moment measure. If a source-derived measure `mu` satisfies

\[
 g_n=\int t^{n-1}\,d\mu(t),
\]

then the Loewner kernel has the Gram form

\[
 K_F(x,y)=\int\frac{d\mu(t)}{(1+tx)(1+ty)}.
\]

Its Newton divided differences are generated by rational features with
products of `(1+t x_i)` in the denominator. This is the first candidate common
source carrier capable of preserving the determinant cancellation. The next
acceptance test is to resolve the five undecided twisted Hankel minors and
derive the moment representation from the theta source; finite minors alone
do not provide a global measure or monotonicity theorem.

- Checker: `checkers/central_F_hankel_moment_probe.py`
- Result: `results/central-F-hankel-moment-probe.json`

The measure construction is not a low-cost auxiliary lemma. If `mu>=0`
exists with the displayed moments, then the integral formula makes every
finite Loewner matrix on its convergence domain a Gram matrix, not merely the
rank-five matrix. Thus a source derivation of `mu` would supply an all-rank
positivity promotion. It must not be obtained from a zero expansion that
already assumes the required zero locus or from the finitely positive Hankel
minors. The admissible derivation must start from the eta/gamma/theta source
used by `central_H_degree_eleven_interval.py` and prove positivity of the
representing functional independently. Until that arrow exists, the moment
route is a reformulation of the central all-rank gate rather than a completed
explanation.

## RH-conditional atom audit

Let a critical-line zero pair have centered coordinates `q=+-i gamma` and put
`r=gamma^2>0`. In the squared coordinate `x=q^2`, its logarithmic-derivative
atom is `1/(r+x)`. Multiplication by the implemented prefactor gives

\[
 F_r(x)=\frac{4x-1}{r+x}.
\]

Subtracting its constant term yields

\[
 F_r(x)-F_r(0)=
 \frac{4r+1}{r^2}\frac{x}{1+x/r}.
\]

Thus the conditional measure has location `u=1/r` and positive mass
`w=(4r+1)/r^2`. Its kernel atom is

\[
 \frac{F_r(x)-F_r(y)}{x-y}
 =\frac{4r+1}{(r+x)(r+y)}
 =\frac{w}{(1+ux)(1+uy)}.
\]

The exact checker verifies the increment, kernel, and alternating-moment
identities over rational fixtures, including a deliberate negative-mass
failure. This establishes the algebra of one RH-conditional zero pair. It does
not justify summing over zeros, convergence, the absence of additional entire
terms, or the converse from a positive measure to critical-line localization.

- Checker: `checkers/rh_conditional_stieltjes_atom_identity.py`
- Result: `results/rh-conditional-stieltjes-atom-identity.json`

## Pole-locus converse

A complete-Bernstein representation is analytic away from the negative real
cut. A nontrivial zero `rho` gives a logarithmic-derivative pole at

\[
 t_\rho=(\rho-1/2)^2.
\]

The prefactor `4t-1` can cancel such a pole only at `t=1/4`, corresponding to
the endpoints `s=0,1`, not a nontrivial zero of the completed function. Hence
a proved global representation forbids every zero pole off the negative cut.
Writing `rho-1/2=a+ib`, the imaginary part of `t_rho` is `2ab`; negative-real
`t_rho` forces `a=0`. Real centered zeros map to the positive axis and are
also forbidden by analyticity there. Therefore the representation implies
`Re(rho)=1/2`, provided the analytic identification proves that every
nontrivial zero contributes an uncancelled pole and that no source term
cancels it.

- Checker: `checkers/stieltjes_pole_locus_converse.py`
- Result: `results/stieltjes-pole-locus-converse.json`

The uncancelled-pole condition has a local exact form. Centered completed xi is
an even entire function by its functional equation, so it descends as
`xi(1/2+q)=G(q^2)` for an entire `G`. If `G(t)=(t-tau)^m h(t)` with
`h(tau)!=0`, then `G'/G` has residue `m`, and the implemented function has
residue

\[
 m(4\tau-1).
\]

This vanishes only at `tau=1/4`, whose centered preimages are `q=+-1/2`, or
`s=0,1`. The completed function is nonzero there. Hence every nontrivial zero
produces an uncancelled pole. This closes the local cancellation alternative,
conditional only on matching the implemented eta/gamma normalization to the
standard entire completed xi. The unresolved hard step is now the direct
source proof of the global positive representation.

- Checker: `checkers/xi_squared_coordinate_pole_residue.py`
- Result: `results/xi-squared-coordinate-pole-residue.json`

## Direct positive-measure attempt

The source Fourier/theta representation gives the entire squared-coordinate
function `G`, while the proposed measure concerns the nonlinear quotient

\[
 F(x)=(4x-1)\frac{G'(x)}{G(x)}.
\]

Positivity of the theta density does not pass through this quotient. A direct
complete-Bernstein proof must establish both that `G` has no zeros off the
negative cut and that the boundary imaginary part of `F` has the sign needed
for Stieltjes inversion. The first requirement is already the pole-locus form
of RH. Rewriting `G'/G` as a zero sum produces the desired positive atomic
measure only after critical-line localization has been assumed, so it is not a
source proof.

The coefficient route reaches the same boundary in real algebra. A positive
measure exists if the alternating moment functional is positive on every
square and on `t` times every square, together with the required completion
and growth conditions. The finite Hankel tests verify bounded restrictions of
those forms, but the universal positivity statement is the missing all-rank
theorem. No source-derived finite-generation or compactness theorem promotes
the tested restrictions.

Disposition: the direct attempt does not yet construct a measure. Its first
missing typed object is a source proof of the Pick boundary sign, or
equivalently universal positivity of the alternating Hankel forms. Acceptance
requires that proof without a zero expansion or RH-equivalent assumption.
