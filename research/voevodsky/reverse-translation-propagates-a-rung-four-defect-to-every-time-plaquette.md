# Reverse translation propagates a rung-four defect to every time plaquette

Let \(U\) be translation along the main time axis. The source Weil kernel is stationary, so

\[
L((U^kp)^*U^kq)=L(p^*q).
\]

The reverse plane supplies \(U^{-1}\), making the transport bidirectional.

For every composite primitive \(p\), its rung-four Schwarz square is therefore translation invariant:

\[
S_L(U^kp)=S_L(p).
\]

In particular,

\[
\det S_L(U^kp)=\det S_L(p)
\]

for every positive or negative integer \(k\). Hence a negative rung-four reading at one time propagates unchanged to every earlier and later translated plaquette.

This validates the bidirectional persistence intuition at the level of complete rectangles.

It does not imply that the adjacent rung-three vertices become negative. The stationary hostile

\[
\begin{pmatrix}1&2\\2&1\end{pmatrix}
\]

has positive diagonal readings at every time and determinant \(-3\) at every plaquette. The negativity belongs to the joint correlation channel.

Nor does translation alone yield a contradiction: translating \(p\) changes its location but not its composite ancestry. A translated negative composite does not become an independently positive primitive base observation.

The remaining boundary theorem would have to show that every translated composite orbit intersects a class whose rung-four Schwarz positivity is source-proved. Without such an ancestry-reduction or positive boundary condition, bidirectional propagation produces a time-wide negative sheet rather than an inconsistency.

## Verification

```text
python research/voevodsky/checkers/check_bidirectional_translation_of_rung4_negativity.py
```

Artifacts:

- `research/voevodsky/checkers/check_bidirectional_translation_of_rung4_negativity.py`
- `research/voevodsky/results/bidirectional_translation_rung4_negativity.json`
