# A complete neutral-mediator interaction restores the heavier-belt ordering

## Result

The complete scalar-field model below gives a heavier belt with one shared law, including the mediator's energy and the full induced self-energy. No proton-specific or belt-specific offset is introduced.

For the fixed rule Delta=1, g=1/2, the certified result is

    0.13964821899185 < (E_belt-E_proton)/E_star < 0.13964821901016.

The bound includes the infinite oscillator tail. It is not just a finite-cutoff eigenvalue.

## What is reused and what is added

Reused source data: the all-face profiles constructed in `source-channel-closure-and-all-face-dressing.md` and checked in `results/all_face_contact.json`. Both carriers have six actual cross-face contacts. Their normalized equal-phase sums W_s have spectra

    proton: poles (0), weights (1),
    belt: poles (0,4485/3292), weights (2386/4485,2099/4485).

Thus W_proton is its coherent return. W_belt is not: it combines a coherent mode with a positive-energy collective mode.

Added interaction input: one neutral scalar Fock mediator per occupied particle sector, with the same spacing and vertex rule in both sectors. The spacing is E_star, the elementary reference gap; the field vertex is half that unit. This is a new uniform field construction, not a claim that the old carrier projectors already implement an oscillator. The actual source supplies the contact addresses, metrics and profile, not the physical mediator.

The elementary spinor defect gap and the elementary coherent-sector rest offset remain separate. This calculation uses the gap as its reference, without equating it to the electron rest energy.

## Complete Hamiltonian

Let P_s=|W_s><W_s|. In elementary-gap units define

    H_s = mu I + K_s + Delta a^dagger a + g P_s(a+a^dagger).

Here a acts only on the mediator. All terms act as I_2 on the logical spin. Species number, Q and B are fixed within each particle sector; the vertex displaces a neutral field rather than converting one particle into another. The common empty reference is a separate zero-particle vacuum. Mediator occupation need not be conserved.

The shared rule tested is Delta=1, g=1/2. Neither parameter was chosen from a measured mass. The two carrier sectors have identical oscillator and bare-offset data.

The full energy can be written

    H_s-mu = K_s
             + Delta(a+g P_s/Delta)^dagger(a+g P_s/Delta)
             - (g^2/Delta) P_s.

This retains the positive field energy, displacement cost and negative induced contact term. It is bounded below by -g^2/Delta. No negative constant has been independently added to match a target.

Unlike the failed elementary-gap exchange projector, this is a field-displacement interaction, not an auxiliary/contact swap with its mandatory |W><W|/2 diagonal term. The previous failed rule remains unchanged as a control.

## Exact ordering for every shared Delta>0 and nonzero g

For the proton, P_proton projects onto a native zero mode. The coherent carrier and oscillator coherent state of amplitude -g/Delta attain

    E_proton = mu-g^2/Delta.

For the belt, attaining that lower bound would require simultaneously

    K_belt psi=0,
    P_belt psi=psi,
    (a+g P_belt/Delta)psi=0.

The first two conditions are incompatible because W_belt is not its coherent zero mode. The finite carrier coupled to a confining oscillator has compact resolvent, so its ground infimum is attained. Therefore

    E_belt > E_proton.

This argument retains the full operator. It does not replace K_belt by its expectation or assume that K_belt commutes with P_belt.

Both shifts are attractive relative to the same bare offset. A product trial using the coherent belt mode, with overlap squared r=2386/4485 and optimized oscillator displacement -g*r/Delta, gives

    E_belt-mu <= -g^2*r^2/Delta < 0.

The empty reference remains below both particle sectors whenever mu>g^2/Delta. The common mu cancels from their difference.

## Infinite-oscillator verification

Use an unnormalized Fock basis with metric n! and spectral carrier metric diag(r,1-r). The annihilation/creation and projector matrices then have rational coefficients. Exact weighted Hermiticity is checked before every rational LDL test.

For a cutoff M, the retained principal section gives a variational upper bound. On the omitted levels n>=M+1, the oscillator and vertex obey

    H_tail >= Delta*N/2-2*g^2/Delta.

Let L=Delta*(M+1)/2-2*g^2/Delta. For a test energy lambda<L, Schur elimination bounds the tail correction at retained level M by

    g^2*(M+1)/(L-lambda) * P_s.

Positive definiteness of the retained H-lambda minus this correction certifies H_full>lambda. Thus the lower bound is for the infinite oscillator. No truncated canonical-commutator identity is used.

| Retained maximum occupation | Belt-minus-proton lower | Upper |
|---|---:|---:|
| 4 | 0.13963857561771 | 0.13965350516872 |
| 8 | 0.13964821899185 | 0.13964821901016 |

The exact proton shift is -1/4. The belt shift is between -0.11035178100815 and -0.11035178098984. Native dark carrier modes remain uncoupled and nonnegative, so they cannot undercut these negative ground energies.

## Next connection

This closes the complete-interaction ordering test for the stated field law. It does not derive the neutral Fock field or half-gap vertex from the native operations, nor select the elementary rest offset. Those are the next constructor inputs, not adjustable species corrections.

This is single-particle dressing, not yet deuterium binding. A common mediator coupling to two occupied carriers introduces a cross term upon displacement, but its spatial profile, separation limit and spin channel must be constructed before that term can be used as a nuclear interaction. The isotope breakup reference must remain identical.

## Reproduce

    python research/voevodsky/checkers/check_all_face_contact.py
    python research/voevodsky/checkers/check_neutral_mediator_mass_bridge.py

Results: `results/neutral_mediator_mass_bridge.json`. The checker retains the all-face source hash, rational global-energy intervals, cutoff controls and shared input parameters. No empirical mass data enter the calculation.
