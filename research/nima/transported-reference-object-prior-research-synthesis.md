# A transported reference object: frames, return transport and retained paths

## What was investigated

The proposed higher object has a reference/relationship decomposition that moves under a triangle half-phase and returns after a complete frame cycle. This note compares it with prior project research and checks the concrete finite conjugation model.

The finite adapter is explicit: embed the triangle short root as u=diag(S,1) on four state coordinates, then let T=Ad_u act on V=sl4(R). This is the conjugation candidate used in the preceding discussion. It is distinct from the five-edge two-triangle serial model, and an equivalence to native packet dynamics has not been constructed.

## Endpoint-gradient bridge added to the existing checker

There is now an explicit restricted justification of u=diag(S,1). For four endpoint potentials x define the actual ABC packet incidence map

    Bx=(x_B-x_A,x_C-x_B,x_A-x_C).

Exact rational checks give

    B u = S B.

Thus the existing triangle coefficient update and four-state update commute on gradient packets. The kernel of B is spanned by the ABC constant vector and the spectator D. Requiring the triangle total and D value to remain unchanged makes the lift unique: stacking B with these two covectors has rank four. This is uniqueness under those explicit preservation requirements, not a derivation of the short-root branch or physical metric.

The full six-arrow seed incidence has rank three and loses only the global potential constant, which u fixes. Consequently u induces a well-defined reversible update on its gradient packet subspace, with six-step return. This closes a state/triangle coefficient interface within that subspace.

The limitation is exact: independent seed arrow values have three additional cycle coordinates (ABC, ADB and AB+BA). All three sums vanish on gradients. The bridge therefore does not represent arbitrary retained path resources or circulation data. A native packet identification must either justify this sector or extend the update to the retained cycle records. The earlier `seed-cycle-retained-pair-trial.md` supplies a coordinate decomposition, not a uniquely selected dynamics on those records. The following extension now tests a specific preservation policy without assigning the earlier arbitrary cycle-permutation dynamics.

The checker extension reruns all original reference-algebra assertions; the153/105/225 dimensions and frame periods remain unchanged.

## Full six-arrow extension with conserved cycle records

Let x=(AB,BC,CA,AD,DB,BA) have six independent real coefficients. Apply S to the first three and write their increments as (a,b,c). Since S preserves their sum, a+b+c=0. Choose endpoint increments

    dA=-(2a+b)/3,
    dB=dA+a,
    dC=dB+b,
    dD=0.

Update EVERY seed arrow by x_(i->j)'=x_(i->j)+dJ-dI. This simultaneously realizes the desired ABC half-phase, preserves the triangle-total endpoint increment dA+dB+dC=0, and fixes the spectator increment. These conditions uniquely determine the endpoint increments. Requiring an exact endpoint increment ensures all cycle sums remain unchanged.

The resulting six-by-six linear update F satisfies

    local_ABC F = S local_ABC,
    cycles F = cycles,
    F incidence = incidence u,
    F^6=I, F^-1=F^5.

The three cycle readings are AB+BC+CA, AD+DB+BA and AB+BA. The checker tests nonzero values (7,56,33), not just the gradient sector where all vanish. Every seed arrow is updated, including arrows in the second triangle. This is NOT a claim that its local triple simultaneously undergoes the same S; that requires the separate seam-compatibility conditions from the shared-triangle model.

Thus there is now a lossless extension to arbitrary scalar seed-arrow data using the same triangle step, with no additional state coordinates and no arbitrary permutation of circulation records. A positive invariant metric can be constructed as sum_(k=0)^5 (F^k)^T F^k; it is positive because its first term is I. Its conservation is checked, but this orbit-averaged metric is a mathematical certificate, not a derived physical energy.

The preservation policy is explicit: cycles fixed, exact endpoint increments, zero triangle-total increment, stationary spectator. The seed alone has not selected this policy over others. In particular six-step operator return does not erase traversal history, determine rung4 physics, produce distinct species, or count primitive execution arrows.

## Precise moving object

Let h be the three-dimensional traceless diagonal space and m the twelve-dimensional off-diagonal space. Let D project onto h, and Gamma=2D-I distinguish the two sectors.

