# Observer growth versus source priors controls uniform finite certification

## Result

For an admitted family of attachment observers, uniform finite-corner approximation on a weighted source-prior ball has an EXACT criterion: the family’s cornerwise source-functional norms, divided by the prior weights, must tend uniformly to zero outside finite packets.

A height-growth bound of order kappa and a source height moment of order eta give tail error O(H^(kappa-eta)) when eta>kappa. The threshold is necessary if corresponding lower growth occurs on escaping corners. Local finite-prime, source-coefficient and response-noise budgets can be added explicitly.

Uniform observation approximation does NOT by itself certify every member of an infinite family as nonzero. Nonvanishing needs a positive margin. For separately localized observers on escaping corners, even a common positive margin is generally impossible for one summable source.

## 1. Retain actual observers and their owning forward maps

Use the proper convex source height from `convex-source-heights-preserve-endpoint-budgets-through-attachment-operations.md`. Let c denote a full typed endpoint corner and V_c=(I^2)_c, or the declared homogeneous subspace when an observer requires one. At a fixed radius R put

`q_c(v)=n(c)! R^n ||v||_Gamma`.

For each corner let A_c:V_c->Y_c be its EXISTING attachment-to-labelled-response map, with its already admitted derivative, balancing and normalization. Let A_(N,c) be its finite-prime version. They are linear on source coefficients; changing the prime response does not change the window residual or the source ideal.

Take a specified family of ACTUAL descended observers indexed by j. Write ell_(j,c) for their bounded response tests on Y_c and

`L_(j,c)=ell_(j,c) A_c`.

Zero restrictions are allowed, including the fixed calibrated observer outside its selected finite packet. No arbitrary tensor-dual element is declared descended by this notation. All norms below are restricted to the true source subspace V_c.

Define the exact source envelope

`a(c)=sup_j ||L_(j,c)||_(q_c^*)`.

Assume this is finite on each corner. This is a real family hypothesis: individual boundedness does not imply uniform boundedness over j. For explicit response-error budgets we will also require

`t(c)=sup_j ||ell_(j,c)||_(Y_c^*)<infinity`.

A supplied forward bound F(c)>=||A_c|| gives a(c)<=t(c)F(c). This upper bound is usable but need not be sharp.

## 2. The sharp tail criterion

Fix prior weights W(c)>=1 and M>0. Consider genuine sources in J_(2,Gamma) satisfying

`Q_(R,W)(x):=sum_c W(c)q_c(x_c)<=M`.

Each finite-corner source belongs to this domain after rescaling; no completed-projectivity hypothesis is needed.

Let F_H be the finite convex packet of height <=H. Set

`tau_H=sup_(c outside F_H) a(c)/W(c)`.

For finite sources, weighted l1 duality gives the EXACT worst-case truncation error

`sup_(Q_(R,W)(x)<=M) sup_j
 |sum_(c outside F_H) L_(j,c)(x_c)| = M tau_H`.

For the upper bound, sum a(c)q_c(x_c). For the lower bound, choose a corner and an actual observer approaching the supremum, then choose a unit vector in V_c approaching its functional norm and scale it to prior mass M/W(c). This is a finite, genuine source in I^2. Thus the lower bound does not invent an observer or a new source arrow.

If tau_H->0, local finiteness of a(c)/W(c) implies its global supremum is finite. All observer sums then converge absolutely on the prior domain and define a bounded map into the space of bounded scalar families. The equality extends to this domain.

Therefore uniform finite-packet approximation on this prior ball holds IF AND ONLY IF tau_H->0. If it fails, the same cornerwise construction produces actual prior-bounded hostile sources and admitted observers whose omission error stays positive. If the ratios are unbounded, no uniform finite error bound exists on that ball.

For each fixed H the displayed equality may be read first on finite sources, allowing infinity; no convergence of an undefined infinite observer sum is presumed.

## 3. Height moments and the sharp conditional threshold

Take W(c)=h(c)^eta. If

`a(c)<=C h(c)^kappa`, with kappa>=0 and eta>kappa,

then

`sup_j |L_j(x)-L_j(P_H x)|
 <=C M (H+1)^(-(eta-kappa))`.

If, on an escaping sequence of admitted corners, a(c)>=c_0 h(c)^kappa with c_0>0, then eta=kappa leaves a nonvanishing worst-case tail, and eta<kappa leaves unbounded worst-case tails. This lower-growth assumption is essential; an upper growth estimate alone does not prove sharpness for a particular family.

No polynomial growth is asserted for all calibrated observers. Dividing by very small window amplitudes can make their response norms large. A finite witness’s normalization constants cannot be assumed uniform over translated packets. The actual envelope or a certified upper bound must be supplied. The general ratio criterion applies even when power moments are inappropriate.

