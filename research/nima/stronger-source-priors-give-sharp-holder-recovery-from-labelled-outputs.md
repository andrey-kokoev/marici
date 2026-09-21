# Stronger source priors give sharp Hölder recovery from labelled outputs

## Result

The full five-label response has a quantitative conditional inverse on an explicit stronger prior class. For gamma>1/2 and delta>0, give the even port one extra weighted derivative and both ports extra spatial decay:

`M(u,r)=||u||_(H^2_(gamma+delta))+||r||_(H_(gamma+delta))`.

Then

`||(u,r)||_(D_gamma direct-sum H_gamma)
 <= C_(gamma,delta) M(u,r)^(1-alpha) ||O(u,r)||_response^alpha`,

where

`alpha=min(1/2,delta/(2 gamma+delta))`.

This exponent is optimal among uniform Hölder POWER estimates on this full port/prior class, even when every arithmetic response coordinate is retained. The proof of the upper bound needs only the two weak response copies; the arithmetic channels cannot increase the uniform power exponent. Improvements in constants or logarithmic moduli are not excluded.

This is conditional recovery, not a bounded inverse on the unrestricted source or an ordinary-L2 realization of Tate leakage.

## 1. Domains and the measured weak information

On the positive half-line define

`||f||_(H_a)^2=integral exp(2 a x)|f(x)|^2 dx`,

`||f||_(H^j_a)^2=sum_(k=0)^j ||f^(k)||_(H_a)^2`.

Derivatives are weak; no zero endpoint trace is imposed. D_gamma=H^1_gamma.

Retain the already supplied output

`O(u,r)=(B_rig u,-leak_rig u,J_end beta_end(u),r,u)`.

The two final coordinates carry H_(-gamma), not strong source, norms. With the declared sum norm on all output labels,

`e_0=||u||_(H_(-gamma))+||r||_(H_(-gamma))
 <= ||O(u,r)||_response`.

Also e_0<=M(u,r). The arithmetic operator and all its endpoint/leakage labels remain unchanged.

## 2. Exact weighted interpolation for the residual port

Put theta=delta/(2 gamma+delta). The weight identity

`gamma=theta(-gamma)+(1-theta)(gamma+delta)`

and Hölder's inequality give

`||r||_(H_gamma)
 <= ||r||_(H_(-gamma))^theta
    ||r||_(H_(gamma+delta))^(1-theta)`.

Since alpha<=theta and the weak norm is no larger than the prior norm, this remains true with theta replaced by alpha. No regularity of r beyond the stated weighted L2 prior is needed.

## 3. Weighted derivative interpolation for the even port

We prove

`||u||_(H^1_gamma)
 <= C_(gamma,delta) ||u||_(H_(-gamma))^alpha
    ||u||_(H^2_(gamma+delta))^(1-alpha)`.

Choose a smooth bounded-overlap partition into intervals of uniformly bounded length near j=0,1,2,..., with uniformly bounded first and second cutoff derivatives. For its localized pieces v_j set

`a_j=||v_j||_L2`, `b_j=||v_j||_H2`, `c_j=||v_j||_H1`.

Uniform local interpolation gives c_j<=C a_j^(1/2)b_j^(1/2). Since a_j<=b_j and alpha<=1/2,

`c_j<=C a_j^alpha b_j^(1-alpha)`.

For the interval touching zero, this uses the standard unrestricted-trace H2 extension. Explicitly, on the negative side one may use 3v(-x)-2v(-2x), which matches both value and first derivative at zero. Its L2 and H2 bounds are uniform. Fourier Cauchy--Schwarz on that extension gives the same interpolation inequality. No Dirichlet condition is introduced.

Set A_j=exp(-gamma j)a_j and B_j=exp((gamma+delta)j)b_j. Then

`exp(gamma j)c_j
 <= C exp([alpha(2 gamma+delta)-delta]j)
        A_j^alpha B_j^(1-alpha)
 <= C A_j^alpha B_j^(1-alpha)`.

The last inequality is exactly the spatial restriction alpha<=theta. Squaring, summing and applying sequence Hölder proves the desired estimate. Bounded overlap and bounded weight variation on each interval identify the localized weighted sums with the original weighted Sobolev norms, with constants depending only on gamma,delta and the fixed cutoff family.

## 4. The conditional inverse and noisy-data consequence

Combine sections 2 and 3, and apply Hölder to the two component bounds. This yields

`||u||_(D_gamma)+||r||_(H_gamma)
 <= C M(u,r)^(1-alpha) e_0^alpha
 <= C M(u,r)^(1-alpha) ||O(u,r)||_response^alpha`.

In particular, on a prior ball M(u,r)<=M, the inverse on the actual output range is uniformly Hölder in the strong port norm.

If two candidate ports have prior norm at most M and each fits the same measured response within epsilon, their difference has prior norm at most 2M and output norm at most 2epsilon. Hence

