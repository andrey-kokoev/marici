# Universal-form Fox lifts control the completed ideal-power topologies

## Result

The reverse norm comparison exists. At an endpoint interval of event length n, with the previously specified presentation quotient norms,

`nu_2(z) <= 32^n nu_1(z)`, for z in I^2.

More generally, arbitrary ideal powers have linear factorization lifts with unweighted coefficient cost at most 32^n, uniformly in their depth. Consequently

`nu_(r+1)(z) <= 64^n nu_r(z)`, for z in I^(r+1).

These deliberately nonoptimal constants are independent of arithmetic endpoint location. Radius enlargement absorbs them. The inherited kernel and independently completed next ideal power therefore agree topologically on the compatible all-radius intersections. They need not agree at a fixed Banach stage.

This closes the norm-comparison gate in `completed-attachments-are-strict-only-with-the-kernel-topology-specified.md`. It also compares Voevodsky's common-path first filtered extension and its nonzero balanced attachment with the earlier presentation scales. It does not prove projectivity over a completed algebra or a completed tensor-Hom equivalence.

## 1. An explicit normal form for the terminal quotient

Fix a finite monotone endpoint interval [x,y]. Let D be its vertex-idempotent algebra and A its incidence algebra: there is one basis element a_(u,v) for each u<=v, and composable basis elements multiply by concatenating endpoints.

The terminal quotient B of the two-mark path source is the relative universal differential envelope Omega_D(A). A forgotten elementary arrow maps to a_(u,v); a retained one maps to d a_(u,v).

Here is a direct verification, including injectivity. Realize degree k universal forms inside A tensor_D ... tensor_D A, with k+1 factors. A tensor basis element is a weak vertex chain with k internal vertices. Send it to the ordered tensor of those internal vertex symbols, retaining its outer endpoints. Distinct weak chains have distinct tensors. Under this embedding, d a=1 tensor a-a tensor 1 maps to u_start-u_end, the negative of the prescribed retained event vector. Degree k therefore differs from the terminal recorder by the single sign (-1)^k, which changes no kernel.

Anchoring u_x=0 does not introduce a kernel: products of differences lie in the tensor algebra on the span of u_v-u_x, and projection killing u_x is an isomorphism on that difference span. The chamber realization of those vertex differences is injective. Thus this argument uses the actual formal event windows, not sampled analytical features.

The normalized relative bar description gives a basis of degree k forms indexed by

`x <= v_0 < v_1 < ... < v_k=y`,

represented by

`a_(x,v_0) d a_(v_0,v_1) ... d a_(v_(k-1),y)`.

In the unnormalized tensor expansion, quotient out vertex identities in the last k factors. Exactly the displayed normalized tensor survives from that form. This is the usual explicit inverse between normalized tensors and universal forms.

The marked path generators generate all these forms: an interval incidence element is a forgotten path, and its differential is the sum of its single-retained versions. This proves both surjectivity onto Omega_D(A) and equality of its kernel with the terminal-record ideal I.

## 2. A section with exponential coefficient bounds

Choose a fixed order of event primes and use the sorted forgotten path for every interval incidence element. Lift a differential d a_(u,v) by differentiating that chosen path: the sum over its single-retained versions. Let sigma:B->S be the resulting endpoint-preserving linear section in the normalized basis.

For a source path of length p with k retained events, expansion of its universal form has at most 2^k terms. Normalization discards identity-factor terms and cannot increase coefficient l1 norm. Thus

`||rho(w)||_bar <= 2^p`.

For a normalized basis form b of event length p, its source lift has coefficient mass the product of the lengths of its differentiated blocks. Since each positive block length l is at most 2^l,

`||sigma(b)||_path <= 2^p`.

Both bounds extend linearly. Moreover rho sigma=id, and sigma sends vertex identities to themselves. The construction is compatible with convex packet inclusions when the event order is fixed globally. It is linear but is not asserted to be a multiplicative section.

## 3. Fox differentiation splits off a relation factor

Let V be the typed space of marked elementary arrows. Define the left-recorded path derivative

`nabla:S -> B tensor_D V tensor_D S`

by

`nabla(w)=sum_i rho(prefix_i) tensor e_i tensor suffix_i`.

Its product rule is

`nabla(uv)=nabla(u)v+rho(u)nabla(v)`.

In particular nabla restricted to I is right S-linear. For a normalized basis element b ending at the source of an arrow e, put

`t(b,e)=sigma(b)e-sigma(b rho(e))`.

This belongs to I. Extending t by right multiplication gives a map from the displayed free right-module presentation to I. Telescoping along a path proves

`t nabla(z)=z-sigma rho(z)`.

It is therefore the identity on I.

If z belongs to I^r, then nabla(z) belongs to

`B tensor_D V tensor_D I^(r-1)`.

Indeed write z as a finite sum of products u v with u in I and v in I^(r-1). The product rule gives nabla(uv)=nabla(u)v. Every coefficient in the normalized B/arrow basis is consequently in I^(r-1). This membership statement does not depend on choosing that factorization to compute nabla(z).

For r=2, writing these coefficients as z_(b,e) gives the explicit linear lift

`L_2(z)=sum_(b,e) t(b,e) tensor z_(b,e)` in the two-factor relation presentation.

Multiplication sends L_2(z) to z. Both factors are genuine relations. There is no inversion of the analytical receiver and no choice of a minimal-norm factorization.

## 4. Quantitative bound for the first lift

Suppose b has event length p. The bounds in section 2 give

`||sigma(b)e||_path <= 2^p`,

`||b rho(e)||_bar = ||rho(sigma(b)e)||_bar <= 2^(2p+1)`,

`||sigma(b rho(e))||_path <= 2^(3p+2)`.

Thus

