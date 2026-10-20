# Marici rung successors versus the circle-join tower

Date: 2026-10-19

## Result

The existing Marici homotopy-pushout constructor has an explicit specialization that is exactly the desired join successor. The required span is the complete pair table

    A <- A x T -> T,

with the two projections as attachments. Source/target re-fibration preserves this span up to equivalence, so the existing span-comparison machinery supplies the mathematical compatibility with changes of rung presentation.

For a retained circle torsor T, its displacement group G, and E_n=T^{*(n+1)}, the resulting quotient successor has an equally explicit cofiber description. With B_n=E_n//G and M_n=(E_n x T)//G,

    B_(n+1) ≃ Pushout(B_n <- M_n -> *).

A temporary choice of a torsor point identifies M_n->B_n with p_n:E_n->B_n. Thus B_(n+1) is the homotopy cofiber of the previous bundle projection. This includes the Hopf attachment giving CP^2.

This is a mathematical specialization/comparison of inspected source definitions, not a newly compiled Agda theorem and not a finding that the existing numerical T9 fixture already selects this span. No repository changes were made.

## 1. Sources inspected in this continuation

The following default-branch files were read through the GitHub connector. The hashes are GitHub content-blob SHAs, not hashes of this note.

| Source | Blob SHA | Use |
|---|---|---|
| research/grothendieck/agda/ClosureGeneratedMapNecessity.agda | 1332e7f686e0e85c73c08d6f98c430f6e58b863a | Complete pushout cocones and reconstruction |
| research/voevodsky/agda/ClosureFiniteGluingNormalization.agda | 1ae0b4d07fb4ef86d7c7bd7091731502fb21006e | Actual pushout realization and LiftSpan |
| research/voevodsky/agda/ClosureFiltrationMapNaturality.agda | 1a964d8ef518edd76fcc1a1d87cd9e1870945191 | Actual cofiber constructors and maps |
| research/nima/label-from-to-fibration-tower.md | 22e7685c51097bf0fc46e43e8c98f1e029942187 | Re-fibration recurrence |
| research/nima/section-field-promotion-cycle.md | b87060c170be008974cc803cdd5d5fbebad47dbc | Section-valued successor |
| research/nima/checkers/check_rung_transport_diagram.py | 4245dbab396653fedfb05ea71ef735913edd6097 | The two actual incoming-family T9 policies |

A name such as `Join` inside the chain normalizer does not by itself mean the topological join: it is a pushout over that chain's specified boundary. The projection-span specialization below is what makes it a topological join.

## 2. The exact source-to-join specialization

Marici's `ClosureGeneratedMapNecessity.Generated` takes f:S->A and g:S->B, sets P=Pushout(f,g), and constructs an isomorphism

    (P -> X) ≃ Sigma(l:A->X) Sigma(r:B->X)
                       ((s:S) -> l(f(s)) = r(g(s))).

Both inverse laws are defined in the inspected source. The attachment paths are part of the right-hand side, not omitted equality obligations.

Use the ordinary table fields

    Rows = A x T
    label(a,t) = (a,t)
    from(a,t) = a
    to(a,t) = t.

Instantiate S=A x T, f=pr_A, g=pr_T. The resulting pushout is, by definition, A*T. In the standard double-mapping-cylinder model its points are (a,t,u), with u in [0,1], where the T coordinate is forgotten at one endpoint and the A coordinate at the other. These are precisely the join identifications.

Accordingly the constructor data for a map A*T->X are:

    l:A->X,
    r:T->X,
    h:(a:A)(t:T)->l(a)=r(t).

This is an exact instance of the existing one-node theorem. It does not require a new independent Hopf attaching map or a new universal gluing axiom.

The current incoming-family T9 fixture instead performs two groupings/promotions of 137 matrix-valued records, with either inherited or common targets. Its code contains no instance identifying those particular data with this complete pair span. The new specialization therefore must not be reported as an executed property of that fixture.

## 3. Compatibility with rung reindexing and symmetry

Let e:R'≃R be a retained-row presentation change preserving the attachments to A and T. It gives an equivalence of spans with e in the middle and identities on the endpoints. Marici's `LiftSpan` accepts exactly such data and produces an equivalence of the pushouts.

For an exact coordinate version, the induced map keeps inl(a), inr(t), and sends the seam push(r') to push(e(r')). An inverse uses e inverse and its inverse homotopies. Thus reindexing before gluing and transporting after gluing compare using the full seam witnesses.

