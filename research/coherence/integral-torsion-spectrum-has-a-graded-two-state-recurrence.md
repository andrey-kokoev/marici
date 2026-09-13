# The integral torsion spectrum has a graded two-state recurrence

## Streaming path matching

For one prime \(p\), let the incoming gap edge have cost

\[
c=v_p(x).
\]

At matching grade \(k\), retain two boundary states:

\[
Z_k=\text{minimum cost with the latest edge absent},
\]

\[
O_k=\text{minimum cost with the latest edge selected}.
\]

Appending one edge updates them by

\[
Z_k'=\min(Z_k,O_k),
\]

\[
O_k'=Z_{k-1}+c.
\]

The first rule skips the new edge. The second selects it and therefore requires the previous edge to have been absent.

The Pfaffian-divisor valuation is

\[
v_p(D_k)=\min(Z_k,O_k).
\]

## Rank by grade

At each fixed matching grade \(k\), only two boundary states are needed. But the complete divisor spectrum contains all grades

\[
0\le k\le\lfloor n/2\rfloor.
\]

Hence its streaming state grows with configuration size:

```text
fixed grade k:       two-state tropical recurrence
all torsion grades:  graded family of growing total size
```

This is an arithmetic analogue of the contextual realization split: finite local transition width coexists with unbounded complete state dimension.

## Self-recursion

The update consumes one new gap and returns the same typed pair at every existing grade, plus one newly available top grade. It is therefore a genuine size-recursive residual:

```text
T_n = {(Z_k,O_k) : 0 <= k <= floor(n/2)}
T_n + new gap -> T_(n+1)
```

No dense matrix, minor enumeration, or integer gcd operation is required during streaming. Integer elementary divisors can be reconstructed afterward from the primewise differences

\[
v_p(d_k)=v_p(D_k)-v_p(D_{k-1}).
\]

## Boundary interpretation

The two states record whether the currently exposed boundary edge is available or occupied by the matching. They are a tropical incoming/outgoing interface for arithmetic torsion propagation.

Unlike the stationary hyperbolic double, this pair is replicated at every matching grade. Collapsing all grades to one pair would discard lower Smith factors while retaining at most one terminal Pfaffian statistic.

## Verification

```text
python research/coherence/check_streaming_tropical_torsion_recurrence.py
```

The checker compares the streaming recurrence with exhaustive path-matchings for 510 weighted paths through seventeen edges.

Artifacts:

- `check_streaming_tropical_torsion_recurrence.py`
- `streaming-tropical-torsion-recurrence.v1.json`
