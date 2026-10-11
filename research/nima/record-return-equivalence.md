# Left/right return laws are equivalent after transporting bank coordinates

## Question

The selection audit found two conservative, invertible order-six updates using L_left=R tensor I and L_right=I tensor R. Are these necessarily inequivalent response mechanisms?

No. The existing Clifford multiplication table supplies an explicit orthogonal conjugacy preserving the active carrier and sewing readout. The interpretation of that conjugacy as an admissible source presentation change remains distinct from reversing directed source paths.

## Constructed comparison

Write the existing basis multiplication as

    e_i e_j = sigma(i,j) e_(i xor j).

Define the signed factor interchange

    B(e_i tensor e_j) = sigma(i,j)*sigma(j,i) e_j tensor e_i.

Its signs come from the existing product, not a fitted coefficient. The exact checker verifies on the full sixteen-dimensional bank:

    B^2=I,  B^T B=I,  C B=C,
    B L_left=L_right B.

The first three identities also imply B C^T=C^T, so S=diag(I4,B) commutes with the carrier-record exchange. Hence on the complete twenty-dimensional state:

    S U_left = U_right S,
    U_right = S U_left S.

For O(x,t)=(x,Ct), O S=O. Induction gives

    O U_right^n S = O U_left^n

for every nonnegative n. The full-space matrix identities are checked exactly; powers zero through twelve are also tested directly. This is not an extrapolation from those samples.

## Consequence for the prior examples

The ordinary/twisted tetrahedral banks 1 tensor 1 and e2 tensor e2 are fixed by B. Their observed trajectories therefore agree under the two laws at every step, not only at the initially tested response.

The previous separating input 1 tensor e1 is NOT fixed: B takes it to e1 tensor 1. Applying the right law to that transformed input gives the same next carrier as applying the left law to the original input. Holding the bank coordinates fixed while changing only the law compared different preparations relative to this equivalence.

## Keep the source roles separate

This is a numerical bank-coordinate transformation. The port adapter uses tensor order (later edge12, earlier edge01), corresponding to traversal 01 then 12. Literal execution 12 then 01 fails the endpoint match. Nothing in B constructs that reversed source route or identifies the original histories.

A consistent transported adapter is E_right(P)=B E_left(P), while retaining the same source package P, path labels and witnesses. Under that adapter transport the two numerical descriptions are observationally equivalent. If an application instead fixes the original coefficient interpretation of both ordered factors and disallows this transformation, the two fixed-adapter updates remain different. No source or physical admission policy is inferred merely from an orthogonal matrix.

## Disposition

The earlier countercandidate does not establish two inequivalent physical mechanisms. This particular left/right numerical ambiguity can be removed by the explicit readout-preserving equivalence, provided the adapter is transported with it. We have not selected the adapter, the metric, the exchange schedule or gravitational coefficients uniquely, and have not established a physical gauge principle.

## Verification

`python research/nima/checkers/check_record_return_equivalence.py` passed with exact Fraction matrices. Results: `results/record-return-equivalence.json`, including source digests and role-boundary controls. No prior update law was modified. No ledger entry, commit or publication is claimed.
