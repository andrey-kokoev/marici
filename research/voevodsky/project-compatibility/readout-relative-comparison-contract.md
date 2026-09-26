# Readout-relative comparison contract, version1

## Status

Candidate contribution to construction–observation compatibility, extracted from the frozen comparison benchmark. Not a universal physical foundation or a certificate that another sector satisfies these obligations. The basic contract is stated for sets; module and normed-linear refinements require those additional structures. Derived sectors must supply their actual complexes and coherence witnesses rather than inherit a set-level theorem by analogy.

## Typed data and source authority

A sector must supply, independently of the desired result:

- V: admitted source presentations, including coefficient object, normalization and admissible parameter domain;
- O:V->Z: intended readout and its reading type;
- Y: retained port data, including required occurrence labels, comparison jets, sheets and boundary grades;
- F:V->Y: source-derived comparison/observation map;
- K subset Y: declared compatible-output object, with its independently specified equations or witnesses;
- source actions, orientation/local-system types and their coherence witnesses;
- the relevant completion/topology on outputs and readings;
- source provenance for each item, including which maps are merely mathematical candidates.

A coefficient realization with matching moments is not automatically the physical operator. Admission of a graph transition is not scientific source authority. Changes of normalization or source model require a new comparison witness.

## 1. Compatible outputs and realization are different obligations

Prove F(V) subset K. If K=ker(H) in a module model, this requires HF=0. Claiming exactness at the output further requires ker(H)=im(F), not merely injectivity of F. Claiming that all declared compatible outputs are physically realizable requires the corresponding source-surjectivity statement; it must not be obtained by silently defining K as im(F).

Recovered example: F(x)=(Ax,Bx), with invertible B. The ordinary3->6 map has a rank3 cokernel. The independently displayed compatibility equation

    H(y,z)=y-A B^(-1)z

gives a split exact3->6->3 complex. That is not the ordinary two-term cone. It is a specific linear realization requiring B invertible over the declared coefficient ring.

If only realized outputs are in scope, one may work on F(V), but must explicitly label that restriction. It does not settle existence or uniqueness of a readout on a larger K.

## 2. Retain exactly enough data for the intended readout

The fundamental factorization test is

    F(v)=F(w) implies O(v)=O(w).

It is necessary and sufficient for a unique readout r:F(V)->Z satisfying r F=O. In the module-linear setting it becomes ker(F) subset ker(O). Full recovery of v is unnecessary when O intentionally forgets some directions. In an equivariant sector, F and O must first be well-typed equivariant maps; only then does fiber constancy yield an equivariant factor. A set-level factorization does not repair a representation mismatch. `readout-orientation-obstruction.md` tests this on the actual even physical line and odd Tate coefficient.

Every proposed forgetting map q:Y->Y_coarse must pass the SAME test with qF in place of F. This is the correct way to audit removal of labels, sheets, normalization coefficients or asymptotic grades. A retained-data budget is readout-specific, not universally sufficient for all observations.

The triangle controls instantiate this distinction: P0 of P=RG retains the regulator residue but not the finite part; the latter needs P1 and the second comparison coefficient. The two branches X=+P and X=-P have the same algebraic normal nu0 but different analytic behavior. Neither a regulator residue nor nu alone selects a physical finite readout or branch prescription.

## 3. Completion requires a readout bound, not necessarily a full inverse

Normed-linear specialization: let Y be normed, Z Banach, and F,O linear. A bounded readout on im(F) exists exactly when some finite C satisfies

    ||O(v)||_Z <= C ||F(v)||_Y for every v.

The estimate implies kernel inclusion. It defines a unique bounded r on im(F), and completeness of Z extends r uniquely to closure(im(F)) in the completion of Y. If the claimed target is a larger completed K, density or an independently justified extension is still required.

For parameter families the constant must be uniform on the declared domain. A sequence F_t(v_t)->0 with O_t(v_t) not tending to0 falsifies that uniform claim. A different weighted topology is a different completion claim unless the source establishes the needed equivalence.

Severe readout-relative control: F_t(x,y)=(x,t y). Reading x is uniformly stable with C1 even though the full inverse diverges as t->0. Reading y has no such bound. Thus our earlier full-inverse estimates were sufficient local tools, not necessary conditions for EVERY readout.

For nonlinear or nonnormed sectors the appropriate continuity/uniformity condition must be stated explicitly; this linear estimate is not imposed as their universal topology.

## 4. Coefficient authority cannot be bypassed by scalar inversion

An integral control exposes a distinct extension obstruction. Let F:Z->Z be n->3n and O:Z->Z/3 be n->n mod3. There is a unique readout on im(F)=3Z,

    r(3n)=n mod3.

It does not extend to a group homomorphism on the whole ambient Z: an extension would need r(3)=1 but also r(3)=3r(1)=0. Kernel inclusion alone does not supply an ambient-target extension.

No inversion of3 was used. Rationalizing would erase the intended Z/3 readout. This is an exact control for the contract, not a claim that it is already a source map in Nima's Tate sector.

## Composition obligation

For a subsequent source-authorized comparison G, require O to be constant on fibers of GF, not just of F. An already valid readout can be lost under the second comparison. If compatible readouts r1 and r2 satisfy r1F=O and r2G=r1 on realized outputs, the composite square commutes. Bounds compose where their domains, topologies and uniformity hypotheses actually match. Derived or presentation-groupoid coherence is additional evidence, not supplied by this elementary statement.

## Evidence map and current admission boundary

| Obligation | Existing evidence | Limit |
|---|---|---|
| Compatible outputs | `spectral-observer-compatible-completion.md` | Explicit augmented complex; owner interpretation pending |
| Retained data | `triangle-readout-jet.md`, `contact-infinity-filtered-recovery.md`, `positive-sheet-normal-integration.md` | Readout/label/sheet budgets are scoped; not universal source admission |
| Completion | `contact-score-fisher-gate.md`, `contact-full-score-tower.md` | Fixed score ports can lose uniform norm control; not all physical observables |
| Source identity | `contact-primary-operator-typing.md`, `contact-external-leg-comparison.md` | Physical source exists; normalized operator/contact extraction remains separate |
| Consolidated singular comparison | `threshold-regulator-consolidation.md` | Same-density pole/log match, NOT canonical finite-part equality |

## Tested source instances and next gate

The first cross-source tests are now recorded in `readout-comparison-synthesis.md` and `readout-comparison-claims.json`: the integral odd Tate bridge, later realized even fs/Kato diagonal packet, and forbidden untwisted even-to-odd comparison are distinguished from the spectral observer. No normal or integer3 is inverted. The existence of the later fs/Kato realization corrects the older formal-star missing-realization diagnosis within its scope.

Next recover an independently stated project-level observation/constructor requirement and test the comparison it actually needs. A direct map between differently typed sector readouts is not mandatory merely because both occur in a common calculus. Keep physical triangle admission parallel rather than resuming auxiliary asymptotics.

## Verification

`check_readout_relative_contract.py` checks the finite fiber test, the stable/unstable readout distinction for one degenerating comparison, readout loss under composition, and the integral image-versus-ambient obstruction. These controls accompany the written factorization and extension proofs; they do not certify a new physical sector or formalize the general theorem.
