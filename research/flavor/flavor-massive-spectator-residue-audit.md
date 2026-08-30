# WP156 — massive-spectator residue audit

## Bounded question

Does requiring every WP155 spectator to be heavy through a symmetry-preserving
bilinear mass force its \(\mathbb Z_4\) residue to vanish?

## Frozen mass grammar

Work with the same additive linear residue modulo four.

A Dirac block pairs two left-handed charges \(q\) and \(-q\):

\[
q+(-q)=0\pmod4.
\]

Every Dirac block therefore contributes spectator residue zero.

A one-field Majorana block is invariant when

\[
2q=0\pmod4.
\]

This permits \(q=0\) and \(q=2\). The charge-two Majorana block is massive and
symmetry preserving, yet contributes residue two.

## Exact completion classes

Finite sums of Dirac and allowed Majorana blocks generate exactly

\[
s\in\{0,2\}.
\]

Consequently:

- restricting spectators to Dirac blocks gives \(s=0\) and restores WP154's
  16-packet flavor kernel;
- allowing all symmetry-preserving massive bilinears gives a 32-packet flavor
  image, the even-spectator branch already seen in WP155.

The smallest hostile flavor packet is

\[
f=(2,2,2),
\qquad \sum_i f_i=2\pmod4.
\]

One charge-two Majorana spectator has \(s=2\), so the total residue vanishes.
Thus a mass gap does not by itself close the selector domain.

## Source interpretation

An independently conserved fermion number, complex representation constraint,
or other source law forbidding Majorana masses would restrict the massive
completion grammar to Dirac pairs and recover the 16-packet selector. Without
such a law, “heavy spectators decouple” is insufficient: the residue survives
decoupling even when ordinary threshold production is impossible.

## Typing

- **Admitted state domain:** finite multisets of symmetry-preserving Dirac and
  Majorana spectator mass blocks.
- **Faithful quotient coordinate:** `physical16` downstream; spectator mass
  blocks are upstream completion data.
- **Source-authorized probes:** bilinear mass invariance and total linear
  residue.
- **Contextual partition:** Dirac residue zero versus Majorana parity residue
  two.
- **Separation:** total anomaly detects the combined residue but not its block
  decomposition.
- **Selection:** 16-packet selector on the Dirac-only domain; only a 32-packet
  partial selector on the general massive domain.
- **Rigidification:** none.
- **Descent:** charge-pairing conditions are invariant under spectator basis
  changes and the induced flavor restriction descends under full weak-basis
  equivalence.
- **Reference port:** threshold spectroscopy would be a new relational
  experiment and cannot recover a decoupled anomaly residue automatically.
- **Physical instrument:** absent.

## Claim boundary

The checker audits the additive \(\mathbb Z_4\) residue and bilinear mass
grammar exactly. It does not claim a complete four-dimensional discrete gauge
anomaly classification; cubic, mixed-gauge, global, and spin-structure terms
remain to be derived in a gauge-complete model.

## Smallest exact falsifier

A single charge-two Majorana block satisfies \(2q=0\pmod4\) but has
\(s=2\). Together with \(f=(2,2,2)\), it cancels the total residue and doubles
the admitted flavor image relative to WP154.

## Reopening condition

Derive a conserved fermion number or representation theorem that forbids all
charge-two Majorana blocks throughout the UV domain, then compute the complete
local and global anomaly packet. Alternatively, show that the correct anomaly
group quotients the charge-two block to zero; that would change the target
character and requires redoing WP154 rather than silently absorbing the term.

## Verification

```text
python research/flavor/checkers/wp156_massive_spectator_residue.py
```

The dependency-free exact checker writes the result JSON and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 9/10, confidence 10/10, expected information gain
9/10. The attraction was the sharp distinction between Dirac decoupling and
Majorana residue. The confound was the deliberately incomplete anomaly packet.

Frozen optionality snapshot: four Dirac charge pairs, two Majorana charges,
two generated spectator residues, one 16-packet branch, one 32-packet branch,
one hostile massive block, 12 checks, and no instrument.

Post-objective: excitement 9/10, confidence 10/10, realized information gain
9/10. The full-residue ambiguity shrank from four classes to two under the mass
gap, but did not vanish. A Dirac-only source law restores WP154 exactly; the
charge-two Majorana block remains the smallest obstruction. No conserved
fermion number, complete anomaly calculation, or physical instrument was
constructed.

