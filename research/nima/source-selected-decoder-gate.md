# Source-selected decoder gate

## Question

The chain complex types syndromes and legal repair equivalence, but does it
select a physical recovery operation?

No. A decoder requires an additional source datum assigning relative cost or
likelihood to candidate histories.

## Exact finite audit

On the \(3\times3\) periodic toric lattice, fix the endpoint syndrome at
\((0,0)\) and \((1,1)\). Under uniform edge weight there are exactly two
minimum corrections of weight two. Their difference is one face boundary, so
they represent the same repair class. The cellular complex therefore
rigidifies the answer only up to local repair; it does not select a path.

Two different local edge-cost models each select a unique path, and the two
selected paths differ by that face boundary. Thus:

\[
\boxed{
\text{source cost selects a representative;
the complex supplies its equivalence type.}
}
\]

## Hostile logical failure

Syndrome plus an arbitrary cost model is still insufficient for physical
correction. Make a noncontractible detour artificially cheap. It has the same
endpoint syndrome but differs from the local correction by a nontrivial
homology class. The cost minimizer then applies a logical operation.

Therefore a valid decoder contract needs both:

1. a source-derived likelihood/cost model;
2. a declared logical objective or prior determining which homology class
   counts as successful recovery.

This separates two choices often hidden inside “minimum-weight decoding”:

\[
\text{representative selection within a repair class}
\quad\text{and}\quad
\text{logical-class selection across the syndrome fiber}.
\]

## Marici architecture

The result refines selector versus rigidifier:

- the chain complex and stabilizers rigidify histories into syndrome and
  logical classes;
- the noise model assigns weights to histories;
- the recovery objective selects a logical class;
- an optimization/tie-breaking protocol selects a representative;
- the physical instrument implements that representative.

None of these arrows is supplied by the others.

In software language, the quotient defines valid equivalence; the source
model supplies a query plan or cost function; the recovery policy states the
desired semantic result; and the executor performs one concrete update.

## Cross-sector implications

- A cosmological relative cycle is not selected by knowing its homology group;
  an integration contour and boundary prescription are additional source
  data.
- A flavor quotient does not select a texture representative; a dynamical or
  UV objective is required.
- Strominger's canonical kernel lift is stronger than a bare kernel class
  because the invertible prefix selects its representative, but physical
  activation still requires a readout objective.
- Constructible reference ports require both an accessible operator and a
  source task deciding when and how it is used.

## Falsifier

Any claimed canonical decoder must remain unchanged under every variation of
the cost, prior, tie-breaking, and implementation data that the frozen source
leaves unspecified. If two admissible choices select different operations,
the decoder is not source-canonical.

## Verification

- `research/nima/checkers/check_source_selected_decoder.py`
- dependency-free invocation:
  `python research/nima/checkers/check_source_selected_decoder.py`

