# All-prime leakage has a weighted-dual limit and a source endpoint subtraction

## Strength and result

The unregularized all-prime full-line L2 operator limit is obstructed, as proved in Grothendieck's supplied note. There is nevertheless a concrete operator-norm limit in an explicitly weaker, exponentially weighted dual target. Its endpoint subtraction is independently derived from the continuum part of the Mangoldt measure and the first archimedean tail, not fitted from the desired Clark scalar.

The residual is controlled in that weighted target. Ordinary unweighted L2 convergence of the residual is NOT inferred; its precise remaining prime-fluctuation transform is displayed below.

Inputs:
- `../grothendieck/all-prime-tate-leakage-diverges-on-the-common-euler-source-domain.md`
- `the-trivial-sector-arithmetic-form-is-a-tate-compression-with-explicit-leakage.md`
- `a-subtracted-gamma-shift-operator-completes-the-one-slot-euler-green-form.md`

## 1. The old graph topology genuinely fails

For nonnegative f supported in (0,L), L<log 2, the source prime leakage satisfies

    ||sum_(p in P) leak_p f||_2^2
      >= ||f||_2^2 sum_(p in P) (log p)^2/(p-1) -> infinity.

Cross-prime terms are nonnegative, not assumed orthogonal. The fixed archimedean L2 vector cannot cancel this norm divergence. The same obstruction holds on positive Euler exponential states. The fresh supplied checker passes.

Thus the next construction changes the target topology explicitly. It is not described as a recovered strong/weak limit in the old full-line Hilbert space.

## 2. A weighted dual target with an operator-norm limit

Fix alpha>1/2 and use

    H_alpha^+=L2(R_+,exp(2 alpha u)du),
    K_alpha=L2(R,exp(-2 alpha |u|)du).

K_alpha is the continuous scalar-dual carrier, under the unweighted integral, of L2(R,exp(2 alpha |u|)du). It embeds into distributions on compact tests, but its elements need not be tempered. No ordinary Fourier multiplier on the limit space is being presumed.

For f in H_alpha^+, let E_+f be zero extension. Full-line translations S_a h(u)=h(u+a) obey

    ||S_a E_+f||_Kalpha <= exp(-alpha a)||f||_Halpha,
    ||S_(-a) E_+f||_Kalpha <= exp(-alpha a)||f||_Halpha,

for a>=0. The first estimate uses |x-a|>=a-x after substituting x=u+a; the second is immediate from u=x+a>=0.

Therefore the source-defined prime series

    P_infinity f = sum_(n>=2) Lambda(n)n^(-1/2)
                   [S_(log n)+S_(-log n)]E_+f

converges absolutely in operator norm H_alpha^+ -> K_alpha. Its norm is at most 2 sum Lambda(n)n^(-alpha-1/2).

If the finite-place cutoff contains every prime <=N, its omitted prime powers are among n>N. With sigma=alpha+1/2>1, for sufficiently large N the operator tail is at most

    2 N^(1-sigma)[log N/(sigma-1)+1/(sigma-1)^2].

This is the actual limit of the finite prime operators on positive-half-line source vectors, now in K_alpha. It is not an absolute square-sum of unitary prime channels.

The archimedean map Atilde_infty E_+ is bounded from D_alpha=H^1(R_+,exp(2 alpha u)du) to ordinary full-line L2 by the previously proved graph bound, hence also to K_alpha. Thus

    T_infinity=Atilde_infty E_+ + P_infinity : D_alpha -> K_alpha

is the operator-norm limit of the finite-place source-to-full-line maps.

## 3. Derive the growing prime endpoint mode

Write the negative coordinate as u=-v, v>0. For a smooth compactly supported source f on [0,infinity), the prime leakage is locally the finite sum

    P_infinity f(-v)=sum_(n>exp(v)) Lambda(n)n^(-1/2) f(log n-v).

Let psi(t)=sum_(n<=t) Lambda(n), E(t)=psi(t)-t, and e(v)=exp(-v/2)E(exp(v)). Splitting dpsi=dt+dE is an identity of source measures. The continuum term is

    integral_(exp(v))^infinity t^(-1/2)f(log t-v) dt
      =exp(v/2) ell_-(f),
    ell_-(f)=integral_0^infinity exp(x/2)f(x) dx.

