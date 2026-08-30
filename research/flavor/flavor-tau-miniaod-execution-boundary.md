# Tau MiniAOD execution boundary (WP247)

## Pilot

WP247 imports the smallest 140-GeV CMS tau-signal file from record 19459:
316,932,303 bytes, 14,688 events, Adler-32 `494b83da`. The file is a physical
2015 detector simulation of bottom-associated scalar production with tau-pair
decay.

Uproot reads the split reconstructed-tau four-vector and charge fields, along
with split MET and generator kinematics. The required embedded tau-ID payload
has type `vector<pair<string,float>>[]` and fails with `NotImplementedError`
because its memberwise serialization is unsupported. Generic ROOT 6.40 also
lacks the `edm::Wrapper<vector<pat::Tau>>` and `pat::Tau` dictionaries.

The narrower detached-leaf repair was tested hostilely. After generating only
the standard-library dictionaries for `pair<string,float>` and its vector,
generic ROOT reached entry 1 and reported one tau, but assigned its ID vector
the impossible length `14757395258967575620`. This exceeds the entire
316,932,303-byte file even under the deliberately absurd lower bound of one
byte per ID. The split leaf therefore depends on the missing `pat::Tau`
streamer layout; an STL-only proxy corrupts the record and is not an
instrument.

A second repair used the file's own ROOT streamer metadata. `TFile::MakeProject`
generated 299 dependency classes for the requested `pat::Tau` class. After
putting the bundled `rootcling` on `PATH`, compilation stopped at a generated
class/namespace collision: `reco::CaloJet` had already been declared as a
class when another generated header declared `namespace CaloJet`. No shared
dictionary was produced. This establishes that metadata are present, but does
not authorize a hand-patched layout: any such repair still needs validated
readback against the official CMSSW streamer.

## Consequence

A kinematics-only selection is not a physically typed tau instrument. It would
count jet fakes as tau candidates and fit acceptance from an incomplete object.
Therefore WP246's promising rate cannot yet be converted into a detector
response or finite-power source identifier on the current execution surface.

The smallest falsifier is exact: the detached proxy reports more ID elements
for one tau than there are bytes in the whole file. Independently, remove the
derived tau-ID discriminator and a reconstructed object is no longer
established as a tau.
The remaining gate is a compatible CMSSW 7.6 environment, an official flat
derivation that preserves tau IDs, triggers, MET, generator matching, and
provenance, or a repaired generated dictionary whose layouts validate against
official CMSSW readback. No inferred ID proxy is admitted.

## Supersession

WP248 repairs the generated dictionary's first mechanical collision and reads
one stable 98-ID schema across the complete pilot. It supersedes this packet's
claim that offline tau identification is not executable. The narrower gate
that survives is official-layout and trigger calibration; WP248 does not yet
supply a complete detector acceptance.

Run `uv run --with numpy --with awkward --with uproot python
research/flavor/checkers/wp247_tau_miniaod_execution_boundary.py` to reproduce
the readable/unreadable product boundary and generated JSON result.
