# Ordinary Yoneda reconstruction

## Question

Recover ordinary Yoneda, including noninvertible arrows, and retain its typed
reconstruction witnesses through the existing native constructor interface.
This is a bounded step toward, not a proof of, the proposed four-channel theorem.

## Claim boundary and disposition

Fresh safe Cubical Agda checking passed. `OrdinaryYoneda.agda` proves, for an
explicit category C with set-valued homs and a set-valued contravariant presheaf F,

\[
\operatorname{Nat}(C(-,a),F)\simeq F(a).
\]

Object, hom and value universes are parameters. Neither finiteness nor inverses
are assumed. The category supplies identities, composition and their laws; the
presheaf supplies its action and functor laws. Reconstruction is derived, not
an input field.

The maps are evaluation at the identity and extension by the presheaf action:

\[
\alpha\longmapsto\alpha_a(1_a),\qquad
z\longmapsto\bigl(f:x\to a\longmapsto F(f)(z)\bigr).
\]

The inverse laws follow respectively from the presheaf identity law and
naturality of alpha. The formal source also checks naturality of evaluation in
both the presheaf and object arguments and contractibility of each evaluation
fiber. Specializing F to C(-,b) gives full faithfulness:

\[
\operatorname{Nat}(C(-,a),C(-,b))\simeq C(a,b).
\]

The representable embedding's componentwise identity and composition laws are
checked. This is hom-wise recovery, not reconstruction of arbitrary raw object
labels or a derivation of category axioms from channel counts.

`NativeYoneda.agda` specializes to universe zero and uses actual native Pi,
Sigma, maps, retention, comparison and path constructors. It retains the raw
components together with their naturality witness and packages the reconstructed
value and inverse-law witness. The six frozen core files from the Stone pilot
remain byte-identical. No new core primitive is introduced.

## Governing falsification

- Problem: relational encoding does not itself recover transformations.
- Conjecture: evaluation at identity recovers precisely the natural families,
  also when arrows are not invertible, within the supplied categorical interface.
- Rivals: invertibility is secretly required; equality at identity suffices
  without naturality; contravariant and covariant composition are interchangeable.
- Risky consequences: a category with an absorbing noninvertible arrow must
  satisfy the theorem; nonnatural families can agree at identity and differ elsewhere.
- Strongest tests: the formal positive controls prove the latter counterexample
  and noninvertibility. `YonedaBadNaturality.agda` must fail specifically with
  `UnequalTerms`. An independent noncommutative four-arrow endofunction monoid
  enumerates all 256 raw families, exactly four of which are natural, and rejects
  reversed composition variance.
- Disposition: these tests and the general proof pass. What remains missing is
  a precise four-channel source structure and a proved construction of the
  categorical operations/laws from it. Supplying those laws is not deriving them.

## Relation to existing work

`research/nima/agda/RetainedActionYoneda.agda` already contains a covariant
set-action Yoneda construction over a retained groupoidal structure. The new
proof does not import it or assume invertibility. It isolates the ordinary
contravariant theorem and its integration with the native constructor interface.

The interrupted uniform Stone work in `../finite-stone/UNIFORM.md` and
`research/nima/checkers/uniform_finite_stone.py` remains an unverified draft;
no new finite Stone theorem was established by this work.

## Reproduction

```text
pwsh -NoProfile -File research/nima/checkers/check_ordinary_yoneda_kernel.ps1
python research/nima/checkers/check_ordinary_yoneda.py
python research/aspect/scc/scc.py check nima-ordinary-yoneda
```

Fresh proof execution: `structured_command_execution:e_16084_1791126012228848600_6`.
Audit: `structured_command_execution:e_16084_1791126104514785600_7`.
Receipts: `research/nima/results/ordinary-yoneda-kernel.json` and
`research/nima/results/ordinary-yoneda-audit.json`. The kernel receipt binds all
Agda inputs, the compiler and driver and rejects input drift. Active-process
state is in the ignored `.ai/tmp/scc-state/nima-ordinary-yoneda-run.json`.
No commit or push is authorized by these checks.
