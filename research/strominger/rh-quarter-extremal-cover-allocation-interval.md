# Collective Hall slack is the exact central-allocation interval width

## Question

Can the extremal min-cut be converted into an explicit local transport certificate?

## Claim boundary

Yes. Let \(x\) be central supply sent to the left demand. Exact feasibility is

\[
d_0-p_0\leq x\leq p_1+p_2-d_1.
\]

The interval width equals the collective Hall slack exactly. Its midpoint is an integer in common-scale coordinates and gives a strict interior flow satisfying both demands and every supply capacity.

At the midpoint, the central supply is exhausted and the two endpoint supplies retain equal unused mass. Each equals half the collective slack. This equality is not an extra source symmetry: it follows algebraically from choosing the midpoint.

## Disposition

The opaque extremal cut now has a canonical exact flow. Extract a reusable symbolic five-vertex path lemma: the three Hall inequalities are necessary and sufficient; interval width is collective slack; and the midpoint uniquely maximizes the minimum endpoint residual. Include deliberate failures for each cut. This local theorem is a candidate building block for an all-order Hasse decomposition, not evidence that all larger cut graphs decompose into paths.
