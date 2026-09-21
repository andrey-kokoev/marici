# Three-prime cut duality locates the ghosts in the marginal cofiber

## Result

The sheet-reduced three-prime joint-cut receiver now has an explicit compatible diagram of nondegenerate signed pairings, unique contragredients, and dual cone/fiber comparisons.

The two marginal ghosts have a stronger interpretation than rank loss: they give independent classes in degree -1 of the marginal-compression cone, detected by independent dual classes in degree 1 of its dual fiber. Their dual observers cannot be assembled from the two separate marginal mate images.

There is also a finite typed analytical path-algebra refinement with a source-derived algebra retraction. It retains event slots before terminal composition. Its exact stable extension is split faithful; the later terminal recorder is not. These are different functors.

This note uses, rather than reproves, Grothendieck's generator-to-derived extension theorem. The new work is the concrete joint-cut application, its cohomological negative controls, and the explicit typed analytical refinement.

## 1. Inputs and carriers

Inputs:

- `../voevodsky/the-three-prime-clark-cut-diagram-needs-joint-attachments.md`;
- `../voevodsky/the-marked-clark-diamond-has-a-nondegenerate-dual-pair-after-sheet-reduction.md`;
- `../grothendieck/typed-event-cut-reconstruction-and-the-joint-observation-criterion.md`;
- `../grothendieck/generator-to-derived-extension-with-the-clark-dual-receiver.md`.

Fix the three-prime source from 2 to 60, its seven chamber intervals, the prepared forcing, and the open spectral disk. Let

`W0=Lhat(V)`, `W=W0+J W0`.

The inherited Hilbert space W is finite-dimensional and J-invariant; J is a self-adjoint involution. No new metric is fitted. For a segment with event capacity c use

`F_c(W)=direct_sum_(r=0)^c W^(tensor r)`

with Hilbert weights tau^(2r) and signature direct_sum J^(tensor r).

For a cut set S subset {1,2}, let Y_S be the direct sum, over its admitted vertex tuples, of the tensor products of these segment spaces. Their capacities are (3), (1,2), (2,1), and (1,1,1). Denote their signatures by J_S and their pairings by q_S. Every J_S is an invertible self-adjoint involution in the weighted Hilbert metric.

The prepared source line may be retained as in the input pilot. Trivializing it by the actual unitary reassembly maps leaves the record formulas below unchanged. This does not duplicate an arbitrary unknown physical state into multiple source factors.

## 2. Rejoining, mates, and the pairing square

For T subset S, let A_(T<-S):Y_S->Y_T concatenate across deleted cuts and forget those vertex labels, summing colliding coordinates. These are the existing record maps, not a new projection chosen to repair a metric residual.

Each map is bounded: on a fixed degree allocation and label branch it is tensor reassociation, and only finitely many allocations and branches occur. The weights agree because total retained degree is unchanged.

With beta_S(y)(x)=q_S(x,y), define the unique Green mate by

`beta_S A^sharp = A^vee beta_T`.

It is the sum over all allowed degree splittings and restored vertex-label preimages. It need not be an inverse. In the signed coordinate fixture the signature weights of an input basis word and its concatenation coincide, so the mate is the ordinary transpose of the real rejoining matrix.

The resulting equations are

`A_(U<-T) A_(T<-S)=A_(U<-S)`,

`A_(T<-S)^sharp A_(U<-T)^sharp=A_(U<-S)^sharp`.

Lossless changes of parentheses use the canonical tensor associators and preserve these pairings. They must not be conflated with the lossy maps deleting cuts or labels.

## 3. Naturality on cones, not only isolated generators

Take any commuting cut square

`X --A--> Y`, `X' --B--> Y'`,

with vertical maps U:X->X' and V:Y->Y', satisfying B U=V A.

It induces the chain map (U,V) between Cone(A) and Cone(B), in cohomological degrees -1 and 0. Conjugate duality has differential -A^vee in degrees 0 and 1. Under beta, this becomes -A^sharp. The reflected chain map is (V^sharp,U^sharp), since

`U^sharp (-B^sharp)=(-A^sharp) V^sharp`.

The beta squares commute degree by degree. Thus the same supplied pairing comparison extends over the square; no cone-level pairing is independently selected.

