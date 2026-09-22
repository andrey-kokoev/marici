# The assembled source observer and continuation profiles are incomparable

## Frozen critical-path DPC

On the independently specified 638-state coupled protocol, test whether equality of the owning current observer is exactly equality of continuation profiles. The current observer here is the protocol's existing `current_key`: typed corner, authoritative recorder, and assembled row signature. It is not an unrestricted numerical O3 evaluation on individual paths.

Continuations are all finite words in the original sixteen labels. A word with a rejected prefix has profile value bottom; an admitted word returns the typed corner, received value or absence, and issued value or absence. The empty word observes the current output.

The source/evidence verifier is freshly run. A deterministic partition fixed point computes equality of profiles for every finite word, and each equal class is checked for equal outputs and equal accepted successors. There are 62 profile classes. Exported formal observer signatures give 67 current classes and 461 evidence-enriched classes; these counts alone are not claims about exact numerical ranks or independence of analytical parameters.

## Falsification: missing continuation distinction

Two reachable histories have the same source word [0,1], zero marks, identical typed corner and identical assembled source observation. One has no acquired producer evidence; the other has producer value 1. Both have received and issued values absent.

The continuation `acquire` is admitted in the first and rejected in the second. Equivalently, `deliver` is unavailable in the first and available in the second. Thus equal source observations have different continuation profiles, even with the same immediate operational output.

The source-only observer cannot represent the independently declared acquisition history. This is an actual coupling distinction, not a formal-coefficient nonvanishing inference.

## Falsification: retained source distinction invisible to this continuation language

Take source word [0,1,3,2] with producer, received and issued values all equal to 1. Compare zero marks with marks [0,0,0,1]. Their exact source recorder polynomials differ: the former is the unit, while the latter records the last vertex-potential difference. Nevertheless they belong to the same full continuation-profile class.

The current observer, and also its evidence-enriched version, retain this source distinction. The frozen continuation language and outputs do not expose it. This is an independently checked recorder difference, so the redundancy conclusion does not rely merely on different formal row strings.

## Disposition

The critical-path biconditional is refuted for this independently fixed observer and protocol. The failure occurs in both directions: source observation omits evidence history relevant to continuations, and retains source distinctions irrelevant to these continuations.

The existing evidence-enriched observer is sufficient for all continuation profiles, but is not minimal. The 62-state profile observer represents the independently frozen continuation behavior exactly; it is constructed from that behavior, so its exactness is a representation theorem rather than corroboration of the original observer conjecture.

Structurally, source equivalence and continuation equivalence define crossing partitions. Adding evidence gives a sufficient common refinement, then quotienting by future behavior yields the continuation observer. History–possibility reciprocity therefore depends on matching the source representation with the chosen continuation structure; one does not automatically present the other.

## Reproduction

    python research/voevodsky/checkers/check_observer_continuation_profile_dpc.py

Artifacts:

- `results/observer-continuation-profile-contract.json`
- `results/observer-continuation-profile-dpc.json`
