# Theta-tail dominance controls actual-letter factorization lifts

## Result

The actual-letter factorization comparison is positive for the prescribed theta forcing and actual prime-event generators. Terminal-anchored normal forms only move retained letters later. Uniform tail dominance then bounds their Gamma-weighted coefficient cost exponentially in event length, independently of endpoint location.

In particular the inherited and native two-factor completions agree on their compatible all-radius intersections. The same construction supplies a depth-uniform exponential path-tuple lift for all ideal powers.

This uses the actual theta forcing and the minimum prime step log(2). It is not a theorem for arbitrary positive letter weights, arbitrary forcings, or newly introduced arbitrarily short event generators.

## 1. Actual weights and a uniform tail constant

Keep gamma_e=sqrt(w_seam)||1_(E_e)Phi||_beta and Gamma(w)=product gamma_e over retained events. Set

`h_beta(x)=exp(beta x)(1+x)Phi(x)`, `a_0=log(2)`,

`T(a)=integral_a^infinity h_beta(x)^2 dx`.

The declared theta atoms are positive on this half-line. For one atom put q=pi n^2 exp(2x). Direct differentiation gives

`partial_x log Phi_n=9/2+6/(2q-3)-2q <=5-2q`, since q>=4pi>12.

Termwise differentiation is justified by the locally uniform theta series and its derivative majorants. Positivity makes the logarithmic derivative of the sum a weighted average. Thus

`partial_x log h_beta <= beta+6-2pi exp(2x)`.

Choose

`X_beta=max(a_0, (1/2)log((beta+7)/(2pi)))`.

For x>=X_beta, h_beta'<=-h_beta. Therefore

`T(a+log(2)) <= T(a)/4`, for a>=X_beta.

Every actual elementary event has window [a,b] with b-a=log p>=log(2). On that region its norm consequently satisfies

`sqrt(T(a)) <= (2/sqrt(3)) sqrt(T(a)-T(b))`.

On the remaining compact interval a in [a_0,X_beta], the ratio

`T(a)/[T(a)-T(a+log(2))]`

is finite and continuous with strictly positive denominator. Hence there is a fixed C_tail>=1 such that for EVERY event e beginning at a,

`sqrt(w_seam T(a)) <= C_tail gamma_e`.

This constant depends on the fixed beta and forcing, not on the packet, endpoint background, event prime or event length. If beta<=8pi-7, the derivative estimate already applies from a_0, and C_tail=2/sqrt(3) suffices. In particular it covers the declared beta=3 fixtures.

Any event window lying wholly after a has norm at most sqrt(w_seam T(a)). Thus a retained event moved later costs at most C_tail times the original retained event norm.

## 2. Why the terminal normal form only moves letters later

Use the terminal-anchored normal basis and sorted path section sigma from

`../grothendieck/a-terminal-normal-form-retraction-gives-an-exponential-two-factor-lift.md`.

A source path with q retained events expands into at most 2^q terminal-potential tensors. A surviving strict-chain coordinate chooses one endpoint of EACH original retained event, in their original order. Write these selected vertices v_0<...<v_(q-1), followed by the terminal vertex v_q.

Its source lift differentiates the sorted paths on the blocks [v_i,v_(i+1)], preceded by a forgotten path. Every new retained edge in block i starts at or after v_i. The latter is an endpoint of the corresponding original retained event and therefore is no earlier than that original event's start.

Section 1 consequently bounds each replacement letter by C_tail times its corresponding old letter. For differentiated block lengths l_i, the lift has at most product l_i terms, and product l_i<=2^(n-q). Retained degree is unchanged. Therefore the terminal retraction R=sigma rho satisfies

`||R(w)||_Gamma <= 2^n C_tail^q Gamma(w) <= kappa^n Gamma(w)`,

where `kappa=2 C_tail>=2` and n is event length. Here ||.||_Gamma is the actual weighted marked-path coefficient l1 norm.

This is the missing within-corner estimate. Multiplying the old unweighted inequality by one arbitrary corner scalar would not prove it, because Gamma varies between paths. Terminal anchoring and the actual tail bound are essential.

## 3. The weighted two-factor lift

For w=e_1...e_n use the same source-defined telescoping map

`H(w)=sum_i [R(e_1...e_(i-1))e_i-R(e_1...e_i)] tensor suffix_i`.

Every bracket is in I, multiplication gives w-R(w), and H restricted to I is right S-linear. Hence H(I^2) lies in the actual two-factor presentation I tensor_D I and multiplies to the input.

Gamma is multiplicative under typed concatenation. The ith summand has weighted tuple norm at most

`[kappa^(i-1)+kappa^i] Gamma(w)`.

Consequently

`||H(z)||_(Gamma,tuple)
 <= D (kappa^n-1) ||z||_Gamma`,

