# Actual continuation admission descends with the typed source corner

## Frozen contract

We test the existing six-event square-free source, using its independent source recorder in `certificates/verify_filtered_obstruction.py`. Histories are typed paths with binary retained marks. Their initial and terminal masks remain part of their type. A continuation appends unused events, each marked zero or one.

The recorder is the admission oracle for these validly encoded candidates: it rejects an event already present in the running mask. No certificate-availability or calibration-version condition appears in this source path admission rule.

## Exact test

The checker exhausts 125,248 admitted paths across all 729 typed corners, including identities and one-event paths. It queries all twelve possible one-event extensions of each path:

- 125,184 accepted extensions;
- 1,377,792 rejected repeated-event extensions.

At each corner, every path has exactly the same next-extension set: unused events times {0,1}. Matching extensions can therefore be chosen identically. Their updated endpoints agree. Induction gives identical admitted continuation languages and strictly compatible matching under concatenation.

A fresh run of the actual opposite-observer transport checker also independently reconstructs all 6,001 original source-action entries from the actual raw observer rows. Thus on the declared ideal-source domain, equality of observer values survives every admitted source action and their compositions. This is the algebraic descent clause of the conjecture.

## Actual collision

The actual hidden relation z=[1,0,3]-[0,1,3], with all marks zero, lies in corner (0,11) and has zero assembled observer column. Its two constituent paths are admitted by the recorder. Their common next events are exactly 2,4,5, with either retained mark. The recorder values also agree: both zero-mark paths record the constant unit, so their difference is an ideal element.

The matching continuation is the same event word on each path. The verified source action sends the zero observed difference to zero at every admitted extension. This is distinct from the earlier reversal witness, which exposed z after reversing into a different observer presentation.

## What this establishes

The typed algebraic continuation clause passes. Endpoint types retain all admission information in this source grammar, and contextual observer closure retains equality of extension effects on the ideal-source domain.

The assembled O3 presentation is defined on ideal-source elements. We do not infer an unrestricted physical-history observer from it. Comparing individual paths through their difference is justified only where that difference belongs to the declared domain, as in the explicit collision.

The stronger DPC also mentions evidence dependencies. Those are not specified as additional continuation guards in this source grammar. The separate signed-certificate ledger supplies a different evidence-state system, but an authoritative coupling of its states to these source paths has not been constructed. Consequently the full evidence-dependent claim is not yet a frozen testable contract. This run establishes neither a counterexample nor closure of that stronger clause.

## Reproduction

    python research/voevodsky/checkers/check_actual_continuation_admission.py

Artifact: `results/actual-continuation-admission.json`.

The checker freshly invokes the actual action-transport test, uses the existing exported source basis and collision certificate with matching presentation digests, and exhausts recorder admission directly. It does not rebuild the owning full presentation.
