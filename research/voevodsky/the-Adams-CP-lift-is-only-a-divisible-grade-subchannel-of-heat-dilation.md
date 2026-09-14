# The Adams CP lift is only a divisible-grade subchannel of heat dilation

Adams grade raising

\[
k\longmapsto rk
\]

has a formal relation to heat dilation:

\[
e^{-t(rk\log p)^2}
=
e^{-r^2t(k\log p)^2}.
\]

This suggests identifying the Adams CP lift with heat transport \(t\mapsto r^2t\).

The identification fails at support level. Adams maps onto the proper closed subspace of grades divisible by \(r\). The full heat observer at time \(r^2t\) still sums over every original grade \(k\), including grades not divisible by \(r\) in the target labeling.

For doubling, the Adams image contains grades

\[
2,4,6,\ldots,
\]

while the full heat trace contains

\[
1,2,3,4,5,6,\ldots.
\]

The omitted odd-grade contribution is nonzero and cannot be removed by the Adams cocycle.

Therefore

\[
\text{Adams CP matrix coefficient}
\neq
H(r^2t)
\]

for the complete source heat observer.

The CP lift remains a valid positive coherent **subchannel**. To reconstruct full heat dilation, one would need all residue classes modulo \(r\), not only the divisible class, together with a positive coherent assembly of their returns. That enlargement must also include endpoint and gamma sectors.

Thus the current Adams construction does not cross the RH gate, but it suggests a sharper candidate: a complete polyphase decomposition of grade space into all congruence classes, whose CP branches jointly reconstruct heat transport.

## Verification

```text
python research/voevodsky/checkers/check_Adams_CP_heat_trace_crossing_no_go.py
```

Artifacts:

- `research/voevodsky/checkers/check_Adams_CP_heat_trace_crossing_no_go.py`
- `research/voevodsky/results/Adams_CP_heat_trace_crossing_no_go.json`
