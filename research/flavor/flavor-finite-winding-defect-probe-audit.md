# WP160 — finite-winding defect-probe audit

## Bounded question

Can a source-derived finite tower of relational defect windings distinguish
WP159's four rival protector constructors?

## Frozen ideal probe

Prepare one protector defect, wind a unit test charge around it \(m\) times,
and record whether the holonomy returns exactly to identity. For a primitive
\(\mathbb Z_n\) defect,

\[
R_m(\mathbb Z_n)=
\begin{cases}
1,&n\mid m,\\
0,&n\nmid m.
\end{cases}
\]

For the frozen generic \(U(1)_F\) rival, no finite winding returns exactly to
identity. Include a normalization record \(R_0=1\) for every constructor. The
probe family through depth \(W\) is

\[
(R_0,R_1,\ldots,R_W).
\]

This is a relational experiment: it measures charge--defect holonomy, not an
absolute phase of the original flavor experiment.

## Exact contextual partitions

At \(W=4\), only \(\mathbb Z_3\) has returned:

\[
\{\mathbb Z_3\},
\qquad
\{\mathbb Z_5,\mathbb Z_7,U(1)_F\}.
\]

At \(W=6\), the partition is

\[
\{\mathbb Z_3\},
\quad
\{\mathbb Z_5\},
\quad
\{\mathbb Z_7,U(1)_F\},
\]

and the response rank is three. The exact hostile pair is therefore
\(\mathbb Z_7\) versus generic \(U(1)_F\).

At \(W=7\), all four response columns differ and the normalized response
matrix has rank four. Exhaustive exact search gives

\[
W_{\min}=7.
\]

The normalization port is load-bearing: the unnormalized return rows have rank
three because the generic \(U(1)\) column is identically zero.

## Typing and authority

- **Admitted source domain:** the four frozen WP159 protectors with primitive
  discrete defects and one generic non-returning continuous holonomy.
- **Faithful flavor quotient:** `physical16` is unchanged; this probe acts on a
  new protector-defect experiment.
- **Source-authorized probe family:** ideal return predicates through winding
  seven, conditional on defect and test-charge availability.
- **Contextual partition:** one class at ordinary flavor readout; three classes
  at \(W=6\); four singleton classes at \(W=7\).
- **Separation:** jointly faithful on the frozen four-constructor domain at
  \(W=7\).
- **Selection:** none; the probe identifies protectors but does not further
  reduce the selected flavor family.
- **Rigidification:** none.
- **Reference port:** required. The defect and winding path enlarge the
  stabilizer groupoid and define a new relational experiment.
- **Descent:** return order is invariant under protector gauge presentation;
  ordinary flavor descent under the full weak-basis groupoid is unaffected.
- **Physical instrument:** absent.

## Instrument gates

The exact rank result does not establish executable control. A physical
realization must derive:

1. finite-tension stable defects from each protector source;
2. an admitted test charge and controlled windings up to seven;
3. coherence against defect motion, mixing, and environmental decoherence;
4. finite phase resolution and false-return/false-nonreturn rates;
5. symmetry-breaking scales within reach;
6. an enlarged hostile family including nonprimitive defects and rational
   \(U(1)\) holonomies.

## Smallest exact falsifier

Truncate at \(W=6\). Then \(\mathbb Z_7\) and the frozen generic \(U(1)_F\)
have identical normalized records, leaving rank three. This proves that fewer
than seven ideal windings do not identify the frozen family.

## Verification

```text
python research/flavor/checkers/wp160_finite_winding_defect_probe.py
```

The dependency-free exact checker writes the JSON result and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 9/10, confidence 10/10, expected information gain
9/10. The return-order tower is source-derived and finite on the frozen family.
The confound was ideal exact phase resolution and assumed defect preparation.

Frozen optionality snapshot: four protectors, seven winding depths plus one
normalization port, partitions at depths four, six, and seven, 12 checks, and
no physical instrument.

Post-objective: excitement 9/10, confidence 10/10, realized information gain
9/10. A source-derived canonical probe tower replaced WP159's arbitrary moment
labels. It becomes jointly faithful at exact depth seven; the depth-six kernel
is explicitly the \(\mathbb Z_7/U(1)\) pair. One normalization port and a new
relational groupoid are required. No defect preparation, reach, resolution, or
detector was constructed.