`||port_1-port_2||_strong <= 2 C M^(1-alpha) epsilon^alpha`.

This is a stability guarantee for admissible candidates, not a claim that every noisy response has a source preimage or an existence theorem for a reconstruction algorithm.

## 5. The derivative obstruction forces alpha<=1/2

Use the oscillating-source estimates from

`../voevodsky/the-reduced-rigged-arithmetic-response-is-compact-with-nonclosed-range.md`

and their full-output extension in

`the-full-labelled-response-is-injective-but-unstable-on-aggregated-euler-packets.md`.

Fix a nonzero real smooth bump chi compactly supported away from zero and put

`u_n=n^(-2) exp(i n x) chi(x)`, `r_n=0`.

Their H^2_(gamma+delta) norms are uniformly bounded, while

`||u_n||_(D_gamma) is comparable to 1/n`.

The fixed gamma response has norm O(log(2+n)/n^2), by the logarithmic multiplier estimate. Prime, endpoint and weak-copy responses have norm O(1/n^2). Thus the FULL labelled output obeys

`||O(u_n,0)||_response=O(log(2+n)/n^2)`.

Any uniform Hölder exponent a>1/2 on this prior ball would require 1/n to be bounded by a constant times (log(2+n)/n^2)^a, which is impossible. Retaining the arithmetic channels therefore does not remove the derivative exponent ceiling.

## 6. The spatial obstruction forces alpha<=theta

For the residual coordinate alone take

`u_R=0`, `r_R(x)=exp(-(gamma+delta)R) chi(x-R)`.

Its prior norm is independent of R. Exactly,

`||r_R||_(H_gamma)=exp(-delta R)||chi||_(H_gamma)`,

`||O(0,r_R)||_response
 =||r_R||_(H_(-gamma))
 =exp(-(2 gamma+delta)R)||chi||_(H_(-gamma))`.

All arithmetic and endpoint coordinates are zero, because u_R=0. Hence a uniform Hölder exponent a would require a<=delta/(2 gamma+delta).

Together with section 5, this proves optimality of the displayed alpha for the FULL port/prior class. It is not an optimality theorem on a smaller residual-zero or specially constrained forcing family.

## 7. Relation to aggregated Euler packets and earlier no-go results

The hostile sources above are smooth compactly supported functions. Each has a norm-summable vertical Euler presentation: on a line with alpha_0=sigma-1/2>gamma, Fourier-expand exp(alpha_0 x) times its smooth compactly supported extension. The resulting density is Schwartz and has the required first absolute moment. The prior bounds in this theorem are imposed on the AGGREGATED source, not on every individual exponential in such a presentation.

For the translated residual example one may even choose alpha_0=gamma+delta: its transformed smooth bump is just translated, so the Fourier-density modulus and first absolute moment stay fixed. Individual exponentials are in the original D_gamma, while membership in the stronger aggregate prior follows from the explicit compact-support calculation. No interchange in an unjustified stronger Bochner norm is asserted.

Without the extra decay delta, the translated residual family gives no positive spatial Hölder exponent. Without the additional derivative on u, the earlier normalized oscillating family rules out strong-port recovery. Thus both parts of the prior address actual, distinct obstructions.

Nothing here bounds the unweighted full-line leakage or changes the weighted-dual response topology. Nor does it recover an underlying forcing from its spectral amplitudes. The theorem concerns the declared arithmetic/residual port domain and its existing full labelled output.

## 8. The new reduced-response kernel makes the weak copies essential

The subsequent `../voevodsky/infinite-euler-cancellation-gives-a-full-line-kernel-with-zero-endpoints.md` constructs nonzero sources annihilated by BOTH the full rigged Tate response and the endpoint map. This is a kernel of the reduced output, not of O.

These examples can satisfy the prior used here. Choose their packet line sigma>gamma+delta+1/2 and retain their decay parameter M_0>=8. Their density is O(|t|^(2-M_0)), so its second absolute moment is finite. Since the norm of an Euler state in H^2_(gamma+delta) grows at most quadratically in |t| on that line, its Bochner integral belongs to H^2_(gamma+delta). The nonzero source certificate and both zero-output identities are unchanged. Compatibility of the rigged responses on domain intersections gives the same zero response at gamma.

Rescaling such a source places it in any nontrivial prior ball. Therefore no positive-modulus recovery estimate for the REDUCED map can hold on this prior class without addressing its kernel. In contrast, O(f,0) still contains the nonzero weak even copy f, and the theorem above applies exactly as stated. Regularity assumptions do not manufacture information absent from the reduced data.

## Verification

`uv run --with sympy python research/nima/checkers/check_conditional_labelled_recovery.py`

The checker verifies the exact weight interpolation, the two exponent restrictions, the unrestricted-trace extension matching, and the oscillation/translation sharpness formulas. Functional interpolation and the arithmetic response bounds are the proofs above and the cited operator theorem, not finite numerical recovery experiments.