The exact fixture verifies all 36 commuting arrow squares in the four-object cut poset, including identities, and all 16 composable triples. It checks the cone/fiber sign for all nine arrows and for an independent complex recording generator. A hostile check rejects the positive sign in place of -A^sharp.

By the generator-to-derived theorem, the finite cut-category representation extends to perfect modules over its category algebra with this natural duality square. Its commutative-square relations have now been checked explicitly. This statement does not identify a cut-compression cone with a source-arrow cofiber merely because both are called cofibers.

## 4. The ghosts become cohomology and dual-observation classes

Let R:H_48->Y_{1,2} be the faithful joint-cut observation of the 48 marked paths. Let

`M=(A_({1}<-{1,2}), A_({2}<-{1,2}))`

map into Y_{1} direct_sum Y_{2}. Its mate is

`M^sharp(eta_1,eta_2)=A_({1}<-{1,2})^sharp eta_1
                       +A_({2}<-{1,2})^sharp eta_2`.

Use the route order and alternating signs of the three-prime packet:

`epsilon=(-1,+1,+1,-1,-1,+1)`,

`g0=sum_r epsilon_r [r;000]`,

`g1=sum_r epsilon_r ([r;001]+[r;010]+[r;100])`.

Set x_i=R(g_i). Faithfulness gives independent nonzero x_0,x_1. Both lie in ker M. Since Cone(M) has only degrees -1 and 0, they represent independent classes in

`H^(-1)(Cone M)=ker M`.

This is a two-dimensional source-generated subspace of that kernel. The full ambient kernel can be larger; no claim that the whole cohomology has dimension two is made.

Now take the prescribed dual observations

`eta_i=J_{1,2} x_i`.

Then

`q_{1,2}(x_i,eta_i)=||x_i||_Hilbert^2>0`.

For every marginal observer z,

`q_{1,2}(x_i,M^sharp z)=q_marginal(M x_i,z)=0`.

Therefore eta_i is not in image M^sharp. It gives a nonzero class in

`H^1(Fib M^sharp)=coker M^sharp`.

The two cross-pairings vanish because x_0 and x_1 have distinct retained degrees. The resulting two-by-two pairing on these chosen classes is diagonal with strictly positive entries, proving independence on both sides.

The pairing descends from ker M times Y_{1,2} to ker M times coker M^sharp by the displayed annihilation identity. This is exactly where the missing joint observations live in the cone/fiber comparison.

The positive quantities here are Hilbert norms obtained by pairing a vector with its **different signed-dual observation** Jx. They do not imply positivity of q(x,x), a positive Clark kernel, or a terminal invariant metric.

## 5. A split typed analytical refinement before compression

The local dual observations also give an explicit faithful algebra stage, not merely a vector-space storage trick.

Let B be the vertex-idempotent algebra of the finite three-prime cube. For each elementary unmarked arrow e:x->y, put

`K_e=C Omega_e direct-sum W_e`,

where W_e is a copy of the prescribed W. Define the local marked embedding

`j_e(e^0)=Omega_e`, `j_e(e^1)=g_e=Lhat(v_e)`.

Both images belong to **event length one**. Omega_e has retained-record degree zero, but is not a vertex identity. Since g_e is nonzero and lies in the other summand, j_e is injective.

The prescribed dual feature gives the linear extraction

`a_e(z Omega_e+w)=z e^0 + [<g_e,w>/||g_e||^2] e^1`.

Its numerator is equally q(J g_e,w). Thus the covector is already available in the source-generated dual envelope, even if q(g_e,g_e)=0. It is not a fitted scalar probe. Directly, a_e j_e=id.

Let S be the marked source path algebra and form

`A=T_B(direct_sum_e K_e)`.

The graph is acyclic and has maximum path length three, so this tensor path algebra is finite-dimensional. Local maps extend multiplicatively to unital algebra maps

`j:S->A`, `a:A->S`, with `a j=id_S`.

Noncomposable products are zero, and every vertex idempotent is preserved. Full event-cut blocks are precisely the vertex-chain tensor summands of A. This is the joint-slot carrier, not the coefficient-only tensor algebra that erases forgotten events.

Consequently derived extension and extraction give

`Perf(S) --A tensor_S^L - --> Perf(A) --S tensor_A^L - --> Perf(S)`

with composite naturally equivalent to the identity. This is the same split-base-change argument as the earlier decorated construction, now with the explicit analytical feature blocks and dual-observation extraction. No flatness is assumed.

