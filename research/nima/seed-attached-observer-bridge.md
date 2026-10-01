# Actual seed instantiated in the retained attached-observer construction

## Construction

`agda/SeedAttachedObserver.agda` imports the actual `ObserverCoherenceCube.FromSource` constructor. It uses the four vertices as I and the actual outgoing seed fibers as J:

    Out A = {AB,AD}, Out B = {BC,BA}, Out C = {CA}, Out D = {DB}.

K, L and B are unit families in this first adapter. Hence source X is, up to these contractible decorations, the four source sections of the actual seed. This is an explicit minimal adapter choice, not a derivation that all packet information is exhausted by a selected section. Target endpoints are defined for all six constructors; the generic coherence laws do not impose a dynamical law on them.

Two source values are constructed:

- cycle: AD, BC, CA, DB (the unique cycle-cover routing);
- other: AB, BC, CA, DB (a different source section).

For every q the module constructs its canonical full traces and an actual attachment witness using `diagonal-attaches`. It passes the two attached observers into the imported `nextAttachedQ`, producing a `Whole.Universe.Complete` value. The imported recovery law proves that both attached observers, including their witness data, survive in the successor.

## Attachment scope: a proved distinction

The new theorem `attachment-implies-source-equality` proves for arbitrary canonical traces u,v in this adapter:

    Attach(u,v) -> source(u)=source(v).

The proof uses the actual inverse of routeA and the actual comparison of routeA with routeB. Thus an attached observer aligns two presentations of the same source value. It does not permit arbitrary unequal section values to be attached just because their routes have the same types.

But `nextAttachedQ` takes a PAIR of such attached observers. Its record retains each observer's internal attachment and a presentation square. It does not demand a cross-attachment between the sources of those two observers. Accordingly the constructed successor can contain the two explicitly different source sections above.

This yields a retained two-observer package, not yet a coupled pair of physical bodies. An interaction between its two components must be supplied by an additional source-derived comparison or boundary condition; the internal attachment theorem must not be misreported as that coupling.

## What is now connected and what is not

Connected: actual seed fibers -> supplied source sections -> canonical retained traces -> proved attachments -> the existing nextAttachedQ constructor -> a complete package with recovery.

Not yet connected: this package's native-table encoding and derivation under an explicit admission policy; the intended horizontal rung transport; a rung4 physical observation; a cross-observer dynamical interaction. The existing generic native-table equivalence is relevant but this module does not instantiate that bridge or assign rung numbers to its internal stages.

No free enumeration of billions of section contexts is required to construct this particular supplied successor. Conversely, selecting two source sections does not prove that every other section context is physically redundant or may be pruned.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedAttachedObserver -Fresh

Fresh headless safe Cubical compilation passed, including imported source dependencies. Receipt: `results/agda-SeedAttachedObserver.json`. This checks the formal construction and theorem, not a particle identification or physical prediction.
