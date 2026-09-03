# Radial R-zeta source adequacy against the mixed-completion theorem

## Question

Do the current radial source materials satisfy the acceptance hypotheses for the unbounded closed-form mixed bridge?

## Claim boundary

This packet compares materialized source claims with the sufficient theorem in `semibounded-form-mixed-completion.md`. It does not construct missing radial data or treat a desired identity as its own derivation.

## Acceptance matrix

The completion theorem requires six independently sourced fields:

| Required field | Current source status | Consequence |
| --- | --- | --- |
| common invariant form core | absent | domains cannot be compared |
| independently derived intertwiner \(R_\zeta\) | absent | no mixed bridge map exists |
| factorization \(CR_\zeta=B\) on that core | proposed shape only | equality cannot be tested |
| coercive pivot form | unverified | Schur reduction may be unbounded |
| strict relative cross bound below one | unverified | closed positive Schur form does not follow |
| closure, radical, and dense-range identification | unverified | quotient completion is not identified |

The first missing typed object is the pair consisting of an independently derived common core and intertwiner. All later tests depend on that object but remain logically distinct.

## Why finite and synthetic evidence do not fill the gap

Finite Green positivity supplies neither the radial form domain nor \(R_\zeta\). The synthetic weighted-\(\ell^2\) realization proves that the acceptance theorem is nonempty, but it has no source-derived map to the radial construction. Defining \(R_\zeta\), \(B\), or \(C\) to force \(CR_\zeta=B\) would insert the target assertion as an assumption.

Three countermodels from the prior typing audit remain active:

1. equality on a dense algebraic core need not identify closed domains;
2. positive finite stages may acquire a completed radical;
3. injective dense-range maps may have reduced minimum modulus zero.

## Disposition

The radial source is not adequate for admission into the unbounded mixed-bridge realization. This is an authority blocker, not a falsification of the proposed radial identity. The branch reopens only when a source-derived common core and intertwiner are materialized, together with independently defined \(B\) and \(C\). No successor waiting leaf is created.

The abstract coherence-pyramid programme has reached its demonstrated boundary: finite, bounded, and synthetic unbounded realizations exist under explicit certificates; the claimed radial realization does not yet exist.

## Verification

- `research/voevodsky/checkers/check_r_zeta_source_adequacy.py`
- `research/voevodsky/results/r_zeta_source_adequacy.json`
- `research/voevodsky/unbounded-r-zeta-identity-typing-audit.md`
- `research/voevodsky/semibounded-form-mixed-completion.md`
