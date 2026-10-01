# What selects the return of the six-packet tower?

## Input and question

Keep the original occurrences

    [AB, BC, CA, BA, AD, DB].

Use the incoming-incidence operator already proposed for this vector, in the A,B,C,D family basis:

    M=[[0,1,1,0],
       [1,0,0,1],
       [0,1,0,0],
       [1,0,0,0]].

Its spectrum is phi=(1+sqrt(5))/2, psi=(1-sqrt(5))/2, omega=exp(2*pi*i/3), and conjugate(omega).

The proposed rung table advanced the complex phase at promotion boundaries and decoded at rung0. This audit tests whether retained regrouping or the operator itself supplies those steps. This four-family M is distinct from the single-triangle cyclic C in `spectral-promotion-nine-cycles.md`.

## 1. Grouping leaves the operator unchanged

Nine rounds of source grouping, unpacking and target grouping preserve all six occurrences and reconstruct exactly the same M. Sorting by retained occurrence IDs restores the original order.

Thus pure record regrouping does not apply M to a coefficient state or accumulate an eigenphase. Its effect is a change of data presentation. Repeated spectral promotion likewise preserves the same projector, since each spectral projector commutes with M. Executing the operator is a separate operation from representing it.

## 2. Exact spectral synthesis already provides a return

Let R exchange A with B and C with D. Then M commutes with R. The projectors

    P_even=(I+R)/2, P_odd=(I-R)/2

split the two real modes from the conjugate pair. Define

    K=(2M-I)P_even, L=(2M+I)P_odd.

They satisfy K²=5P_even and L²=-3P_odd. Hence the four spectral projectors are

    P_phi=(P_even+K/sqrt(5))/2,
    P_psi=(P_even-K/sqrt(5))/2,
    P_omega=(P_odd+L/(i*sqrt(3)))/2,
    P_conjugate=(P_odd-L/(i*sqrt(3)))/2.

Each is rank one and idempotent. Their eigenvalue-weighted sum is exactly M. In particular, the conjugate pair contributes (L-P_odd)/2 and the real pair contributes (K+P_even)/2.

The imaginary and irrational coefficients cancel in the reconstructed integer matrix. Its six nonzero entries recover the original six endpoint pairs; retained occurrence IDs restore their original order.

This reconstruction is available whenever the spectral descriptors and coordinate frame are retained. Waiting for a phase wrap is not required for the inverse law.

## 3. Applying M evolves amplitudes as well as phases

Under x_next=Mx, the four mode amplitudes multiply by phi, psi, omega and conjugate(omega). The phi mode grows and the magnitude of the psi mode contracts. Since phi>1, no positive power of M is the identity.

The complex pair has a three-step return. The complete raw operator has no finite return. This follows from its exact eigenvalues, independently of the nine checked powers.

## 4. The full spectral phase has a six-step period

Extracting the spectral phase lambda/abs(lambda) gives

    phi -> +1,
    psi -> -1,
    omega -> omega,
    conjugate(omega) -> conjugate(omega).

The negative real eigenvalue contributes phase pi per operator step. It was omitted by the proposed complex-only full-turn gate.

The resulting phase operator is

    U=M P_odd + K/sqrt(5).

It has U^6=I, U^3=P_odd+K/sqrt(5), and exact order six. Its positive spectral modulus is

    A=P_odd + sqrt(5)*P_even/2 + K/(2*sqrt(5)),
    M=UA=AU.

This is a spectral phase/modulus split. M is nonnormal in the counting inner product, and U is not orthogonal in that metric. It is not the Euclidean polar decomposition or a newly justified physical update law.

| Operator steps | Complex pair returned? | psi phase | All spectral phases returned? | Raw M returned? |
|---:|---|---:|---|---|
| 3 | yes | -1 | no | no |
| 6 | yes | +1 | yes | no |
| 9 | yes | -1 | no | no |

Thus a three-promotion gate based on omega alone is a gate for one sector. A gate on all spectral phases would require six actual phase updates. Neither timing is supplied by grouping or label promotion, and no rung number is selected by this calculation.

## Result

The robust closed operation is

    retained packets -> full spectral descriptors -> reconstructed packets.

Its closure follows from an exact inverse. It is compatible with preserving phase history separately. Assigning phase updates to specific rungs remains an additional schedule, and raw incidence dynamics cannot be replaced silently by phase-only dynamics.

The earlier single-triangle nine-round experiment and this six-packet experiment share history interfaces but have different spectra. In particular the current psi=-1 phase contribution has no analogue in the single triangle's common eigenvalue +1.

## Verification

    python research/nima/checkers/check_natural_tower_return.py

Fresh exact checks pass for nine regrouping rounds, all four algebraic spectral projectors and their eigenvalue equations, paired synthesis to the exact original incidence matrix, commutation of projectors with M, the phase/modulus split, the counting-metric nonorthogonality control, and nine raw/phase operator steps.

Artifact: `results/natural-tower-return.json`. No angle, mass value or target rung is fitted. The phase counter is reported as an operator-step diagnostic, not inserted into record promotion.
