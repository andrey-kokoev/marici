# Factorial path scales sum the full Fox-jet family

## Result and domain

An explicit factorial strengthening of the common-path source makes its entire ordered Fox-jet family summable in the existing depth/feature receiver. Multiplication is continuous with radius loss two. On the forcing-resolved realization, the separately labelled current maps restrict continuously to this summed image.

This is a sufficient stronger domain, not an identification with the source recovered in `../voevodsky/the-bounded-filtered-limit-recovers-the-source-and-its-faithful-fox-jets.md`. No inverse analytical estimate or minimality of the strengthening is asserted.

## 1. Factorial source scale

Choose A>=1 bounding the prescribed forcing-resolved and analytical letters. Retain the actual marked-path coefficients and typed endpoints. Set

`q_R(x)=sum_c n(c)! (R A)^(n(c)) ||x_c||_path`, for integer R>=1.

Let S_fact be the intersection of these weighted l1 spaces, and let I_fact be its closed subspace of terminal-record relations. Coordinate projections and finite-support truncation prove completeness and density in the usual compatible intersection topology.

This domain embeds continuously in every fixed-polynomial, all-radius common-path domain: (1+n)^p<=2^(p n) is absorbed by enlarging R. The reverse inclusion is not assumed. These are positive control norms, not changes to the prescribed signed pairings.

## 2. Sum the jet estimates before taking a limit

Let F_(s,b) be the existing forcing-resolved l1 receiver, summed over jet order k, with graph weight b_s(k)=(2 lambda s)^k k! and feature weight b^d. Include the zero-seam terminal-record sector. No independently prepared root state is duplicated.

For a path w of length n,

`||D_k(w)||_(F_(s,b)) <= (2 lambda s)^k k! binomial(n,k) (b A)^n`.

Put t=2 lambda s>=2. The exact sum is

`sum_(k=0)^n t^k k! binomial(n,k)
 = n! t^n sum_(j=0)^n t^(-j)/j!
 <= exp(1/t) n! t^n
 <= 2 n! t^n`.

Consequently the full jet map satisfies

`||D(x)||_(F_(s,b)) <= 2 q_(2 lambda s b)(x)`.

Round a noninteger source radius upward. Finite source approximations converge in this norm, so this constructs an actual l1-summed jet family, not only a product-topology family. Bounded coordinate projections identify its kth component with the previously defined D_k. The normalized Clark transfer adds only its established fixed feature-radius loss.

The full map is faithful: if every jet is zero, stabilized finite endpoint corners and the finite-jet separation theorem give x=0. It need not have a continuous inverse on its image.

On I_fact, D_0=0. On the whole source, the zero-seam sector is necessary for the product identity. D_k on an arbitrary element is a record, not necessarily a cycle. Cycle and isolated source-equivariance assertions remain restricted to the appropriate ideal power/layer.

## 3. Multiplication and the convolution identity

For composable lengths n,m,

`(n+m)! <= 2^(n+m) n! m!`.

The path convolution inequality therefore gives

`q_R(xy) <= q_(2R)(x) q_(2R)(y)`.

Thus S_fact is a complete locally convex algebra and I_fact is a closed ideal. No infinite sum of vertex identities is adjoined.

On finite paths the jet identity is

`D_k(xy)=sum_(i+j=k) D_i(x) tensor_balanced D_j(y)`.

Use ordinary jet-order convolution on the unshifted record sectors. The target tensor estimate loses only s->2s; absolute l1 summability justifies the full double sum. The source product estimate and the full-jet bound give common controlling source radii, so the identity extends by density to S_fact. Cochain suspension comparisons use the previously prescribed phases; jet convolution introduces no new signs.

## 4. Separately labelled currents

The input theorem is `../voevodsky/bulk-and-forcing-currents-converge-separately-on-the-forcing-resolved-completion.md`, together with its existing all-depth graph controls. At a fixed compact spectral interior choose s and a feature radius b large enough for its labelled current bounds. The full jet belongs to that forcing-resolved scale by section 2.

Pullback of each declared continuous sesquilinear current map is therefore continuous on S_fact, with a bound by a constant times

`q_(2 lambda s b)(x) q_(2 lambda s b)(y)`.

Keep the prescribed shape/type matching rules. This does not introduce pairings between incompatible jet sectors, an arbitrary cross-degree Green form, or an unweighted sum of unrelated observables. The statement is restriction of the already bounded labelled current maps to the summed forcing-resolved image.

Their separate bulk, forcing, and vacuum-incidence limits and the admitted relative sewing identities follow by source approximation and continuity. No convergence claim is inferred merely from cancellation of bulk plus forcing, and no spectral-boundary evaluation is added.

## 5. A quantitative jet-order tail

For N>=0, only paths of length n>N contribute to orders k>N. If R>=2 lambda s b and L>1, the preceding full-sum estimate gives

`||sum_(k>N) D_k(x)||_(F_(s,b)) <= 2 L^(-(N+1)) q_(L R)(x)`.

Indeed, on those path lengths R^n<=(L R)^n L^(-(N+1)). The l1 triangle inequality handles collisions. This proves uniform jet-order truncation on bounded subsets of a stronger source seminorm, in addition to existence of the full sum.

For any bounded sesquilinear labelled current map, replacing one or both inputs by their jet truncations now gives convergence by the usual two-term difference estimate. This statement concerns the declared current maps and their labels, not an independently chosen arithmetic Green operator.

## 6. Scope

Closed: a sufficient factorial source domain, continuous faithful summed Fox jets, multiplicative convolution with explicit radius loss, current pullback, and quantitative order tails.

Not claimed: equality with the earlier common-path source, necessity or optimality of factorial weights, stable inversion, completed projectivity, or a completed tensor-Hom equivalence. The bounded inverse-limit theorem remains a separate characterization in its original source seminorms.

## Verification

`uv run python research/nima/checkers/check_factorial_fox_jet_bounds.py`

The checker verifies exact jet-sum identities, rational uniform majorants, factorial product bounds, and the radius-tail inequality. Completion and current pullback follow from the estimates above and the cited forcing-resolved theorem, not from finite numerical samples.
