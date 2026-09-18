# qRB microstep 146: residue-corrected comparison checklist

Before testing translate-Gram positivity, the continued source kernel must pass four checks:

1. endpoint gauge agreement under `xi=-i d/(4 sigma)`;
2. symmetric prime continuation;
3. gamma contour residues at every crossed pole;
4. Hermitian branch symmetry under `d -> -d`.

Only after these pass may one form

$$
K_t(a_i,a_j)=\mathcal K_t(a_i-a_j)
$$

and test its Toeplitz minors.

A failure at any earlier stage is a normalization/interface defect, not evidence against positivity. The current repository has algebraic endpoint and prime checks, but not the complete residue-corrected gamma verification.

Status: pre-positivity checklist assembled; gamma residue implementation remains the next concrete calculation.
