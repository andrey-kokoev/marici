# Convex source heights preserve endpoint budgets through attachment operations

## Result

A proper height compatible with the existing source can be constructed from its complete typed vertex labels by finite convex closure. With this height:

- concatenation preserves a fixed height-moment class, with the usual path-radius loss;
- Fox cuts, terminal retractions and relation-factor lifts retain their old bounds with the SAME height moment;
- existing endpoint-preserving balancing estimates transfer unchanged;
- finite-height projection is multiplicative and commutes with these source operations.

This closes the operation-stability gate left by `endpoint-tightness-completes-finite-packet-approximation-of-filtered-towers.md`. Height is an additional positive prior, not a change to the original source, relation ideal or response norm.

A necessary convention is explicit: a tuple or receiver record is charged ONE height weight for its total outer corner. Independently charging every tensor factor has a different estimate, recorded below.

## 1. Build the height from the actual typed vertex set

Use the existing countable, directed, locally finite source: event paths are acyclic, and the interval between fixed compatible endpoints contains finitely many vertices and marked paths. Keep all packet/background labels that the source actually retains; identify ambient refinements only where the source already identifies them.

Fix an injective positive-integer code g(v) for the COMPLETE declared vertex labels. For finite arithmetic labels this may be a fixed canonical encoding of their integer/prime data and retained type fields. The proof does not require that numerical endpoint size alone distinguish vertices. No new vertices or arrows are introduced.

Let C_H={v:g(v)<=H}. Define

`V_H=union { [a,b] : a,b in C_H and a<=b }`.

Intervals with a=b include the seeds. Each V_H is finite by local finiteness, and the increasing family exhausts the vertices.

It is convex. If u lies in [a,b], v lies in [c,d], and u<=z<=v, then a<=z<=d, with a,d in C_H; therefore z belongs to V_H.

Set h(v)=min{H:v in V_H}, and for a corner c=[x,y] set

`h(c)=max(h(x),h(y))`.

Its sublevel corners form a finite full convex source packet. In particular h is proper on corners, unlike an incomplete numerical endpoint label. For every intermediate vertex z in [x,y],

`h(z)<=max(h(x),h(y))`.

The chosen coding specifies the prior; no coding-independent equivalence of all power-moment classes is asserted. What removes the earlier arbitrary-enumeration obstruction is convex closure, not a claim that this code is a unique physical observable.

## 2. Concatenation preserves fixed height moments

For eta>0 use the extra source seminorm

`Q_(R,eta)(x)=sum_c n(c)! R^n h(c)^eta ||x_c||_Gamma`.

For composable corners [x,y],[y,z],

`h([x,z])<=max(h([x,y]),h([y,z]))
          <=h([x,y])h([y,z])`.

Together with exact Gamma multiplicativity and (n+m)!<=2^(n+m)n!m!, this proves

`Q_(R,eta)(xy)<=Q_(2R,eta)(x) Q_(2R,eta)(y)`.

There is also the useful one-moment-at-a-time bound

`Q_(R,eta)(xy)
 <=Q_(2R,eta)(x)Q_(2R)(y)+Q_(2R)(x)Q_(2R,eta)(y)`.

Thus the all-radius fixed-eta domain is a complete locally convex source algebra. Its cornerwise ideal powers are closed subspaces as before. These are prior classes inside S_Gamma, not replacements for it.

## 3. Fox cuts and full forcing-resolved jets

Charge each receiver record the factor h(c)^eta of its total outer source corner. Equivalently this is the maximum vertex height along its typed buffers and seams: every intermediate vertex lies in [x,y], and the two outer endpoints are still present among the labels.

Every Fox cut term retains this same outer corner. Multiplying the existing cornerwise estimate by h(c)^eta therefore gives

`||D(x)||_(F_(s,b,eta)) <=2 Q_(ceil(2 lambda s b),eta)(x)`.

The labelled top-jet argument also gives

`Q_(R,eta)(x)<=||D(x)||_(F_(R,1,eta))`.

These bounds hold for the original forcing-resolved map with an added location prior on both sides. They do not imply an inverse from analytical outputs alone. No root state is copied.

For ordered jet convolution, the output height is at most the maximum of the two composable input heights. The existing graph/feature-radius convolution estimates therefore transfer with the same eta. There is no additional height-moment loss.

## 4. Terminal retractions and relation-factor lifts

The terminal normal-form retraction preserves both outer endpoints. Its replacement paths remain in the same interval. Consequently the weighted estimate from `theta-tail-dominance-controls-actual-letter-factorization-lifts.md` becomes

`||R(z_c)||_(Gamma,h^eta)<=kappa^n ||z_c||_(Gamma,h^eta)`

with the SAME kappa=2 C_tail.

For a composable r-tuple, define its height to be the maximum height of its factor corners. Convexity and the presence of the original outer endpoints imply this maximum is EXACTLY h(c), where c is the total corner. The old tuple norm can therefore be multiplied by the single scalar h(c)^eta.

The source-defined Fox lifts H and L_r preserve total corner and satisfy

