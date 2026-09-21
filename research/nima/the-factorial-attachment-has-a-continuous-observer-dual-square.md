# The factorial attachment has a continuous observer-dual square

## Result and qualification

The first factorial filtered attachment admits a continuous contragredient square on its explicit two-term model. The observer domain is the graph domain of the prescribed ambient Green mate, not an assumed self-duality of the completed cut-l1 carrier.

The joint observer pullback does NOT exhaust the continuous source dual. A translated four-event product provides a bounded approximate-null family even on the factorial source, and an explicit source functional without any continuous joint-target lift.

This constructs model-level paired naturality. It does not identify the scalar continuous dual with perfect-module Hom into the source algebra, assert completed projectivity, or claim a completed tensor-Hom beta equivalence.

Inputs include:

- `../voevodsky/the-completed-first-filtered-extension-has-a-nonzero-balanced-attachment.md`;
- `../voevodsky/factorial-fox-summability-has-a-vacuum-necessity-test-and-compatible-filtered-exactness.md`;
- `the-attachment-opposite-comparison-needs-a-koszul-correction-and-a-distinct-green-dual.md`;
- `tail-localized-diamond-cycles-obstruct-stable-inversion-at-fixed-event-length.md`.

## 1. Source complex and dual topology

Use the factorial common-path spaces and their actual quotient seminorms. Let

`P=J_2/J_3`, `E=J_1/J_3`, `C=J_1/J_2`,

where the J_i now denote the closed ideal-power subspaces of the specified factorial domain. The strict source sequence gives

`K=[P --mu--> E]`, in degrees -1,0,

its augmentation q:K->C, and the projection pi:K->P[1].

For a locally convex space V, V^h is its continuous conjugate-linear scalar dual, with the STRONG topology of uniform convergence on bounded subsets. This is not Hom_S(V,S). Every continuous linear map induces a continuous pullback between these strong duals: its image of a bounded set is bounded.

Use

`(V^h)^n=(V^(-n))^h`,

`d_(V^h)^n=(-1)^(n+1) (d_V^(-n-1))^vee`.

Thus K^h has E^h in degree zero and P^h in degree one, with differential -mu^vee. The dual connecting projection is the literal degree-one inclusion

`pi^vee:P^h[-1] -> K^h`.

At each common factorial Banach stage, Hahn--Banach gives the strictly exact scalar-dual sequence 0->C^h->E^h->P^h->0. On the all-radius intersection the scalar-dual sequence is algebraically exact by locally convex Hahn--Banach, and the maps are strong-continuous. We do not infer strictness in the strong-dual topology, or a derived duality equivalence, merely from that algebraic exactness.

There is a further scale distinction: factorial source multiplication loses radius. A fixed source path need not act boundedly on one unchanged factorial Banach stage. Source actions are continuous on the all-radius intersection, with the previously established scale losses. The Banach-stage estimates here concern linear complexes and functional bounds; they do not silently make each stage a module over one fixed Banach source algebra.

## 2. The joint target and prescribed beta map

Let T=J_(R,2)[-1] be the analytical joint target. Its nonzero degrees are -1,0,1. Retain the existing graph/feature scale and its J-invariant ambient feature envelope. Write

`beta_T(y)(x)=q_T(x,y)`

degreewise, using the prescribed Green form and compatible typed shapes. The form is bounded at the positive carrier norms, so beta maps continuously into the strong continuous dual of the scale intersection. For a bounded set B of inputs, its strong-dual seminorm is bounded by the corresponding input bound on B times an observer seminorm.

The ambient beta is injective: a nonzero shape coordinate is separated by a same-shape vector using its nondegenerate ambient signed carrier. This does not assert nondegeneracy of the form restricted to a source image.

Beta need not be onto the continuous dual. In particular l1 completion must not be treated as if its dual were the same l1 space.

## 3. An explicit observer complex without an unproved mate extension

Boundedness of d on a cut-l1 carrier gives a bounded transpose on its dual, not automatically a Green mate on the original cut-l1 carrier. Define the representable-mate graph domain instead.

In degree n, an observer is a pair (y,z), with y in T^(-n) and z in T^(-n-1), satisfying

`beta_T(z)=(-1)^(n+1) d_T^vee beta_T(y)`.

Here the transpose uses the differential from T^(-n-1) to T^(-n). Injectivity of beta makes z unique. Give this domain O_T^n the graph seminorms

`||y||_(s,b)+||z||_(s,b)`.

The equation defines a closed subspace of the product of the two complete target spaces: both sides are continuous into a Hausdorff continuous-dual space. Thus the graph domain is complete, at each fixed Banach scale and on the compatible intersection.

Set d_O(y,z)=(z,0). This is well defined because (d_(T^h))^2=0. It has graph-seminorm norm at most one, and d_O^2=0. The map (y,z)->beta_T(y) is a continuous chain map O_T->T^h.

This is the maximal domain, within the declared ambient observer carrier, whose first Green mate remains representable there. The construction does not assert that every cut-l1 observer lies in it. It retains the prescribed finite packet/finite total-feature-degree Green observations: their mates remain in the corresponding finite shape sectors. No new signed form is fitted.

For the unshifted joint differentials d2 and d1, the shifted dual differentials are -d1^vee and +d2^vee. Their graph-domain Green presentations have exactly the same signs with the prescribed Green mates. Opposite-history reversal is a different operation and is not used here.

