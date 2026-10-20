# WG prior-proof audit: circle, gluing, coherence and bundle constructions

Date: 2026-10-19.
Repository: andrey-kokoev/marici. Search covered the connected default branch; results reported commit ace56bdce2a23bc7627649366c2a1bd49fc26414. File contents were read through the GitHub connector. This is not an audit of an external uncommitted working tree.

## Findings

Several components previously described as missing already exist. This audit located an actual circle-from-Bool construction, mixed dependent/gluing refinement trees, arbitrary-finite-dimensional framed comparison theorems, recursive witness-bearing resolution with self-application, and a prior torus-join realization whose base uses circle classifying spaces. It did not locate an end-to-end theorem identifying the intended rung/T9 successor with the full circle-torsor universal bundle tower.

No proof assistant was executed. The repository's verification reports are historical source evidence, not fresh verification by this audit. No repository files were changed.

## 1. An actual constructed circle

Source: research/voevodsky/agda/ClosureGluingTreeRegression.agda.
Blob SHA: e3b059868de8aa2d3c6d0c795f15c879de9bf932.

The module defines f,g:Bool -> Unit and proves:

    circleEquiv : Pushout f g ≃ S¹

It constructs a refined boundary Tree Bool 1 and a gluedTree : Tree S¹ 2. The comparison to S¹ is computed using the adopted Cubical library's suspension equivalences, rather than supplied as an unproved field by a caller.

The actual loop is

    push(false,tt) · inverse(push(true,tt)).

Named declarations falseAttachment, trueAttachment and preservesLoop show that it maps to the generating circle loop. gluedLoopNotRefl proves that this retained loop is not reflexivity, using the established Boolean-swap cover. cycleIsTrivial concerns a different loop: a change-of-presentation cycle. Internal topology and presentation coherence are kept separate.

This closes circle construction within the adopted homotopy-pushout foundation. It does not itself identify this two-edge circle with the exact promoted, marked four-cycle and its symmetry action. It also does not select a metric or physical realization.

## 2. Mixed dependent and pushout trees

Source: research/voevodsky/agda/ClosureDependentRefinementTrees.agda.
Blob SHA: 34fa4b010b1b7f50d985cc2131de1dafdf1fde87.

Tree has leaf, sigmaNode, piNode and glueNode constructors. glueNode retains an actual span M -> L, M -> R, its local parent equivalence and refinement trees for all three objects. At and frame recurse together, deriving refined attachments and cut-to-parent equivalences.

The natural-number index is a depth bound. Index types may be arbitrary small higher types, so bounded depth does not imply a finite number of nodes.

For an output defined to be the actual pushout, the local parent equivalence can be the identity. A comparison to an independently specified output remains a theorem obligation.

## 3. All finite framed coherence levels

Source: research/voevodsky/agda/ClosureAllDimensionalCutCoherence.agda.
Blob SHA: d64f891a60ea8b440ee413eb361cb62f07adad22.

Given common input/output realization frames and a common operation, Compatible(k) is the type of a presented map together with its normalization square. The module proves this type contractible, constructs actual changes of cuts and comparisons of arbitrary finite routes, and proves:

    allCellsContractible : (n : Nat) (b : Boundary n) -> isContr (Cell n b)
    fillCell : (n : Nat) (b : Boundary n) -> Cell n b

The induction is over every finite globular dimension, not just triangles/tetrahedra. It does not make the underlying spaces contractible or fill arbitrary independently chosen boundaries outside the compatible-presentation fibers.

ClosureDependentRefinementTrees supplies actual frames for its admitted stages. Instantiating the framed coherence theorem on those frames is the relevant integration; independently defined higher cells still require compatibility with the full endpoint squares.

Source: research/voevodsky/closure-selected-higher-admission.md.
Blob SHA: 0465c9ed2d46741d61e074146507c94f46c3052c.

This later result gives an all-finite-dimensional criterion for lifting a selected target cell. It includes a circle-loop counterexample showing why compatible endpoint maps alone do not admit every intervening homotopy.

## 4. Recursive generation and self-application

Source: research/nima/coherence-resolution-closure.md.
Blob SHA: daff9eebb740d4dcd35bde3057baf490a33a91ab.

For declared complete package and witness-rule types, Resolve retains seeds, unary rules and binary rules. flatten substitutes complete prior derivations into later derivations, with unit and associativity laws. PackageClosure retains the complete package and finite derivation.

Flattening is not generally an equivalence of fully retained nested histories. The propositional reachability projection is idempotent. Neither statement selects the leaf rule signature or a resolution order.

## 5. The source formulation explicitly includes attachment and colimit