This exact stable refinement is split faithful, not generally fully faithful. The algebra extraction a is also **not** asserted to be the Green mate of j: a is a retraction supplied by the dual observer Jg, whereas a mate would require its own specified source pairing.

### Where the terminal receiver fits

On the fixed degree-three memory carrier, a local vector z Omega_e+w acts by

`T_e tensor (z I+c_R(w))`.

This defines a right A-module in the chronological convention. Restricting along j recovers exactly the earlier marked maps T_e tensor I and T_e tensor c_R(g_e).

By Grothendieck's theorem this terminal representation has its exact perfect-module extension and its separately typed dual contraction receiver. Associativity of derived tensor identifies its composite with the faithful refinement with the original marked receiver extension.

But the terminal representation loses information. The ghosts above are already killed by its terminal records; for the all-forgotten cycle the composite operator itself is the alternating sum of the same seam transport and vanishes. Faithfulness of the preceding stable refinement is not inherited by this further functor.

This separates three stages:

`marked source -> split faithful typed analytical paths -> terminal operator observation`.

The cut diagram describes specified compressions of the middle stage. It does not claim that every joint tensor record is already the image of a particular interval quotient under the last functor.

## 6. Opposite polarity and contraction remain distinct

The opposite cut carrier must have its own vertex tuples. A cut at position j reflects to position 3-j while retaining the arithmetic vertex; the first-cut vertices 4,6,10 do not become the forward second-cut vertices 12,20,30 by relabelling the position alone.

The checker builds these opposite coordinate lists independently from the reversed routes. Slot reversal, conjugation, and sheet swap intertwine every rejoining map and mate, with -J on the lower one-letter carrier. Total degree r therefore contributes the required orientation factor (-1)^r.

This transports the cone/fiber comparisons between orientations. It does not turn creation-based opposite-history polarity into contraction-based contragredience. The derived theorem uses the conjugate opposite algebra and the dual observation carrier. Its retracts must likewise keep the paired dual image rather than assume a nondegenerate restriction on the primal image alone.

## 7. Exact verification and its analytical boundary

Command:

`uv run --with sympy python research/nima/checkers/check_three_prime_reduced_cut_duality.py`

Artifacts:

- `checkers/check_three_prime_reduced_cut_duality.py`;
- `results/three-prime-reduced-cut-duality.json`.

The two-sheet fixture has cut dimensions 15,63,63,162, including all admitted vertex-label summands. It verifies:

- nondegenerate weighted signed forms;
- nine pairing and dual-cone squares;
- 36 commuting-square/fiber-chain comparisons and 16 compositions;
- independently indexed opposite rejoining and mate naturality;
- a full-cut left inverse on all 48 complete marked paths;
- source-generated local retractions for all 12 elementary cube arrows;
- the tensor retraction on all 38 typed source paths, accounting for all 128 marked paths, including identities;
- both ghosts and their detecting dual classes, including the stacked marginal cone;
- complex creation/contraction and the wrong-cone-sign hostile.

In this fixture the typed analytical path algebra has dimension 314. The dual witness pairings are 6 and 2759/2. These are fixture values, not numerical values of the completed theta/Clark source.

A two-dimensional sheet fiber cannot inject the seven-dimensional chamber source at a single spectral point. The actual analytical construction uses the full spectral feature space W. Its faithfulness is supplied by the preceding analytic uniqueness argument and the endpoint-block reconstruction theorem. The fixture needs only nonzero local event features, not global chamber independence, to verify the full typed-cut left inverse.

The perfect-module results are mathematical applications of the existing derived-extension and split-base-change theorems, not conclusions of the finite matrix tests. No Agda verification of the new derived construction is claimed.

## 8. Next comparison

The finite joint-cut diagram now supports the requested signed duality and cone/fiber compatibility. The abstract generator-to-derived extension is no longer an open gate for this finite prepared model.

The remaining attachment question should be stated explicitly: which interval-closure object and which comparison map are intended to realize a given joint tensor cut record? One must either construct that map with its complete attachment data, or retain the joint-cut observation as a separate indexed realization. Exactness alone does not identify these objects.

No positivity, terminal isometry, physical event access, infinite-dimensional topological derived extension, or spatial reciprocal identification has been inferred.
