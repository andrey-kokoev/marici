# Completed attachments are strict only with the kernel topology specified

## Follow-up

`universal-form-fox-lifts-control-the-completed-ideal-power-topologies.md` now proves the missing reverse comparison: nu_2<=32^n nu_1 and, generally, nu_(r+1)<=64^n nu_r. Thus the inherited and independent next-depth completions agree on the compatible all-radius intersections. The fixed-Banach-stage obstruction below remains valid. References below to the norm-comparison gate record the question resolved by that follow-up; completed tensor-functor justification remains separate.

## Result

There is a continuous strict completed source attachment, with an explicit connecting map and bounded fibre reconstruction, provided the kernel carries the topology inherited from the completed middle ideal power.

It is generally **not** the sequence obtained by independently completing each ideal power with its own depth weight. At a fixed Banach stage, that natural adjacent-depth inclusion has dense nonclosed range. An exact source family has norm ratio 1/(1+n), where n is event length.

The inherited-topology triangle has a continuous contragredient square and a bounded termwise quotient model with the familiar shifted connecting projection. Calling that model the derived tensor product over a completed source algebra, or composing its next-layer term with the previously completed analytical receiver, requires additional estimates. Those assertions do not follow from finite source heredity.

## 1. Norms must be declared before completing the sequence

Use the finite relation tower and the endpointwise source presentations from:

- `../grothendieck/packet-refinement-preserves-the-relation-tower-but-coarse-seams-lose-higher-products.md`;
- `../voevodsky/endpointwise-separation-and-bounded-differentials-close-the-fixed-depth-l1-receiver.md`;
- `../voevodsky/an-all-depth-seam-scale-has-bounded-differential-and-continuous-balanced-tensoring.md`.

Fix r>=1 and first work at one Banach stage. Write

`w_r(n)=(1+n)^r a^n`.

A fixed feature radius can be included by replacing a with b a. The graph multiplier at fixed depth is a positive constant; it is suppressed initially and restored below. No finite Green form is changed.

For each finite endpoint interval c, let P_(r,c) be its r-factor relation presentation with the prescribed weighted path-tuple l1 norm. Multiplication maps it onto I_c^r. Define nu_(r,c) on I_c^r by that quotient norm, BEFORE quotienting by I_c^(r+1).

Put

`E_r = l1 direct_sum_c (I_c^r,nu_(r,c))`,

`A_r = {x in E_r : x_c in I_c^(r+1) for every c}`,

`X_r = l1 direct_sum_c (I_c^r/I_c^(r+1), quotient of nu_(r,c))`.

X_r is the already used associated-layer completion: quotienting a presentation first by the multiplication kernel and then by the next ideal power is the same quotient norm as mapping the presentation directly to G^r.

A_r carries the norm inherited from E_r. It is not, by definition, the independently weighted E_(r+1).

## 2. Strict exactness with the inherited kernel norm

Each endpoint space is finite dimensional. Bounded endpoint projections show A_r is closed in E_r. Finite-support truncation shows it is exactly the closure of algebraic I^(r+1) in that inherited norm.

The standard l1 quotient argument gives

`0 -> A_r --mu--> E_r --q--> X_r -> 0`

as a strict exact sequence: mu is an isometric closed inclusion, q is a metric quotient, and its kernel is precisely A_r. To lift a summable quotient vector, choose finite-corner lifts with a summable sequence of norm errors. Finite-dimensionality also allows norm-minimizing lifts.

The source actions remain part of the data. Multiplication by a fixed marked path of length l has norm at most (1+l)^r a^l on the r-presentation norm. It preserves the ideal subspaces and therefore extends to the completions and quotients. One may use the corresponding weighted source algebra, or retain these compatible bounded path actions. No source-linear section is selected.

## 3. The continuous connecting map and fibre

Represent X_r by the strict two-term resolution

`K_r=[A_r --mu--> E_r]`, in degrees -1,0.

The augmentation to X_r is a strict quasi-isomorphism. In the derived category using strict exact source-module sequences, the connecting map is represented by

`delta_hat:K_r -> A_r[1]`,

identity in degree -1 and zero in degree zero.

Its fibre is the explicit complex

`[A_r -> A_r direct-sum E_r]`,

with differential `a -> (-a,mu a)`. Use the l1 direct-sum norm. The maps

`p(a,e)=e+mu a`, `i(e)=(0,e)`, `H(a,e)=-a`