`||H(z_c)||_(Gamma,tuple,h^eta)
 <=D(kappa^n-1)||z_c||_(Gamma,h^eta)`,

`||L_r(z_c)||_(Gamma,tuple,h^eta)
 <=Lambda^n ||z_c||_(Gamma,h^eta)`,

where D=(kappa+1)/(kappa-1) and Lambda=2(kappa+1). All original factorial, graph and radius comparisons follow unchanged. The native/inherited comparisons thus preserve this location prior on their all-radius intersections.

These are the expanded marked-path-tuple norms, not an unproved identification with a projective tensor product of independently completed ideal factors.

## 5. Balancing and the factorwise-height distinction

For an existing linear normalization or balancing map that preserves the total outer corner, a uniform unheighted bound transfers to the heighted norms with the SAME constant. Indeed h(c)^eta is scalar on that block, so multiply the established estimate and sum the corner norms. In particular the quotient balancing map is contractive for its quotient norm. Any extra cut normalization keeps its previously justified radius loss and constant; this argument does not manufacture an unproved bound.

This applies to the declared forward concatenation/balancing operations and to the selected finite observer normalization where its bound is already supplied. It does not assert that every analytical tensor functional descends, or that an arbitrary reverse-cut adjoint is bounded.

If instead a presentation is charged the PRODUCT of its r factor heights, each to power eta, then only

`product_i h(c_i)^eta <= h(c)^(r eta)`

follows. The lift is controlled by an input r*eta moment, not by the one eta moment proved above. Thus one may use all height moments for fixed-depth factorwise constructions, but no depth-uniform fixed-eta assertion for that different tensor norm is inferred.

## 6. Finite-height projection is now an exact source operation

Let P_H retain the corners whose endpoints are in V_H. It contracts every Q_R and Q_(R,eta), and preserves the cornerwise source ideal powers.

Unlike an arbitrary finite-corner projection, it satisfies

`P_H(xy)=(P_H x)(P_H y)`.

For an output corner inside V_H, every possible intermediate vertex in a composable path lies in that interval and hence in V_H. Thus no omitted path can leave the finite packet and return to contribute. For an output corner outside, at least one outer endpoint is absent, and the projected product is zero there as well.

Endpoint preservation also gives

`P_H R=R P_H`, `P_H D=D P_H`, `P_H L_r=L_r P_H`,

where target projection keeps the total outer corner. Projecting every typed factor is equivalent here, since all intermediate vertices are inside whenever the outer endpoints are. Existing endpoint-preserving balancing maps commute with the same projection.

These identities extend by continuity and density on the stated source/presentation domains. They preserve exact algebraic identities on the projected finite source. They do not assert that P_H is an endomorphism of the original source bimodule with its action unchanged; the projected source acts through the algebra map P_H.

## 7. Finite recovery with a structure-preserving cutoff

The usual moment bound is now compatible with every operation above:

`Q_R(x-P_H x)<=(H+1)^(-eta) Q_(R,eta)(x)`.

For example,

`Q_R(xy-(P_H x)(P_H y))
 <=(H+1)^(-eta) Q_(2R,eta)(x)Q_(2R,eta)(y)`.

For full forcing-resolved jets, with R_0=ceil(2 lambda s b),

`||D(x)-D(P_H x)||_(F_(s,b))
 <=2(H+1)^(-eta) Q_(R_0,eta)(x)`.

The finite convex packet has a finite maximum event length N_H. If 2(m+1)>N_H, its ideal power I^(m+1) vanishes in every retained corner. A compatible tower's level m then determines ALL of P_H x, not just a length-truncated part. Thus a finite level and a finite source packet reconstruct a finite source with the displayed error while retaining the source operations exactly on that packet.

This is stronger structurally than a separate length cutoff, which need not be multiplicative. For any prescribed tolerance and bounded height prior one can first choose H, then take m>=max(1,floor(N_H/2)). Computing an efficient numerical H from a particular label encoding is a separate task; no calibrated arithmetic measurement tolerance is claimed here.

An exact nonzero observer is not automatically preserved if its witness corner is discarded. Include the known witness's finite vertex support when choosing H. This neither modifies Voevodsky's calibrated finite-prime certificate nor treats noisy records as genuine source chains.

## 8. Scope

Closed: a proper full-label height, fixed-moment source algebra bounds, height-preserving Fox and native lifts, transfer of existing balancing bounds, and an operation-compatible finite-packet approximation.

Not claimed: a pure numerical-endpoint height without a label audit, fixed-eta bounds for products of arbitrarily many factor heights, arbitrary new-label operations, or inverse reconstruction from analytical responses. If the common-path source is also required, the same scalar height method can be applied to its established bounds, but both source requirements must still be tracked.

## Verification

`uv run --with sympy python research/nima/checkers/check_convex_source_height.py`

The checker uses actual finite Boolean source vertices, including a deliberately scrambled injective label code, to check convex closure, composable projections, cut heights and terminal-lift endpoint preservation. The infinite theorem follows from countability, local finiteness, convexity and the supplied weighted lifting bounds.
