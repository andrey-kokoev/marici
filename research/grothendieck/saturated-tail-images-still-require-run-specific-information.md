# Saturated tail images still require run-specific information

## Result

On the owning two-moment tail family, there are 2^H distinct fiber-saturated
refinement carriers with the same source model, optimizer, minimum and positive
objective certificate. Their declared observable queries require exactly H
run-specific bits in the frozen refinement grammar.

This complements `research/voevodsky/fiber-saturation-locates-the-exact-storage-obstruction.md`.
That result locates information lost INSIDE an unchanged visible fiber.
Here no such hidden restriction exists. The information resides in which
VISIBLE possibility image remains after accepted evidence.

Saturation supplies recoverability from the image; it does not bound the
information needed to represent that image.

## Owning source and shared data

Fix one of the admitted atom-box faces from
`two-moment-tail-images-have-unbounded-exact-facet-complexity.md`:

    P_m = product_j [0,100+2j],
    L(t)=(U,V)=sum_j t_j*(1,2^-7j).

Its two-dimensional image Z_m has exactly 2m exposed vertices and edges.
The owning all-m admission proof establishes that these are normalized faces
of the bounded-atom Chebyshev relaxation. They are not actual prime-realizable
uncertainty sets.

Shared information, fixed before the run-specific refinements, consists of
P_m, L, an indexed cut library and an exact reconstruction/query algorithm.
Their descriptions and coefficients count as shared model/verification data.
No per-run special program or uncounted evidence journal is allowed.

## Independently constructed observable cuts

The all-upper-atom source t_j=100+2j uniquely maximizes V because every slope
is positive. Reserve its image v_* as a common optimizer for G=-V.

For each other original polygon vertex v_i, add its two incident outward
facet normals to obtain a functional a_i uniquely maximized there. Let

    peak_i=a_i.v_i,
    other_i=max_(v!=v_i) a_i.v,
    d_i=(peak_i+other_i)/2.

The cut H_i={z:a_i.z<=d_i} excludes v_i but strictly retains every other
original vertex, including v_*. Choose any H<=2m-1 such cuts before exploring
refinement states.

For a retained index set J define

    Q_J=Z_m intersect intersection_(i in J) H_i,
    C_J=P_m intersect L^-1(Q_J).

Every carrier is nonempty, has the same all-upper source optimizer, and is
fiber-saturated by construction. Every accepted frame is an old-observable
halfspace, so no hidden inside-fiber evidence is introduced.

## One current certificate for every run

Every C_J has exactly the same minimum

    min G=-Vmax,       Vmax=sum_j (100+2j)2^-7j.

The atom caps give the common certificate G>=-Vmax. The reserved optimizer
attains it in every carrier. The frozen control threshold is -2Vmax, giving
a positive margin in every case.

This task is the normalized signed-kernel objective on the admitted face,
not the separately frozen full-prime midpoint task. No midpoint improvement
or source-infeasibility verdict follows.

## Exact distinguishing queries

Use the read-only feasibility query L(t)=v_i, encoded by four rational closed
halfspaces. It is feasible in C_J exactly when i is absent from J.

- If absent, the original vertex's exported atom-box lift satisfies every
  retained cut and is an explicit source witness.
- If present, its own cut contradicts that point equality. Adding the
  appropriate nonnegative multiples of the point-equality directions gives
  a Farkas contradiction with rhs d_i-a_i.v_i<0.

Thus the visible images Q_J are all different. Each difference has an
owning-source feasibility or contradiction certificate. The common optimizer
cannot replace the possibility set, despite saturation.

## Representation-or-obstruction contract

An H-bit membership mask is sufficient. Decode J and reconstruct Q_J from
the shared source and cut library. This supports arbitrary later read-only
rational halfspace feasibility queries in the two observables, not only the
named singleton probes. Repeated frames and their order may be forgotten.

Conversely, there are 2^H distinct answer functions. An exact deterministic
interface needs at least H history-dependent bits. A smaller budget must be
refused. This includes any varying hash, specialized code or external journal
used to recover J.

The exported audit polygons, source lifts and query tables occupy much more
than H bits. They certify the construction; they are NOT counted as an H-bit
runtime implementation. The claimed runtime state is only the membership
mask plus access to the shared model/library/algorithm. There is no bound
on query time from this storage statement.

For every H one can take m with 2m-1>=H. This is a family theorem, not an
assertion that a fixed finite m supplies arbitrarily many original vertices.
The ambient analytical relaxation is fixed; the selected finite-support
face and its shared cut library are declared before each family's histories.

## Exact verification

The finite workload freezes (m,H)=(2,3),(3,5),(4,7),(8,8). It checks:

- 424 admitted saturated refinement carriers;
- 3,128 exact primal/Farkas query answers;
- 41,292 pairwise separating-query instances;
- common optimizer and strict certificate throughout;
- exact source-lifted polygons for every refinement;
- refusal of H-1 bits and sufficiency of H bits.

The producer freshly replays the owning independent tail-face verifier.
The new independent verifier imports neither the producer nor a clipping
algorithm or optimizer. It reconstructs the arrangement of source and cut
lines, selects the exact vertices for every retained mask, checks all source
lifts, and verifies every query answer and counting obstruction.

Source-image equality plus the observable-only frame grammar proves saturation;
a vertex lift alone would not. The arbitrary-H argument follows from the
exposed-vertex construction and the separating membership queries, rather
than extrapolating finite counts.

## Structural synthesis: two independent storage locations

A complete source model and an image Q can reconstruct a carrier exactly at
fixed points of fiber saturation. That eliminates the need to retain extra
restrictions INSIDE each visible fiber. It does not eliminate the need to
retain Q itself.

Accordingly, a representation contract must distinguish:

1. shared source/model structure;
2. run-specific visible-image restrictions;
3. run-specific hidden fiber restrictions, if saturation is not maintained.

The source model does not determine which accepted visible cuts describe the
run, just as it does not determine which hidden subfamily was retained in an
unsaturated run. Both can have the same current numerical decision.

This is not a new physical acquisition or authentication result. Frame truth
and faithful retention remain assumptions. It is a source-bound separation
of reconstructible structure from evidence-dependent information.

## Reproduction

    uv run --with python-flint python research/grothendieck/checkers/construct_saturated_tail_refinement_storage.py
    python research/grothendieck/checkers/verify_saturated_tail_refinement_storage.py

Contract: `results/saturated-tail-refinement-storage-contract.json`.
Audit packet: `results/saturated-tail-refinement-storage.json.gz`.