satisfy

`p i=id`, `id-i p=d H`, `H d=id`

in the appropriate degrees. The maps p,i,H have norm at most one, and the displayed differential has norm at most two. Thus the fibre reconstructs E_r by bounded source-linear maps, without choosing a section of q.

The attachment remains nonsplit as source-module data. Restrict a putative equivariant splitting to a finite critical packet with I^(r+1) nonzero and I^(r+2)=0. Both the quotient G^r and the subobject I^(r+1) are annihilated by I there, whereas I acts nontrivially on I^r. A splitting would contradict I I^r=I^(r+1). Finite terminal/packet summands retain this obstruction inside the completion.

## 4. Why independent adjacent-depth completions fail

There is a continuous natural map

`E_(r+1) -> A_r`.

Merge the first two relation factors of an (r+1)-factor presentation. This does not increase its unweighted path-tuple coefficient l1 norm. At an endpoint of length n,

`nu_r(z) <= nu_(r+1)(z)/(1+n)`.

The loss is genuine. Let a_1,...,a_(r+1) be successive forgotten diamond relations, and append a fixed all-forgotten suffix w to the last factor. Put

`p_n=a_1 ... a_(r+1) w`,

with total event length n>=2(r+1). Its 2^(r+1) source coefficients have modulus one and distinct paths.

The (r+1)-factor presentation attains this coefficient l1 mass. Merging the first two relations gives an r-factor presentation attaining the same mass. Conversely multiplication cannot increase path-coefficient l1 norm. Hence the two infima are exact:

`nu_(r+1)(p_n)=2^(r+1) w_(r+1)(n)`,

`nu_r(p_n)=2^(r+1) w_r(n)`.

Their ratio is exactly 1/(1+n). Fixed graph multipliers multiply this ratio by the constant b_s(r)/b_s(r+1); they do not remove its decay.

Normalize p_n to E_(r+1) norm one and choose distinct endpoint lengths n_k with 1/(1+n_k)<=2^(-k). The sum of their images converges in A_r. Any preimage in E_(r+1) would have norm-one components at all those endpoints and hence infinite l1 norm.

Therefore the natural inclusion has proper dense, nonclosed image in A_r. In particular

`0 -> E_(r+1) -> E_r -> X_r -> 0`

is not even exact at E_r as a sequence of the independently completed Banach spaces. Its missing middle vectors lie in ker q but not in the image of E_(r+1).

This is a source-topology obstruction, separate from the receiver's nonclosed image proved by the forgotten-suffix and tail-localized families.

## 5. Compatible scale intersections: what follows and what does not

At fixed r, reinsert the graph and feature-radius weights

`b_s(r) (1+n)^r (b a)^n`.

They multiply every norm in a fixed endpoint presentation by one scalar. Thus a finite-corner lift minimizing the underlying quotient norm works simultaneously for all s,b. Coordinatewise such lifts prove surjectivity onto the intersection of the X_(r,s,b), with the same seminorm bounds.

Accordingly the inherited-kernel sequence also gives a strict exact Fréchet sequence on that specified compatible intersection, and the bounded fibre formulas remain valid seminorm by seminorm.

Do not infer from section 4 that independently completed adjacent powers necessarily differ on the entire radius intersection. The polynomial factor 1+n is absorbed by a radius change b->2b, since 1+n<=2^n. The explicit fixed-stage family alone cannot decide that stronger comparison.

Conversely, this absorption does not prove equivalence of the two general ideal-power norms. One still needs bounds for lifting arbitrary elements of I^(r+1) from their inherited r-factor norm to their own (r+1)-factor presentation norm. Finite-dimensional equivalence at each corner supplies no uniform radius-loss estimate.

## 6. The quotient-model projection remains continuous

Within A_r let A_r^(2) be the closed subspace with endpoint values in I^(r+2), again with the inherited nu_r norm, and define

`Z_r=A_r/A_r^(2)`.

It completes the finite layer G^(r+1) with an INHERITED norm, not automatically its independently declared depth-(r+1) norm.

Taking the termwise closed ideal-action quotients of K_r gives

`Q_r=[Z_r --0--> X_r]`.

The differential vanishes because mu lands in the next ideal power. The quotient-unit model has components

`eta^(-1):A_r->Z_r`, `eta^0:E_r->X_r`.

All maps are bounded. The square

