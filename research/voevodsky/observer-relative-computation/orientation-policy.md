# Orientation is explicit admissibility data in this model

Fresh safe Cubical Agda --ignore-interfaces check passed for `agda/ObserverOrientationPolicy.agda`; log: `results/agda-orientation-policy.log`.

Two policies share the SAME static support and SAME semantic value-observer map:

- forward admits Run(c,d);
- backward admits Run(d,c), read as a comparison from c to d by path reversal.

Both policies are semantically sound. The concrete supplied-program→finished-result pair is admissible forward, not backward. The reversed pair is admissible backward, not forward. The backward policy is a relation on finite supplied histories, NOT an implementation of a reverse-execution search algorithm.

Agda proves there is no function of the common value-observer map that reconstructs both supplied policy choices correctly. A convention can of course choose forward; the theorem does not forbid choosing a policy. It shows the common semantic observation does not identify WHICH of these extra policies was supplied.

For a fixed policy and endpoint pair, a retained view consists of a support path, an actual admissible history, and a comparison equating that history's realization with the path. The earlier record construction gives a checked equivalence between these views and admissible histories, with both inverse laws. This is a lossless evidence-bearing representation; it is not a way to manufacture a history from a bare comparison or from a merely positive observer support.

## Interpretation

The example supports a precise version of direction-as-additional-structure: identical semantic observation is compatible with opposing admissibility readings. It does not establish that all physical direction is conventional, derive causality, or show an arbitrary operational system can be reversed.

The lossless record stores the entire history. It would be misleading to call this a minimal observer or an explanation of how a history can be discovered from less evidence.

## Next

Investigate policy-local reconstruction in the deterministic fragment: when can mere admissibility suffice to recover a history without retaining it explicitly? Prove the required uniqueness condition or exhibit an obstruction. Do not assume the origin-selection prohibition disappears just because the policy is fixed. This tests whether a smaller observer interface suffices under clearly stated computational hypotheses.
