# Finite retained comparison: typed sectors, discriminator and assembly

This proof uses the user-selected cycle-defect K, zero vacuum extension, one
neutral record, g=1/2 and t=1. It concerns the frozen finite constructor, NOT a
physical theory selection. Full generator/readout derivations are in
`common-resource-accounting.v1.md`. The executable closure checker freshly
reruns those checks and their native dependencies rather than copying old ++ labels.

## 1. Typed number and charge operators

On matter V tensor conjugate(V) direct_sum vacuum, dim V=10, define c=I100 direct_sum 0.
The retained pair sector contains one object of each declared constituent type:

    n_left=c, n_right=c, n_pair=c, n_constituents=2c,
    Q_declared=q(n_left-n_right)=0,  n_record=I101 tensor |1><1|.

These are definitions on this truncated pair/vacuum space. There are no singly
occupied sectors here, and no claim that the constituent labels identify physical
electrons or positrons, fermionic exchange statistics, or an absolute electrical
charge unit. Both K and P (Pi or c-Pi) have zero vacuum cross blocks. Thus
[K,c]=[P,c]=0, so both Hamiltonians preserve all the declared matter-number and
charge operators. Empty matter is a reducing sector; neither rule annihilates
an occupied pair into vacuum.

Record occupation is different: [H,n_record]=-g P tensor [X,N], and
[X,N]=[[0,1],[-1,0]] is nonzero. Both projections have positive rank (1 and 99),
so both rules can change neutral record occupation on their active subspace.
The rival is dark only on the frozen scalar input, not on its full complement.

## 2. Separately stated variable-phase contract

The partner is the **declared conjugate copy**. Supply a global variable phase
z in U(1), with left weight +1 and conjugate-right weight -1:

    v -> z v, conjugate(w) -> z^(-1) conjugate(w).

Their tensor pair has Laurent weight 1+(-1)=0; vacuum and neutral record have
weight zero. The entire retained pair/vacuum space therefore carries the identity
under this supplied diagonal phase action. K, the two P choices and both joint
Hamiltonians are invariant. q above is an arbitrary common charge scale; neither
its value nor this external action is inferred from a frozen complex-linear
frame map. Independent constituent phases would give the pair their sum, not a
neutral invariant. No local spacetime gauge field or phase-dependent physical
interaction is asserted. This is a mathematical input-type convention, matching
the supplied conjugate partner, not resolution of physical U4/U5.

## 3. Same-input discriminator and readout

For every native choice the normalized scalar v=J(1,0,0,1)/sqrt(2) obeys
Pi v=v, (c-Pi)v=0 and Kv=epsilon v. Accounting derives the full bare diagonals,
then subtracts exactly the same g I202. The selected-K and readout checks give

    primary: p=(1-cos(sqrt(2)))/4,  rival: p=0,
    0.21 < p < 0.22.

The interval is rational and follows from adjacent alternating cosine sums
through powers 20 and 22. It is not an unvalidated floating-point separation.
Exact energy/readout results, retaining both outcomes and the matter state:

| Quantity | Primary | Rival on the scalar input |
|---|---|---|
| Record occupation | p | 0 |
| Pre-readout record energy | p | 0 |
| Pre-readout interaction energy | -p | 0 |
| Pre-readout full energy | epsilon | epsilon |
| Post-readout nonselective full energy | epsilon+p | epsilon |
| Conditional post-readout full energies | epsilon, epsilon+1 | epsilon |

Readout is explicitly ideal projective measurement of the neutral record. The
measurement interaction supplies the energy increase p in the modeled system;
the external apparatus is not constructed here. No complementary result or
carrier is erased. Conditional states are v tensor |0> and v tensor |1>.
The occupied-outcome branch of the rival has probability zero and is not assigned
a normalized conditional state. Exact epsilon is the selected source value 2e
for each native case, not a fitted species offset.

## 4. Complete conditional target

The fresh native adapter verifies Jdagger J=I, the native metric, both effective
cycle actions, scalar covariance and disclosed ambient-output incompatibilities.
K is the displayed-lift operator selected in the pinned source-K contract; both
rules use the same input, native choices, record pool, gap, coupling, time and
reference. All 202 coordinates remain. The common Hamiltonian derivation,
number/charge classification, separately declared phase action and certified
readout difference above give the requested retained conditional comparison.

This selects neither native doublet physically and does not silently replace
an incompatible ambient output action. Use the calculated effective action for
each doublet, as required by the frozen contract. Local covariance is checked;
no extra ambient identification or physical output channel is inferred.

The three conclusion receipts and the final target receipt have distinct attempt
nonces and existing budget costs. The umbrella proof bundle reuses this proof,
the accounting proof and fresh exact evidence. Its review is local assistant
mathematical/code review, not independent human review or kernel certification.

## Explicit limits

No physical admission, particle/photon identification, charge calibration,
source-selected external symmetry, exchange statistics, real-time calibration,
Maxwell propagation, native annihilation law, unique constructor or empirical
branching ratio follows. U1-U11 are not automatically resolved. A physical
selection between these rules requires the separate evidence gate.
