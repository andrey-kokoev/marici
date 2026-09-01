# Brane-coupling representation fiber: WP1117

## Question

What representation-theoretic constraints apply to the missing
brane-to-physical16 coupling matrix?

## Row orbit data

The six bulk branches have dimensions

\[
(6,8,1,4,2,2),\qquad \sum d_i=23,
\]

and five row orbits:

\[
[6],\quad [8],\quad [1],\quad [4],\quad [2_a,2_b].
\]

The unresolved localized-quartet choice leaves an orbit of two candidate
kernels. The coupling matrix has shape \(6\times6\), hence \(36\) entries.

## Gauge-invariance rule

A source-invariant coupling \(K_{eb}\) may be nonzero only when the tensor
product of branch \(b\) with event \(e\) contains the source singlet. However,
WP1052's six physical16 event roles currently have no
\(SU(4)\times SU(2)\times U(1)\) representation assignment. Therefore zero
singlet constraints are evaluable and zero coupling entries are known.

## Classification

Conditional gate. Row representation orbits are necessary constraints, not a
coupling matrix. The next gate is a source representation assignment for the
six event roles.

Checker: `research/flavor/checkers/wp1117_brane_coupling_representation_fiber.py`

Result: `results/wp1117_brane_coupling_representation_fiber.json`
