# Direct carrier-energy audit: slots are not excitation eigenvalues

## Source and scope

Return to the existing carrier rather than compiling another controller. The
shared-reference slot and Gram-energy checkers are freshly rerun. Their data are

    G = 11 I4 + ones(4,4),
    v_(i,j) = e_j-e_i,
    state feature = e_i, i != reference.

There are1836 labelled comparison instances, but counting labels does not specify
a Hamiltonian. This forward-realization audit tests an explicit Gram-generated
candidate and computes its complete nonzero spectrum exactly. No measured mass
or controller coupling is used to select that spectrum.

## Keep the two comparison types

Map a labelled slot into tensor features:

    outer/arrow-pair -> v_outer tensor v_a tensor v_b,
    outer/state-pair -> v_outer tensor e_a tensor e_b.

Keep the two types in separate tagged feature blocks. Call this map F from the
1836-dimensional label space into two copies of the64-dimensional tensor space.
Use M=G tensor G tensor G on each block. On an orthonormal LABEL basis, a positive
candidate energy operator is

    H_slot = F^dagger M F.

This is a conditional Hamiltonian choice, not a theorem that a metric generates
physical time evolution. Its construction is fully specified so it can be tested.

All directed-arrow vectors span the three-dimensional standard carrier subspace.
Consequently the arrow block has rank3^3=27. The three nonreference state features
are independent, so the state block also has rank27. Their tags keep them
independent: total rank54, with1782 zero-energy label directions in H_slot.

Exact elimination checks the full1836 columns. If the two tags are instead
identified in a common tensor space, the rank is42: the two27-dimensional images
intersect in dimension12. That identification is a different realization, not a
license to discard the original comparison types.

## Exact spectrum

The directed-arrow frame operator is

    S = sum_e v_e v_e^T = 8 I4 - 2 ones(4,4).

S G has eigenvalue88 on the three-dimensional standard subspace. For the
nonreference state frame R=diag(0,1,1,1), the nonzero eigenvalues of R G are14,11,11.
The nonzero spectra of F^dagger M F and F F^dagger M agree. Tensor products give:

| Energy eigenvalue | Multiplicity | Ratio to smallest positive eigenvalue |
|---|---:|---:|
|10648|12|1|
|13552|12|14/11|
|17248|3|196/121|
|681472|27|64|
|0|1782|0|

The numbers use the specified dimensionless Gram normalization; no MeV unit or
electron identification is derived.1836 is not a ratio of a nonzero eigenvalue
to the smallest one in this candidate. Its largest such ratio is64.

The trace is18741888. Dividing it by the smallest positive eigenvalue gives
212976/121, reproducing the earlier conditional Gram-energy SUM ratio. A trace
is a sum of eigenvalues, not the energy gap of a particular particle.

## Why this does not refute retained path resources

Opposite outer arrows with the same inner feature cancel coherently. The checker
exhibits that kernel direction explicitly. A retained-record implementation can
distinguish both histories and charge positive cost for each traversal. Such an
implementation need not factor its energy through F and is not ruled out here.

However, independent record energies are then additional physical data. Replacing
H_slot by its diagonal discards coherent cross terms; replacing it by the identity
also normalizes unequal raw features. Neither operation follows merely from the
Gram matrix. The prospective charge-locking circuit supplied one such additional
implementation, but selected its charging law externally.

## Metric versus dynamics

Even on the original four-dimensional carrier, permutation symmetry and G do not
select one energy generator. With P0=ones(4,4)/4 and P1=I-P0, every

    H = a P0 + b P1

is permutation-invariant and self-adjoint for the G inner product when a,b are
real. Positivity only constrains their signs. Treating G as a quadratic energy
with G also the kinetic metric yields generator I; treating G as an operator
in the Euclidean metric yields eigenvalues15 and11. These are different physical
choices. None follows from a label count alone.

## Verification and outcome

    python research/nima/checkers/check_mass_carrier_gram_spectrum.py
    python research/aspect/scc/scc.py check nima-mass-carrier-gram-spectrum

All ranks, frame eigenvector checks, multiplicities, trace identities and ratios
use exact integer/rational arithmetic. No1836-square numerical diagonalization
is needed. Report: `results/mass-carrier-gram-spectrum.json`.

The direct static carrier realization does not supply the proposed mass gap.
The outstanding source input is a physical operation/action that retains the
comparison records, fixes their energy metric and selects a conserved particle
sector. A controller can demonstrate possibility, but cannot supply that law by
being recompiled. The existing1836 expression remains a comparison count with a
conditional energy interpretation, not a derived proton/electron mass ratio.