Conjugation fixes the matrix unit I4 exactly. What moves is the choice of diagonal reference algebra, its primitive state projectors, and the resulting distinction between h and m. Thus "identity changes" is most precisely read here as "the reference decomposition is transported".

The transported objects are

    Gamma_1=T Gamma_0 T^-1,
    A_1=T A_0 T^-1,
    A_j={F in End(V): F Gamma_j=Gamma_j F}.

Each A_j is a response algebra of dimension 3²+12²=153.

## Two clocks on the same six-step lift

Exact calculation gives

    Gamma_1 != Gamma_0,
    T Gamma_1 T^-1=Gamma_0,
    T² != I,
    (T²)³=I,
    T⁶=I.

The reference split has period TWO. The transport remaining inside the returned frame has order THREE. The labelled operator has order SIX.

The same cyclic group C6 therefore has two useful projections:

- the half-phase-to-triangle map, with a C2 kernel and C3 cyclic endpoint;
- the frame-orbit map, with a C3 stabilizer and C2 frame endpoint.

For this finite model C6 is isomorphic to C2 x C3. A frame-parity reading and a three-position reading together distinguish its six operator states. Raw retained histories distinguish repeated traversals beyond those six endpoint states.

The two-step frame loop returns with holonomy T²=Ad_diag(C,1): it permutes the reference labels and relationship channels. Recovering the frame split does not by itself recover each labelled record. This return transport is visible to the retained-history window.

The loop uses two successive forward T operations. A passive coordinate change followed by its inverse would instead return by T^-1 T. The schedule specifying the forward cycle is part of this trial.

## The 153-dimensional algebra is a phase-indexed fiber

Three response spaces are now distinguished exactly:

| Response space | Dimension |
|---|---:|
| Preserves one chosen reference split | 153 |
| Preserves both transported splits simultaneously | 105 |
| Algebra generated by both frame response algebras | 225 |

The full End(V) has dimension 15²=225, with 72 mixed blocks relative to either one split. The two 153-dimensional algebras are conjugate; they are not equal. Their common algebra has dimension 105, and allowing products of responses from both frames generates all of End(V).

The last statement follows constructively: A0 contains every within-block matrix unit; Gamma1 has nonzero entries in both mixed directions. Multiplying Gamma1 on the left and right by the A0 matrix units isolates and generates every mixed matrix unit.

Consequently 12*153 describes a transition-indexed response fiber at a specified phase, if the twelve transition channels are adopted as the outer index. The whole phase-changing apparatus also contains the transport between those fibers. An interpretation that permanently suppresses all mixed responses would lose that transport.

These are dimensions of an explicitly declared real coefficient model, not measured particle energies or physical mode counts.

## Relative geometry of the reference sectors

The common diagonal sector of h and T(h) has dimension one. Their other two principal angles have cosine 1/3. Equivalently, with Q and P the triangle common/contrast projectors, the compression of the transported diagonal projector to h is

    Q+(1/9)P.

Their off-diagonal complements share a ten-dimensional space. The remaining four dimensions carry two equal-angle two-projection blocks. This yields another derivation of the common response-algebra dimension:

    1² + 10² + 2² = 105.

The value 1/3 also appears in regular-tetrahedron normal geometry (with sign -1/3 for distinct outward unit normals). The tested equality is a principal-angle calculation for reference subspaces. A spatial identification with tetrahedral normals would require a map between those two constructions.

## Prior research: several views of the same structural issue

### 1. Transported algebra and moving measurements

`cayley-product-transport.md` constructs transported products

    x star_T y = T(T^-1 x * T^-1 y)

and transported readouts, and explains when visible motion is a presentation change. It also explicitly distinguishes a fixed algebra unit from a changing representation/product. This supports reading the present object as a state together with its reference algebra and transport.

Our matrix conjugation is an automorphism of the full matrix algebra, while moving its diagonal subalgebra. The earlier pointwise-product example needed to transport the product itself. These are related mechanisms with different source algebras.

### 2. Polarization and half-angle lifts

