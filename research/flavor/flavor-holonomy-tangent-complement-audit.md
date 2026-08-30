# WP162 — holonomy tangent-complement audit

## Bounded question

Can a source-derived local-deformation probe complement WP161's return tower
and distinguish discrete protectors from rational continuous holonomies?

## Frozen complementary family

The WP161 return tower sees only the order of one chosen holonomy. Add the
local tangent indicator

\[
D=
\begin{cases}
0,&\mathbb Z_n,\\
1,&U(1),
\end{cases}
\]

which records whether arbitrarily small source-authorized holonomy
deformations exist near the tested configuration.

For mixture identification, also freeze two mixed responses

\[
nD,
\qquad n^2D,
\]

where \(n=3,5,7\) for rational continuous holonomies and \(n=0\) labels the
irrational continuous branch. These are not arbitrary source labels: they
couple the tangent capability to the return order already measured by WP160.

## Point separation versus joint faithfulness

Appending the single binary record \(D\) makes all seven constructor records
distinct. Every discrete/continuous alias pair is separated:

\[
(\mathbb Z_n,U(1)_{\mathrm{ord},n})
\longmapsto(0,1).
\]

However, the response rank rises only from four to five. The seven point
alternatives form singleton contextual classes, while arbitrary linear source
mixtures retain a two-dimensional kernel:

\[
\text{point separation}\not\Rightarrow\text{mixture faithfulness}.
\]

Adding \(nD\) raises the rank to six. Adding \(n^2D\) raises it to seven. The
rank sequence is exactly

\[
4\to5\to6\to7.
\]

Thus the three-row complementary tower \((D,nD,n^2D)\) is jointly faithful on
the frozen seven-source coefficient packet.

## Typing

- **Admitted source domain:** WP161's seven protectors/holonomies.
- **Faithful flavor quotient:** `physical16` remains unchanged.
- **Source-authorized probe family:** conditionally, return records plus local
  tangent susceptibility and its first two order-conditioned moments.
- **Contextual partition:** seven singleton point classes after the binary
  tangent record.
- **Separation:** binary tangent suffices for point alternatives; the complete
  three-row tower is required for linear source-mixture faithfulness.
- **Selection:** none.
- **Rigidification:** none.
- **Descent:** tangent dimension and return order are invariant under gauge
  presentation changes; the flavor packet still descends under full weak-basis
  equivalence.
- **Reference port:** the controlled holonomy deformation is a new relational
  source experiment.
- **Physical instrument:** absent.

## Executability gate

Algebraic span is not executable control. Implementing \(D,nD,n^2D\) requires
a calibrated continuous gauge-field actuator, stable defects, controlled small
deformations, repeated winding, and a detector that resolves susceptibility
from zero. A discrete theory with finite-resolution pseudo-deformations or a
continuous theory with an inaccessible massive gauge mode can collapse the
operational rank.

## Smallest exact falsifier

The single binary tangent record gives seven distinct columns as point records
but total rank only five. It therefore leaves a two-dimensional ambiguity for
source mixtures. This is the smallest exact witness against confusing
contextual point separation with joint linear faithfulness.

## Reopening condition

Derive a finite-energy tangent susceptibility and detector convolution from
each protector action. Compute the rank after gauge-boson mass, defect tension,
finite coherence, resolution, and rational-holonomy uncertainty are included.
Identification authority requires the implemented—not merely algebraically
spanned—response to retain rank seven on an enlarged rival grammar.

## Verification

```text
python research/flavor/checkers/wp162_holonomy_tangent_complement.py
```

The dependency-free exact checker writes the JSON result and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The complementary tangent direction directly targeted WP161's first
nonfaithful arrow. The confound was that infinitesimal control is formal until
instrumented.

Frozen optionality snapshot: seven sources, one binary tangent probe, two
mixed tangent-order probes, expected ranks five through seven, 12 checks, and
no physical instrument.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. One binary probe split every point class but left a two-dimensional
mixture kernel. Two additional source-conditioned moments killed that kernel
exactly. The mathematical complement is progressive; no finite-energy
actuator, detector convolution, or open-rival instrument was constructed.

