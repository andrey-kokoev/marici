# Persistent seam occupation: a positive belt energy increment with the return retained

## Result

We have coupled the actual 21 belt seam projectors to neutral occupation registers. This supplies an explicit candidate for the missing link

    formed interfaces -> persistent occupations -> stored energy.

Under the stated coupling and a simple stability inequality:

- the existing belt return remains the unique carrier ground state;
- the 21 registers are occupied when record mixing is zero;
- coherent empty/occupied mixing changes their occupation and energy but does not destroy the carrier return;
- the belt has a strictly positive extra energy relative to the same registers in the inactive reference configuration.

This is a constructed interface-dressing mechanism. Its positive sign does not require assigning Delta_L>Delta_G. The physical identification of its registers and their elementary energy scale remains to be connected to the other particle sectors.

This reuses Nima's existing `research/nima/mass-comparison-charged-core-dressing.md` occupation Hamiltonian and its transverse-mixing formula. The new work is to replace its abstract core-only control by the actual local satisfied-interface controls, and to prove that these noncommuting carrier couplings preserve the constructed belt return under the stated bound. The two-level dressing formula itself is not a new discovery.

## 1. Start with the actual formation constraints

The preceding native-operation construction supplied:

- a positive native phase/alignment energy H_native;
- 21 normalized shared-edge mismatch projectors P_e;
- the exact one-dimensional common kernel

    ker(H_native) intersect intersection_e ker(P_e) = im(N).

Here e labels a seam, not an electron. The P_e are the actual projectors reconstructed from the six-triangle graphs inside each paired belt sector. They do not all commute. The checker explicitly exhibits that noncommutation and verifies P_e N=0 for every seam.

The threefold sector rotation permutes the projectors and their seam labels. All register parameters below are common across seams, so this symmetry is preserved.

We measure energies in one common unit in which the preceding native Hamiltonian is represented by one quarter of its stored 4H/pi matrix. The preceding normalized seam coefficient corresponds to kappa=1 in that convention. No conversion to MeV is selected.

## 2. Bond registers, not error bits

For each seam introduce a neutral two-level register with occupation n_e=0 or 1 and flip X_e. These registers describe a proposed persistent interface resource, not the transient syndrome bits used to record whether a constraint is violated.

Include a vacuum sector c=0 and a carrier-present sector c=1. Extend each P_e by zero on the vacuum. Define the satisfied-interface control

    S_e = c-P_e.

It vanishes in the vacuum; on a formed belt state it equals one. The carrier number c is conserved by the declared model. We are not deriving particle creation, charge, or baryon-number protection from this flag.

Use the same coupling at every seam:

    h_e = epsilon n_e + J(n_e-S_e)^2 - g X_e,

with epsilon>0, J>0 and g>=0. The complete carrier-sector energy is

    H = mu c + H_native + kappa sum_e P_e + sum_e h_e.

The bare contribution mu is retained explicitly. Inactive registers are included in the reference/vacuum, so energy differences include their own mixing energy rather than silently discarding it.

This rule declares that a satisfied physical interface should have its occupation register present. A missing register costs J; a present register costs epsilon. Conversely, a vacant carrier does not require an occupied seam. This is the additional interaction law being constructed and tested, not a theorem that every mathematical gluing carries such a register.

## 3. Exact one-register solution

On an inactive interface, S=0; on a satisfied interface, S=1. In the n=0,1 basis the two matrices are

    h_inactive = [[0, -g], [-g, epsilon+J]],
    h_matched  = [[J, -g], [-g, epsilon]].

Their lowest energies are

    lambda_v = (epsilon+J - sqrt((epsilon+J)^2+4g^2))/2,
    lambda_b = (epsilon+J - sqrt((J-epsilon)^2+4g^2))/2.

The relative energy of one matched interface is therefore

    delta = lambda_b-lambda_v
          = [sqrt((J+epsilon)^2+4g^2)
             - sqrt((J-epsilon)^2+4g^2)]/2.

For J>epsilon>0,

    0 < delta <= epsilon.

One way to see the sign without numerical approximation is

    delta = 2 epsilon J /
            [sqrt((J+epsilon)^2+4g^2)
             + sqrt((J-epsilon)^2+4g^2)].

At g=0, lambda_v=0 and lambda_b=epsilon: the matched register is fully occupied. At positive g its ground state is a coherent mixture. Its occupation is

    <n>_matched = [1+(J-epsilon)/sqrt((J-epsilon)^2+4g^2)]/2,

while the inactive register has

    <n>_inactive = [1-(J+epsilon)/sqrt((J+epsilon)^2+4g^2)]/2.

Thus persistence need not mean a fixed classical bit after record mixing is introduced.

## 4. Why all 21 interfaces retain the same coherent belt

For one seam, decompose its carrier space by P_e. The edge term is

    (I-P_e) tensor h_matched
    + P_e tensor (kappa I + h_inactive).

