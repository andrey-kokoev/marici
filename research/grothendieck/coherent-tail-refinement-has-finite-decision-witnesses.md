# Coherent tail refinement has finite decision witnesses

## Scope and disposition

The DPC is proved for nested closed refinements of the compact,
uniformly tail-dominated carrier defined in
`witness-or-separator-for-dominated-tail-carriers.md`.
Its persistent-frame implementation passes exact constructive controls.

This is not a new actual-prime midpoint certificate. The runnable frames
use a declared rational bounded-sequence carrier, not an adapter admitting
arbitrary analytical evidence into the actual source task. The general
proof identifies the obligations such an adapter must preserve.

## Finite-prefix theorem

Let A_0 be compact and F continuous, with a common uniform absolute tail
bound. Accept closed evidence frames E_j on the SAME variables and retain

    A_k = A_0 intersect E_1 intersect ... intersect E_k.

1. If every A_k is nonempty, their nested intersection is nonempty. One
   measure satisfies the entire accepted sequence; separate witnesses are
   not being switched between obligations.
2. If the intersection is empty, compactness implies A_k is empty for some
   finite k. This is evidence inconsistency, not source infeasibility.
3. If the intersection is nonempty and its minimum exceeds theta by delta>0,
   some finite prefix already has minimum greater than theta+delta/2.
   Otherwise the nested compact sets A_k intersect {F<=theta+delta/2}
   would all be nonempty and have a common point, a contradiction.

If each frame is finite-supported linear evidence, choose a variable horizon
containing the first k frames and large enough that the uniform tail error
is less than the remaining positive margin. The owning base carrier's
finite-to-infinite extension property then supplies the finite primal/dual
sandwich. A finite LP dual plus that tail error certifies the decision.
Finite inconsistent prefixes have finite infeasibility certificates under
the same extension property.

Closedness alone proves the finite-prefix statement; it does NOT by itself
make a prefix an effectively representable finite LP. Finite-supported
linear frames are an additional implementation assumption here.

## Implemented retained state

The state retains its context and ALL prior finite-support rational frames.
Each frame names its predecessor digest and uses the same coordinate system.
Append validates context, lineage and syntax. A contradictory conjunction is
retained and classified rather than silently replaced by the latest frame.

The implementation does not carry a selected optimizer as its live source.
It compiles the retained feasible set at the maximum referenced coordinate,
then emits a checked primal/dual packet or a Farkas packet. Hashes bind the
submitted chain; they do not authenticate frame truth or prove that an
unreported earlier frame never existed. Faithful retention and sound admission
remain explicit assumptions.

The exact test carrier is 0<=x_n<=1 with objective -sum 2^-n x_n. Its uniform
tail error is 2^-m. All retained frames reference coordinates through m;
setting every later x_n=1 is a coherent infinite extension attaining the
negative geometric tail. Thus each finite packet has an exact infinite
primal as well as a dual lower certificate.

## Decisive controls

### Finite separation

Freeze theta=-3/8. The initial minimum is -1. Accept x_1<=0, yielding minimum
-1/2. Accept x_2<=0 as well, yielding minimum -1/4>theta. One retained prefix
and its exact dual certificate now universally separate the threshold.
Reversing these two frames yields the same feasible set and extremum, though
not the same lineage digest.

### Separate admission does not compose

The frames x_1<=0 and -x_1<=-1 are separately feasible. Their persistent
conjunction is inconsistent. A nonnegative Farkas combination has A^T y>=0
and b.y<0, contradicting any x>=0 with Ax<=b. The independent verifier checks
this finite contradiction; no solver status is treated as proof.

During development, the optimizer returned an invalid primal candidate for
this degenerate inconsistent case. Exact feasibility checks caught it, and
the engine required a separately checked Farkas packet before classifying
inconsistency. This is why numerical or symbolic solver returns do not serve
as admission authority.

### A minimizer is not a committed source witness

With x_1+x_2<=1, the minimizing first coordinate is x_1=1. Adding x_1<=0 keeps
the joint carrier nonempty but changes the optimizer to x_1=0. This is valid
refinement of a possibility set. It would be invalid to claim that a previously
committed actual x_1=1 had evolved to zero under a static evidence update.
Coherence belongs to the accumulated constraints, not to arbitrary choices
made by the optimization routine.

### Horizon enlargement

A later lower constraint x_17>=1 forces compilation to include coordinate
17. Its previously unrepresented value is no longer handled merely by a
truncation default. The whole accumulated conjunction is recompiled, and
its infinite extension is checked.

### Exact-threshold boundary

Accept x_n<=0 successively for every n. The limiting carrier is the single
zero sequence, whose objective is 0. Every finite prefix still has minimum
-2^-m<0. Thus even non-strict threshold validity at the limit need not have
a finite witness without a positive separation margin. The general claim
is proved by the explicit infinite schedule; eight finite prefixes are
checked as implementation controls, not as proof by extrapolation.

## What this adds to the structural synthesis

There are now three independently justified mechanisms:

- Joint admission prevents incompatible local summaries from being assembled.
- Persistent refinement prevents silent replacement of witnesses between
  accumulated obligations.
- Compactness and uniform tail control turn a positive limiting decision
  margin into a finite evidence prefix and finite certificate.

The third does not follow just from relational composition. It is a
closure/continuity result with concrete hypotheses. Nor does it provide
truthful selection of the actual source or authority for a physical action.

## Reproduction

    uv run --with sympy python research/grothendieck/checkers/construct_coherent_tail_refinement.py
    python research/grothendieck/checkers/verify_coherent_tail_refinement.py

Files:

- `checkers/coherent_tail_refinement.py`: retained-frame implementation;
- `results/coherent-tail-refinement-contract.json`: frozen control scenarios;
- `results/coherent-tail-refinement.json`: persistent states and certificates.

The verifier imports neither the producer nor the optimizer. It reconstructs
constraints and chain digests, checks exact primal/dual and Farkas identities,
checks infinite geometric tails and monotonic refinement, and rejects
corrupted contradiction packets and reset-frame histories. Foreign-context
and stale-parent frames are also rejected by the producer tests.

These checks corroborate the representation/update mechanism on the frozen
control family. A prime-calibration evidence adapter, independent proof-frame
admission, authenticated retention and computational bounds for large real
tail problems remain separate obligations.
