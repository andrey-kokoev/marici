# Iteration5: independently enclosed full-divisor comparison

## What each triangle actually computes

**Bare seed:** each triangular occurrence cycles three coefficient amplitudes.
The cycles AB,BC,CA and BA,AD,DB do not themselves evaluate primes, gamma or
zeta zeros. The raw shared cochain edge is BA=-AB; it alone does not identify
all the private face coefficients or force equal outputs.

**RH-decorated arithmetic face:** on a common analytic polarized test h_c,
its source evaluator computes endpoint moments + gamma multiplier integral
minus weighted logarithmic prime-power translation correlations. Iteration4
freshly generated those operations and certified their errors.

**RH-decorated spectral face:** its source evaluator computes

    Z(c)=(1/2) sum_rho m(rho) h_c((rho-1/2)/i).

Iteration5 independently computes this full-divisor packet through a complete
window plus a rigorous infinite-tail enclosure. It never defines the missing
spectral tail as the arithmetic residual. These computations are classical
analytic evaluators attached beside the carriers, not native face algorithms.

**Decorated common edge:** it identifies the test descriptor (t,a,c), its
analytic continuation, Fourier convention, multiplicities, evenization and
half-divisor factor. Equality follows from the inspected classical explicit
formula, not from AB=-BA alone. RH concerns positivity on the complete
appropriate test domain; equality itself is unconditional.

## 1. Complete divisor window, not a positive-zero scout

Installed python-flint0.9.0 / FLINT3.6.0 provides rigorous balls and a total
zeta zero count. The actual documentation was inspected; its count includes
all zeros with positive imaginary part and their multiplicities.

At T=80, N(T)=21, also constant in a small neighborhood of80. The21 proposed
critical-line locations are enclosed in disjoint rational brackets. At each
bracket's endpoints the completed function

    xi(s)=s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2

has opposite certified real signs on s=1/2+i gamma. It is real on this line by
the functional equation and conjugation. The intermediate value theorem
therefore gives at least one critical-line root in each bracket. The total
multiplicity count21 proves that each is simple and there are no omitted
off-critical roots in this window. A ball evaluation merely containing zero
is not used as the existence proof.

There are no nontrivial real zeros: for0<s<1 the alternating eta series is
positive, while its zeta denominator1-2^(1-s) is negative. Conjugation supplies
the complete negative-ordinate half. These are finite-window facts, not an
assumption of RH beyond80.

## 2. An unconditional all-height count majorant

A deliberately coarse bound suffices:

    N(v) <= (v+3)^2,  v>=13.

Here is the derivation, not a fit to computed counts. Put

    psi_theta(x)=sum_(n>=1) exp(-pi n²x).

Mellin-transform the Gaussian theta series for Re(s)>1, split the integral at1
and apply Poisson summation. This gives the entire completed-function identity

    xi(s)=1/2 + s(s-1)/2 integral_1^infinity
                    [x^(s/2-1)+x^((1-s)/2-1)] psi_theta(x) dx.

The rational contribution from the interval(0,1) is1/[s(s-1)] before
multiplication. Uniform exponential convergence continues the identity to C.
For x>=1, n²>=1+3(n-1) gives psi_theta(x)<=2exp(-pi x).

Let R=v+2, r=2R and k=r/2=v+2. On |s-2|<=r, both powers of x are at most x^k,
|s(s-1)|<=(r+2)(r+1), and consequently

    |xi(s)| <=1/2+2(r+2)(r+1) Gamma(k+1)/pi^(k+1)
             <=9(k+1)^(k+3).

The last inequality uses Gamma(k+1)<=(k+1)^(k+1): log-convexity bounds it by
the adjacent integer factorials, each bounded by the larger integer raised to
itself. This larger integer is at most k+1.

Since xi(2)=pi/6>1/2, Jensen's formula between radii R and2R bounds the total
number n(R) of zeros in the inner disk by

    n(R) <=[log18+(v+5)log(v+3)]/log2.

Every nontrivial zero with ordinate at most v in magnitude lies in that disk:
0<=Re(rho)<=1 and |rho-2|<=sqrt(v²+4)<R. In particular N(v)<=n(R).
Writing x=v+3>=16, log18<3, log2>1/2 and log x<=x/4 give

    n(R) <6+x²/2+x <=x².

