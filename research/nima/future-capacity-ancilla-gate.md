# Future Capacity: Independent-Ancilla Gate

Total prospective Shannon entropy is not yet a viable dynamical objective.
Given any future tree, append an independent fair spectator bit.  The system's
dynamics and marginal future are unchanged, but

\[
H(Y,Z)=H(Y)+\log 2.
\]

A law maximizing total future entropy would systematically prefer the
creation or recording of irrelevant noise.  Repeating the construction makes
the score arbitrarily large.  This is the **spectator-noise catastrophe**.

The exact finite checker contrasts total entropy with connected information.
For a present variable \(X\), its future \(Y\), and an independent spectator
\(Z\),

\[
I(X;Y,Z)=I(X;Y).
\]

Thus the next surviving candidate is not the size of the whole future space,
but the size of the part related to the present operation:

\[
\boxed{
C_{\rm conn}(X\to Y)
=I(X;Y)
\quad\text{or, with controllable inputs,}\quad
\max_{p(X)}I(X;Y).
}
\]

The latter is ordinary channel capacity.  In Marici language it counts
future distinctions that the current port/operation can actually propagate,
while quotienting independent coefficient sectors.

This remains only a candidate.  It requires a source-defined joint state,
past/future effect algebras, and a canonical channel between them.  Choosing
those after seeing the answer would reproduce the same presentation problem
that falsified raw branch counting.

The Operator's intuition therefore survives in a narrower form:

> Development may favor operations preserving the greatest invariant space
> of causally accessible future distinctions—not the greatest total number of
> future events.

Certificate:
`research/nima/checkers/check_future_capacity_ancilla_gate.py`
