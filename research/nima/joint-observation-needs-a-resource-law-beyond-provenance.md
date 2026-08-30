# Joint Observation Needs a Resource Law Beyond Provenance

## Question

Suppose two marginal observers are source-authorized and their records can be
matched to one preparation identity. When does that produce a jointly
executable observer?

## Static provenance layer

Let \(P\) be the carrier of source preparations, with marginal instruments

\[
I_E:P\to R_E,
\qquad
I_M:P\to R_M.
\]

If both record carriers retain their preparation map, compatible record pairs
form the pullback

\[
R_E\times_P R_M.
\]

This removes pairs assembled from different source occurrences. It is a static
incidence theorem. It does not construct a process producing a point of the
pullback.

## Operational layer

A primitive joint instrument is a source-authorized arrow

\[
J:P\to R_E\times_P R_M
\]

whose marginals recover \(I_E\) and \(I_M\).

If \(J\) is absent, one may try to use two copies:

\[
P\xrightarrow{\Delta}P\otimes P
\xrightarrow{I_E\otimes I_M}
R_E\otimes R_M.
\]

This route is valid only when the diagonal or replication constructor
\(\Delta\) has independent source authority and preserves the preparation
identity relevant to the claim.

Thus there are three different objects:

1. provenance compatibility, expressed by a pullback;
2. primitive joint acquisition, expressed by \(J\);
3. replicated marginal acquisition, expressed through \(\Delta\).

None can be substituted for another.

## Finite falsifiers

### Cross-occurrence hostile

Two preparations produce \((0,0)\) and \((1,1)\). The unrestricted product also
contains \((0,1)\) and \((1,0)\). These are removed by the pullback.

### Consumable-preparation hostile

Each marginal instrument exists, but applying either consumes the capability
required by the other. The pullback is nonempty while no joint instrument
exists.

### Unauthorized-copy hostile

A proof uses \(I_E\otimes I_M\) after silently inserting \(\Delta\). Deleting
the copying or repeated-preparation authority destroys the proof while leaving
both marginals valid.

### Nonidentical-replica hostile

Two preparations have the same coarse label but differ in a hidden source
coordinate relevant to the readout. Independent marginals then do not
constitute a same-preparation joint record.

## Cross-lane classification

### Strominger

The parity lane supplies the exact consumable-preparation hostile. The
electric/magnetic record pullback is necessary, but closure requires either a
primitive joint instrument or nondestructive-reuse authority.

### Aspect

The tetrahedral conditioning theorem uses four distinct probe preparations.
It is an ensemble design, not four simultaneous measurements of one unknown
packet. Its apparatus interpretation therefore requires a source-authorized
preparation family or exchangeability law. If one unknown packet is the target,
the theorem does not produce a joint four-probe instrument.

### Flavor

Observers calibrated at different stages or ensembles cannot be combined by
matching their reported coordinates. They require one of:

- a primitive joint experiment;
- a common source occurrence with nondestructive marginals;
- a repeated-preparation law carrying the same microscopic parameters;
- a hierarchical model that explicitly types which parameters are shared.

This sharpens the missing two-error probe: calibration and source derivation
must meet in one joint instrument or one authorized replica family.

### Grothendieck

Theta/Tate data are mathematical sources and may be reread, so physical
consumption is not the principal obstruction. The analogue of resource
compatibility is common-domain compatibility.

Two readouts are jointly defined only on a source-derived common domain with a
topology in which both are continuous or closed. Reusing the formula does not
supply a common completed domain. The seam-jet tower shows how one marginal can
remain finite while another boundary channel escapes under completion.

### Kitaev

For arbitrary quantum states, a universal copying diagonal is unavailable.
Repeated preparation is legal only when a constructor supplies the state from
known source controls. Logical commutator interferometry therefore needs either
a coherent primitive joint circuit or a declared preparation ensemble; a
formal diagonal on the state object would overclaim.

## Categorical form

The provenance pullback lives in the category of typed records. Joint
executability lives in a resource-sensitive symmetric monoidal category of
processes. Moving between them requires a functor that preserves the relevant
pullback and carries a source-authorized joint or replication constructor.

A cartesian record category may have a diagonal for every object. The process
category generally does not. Importing the record diagonal into the process
category is the exact categorical form of illicit copying.

## Decisive audit

For every multi-observer proposal, record:

1. the preparation object \(P\);
2. each marginal instrument and its resource effect;
3. the provenance maps defining the record pullback;
4. whether a primitive joint refinement exists;
5. whether replication is used;
6. the source authority and invariants of replication;
7. the common-domain or completion law;
8. one deletion replay removing joint or replication authority.

The proposal passes only at the first layer it actually constructs.

## Cross-sector prediction

The next recurring false positive will have this shape: two marginal observers
are individually valid and their record pair is provenance-compatible, so a
joint measurement is inferred. The consumable-preparation and unauthorized-copy
hostiles should reject it before any numerical fit or positivity argument.

## Sources

- research/nima/cross-lane-observer-factorization-gate.md
- research/aspect/optical-commutator-tetrahedral-frame.md
- research/kitaev/three-stage-logical-stabilization-witness.md
- research/strominger/parity-port-executability-boundary.md
