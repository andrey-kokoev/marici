# The 91 Saturated Hyperplanes Descend to 26 Explicit Norm Divisors

The character decomposition of the five-radical cover can be computed on the
three-dimensional base without retaining 91 separate cover hyperplanes.
Taking the deck norm of each orbit gives one base divisor.

For an edge orbit,

\[
(T+2y_i)(T-2y_i)=T^2-4R_i.
\]

For a four-element proper-section orbit with invariant part \(A\),

\[
\prod_{\epsilon_i,\epsilon_j=\pm1}
(A+\epsilon_i y_i+\epsilon_j y_j)
=
(A^2-R_i-R_j)^2-4R_iR_j.
\]

Consequently the 91 cover hyperplanes become exactly

\[
\boxed{1+5+20=26}
\]

base norm divisors: the invariant total-energy carrier, five edge norms, and
twenty proper-section norms. No choice of sheet enters this descent.

These 26 divisors are the poles of the descended rational marked form. The
twisted connection also has its five Kummer branch divisors \(R_i=0\).
Therefore the complete logarithmic support packet for the character complex
is

\[
\boxed{
\{q_G=0\}
\cup\{T^2-4R_i=0\}_{i=1}^5
\cup\{N_A=0\}_{A=1}^{20}
\cup\{R_i=0\}_{i=1}^5,
}
\]

with 31 labelled components before fiberwise removal of the parameter-only
total-energy factor. The extra five are existing edge-soft/Kummer branch
support, not new marked carrier divisors.

## Weight-five hostile block

For \(\chi_{12345}\), the rank-one Kummer connection on the base is

\[
\boxed{
\nabla_{12345}
=d+\frac12\sum_{i=1}^5d\log R_i.
}
\]

On Benincasa's frozen asymmetric slice, the corrected physical numerator has
a nonzero weight-five coefficient with 526 monomials, maximum degree 11, and
soft-parameter order zero. This proves that the physical source reaches the
hostile block, but it does not prove that its twisted cohomology class is
nonzero. In particular, this is a numerator statement: the physical
26-factor denominator is not deck invariant, so the coefficient is not yet
the weight-five component of the rational canonical form.

An independent sparse extractor now materializes that numerator coefficient exactly.
It selects the 222 source monomials odd in all five radicals, substitutes the
five quadratic Kummer relations, and obtains 526 base monomials with digest

\[
\mathtt{cdbe5ee6892a5571467ed15e230f7da47ba2dc7847659286840c339c64e750da}.
\]

The correctly typed rational component must first be formed as

\[
\Omega_\chi
=\frac1{32}\sum_{g\in C_2^5}\chi(g)g^*\Omega.
\]

Equivalently, let \(P_{\rm sat}\) be the invariant product of the 91 distinct
cover hyperplanes and compute

\[
H_\chi
=\frac1{32}\sum_g\chi(g)g^*N\frac{P_{\rm sat}}{g^*P}.
\]

Only after factoring
\(H_{12345}=y_1\cdots y_5h_{12345}\) does one obtain the base numerator for
twisted reduction. The 526-term packet is an independently verified
ingredient, not that final numerator.

A black-box implementation now evaluates the correctly projected rational
base function directly, without expanding \(P_{\rm sat}\):

\[
f_{12345}
=\frac{1}{32y_1\cdots y_5}
\sum_g\chi_{12345}(g)g^*\Omega.
\]

It is independent of every square-root choice and is nonzero at two
independent physical-cover samples, taking values \(517\bmod1009\) and
\(429\bmod1013\). This certifies the rational character component as a base
function while making no de Rham non-exactness claim.

The finite pilot is therefore:

1. use base variables \((u_1,u_2,u_3)\), treating external kinematics as
   parameters;
2. use the 26 marked norm divisors together with the five branch divisors
   \(R_i=0\) as the complete logarithmic support set;
3. construct the rational Fourier numerator \(h_{12345}\) with the saturated
   common denominator;
4. reduce the resulting physical weight-five form modulo
   \(\nabla_{12345}\)-exact forms;
5. compare the generic result with the total-energy specialization plus its
   first-Rees cone.

This replaces a 91-hyperplane, 32-sheet reduction by one rank-one twisted
three-variable reduction. A zero result would mean that full numerator
character support overcounts physical cohomology. A nonzero result would be
the first class forced by Kummer/intersection coherence despite the absence
of a weight-five divisor generator.

Artifacts:

- `research/nima/check_five_site_deck_norm_descent.py`
- `research/nima/extract_five_site_weight_five_coefficient.py`
- `research/nima/check_five_site_weight_five_rational_trace.py`
- `research/nima/results/five-site-deck-norm-descent.json`
- `research/nima/results/five-site-weight-five-coefficient.json`
- `research/nima/results/five-site-weight-five-rational-trace.json`