The log inequality follows from its value at16 and derivative1/4-1/x>=0;
the final polynomial inequality likewise holds from16 onward. The checker
verifies the anchor constants with Arb. This is an analytic bound for every
height, not a numerical extrapolation. No critical-line hypothesis is used.

## 3. Full tail admits off-critical spectral parameters

For each feature pair,

    h_ij(u)=b_ij exp[-t(u-xi_ij)²],
    b_ij=exp[-t(a_i-a_j)²/4], xi_ij=(a_i+a_j)/2.

A nontrivial zero rho=beta+i gamma gives
u=gamma-i(beta-1/2), so

    |h_ij(u)| <= b_ij exp(t/4) exp[-t(gamma-xi_ij)²].

This uses only beta in[0,1]. It does not replace u by its real ordinate.
For q=|xi_ij|<T, f(v)=exp[-t(v-q)²] is decreasing on v>=T. Conjugation and
the half-divisor factor yield the absolute remainder bound

    |tail_ij| <=b_ij exp(t/4) integral_(T,infinity) f(v)dN(v).

Integration by parts, dropping the nonpositive boundary term, and the
all-height count majorant give

    |tail_ij| <=b_ij exp(t/4) {
       exp[-t(T-q)²] [(T+3)²+1/t]
       +(q+3)sqrt(pi/t) erfc[sqrt(t)(T-q)] }.

All six bounds are certified below1e-140. The full divisor matrix is real by
conjugation and functional-equation symmetry, so these absolute bounds widen
its real entry enclosures. The unknown tail is bounded, not assigned zero.
A synthetic off-critical quartet still evaluates negatively, while incorrectly
projecting it to real ordinates evaluates positively; the control passes.

## 4. Independent arithmetic/spectral comparison

The spectral producer computes counts, brackets, spectral weights and infinite
tails **before opening the arithmetic result**. It then verifies that its
parameter contract matches iteration4 and that the retained source hashes
still agree with fresh mutable files.

All six independently computed full-divisor enclosures overlap the generated
arithmetic enclosures. Doubling the divisor factor gives disjoint enclosures
and is rejected. Overlap is a certified consistency test, not an assertion
that finite-precision midpoints are exactly equal. Analytic equality is justified
separately by the inspected explicit-formula theorem.

The previous16-positive-zero scout is not used. The complete21-zero window and
unconditional tail now close the numerical full-divisor enclosure gate for
this fixed three-Gaussian span. Fresh spectral interval LDL, computed before
reading arithmetic values, also has strictly positive pivots. It independently
certifies positivity on this finite span, not the full RH test domain.

## 5. Does the same comparison survive in both structures?

Yes **as signed finite forms**, with the neutron metric preserved. Rebuild both
native carriers and attach exact rational midpoint forms for arithmetic,
full divisor and their difference. All three signed pullbacks are checked.

The lifts are affine in the form. For B(G)=X+Y D^-1G,

    B(G_A-G_Z)=B(G_A)-B(G_Z)+X.

Without the reinserted common source X, the naive difference lies entirely in
the null sink and has zero signed form. The corrected comparison lift passes
in both carriers. Certified coefficient errors remain separate from these
exact midpoint identities.

This does **not** imply native processing equivalence. The stage ranks remain
proton(12,3,1) and neutron(3,12,1). Their primitive cycles/projectors do not
perform the Gaussian, gamma, prime or zero-count algorithms.

## 6. Status and continuation

Artifacts:

- `inputs/rh-full-divisor-window-v1.json`.
- `checkers/check_rh_full_divisor_window.py`.
- `results/rh-full-divisor-window-v1.json`.
- `references/flint-zeta-window-contract-v1.md`.

Run the checker for a fresh headless closure. Shared source-owner stores are
read-only. The full-divisor comparison is now independently bounded on the
finite test span; it still is not the complete RH positivity condition.

Next nonredundant obligation: audit the full-test encoding capacity before
constructing an operation-bearing analytic completion. A larger independently
positive Gaussian span can be compared with the native signed form's positive
index. That tests whether one fixed linear encoder can preserve the actual
arithmetic/spectral forms, rather than using a different point attachment for
each query. Preserving only their zero difference would be vacuous.

An analytic completion must then be explicitly distinguished from native
finite-generator execution. Any extension must carry its test-domain
quantifiers and continuity/topology, not infer global positivity from these
three Gaussians. No RH proof or particle dynamics is claimed.
