# Joint records type as attachment parameters, not cofiber objects

## Outcome of the bounded comparison

The smallest interval comparison can be specified without fitting dimensions:

1. In the existing typed analytical path-algebra refinement, full joint event records are projective **mapping-space coefficients**.
2. A canonical coevaluation turns every such coefficient into the second attachment of a two-step filtration.
3. The three associated cofibers have an explicit source-generated comparison and contracting homotopy, compatible with conjugate duality.
4. Typed-unit evaluation recovers the prescribed joint pairing. An unqualified signed Hilbert–Schmidt pairing on the entire projective input instead counts extra prefixes and does not give that form.

This identifies a concrete attachment parameter. It does not identify the record vector with the cofiber object of that attachment.

The newly supplied Grothendieck note `../grothendieck/joint-cut-carriers-as-pointed-multi-input-derived-images.md` gives a complementary, direct construction using external projectives over the original marked source algebra. It supplies the prescribed cut carriers as receiver images and their columns by prepared-vacuum evaluation. That result removes the need to search for an unspecified source object for those carriers. The calculation here concerns the additional typed analytical refinement and an explicit interval attachment in it; the two source categories are not silently identified.

## 1. The correct mapping type

Use the finite typed analytical path algebra A from `three-prime-cut-duality-locates-the-ghosts-in-the-marginal-cofiber.md`. At an elementary arrow e its coefficient space is

`K_e=C Omega_e direct-sum W_e`.

Omega_e is an event slot of retained degree zero, not a vertex identity. Let P_x=A e_x be the vertex projective. In the chronological convention,

`RHom_A(P_x,P_y)=e_x A e_y`

is concentrated in cohomological degree zero. The equality identifies a path coefficient with right multiplication on P_x. Composition agrees with concatenation in A.

For the two-prime diamond,

`e_2 A e_12 = direct_sum_(m=4,6) K_(2,m) tensor K_(m,12)`.

For the three-prime cube, e_2 A e_60 is the analogous sum over full intermediate vertex chains of three elementary factors. These are exactly the finest typed joint record spaces.

This composition is lossless because A retains the free typed paths. It must not be confused with composition in the terminal Fock recorder, which removes vacuum slots and internal labels. The latter is the further observation that loses the marginal ghosts.

## 2. A canonical universal middle object

For the diamond put

`U_m=Hom_A(P_2,P_m)`, `V_m=Hom_A(P_m,P_12)`,

`Z=direct_sum_(m=4,6) U_m^* tensor_C P_m`.

Here U_m^* is the ordinary finite-dimensional linear coefficient dual. It is not a physical inverse or a claim that record polarity is operator adjoint.

There is a basis-independent coevaluation map u:P_2->Z. In a basis (u_i) of U_m it is the sum of u_i^* tensor u_i over m and i. An arbitrary joint coefficient

`h in direct_sum_m U_m tensor V_m`

gives a map v_h:Z->P_12 by evaluation of U_m^* against its first factor. Then

`v_h u = h`,

where the right side means the corresponding projective map P_2->P_12.

Moreover,

`Hom_A(Z,P_12) = direct_sum_m U_m tensor V_m`.

Thus this construction does not require h to be one decomposable tensor, or to factor through one selected middle vertex. The vertex summands remain present in Z.

Readout is explicit: restrict v_h to each coefficient-dual copy of P_m and evaluate it at the typed unit e_m. Right multiplication sends e_m to precisely its suffix-path coefficient. This recovers h without tracing over every possible incoming path.

The same construction applies at a chosen cut in the three-prime packet, retaining the full internal path data inside each block. It is a lossless regrouping in A, not the compressed single-cut Fock observation.

## 3. The smallest complete interval attachment

Use the filtration

`0 -> P_2 --u--> Z --v_h--> P_12`.

Its interval quotients include Cone(u), Cone(v_h u), and Cone(v_h). There are canonical chain maps

`i:Cone(u)->Cone(v_h u), i=(id,v_h)`,

`p:Cone(v_h u)->Cone(v_h), p=(u,id)`.

Their composite is (u,v_h), not the zero chain map. The specified nullhomotopy is the identity Z->Z between the relevant adjacent degrees. Forgetting this homotopy would lose actual attachment data.

Writing v=v_h, the cone of i is the three-term complex

`P_2 --(id,-u)--> P_2 direct-sum Z --(v u,v)--> P_12`

in degrees -2,-1,0. It retracts onto Cone(v) through

- projection in degree -1: (u,id):P_2 direct-sum Z->Z;
- section: z->(0,z);
- identity in degree zero;
- contracting homotopy (x,z)->x into degree -2.

The identities are exact:

`projection section=id`,

`id-section projection=dH+Hd`.

This supplies the cofiber comparison and its attachment homotopy from the actual u and v, not from an independently chosen isomorphism between quotient dimensions.

## 4. Duality check

Conjugate cochain duality reverses this three-term complex. Its two differentials have signs

`-d_1^vee`, `+d_0^vee`.

Under the declared nondegenerate pairing identifications these become the corresponding signed mates. The checker verifies the reversed deformation retract and its homotopy, including these signs. It also verifies (v u)^sharp=u^sharp v^sharp.

