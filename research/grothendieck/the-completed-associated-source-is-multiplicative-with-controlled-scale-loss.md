# The completed associated source is multiplicative with controlled scale loss

## Strength and result

**Completed source multiplication and comparison theorem.** On the existing endpointwise source scales, multiplication satisfies

||x y||_(s,b) <= ||x||_(2s,2b) ||y||_(2s,2b).

It descends through the closed associated-layer presentation kernels. The scale intersection is consequently a complete locally convex algebra of positive associated layers, and its faithful balanced analytical receiver is multiplicative after the prescribed suspension normalization.

The extra path/feature radius is substantive: multiplication is unbounded on a fixed source Banach scale, and a fixed loss only in the depth parameter cannot repair it. An all-forgotten family proves this without analytical conditioning estimates.

No signed metric is changed. This is multiplication of coefficient layers and their typed seam realizations, not multiplication or duplication of independently chosen root states. It does not reconstruct the original filtered extension from the associated graded algebra alone.

## 1. Source, presentations, and norms

Let G^r=I^r/I^(r+1), for r>=1, at each stabilized finite endpoint interval c=(x,y). Keep the endpoint labels. Let n(c) be its event length. Multiplication is the source operation

G^r_(x,y) tensor G^t_(y,z) -> G^(r+t)_(x,z).

Noncomposable endpoint pairs multiply to zero. Event lengths add under composition.

Use the existing r-factor presentation P^r_c inside the marked-path tuple space, with its coefficient l1 norm. Its kernel K^r_c consists of the action-balancing and next-layer relations identified by the finite source theorem. The quotient is the actual G^r_c.

Let a>=1 be the fixed source letter bound, lambda the fixed seam insertion bound, and

b_s(r)=(2 lambda s)^r r!,

W_(s,b)^r(n)=b_s(r) (1+n)^r (b a)^n.

The source space X_(s,b) is the l1 sum of the endpoint quotient norms induced by these weighted presentations. These are the weights already used in the all-depth and holomorphic-feature source domains; they are not new fitted forms.

Every nonzero r-factor source presentation has n>=2r, because a relation consumes at least two events. This source constraint is essential to the estimate below.

## 2. The weight estimate

For composable lengths n,m and depths r,t, put

P=(1+n+m)^(r+t) / [(1+n)^r (1+m)^t].

Using log(1+u)<=u and r<=n/2, t<=m/2 gives

log P
 <= r m/(1+n) + t n/(1+m)
 <= (n+m)/2.

Since exp(1/2)<2,

P <= 2^(n+m).

The graph factorial ratio obeys

b_s(r+t) / [b_(2s)(r) b_(2s)(t)]
 = binomial(r+t,r)/2^(r+t) <= 1.

Finally the input radius 2b pays for 2^(n+m). Therefore

W_(s,b)^(r+t)(n+m)
 <= W_(2s,2b)^r(n) W_(2s,2b)^t(m).

This includes arbitrarily unequal lengths and depths. It does not infer an estimate by treating those quantities as comparable. Without the minimum-event constraint the displayed inequality can fail.

## 3. Presentation multiplication and closed-kernel descent

On finite presentations, concatenate the two ordered lists of relation factors. Expansion in marked-path tuples gives the usual l1 convolution inequality; typed endpoint matching only removes incompatible terms. Applying section 2 yields the weighted presentation bound with constant one.

The kernels are multiplicative in the required sense. If p maps into I^(r+1), its product with a t-factor presentation maps into I^(r+t+1). The same applies on the other side. Action-balancing relations are respected by source multiplication. Thus

K^r P^t + P^r K^t maps into K^(r+t).

This proves finite quotient descent independently of any analytical receiver or Gram matrix.

At every scale the endpointwise kernel is closed, as in Voevodsky's quotient construction. The presentation product is continuous between the indicated scales. Approximating by finite endpoint support shows that its products with the completed kernels still lie in the output kernel. Taking infima over presentation lifts therefore gives