`||t(b,e)||_path <= 8^(p+1)`.

On a path of length n, the sum of the coefficient norms in nabla is at most

`sum_(p=0)^(n-1) 2^p = 2^n-1`.

Every relation t occurring there has length at most n. Expanding the lift in actual marked-path tuples therefore gives

`||L_2(z)||_tuple <= 16^n ||z||_path`.

For the earlier weight w_r(n)=(1+n)^r a^n, the one-factor norm is exactly

`nu_1(z)=w_1(n)||z||_path`.

The lift proves

`nu_2(z) <= (1+n)16^n nu_1(z) <= 32^n nu_1(z)`.

The same calculation holds with a replaced by b a. It is a uniform exponential lifting estimate, not just equivalence of two norms in each finite dimension.

## 5. All powers without iterating an exponential loss r times

Define L_1=id on I. Recursively apply L_(r-1) to the suffix coefficients of nabla(z), and t to its first B/arrow factors. The membership statement in section 3 guarantees that this gives a linear lift

`L_r:I^r -> P_r`, with `multiplication L_r=id`.

For a source path, a term in this recursion chooses r-1 ordered cut positions. A segment before one such cut contains p events, followed by the selected arrow. Its bar expansion and t expansion together cost at most

`2^p 8^(p+1) <= 16^(p+1)`.

The selected segments are disjoint. Their total length is at most n, so their combined cost is at most 16^n, NOT 16^(r n). There are at most binomial(n,r-1)<=2^n choices of cut positions. The remaining suffix is unchanged in the base case. Hence

`||L_r(z)||_tuple <= 32^n ||z||_path`

uniformly in r. The formula can be expanded linearly on all paths; membership in the relation presentation is asserted on I^r.

Multiplication of path tuples is l1-contractive. Consequently

`w_r(n)||z||_path <= nu_r(z) <= 32^n w_r(n)||z||_path`.

Applying this at depth r+1, and using the lower bound at depth r, yields

`nu_(r+1)(z) <= (1+n)32^n nu_r(z) <= 64^n nu_r(z)`.

The reverse direction is the already established merging bound

`nu_r(z) <= nu_(r+1)(z)/(1+n)`.

There is no contradiction with the exact 1/(1+n) ratio on the forgotten-product family: an exponential radius loss is allowed here, whereas that obstruction concerned one fixed Banach stage.

## 6. Restore the depth graph weights

Write E_(r,s,b) for the ideal-power presentation completion with weight

`b_s(r)(1+n)^r (b a)^n`, where `b_s(r)=(2 lambda s)^r r!`.

Give I^(r+1) the inherited E_(r,s,b) norm on the other side. Since r+1<=2^r for r>=1, section 5 gives

`||z||_(E_(r+1,s,b)) <= 2 lambda s ||z||_(E_(r,2s,64b))`.

The forward inclusion is already bounded by merging factors. These compatible endpointwise identity maps therefore identify the inherited-kernel intersection with the independent next-depth intersection, continuously in both directions. They also give simultaneous control over the depth labels with the displayed loss, rather than an unspecified family of finite-corner equivalence constants.

To extend the inverse comparison, approximate by finite endpoint support. The estimate makes the images Cauchy in each requested output seminorm; stabilized endpoint projections identify the limit with the original coordinate vector. Thus the claim includes surjectivity on the scale intersections, not merely dense image.

## 7. Comparison with common path quotients and the new attachment

The two-sided bound

`w_r ||z||_path <= nu_r(z) <= 32^n w_r ||z||_path`

also descends by taking infima over I^(r+1), or over any specified deeper ideal subspace of I^r. It identifies the corresponding common-path quotient and factorization-presentation completions on the all-radius scale, with radius loss at most 32 for the matched depth weights.

At any fixed r, changing a fixed polynomial path weight (1+n)^p to another such weight costs only a further fixed radius enlargement. This does not identify differently weighted Banach stages, or a single fixed-polynomial norm with all depths without their declared depth weights.

In particular the new results

- `../voevodsky/the-first-filtered-extension-is-strictly-exact-and-source-nonsplit.md`;
- `../voevodsky/the-completed-first-filtered-extension-has-a-nonzero-balanced-attachment.md`

already provide the common-path strict sequence

`0 -> I^2/I^3 -> I/I^3 -> I/I^2 -> 0`

and its nonzero continuous forcing/Clark attachment roof. The comparison above removes the previously open topology-identification issue on their compatible all-radius domains. The finite identity comparisons are source-equivariant, and so are their continuous extensions. No new attachment map or fitted pairing is introduced.

This is stronger than the forward associated-source-to-forcing bridge, but consistent with it: the extra ingredient is the source-only Fox factorization lift, not injectivity of the compact Clark map.

## 8. Remaining scope

Closed here: exponential source factorization lifting, comparison of inherited and independent ideal-power completions on the radius intersection, and the corresponding common-path quotient comparison.

Still separate: projectivity or flatness over a completed source algebra, a theorem computing its completed derived tensor functor, and a completed tensor-Hom beta equivalence. The existing first-attachment roof explicitly avoids assuming these. Fixed-stage nonclosed-range examples and analytical inverse instability remain valid.

## Verification

`uv run python research/nima/checkers/check_controlled_ideal_factorization_lift.py`

Artifact: `results/controlled-ideal-factorization-lift.json`.

Passed 442 marked-path recorder/section/telescoping checks, 184 normalized-form section checks, and 42 exact ideal-product lifts, including retained marks, nonlocal kernel factors, and three-factor lifts. The checks reconstruct each source product exactly from its lifted presentation.

The uniform estimates and completion identifications follow from the explicit formulas and bounds above, not from finite ranks or numerical conditioning. No new formal proof-assistant verification is claimed.
