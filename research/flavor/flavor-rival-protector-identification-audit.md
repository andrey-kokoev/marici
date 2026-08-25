# WP159 — rival protector-identification audit

## Bounded question

Is WP158's auxiliary \(\mathbb Z_3\) protector identified by the authorized
flavor response, or do inequivalent protector constructors implement the same
selector?

## Frozen rival grammar

Compare four source constructions:

1. exact \(\mathbb Z_3\) with spectator charges \((1,-1)\);
2. exact \(\mathbb Z_5\) with charges \((1,-1)\);
3. exact \(\mathbb Z_7\) with charges \((1,-1)\);
4. continuous \(U(1)_F\) with charges \((1,-1)\).

In every case, both same-field Majorana bilinears have nonzero protector charge,
the cross-Dirac bilinear is neutral, and the pair has zero linear
\(\mathbb Z_4\) residue. The constructors are inequivalent as source groups;
they are frozen before response comparison.

## Authorized low-energy response

The response packet contains six declared records:

1. \(NN\) forbidden;
2. \(\bar N\bar N\) forbidden;
3. \(N\bar N\) allowed;
4. net spectator \(\mathbb Z_4\) residue zero;
5. WP154 anomaly-kernel size 16;
6. restored topology domain is threshold-accessible.

All four response columns are identical. The exact response matrix has

\[
\operatorname{rank}R_{\rm low}=1,
\qquad
\dim\ker R_{\rm low}=3.
\]

Hence the full authorized low-energy record forms one contextual equivalence
class:

\[
\{\mathbb Z_3,\mathbb Z_5,\mathbb Z_7,U(1)_F\}.
\]

WP158 is therefore not source identified. Its minimality among cyclic groups
does not distinguish it from larger or continuous protectors through flavor
records.

## Formal defect/holonomy tower

For the finite rival packet only, attach formal source labels
\(n=(3,5,7,0)\), with zero denoting the continuous rival, and form the moment
tower

\[
1,n,n^2,n^3.
\]

The resulting Vandermonde matrix has exact rank four because the labels are
distinct. Thus a complete formal protector-order/holonomy tower separates this
frozen four-source family.

This is not yet a physical probe. It presumes access to protector defects or
holonomies and treats the continuous rival through a formal label. No source-
derived preparation protocol, finite-energy defect operator, threshold scale,
width, detector convolution, or open-rival completeness theorem is supplied.
The formal tower defines a new relational experiment rather than improving the
ordinary flavor readout.

## Typing

- **Admitted source domain:** the four frozen protector constructors above.
- **Faithful flavor quotient:** `physical16`; every constructor induces the
  same selected flavor family.
- **Source-authorized probe family:** the six low-energy operator, anomaly, and
  accessibility records.
- **Contextual partition:** one four-member class under authorized probes;
  four singleton classes only under the formal tower.
- **Separation:** no at low energy; yes algebraically after adding the full
  formal source-label tower.
- **Selection:** every constructor conditionally implements WP154's same proper
  flavor-subspace selector.
- **Rigidification:** each protects that selector against the Majorana
  completion, but the protector source is not identified.
- **Descent:** all low-energy records descend under the full weak-basis
  groupoid.
- **Reference port:** defect/holonomy access changes the source groupoid and is
  explicitly a new relational experiment.
- **Physical instrument:** absent.

## Smallest exact falsifier

The \(\mathbb Z_3\) and \(\mathbb Z_5\) constructors have identical columns
for every authorized low-energy record. This pair alone falsifies unique source
identification.

## Deutschian disposition

WP158 explains technical stability but has not yet become hard to vary. The
same selected flavor packet survives changes in protector group, group order,
and continuous versus discrete structure. A hard-to-vary explanation needs a
collateral record derived from the same protector source and accessible to an
actual instrument.

## Reopening condition

Derive finite-energy topological defects, Aharonov--Bohm phases, domain-wall
data, or threshold states from each protector construction; include symmetry-
breaking scales, mixing, widths, decoupling, and detector resolution. Grant
source identification only if the implemented response kills the
three-dimensional kernel on an enlarged rival grammar.

## Verification

```text
python research/flavor/checkers/wp159_rival_protector_identification.py
```

The dependency-free exact checker writes the result JSON and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10 that low-energy rank would
be one, expected information gain 10/10. The confound was the finite rival
grammar.

Frozen optionality snapshot: four protectors, six authorized low-energy
records, one expected contextual class, a four-port formal tower, 12 checks,
and no physical instrument.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Low-energy rank is one with a three-dimensional source kernel; all four
constructors merge contextually. The formal tower reaches rank four but was
retyped as a new uninstrumented experiment. Selector existence survives;
protector identification fails. No threshold or defect instrument was
constructed.

