# WP158 — minimal Z3 Dirac-protector audit

## Bounded question

What is the smallest exact representation constraint that forbids WP157's
charge-two Majorana operator while retaining a symmetry-preserving massive
spectator completion?

## Minimality gate

A cyclic protector must contain a nonzero charge \(q\) with

\[
2q\ne0,
\]

so that a same-field Majorana bilinear is forbidden. No \(\mathbb Z_2\) charge
has this property. The smallest cyclic group that does is \(\mathbb Z_3\),
with \(q=1\) or \(2\).

## Frozen charge packet

Retain WP157's residual \(\mathbb Z_4\) and add an exact auxiliary
\(\mathbb Z_3\). Introduce a spectator pair

\[
N:(2,1),
\qquad
\bar N:(2,2)
\]

under \(\mathbb Z_4\times\mathbb Z_3\). The charge-four parent Higgs
\(\Phi\) is neutral under both residual factors.

The two same-field operators have charges

\[
\Phi^\dagger NN:(0,2),
\qquad
\Phi^\dagger\bar N\bar N:(0,1),
\]

so both are forbidden by \(\mathbb Z_3\). The cross operator has

\[
\Phi^\dagger N\bar N:(0,0)
\]

and generates a Dirac mass after Higgsing.

The pair contributes zero linear residue in both factors:

\[
2+2=0\pmod4,
\qquad
1+2=0\pmod3.
\]

Thus the minimal protector removes WP156's residue-two massive block without
setting an allowed coupling to zero.

## Selector disposition

Combined with WP154, an exact unbroken \(\mathbb Z_3\) protector restores the
Dirac-only spectator grammar and hence the 16-packet anomaly kernel. It is a
genuine conditional representation selector, not a chart rigidifier.

The result is not unconditional. The auxiliary group changes the physical
source groupoid, and its exactness, charge origin, anomaly freedom, and
survival under thresholds and gravitational effects are not established.
If \(\mathbb Z_3\) is absent or broken, WP157's Majorana operator reappears.

## Typing

- **Admitted state domain:** spectator spectra respecting exact
  \(\mathbb Z_4\times\mathbb Z_3\) and the frozen charge packet.
- **Faithful flavor quotient:** `physical16` downstream.
- **Source-authorized operations:** all bilinear mass operators invariant under
  both discrete factors.
- **Contextual partition:** forbidden same-field blocks versus admitted
  cross-Dirac blocks.
- **Selection:** representation-level removal of the residue-two completion;
  combined with WP154, proper flavor-subspace selection.
- **Rigidification:** none.
- **Descent:** charge invariance is independent of spectator basis and the
  flavor result descends under full weak-basis equivalence.
- **Reference port:** adding \(\mathbb Z_3\) is a new source structure, not an
  observational recovery operation.
- **Physical instrument:** absent.

## Smallest exact falsifier

Remove or break the \(\mathbb Z_3\) factor. Residual \(\mathbb Z_4\) alone
assigns zero charge to \(\Phi^\dagger NN\), immediately restoring the
residue-two Majorana completion.

## Remaining gates

1. Derive the auxiliary \(\mathbb Z_3\) and charge packet from a declared UV
   gauge or geometric source rather than choosing them to forbid one operator.
2. Check continuous, discrete, mixed, gravitational, and global anomalies.
3. Prove the protector remains exact after symmetry breaking and RG transport.
4. Type any physical instrument separately; consistency selection does not
   automatically provide a detector.

## Verification

```text
python research/flavor/checkers/wp158_minimal_z3_dirac_protector.py
```

The dependency-free exact checker writes the result JSON and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 9/10, confidence 10/10, expected information gain
9/10. The minimal cyclic-group classification made the route exact. The
confound was that adding the protector changes the source groupoid and leaves
its physical origin unexplained.

Frozen optionality snapshot: failed Z2 branch, minimal Z3 branch, two forbidden
Majorana operators, one admitted Dirac operator, one restored 16-packet
selector, 12 checks, and no instrument.

Post-objective: excitement 9/10, confidence 10/10, realized information gain
9/10. The minimal protecting group was fixed without coefficient fitting; the
residue-two mass block was eliminated on the declared domain; and WP154's
selector was restored conditionally. The source origin, complete anomaly
packet, exactness under transport, and physical instrument remain open.

