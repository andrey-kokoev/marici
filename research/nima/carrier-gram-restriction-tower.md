# A fixed-carrier Gram restriction tower

## Source audit and explicit probe realization

The existing check_gram_from_geometry.py states diagonal (N-1)! and
off-diagonal (N-2)!, attributing them to counts of sigma(i)=j. That attribution
is incorrect: sigma(i)=j has (N-1)! solutions for every i,j.

The stated entries do have a concrete probe realization. On S12 choose
f_i(sigma)=1 if sigma fixes i, and zero otherwise. The counting inner product
gives <f_i,f_i>=11! and <f_i,f_j>=10! for i different from j.
This realizes the numerical Gram already used in the source. It adds an
explicit probe choice; it does not establish its uniqueness or physical role.

Divide by 10! once. The fixed ambient Gram is G12=10I+J.
Let V_r be the span of the first r probes inside this same function space.
The induced Gram at every rung is G_r=10I_r+J_r. Its eigenvalues are
r+10 on the common coefficient direction and 10 on r-1 contrast directions.
These are eigenvalues of the coefficient-space norm matrix, not excitation
frequencies or Hamiltonian energies.

## Gram-orthogonal restriction

For a coefficient vector x in V_r, the projection into V_(r-1) has coefficients

    y_i = x_i + x_r/(r+9),  i=1,...,r-1.

Simply deleting x_r is not an orthogonal projection because the probes overlap.
The removed orthogonal residual has squared norm

    D_r = [10(r+10)/(r+9)] x_r^2.

Thus

    x^T G_r x = y^T G_(r-1) y + D_r.

One may retain the signed record sqrt(10(r+10)/(r+9))*x_r to reconstruct the
input. The direct top-to-r projection is

    y_i = x_i + (sum_{j=r+1}^{12} x_j)/(r+10).

Nested projections compose exactly. Successive orthogonal residuals provide
a conserved retained-plus-record norm budget.

## Rung spectra

| r | Common Gram eigenvalue | Contrast eigenvalue | Contrast multiplicity |
|---:|---:|---:|---:|
| 12 | 22 | 10 | 11 |
| 11 | 21 | 10 | 10 |
| 10 | 20 | 10 | 9 |
| 9 | 19 | 10 | 8 |
| 8 | 18 | 10 | 7 |
| 7 | 17 | 10 | 6 |
| 6 | 16 | 10 | 5 |
| 5 | 15 | 10 | 4 |
| 4 | 14 | 10 | 3 |

The coordinate Gram spectrum is not the four-number assignment 12,11,4,10.
This construction therefore does not justify labelling those four numbers
as eigenvalues of this Gram operator.

## Distribution needed for linear descent

Isotropy in the physical Gram inner product corresponds to coefficient
second moment C=G12^-1, not C=I. Since

    G12^-1 = I/10 - J/220,

an orthogonal projection onto V_r has mean squared norm r, compared with
12 at the top. Consequently E_r/E_12=r/12 follows if energy is proportional
to this norm with a fixed coefficient and the excitation is metric-isotropic.
The exact state-dependent decrease remains D_r above.

## Fixed carrier versus rebuilt carriers

Rebuilding stabilizer probes on each S_r gives a different Gram family:

    raw G_r = (r-2)! [(r-2)I+J].

Normalizing each rung by its own (r-2)! produces common eigenvalue 2r-2 and
contrast eigenvalue r-2. These matrices are not the principal restrictions
of a single fixed G12. Rung-dependent factorial factors cannot be interpreted
as physical energy decay without a measure and normalization transport law.

## Scope and next construction

This supplies explicit restriction maps and a positive quadratic budget from
one realization of the documented carrier Gram. It replaces coordinate deletion
with the correct Gram-orthogonal projection. There is still no Hamiltonian,
kinetic form, time evolution, or map to the separate six-coordinate comparison
prototype. Choosing the norm as energy is an additional dynamical assumption.
Particle identifications and GeV calibration remain unestablished.

Verification:

    python research/nima/checkers/check_carrier_gram_tower.py

The checker audits permutation counts through S7, then uses exact rational
arithmetic for all tower projections, conservation identities, composition,
Gram spectra, and metric-isotropic mean budgets. It writes no result artifacts.