For the one fixed observer of Voevodsky’s `../voevodsky/prior-controlled-filtered-towers-admit-finite-attachment-certificates.md`, a(c)=0 outside a finite set. Its tail is exactly zero once that set is included, without any global height moment. This theorem preserves that sharper fact.

## 4. Finite-prime and measurement budgets

On the retained finite packet suppose the owning forward comparisons supply

`||A_(N,c)||<=F_N(c)`,

`||A_c-A_(N,c)||<=e_N(c)`, with e_N(c)->0 for fixed c.

The constants are in the q_c-to-Y_c norms and must include the actual cut, feature, physical memory and normalization factors. No single-feature cutoff constant is silently applied to arbitrary tensor sums.

Let x be the exact prior-bounded source, and let a_tilde be a genuine source supported in F_H with

`sum_(c in F_H) q_c(a_tilde_c-x_c)<=epsilon_Q`.

Suppose measured labelled responses y_c satisfy

`sum_(c in F_H)||y_c-A_(N,c)a_tilde_c||<=epsilon_Y`.

Define the finite measured observation for every admitted j by

`Lhat_j=sum_(c in F_H) ell_(j,c)(y_c)`.

Put

`beta_(N,H)=max_(c in F_H) t(c)e_N(c)/W(c)`,

`G_(N,H)=max_(c in F_H) t(c)F_N(c)`,

`T_H=max_(c in F_H) t(c)`.

Then the uniform forward budget is

`sup_j |Lhat_j-L_j(x)|
 <= M tau_H + M beta_(N,H)
    + G_(N,H)epsilon_Q + T_H epsilon_Y`.

The four terms are omitted source corners, prime cutoff on the exact retained source, retained source perturbation at finite cutoff, and measurement error. Calibration or numerical functional-evaluation errors must be included separately unless already enclosed in the specified tests/data bounds.

For any positive target tolerance, tau_H->0 permits finite H; at that fixed H, local cutoff convergence permits finite N; then finite G_(N,H),T_H permit positive coefficient/measurement tolerances. This is an existence and forward-bound theorem, not a claim that one noise tolerance works uniformly as H increases. Large calibration norms may force extremely small tolerances.

## 5. Recover the retained packet from a finite tower level

Let N_H be the maximum event length in the finite convex packet. For 2(m+1)>N_H, its source corners stabilize in tower level m. Thus P_H x is determined by finite level-m data. If the tower's degree-one class is zero, its recovered packet lies in I^2.

The finite source candidate must satisfy the exact ideal and homogeneous constraints in section 1. Neither arbitrary quotient noise nor arbitrary measured response vectors are declared source chains. The coefficient error epsilon_Q is a source error; it cannot be inferred backwards from epsilon_Y using this theorem.

This uses the bounded-tower realization theorem and the structure-preserving convex cutoff. If the common-path domain is imposed as well, its independent source conditions remain in force.

## 6. What uniform nonzero certification additionally needs

Let E denote the total error in section 4. For any selected observer j, Re Lhat_j>E certifies Re L_j(x)>0. If a subfamily is known to satisfy Re L_j(x)>=d_*>0 uniformly and E<d_*/2, every observation in that subfamily retains a positive half-margin.

The margin is an additional hypothesis, not a consequence of the prior. For observers j_k each supported on a distinct escaping corner c_k, boundedness of a(c)/W(c) already implies, for a fixed summable x,

`|L_(j_k)(x)|<= [a(c_k)/W(c_k)] W(c_k)q_(c_k)(x_(c_k)) ->0`.

Thus such a family cannot have a common positive absolute margin. Under tau_H->0 this conclusion is automatic. Finite-packet approximation can uniformly approximate these small observations, but cannot thereby certify infinitely many separately supported nonzero values.

If positive individual margins d_j are specified, use the normalized family ell_(j,c)/d_j and repeat the ratio test. Its envelope is generally larger and may fail the criterion. In particular a finite packet gives zero for every observer supported wholly outside it; it cannot give a relative error below one when the omitted true observation has magnitude at least its claimed margin.

An infinite family sharing finite support, such as a uniformly controlled parameter family, does not face this escaping-support obstruction. Its norm and margin bounds still have to be proved by its owning comparison.

## 7. Disposition

The extension from one finite observer to controlled families is governed by a precise growth-versus-prior ratio, with a matching source-based obstruction. The theorem composes source omission, finite depth, finite primes and measured-response errors without identifying their norms or adding unadmitted observers.

It supplies uniform forward observation approximation and conditional sign certification. It supplies neither a source inverse nor automatic simultaneous nonvanishing across infinitely many escaping packets.

## Verification

`uv run python research/nima/checkers/check_observer_family_budgets.py`

The checker verifies exact weighted-l1 envelope identities and attaining one-corner witnesses on rational fixtures, height-exponent thresholds, and the finite forward error decomposition. The fixtures do not establish a norm-growth bound for an unspecified actual observer family; those bounds remain explicit hypotheses of the theorem.
