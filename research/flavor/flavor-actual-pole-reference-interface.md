# Actual-pole reference interface (WP258)

## Candidate repair

WP257 shows that source-mass normalization requires an added reference port.
The closest existing physical candidates are CMS records 43611 and 43651.
They contain source-labelled MSSM scalar samples whose generated parent masses
are the two actual pole values used by the flavor construction.

That numerical match is only one interface field. The candidate records are
2016 NanoAOD forced-dimuon samples. WP256 is a 2015 MiniAOD muon–tau response
using the unchanged WP251 trigger, reconstruction, tau-ID, and object-matching
instrument. A common interface therefore requires:

1. a source-mass reference;
2. common decay topology;
3. common detector era and reconstruction;
4. common event selection;
5. physical branching normalization.

The existing pair supplies only the first item. WP241 already establishes that
the forced dimuon decay is not a physical branching prediction and that shape
and yield transport out of its declared source domain are unauthorized.

## First nonfaithful arrow

The failed arrow runs from the actual-pole dimuon source record to the 2015
muon–tau detector response.

Matching pole numbers does not parallelize the source and detector frames.
The dimuon records rigidify their own MSSM mass-hypothesis presentation, but
they neither select a `physical16` point nor repair WP256's reference port.

## Decisive next experiment

The smallest constructive repair is an actual-pole tau sample in the same era
and reconstruction frame, with physical branching normalization and the
unchanged WP251 selection. A validated source-derived reweighting carrying all
four missing interface fields would also suffice. Until then, direct-pole
transport is source-support closed rather than algebraically incomplete.

Run `uv run --with sympy python
research/flavor/checkers/wp258_actual_pole_reference_interface.py` for the
exact five-field interface audit and hostile complete-interface claim.
