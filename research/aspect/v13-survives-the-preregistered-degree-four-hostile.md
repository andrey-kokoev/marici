# v13 survives the preregistered degree-four hostile

## Attack

Freeze a source Postnikov profile only through degree three. After replay begins, present the normalized degree-four cocycle on (\mathbb Z_2)

\[
\omega_4(a,b,c,d)=(-1)^{abcd}.
\]

The checker exhausts its full degree-four cocycle equation and confirms the nontrivial value at ((1,1,1,1)).

## Result

v13 does not add a degree-four cell. It rejects the packet at the preregistered typing boundary.

That is the required result. Automatically adding a filler would make the higher-coherence signature vacuous; accepting the packet while ignoring the class would make it blind. Rejection preserves both falsifiability and source authority.

## Present stopping point

The current hostile does not falsify v13. This is a local frozen-signature result, not a proof that v13 is universal. The construction/falsification loop terminates under the operator's rule because the attempted falsification failed.

## Verification

```text
uv run python research/aspect/checkers/check_v13_anti_vacuity_hostile.py
```