This supplies a mathematical implementation of the required rung squares for the join-span candidate. It does not identify the candidate with every other coherent T9 or provide an uncompiled all-dimensional native realization theorem.

If G acts on A and T, use its diagonal action on R=A x T. Both projections are equivariant. In the geometric model the induced action is

    g.[a,t,u] = [g.a,g.t,u].

Identity and composition follow on every coordinate, including the endpoint identifications. A map of input G-spaces induces a map of joins. Equivalences of input G-spaces induce equivalences of joins with the actions retained. Synthetic higher-coherence formalization must preserve the input action's coherence data; this note does not replace it by a set-valued endpoint action.

The join iteration index n is separate from the presentation labels 12,11,10,... . Re-fibration can preserve one stage while a separately specified horizontal successor changes the stage.

## 4. A circle is already a pushout of finite source data

The two-point span

    * <- Bool -> *

has a homotopy pushout with two point constructors and two joining paths. One path can be contracted; the remaining loop gives S^1. The equatorial C4 admits the same homotopy description by splitting it into its two two-edge arcs and retaining their two common endpoints. Each arc is contractible, but their two-component intersection must not be collapsed to one component.

This construction produces the circle's homotopy type directly in the pushout-closed foundation. It does not require a separate real-number completion or an assigned quarter-turn angle. It does not, merely by constructing the type, identify its coherent multiplication or a specific continuous physical rotor with a native rung operation.

An ordinary SET pushout of the same span is a single point. Retaining its path constructor is essential.

## 5. Quotient growth is a cofiber of the preceding bundle

Work with the retained topological circle group G and G-torsor T from the previous conditional construction. Let E be a free G-space and B=E//G. Homotopy orbits are homotopy colimits, so applying them to the equivariant join pushout gives

    (E*T)//G ≃ Pushout(E//G <- (E x T)//G -> T//G).

The G action is free on the spaces used here. Ordinary orbit spaces and homotopy orbits agree up to homotopy. Since T is a torsor, T//G is contractible. Define

    M=(E x T)//G,
    q:M->B,  [e,t] |-> [e].

Then the next base is canonically, up to the retained equivalences,

    B^+ ≃ Cofib(q).

Choose t0 in T only to identify this formula with familiar coordinates. Write t=g.t0 and send [e,t] to g inverse.e. This identifies M with E and q with p:E->B. Different t0 choices give transported identifications; the original M construction required no preferred origin.

For E_n=T^{*(n+1)}, the sphere/quotient model gives

    E_n ≃ S^(2n+1),   B_n ≃ CP^n,
    CP^(n+1) ≃ Cofib(S^(2n+1) -> CP^n),

where the map is the actual preceding circle-bundle projection, not a freely selected map with the same domain and target.

The first base extension is * union_(S1) *, namely S2. The next attaches a four-cell along S3->S2, the Hopf projection, giving CP2. Subsequent attachments use the same operation.

A bundle can also be described through compatible local torsor families. Over the two pieces B and * use the original fiber and T. A point [e,t] of M supplies the unique equivariant identification of those fibers sending e to t. These are actual seam equivalences; no global section of p is required. This is the form suited to dependent pushout gluing and its flattening theorem.

## 6. Fixed-target filling versus adjoining a cell

The previous obstruction remains correct for a filler D4->S2 of a fixed map S3->S2: that would make the map nullhomotopic in S2.

The cofiber constructor is a different operation. It changes the target:

    S2 -> S2 union_eta D4 = CP2.

The Hopf map eta is non-null in the old S2 and becomes null after this inclusion. The interior exists in the enlarged type, not in the old type. Therefore that fixed-target obstruction does not prohibit a WG that genuinely adjoins a new cell. Counting a fifth call still does not identify its attachment, but the target-changing version of the proposed mechanism is mathematically viable.

## 7. Discriminating tests against other rung successors

### Retained-total re-fibration

The actual theorem T_p(E)≃E immediately rules out identifying this successor alone with E*T in general. At E=T=S1, the first remains S1 while the second is S3. This does not invalidate re-fibration: it is the correct mechanism for lossless vertical presentations, rather than topology growth.

### Global-section promotion

The section rule produces

    Section(p)=prod_(b:B) fib_p(b),
    E^+=Sigma_(sigma:Section(p)) B.