Integrating the remaining Stieltjes term by parts gives, for almost every v,

    R_psi f(v)
       =-e(v) f(0)
        +integral_0^infinity e(v+x)[f(x)/2-f'(x)] dx.

The boundary term is essential for the unrestricted-trace source core. If f vanishes near zero it disappears. Conventions at the isolated prime-power discontinuities do not change the L2-class identity.

Thus the exact source decomposition is

    P_infinity f(-v)=exp(v/2)ell_-(f)+R_psi f(v).

Using the classical prime number theorem E(t)=o(t) additionally shows R_psi f(v)=o(exp(v/2)) for each compact source. This asymptotic is NOT used to prove the weighted operator limit and is not an unweighted L2 bound.

## 4. The archimedean endpoint tail is fixed too

On the negative side, the constant/local subtraction terms in the Tate gamma operator multiply E_+f and vanish. Its remaining shift kernel gives

    Atilde_infty E_+f(-v)
      =integral_0^infinity
         exp(-(v+x)/2)/[1-exp(-2(v+x))] f(x) dx.

Split its kernel exactly as

    exp(-a/2)/(1-exp(-2a))
      =exp(-a/2)+exp(-5a/2)/(1-exp(-2a)).

The first term is exp(-v/2)ell_+(f), with ell_+(f)=integral exp(-x/2)f(x)dx. The remaining Gamma_tail f belongs to ordinary L2 in v for f in D_alpha, by the earlier gamma graph bound after subtracting the elementary L2 mode. For v>=1 it decays at least as exp(-5v/2) times a bounded source functional.

Combining the two source calculations,

    T_infinity f(-v)
      =exp(v/2)ell_-(f)+exp(-v/2)ell_+(f)
       +R_psi f(v)+Gamma_tail f(v).

The first two terms are precisely the negative-side continuation of the already prescribed endpoint swap response.

## 5. A specified relative operator, not a fitted cancellation

Define the source endpoint response on the full real line by

    E_end f(u)=exp(u/2)ell_+(f)+exp(-u/2)ell_-(f).

It is bounded H_alpha^+ -> K_alpha because alpha>1/2. Its unweighted pairing with a positive-half-line source reproduces the endpoint swap:

    <E_+f,E_end g>
      =conjugate(ell_-(f))ell_+(g)
       +conjugate(ell_+(f))ell_-(g).

Put

    R_infinity=T_infinity-E_end : D_alpha -> K_alpha.

This is a continuous, source-prescribed relative operator. Finite-place maps with the SAME endpoint response subtracted converge to it in the stated operator topology. On negative coordinates its explicit residual is

    R_infinity f(-v)=R_psi f(v)+Gamma_tail f(v).

The source has not been reconstructed from a desired scalar cancellation: P_infinity is defined by Mangoldt translations, E_end by the original endpoint functionals, and their match is proved by the two independent source kernel decompositions.

## 6. Recover the convergent arithmetic form

Unweighted pairing between H_alpha^+ and the positive restriction of K_alpha is continuous. The finite-place compression theorem and operator convergence therefore yield

    q_ar,infinity(f,g)=-<E_+f,R_infinity g>

on D_alpha, with the pairing interpreted in this dual rigging. This is exactly the already constructed half-line endpoint--gamma--prime form. Hermitian symmetry follows from those finite forms and continuity, not from declaring R_infinity self-adjoint on K_alpha.

Thus the all-prime form now has an accompanying source-to-weighted-dual OPERATOR limit. It is a different, explicitly specified statement from a full-line self-adjoint operator limit in ordinary L2.

## 7. The remaining unweighted residual gate is localized

On the compact smooth source core, Gamma_tail f is in ordinary L2. Therefore negative-side unweighted L2 membership after endpoint subtraction is equivalent to

    -e(v)f(0)+integral e(v+x)[f(x)/2-f'(x)]dx in L2(R_+,dv).

This is a concrete transform of the prime-counting error, with its boundary trace retained. The prime number theorem alone supplies only an o(exp(v/2)) estimate and does not settle this criterion. No critical-line, positivity, or full-line graph-convergence claim is inferred.

The right-hand/full-line residual may require additional analysis as well. The weighted-dual theorem already controls it in K_alpha; the displayed criterion localizes only the negative leakage refinement.

## Subsequent Euler-domain obstruction

`endpoint-subtracted-tate-leakage-is-not-L2-on-any-nonzero-finite-euler-packet.md` settles the negative-side criterion on the prepared Euler family: its Laplace transform is a divided difference of xi'/xi, whose surviving critical-zero poles exclude ordinary L2 for every nonzero finite Euler packet. This does not change the weighted-dual limit proved here or classify arbitrary infinite superpositions.

## Verification

- Fresh `uv run --with sympy python research/grothendieck/checkers/check_all_prime_tate_leakage_obstruction.py` passes the supplied divergence fixtures.
- `uv run --with sympy python research/voevodsky/checkers/check_all_prime_leakage_subtraction.py` passes exact Mangoldt staircase integration by parts, the endpoint/gamma kernel decomposition, and translation-weight inequalities.

Finite increasing norm values are regression illustrations. Infinite divergence uses the supplied reciprocal-prime argument; weighted convergence and subtraction use the proofs above.
