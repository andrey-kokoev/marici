# Iteration 1: graded boundary recovery and a mapping-out universal property

## Question and operator direction

Construct the open-boundary/filler distinction and grade transitions in Cubical Agda. Test a return from grade four to the initial question; explore the simplest explanatory universal property while preserving witnesses. The operator requested an iteration series and prohibited compiler launches that open a terminal or steal focus.

SCC obligations: forward realization and route/coherencer compatibility. This iteration defines a globular parallel-comparison tower. It does not yet specify all faces of geometric simplices or identify the construction with the four-chart stable helix.

## Frozen test

- Conjecture: freely adjoining a second filler together with a path from the first gives a completed package equivalent to the original completed package. Iterating preserves the initial answer type and supplies a mapping-out universal property.
- Rivals: the return preserves only a coarse readout; every well-formed boundary automatically fills; recovery implies unique fillers even with a fixed boundary.
- Required consequences: both recovery laws at every grade; a contractible space of extensions for every initial interpretation; preserved distinct initial answers; explicit comparison reversal with a two-reversal witness.
- Hostiles: an empty initial answer type; the incompatible Boolean endpoints false and true; distinct fillers of a fixed type-level boundary; attempted compiler acceptance of an incompatible filler or answer erasure.

## Typed construction

For a type A, define open boundaries and their filler types mutually:

\[
B_0=1,\qquad F_0(*)=A,
\]
\[
B_{n+1}=\sum_{b:B_n}(F_n(b)\times F_n(b)),
\qquad F_{n+1}(b,x,y)=(x=y).
\]

The initial question B0 exists even if A has no inhabitant. An upper boundary records two actual fillers of its lower boundary. The completed grade-n package is

\[
C_n=\sum_{b:B_n}F_n(b).
\]

This is a recursion of the same declaration/constraint/witness constructor, not identification of those roles. Grade counts iterated comparisons, not physical time.

Expansion and recovery are

\[
u_n(b,x)=((b,x,x),\mathrm{refl}),\qquad
r_n((b,x,y),p)=(b,x).
\]

Agda proves both laws:

\[
r_nu_n=I,\qquad u_nr_n\simeq I.
\]

The second homotopy at ((b,x,y),p) is

\[
i\longmapsto ((b,x,p(i)),\ j\longmapsto p(i\wedge j)).
\]

It retains the lower boundary b, but allows the upper endpoint y to move. It is not a homotopy relative to the entire marked upper boundary.

Induction gives maps expand_n:A -> C_n and close_n:C_n -> A, with both inverse laws, hence

\[
C_n\simeq A
\]

for every natural grade n and arbitrary universe-level A. In particular `close-four : Cell 4 -> A` and `four-return` implement the proposed return for completed grade-four packages. The return reads a witness from a completed package; the construction of an upper boundary already uses lower fillers. It does not generate a witness from an unfilled initial question alone.

## The proved universal property

For every target type Y, restriction along expand_n and extension along close_n give an equivalence

\[
(C_n\to Y)\simeq(A\to Y).
\]

For a fixed interpretation f:A -> Y, define

\[
\operatorname{Extension}_n(f)
=\sum_{h:C_n\to Y}(h\circ\operatorname{expand}_n=f).
\]

The formal theorem `unique-extension` proves

\[
\operatorname{isContr}(\operatorname{Extension}_n(f)).
\]

Thus a prescribed interpretation of the starting answers has one coherent extension to the freely completed parallel-comparison packages. The extension includes its agreement witness. This is a universal property of the constructed type equivalence, not yet a free category of all Marici operations or a universal filling of arbitrary marked boundaries.

## Rotating the comparison

Define

\[
\rho_n((b,x,y),p)=((b,y,x),p^{-1}).
\]

`reverse-twice` proves rho_n squared is identity. `reverse-base` supplies the path between the two lower packages read by the opposite orientations. This models an exchange of the question's two endpoints and reverses its witness; no complex scalar or phase is inserted.

## Tested distinctions

1. `empty-question` inhabits B0 for A=Empty, but `no-empty-completed-cycle` proves C_n -> Empty for every n. The same graded recovery explains why no completed proof can be manufactured for an empty answer type.
2. For A=Bool, the marked grade-one boundary (*,false,true) exists, but its filler type is empty. `no-universal-marked-filler` rejects a solver for every marked boundary.
3. `answers-retained` proves that the grade-four expansions of false and true are distinct.
4. For A=Type0, take the fixed boundary (*,Bool,Bool). Both reflexivity and the univalent path for Boolean negation fill it. `marked-fillers-distinct` proves these fillers unequal: transporting false along them gives false and true respectively. `marked-fillers-not-contractible` refutes contractibility of this particular filler type.
5. Two negative modules attempt to fill false=true by reflexivity and identify the two grade-four answers. Both must reject with the expected false/true unequal-term diagnostic.

The total-package equivalence and the noncontractible marked filler space coexist because the total-package recovery homotopy can move an endpoint. Confusing these two bases would erase the distinction the operator wants retained.

## Verification

Formal root: `agda/GradedBoundaryCoherence.agda`.

```powershell
pwsh -NoProfile -File research/nima/checkers/check_graded_boundary_coherence.ps1
```

The runner uses `-NoNewWindow`, redirects output, freshly checks with `--ignore-interfaces`, verifies both intended rejection controls, and checks stable compiler/owner/library source hashes. The module is safe Cubical Agda with no postulates or unsolved holes.

Receipt: `results/graded-boundary-coherence-formal-audit.json`.
Source-bound audit: `checkers/check_graded_boundary_coherence.py`.

## Disposition and executable continuation

The witness-retaining graded return and its mapping-out universal property are proved. Automatic filling and universal uniqueness at a fixed boundary are refuted by explicit terms in the same formal module.

The next substantive step is to keep the entire upper boundary marked and construct actual triangle face/edge data, then compare its filler space with the parallel-path tower. In particular, specify which endpoint movements are allowed before claiming a boundary-preserving universal property. The fixed Bool-type boundary with its identity and negation fillers is a mandatory retention control for that comparison. This is an executable extension, not a request for external authority.
