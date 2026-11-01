# Period returns: what local coherence determines and what it leaves open

Date: 2026-10-28.

## Result and scope

The supplied native window specification determines an exact translation lattice and complete labelled-wire regroupings. It explicitly introduces no comparison-packet constructor. The previous packet calculus proved coherent reordering for lossless common-record presentations, but that was a theorem about sets and maps, not a geometric filler-admission rule.

This continuation answers a narrower question: can the recorded period formula, together with reversibility and all-dimensional categorical coherence, select whether a return has a filling comparison?

It cannot, within the explicitly defined period-count diagnostic below. We classify all additive comparison quotients that preserve the full integer displacement. They differ by one subgroup of an integer return register. All have coherent groupoid nerves. The classification does not show that these alternatives are admitted by the native Su-32 calculus.

A constructive result accompanies this separation. Once actual return comparisons are supplied, their consequences can be computed, rather than selecting a new relation for each composite boundary. For the uniform reversible one-return fragment, the generated comparison relation is determined by a greatest common divisor. This is a local-to-global mechanism for comparison existence, not a theorem that arbitrary higher comparison witnesses are unique or coherent.

No native release records, typed port routes, or native comparison producers were executed. No source repository was changed and no Agda or Lean compilation was performed.

## 1. Source facts kept fixed

The uploaded `su32-native-window-operation-v1.md` gives

    g_i = (1,1,1,1) - 4 e_i,       sum_i g_i = 0.

The first three generators form a basis for the period lattice. Lifted ports have identities `(p,a)`, where `p` is the whole base-port record and `a` is an integer triple. Actual wire edges update `a` by their supplied translations. Translation of every integer index by the same triple is a graph automorphism of this algebraically specified global family: it commutes with every update and keeps the base-port record fixed. This is not a claim that a chosen translation is a primitive path of native wire edges.

The note also gives an invertible presentation change on 420 complete wire values. It retains the boundary slots and explicitly disclaims numerical mixing, comparison-packet construction, and history deletion.

These facts do not identify the four period generators with four polarity flips. Nor do they identify a 4-packet point with a five-vertex 4-simplex. Those distinctions remain in force.

## 2. A coordinate decomposition of formal period counts

Let c=(c0,c1,c2,c3) be an integer expression in the four named period generators. These are formal signed counts. They forget word order and are not a complete representation of native retained histories. Any raw word or derivation must be retained separately.

Since g3=-g0-g1-g2, the displacement in the first-three-generator basis is

    D(c) = (c0-c3, c1-c3, c2-c3).

The four-coordinate physical displacement is

    G(c) = (sum_i c_i)(1,1,1,1) - 4c = L(D(c)).

Let delta=(1,1,1,1). Then

    ker D = Z delta.

More strongly, the map

    c -> (D(c), k=c3)

is an integral isomorphism Z^4 -> Z^3 x Z, with inverse

    (a0,a1,a2,k) -> (a0+k,a1+k,a2+k,k).

Therefore every fixed displacement a has a whole affine integer family of count presentations. Increasing k by one adds one use of every named generator and changes no displacement.

This is a statement about decomposition/provenance of translations, not an additional physical degree of freedom. The choice k=c3 uses the selected fourth generator; a different choice gives a different splitting. For two count records with the same displacement, their difference is uniquely n delta, so the relative integer n is independent of that splitting.

The four-letter formal word 0,1,2,3 and the empty word are distinct raw histories even though their count displacement is the same. The source has not supplied a native primitive route for this formal word.

## 3. All additive count comparisons preserving displacement

Specify the diagnostic class before drawing conclusions. We consider congruences on the abelian count group Z^4 that:

- preserve D;
- are stable under adding the same count context;
- have reversible comparisons and composition.

Such congruences are exactly quotients by subgroups N of ker D. This follows directly by setting N={c: c is compared to 0}; group compatibility makes N a subgroup, and c is compared to c' precisely when c-c' is in N.

Every subgroup of the infinite cyclic group ker D is

    N_d = d Z delta,       d >= 0.

Here d=0 denotes the zero subgroup, not the whole kernel. The resulting group is

    C_d = Z^4 / N_d = Z^3 x K_d,

where K_0=Z, K_1=0, and K_d=Z/dZ for d>1. The displayed isomorphism uses the coordinate splitting from Section 2.

Thus the same observed displacement is compatible with three qualitatively different policies:

- d=0: every integer return remains distinct in count-level comparison classes;
- d=1: one complete return is compared with the empty return;
- d>1: d complete returns are compared with the empty return, but one need not be.

This exhausts the specified additive diagnostic class, not all source-native comparison theories. Context-dependent or nonabelian histories, higher witness spaces, and native domain restrictions require additional data.

Importantly, this quotient describes comparison classes of an interpretation. It does not erase raw words, source derivations, or comparison certificates from the retained record. Declaring equality of raw histories would be a different operation.

## 4. All these alternatives admit the same coherence properties

For each d define a groupoid G_d as follows. Its objects are integer positions a in Z^3. A morphism a -> b is a class [c] in C_d with D(c)=b-a. Composition adds count classes, identities are zero, and inverses negate them.

Associativity and the inverse laws hold directly. These are translation-count groupoids, not reconstructed native port groupoids. Typed P/N/E port admission has not been checked.

The nerve N(G_d) has n-simplices given by an initial object and n composable arrows. Consequently the Segal map to the sequence of its one-step arrows is a bijection: it is 1-Segal. The general nerve theorem says it is 2-coskeletal, and therefore 3-coskeletal as well. Because G_d is a groupoid, its nerve is Kan. References [2] and [3] verify the latter statements.