`D=(kappa+1)/(kappa-1)<=3`.

If mu_(r,Gamma) is the quotient norm induced by the Gamma-weighted marked-path-tuple presentation, then

`mu_(1,Gamma)(z)=||z||_Gamma`,

`mu_(2,Gamma)(z)<=D kappa^n mu_(1,Gamma)(z)`.

The tensor norm here is the specified norm on expanded marked-path tuples. It is not replaced by a projective norm on independently completed ideal factors.

## 4. Restore factorial, path and graph weights

For definiteness define the native r-factor corner norm by

`nu_(r,s,R,Gamma)=b_s(r)(1+n)^r n! R^n mu_(r,Gamma)`,

where b_s(r)=(2 lambda s)^r r!. Give I^2 its inherited r=1 norm on the other side. The factorial and exponential factors are scalar on a fixed corner and cancel in the comparison. Since 1+n<=2^n,

`||z||_(2,s,R,Gamma)
 <=4 lambda s D ||z||_(1,s,2 kappa R,Gamma)`.

Merging relation factors supplies the bounded comparison in the other direction. These identity maps extend by endpoint truncation to mutually inverse continuous maps on the all-radius intersections.

At fixed r, omitting the polynomial or graph factor only changes the all-radius topology by an already controlled radius enlargement. Thus this compares with the actual-letter Q_R source and its inherited ideal subspaces, not a newly fitted source norm.

No equality or inverse bound at one unchanged Banach radius is asserted.

## 5. A uniform all-power consequence

Recursively split off the first relation using H, applying the same construction to its remaining factor. The right-linearity argument gives

`H(I^r) subset I tensor_D I^(r-1)`.

It therefore constructs a linear lift L_r into the actual r-factor presentation, with multiplication L_r=id on I^r.

For a path expansion a term chooses r-1 ordered cuts. A segment of length l ending at a selected cut has weighted cost at most

`(kappa+1) kappa^(l-1) <= (kappa+1)^l`.

Those segments are disjoint, with total length at most n. There are at most binomial(n,r-1)<=2^n cut choices. Therefore, uniformly in r,

`||L_r(z)||_(Gamma,tuple) <= Lambda^n ||z||_Gamma`,

`Lambda=2(kappa+1)`.

Multiplication is contractive on weighted tuples because Gamma is exactly multiplicative. Hence

`||z||_Gamma <= mu_(r,Gamma)(z) <= Lambda^n ||z||_Gamma`.

The adjacent-depth comparison becomes

`||z||_(r+1,s,R,Gamma)
 <=2 lambda s ||z||_(r,2s,2 Lambda R,Gamma)`,

using (r+1)<=2^r and 1+n<=2^n. This supplies explicit simultaneous depth/radius control as well as the sharper first-step estimate.

## 6. Quotients, completion and cutoff compatibility

Taking quotient infima transfers the norm comparisons to I^r/I^m at every specified finite m>r. In a fixed corner the Gamma-weighted path norm is positive and finite dimensional. Every radius/factorial weight multiplies that same norm by a scalar. One norm-minimizing corner lift thus works simultaneously at all radii, giving intersection-surjectivity and strict exactness by the existing endpoint argument.

Accordingly the previously established INHERITED actual-letter filtered attachments may now be identified with the corresponding native Gamma-weighted presentation intersections. The identity comparisons preserve source operations and the same ideal I; no raw arithmetic-response kernel is substituted for it.

The tail argument also works uniformly for every positive theta truncation Phi_K, K>=1: the logarithmic derivative bound is inherited by each positive partial sum, its tail norm is bounded by that of Phi, and on the possible initial compact interval its density is bounded below by the first atom. Together with the already supplied relative theta comparison, this keeps the cutoff domains compatible without redefining the source kernel.

Chamber refinement does not violate the minimum-event hypothesis: it subdivides coefficient windows, not the prime-event generators. A theorem allowing arbitrarily short new event arrows would need another tail-dominance argument.

## 7. Boundaries

Closed for the prescribed source: Gamma-weighted relation-factor lifting, native/inherited all-radius topology comparison, and the corresponding finite filtered quotient transfer.

Not asserted: unchanged-radius equivalence, arbitrary-weight lifting, projectivity of completed ideals, perfect-module duality, or stable analytical inversion. The localized Clark attenuation and its observer-dual obstruction remain valid after this source-only comparison.

## Verification

`uv run --with sympy python research/nima/checkers/check_actual_letter_factorization_lift.py`

The checker verifies the theta logarithmic-derivative bound algebraically, the terminal retraction's later-start property on actual marked paths, exact weighted-letter inequalities for an exponential-density model, and two-factor reconstruction/membership on nonminimal products. The model is not claimed to be a theta evaluation. Uniformity for the actual theta weights is proved by sections 1--3.
