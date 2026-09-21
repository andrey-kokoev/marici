# The seam attachment needs source action and lifts to the typed refinement

## Result

The conormal and product-layer seam images cannot by themselves realize the original ordinary source extension inside the terminal quotient category while keeping C in degree zero. This does not exclude derived base change: Nima's subsequent computation gives B tensor_S^L C=C direct_sum P[1], with a nonzero connecting projection. Its shift-correct joint-seam comparison is constructed in `the-derived-connecting-projection-has-a-shifted-joint-seam-realization.md`.

The obstruction to the unchanged ordinary extension is the actual multiplication

(I/I^2) tensor_B (I/I^2) -> I^2.

It is nonzero, whereas every terminal-quotient-linear extension kills this action. This gives an exact descent criterion, rather than another rank obstruction.

There is nevertheless a faithful stable lift to Nima's already admitted typed analytical path algebra. Its generator refinement has an explicit source-fixed coefficient retraction, so extension of scalars preserves the nonzero attachment class. The retained product layer is still 24-dimensional at the terminal corner.

This constructs a carrier for the nonsplit attachment before terminal seam observation. It does not reinterpret a direct sum of terminal seam homology groups as that carrier.

## 1. The source extension and its seam images

Use S for the free marked source algebra, I for the terminal record kernel, B=S/I, C=I/I^2 and P=I^2. At the four-event cutoff I^3=0.

The source attachment is

0 -> P -> I -> C -> 0,

with nonzero class delta in Ext^1_S(C,P), using right modules. The analogous left and bimodule statements hold as established previously.

The path derivative realizes C in single-seam homology, and labelled pairs of local seam derivatives realize P in joint two-seam homology. The endpointwise comparison must retain the full family of source action maps to discuss delta: the root-to-terminal vector spaces alone have no nontrivial vector-space Ext^1.

On C and P, the source ideal I acts by zero. On the ambient terminal-memory seam terms it also acts by zero through the external memory actions. These actions factor through the terminal quotient B. In contrast, I acting on the middle object I is not zero: its image contains I^2.

## 2. An exact criterion for descent of an extension

Consider any right S-module extension

0 -> P -> E -> C -> 0

where P I=0 and C I=0. For c in C, choose a lift e in E and let a lie in I. Then e a lies in P. Its value is independent of the lift, because P I=0; it depends on a only modulo I^2, because E I^2=0. Thus the extension has a canonical action-defect map

omega_E:C tensor_B (I/I^2) -> P,

omega_E(c tensor [a])=e a.

The extension descends to an extension of B-modules if and only if omega_E=0. Indeed, vanishing is exactly the condition E I=0, which is exactly the condition for the S action on E to factor through B.

For the source extension E=I, omega_I is the prescribed multiplication

C tensor_B C -> P.

In the four-prime packet it is the isomorphism onto the 24-dimensional product layer proved in the preceding note. Hence delta does not lie in the image of

Ext^1_B(C,P) -> Ext^1_S(C,P).

This is stronger than saying that a particular splitting fails. No terminal-quotient-linear middle object can realize this source extension at all.

## 3. Consequence for an attempted seam-only attachment

Transporting delta along the isomorphisms onto the two seam images defines an S-derived extension class between those images. That formal transport is valid, but does not make it a morphism internal to the B-linear receiver category.

A cone formed entirely from B-linear complexes has cohomology annihilated by I. It therefore cannot recover the middle source module I, whose ideal action has nonzero image P. Equivalently, the transported class is not supplied by a B-derived morphism whose forgetting gives delta.

A source-linear map from I to any strictly I-annihilated module must kill I^2: f(a b)=f(a)b=0. This includes an unconnected direct sum of the two terminal seam images. Keeping their dimensions without the cross-layer source action is insufficient.

The required additional datum is not a new scalar metric. It is the action-defect map above, or equivalently the S-derived attaching morphism retaining that action.

## 4. A faithful carrier already exists in the typed refinement

Let A=T_(B0)(K) be Nima's free typed analytical path algebra, where B0 is the vertex-idempotent algebra and

K_e=C Omega_e direct_sum W_e.

Here B0 is distinct from the terminal quotient B. The marked source generator inclusion is

j_e(e^0)=Omega_e, j_e(e^1)=g_e.

The feature g_e is nonzero by the admitted source-feature injectivity. On the fixed positive Hilbert carrier define

