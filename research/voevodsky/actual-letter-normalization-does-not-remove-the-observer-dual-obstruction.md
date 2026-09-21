# Actual-letter normalization does not remove the observer-dual obstruction

## Result

The observer-dual nonsurjectivity persists on the actual-letter source topology, for the first attachment with INHERITED closed-ideal quotient norms. A normalized four-event family is bounded in every actual-letter source seminorm while its analytical joint images tend to zero. An explicit Q_1-continuous source functional has no continuous joint-target lift.

The corresponding model-level continuous observer square can be formed with these inherited norms. This does not compare them with independently completed Gamma-weighted factorization norms, nor establish completed perfect-module duality.

Inputs:
- `../nima/the-factorial-attachment-has-a-continuous-observer-dual-square.md`
- `../grothendieck/actual-letter-weights-characterize-marked-fox-summability.md`
- `relative-theta-tail-control-preserves-the-actual-letter-fox-domain.md`

## 1. Attenuation after forcing normalization

Let f be supported in [L,infinity), with L>=log(2). On the fixed spectral region eta<=Im z<=Y<beta, set a=beta-Y. The trace estimate improves to

    |h_(sigma,j)(f;z)| <= exp(-a L)||f||_beta/sqrt(2a).

Indeed, the Cauchy--Schwarz integral now starts at L. Integrating the half-line feature norm and applying the fixed normalized sewing matrix gives

    ||Lhat(f)||_feature <= C_feature exp(-a L)||f||_beta.

Thus small actual forcing norms are not the only source of output attenuation. Even after dividing by the forcing norm, the analytic feature map decays uniformly for translated support. This uses the positive source/control norms and makes no assertion about signed self-pairing signs.

## 2. Normalize a genuine product using actual letters

Translate four fixed event primes by a growing background product Q_N, retaining different endpoint corners. Let a_N be the singly retained first-diamond relation and c_N the forgotten second-diamond relation. Put v_N=a_N c_N. Its eight path coefficients have modulus one and every word contains one retained first-diamond letter.

Write gamma_(N,e)=sqrt(w_seam)||f_(N,e)||_beta for the four first-diamond edges. Then

    Q_1(v_N)=4! * 2 sum_e gamma_(N,e)=48 sum_e gamma_(N,e).

Define u_N=v_N/Q_1(v_N). All denominators are positive. Since every corner has event length four,

    Q_R(u_N)=R^4

for every source radius R. This is a bounded family in S_Gamma and in the inherited four-event product quotient. In that corner I^3=0, so no next-layer quotient can alter its norm.

Its balanced joint image is D(a_N) tensor_balanced D(c_N), with the same normalization. Each first-diamond event feature occurs twice in D(a_N), with memory versus seam multiplier ratio at most lambda. The final forgotten cycle contributes four unit terms. The raw target norm is therefore bounded by

    8 lambda C_feature exp(-a L_N) sum_e gamma_(N,e),

where L_N=log(2 Q_N). Including fixed depth-two and degree-one target weights gives

    ||j(u_N)||_(s,b)
       <= [b b_s(2) lambda C_feature/6] exp(-a L_N) -> 0.

This holds in every target seminorm. Actual-letter normalization does not repair analytical inverse instability.

## 3. A continuous source functional that cannot lift

On each chosen corner, define a conjugate-linear functional by summing the eight selected coefficients with their v_N signs and weights 4! Gamma(w). Sum these functionals over the disjoint endpoint corners. The result ell satisfies

    |ell(x)|<=Q_1(x),   ell(u_N)=1.

Every selected corner has length four, so its I^3 component is zero. Hence ell annihilates the closed third ideal power and descends to the INHERITED product quotient P_Gamma. It is a continuous source functional there.

If a continuous analytical target functional psi lifted ell, then

    1=ell(u_N)=psi(j(u_N)) ->0,

a contradiction. This excludes lifts even from the entire continuous target dual, and therefore also from the Green-representable observer graph domain.

Each u_N is a finite source vector and belongs to S_common intersect S_Gamma. The same ell is continuous on that intersection because Q_1 is one of its seminorms, so the no-lift contradiction applies there too. The family need not be bounded in the added common-path seminorms; that boundedness is not needed for the contradiction.

## 4. The inherited actual-letter model still has a dual square

To specify its topology, take closures of I,I^2,I^3 in S_Gamma and use the INHERITED closed-subspace quotient norms. Within a finite endpoint corner, Gamma gives a fixed positive weighted path norm, while n! R^n is a scalar multiplier. One choice of a minimizing corner lift therefore works for all R. The previous endpoint/intersection argument proves the strictly exact sequence in this topology.

The derivative D2 is continuous by the actual-letter full-jet estimate and kills I^3 before completion, hence its closure afterward. This gives the two-term attachment model K_Gamma and its bounded joint map at the specified scales. The continuous source actions on S_Gamma retain their known radius losses.

Using the SAME prescribed target observer graph O_T from Nima's note, transposition supplies

    F2^vee beta_T = pi^vee j^vee beta_T

as a continuous chain square on strong scalar duals. This follows from functorial transpose and the bounded-on-bounded-set estimate; it does not assert onto beta or onto joint observation. The witness above explicitly prevents the latter.

No Gamma-weighted Fox factorization estimate has been used. It remains unjustified to replace these inherited closed-ideal topologies by independently chosen relation-factor presentation norms without another comparison theorem. Likewise strict exactness of the strong-dual intersection sequence and perfect-module tensor-Hom equivalence remain outside the claim.

## 5. Relation to theta truncation

Uniform relative theta-tail control shows that all fixed K>=1 actual-letter domains agree with radius loss and that their full jets converge in the forcing-resolved topology. It does not bound below the analytic feature map on translated normalized letters. The present no-lift family is therefore compatible with, not contradicted by, uniform theta substitution.

## Verification

Fresh `uv run --with sympy python research/nima/checkers/check_factorial_attachment_dual_square.py` passes its nonreal sign, mate, chain, and connecting-square fixtures.

`uv run python research/voevodsky/checkers/check_actual_letter_dual_obstruction.py` checks exact normalization with unequal positive letter weights, the Q_1 functional, and the joint-term ratio 1/6. These weights are bookkeeping fixtures, not claimed theta evaluations. Actual analytical decay is supplied by the localized trace estimate above.