||x y||_(s,b) <= ||x||_(2s,2b) ||y||_(2s,2b)

on the Banach quotient spaces. No bounded linear choice of quotient representatives is required. Finite-corner approximate lifts with summable errors suffice.

## 4. A complete locally convex source algebra

Set

X_infinity=intersection_(integer s,b>=1) X_(s,b)

with its existing seminorms and endpoint/depth coordinates. The compatible intersection is complete. The inequality proves jointly continuous multiplication on it.

Associativity is inherited from source composition. For a direct continuity proof, both bracketings of a triple product are controlled by the input seminorm (4s,4b), so the finite associativity identity extends by density. Fixed endpoint coordinates also give a direct check: only finitely many intermediate vertices and relation depths contribute inside a fixed monotone interval.

This theorem concerns the positive associated layers. It does not silently adjoin an infinite sum of vertex identities as a global unit. The finite source idempotents and endpoint types are retained.

## 5. Why a fixed source Banach scale is not an algebra

Let a_n be a forgotten two-event diamond relation followed by a selected all-forgotten suffix, of total length n. Let b_n be the forgotten diamond on two fresh events following that endpoint. Their classes have depth one, and

||a_n||_(s,b) <= 2 W_(s,b)^1(n),

||b_n||_(s,b) <= 2 W_(s,b)^1(2).

The product has a nonzero class in G^2. To certify this, choose in the balanced two-seam derivative the first edge of the initial diamond and the first edge of the final diamond, with all buffers vacuum. Its coefficient on a_n b_n is one.

On any marked-path tuple in the two-factor presentation, that same coefficient has absolute value at most one: a monotone path can cross a prescribed edge only once, and the vacuum probe requires every unselected event to be forgotten. The balanced map factors through G^2, so the functional annihilates the presentation kernel. It follows that

||a_n b_n||_(s,b) >= W_(s,b)^2(n+2).

Thus the ratio of output norm to the two input norms is at least

(n+3)^2 / [6(n+1)]
 = (n+5)/6 + 2/[3(n+1)],

which diverges. All exponential source weights cancel here; so do the fixed lambda and s factors except for the factorial ratio already displayed.

Replacing the input depth parameter s by any fixed larger parameter changes this lower bound only by a constant. A depth-only scale loss cannot give a uniform product bound for these norms. The path-radius loss in section 2 is therefore not a dispensable convenience, although no optimal constant is claimed.

This witness uses source coefficients and quotient functionals, not a lower bound inferred from feature injectivity or self-pairing positivity.

## 6. Normalize the target before asserting multiplicativity

Let T_R be the existing balanced analytical single-seam complex. Use

Z_r=(T_R[-1]) tensor_R ... tensor_R (T_R[-1]),

with r factors. Its bottom degree is zero. The conormal derivative is a B-bimodule map into the closed degree-zero part of T_R[-1], via the admitted coefficient embedding B->R.

The source theorem gives G^r=C^(tensor_B r), where C=I/I^2. Tensoring the single-seam derivative therefore defines

jhat_r:G^r -> Z_r,

and the finite equality

jhat_(r+t)(x y)=jhat_r(x) tensor_R jhat_t(y).

This is ordinary source multiplication followed by balanced tensoring. No exchange of factors, arbitrary cut section, or fitted scalar comparison is involved.

The displayed Z_r is canonically related to the earlier J_(R,r)[-r]. With the declared tensor-of-shifts convention, the comparison on bottom cycles has phase

c_r=(-1)^(r(r-1)/2).

Consequently it sends jhat_r to c_r times the previously normalized positive raw cycle map j_r. The phases satisfy

c_(r+t)=c_r c_t (-1)^(r t).

Use Z_r for the strict multiplicative statement, or transport the multiplication through these prescribed identifications. Do not claim that the positive raw j_r is multiplicative under an uncorrected naive tensor of shifted targets.