Source: research/nima/marici-minimal-mathematical-formulation.md.
Blob SHA: 22097430b821387eadc95a3c00beaec99fd7f3a7.

Sections 2-4 distinguish fillers inside an existing structure from objectification by attachment:

    X[beta] = X pushout_(boundary D_c) D_c.

The note explicitly gives recursive X_0 -> X_1 -> ... and X_infinity = colim X_n. Thus describing all such operations as foreign to the intended source formulation was too broad.

This is a mathematical specification relative to an involutive typed higher-cell signature and admitted boundaries. It is not an inspected compiled RecIdFill-to-BU(1) theorem. Attaching a filler in an enlarged space does not prove its old target already admitted that filler.

## 6. Prior torus join and classifying-space realization

Source: research/chatgpt/marici_relative_operation_fibre_20260908.md.
Blob SHA: beb44241d693469e011c448ec6d5c3561ebf9541.

Section 3 takes T to be the topological circle group and constructs

    D_K = (BT)^3 wedge (BT)^3,
    q : D_K -> (BT)^6,
    Z_K = ((D²)^3 x (S¹)^3) union_((S¹)^6) ((S¹)^3 x (D²)^3).

It gives a homotopy-fiber sequence Z_K -> D_K -> (BT)^6 and a projection-span comparison:

    Z_K ≃ (S¹)^3 * (S¹)^3.

It then obtains the nonequivariant decomposition

    Z_K ≃ wedge^9 S³ wedge wedge^18 S⁴ wedge wedge^15 S⁵
          wedge wedge^6 S⁶ wedge S⁷.

The note distinguishes an all-degree theorem for the relative operator algebra from bounded exact checks. It also distinguishes the coefficient-combinatorial realization from the native physical endpoint diagram. It assumes the standard circle and BT in this realization; it does not derive them from T9 or from a bare finite carrier.

This is existing join-to-classifying-space work, not a missing construction to invent again.

## 7. Earlier nested S-construction

Source: research/nima/nested-closure-system-full-categorical-construction-sketch.md.
Blob SHA: 6e5fcc9d5d77377756c983b4b69822db2b9d5c04.

The supplied stable infinity-category supports complete interval/cofiber diagrams, 2-Segal cut reconstruction and iterated S-constructions for every finite nesting depth. This is a genuine mathematical model using cited theorems; it is not a newly compiled universal WG realization. Its indexing, source comparisons and a selected infinite completion remain explicit.

Stable cofiber towers must not silently replace the unstable Hopf/projective-space tower.

## Revised direct specialization

Let

    C = Pushout(Unit <- Bool -> Unit).

The existing circle regression supplies C ≃ S¹. For any constructed X, form

    J(X,C) = Pushout(X <- X x C -> C)

using the two projections. This is the join specialization already analyzed. The complete pair family is expressible by a dependent sum and the pushout is an existing closure constructor. Consequently

    E_0=C; E_(n+1)=J(E_n,C)

is a mathematical recursive specialization of existing constructors. This statement requires no real coefficients, trigonometric functions or metric completion merely to define the spaces.

To identify the quotient tower with CP^n and BU(1), retain the appropriate circle/torsor action, stage inclusions, equivariant gluing and infinite diagram. The inspected sources have ingredients and related realizations; this audit did not locate a theorem deriving the exact intended rung/T9 span, actions and all transition maps and identifying their limit with BU(1).

## What is no longer a generic missing proof

- Circle construction from a finite boundary, within the adopted HIT foundation.
- Mixed dependent/pushout stage construction with complete attachments.
- Self-application and flattening of retained finite witness derivations.
- All-finite-dimensional coherence of compatible framed presentations.
- Existence of a prior torus-join/classifying-space realization.
- Presence of recursive attachment and an infinite-colimit specification in the source formulation.

## Exact remaining comparison, not a new-framework request

For the selected native successor W, construct a retained equivariant comparison

    Realize(W(P_n)) ≃ Realize(P_n) * C

that preserves the specified attachment span, circle action, transition map and complete source witnesses. If the intended source follows a different tower, identify that tower's actual realization rather than forcing this equivalence by renaming the levels.

The present incoming-family T9 numerical fixture cannot stand in for an exhaustive description of the broader closure calculus. Conversely, a generic pushout capability is not by itself proof that the particular T9 fixture has the required realization.

## Source URLs

All paths above are relative to:
https://github.com/andrey-kokoev/marici/blob/main/

Read-through status is stated individually above. No archive note, filename, printed success label or dependency inventory has been treated as a compiled proof of the complete universal bundle theorem.
