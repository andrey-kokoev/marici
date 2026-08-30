# WP161 — rational-holonomy aliasing audit

## Bounded question

Does WP160's complete winding-return tower identify the protector group after
the continuous rival family is enlarged to include rational \(U(1)\)
holonomies?

## Enlarged rival grammar

Retain the discrete protectors \(\mathbb Z_3,\mathbb Z_5,\mathbb Z_7\), and add
continuous \(U(1)_F\) configurations whose holonomies have exact orders
3, 5, and 7, plus one irrational non-returning holonomy.

A \(U(1)\) phase \(e^{2\pi i p/n}\), with \(p\) coprime to \(n\), obeys

\[
h^m=1\quad\Longleftrightarrow\quad n\mid m.
\]

Therefore its return record is exactly

\[
R_m=\mathbf 1_{n\mid m},
\]

the same as WP160's primitive \(\mathbb Z_n\) defect.

## Exact contextual partition

The complete return tower produces four classes:

\[
\{\mathbb Z_3,U(1)_{\mathrm{ord},3}\},
\]

\[
\{\mathbb Z_5,U(1)_{\mathrm{ord},5}\},
\]

\[
\{\mathbb Z_7,U(1)_{\mathrm{ord},7}\},
\]

and

\[
\{U(1)_{\mathrm{irrational}}\}.
\]

The normalized response has rank four on seven constructors, leaving an exact
three-dimensional source kernel. Computing through winding 105 gives the same
rank as winding seven. This is not a finite-depth accident: each paired source
uses the identical divisibility rule, so no number of return predicates can
separate it.

## First nonfaithful arrow

The return probe factors as

\[
\text{protector source}
\longrightarrow
\text{order of one chosen holonomy}
\longrightarrow
\{R_m\}_{m\geq0}.
\]

The first arrow is nonfaithful. A finite discrete gauge group and a continuous
group element can have the same cyclic subgroup and hence the same return
order. The full tower is faithful on holonomy order, not on protector source.

## Typing

- **Admitted source domain:** three discrete protectors, three rational
  continuous holonomies, and one irrational continuous holonomy.
- **Faithful flavor quotient:** `physical16` remains unchanged.
- **Source-authorized probe family:** the complete normalized winding-return
  tower, conditional on the defect experiment.
- **Contextual partition:** three discrete/continuous pairs and one irrational
  singleton.
- **Separation:** holonomy orders are separated; protector group types are not.
- **Selection:** none.
- **Rigidification:** return order rigidifies one cyclic probe presentation.
- **Descent:** the order record is invariant under gauge presentation, but it
  factors through a nonfaithful source-to-holonomy map.
- **Reference port:** the defect remains a new relational reference
  construction.
- **Physical instrument:** absent.

## Smallest exact falsifier

\[
\mathbb Z_3
\quad\text{versus}\quad
U(1)\text{ holonomy }e^{2\pi i/3}.
\]

Both return exactly at windings divisible by three. Their entire return towers
are identical.

## Required complementary probe

Identification now requires information not factored through a single cyclic
holonomy, for example:

- the inventory and fusion of distinct defect sectors;
- continuous small-angle holonomy deformations available only in \(U(1)\);
- a gauge-boson or Higgs threshold tied to the continuous constructor;
- braiding against a source-derived complete charge family.

The complementary probe must be physically executable and source-derived. An
algebraic label declaring the ambient group is not an instrument.

## Verification

```text
python research/flavor/checkers/wp161_rational_holonomy_aliasing.py
```

The dependency-free exact checker writes the JSON result and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The rule-level alias promised a decisive hostile pair. The confound was
the physical stability and accessibility of rational continuous holonomies.

Frozen optionality snapshot: seven sources, three expected alias pairs, one
irrational singleton, a winding tower through 105, 12 checks, and no physical
instrument.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. WP160's four singleton classes expanded to three exact pairs plus one
singleton. The rank stayed four while the source kernel grew to dimension
three. The first nonfaithful arrow was localized to source-to-holonomy-order.
No complementary probe or physical instrument was constructed.

