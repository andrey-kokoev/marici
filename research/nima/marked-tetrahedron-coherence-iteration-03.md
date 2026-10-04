# Iteration 3: tetrahedral face completion and a common criterion

## Question and frozen test

Assemble the four marked triangle faces from iteration 2. Does any three-face horn determine the missing face together with a tetrahedral coherence witness, without moving the four vertices, six edges, or three supplied faces?

SCC obligations: forward realization and route/coherencer compatibility.

- Conjecture: each missing-face problem is a fiber of an equivalence to a common composite-route type, and therefore has a contractible completion space.
- Rival 1: different missing faces require independent closure axioms.
- Rival 2: coherence can be checked only after moving supplied face witnesses.
- Rival 3: agreeing on the final return edge identifies the entire coherent tetrahedron.
- Tests: construct all four face-to-route equivalences and relative universal properties; retain every supplied face; construct two fully coherent tetrahedra with equal return diagonal but provably distinct retained data.

## Marked edges and imported triangle faces

For vertices x0,x1,x2,x3 in an arbitrary type A, retain all six paths e01,e12,e02,e23,e13,e03. The four face types are the actual imported `Triangles.Triangle` types:

\[
a:e_{01}\cdot e_{12}=e_{02},\quad
b:e_{12}\cdot e_{23}=e_{13},\quad
c:e_{01}\cdot e_{13}=e_{03},\quad
d:e_{02}\cdot e_{23}=e_{03}.
\]

The dot denotes path concatenation, first the left path then the right path. No edge or face is identified merely from its endpoints.

Set s=(e01 dot e12) dot e23. The two routes from s to e03 are

\[
L(a,d)=\operatorname{cong}(-\cdot e_{23})(a)\cdot d,
\]
\[
R(b,c)=\operatorname{assoc}^{-1}\cdot
  (\operatorname{cong}(e_{01}\cdot-)(b)\cdot c).
\]

The associator is retained with its actual orientation. The tetrahedral coherence type is

\[
\operatorname{Tetrahedron}(a,b,c,d)=(L(a,d)=R(b,c)).
\]

This is a grade-three filler comparing two composed face witnesses, not an equality of edge readouts.

## Four views of the missing-face question

Each row is an equivalence from its indicated face type to the common route type s=e03:

| Missing face | Face-to-route map |
|---|---|
| 023 | d maps to L(a,d) |
| 012 | a maps to L(a,d) |
| 013 | c maps to R(b,c) |
| 123 | b maps to R(b,c) |

The first two use right whiskering and path composition; the last two use left whiskering, the explicit associator, and composition. Whiskering by an invertible path induces an equivalence of equality types. No truncation of the face-witness types is assumed.

Taking the fiber at the opposite fixed route proves contractibility of all four missing-face completion types. For example,

\[
\operatorname{isContr}\left(\sum_{d:\operatorname{Face}_{023}}
  \operatorname{Tetrahedron}(a,b,c,d)\right).
\]

The `solve023`, `solve012`, `solve013`, and `solve123` equivalences also preserve a chosen tetrahedral witness while expressing it as agreement of the corresponding face with its required value. This is four reversible descriptions of the same marked coherence question. It is not yet a theorem about a geometric four-turn operation.

For all four faces fixed, `incompatible-face` says that a supplied face unequal to its required value obstructs the tetrahedral filler. This iteration gives that conditional criterion; it does not instantiate a same-six-edge, incompatible-fourth-face counterexample.

## One reusable universal-property constructor

`RelativeCoherentCompletion.agda` factors out the common construction. Its inputs are a base B of supplied data, a family F of possible completions, and a proof that each admitted completion space is contractible.

Let T=Sigma b F(b), with projection pi:T -> B. The formal module constructs completion, recovery, the homotopy whose projection is constant, and

\[
\left(\prod_{t:T}Y(\pi(t))\right)
\simeq
\left(\prod_{b:B}Y(b)\right)
\]

for every dependent interpretation family Y:B -> Type. Extension of a specified section has a contractible space of choices.

The characterization `completion-criterion` proves both directions of

\[
\left(\prod_{b:B}\operatorname{isContr}(F(b))\right)
\simeq
\operatorname{isEquiv}(\pi).
\]

Thus the reusable criterion is: forgetting just the freely added completion is an equivalence over the supplied base. It is not a demand that the earlier possibly nonfaithful realization j:E -> K become an equivalence.

All four tetrahedral horns instantiate this same constructor. An additional instantiation at the previous triangle horn proves its completion map, recovery map, and retained recovery witness unchanged by reflexivity (`triangle-completion-preserved`, `triangle-recovery-preserved`, `triangle-witness-preserved`). The vertices and six edges are fixed module parameters; the three supplied face witnesses form the base. The relative recovery path does not move those supplied faces. The new face and its coherence witness can vary together during recovery; this is not an assertion that all fillers of a fully fixed four-face boundary are contractible.

## Grade-three comparison and retention hostile

With all edge and face data retained as parameters, the globular boundary from iteration 1 has endpoints L(a,d) and R(b,c). Its grade-three filler type is definitionally the tetrahedral coherence type. The imported-fiber equivalence is identity; there is no quotient of the source boundary.

For a concrete retention test, take all four vertices to be Bool in the universe of types. Let u be the univalent path of Boolean negation.

- Ordinary edges: all six are refl.
- Twisted edges: e01=u, e12=u inverse, e02=refl, e23=refl, e13=u inverse, e03=refl.

Cancellation and unit witnesses supply three faces in both cases. The proved missing-face constructor supplies the fourth face and the tetrahedral witness, so both packages are fully coherent.

Their return diagonal e03 is definitionally the same refl. Their first edges are distinct, as detected by transporting false. `different-tetrahedra` proves the complete packages unequal; `no-diagonal-recovery` excludes recovery of every complete marked tetrahedron from its return edge alone.

The negative module `MarkedTetrahedronBadErasure` attempts to identify those first-edge actions by reflexivity and must fail with the false/true unequal-term diagnostic.

## Verification

Formal roots: `agda/RelativeCoherentCompletion.agda` and `agda/MarkedTetrahedronCoherence.agda`.

```powershell
pwsh -NoProfile -File research/nima/checkers/check_graded_boundary_coherence.ps1 -Module MarkedTetrahedronCoherence -ReceiptStem marked-tetrahedron-coherence -NegativeModules MarkedTetrahedronBadErasure
```

Fresh safe Cubical Agda compilation and the rejection control pass. Compiler launches use `-NoNewWindow`. The source-bound checker verifies both new modules and the imported owner-local triangle/tower closure, the compiler hash, and the Cubical library inventory.

Receipt: `results/marked-tetrahedron-coherence-formal-audit.json`.
Source-bound audit: `checkers/check_marked_tetrahedron_coherence.py`.

## Disposition and executable continuation

The tetrahedral horn theorem is proved in all four face directions and reduces to the same relative completion criterion as the triangle. Return-edge equality still does not erase retained coherent data.

Next: hold a complete tetrahedral boundary fixed and compare two tetrahedral fillers. Construct the grade-four comparison and examine which additional marked data must remain in its base. A concrete higher-dimensional fixed-boundary obstruction, or explicit four-simplex face data, is needed before promoting the horn theorem to a closure claim about arbitrary complete tetrahedral boundaries. Repeated forward viewpoint changes also require their own higher coherence; the four face descriptions alone do not prove that cycle.
