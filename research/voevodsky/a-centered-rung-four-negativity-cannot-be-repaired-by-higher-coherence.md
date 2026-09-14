# A centered rung-four negativity cannot be repaired by higher coherence

Let \(L_k\) be the source observer at stage \(k\), with source-preserving inclusions

\[
u_k:A_k\hookrightarrow A_{k+1}.
\]

Assume they preserve the unit, primitive reading, and square reading:

\[
L_{k+1}(\nu_kp)=L_k(p),
\qquad
L_{k+1}((\nu_kp)^*\nu_kp)=L_k(p^*p).
\]

Suppose a centered primitive satisfies

\[
L_k(p)=0,
\qquad
L_k(p^*p)<0.
\]

Then at every later rung,

\[
L_{k+r}(\nu p)=0,
\qquad
L_{k+r}((\nu p)^*\nu p)=L_k(p^*p)<0.
\]

Its rung-four Schwarz determinant is unchanged:

\[
\det S_{L_{k+r}}(\nu p)
=
L(1)L_k(p^*p)<0.
\]

Therefore no higher coherence filler can repair a genuine centered negative square while retaining source identity and restriction coherence.

The only apparent escapes are inadmissible for the RH comparison:

- change the observer value;
- quotient out the witness nonfaithfully;
- break successor restriction coherence.

Hence rung four is the terminal substantive positivity gate. Higher rungs can establish closure, presentation independence, and completion, but they cannot turn a negative rung-four observation positive.

This sharpens the proposed architecture:

> If the primitive and primitive-square readings exist coherently at adjacent stages, then RH requires their Schwarz square to be positive immediately. Failure cannot be deferred to a later correction.

The remaining proof obligation is exactly the coupled source inequality on centered primitives. It cannot be discharged by higher categorical coherence alone.

## Verification

```text
python research/voevodsky/checkers/check_centered_rung4_obstruction_persistence.py
```

Artifacts:

- `research/voevodsky/checkers/check_centered_rung4_obstruction_persistence.py`
- `research/voevodsky/results/centered_rung4_obstruction_persistence.json`
