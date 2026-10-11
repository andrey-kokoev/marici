# Identification of the operational Machin candidate with standard pi

## Claim and evidence level

Let C be the **existing** `MetricCompletionCandidate`, not a newly defined real backend. There is a canonical standard-real interpretation

    rho : C -> R,
    rho([x]) = lim_n i_Q(approximation x n),

where R and pi are the ordinary real numbers and usual pi of the imported standard spectral witness. Then

    rho(machinPi) = pi.

The interpretation and this equality are proved below in ordinary classical mathematics. They are **not an Agda theorem about an imported classical-real type**. The construction of machinPi, its rational-sequence convergence, and its operational endpoints are independently safe Agda theorems. This is a mixed-level certificate: kernel-checked operational construction/endpoints plus an explicit written identification with the standard-real reference. It does not claim that the interpretation is kernel-formalized, nor that the phase derivative or full unitary-half-turn certificate is complete.

This supplies an explicit identification at the reference witness's standard-real mathematical level. It must not be presented as a fully kernel-verified correspondence to classical reals. The existing net is not automatically promoted: accepting this mixed verification level, or instead formalizing the interpretation in the kernel, remains an explicit boundary. Consumers requiring kernel verification must retain the interpretation-formalization obligation.

## 1. The actual quotient has a canonical real interpretation

`RegularCauchyStructure.agda` gives rational samples x_n with both directed inequalities expressing

    |i_Q(x_m)-i_Q(x_n)| <= 2^-m + 2^-n.

Thus the sample sequence is Cauchy in R and has a unique real limit by completeness. No pi, arctangent, or choice of sample schedule enters this definition of rho.

`CauchyMetricEquivalence.agda` identifies x and y precisely when, for every k, there is a threshold after which

    x_n <= y_n + 2^-k and y_n <= x_n + 2^-k.

If x is equivalent to y, taking limits gives |lim x-lim y|<=2^-k for every k. The difference is zero. Hence rho is independent of representative and descends to the actual quotient.

Conversely, if their real limits agree, for each k choose a common threshold after which each sequence is within 2^-(k+2) of that limit. Their difference is then less than 2^-(k+1), hence at most 2^-k. This supplies the eventual comparison required by the quotient relation. Thus the interpretation is injective at the standard-real semantic level. Only the forward implication is needed below.

For the constant representative, rho(embedMetricQ(q))=i_Q(q). Therefore this interpretation fixes the declared rational embedding; it is not an arbitrary rescaling or a pi-dependent identification.

Propositional truncations in the definitions assert existence. Eliminating their witnesses into the ordinary real inequalities above is legitimate because those inequalities and limits are propositions. No representative is selected as additional data in defining a class's unique real value.

## 2. The checked convergence interface is sound for this interpretation

`TickCompletionMetric.CompletionWithin(a,b,k)` supplies representatives of a and b eventually within 2^-k. Passing their two inequalities to real limits gives

    |rho(a)-rho(b)| <= 2^-k.

This proof uses the representatives in the existential ball and then representative independence. It does not incorrectly descend a fixed-radius predicate on arbitrary representatives.

`TickCompletionLimits.Converges(u,a)` states that for each k, all sufficiently late u_n are in that ball about a. Consequently, for every real epsilon>0 choose k with 2^-k<epsilon and the supplied threshold. Then |rho(u_n)-rho(a)|<epsilon. Thus rho takes every instance of the **actual checked convergence interface** to ordinary real convergence.

In particular, if embedded rational r_n converges to a in that interface, then i_Q(r_n) converges in R to rho(a). This theorem supplies the interpretation missing from a bare conditional uniqueness statement.

## 3. Identify the concrete rational approximants

The existing recurrence is

    a(q,0)=q,
    a(q,n+1)=-a(q,n)*q^2*(2n+1)/(2n+3),
    A_n(q)=sum_(j=0)^n a(q,j).

Induction, cancelling the positive denominator 2n+1, gives for every n

    a(q,n)=(-1)^n*q^(2n+1)/(2n+1).

This is a symbolic induction, not a conclusion inferred from finitely many numerical fixtures.

`TickMachinReferenceSeries.machinPartialSum` uses one common cutoff:

    M_n=16*A_n(1/5)-4*A_n(1/239).

Its repeated-addition scaling is exactly multiplication by these integers. `machin-series-converges` proves in safe Agda that embedMetricQ(M_n) converges to the original, independently scheduled machinPi. `machin-tail-bound` additionally proves |M_m-M_n|<=20*2^-n for all m>=n.

