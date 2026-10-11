# Whole-composite attachment changes the active state without reopening the first agreement

## Question

Move beyond appending marks: make the next comparison act on the retained composite's current comparison data. Reuse the reversible projection lift already supplied in `comparison-update-dynamics-and-energy-normalization.md`. Active obligation: attachment compatibility, recovery and transport between two construction orders. This is a declared affine comparison model, not an electronic Hamiltonian or a native derivation of a physical attachment rule.

## Actual state update

Let q=(x0,x1,x2) hold core and two witness comparison coordinates. The first agreement is x0=x1, with normal r=(1,-1,0). The second witness compares to the entire pair through

\[
x_2=\frac{x_0+x_1}{2},\qquad s=(1,1,-2).
\]

The normals are orthogonal. With a fresh record z=0, the prior update rule is

\[
a=\frac{r\cdot q}{r\cdot r},\qquad
q'=q+r(z-a),\qquad z'=a.
\]

It stores the removed longitudinal coordinate rather than deleting it. Applying the same transformation again with the populated record reverses the operation. Its conserved quadratic budget is

\[
\|q'\|^2+(r\cdot r)(z')^2=\|q\|^2+(r\cdot r)z^2.
\]

After enforcing r dot q=0, the s update preserves that agreement since r dot s=0. It then enforces the second agreement. Both together yield the common barycenter (mean(q),mean(q),mean(q)). All updates preserve the coordinate sum.

Within this stated affine model, a second correction preserving x0=x1 and the total sum must have direction (d,d,-2d). Requiring the new whole-pair comparison fixes d. These conditions determine the second correction; the conditions themselves are declared modeling inputs, not derived physical laws.

## Opposite attachment order and record transport

The opposite order uses r'=(1,0,-1) and s'=(1,-2,1). Its final active state is the same barycenter, but its intermediate state and retained mismatches generally differ.

For input (1,2,4):

| Quantity | First pair (0,1) | First pair (0,2) |
|---|---|---|
| Intermediate state | (3/2,3/2,4) | (5/2,2,5/2) |
| Final state | (7/3,7/3,7/3) | (7/3,7/3,7/3) |
| Retained mismatch coordinates | (-1/2,-5/6) | (-3/2,1/6) |
| Stagewise transferred squared budget | (1/2,25/6) | (9/2,1/6) |

Both budgets sum to 14/3. Writing the first records as (a,b), the other records satisfy

\[
\begin{pmatrix}a'\\b'\end{pmatrix}
=\frac12\begin{pmatrix}1&3\\1&-1\end{pmatrix}
\begin{pmatrix}a\\b\end{pmatrix}.
\]

This map squares to identity and preserves 2a^2+6b^2. It is an explicit invertible comparison of retained records, not a claim that they are equal or may be erased. This realizes the earlier distinction between a common barycentric representative and different retained construction paths.

## Discriminating control

If the second comparison instead acts only on the original core and the new witness, its normal is (1,0,-1), not (1,1,-2). Starting with (1,0,0), first comparison gives (1/2,1/2,0). That core-only second update gives (1/4,1/2,1/4), reopening the first agreement by -1/4. Whole-composite comparison instead yields (1/3,1/3,1/3) and preserves it.

Thus the operator's distinction between witnessing the core and witnessing the retained composite makes an operational difference in this model. It does not establish which operation physical electrons perform.

## Disposition and verification

The active comparison model exhibits state response, exact recovery and order-dependent record allocation. Its final center and total quadratic budget are order independent. The orthogonal comparison normals provide a specific compatibility criterion for the second update; the order comparison is carried by an isometry of records. No atomic mass, binding energy, physical time or unique native selection of the affine law is inferred.

`python research/nima/checkers/check_nested_active_comparison.py` passed via `structured_command_execution:e_32876_1791227799539656700_48`. Tests cover 125 rational input fixtures plus exact linear basis checks, inverse recovery, the record isometry and the core-only hostile. General statements also follow from the displayed linear identities. Results: `results/nested-active-comparison.json`. No commit or publication is claimed.
