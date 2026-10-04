# A Cubical Agda inhabitant of the retained-comparison candidate

## Question

Does the minimal table of presentations, comparisons, retained changes and realization admit an inhabitant with distinct changes that have the same realization?

The operator requested formalization and existence before comparison with the previous Marici constructors. SCC obligations: forward realization and route/coherencer compatibility.

## Record and proof

`agda/RetainedComparisonStructure.agda` defines `Structure` with:

- object type P;
- comparison types K(p,q), identities, composition, unit and associativity paths;
- change types E(p,q), identities, composition, inverses, unit, associativity and inverse paths;
- realization j:E(p,q) -> K(p,q), with identity and composition preservation paths.

The proof fields are retained. There are no postulates or unsolved holes. The module uses safe Cubical Agda. The record is universe-parameterized and does not require hom-types to be sets. It specifies the listed laws as paths, not an additional infinite tower of coherence cells.

Transport is derived as j(d) composed with a composed with j(e inverse), with a fixed parenthesization. The two generic `realized-inverse` lemmas prove that j carries change inverses to comparison inverses.

The term `example : Structure lzero` is the existence witness, not a sampled test of existence. It supplies:

- P = Bool;
- K(p,q) = Bool for each ordered pair;
- E(p,q) = Bool x Bool for each ordered pair;
- XOR composition, componentwise in E;
- false identities, self-inverse changes, and j = first projection.

All record laws are proved by Boolean elimination and componentwise paths. Two objects and two comparisons in every hom-type remain distinct.

For the same ordered endpoints, `change0 = (false,false)` and `change1 = (false,true)` are provably distinct, while their realizations are equal by reflexivity. `no-recovery` proves that no function K(false,true) -> E(false,true) is a left inverse to realization on all changes. Their induced transports also agree, while the changes themselves remain distinct. This directly witnesses the need to retain change data separately from its realized action.

## Falsification and disposition

The rival claim is that retaining only the realized invertible comparison recovers every change. The positive module refutes this by `no-recovery`. The negative module `agda/negative/RetainedComparisonBadErasure.agda` separately attempts to identify the two changes by reflexivity and must fail with the false/true unequal-term diagnostic.

A fresh headless compilation and this rejection control pass. The result establishes an inhabitant of the candidate record. A universal property, a comparison with the earlier recursive-table representation, and the separate graph/fold/unfold structure are not part of this record.

Reproduction:

```powershell
pwsh -NoProfile -File research/nima/checkers/check_retained_comparison.ps1
```

The runner starts the existing Agda 2.8.0 executable with `-NoNewWindow` and redirected output because PowerShell's pipeline invocation classified that executable as a document in the admitted execution environment. Omitting `-NoNewWindow` opened a Windows Terminal tab and stole operator focus; this was corrected. `-VersionOnly` tests the headless launch without compilation. It records compiler, owner-source and Cubical-library hashes, verifies that they remain stable during checking, and uses `--ignore-interfaces` for the positive root. No external tool or dependency was installed.

Receipt: `results/retained-comparison-formal-audit.json`.
Logs: `results/agda-RetainedComparisonStructure.log` and `results/agda-RetainedComparisonBadErasure.log`.

## First redundancy proof

`agda/RetainedComparisonReduction.agda` derives the right-unit and right-inverse laws using only change composition, associativity, left units, and chosen left inverses. Its input signature excludes both right-hand laws. The proof first derives left cancellation, then right units, involutivity of inversion, and right inverses.

This reduces the independent law requirements, not automatically the retained proof data. For set-valued change homs, the module proves that the supplied right-unit and right-inverse witnesses equal the derived witnesses. It checks this recovery for the original Boolean-product inhabitant. Set-valued homs still retain its distinct changes; they identify proofs of equalities, not different arrows. The unrestricted record has not been changed or silently truncated.

Fresh reduction check: `pwsh -NoProfile -File research/nima/checkers/check_retained_comparison.ps1 -Module RetainedComparisonReduction`.
Source-bound receipt check: `python research/nima/checkers/check_retained_comparison.py --reduction`.
Receipt: `results/retained-comparison-reduction-formal-audit.json`.
