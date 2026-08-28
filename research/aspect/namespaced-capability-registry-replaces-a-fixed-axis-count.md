# A namespaced capability registry replaces a fixed axis count

## Why the numbered tower must open

The six-axis compiler needed a seventh action axis.  The Flavor transfer then
showed that one unqualified action axis is itself too coarse:

- the optical emulator action is authorized;
- the physical dual-source action is missing.

A fixed list of axes would grow indefinitely and eventually smear different
authority loci back together.  The stable construction is a capability
registry with a core profile and namespaced extensions.

## Core profile

The current core remains:

- `scalar`;
- `packet`;
- `incidence`;
- `history`;
- `path`;
- `coefficient`;
- `action`.

Existing seven-axis records remain valid under this profile.

## Namespaced extensions

Additional predicates declare their scope explicitly.  The first admitted
extensions are:

- `duality_exchange`: `intertwined`, `broken`, or `unknown`;
- `action:optical_emulator`: `authorized`, `missing`, or `unknown`;
- `action:physical_dual_source`: `authorized`, `missing`, or `unknown`.

The primitive-product hostile is then recorded without contradiction:

`scalar=dark`, `packet=bright`, `duality_exchange=broken`,

`action:optical_emulator=authorized`,

`action:physical_dual_source=missing`.

The scalar product monitor is dark, the differential packet is bright, the
exchange law is broken, the laboratory action exists, and the physical source
action does not.

## External validation by the infinity packet

Benincasa independently separated the complete infinity packet into two
events.  The physical readout is

`(bright,bright,matched,trivial,admissible,native,authorized)`,

while the selective controller is

`(unknown,unknown,unknown,unknown,disconnected,native,missing)`.

He also supplied counterfactual witnesses varying selector path and action
independently.  The registry imports both records unchanged and verifies all
fourteen external checks.  This is evidence that the core axes compose across
sectors without leaking the bright readout's authority into the missing
controller.

## Registry law

Every capability declaration contains:

- a namespaced key;
- a finite allowed value set containing `unknown`;
- an evidence locus;
- explicitly declared derived rules.

No implication exists merely because two keys share a suffix such as
`action`.  In particular:

- emulator action does not authorize physical source action;
- native coefficients do not authorize an operation;
- path obstruction does not imply missing action;
- a dark scalar does not imply packet zero.

This is the open-ended rung above the seven-axis tester.  New sector
architectures extend the registry rather than renumbering the ontology.

## Verification

```text
python research/aspect/checkers/compile_namespaced_capability_registry.py
```
