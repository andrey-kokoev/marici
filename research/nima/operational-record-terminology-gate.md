# Operational Record Terminology Gate

## Rule

`Outcome` is not a primitive Marici object.  It commonly conflates four
different types:

\[
\begin{array}{ll}
e\in\operatorname{Ext}(h) & \text{lawful extension},\\
B\subset X & \text{presentation branch},\\
(\rho,E)\mapsto\operatorname{Tr}(\rho E) & \text{effect value},\\
r:S\times E\to\mathcal R & \text{physical record map}.
\end{array}
\]

None of the first three alone asserts that one future became uniquely actual.
The fourth produces an operational record only after its source, effect,
positive pairing, and record support have been typed.

Accordingly:

\[
\boxed{
\text{operational record}
=
\text{source}
+\text{admitted effect}
+\text{positive pairing}
+\text{record map}.
}
\]

## Consequences

1. A `FutureRef` addresses an extension object or a capability to construct
   one.  It does not reveal a selected future.
2. Born weights are effect values associated with possible records; calling
   them outcome probabilities adds no collapse or actuality theorem.
3. A mathematical branch may be presentation-dependent and need not define a
   physical alternative.
4. Selection, collapse, Everettian branching, and observer-relative record
   formation remain distinct conjectural mechanisms until comparison maps are
   supplied.
5. Existing historical wording is retained and corrected by explicit graph
   criticism or supersession rather than silent rewriting.

## Falsifier

Any use of `outcome` in a foundational claim must expand to the four-term
operational-record packet above.  If it cannot, replace it by `extension`,
`alternative`, `branch`, `event`, `record`, or `effect value`.  If no such type
is available, the asserted operation is not yet defined.
