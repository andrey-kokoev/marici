# WP154 — faithful Z4 anomaly-selector audit

## Bounded question

Does permutation invariance plus faithfulness determine WP153's missing
modular amplitude constraint without fitting a preferred coefficient?

## Frozen candidate family

Reduce the three central fixed-set Euler values modulo four:

\[
f=(f_1,f_2,f_3)\in(\mathbb Z/4\mathbb Z)^3.
\]

Every permutation-invariant linear character to \(\mathbb Z_4\) has the form

\[
\mathcal A_c(f)=c(f_1+f_2+f_3)\pmod4,
\qquad c\in\mathbb Z_4.
\]

Require the target character to be faithful on the diagonal source charge.
For \(\mathbb Z_4\), faithfulness is equivalent to
\(\gcd(c,4)=1\), so

\[
c\in\{1,3\}.
\]

These are not two different selector kernels: multiplication by either unit is
invertible modulo four. Hence

\[
\ker\mathcal A_1=\ker\mathcal A_3
=\{f:f_1+f_2+f_3=0\pmod4\}.
\]

## Exact selector result

The ambient residue space has 64 packets and the faithful kernel has 16. The
operation therefore selects a proper subspace, reducing the source domain by a
factor four. It rejects WP153's hostile aligned packet
\((1,1,1)\), since its sum is three modulo four.

On the aligned diagonal \(f=(a,a,a)\), anomaly freedom gives

\[
3a=0\pmod4.
\]

Because three is invertible modulo four, this forces

\[
a=0\pmod4.
\]

Thus the combination of WP153 alignment and a faithful invariant character
does constrain the previously free trivial amplitude. It implies
\(F=0\pmod{96}\), restoring WP150's topology congruence and WP147's uniformly
accessible admitted family.

## Hostile faithfulness gate

Faithfulness is load-bearing. The nonfaithful character \(c=2\) has a
32-element kernel and accepts

\[
f=(2,2,2),
\qquad f_1+f_2+f_3=2\pmod4.
\]

The trivial character \(c=0\) accepts all 64 packets. Therefore a merely
distinguishing or symmetric functional is insufficient; the source must
authorize a faithful \(\mathbb Z_4\) anomaly character.

## Typing and authority boundary

- **Admitted state domain:** central fixed-set residues
  \((\mathbb Z_4)^3\), together with the WP153 alignment condition when the
  point-selector consequence is invoked.
- **Faithful flavor quotient:** `physical16`, downstream of the corrected
  topology, flux, and flavor matching maps.
- **Source-authorized probe family:** conditionally, the invariant faithful
  character \(\mathcal A_c\) and its zero-residue consistency projector.
- **Contextual partition:** four anomaly-residue fibers, each of size 16.
- **Separation:** the character separates total residues but not the 16 points
  within a fiber.
- **Selection:** a genuine proper-subspace selector conditional on the
  character being physically source-derived.
- **Rigidification:** none by the anomaly projector; WP153 supplies the
  independent alignment rigidifier.
- **Descent:** the character is invariant under all three-sector permutations;
  its induced topology restriction and flavor packet descend under the full
  weak-basis groupoid.
- **Reference port:** none is mathematically required.
- **Physical instrument:** absent. Anomaly cancellation is a consistency gate,
  not automatically an experimentally executable readout.

## Claim boundary

This is the first candidate in the topology branch whose kernel is determined
by abstract source requirements—permutation invariance and faithfulness—rather
than by choosing the desired coefficient. It remains conditional because no
declared UV flavor action has yet produced this gauged \(\mathbb Z_4\), its
charge assignment, or its anomaly polynomial. Algebraic availability is not
executable physical control.

## Smallest exact falsifier

Drop faithfulness and choose \(c=2\). The packet \((2,2,2)\) lies in
\(\ker\mathcal A_2\) but violates the target sum constraint. This doubles the
kernel from 16 to 32 and destroys selector authority.

## Reopening condition

Construct a gauge-, Lorentz-, and weak-basis-complete source model whose
independently derived discrete anomaly reduces exactly to a faithful invariant
\(\mathbb Z_4\) character on the three central fixed sectors. Verify all local,
mixed, and global anomalies, show that threshold and RG transport preserve the
kernel, and state whether anomaly freedom is only a consistency condition or
has an actual physical instrument.

## Verification

```text
python research/flavor/checkers/wp154_faithful_z4_anomaly_selector.py
```

The dependency-free exact checker enumerates all 64 residue packets, writes
the generated JSON, and requires 12/12 checks.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The key attraction was that faithfulness might determine the kernel
without fixing a numerical coefficient. The confound was the missing physical
derivation of the gauged character and its instrument.

Frozen optionality snapshot: four invariant characters, two faithful
coefficients, one common 16-point kernel, one nonfaithful 32-point hostile
kernel, one trivial 64-point kernel, 12 checks, and no physical instrument.

Post-objective: excitement 10/10, confidence 10/10 in the finite theorem,
realized information gain 10/10. The two faithful branches merged to one
canonical kernel; 48 of 64 residue packets were eliminated; WP153's hostile
aligned amplitude was rejected; and the nonfaithful and trivial branches were
retained as exact falsifiers. The mathematical selector is progressive, but
no UV anomaly polynomial, gauging, RG preservation theorem, or physical
instrument was constructed.

