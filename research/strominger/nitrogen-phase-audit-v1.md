# Nitrogen: N-14 blocked in the current ansatz, N-15 admitted

**Superseded witness:** the [all-contact repair](assembly-contact-coverage-repair-v1.md)
reselected B/C/N references and regenerated N-15 at orientation 5801. Current
admission enforces every physical contact. Witness cell IDs, orientation and
certificate-state counts below describe the historical pre-repair selection;
use the repair note and refreshed receipts for current data.

Both N-14 and N-15 are physically stable isotopes. This audit does **not** derive
that fact. It exposes a limitation of the existing isotope-search ansatz rather
than weakening its rules to make every target pass.

## N-14: complete bounded negative

Target: 7P/7N/7e. Extensions retaining the selected C-13, C-12 or B-11 did not
produce complete geometry candidates. An unrestricted-root search was therefore
run over the existing 343-cell domain, including all six root MMCC role choices.

That complete geometry search finds **2,384 typed nuclei**, but **zero complete
neutral assemblies**:

- 1,920 typed nuclei have seven individually eligible electron cells.
- 464 have eight individually eligible electron cells.
- All `1,920 + 464 * choose(8,7) = 5,632` seven-electron combinations contain an
  electron/electron full-face contact, forbidden by the existing rules.
- Consequently no candidate reaches phase compilation.

This result is not a timeout, not merely failure of one retained core, and not
physical nonexistence or instability of N-14. Its scope is the fixed domain,
root proton, MMCC/contact grammar, split-cell electron restriction and requirement
that every neutron have an occupied native proton reference. Those are stronger
assumptions than the common locally generative source constructor. The failure
does not distinguish which restriction would need changing, and does not justify
adding a special N-14 exception or an unwitnessed E/E interaction.

**N-14 is not added to the viewer.** Its selector admission explicitly fails
with a bounded-ansatz message rather than fabricating a reference.

## Search optimization—not an admission relaxation

Nitrogen searches reject a connected nuclear prefix early only if none of the
six root markings admits the existing global MMCC coloring. This is sound:
every valid final coloring restricts to a valid coloring on each connected
prefix; adding cells cannot repair a contradictory role on an existing face.
No valid candidate is removed by this rejection.

The checker compares the entire candidate lists, not just counts, between
pruned/unpruned complete Li-5/6/7/8 searches. It also compares both modes for
the retained-C-13 N-15 search. Earlier isotope searches retain their old default
without early pruning. Prefix counts with pruning are not comparable to older
untyped-prefix counts and are labelled accordingly in the receipt.

## N-15: retained C-13 reference

Target: **7P/8N/7e**, 22 carriers. A separate search retaining C-13 succeeds:

- Adds proton **18**, neutron **230**, electron **227** (geometric cell IDs).
- Retains C-13 cells/species, C/M roles, native readers and every old transport
  edge. It does not pass through an admitted N-14 or imply a physical growth law.
- Four geometry candidates; all **65,536** reader assignments tested.
- Three assignments pass and preserve the old readers. The selected first
  witness uses orientation **11417**.
- **61** history-bearing certificate states; all **22/22** carriers covered,
  with every entered state able to reach an E exit.

An initial unrestricted N-15 exploration also found a separate compatible
reference; the viewer instead uses the subsequently verified retained-C-13
witness. No exhaustive phase classification of unrestricted N-15 is claimed.

The witness is stored in `nitrogen15-reference.mjs` to avoid searching reader
assignments on the browser's UI thread. This is not an audit bypass: uncached
admission recompiles the native packets and complete phase certificate, checks
particle counts and retention of C-13, and runs the phase audit. The offline
checker independently regenerates the candidate list and checks that the frozen
witness is its first reader-preserving acceptance.

## Verification and UI

Only **N-15** is added to both viewer selectors, with 22 looping steps. Checks
cover N-15 alone and both orders of C-13/N-15 comparison, shared controls and
absence of an N-14 option. The phase suite now covers ten reference isotopes,
90 character/phase inputs, full five-slot transport and all face modes, inverse
recovery, display round trips and corruption controls.

```sh
node research/strominger/checkers/check_nitrogen_assemblies.mjs
node research/strominger/checkers/check_phase_assembly.mjs
node research/strominger/checkers/prepare_particle_overlap_viewer.mjs
node research/strominger/checkers/check_fiber_space.mjs
```

The expensive nitrogen search audit is separate from the browser checker;
the browser/phase suite revalidates the selected witness, not the entire search.

Evidence:

- `results/nitrogen-assembly/verification.json`
- `results/phase-assembly/verification.json`
- `results/fiber-space/verification.json`
- `results/fiber-space/carbon13-nitrogen15-comparison.png`

**Conclusion:** the rules admit a compatible N-15 reference but fail to cover
stable N-14 within this ansatz. They are neither a sufficient stability test
(Li-8 was admitted) nor an established complete description of stable nuclei.
Binding, decay, larger-domain effects and broader source-supported geometry
remain separate questions.