`research/grothendieck/paired-polarization-quarter-rotation.md` constructs a canonical coefficient--Betti quarter-turn J with J²=-1 and discusses a chosen positive-path half-rotation. `research/buzzard/polarization-quarter-turn.md` records its algebraic formalization and separates it from the extra path/metaplectic data.

Our 3+12 sector split is not itself that equal-dimensional Lagrangian polarization pair. The relevant connection is the architecture: a paired presentation, an exchange operator, and a path-sensitive lift. The triangle supplies a new finite instance with its own exact 60-degree branch.

### 3. Reference holonomy

`flat-reference-attachment-and-holonomy-gate.md` derives frame-covariant reference attachments and promotion. Its nonflat control shows that a loop response changes only by conjugation under local frame changes. This directly illuminates the present two-step return: the frame split can close while its labelled contents undergo nontrivial return transport.

`witnessed-reference-reanchoring.md` separately constructs reference substitution with immutable parents, exact composition and preserved mixed rectangles. It gives an existing route for changing the comparison standard while preserving the actual maps and their history. It is a different operation from conjugating every state and observable together.

### 4. History and continuation are jointly retained

`research/voevodsky/history-and-possibility-swap-under-coherent-cut-reversal.md` constructs joint history/continuation relations, transports cuts, and proves that reversal exchanges the two projections. Its counterexample shows that retaining separate marginals permits combinations absent from the original source.

This suggests a stronger role for the history window: it can determine which next arrows are compatible with a given retained identity. It can function as an admissibility interface, as well as provenance storage. Implementing that role requires an admitted continuation relation. The Cartesian E x E and S x S counts correspond to a full independent comparison domain; a constrained continuation relation can have a smaller admissible domain.

### 5. Two composition directions and the arity square

`binary-arity-square-is-the-duoidal-skeleton.md` identifies the four roles (1,1), (1,*), (*,*), (*,1) with a Gray cycle. It distinguishes horizontal composition of histories, vertical expansion/coaction, and their interchange cell. Its strict result has a specified transverse source domain.

This provides a higher-categorical way to organize the proposal: ordinary packet composition and reference/presentation transport are separate directions, with compatibility comparisons between their orders. The retained object includes those comparisons rather than only the endpoint graph. The current finite matrix trial does not itself supply the full duoidal source structure.

### 6. A returning chart and a growing source

`research/voevodsky/the-joint-source-graph-makes-the-chamber-twistor-tower-analytically-equivariant.md` supplies four source-retaining analytic charts and their transported successors. `prior-source-tower-identifies-chart-rotation-and-cycle-count-through-an-explicit-successor-schedule.md` constructs a full-turn wrap after supplying a successor schedule.

These distinguish phase return from source advancement. They also provide twelve directed chart-comparison maps on four presentations. Identifying those chart maps with the twelve state-transition channels of the present counting model remains a separate adapter.

The related formal helix in `research/voevodsky/a-clean-universal-category-for-the-eight-lattice-four-chart-suspension-system.md` explicitly retains a turn counter. It exemplifies how a return at the presentation level can coexist with a new source index, once a successor has been specified.

## A compact description of the higher object

At the finite endpoint level, this is a family of reference algebras over a two-phase orbit, equipped with transport and nontrivial return automorphism. The C6 action on the two frames gives a transitive action groupoid with C3 isotropy. The retained-history version also remembers the path and occurrence IDs mapping to each such endpoint action.

A useful package is

    (active packet presentation,
     reference algebra at the current phase,
     transport to the next phase,
     retained path and its allowed continuations).

A particle interpretation would have to be a physical realization of such a package. The present source comparison and exact calculations establish a structural object with several previously developed pieces; they do not select that realization.

## Fresh verification and research boundary

    python research/nima/checkers/check_transported_reference_algebra.py

Fresh exact rational checks establish the fixed matrix unit, two-frame period, order-three within-frame return, six-step labelled return, principal-angle compression and response dimensions 153, 105 and 225. The prior research above was read for this synthesis; its Agda/Lean/analytic results were not recompiled or independently reproved here.

Artifact: `results/transported-reference-algebra.json`.