ell_e(w)=<g_e,w>/||g_e||^2.

This is complex linear in w under the convention conjugate-linear in the first argument. Define the endpoint-preserving coefficient retraction

r_e(z Omega_e+w)=z e^0+ell_e(w)e^1.

Then r_e j_e=id. Free path composition extends these maps to algebra maps

j:S->A, r:A->S, r j=id_S.

The retraction uses the existing positive Hilbert structure only to extract the coefficient along the already prescribed g_e. It neither changes the signed Green form nor asserts an isometry. In particular it is not the terminal recorder: Omega_e remains an actual event arrow under r.

The inclusion j and the stable lift below do not depend on selecting a retraction. The displayed retraction certifies their split faithfulness using fixed source data.

## 5. Exact and faithful stable lift

For right modules define

F:Perf(S)->Perf(A), F(M)=M tensor_S^L A,

G:Perf(A)->Perf(S), G(N)=N tensor_A^L S,

with actions induced by j and r. Associativity of derived tensor and r j=id give

G F equivalent to id.

Therefore F preserves the nonzero class delta: if F(delta) were zero, applying G would make delta zero.

There is also ordinary flatness here, not merely derived exactness. The local coefficient retraction splits K into the two marked directions plus a complementary space U. Every word in A either belongs to S or has a unique first U-letter. Thus, as a left S-module,

A is isomorphic to S direct_sum (S tensor_(B0) U tensor_(B0) A).

Because B0 is semisimple, the second term is a sum of vertex projectives. Hence A is left S-projective and flat. The last-U-letter argument gives the corresponding right projectivity. This argument uses the free refinement; a split algebra map alone would not imply flatness.

Consequently the source short exact sequence lifts to an ordinary short exact sequence

0 -> P tensor_S A -> I tensor_S A -> C tensor_S A -> 0.

The middle term identifies with the actual right ideal j(I)A inside A, since flat base change preserves the injection I->S. The product term remains P: it is supported at the terminal vertex, and that vertex has no outgoing nonidentity paths in A.

Thus the same 24-dimensional product layer is attached nontrivially to the refined conormal receiver. The original source extension is recovered by G. No arbitrary vector-space splitting has been selected.

## 6. What the refinement retains that terminal seams do not

In A, composing j(a) with j(b) is the nonzero typed coefficient j(a b), including its internal event slots and source labels. A relation for the terminal recorder is not a zero arrow of the refined source.

This is exactly the distinction in Nima's attachment-parameter construction: records are projective mapping coefficients before terminal observation. Passing to the memory algebra makes their terminal relation vanish. The stable refinement preserves the attachment precisely because it does not make that quotient first.

The lifted triangle

F(P) -> F(I) -> F(C) -> F(P)[1]

is the promised faithful carrier of delta. Its full maps remain source-generated. It can be represented by the lifted projective complex and the same connecting-map formula as before.

The single-seam and joint-seam observations remain valid projections of the two associated layers. They do not become an equivalent replacement of the entire lifted triangle. Constructing any further analytical comparison must specify how it retains or intentionally forgets the nonzero action-defect map.

## 7. Relation to the existing Green and opposite constructions

The retraction r is a positive-Hilbert coefficient decoder. The Green mate uses the signed signature, while opposite prefix action and module duality have their own variance. None of those three operations is identified with r.

The faithful lift is a theorem about the typed analytical path algebra and its perfect modules. It does not prove that subsequent evaluation in a terminal Hilbert memory is faithful, or that the relation ideal has a prescribed nondegenerate pullback form.

Opposite source refinement gives the analogous left-module lift, and duality transports the triangle with the previously established cochain signs. No inverse arithmetic event is introduced.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_seam_attachment_source_lift.py`

Exact checks pass for all 32 generator retractions and all 1,040 typed marked histories. The checker also verifies the local nonzero action defect and the fact that intertwiners to an I-annihilated target kill the product direction.

The general extension-descent criterion, flatness argument, and split exact stable lift are proved above. They are not an Agda implementation of the derived categories. The finite fixture uses independent chamber coordinates; the analytical retraction uses the actual nonzero g_e and its existing positive Hilbert norm.

References:

- `the-relation-to-seam-map-detects-conormal-classes-and-kills-products.md`;
- `the-four-prime-relation-layer-has-a-forced-nonsplit-attachment.md`;
- `research/nima/joint-records-type-as-attachment-parameters-not-cofiber-objects.md`.
