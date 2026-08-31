# Overlap-monitor null-accounting gate: WP1049

## Question

Does an overlap monitor certify `physical16` cofinality without null-retaining
loss accounting?

## Monitor-loss coordinate

WP1048 gives two ways to close the cofinality gate: derive one shared final
state, or measure the overlap. A monitor of the overlap has its own collection
efficiency. Write

\[
H=\eta c,
\]

where \(c\) is the coherent final-state overlap and \(\eta\) is the monitor
collection efficiency. Use coordinates

\[
(B,\mathcal L,g,\nu,d,c,\eta).
\]

The WP1044--WP1048 rows plus \(H\) have rank six on seven coordinates. Adding
a null-loss or efficiency row for \(\eta\) raises the rank to seven.

## Exact collision without null accounting

The partial-support packet

\[
(B,\mathcal L,g,\nu,d,c,\eta)=(0,4,1,1,1,1/2,1)
\]

and the full-support packet with lossy monitor

\[
(B,\mathcal L,g,\nu,d,c,\eta)=(0,1,2,1,1,1,1/2)
\]

share all records before the monitor loss is retained:

\[
B=0,
\qquad
S=4,
\qquad
D=8,
\qquad
V_{\rm ref}=1,
\qquad
\text{epoch}=1,
\qquad
H=1/2.
\]

If \(H\) is decoded as \(c\) by assuming \(\eta=1\), the full-support lossy
packet is assigned

\[
(\mathcal L,g)=(4,1)
\]

instead of its actual \((1,2)\).

## Null-retaining reconstruction

With \(\eta\) retained,

\[
c=\frac{H}{\eta},
\qquad
 g=\frac{4\nu d(H/\eta)(S-B)}{D}.
\]

The full-support lossy packet then reconstructs \((c,\mathcal L,g)=(1,1,2)\).

## Classification

This is a conditional null-accounting gate. An overlap monitor measures
cofinality only after monitor loss and null events are retained or
independently calibrated. Otherwise monitor inefficiency is another gain-like
fiber.

## Disposition

Productive. WP1048's overlap-monitor alternative now has a minimal requirement:
a `physical16` cofinality monitor with null-complete outcome space, efficiency
calibration, and proof that its null channel is not another Flavor-gain path.

Checker: `research/flavor/checkers/wp1049_overlap_monitor_null_accounting_gate.py`

Result: `results/wp1049_overlap_monitor_null_accounting_gate.json`
