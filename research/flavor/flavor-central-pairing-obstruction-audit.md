# WP152 — central fixed-sector pairing obstruction

## Bounded question

Can a source-derived involutive pairing of the central fixed sectors force
WP150's total correction \(F\) to vanish modulo 96?

## Frozen pairing grammar

WP151 found three nonidentity central singleton sectors:

\[
\mathcal C=\{\mathrm{CP},-1,-\mathrm{CP}\}.
\]

Freeze the weakest supersymmetric or index-like repair: an involution
\(J:\mathcal C\to\mathcal C\) exchanges sectors in pairs, and the fixed-set
Euler contributions on an exchanged pair are opposite. This grants exact
cancellation on every two-cycle without assuming the desired total result.

## Exact parity obstruction

There are four involutions on a three-element set: the identity and three
transpositions. Every nontrivial involution exchanges one pair and fixes the
remaining sector. No fixed-point-free pairing exists because
\(|\mathcal C|=3\) is odd.

For any of the three nontrivial pairings, assign the exchanged sectors values
\(+24\) and \(-24\), while the unavoidable fixed sector has value \(+24\).
Then

\[
F_{\rm central}=24-24+24=24.
\]

The pairing law is fully satisfied, but at \(\chi(X/G)=1\),

\[
k=4-\frac{24}{24}=3.
\]

Thus involutive cancellation alone does not derive the modulus-four selector.

## Typing and claim boundary

- **Admitted source domain:** fixed-set Euler packets on the three central
  nonidentity sectors.
- **Faithful flavor quotient:** `physical16` downstream; the pairing acts on
  upstream equivariant source data.
- **Source-authorized operation:** a declared involution and antisymmetric
  cancellation on its two-cycles.
- **Contextual partition:** one exchanged pair and one fixed sector for each
  nontrivial involution.
- **Selection:** none. The fixed sector retains a free correction residue.
- **Rigidification:** pairing organization only.
- **Descent:** the parity statement is invariant under relabeling of the three
  central sectors; no weak-basis obstruction occurs downstream.
- **Reference port:** resolving the fixed sector requires new source data, not
  recovery of an absolute phase.
- **Physical instrument:** absent.

The audit does not exclude a higher-rank equivariant index relation coupling
all three sectors simultaneously. It excludes the common move of citing
pairwise supersymmetric cancellation without typing the odd residual sector.

## Smallest exact falsifier

For any transposition pairing,

\[
(f_a,f_b,f_c)=(24,-24,24)
\]

with \(a,b\) exchanged and \(c\) fixed satisfies pair cancellation but leaves
\(F=24\), hence \(k=3\).

## Reopening condition

A valid successor must provide an independently derived relation that also
constrains the unavoidable fixed sector—for example, a vanishing theorem for
its index or a three-sector identity whose coefficient lattice forces total
divisibility by 96. The relation must be demonstrated across the complete
admitted source domain rather than on one symmetric packet.

## Verification

```text
python research/flavor/checkers/wp152_central_pairing_obstruction.py
```

The dependency-free exact checker writes the JSON result and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 7/10, confidence 10/10, expected information gain
8/10. The odd-cardinality obstruction was transparent. The confound was that
a higher-rank index identity need not factor through pairwise involution.

Frozen optionality snapshot: four involutions, three nontrivial pairings, one
unavoidable fixed sector per pairing, three hostile assignments, 12 checks,
and no physical instrument.

Post-objective: excitement 7/10, confidence 10/10, realized information gain
8/10. Every pairwise-cancellation branch was eliminated as a sufficient
selector. The residual authority was localized to one central fixed sector.
No claim was made against simultaneous three-sector identities, and no source
vanishing theorem or instrument was constructed.

