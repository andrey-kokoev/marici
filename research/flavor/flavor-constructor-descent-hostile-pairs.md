# Constructor descent and hostile pairs (WP75, move 4/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Rule

A representative task descends only if `q(T(g.y))=q(T(y))` for every full
weak-basis action, including its apparatus record. Descent precedes image
testing: a proper chart locus has no selector meaning when it varies along a
physical orbit.

## Exact hostile pairs

The WP57 branches satisfy `pi10(x+)=pi10(x-)` while

\[
\operatorname{Tr}(H_uH_d)(x_+)-\operatorname{Tr}(H_uH_d)(x_-)
=9\sqrt{10}/250\ne0.
\]

Thus measured ten merges physically inequivalent points; the descending mixed
Gram word discriminates without selecting. Conversely, a generic weak-basis
rotation preserves the physical point and Gram invariants while destroying a
sparse texture and changing its loop phase. Chart preparation therefore fails
descent.

RG and Gram probes descend on `physical16`; threshold maps descend between
declared UV/IR quotients; component CP rules and texture permutations fail;
reference tasks descend only on `(X16 x R)/G_R`. The smallest projection
falsifier is the nonzero exact complement above. The smallest descent
falsifier is one same-orbit pair with unequal chart output.

Verification: `uv run --with sympy python
research/flavor/checkers/wp75_constructor_descent_hostile_pairs.py`.
