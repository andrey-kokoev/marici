# Neighboring plus-cap Hall charts stabilize under cutoff extension

Start from the preferred consecutive-depth basis consisting of the minus spine
and finite plus cap. Construct its first neighboring chart by:

1. choosing the least omitted plus depth;
2. exchanging it with the nearest retained plus depth that preserves maximal
   rank;
3. leaving every minus-spine column fixed.

This exchange preserves branch orientation and differs only inside the finite
plus cap. Across all 135 cases with

\[
2\le g\le10,
\qquad
1\le q\le15,
\]

the exchange pair and exact forward transition bound were identical at
cutoffs \(N=15\) and \(N=20\).

Representative stabilized transitions are:

| \((g,q)\) | exchanged depths | forward max | inverse max |
|---|---|---:|---:|
| \((6,3)\) | \(9\leftrightarrow10\) | \(1287/64\) | \(143/4\) |
| \((6,8)\) | \(4\leftrightarrow5\) | \(5/9\) | \(9/4\) |
| \((6,13)\) | \(8\leftrightarrow9\) | \(32/21\) | \(20/7\) |
| \((3,10)\) | \(8\leftrightarrow9\) | \(8/3\) | \(3/4\) |

The exchange in \((6,3)\) first becomes available after depth 9; from cutoff
12 onward its coefficients remain literally constant.

This contrasts with the hostile global plus-first/minus-first change, whose
coefficients grow rapidly with cutoff. The evidence therefore supports a
completion-safe local atlas:

- authorized charts differ by finite cap exchanges;
- transition matrices become constant after the cap enters the cutoff;
- global branch reordering is outside the uniformly controlled atlas.

The result is bounded discovery evidence. The theorem still requires a
source-derived definition of authorized cap exchanges and proof that every
such exchange is supported in a cutoff-independent finite reflection window.
Graph-norm equivalence must then be derived from the source norm; stabilized
raw coefficient bounds are a necessary hostile gate, not the final topology.