The existing attachment target J_(R,r)[1-r] and its connecting map are unchanged. Converting between presentations carries the same c_r; it is not a new coherence parameter.

## 7. Extension to the completed analytical comparison

Reindexing the target cochain degrees as Z_r does not change its shape norms, active-edge count, feature count, or the previously proved estimates. Target balanced tensoring satisfies

||u tensor_R v||_(s,b) <= ||u||_(2s,b) ||v||_(2s,b).

The source layer maps are continuous into the corresponding target scales by the existing path-length bounds. Therefore the finite multiplicative identity extends by density to X_infinity. This yields a continuous injective algebra map into the normalized balanced seam scale.

Injectivity remains the endpointwise argument: every finite endpoint and depth projection is the established faithful function-valued map. Products introduce no new unidentified relations between endpoints. The image consists of bottom cycles; there are no incoming boundaries in those normalized bottom degrees.

This is an associated-layer coefficient algebra comparison. Full derived receiver modules still retain their actual vertex carriers. Tensoring two coefficient histories does not authorize multiplying or copying independently prepared root states.

## 8. This does not repair stable reconstruction

The all-forgotten suffix family also prevents a continuous inverse on the scale intersection. Normalize its depth-one class to have source norm one in X_(1,1). Its target consists of four vacuum seam coordinates. In every target seminorm the depth is fixed and the feature count is zero, so its norm tends to zero as the source path length tends to infinity, whereas its X_(1,1) norm remains one.

Thus the stronger source is faithfully represented but not topologically embedded with a continuous inverse. In particular the image is not closed in the complete target scale: if it were closed, the open mapping theorem for Frechet spaces would give that inverse continuity.

The new multiplication theorem does not change the prescribed Green form, assert source positivity, or turn weak paired separation into stable norm reconstruction.

## 9. Relation to the separately convergent current channels

Voevodsky's forcing-resolved completion now controls the bulk, forcing, and vacuum channels separately. Its subsequent noncollapse theorem proves injectivity of the normalized Clark map on the full weighted forcing space and of its finite projective tensor powers, hence faithful realization of summable forcing-resolved normal-form records. Both convergence and noncollapse are closed on that declared domain. The one-letter map is Hilbert--Schmidt, so injectivity supplies no stable inverse or forcing-norm estimate in the weaker feature-image norm.

The multiplication theorem here concerns the existing weighted associated-layer quotient norms. It neither infers forcing norms from output feature norms nor identifies the forcing-resolved projective completion with this quotient scale without a separate comparison. Existing relative-current identities are retained; no new correction is fitted to make multiplication hold.

## Verification

`python research/grothendieck/checkers/check_completed_source_multiplication.py`

Passed:

- 20736 exact integer weight inequalities;
- five highly unequal length/depth cases;
- rejection when the minimum-event hypothesis is removed;
- 63 actual forgotten-suffix product witnesses, with a surviving balanced coefficient;
- 1521 suspension-phase composition checks.

The Banach quotient descent, Frechet algebra construction, and completed analytical multiplicativity are the proofs above. No finite experiment is used to infer completed injectivity or a norm lower bound for the Clark feature map.

References:

- `research/nima/nonminimal-relation-factorizations-descend-through-balanced-seam-complexes.md`;
- `research/voevodsky/endpointwise-separation-and-bounded-differentials-close-the-fixed-depth-l1-receiver.md`;
- `research/voevodsky/an-all-depth-seam-scale-has-bounded-differential-and-continuous-balanced-tensoring.md`;
- `research/voevodsky/holomorphic-feature-closure-retains-completed-cross-spectral-packets.md`;
- `research/voevodsky/bulk-and-forcing-currents-converge-separately-on-the-forcing-resolved-completion.md`;
- `research/voevodsky/the-forcing-resolved-completion-embeds-faithfully-in-normalized-clark-features.md`.
