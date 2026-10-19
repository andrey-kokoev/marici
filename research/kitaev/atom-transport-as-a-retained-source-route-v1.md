# Atom transport as a concrete retained source route

## Result

The current He-3, He-4 and Li-6 phase-assembly commands have been given an executable single-source retained-route adapter. It imports Strominger's actual constructors and phase maps, rather than recreating their geometries or substituting a new dynamics model.

This supplies a concrete ancestry comparison with `SingleSourceRouteCompiler.agda` and `RetainedTransportResolution.agda`: one input, typed successive comparisons, computed target, retained witness/history, and recoverable source payload. It is an executable specialization of that interface pattern, not a newly compiled Agda instantiation. It does not identify the atom carrier with the separate137-record numerical T9 fixture.

## Actual object and commands

At a chart c and absolute origin n, take a five-complex-coordinate fiber V_(c,n), with its declared geometric aliases and phase occurrences. A command e has a witnessed source and target and acts by

    V_(c,n) -> V_(c',n+delta_e), x -> P_e x.

The existing permutations, in pullback-array convention, are:

| Command | Permutation | Origin change |
|---|---|---:|
| PN / inverse-PN | [3,1,2,0,4] |0|
| NE | [0,4,2,3,1] |0|
| Proton reader advance | [2,3,0,1,4] |1|
| Neutron reader / NN advance | [0,3,4,1,2] |1|

The route packet retains its source, all command indices, actual frames and witnesses, computed intermediate values, terminal origin and complete coefficient permutation. There is no independent intermediate seed. Typed composition is concatenation with matching source chart; the origin advances as supplied by the actual command.

For every existing certificate route, direct application and split-route composition agree. Inverse coefficient maps recover the initial payload, but do not undo its realization history. A native PN/inverse-PN backtrack and the empty route have equal endpoint values and origins while remaining distinct retained histories.

This is the concrete sense in which the atom transport is a small instance of earlier retained transport. Its five numerical coefficients are not the entire mathematical state.

## Connection-like transport is already present

A passive local frame change g_(c,n) transforms each command by

    P'_e = g_target P_e g_source^(-1).

Consequently a composite has the endpoint covariance

    P'_route = g_end P_route g_start^(-1).

The intermediate frame changes cancel by composition. The checker tests this on all56 certificate routes using varying local permutation frames, with unchanged command histories and phase origins. The general cancellation is the elementary composition identity above.

This gives an explicit discrete parallel-transport/associated-fiber comparison relevant to the gauge-theory ancestry question. Local changes of coefficient basis are not, by this calculation alone, a selection of a physical gauge group or a Yang–Mills action. The constructive point is that connection-style composition and full witness retention are available now, not absent until a continuum field theory is built.

## Do not force the old S4 coefficient model onto these commands

After forgetting charts and histories, the four five-slot permutations generate all120 permutations of five slots, S5. A concrete generated five-cycle is[2,0,3,4,1]. Therefore these four unrestricted coefficient maps cannot all be the image of one fixed S4 action alone: S4 has order24 and no element of order5.

This is a statement about the UNRESTRICTED coefficient skeleton. Actual atom routes obey chart/phase restrictions; their realization histories are not quotiented by this finite group. It neither identifies S5 as a physical gauge group nor excludes a richer higher construction, a chart-dependent representation, or a larger retained ancestor. It rules out only the shortcut of equating this skeleton with the old single S4-action model.

## A retained context is observable later

An actual He-4 route reaches neutron chart through commands[11,0], then performs neutron advance12. At that step, multiplying the outside coefficient(slot0) by-1 leaves all four immediate geometric coefficients unchanged and preserves the full coefficient norm. It is another invertible coefficient comparison, but violates the current model's explicit outside-context retention rule.

The actual typed continuation[9,17], inverse-PN followed by proton reader advance, brings this distinction into the active proton face. For the checker input[(1,2),(3,-4),(5,6),(-7,8),(9,-10)] in(real,imaginary) pairs, the active middle amplitude becomes(3,-4) versus(-3,4). The normalized common-character intensities are61/3 and5/3.

Thus the context is not dispensable bookkeeping. It carries information that a later native reader can expose. This is a useful operational instance of the retained-source argument already proved in the larger framework.

The sign rival is NOT admitted by the full current atom contract. This test does not show that the earlier iceberg fails to select its reference law; it identifies exactly which stronger source-level law must be followed when checking that selection. Generic equivalence/retention alone and the full source theory are not interchangeable.

## Verified coverage

Fresh Node execution passes:

-56 actual certificate routes, preserving chart, origin and coefficient action;
-271 route splits with identical computed terminal states;
-280 basis-route evaluations;
-20 current viewer carrier readouts;
-56 local-frame covariance routes;
-3 equal-effect/different-history controls;
-wrong-source rejection, the120-element coefficient closure, and the actual context-to-active discriminator.

The counts describe different overlapping checks, not independent scientific evidence. Owner source files and receipts were not modified. The result records hashes of the two formal interface sources and two immediate atom implementation sources, not the full transitive import closure.

Checker: `research/kitaev/checkers/check_atom_retained_transport_ancestry.mjs`.
Receipt: `research/kitaev/results/atom-retained-transport-ancestry-v1.json`.

## What to trace next

The next source comparison is the origin of the four command equivalences and the outside-context retention law in the prior structured constructors, using these actual fiber/route types. The existing generic compiler and tetrahedral completion must be reused, not requested again. The separate137-record T9 Hamiltonian and the scattering operators need explicit representation/operation maps before they can be identified with this atom carrier; the current S5 skeleton already prevents the simplest fixed-S4 identification.

For the Yang–Mills question, we now have a concrete connection-style atom transport to compare with the existing amplitude/CR and native contact-scattering branches. Recovering the conventional gauge dynamics is a subsequent operation/readout comparison, rather than an instruction to discard this retained structure and restart from our obstructed lattice route.
