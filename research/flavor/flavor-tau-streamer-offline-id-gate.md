# Tau streamer offline-ID gate (WP248)

## Bounded question

Can the checksum-pinned 140-GeV CMS MiniAOD pilot supply an executable offline
tau-ID response without inventing an ID proxy?

## Repaired read path

ROOT's file-local streamer metadata generate 299 dependent classes. The first
generated build defect is mechanical: `pat__Jet.h` redeclares
`reco::CaloJet::Specific` through a namespace although `reco__CaloJet.h`
already supplies the containing class and nested enum. Replacing only that
duplicate declaration with the generated class header changes no serialized
member or ordering. The rebuilt 5.43-MB dictionary loads and reads the full
`edm::Wrapper<vector<pat::Tau>>` branch.

Across all 14,688 events, all 17,352 reconstructed taus carry one common schema
of exactly 98 named IDs. Freeze the independently named conjunction

\[
\texttt{decayModeFinding}\wedge
\texttt{byMediumIsolationMVArun2v1DBoldDMwLT}\wedge
\texttt{againstElectronVLooseMVA6}\wedge
\texttt{againstMuonTight3}.
\]

It selects 6,431 taus, with at least two selected taus in 811 events. The exact
offline-ID event fraction is

\[
\frac{811}{14688}\approx 0.05522.
\]

This exceeds WP246's weaker-pole 2.49% one-event feasibility screen but not its
8.30% ten-event screen.

## Claim boundary

This is an executable file-local **offline tau-ID response**, not yet a
trigger-calibrated detector acceptance. It does not validate the generated
layouts against official CMSSW, incorporate a trigger, establish the 2016
frame, subtract backgrounds, interpolate the 130/140/160 response, or prove a
rank-two source detector. The smallest exact falsifier is any disagreement in
ID names or values under official CMSSW readback.

Run `uv run --with sympy python research/flavor/checkers/wp248_tau_streamer_offline_id_gate.py` to
reproduce the exact arithmetic classification and generated JSON result.