Subtract lambda_b. The residual is the sum of positive record excitation terms and

    (kappa-delta) P_e.

Consequently, if kappa>delta,

    H - mu - 21 lambda_b
      >= H_native + (kappa-delta) sum_e P_e >= 0.

This argument does not require the P_e to commute. The original N annihilates every carrier defect simultaneously. Tensoring its state with the same matched register ground state on all seams attains the lower bound.

Conversely, equality forces every P_e and H_native to vanish, hence forces the carrier into im(N). The local record ground states are unique, so the complete ground state in this declared carrier sector is unique too.

A convenient sufficient condition is

    J>epsilon>0, kappa>epsilon, g>=0.

It preserves the belt state for every nonnegative mixing g. The registers contribute a positive vacuum-subtracted energy while the formation constraints remain exactly satisfied.

This is stronger than merely adding a chosen constant to the final return: the same local interface coupling determines occupation, quantum mixing, the energy increment, and the penalty for abandoning a seam.

## 5. Belt–proton comparison and what is being held fixed

The current proton's operator-local groups are individual small triangles, so the preceding within-group interface construction adds no corresponding seam registers. The belt has 21.

For a comparison with equal bare carrier baselines and the same inactive-register reference, this mechanism supplies

    additional belt energy = 21 delta > 0.

The inactive registers may be included as spectators in the proton sector to place both comparisons in one register Hilbert space. Their energy is then the same as in the vacuum reference. The difference is activation by the actual belt interfaces, not a different choice of energy zero.

This is an extra contribution, not the complete neutron–proton mass formula. Different bare contributions, additional proton interfaces, other persistent records, or electromagnetic energies would need to be included in the same comparison. The initial 1836 baseline is not derived by these new seam registers.

The 21 registers correspond to the 21 actual seams, not just the 15 independent amplitude equations. Removing the six redundant-in-kernel seams preserves the selected carrier subspace but changes the proposed physical record network and its energy. That is a different implementation, not a coordinate relabelling. The register ontology therefore matters and must be tested against the intended retained source.

The registers are declared neutral: their occupation does not change any pre-existing core charge. This model does not itself construct the neutral-neutron charge assignment or its spin.

## 6. Discriminating control: defect records do not produce this increment

If instead the register couples to the mismatch itself,

    S_e=P_e,

then S_e=0 on the already formed state N. Every register has the inactive ground energy there. Its vacuum-subtracted contribution is zero.

More explicitly, the residual carrier penalty becomes (kappa+delta)P_e rather than (kappa-delta)P_e, and the selected carrier state remains N with inactive records. Thus both constructions can stabilize the same return, but only the **satisfied-interface resource** interpretation produces the positive occupation increment.

This is the concrete physical choice now exposed: is the record a persistent bond resource or an error/syndrome excitation? Those roles must not be conflated merely because both are attached to the same seam.

## 7. Exact checks and illustrative parameters

The checker reads the actual seam projectors and native energy from `native_operation_energy_lift_store.json`. It verifies their projection identities, noncommutation, common return, and threefold covariance. It then verifies exact two-level spectral projectors and energy identities for:

    epsilon=1/4, J=1/2, kappa=1,
    g=0, 1/8, 3/8.

The positive square roots lie in the existing exact number field. The corresponding 21-seam increments are

| g | Extra energy in the declared common units |
|---|---|
| 0 | 21/4 |
| 1/8 | 21(sqrt(10)-sqrt(2))/8 |
| 3/8 | 21(3sqrt(2)-sqrt(10))/8 |

These values are controls, not values fitted to neutron mass. The general positive-ground argument above establishes the many-register result symbolically; we do not enumerate a 36 times 2^21 matrix and do not claim to have performed such a diagonalization.

The new occupation model also does not assign a production rate or show that a closed system settles automatically into the ground state. It specifies the persistent sector and its energy once formed; a formation process must account for any exchanged energy and information.

## 8. Next synthesis step

The formation-to-occupation-to-energy chain now has an explicit candidate implementation on the actual belt interfaces. Its sign and stability follow once the common positive record gap, binding penalty, and satisfied-interface interpretation are declared.

The most consequential remaining identification is the elementary gap epsilon and the physical meaning of the neutral seam register. Connecting those registers to the existing elementary excitation and retained source records would determine whether this is the appropriate contribution to the neutron–proton difference, rather than treating delta as a number to fit.

## Reproduction

    python research/voevodsky/checkers/check_native_operation_energy_lift.py
    python research/voevodsky/checkers/check_seam_occupation_energy.py

Results: `research/voevodsky/results/seam_occupation_energy.json`.

The many-register bound is the written positive-operator proof above, supported by exact local spectral and source-coefficient checks. No Agda formalization, relativistic mass pole, measured mass prediction or electron normalization is claimed.
