# Lakatos research-programme protocol

## Purpose

This protocol records the diachronic architecture of a Marici research
programme: which commitments are held fixed during a bounded programme, which
hypotheses may be revised, which moves are licensed or forbidden, and whether
a revision produced independently testable information.

It complements rather than replaces Popperian testing. A test evaluates a
claim. A Lakatos record evaluates a sequence of theory revisions relative to
its predecessor.

A hard core is a scoped methodological commitment or established constraint.
It is not certified truth, cannot overrule contrary evidence, and must carry a
reopening rule.

## Typed objects

Use these namespaced epistemic-graph kinds:

- `marici:research_programme`: versioned programme with owner, scope, and
  predecessor;
- `marici:hard_core`: commitments held fixed within that programme version;
- `marici:protective_belt`: explicitly revisable hypotheses;
- `marici:positive_heuristic`: source-admissible directions for constructing
  new tests;
- `marici:negative_heuristic`: prohibited or degenerating moves;
- `marici:problem_shift`: a revision from one programme version to another;
- `marici:programme_appraisal`: progressive, neutral, degenerating, or
  crisis assessment relative to a named predecessor.

Recommended namespaced relations are:

- `marici:has_hard_core`;
- `marici:has_protective_belt`;
- `marici:has_positive_heuristic`;
- `marici:has_negative_heuristic`;
- `marici:successor_programme`;
- `marici:adjusts_belt`;
- `marici:threatens_core`;
- `marici:licenses_test`;
- `marici:forbids_reopening`;
- `marici:appraises_shift`.

The object payloads must state scope, assumptions, evidence boundary, owner,
version, and reopening or retirement conditions. Graph admission records the
programme architecture; it does not certify any mathematical claim.

## Version and appraisal discipline

Before a substantive belt adjustment, freeze:

1. the predecessor programme version;
2. the anomaly or new source input;
3. the predicted new support, map, rank, monodromy, period, or other typed
   effect;
4. the admissible test;
5. the result that would count against the adjustment.

A shift is **progressive** only when an independently motivated enlargement
predicts a new effect and the effect survives its declared test. It is
**neutral** when it improves typing or organization without new tested
content. It is **degenerating** when it adds post-hoc structure only to recover
a desired result, relocates a failed claim without a new source map, or
produces no new consequence beyond a restatement. It is a **crisis** when
evidence inside the exact declared scope contradicts the hard core and no
admissible belt adjustment absorbs the contradiction.

Outside-scope evidence modifies or extends the belt; it does not refute a
scoped theorem. Conversely, scope may not be narrowed after a failure unless
the narrowing was already source-defined or is recorded as a degenerating
shift.

## Hard-core reopening rule

“Protected” never means unfalsifiable. A hard core may be reopened only by:

- a contradiction inside its declared scope;
- failure of a theorem dependency or source normalization on which it rests;
- a source-derived comparison proving that two previously separated scopes
  are the same;
- an operator-authorized programme reset, recorded as a new version rather
  than a silent rewrite.

Every reopening must preserve the prior version and link the successor by an
explicit problem shift.

## Relation to the Carrier

This is a small governance Carrier for reasoning about research programmes.
Its entities, typed relations, legal transformations, residual anomalies, and
readout appraisals form a meta-level calculus applied to investigations of the
physical Carrier. The recursion is useful only while the governance calculus
remains weaker, inspectable, and falsifiable. It must not manufacture
scientific evidence or shield the object-level Carrier from tests.