Thus reversibility, the Segal reconstruction property, and these coskeletality bounds all hold for every d. They do not select d. The nerve constructions have different low-dimensional comparison relations, despite sharing those structural properties.

This also distinguishes horn filling from filling a specified full boundary. Given two composable arrows, the nerve supplies their composite and its composition triangle. It does not equate that composite with an independently given third arrow unless the equality holds in C_d. Coskeletality controls higher reconstruction after the relevant lower-dimensional data have been fixed.

Every G_d is connected, and its automorphism group at any object is K_d. Its classifying space therefore has fundamental group K_d and no higher homotopy groups. In particular the d=0, d=1 and d>1 models have different homotopy types. This uses the classifying-space theorem [3]; it is not a claim about Su-32's geometric realization.

The resulting action groupoids only capture 1-types. They cannot certify the multiplicity or higher topology of actual native filling witnesses. A unique comparison class is not the same as a contractible space of comparison witnesses.

## 5. A constructive local-to-global admission rule

Now assume that the source really supplies specified return comparisons and the operations needed to invert, compose, and place them in compatible contexts. For the uniform one-return fragment, let their integer differences be r1,...,rm. Their generated differences form

    R = r1 Z + ... + rm Z = d Z,
    d = gcd(|r1|,...,|rm|).

For an empty list or a list of zeros, d=0. A candidate difference n has a generated count-level comparison exactly when n is in dZ. For d>0 this means d divides n; for d=0 it means n=0.

Necessity follows because each composition adds differences and each inverse negates one. Sufficiency follows from Bezout coefficients: whenever d divides n, there are integers b_i with sum_i b_i r_i=n. The certificate retains those coefficients and the exact source comparisons they invoke. It does not introduce a new primitive relation for n.

An example makes the mechanism concrete. Let w be an admitted return loop, with actual invertible comparisons

    rho2: w^2 => 1,
    rho3: w^3 => 1.

Then there is a derived comparison

    w = w*1 --(w*rho2^-1)--> w^3 --rho3--> 1.

Only the two supplied comparisons, whiskering, and composition were used. This realizes 1=3-2. In contrast, comparisons of two and four returns generate only even differences; parity remains an obstruction to comparing one return with the identity.

For arbitrary typed source comparisons, integer divisibility alone is not sufficient: the required contexts, domains, inverses, and whiskerings must be admitted. The exact if-and-only-if theorem is restricted to the declared uniform additive fragment. The program's certificates are arithmetic certificates, not native proof terms.

This establishes a local-to-global principle for existence of composite comparisons. It does not establish coherence between different Bezout derivations or fill all higher boundaries. Those are further witness-level questions, just as in the previous packet calculus.

## 6. Consequence for the research target

The current native specification does not state a return-comparison generator or an associated higher-cell producer. The period equation supplies an invariant and a kernel, not a rule filling that kernel. The complete-wire regrouping theorem supplies equality of value maps, not an implicit relation on every retained history.

The question has therefore become explicit within this fragment: which actual native comparison, if any, relates histories whose count difference is delta? More generally, which integer differences do actual native comparisons generate, with their typing and derivations retained?

Zero native comparison records in the available input is an evidence limitation. It is not a proof that the complete repository admits none, and it does not justify selecting d=0 as the native answer.

C1 remains viable: locally generated comparisons can determine additional admissibility, as Section 5 proves. The new separation is that coherence constraints propagate and test a selected rule system; they do not by themselves choose its elementary return relations. A source-dependent selection theorem must use more than the displayed translation formula and categorical coherence properties.

No Hopf bundle, circle action, 2-Segal structure for native Su-32, or native geometric filler has been established in this continuation.

## Verification

Run:

    python check_period_relations.py --output results.json

The standard-library program checks exact count/deck conversions on 625 count vectors; the kernel and split-coordinate identities; quotient-group arithmetic for d=0 through 6; preservation or collapse of the primitive return; and constructive/obstruction certificates for the gcd rule. The results distinguish these synthetic arithmetic models from native execution. The unbounded statements are proved algebraically above, not inferred from the finite test ranges.

Raw source bytes are copied unchanged as `source_native_window_note.md`. `manifest.json` records SHA-256 values. No native Node checker or proof assistant was run.

## References

[1] User-supplied `su32-native-window-operation-v1.md`, sections Global source operation and Restrict the global family to the actual window. Source for native facts, not for the diagnostic comparison policies.

[2] Jacob Lurie, Kerodon, Coskeletal Simplicial Sets, Example 3.5.3.4 and Remark 3.5.3.6, https://kerodon.net/tag/051Z. Consulted 2026-10-28. Category nerves are 2-coskeletal; coskeletality is monotone in its bound.

[3] Jacob Lurie, Kerodon, The Nerve of a Groupoid, Proposition 1.3.5.2 and Example 1.3.5.3, https://kerodon.net/tag/0035. Consulted 2026-10-28. Groupoid nerves are Kan; a group's classifying space has its group as pi_1 and no higher homotopy groups.

[4] Previous conversation artifact `packet_extension_calculus.md`, especially Sections 3, 4 and 6. The kernel Z delta and value-level coherence theorem are reused, not claimed as new. The present addition is the classification of compatible count-level relation policies, their equally coherent nerves, and the constructive relation-generation criterion.
