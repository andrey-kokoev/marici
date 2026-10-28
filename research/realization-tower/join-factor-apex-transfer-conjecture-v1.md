# Join-factor apex transfer: a moving input–output division

## Combined picture

Operator-requested record of the proposed mechanism following the
[channel-trade test](channel-trade-test-v1.md).

The whole is retained while its input–output division moves. Write

    X = A * B,

with A the input factor and B the output factor. If the output factor is
presented as v * B', transfer the marked apex v:

    A * (v * B')  ->  (A * v) * B'.

This combines:

- taking the apex link on the output side, recovering B';
- coning the input factor at v;
- retaining the complete join, the selected vertex and the transfer history.

The precise proposed name is **join-factor apex transfer**. “Counter-coning”
is an informal description of the paired operations, not a new standard
simplicial operation.

## Exact simplicial identity

For disjoint vertex sets, augmented simplicial join is associative. Thus the
underlying complexes on the two sides have the same faces, while their marked
factor decompositions differ. For a fresh apex v,

    Lk_v(v * B') = B'.

If the factors are filled simplices with I and O vertices, respectively,

    Delta^(I-1) * Delta^(O-1) = Delta^(I+O-1).

Selecting one of the O output vertices and transferring its factor membership
therefore gives

    (I, O) -> (I+1, O-1).

This is reallocation of a marked vertex between factors, not ordinary coning
of the entire complex. It does not contradict the preceding test: ordinary
coning adds a vertex, whereas this operation retains the vertex and moves its
role.

## Proposed rung accounting

| Rung | Input elements | Output elements |
|---:|---:|---:|
| 12 | 3 | 12 |
| 11 | 4 | 11 |
| 10 | 5 | 10 |
| 9 | 6 | 9 |
| 8 | 7 | 8 |
| 7 | 8 | 7 |
| 6 | 9 | 6 |
| 5 | 10 | 5 |
| 4 | 11 | 4 |

In this candidate, I+O=15 throughout. Descent incorporates more elements into
the input structure and leaves fewer on the output side. Reverse traversal
moves the division back using the retained selection/history.

A specified vertex transfer has an inverse role transfer. The counts alone do
not select which vertex moved; without its identity/history there is no unique
reverse choice.

## Transfer is not quotient

No vertices or faces are identified or discarded by reassociating and
repartitioning the join. Consequently the transfer is not itself quotienting.
An observation or comparison interface may impose a separate equivalence;
that quotient and its location require their own definition.

## Relation to the actual tower

The exact identity above uses simplex VERTICES as counted elements. Fifteen
such vertices give a 14-simplex as the total join, not a four-dimensional
spatial simplex. No assertion that physical space has fourteen dimensions is
made: a channel/record complex could differ from its spatial realization.

The remaining bridge is to identify A, B, v and the fifteen elements with
actual lattice channels, their incidence and the WG operation. The tetrahedral
carrier's twelve directed edges and three local outgoing edges do not by
themselves supply fifteen distinct vertices or channels.

The existing tower diagram still has six object presentations and three
horizontal transport roles. This candidate serial accounting is recorded
alongside it; no identification with its nine numerical labels is assumed.

## Status and provenance

Recorded at the operator's explicit request after discussing counter-coning
and the combined input–output picture. The join/link equations are elementary
simplicial identities. Their proposed channel interpretation and assignment to
the Realization Tower are conjectural.

This note adds no new executed test or formal proof. The preceding channel
partition audit remains the executed result; it did not test this candidate's
binding to WG. No glossary version, proof verdict, graph task or source API is
changed here.