For the Hopf projection p:S3->S2, Section(p) is empty. A homotopy section s would give p_* s_*=id on pi2(S2)=Z, while pi2(S3)=0. Hence its successor is empty for this selected field. This is an obstruction to that particular substitution of p into the rule, not a no-go for all choices of fields or for local section-and-seam constructions.

### Incidence line graphs

L(C4)≅C4, and repeating it leaves a cycle at every stage. Thus raw repeated line-graph promotion of the already extracted cycle is not the sphere-join successor. Other graph seeds and additional realization operations remain different possibilities.

### Incoming-family numerical T9

The inspected code preserves all original leaves and checks two different endpoint policies. It does not compute a circle action, a projection-span pushout or a bundle attachment. No equality with the join successor can be obtained by substituting its rung labels for topological dimensions.

## 8. Finite computations performed

The independent checker uses exact rational sparse elimination, never floating-point rank tests. The main results are:

| Model | f-vector | Rational Betti numbers |
|---|---|---|
| C4 | (4,4) | (1,1) |
| Discrete pair-span pushout on two four-sets, K4,4 | (8,16) | (1,9) |
| Both cycle edges and cross edges, no higher cells | (8,24) | (1,17) |
| Full C4*C4 | (8,24,32,16) | (1,0,0,1) |
| Full C4*C4*C4 | (12,60,160,240,192,64) | (1,0,0,0,0,1) |

These distinguish pair inventories from higher-type input. A pushout of the two discrete four-sets does not become the Hopf total space. The paths in each circle and their product structure must be retained. With full types, the homotopy-pushout construction accounts for those higher cells; they are not independent fitted attachment lists.

Further exact controls check table reconstruction, source/target presentations of complete pair tables, six line-graph iterations of C4, the full D4 x D4 action on the two-cycle join, and finite diagonal-orbit identifications. The connected covering C8->C4 has 16 vertexwise section candidates and no edge-compatible section; the trivial double cover has two. This is a finite local-versus-global section control, not a numerical proof about the Hopf bundle.

The new checker passed 1,347 assertions. The previous circle-torsor checker was also freshly rerun and passed its 53,205 assertions. Neither checks the infinite-dimensional classification theorem or recompiles Agda.

## 9. Sequential completion does not require another primitive

Given stage types X_n and transition maps i_n, let D=Sigma_(n:Nat) X_n and s(n,x)=(n+1,i_n(x)). The homotopy coequalizer of id_D and s is the sequential homotopy colimit.

That coequalizer itself can be constructed as the homotopy pushout

    D <-[id_D,s]- D coproduct D -fold-> D.

The two copies of the target D have different roles. For each element of D the pushout creates a two-edge path from it to its successor; contracting the auxiliary hub recovers the usual telescope relation. Thus dependent sums over Nat, coproducts, and homotopy pushouts suffice for this completion as a homotopy type.

This corrects treating sequential completion as necessarily a new axiom outside the available foundation. It does not prove an analytic/norm completion theorem, convergence of a physical operator, or a repo-native compiler comparison for the actual stage diagram.

## 10. Remaining proof obligation

The mathematical gluing capability is available, and the join/cofiber interpretation is now explicit. What is not established is that the particular intended WG/T9 request supplies the complete pair span, its structured circle action, and the retained bundle projection at each stage. A new proof-assistant adapter must instantiate the existing theorems on those data and compare all stages and arrows. The current incoming-family fixtures do not certify that identification.

Original A4 equivariance on a single Hopf base, BSU(2), BSU(3), physical dynamics and measured quantities are not established by this comparison.

## References

Repository paths above are in https://github.com/andrey-kokoev/marici . Source content and its hypotheses govern the claims, not comments identifying a module with physics.

E. Rijke, *The join construction*, arXiv:1701.07538. https://arxiv.org/abs/1701.07538

U. Buchholtz and E. Rijke, *The real projective spaces in homotopy type theory*, arXiv:1704.05770, Introduction (pushouts, joins, sequential colimits), flattening lemma, and Conclusion (complex-projective and Milnor extensions). https://arxiv.org/html/1704.05770v1

The complex-projective quotient/cofiber comparison in this note is proved using the displayed equivariant pushout and sphere model; the cited article is not being represented as a compiled Marici proof of that comparison.

## Reproduction

    python check_rung_join_bridge.py --output rung_join_cofiber_bridge_results.json

Python standard library only. Artifacts were created in the conversation working directory; no repository commit, upload or publication was performed.
