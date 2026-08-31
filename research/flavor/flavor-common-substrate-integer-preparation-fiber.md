# Common-substrate integer preparation fiber: WP1038

## Question

Does placing WP1036's compatible integer labels in one finite common substrate
select \((k,C)=(2,23)\)?

## Same-substrate hostile

Freeze the smallest positive-integer neighborhood on the compatible
nonprimitive slice:

\[
D=\{(2,22),(2,23),(2,24)\}.
\]

Two positive-gapped quadratic preparations on this same substrate are

\[
E_{23}(k,C)=(C-23)^2,
\qquad
E_{22}(k,C)=(C-22)^2.
\]

They have the same polynomial degree and the same unit gap above their
minimum. The first selects \((2,23)\); the second selects \((2,22)\). The
selected labels have different pole coefficients:

\[
h(2,23)-h(2,22)=\frac{6\pi^2}{1367}.
\]

Thus common finite support and a positive-gapped preparation grammar do not
select the compatible label. The selecting order or energy is additional
source data.

## Translation fiber

A symmetric middle-of-three law also fails to select the absolute coefficient.
On \(\{22,23,24\}\) it selects \(23\), while on \(\{21,22,23\}\) it selects
\(22\). The rule fixes a relative slot only; the absolute origin of the
integer domain remains the missing source datum.

## Classification

The first nonfaithful arrow is

\[
\{\text{common finite source support and gapped preparation grammar}\}
\longrightarrow
\{\text{source-derived absolute label order}\}.
\]

A detector or fitted compatibility interval can identify which prepared label
matches the readout, but it cannot derive the preparation law.

## Disposition

Negative for the bare common-substrate repair of WP1037. Reopening requires a
representation, topology, or locality theorem that derives the integer domain,
its absolute origin, and a unique energy/order selecting \(C=23\) before
threshold transport or `physical16` instrumentation is invoked.

Checker: `research/flavor/checkers/wp1038_common_substrate_integer_preparation_fiber.py`

Result: `results/wp1038_common_substrate_integer_preparation_fiber.json`
