# Candidate factorization of RH source types

## Question

Can the source types currently entering the RH Interaction Net be assigned stable identifiers and factored into independently auditable fields without confusing equal SCC instrument profiles with source identity?

## Claim boundary

This packet defines a candidate RH registry and a finite schema test. It does not provide a project-wide source-type census, construct any open bridge, establish a common carrier, identify the boundary pencil with the xi zero divisor, or prove RH.

## Disposition

Retain a nine-factor dependent signature:

1. geometry and support;
2. coefficients;
3. constructor grammar;
4. transport and composition;
5. quotient;
6. completion;
7. probe grammar;
8. readout;
9. authority.

The factors form a dependency chain rather than a Cartesian product. Constructor grammar depends on its carrier; quotient and completion must preserve the admitted constructors; probes must act on the completed quotient; readout must descend through that quotient; authority constrains every map.

The candidate registry contains eight RH source families. Two entries remain deliberately intermediate: the completed boundary pencil is an open bridge-source candidate, while the xi spectral target is an analytic target whose identification with that pencil remains open.

Registry objects carry one of six kinds: `primitive_source`, `derived_source`,
`bridge`, `bridge_source`, `analytic_target`, or `derived_readout`. This prevents a comparison
constructor from being counted as though it were an independently given
carrier.

The registry records four bridge obligations. The first realizes prime incidence as a passive Schur operator. The second joins the Schur and primitive-trace sources at the regularized determinant line. The third is the first zero-capable three-input sewing and therefore requires all pairwise overlaps plus a typed three-way associator. The fourth compares the completed pencil with the xi spectral target.

Source-type equality requires equality of all nine factor identifiers and their dependency maps. Equal SCC instrument profiles remain a many-to-one capability projection. In particular, changing completion, probe grammar, or transport changes the source type even when the SCC profile and scalar readout remain unchanged.

## Organization

Let the carrier factors form a base category. Constructor grammars fiber over carriers; identity and completion data fiber over constructors; instruments and authority fiber over completed identities. A fully specified source packet is an object in the resulting iterated Grothendieck construction. Its coherence pyramid lies over that object. Cross-source bridges are spans or multi-input sewing constructors in the total category, not extra rungs silently appended to one input pyramid.

The Interaction Net is an executable projection of selected source objects, bridge ports, and local reductions. Net confluence is weaker than global coherence: competing reductions must still lift to associators and subsequent higher cells in the relevant bridge pyramid.

## Seven-case validation

The nine fields were applied to seven independently authored constructions.
The reciprocal lossy cavity is a primitive source whose first open gate is
continuum completion. The flavor canonical-source-to-`physical16` portal is a
bridge, not one source row; its authority remains open because the portal
coefficient and common-frame experiment are not source-derived. The finite
`D(S3)` plaquette is a primitive source with conditional authority for
non-native element-resolved pulses. The punctured radiative construction is a
primitive source with an explicit LF completion, while realization
faithfulness on collision strata remains partial. The magneto-optic loss
channel is a bridge-source: magnetic bias and causal material response are
converted into a polarization-resolved optical channel, then completed by one
bath mode per circular channel at a single frequency bin. Its finite quantum
completion is constructed, but broadband completion, jointly faithful
frequency probing, and material-specific fluctuation-dissipation authority
remain partial. The three-site cosmological correlator amplitude is a derived
source: its eight labelled deletion summands, rational coefficient operations,
and final correlator sum are source-defined, but Boolean-cube incidence has no
source-derived coefficient-level transport between deletion grades. Therefore
the amplitude readout is constructed while transport, quotient comparison,
period probes, and analytic completion remain partial. The cosmological
quartic is a derived readout, not a source or physical threshold: its unique
nonsoft positive real crossing and trivial generic transport are constructed,
while no source-derived port adapter assigns that crossing physical singular
support. Here authority is constructed as a negative boundary on
interpretation rather than as permission to promote the readout.

These cases show that factor presence is uninformative because every admitted
object must type all nine slots. The useful matrix records `constructed`,
`partial`, or `open` for each factor and preserves object kind separately.
Each status is relative to an explicit assessment scope: completion can be
constructed for a finite frequency bin while remaining open for a broadband
continuum.

## Falsifiers

The checker rejects the following identifications:

- equal SCC instrument profile with different completion;
- equal carrier and constructor grammar with different probe grammar;
- equal scalar readout with different transport law;
- a bridge missing any declared factor-compatibility witness;
- a probe designed after observing the target.

## Durable verification

- Contract: `research/aspect/contracts/source-type-factorization.v1.json`
- Checker: `research/aspect/checkers/check_source_type_factorization.py`
- Result: `research/aspect/results/source_type_factorization.json`