## 4. The continuous attachment square

The existing joint observation is

`j:P[1] -> T`, given by D2 in degree -1,

and the attachment component is F2=j pi:K->T. It is first defined on forcing records and transferred to the normalized analytical target. The factorial jet estimate bounds j and F2 at matching scales: for a sufficiently enlarged source radius R, their operator norms are at most two. The fixed forcing-to-Clark feature-radius loss is included in this choice of R.

The required square is

```
O_T  -------- beta_T --------> T^h
 |                             |
 | j^vee beta_T                | F2^vee
 v                             v
P^h[-1] ------ pi^vee -------> K^h
```

It commutes literally because (j pi)^vee=pi^vee j^vee. All arrows are continuous chain maps. At matching Banach stages beta has bound at most one, the two attachment pullbacks have bound at most two, and pi^vee has bound one. On the intersection, for bounded B subset P,

`sup_(p in B) |q_T(j p,y)|
 <= 2 [sup_(p in B) q_R(p)] ||y||_(s,b)`.

This proves strong-dual continuity without identifying the strong topology with an unspecified inductive-limit topology.

The source-linear finite identities persist with the declared continuous source actions and their mates wherever those actions preserve the observer domain. More generally the intrinsic transposed square is source-contragredient on the full continuous dual modules. We do not assert that every continuous dual action is represented by an ambient observer in O_T.

At a common Banach stage, q^vee:C^h->K^h is a strict quasi-isomorphism of scalar complexes by the dual exact sequence. On the full intersection the displayed model-level square and dual connecting inclusion are the asserted comparison. Promotion to a strict localized strong-dual module equivalence is a separate claim, not implicit in this construction.

## 5. Why this is not surjectivity onto the full source dual

Take two consecutive two-event diamonds on four fixed event primes, translated by growing background products Q_N using other primes. Let a_N be the singly retained relation on the first diamond and c_N the forgotten relation on the second. Put v_N=a_N c_N.

These are four-event elements of I^2. In their corners I^3=0, so no next-power quotient changes their path coefficient norm. Each has eight coefficients of modulus one. Normalize them to have the first factorial source seminorm one, calling the results u_N. In every fixed source radius their norms are constant in N (the radius dependence is R^4).

Their images are

`j(u_N)=D(a_N) tensor_balanced D(c_N)`

with the same normalization. Every term contains exactly one retained feature supported beyond log(2 Q_N). The established localized feature bound gives

`||j(u_N)||_(s,b) <= C_(s,b) exp(-epsilon log(2 Q_N)) ->0`

in every target seminorm. Depth, event length and feature count are fixed, so the factorial and graph weights do not remove this decay.

The endpoints are distinct. In each chosen source corner choose a norm-one conjugate-linear functional taking u_N to one, and sum these coordinate functionals. The endpointwise l1 norm gives a continuous functional ell on P, bounded by its first seminorm, with ell(u_N)=1 for every N.

No continuous target functional psi can satisfy ell=j^vee psi, because continuity would force psi(j(u_N))->0. In particular ell is not in the image of j^vee beta_T from the observer graph domain. The failure holds even if one allows all continuous joint-target functionals rather than just Green-representable observers.

This concerns the full source functional space, not a claim that a particular degree-one vector is a nonzero scalar cohomology class of K^h. Intrinsic dual exactness and source-module attachment classes must remain distinct.

## 6. Disposition

Established: a declared strong continuous-dual topology, a complete representable-mate observer complex, the signed dual connecting inclusion, a continuous paired attachment square with scale bounds, and a concrete obstruction to full source-dual surjectivity.

Not established: equality of the observer graph domain with the whole receiver, strict strong-dual exactness on the intersection, completed perfect-module tensor-Hom equivalence, or identification of contragredient duality with opposite-history reversal.

Separate bulk/forcing currents remain those of the forcing-resolved theorem. The present square uses the prescribed analytical Green beta and does not obtain separate current convergence from their sum or manufacture a relation metric.

## Subsequent inputs and domain boundaries

`../grothendieck/actual-letter-weights-characterize-marked-fox-summability.md` identifies a larger exact forcing-resolved coefficient domain using actual letter norms Gamma(w). The present square and its stated functional obstruction use the unweighted factorial source topology. They are not automatically claims about every continuous dual of that larger domain: its functional continuity and filtered-presentation comparisons require their own checks. In particular, the source functional in section 5 was bounded using the declared unweighted source seminorm.

`../voevodsky/the-euler-prime-channel-has-a-source-defined-shift-operator-comparison.md` adds a genuine one-slot prime operator on H_gamma. Its form uses the prescribed unweighted half-line pairing, despite the weighted control norm. This reinforces the distinction between domain norms and paired observation. It does not replace the ambient Green beta in the square above, identify bulk/forcing with gamma/prime channels, or supply a two-seam arithmetic tensor-Hom equivalence. No invertibility of its prime form is presumed here.

## Verification

`uv run --with sympy python research/nima/checkers/check_factorial_attachment_dual_square.py`

The checker uses non-real differentials and signed ambient forms to verify shift/dual signs, mate naturality, square-zero, the joint-cycle pullback, and the dual connecting inclusion. Its matrices are algebraic fixtures, not sampled Clark spectra. The completion, graph-domain and non-surjectivity arguments are the proofs above.
