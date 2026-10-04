# Iteration 5: equivariant extension for retained changes

## Frozen test

SCC obligations: attachment transport, route/coherencer compatibility, then readout descent.

- Problem: the path universal property cannot treat the original E-arrows as equality paths on P.
- Conjecture: for a set-valued E-action D and marked object p, equivariant extensions from E(p,-) are equivalent to D(p), by evaluation at the identity.
- Rivals: an initial value already determines arbitrary functions on changes; realized K-actions detect everything detected by retained regular actions; extra inverse-action data are needed.
- Risky consequences: construct both inverse maps including naturality witnesses; derive inverse action from the existing laws; distinguish equal-realization changes with a regular action; exhibit different unrestricted functions agreeing at the identity.
- Test: fresh safe Agda compilation of `RetainedActionYoneda.agda` with deliberate false/true rejection in `RetainedActionBadErasure.agda`.
- Additional outward test: determine whether hom-wise representability also recovers raw object labels. Compare the regular actions at false and true in the concrete model, retaining the source label separately if those actions coincide.
- Disposition: fresh safe compilation and the expected erasure rejection pass. Equivariant extension is unique for the declared set-valued actions. Unrestricted functions, realized observations, and unmarked representables each fail their stronger recovery tests.

## The action interface

`RetainedActionYoneda.Actions` uses the original `RetainedComparisonStructure.Structure`, without replacing its P, E, K, or realization j. A `SetAction` consists of:

- a family D:P -> Type, with each D(p) a set;
- an action of every e:E(p,q) taking D(p) to D(q);
- retained unit and composition witnesses.

The action does not identify p and q as native equality paths. `action-iso` derives invertibility of each action map from the original inverse-E laws and the two action laws. No independent inverse-action field is introduced.

## Universal property

For a marked p, a candidate extension has components

\[
f_q:E(p,q)\longrightarrow D(q).
\]

Its equivariance witness states, for e:E(p,q) and d:E(q,r),

\[
d\cdot f_q(e)=f_r(d\circ e).
\]

`Natural` is the dependent pair of the component function and this witness. Evaluation and extension are

\[
\operatorname{ev}(f)=f_p(1_p),\qquad
\operatorname{ext}(v)_q(e)=e\cdot v.
\]

`universal-iso` proves

\[
\operatorname{Nat}_E(E(p,-),D)\simeq D(p).
\]

The unit action law proves evaluation of extension. For the opposite direction, equivariance at (e,1_p), followed by the right unit law, recovers every component. Since the target fibers are sets, the type of equivariance witnesses for a fixed component function is a proposition. `Σ≡Prop` then recovers the entire natural pair, including its selected witness.

`unique-extension` proves contractibility of the space of natural extensions together with an agreement path to a prescribed initial value. The initial value is supplied; the theorem does not create a point in an empty target fiber.

The extension proof uses composition, units, and action laws. Inverses are used only in the separate action-isomorphism construction. The original inverse data remain stored in the source structure.

## Regular and realized readings

For set-valued retained hom-types, the regular action at p has D(q)=E(p,q), acted on by postcomposition. It is the free set-valued E-action generated at the marked object p in the precise sense of the displayed universal property.

`representable-universality` specializes the target to another regular action:

\[
\operatorname{Nat}_E(E(q,-),E(p,-))\simeq E(p,q).
\]

The functor direction is reversed: evaluation of the natural transformation at the identity of q recovers an arrow p -> q. Both object labels remain parameters. `regular-detects` separately shows that the regular action on the identity distinguishes retained arrows.

For set-valued K-homs, the realized action at p has D(q)=K(p,q) and

\[
e\cdot k=j(e)\circ k.
\]

The original functor laws for j supply its action laws. `realization-extension` exhibits j itself as the natural extension of the K-identity. `recover-realization` retrieves j(e) by acting on that identity. These statements are relative to the supplied realized action; they do not construct or uniquely choose that action independently of j.

In the explicit Boolean model, the regular action sends the identity to change0=(false,false) or change1=(false,true), which are distinct. The realized action sends both to false. `regular-distinguishes` and `realized-identifies` prove these statements; the negative compiler control tries to equate the regular action's hidden coordinate and is rejected.

## Why the witnesses and the object mark remain

`raw0` is the constant-zero function on outgoing retained arrows; `raw1` is the identity function. They agree at the identity arrow but differ at change1. `constant-not-equivariant` proves that raw0 fails the naturality condition, while `identity-is-equivariant` supplies the witness for raw1. Thus evaluation is not enough for unrestricted functions; the equivariance condition is doing the work.

The same example has definitionally identical regular action records at false and true: `same-regular-actions`. `no-unmarked-object-recovery` rules out recovering both distinct object labels from those records alone. Hom-wise representability is not injectivity on raw object labels.

`marked-regular` retains the pair (p,regular(p)); its first projection recovers p. No quotient of object labels is performed.

## Verification and residuals

Source: `agda/RetainedActionYoneda.agda`.

```powershell
pwsh -NoProfile -File research/nima/checkers/check_graded_boundary_coherence.ps1 -Module RetainedActionYoneda -ReceiptStem retained-action-yoneda -NegativeModules RetainedActionBadErasure
```

Fresh safe Agda and the explicit false/true rejection pass. The first compile exposed three ambiguous identity-arrow indices in the concrete model, where hom-types are constant in their object arguments. Explicit false indices repaired those terms without changing a theorem or hypothesis. Compiler launches retain `-NoNewWindow`.

Receipt: `results/retained-action-yoneda-formal-audit.json`.
Source-bound audit: `checkers/check_retained_action_yoneda.py`.

The extension theorem assumes set-valued target fibers; faithful regular probes additionally require set-valued E-homs. Higher source proof fields are not discarded, and no unrestricted higher-valued Yoneda theorem is claimed. The given structure and action are inputs, not a uniquely selected global structure.

Next executable test: remove the target-set hypothesis while retaining naturality witnesses. Test a constant universe-valued action with two different unit-naturality loops at Bool. Determine whether an explicit unit-coherence condition is required to recover uniqueness, rather than silently identifying the two witnesses. The fixed-boundary higher-dimensional examples and full four-simplex remain separate open constructions.