This is a finite analytical chain-complex realization of the attachment. Grothendieck's derived-extension theorem supplies its extension from generators to perfect complexes. It does not make the underlying vector conjugate dual identical to algebraic projective duality without the intervening receiver. For example, A e_x and the opposite-module dual e_x A need not even have the same underlying complex dimension.

No claim is made here that these chain calculations constitute an Agda implementation of `ClosureTreeBoundarySemantics`. They supply the concrete attachment and homotopy data that such a comparison must carry.

## 5. Pairing audit: typed units versus an all-input trace

The joint form is the prescribed direct sum of tensor forms q_(U_m) tensor q_(V_m). Its realization on Hom_A(Z,P_12) is obtained by the typed-unit readout above. This is a specific source-derived observation, not a generic metric on all linear maps between the underlying vector spaces.

To test a tempting alternative, give each projective its direct-sum path pairing, and U_m^* its dual coefficient pairing. The signed Hilbert–Schmidt formula on attachment maps is

`q_HS(V,H)=trace(Q_Z^(-1) V* Q_(P_12) H)`.

A suffix right-multiplication map acts on every incoming basis path of P_m. The trace therefore repeats its suffix pairing once for each such prefix. On the m block it gives

`q_HS = dim_C(P_m) times q_joint`.

In the two-sheet diamond fixture dim(P_4)=dim(P_6)=4, and exact calculation gives q_HS=4 q_joint, not q_joint. This is not repaired by silently rescaling the prescribed Clark form. Evaluating at the typed unit selects the intended suffix coefficient and has no overcount.

The all-input projective pairing is an explicitly tested candidate, not an assertion that it was the already prescribed physical Green pairing. The audit explains why an arbitrary trace metric cannot substitute for the specified pointed readout.

## 6. The three-prime ghosts locate the actual quotient

The checker constructs the two known alternating braid ghosts in the refined path algebra. For both:

- the joint coefficient h is nonzero;
- the attachment v_h is nonzero;
- typed-unit readout recovers h;
- even the composite v_h u remains the nonzero typed projective map h;
- terminal feature composition erases the internal event slots and vertices and gives zero.

Thus, in this model, the loss is not caused by projective composition itself. It occurs when passing to the terminal recorder. This sharpens the phrase "rejoining loses information": lossless typed regrouping and compressed terminal rejoining are different operations.

## 7. Relation to the pointed multi-input theorem

Grothendieck's external receiver works over tensor products of the original marked source algebra and identifies the prescribed joint carrier as an actual receiver image. Its path columns arise by evaluating external path maps on independently prepared segment vacua. Our typed-unit readout in the refined algebra plays a related pointing role but is not automatically the same functor or the same source object.

Both results reject two shortcuts:

- a joint tensor record is not automatically a cofiber quotient;
- rejoining does not automatically intertwine independent creation actions on arbitrary memories.

The external theorem gives the concrete all-state hostile:

`mu(c_R(a) Omega tensor b)=a tensor b`,

`c_R(a) mu(Omega tensor b)=b tensor a`.

The present attachment construction does not bypass that noncommutativity. If all-state derived coarsening is required, its source must be a typed composition correspondence or a suitable bimodule/enriched-arrow construction, not restriction along a supposed algebra map S tensor S->S.

## 8. Verification

`uv run --with sympy python research/nima/checkers/check_joint_record_interval_attachment.py`

Passed exact checks:

- diamond path algebra dimension 34, joint Hom dimension 18;
- three-prime path algebra dimension 314, joint Hom dimension 162;
- coevaluation, attachment, and typed-unit readout on every joint basis element;
- explicit cofiber deformation retract and nonzero composite nullhomotopy;
- dual deformation retract and cochain signs;
- the factor-four trace hostile;
- retention and subsequent terminal annihilation of both braid ghosts.

Certificate: `results/joint-record-interval-attachment.json`.

These dimensions use a two-sheet signed-coordinate fixture. They are not dimensions of the actual seven-chamber spectral feature image. The general mapping identifications and attachment construction hold for the prescribed finite W by the displayed algebraic arguments. No numerical spectral sampling or positivity conclusion is used.

## 9. Numerical evaluator convention gate

The supplied `../voevodsky/checkers/check_clark_feature_evaluator.py` prompted an independent read-only audit of its adapter. The implementation loops over sigma before moment order and returns

`(+,0),(+,1),(-,0),(-,1)`,

while the docstring and fixed Clark matrix use

`(+,0),(-,0),(+,1),(-,1)`.

The smoke test also passes twice the prescribed C_Clark, omitting its factor 1/2. Passing C as an argument is legitimate for a generic bilinear evaluator, but this fixture consequently does not test the frozen Clark normalization.

`uv run python research/nima/checkers/check_clark_evaluator_conventions.py`

compares the exp(-x) test forcing against closed-form interval moments. It detects both issues. With 4096 midpoint cells, reordering components and using C_Clark gives a kernel error about 3.44e-11; the current smoke-test convention differs by about 0.0472. This is a numerical regression, not an interval certificate. The upstream files were not modified.

Certificate: `results/clark-evaluator-conventions.json`.

Before using that adapter as evidence for the source comparison, repair its output convention and add a value-based normalized-kernel test. A finiteness assertion alone cannot check the sewing convention.