By section 2, M_n therefore converges in R to rho(machinPi). The argument does not pretend the candidate's scheduled representative is literally M_n at every index.

## 4. The ordinary real limit is a specific arctangent combination

For 0<=t<=q<=1, the exact finite geometric identity is

    1/(1+t^2) = sum_(j=0)^n (-1)^j*t^(2j)
                  + (-1)^(n+1)*t^(2n+2)/(1+t^2).

Integrating this finite identity from 0 to q yields

    arctan(q)=A_n(q)+R_n(q),
    |R_n(q)| <= q^(2n+3)/(2n+3).

Here arctan(q) is the ordinary inverse tangent with arctan(0)=0 and derivative 1/(1+q^2). The equality follows from the fundamental theorem of calculus, not an assumed operational inverse-trigonometric law. The bound follows from 0<1/(1+t^2)<=1. For q=1/5 and q=1/239 it tends to zero geometrically.

Hence uniqueness of ordinary real limits gives

    rho(machinPi)=16*arctan(1/5)-4*arctan(1/239).

Equivalently the common-cutoff reference sequence has the explicit standard-real error bound

    |M_n - [16*arctan(1/5)-4*arctan(1/239)]|
      <= [16*(1/5)^(2n+3)+4*(1/239)^(2n+3)]/(2n+3).

No interchange of an infinite sum with integration is needed: all integrations above are finite identities with an explicit vanishing remainder.

## 5. Fix the branch, not just a half-turn modulo full turns

Put A=arctan(1/5), B=arctan(1/239), theta=4A-B. Strict integral bounds imply

    1/5-(1/5)^3/3 < A < 1/5,
    0 < B < 1/239.

For the lower bound, 1/(1+t^2)>1-t^2 for t>0. For the upper bounds, 1/(1+t^2)<1 for t>0. Thus

    L=4*(1/5-(1/5)^3/3)-1/239 < theta < 4/5,
    L>0.

Independently, arctan(1)=pi/4 for the usual standard-real pi, and

    arctan(1)=integral_0^1 1/(1+t^2) dt > 1/2.

Therefore pi/2>1, and 0<theta<4/5<1<pi/2.

The classical double-angle identity gives

    exp(2i*arctan(q)) = C(q),
    C(q)=((1-q^2)+2iq)/(1+q^2).

The rational identity is exact:

    C(1/5)=(12+5i)/13,
    C(1/5)^2=(119+120i)/169,
    C(1/5)^4=(-239+28560i)/28561,
    C(1/239)=(28560+239i)/28561,
    C(1/5)^4=i*C(1/239).

It is now also independently certified by `TickMachinRationalGate.rational-machin-gate` using the operational rational embedding. In ordinary complex numbers it implies exp(2i*theta)=i. Since 2theta is in (0,pi), the unique such argument is pi/2. Hence theta=pi/4, so 16A-4B=pi.

Combining sections 3–5 proves **rho(machinPi)=pi**, not merely that its image is an unspecified odd half-turn.

## 6. Combine with the operational endpoint certificate

`TickMachinEndpoints.agda` supplies, without hypotheses:

- `completionCosine (-completion machinPi) = -completion oneCompletion`;
- `completionSine (-completion machinPi) = zeroCompletion`;
- `phase machinPi oneCompletion = complex (-completion oneCompletion) zeroCompletion`.

These are kernel theorems about the actual implementation. Sections 1–5 identify the same chosen scale with the usual pi used in `uniform-local-core-proof.md` and `spectral-whole-return-proof.md`, whose reference theorem is itself standard-real written mathematics.

We do not need to assume an interpretation theorem for completionCosine or completionSine to obtain these endpoints: they have already been proved internally. Nor does this identification supply `PhaseDerivativeLaw`, metric unit-circle flow, or the operational whole-return assembly.

## Verification contract

`checkers/check_standard_pi_identification.py` reruns the fresh safe endpoint and reference-series closures, checks the finite rational branch/rotation identities and recurrence fixtures, validates the pinned imported standard witness, and binds this written proof plus the actual metric definitions. The receipt explicitly distinguishes written analytic identification from kernel-checked endpoints and convergence. Exact finite checks support the argument; they do not replace completeness of R, the finite geometric remainder proof, or classical inverse-tangent theory.