```
K_r  --delta_hat-->  A_r[1]
 | eta                 | quotient[1]
 v                     v
Q_r  --projection-->  Z_r[1]
```

commutes literally. Thus the completed model retains the same shifted connecting projection, with its norm now explicitly specified.

At every finite packet this is the known one-sided derived quotient calculation, performed on the full source modules before taking corners. Globally it is a continuous quotient diagram for the chosen completed resolution. It is NOT yet a proof that Q_r computes a derived completed tensor product over a new completed algebra: projectivity of finite path-algebra ideals does not imply Banach projectivity or flatness of these completions.

## 7. The continuous contragredient square

For the intrinsic continuous conjugate duals, strictness gives

`0 -> X_r^h -> E_r^h -> A_r^h -> 0`.

The last map is restriction of functionals and is surjective by Hahn--Banach. This is not a statement that every such functional comes from an ambient Clark observer.

The cochain dual of K_r has E_r^h in degree zero, A_r^h in degree one, and differential

`-mu^vee`.

The dual of delta_hat is the corresponding inclusion in degree +1 on this model. Dualizing the square in section 6 reverses its arrows and gives the same componentwise identity between the restriction/pullback maps. No Hermitian form on the completed ideal powers has been fitted to obtain it.

Finite-endpoint Green observations compose with this square through the existing beta maps. Extending the full analytical comparison to all of Z_r requires a bounded map from its inherited norm into the balanced target. The established analytical estimate is on the independently normed next associated layer; it must not silently be substituted for this estimate.

Nor does the intrinsic dual exact sequence make the completed ambient beta map surjective onto the full source dual. The explicit continuous-dual obstruction from `tail-localized-diamond-cycles-obstruct-stable-inversion-at-fixed-event-length.md` remains in force.

## 8. Separation from the new current convergence theorem

The new input `../voevodsky/bulk-and-forcing-currents-converge-separately-on-the-forcing-resolved-completion.md` supplies separate absolute convergence of bulk and forcing channels on its declared forcing-resolved topology. It removes the separate-current convergence gate there.

It does not compare the inherited ideal-power norm nu_r with the independent norm nu_(r+1), and does not assert completed module projectivity. The source attachment issue above therefore remains distinct from that successful analytical convergence result.

Two further inputs sharpen this separation:

- `../grothendieck/the-completed-associated-source-is-multiplicative-with-controlled-scale-loss.md` proves multiplication on the associated-layer scale with input loss (s,b)->(2s,2b), including its suspension normalization. This is an upper bound on products, not a uniform lifting bound for an arbitrary element of the filtered subobject I^(r+1) equipped with nu_r. As that note specifies, associated-graded multiplication alone does not reconstruct the filtered extension.
- `../voevodsky/the-forcing-resolved-completion-embeds-faithfully-in-normalized-clark-features.md` proves injectivity on the full weighted forcing space and its finite projective tensor powers. Its compact one-letter map has no bounded inverse. Thus this faithful forcing-resolved realization cannot be used to pull back a missing factorization-norm estimate from the output feature topology.

Neither result conflicts with the strict inherited-kernel triangle. They do not yet identify its kernel or quotient-model next layer with the independently completed next-depth source via a controlled inverse comparison.

## 9. Disposition

Established:

- a strict completed source attachment using the inherited kernel norm;
- its continuous nontrivial connecting class and explicit bounded fibre reconstruction;
- its intrinsic continuous contragredient square;
- the continuous zero-differential quotient model and connecting projection;
- failure of the naive adjacent-depth Banach completion sequence, with exact norm ratio.

Still required to identify this with the entire previously completed analytical attachment: a uniform comparison or controlled radius-loss estimate for the next ideal/layer norm, followed by the appropriate completed tensor-functor justification. No universal exactness of completion, completed hereditary theorem, or full ambient-observer duality equivalence has been inferred.

## Verification

`uv run --with sympy python research/nima/checkers/check_completed_attachment_norms.py`

Artifact: `results/completed-attachment-norms.json`.

Passed exact fibre and homotopy identities with explicit l1 bounds, the source-linear splitting hostile, the dual differential sign, the quotient chain equation, and fifteen actual forgotten-product norm/cycle fixtures through event length 64.

The strict completion, nonclosed-range, and Fréchet lifting assertions are the proofs above, not extrapolations from finite matrices. No new Agda verification is claimed.
