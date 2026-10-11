# Amplitude memory reaches occupation storage on one actual seam

## Result

An explicit isometric encoding and reversible write/read operation now connect
one actual belt seam's amplitude memory to the **existing** zero-mixing
occupation Hamiltonian. The coherent carrier survives the hold interval,
occupation is retained, and phase-corrected readout recovers the original data.
Write/read work is accounted for explicitly.

Extending the same encoding to all 21 seam memories succeeds as a **one-hot
memory code**, not as the fully occupied 21-bond ground state. That distinction
is the next precise boundary, rather than another missing generic mechanism.

## Single-seam encoding

Use the first stored seam, its metric projector P and a nonzero column u, with
h=||u||_G^2. Let w be the actual coherent vector, b=||w||_G^2. Then Pu=u,
Pw=0 and K w=0, where K is the existing stored native positive matrix in its
4H_native/pi convention, with the declared model coefficient.

The prior memory state is (q,z), with norm ||q||_G^2+h|z|^2. Encode it as

    E(q,z) = q|0> + z*w|1>.

Display the occupied-bit basis with squared norm h/b; this is a coordinate
normalization, not a new physical metric or energy fit. Equivalently, in an
orthonormal bit basis the second term is sqrt(h/b)*z*w|1>.

E is an isometry from 37 dimensions into the 72-dimensional carrier/bit space.
Its image is the complete carrier at bit zero plus the coherent line at bit one.
The checker verifies E^sharp E=I and E E^sharp=diag(I,N).

The previous swap lift U extends to a full unitary involution

    V = E U E^sharp + I-E E^sharp.

It exchanges u|0> and w|1> in the displayed metric, leaves w|0> unchanged and
acts as identity on the code complement. This construction uses the **full
coherent vector w**; a local physical implementation is not established.

## Existing hold law, no new fitted energy

Use epsilon=1/4, J=1/2, kappa=1, g=0 from the existing occupation fixture:

    H = K + kappa*P + epsilon*n + J*(n-(I-P))^2.

Its two blocks are

    H_0 = K + kappa*P + J*(I-P),
    H_1 = K + (kappa+J)*P + epsilon*I.

The code is invariant. A written input alpha*w+beta*u becomes

    w tensor (alpha|0> + beta|1>)

in the displayed bit frame, and holds as

    w tensor (alpha*exp(-i J t)|0> + beta*exp(-i epsilon t)|1>).

Thus the carrier stays on its coherent line and occupation probability stays

    beta^2*h / (alpha^2*b + beta^2*h)

for the real exact fixtures. General complex coefficients use squared magnitudes.
The register is a coherent superposition, not a forced classical occupied bit.
A pure mismatch input writes the fully occupied one-seam ground state with
normalized energy epsilon. Mixed inputs retain both amplitudes and relative phase.

Exact spectral block identities prove the hold formula for all t. The checker
also tests t=4*pi, where the two phases are +1 and -1, and corrects that phase
before inverse write. Omitting correction changes relative phase for mixed
inputs; on a pure occupied input it only changes a global sign.

## Energy and recovery accounting

The write operation does not commute with H. For the unnormalized input above,

    E_before = alpha^2*J*b + beta^2*(<u,K u>_G + kappa*h),
    E_written = alpha^2*J*b + beta^2*epsilon*h,
    W_write = beta^2*((epsilon-kappa)*h - <u,K u>_G).

W_write is negative at this fixture: writing retains positive register energy
while releasing the larger initial mismatch energy. The explicit reservoir
account gains -W_write. Hold preserves energy; phase correction has zero net
change of H. Exact read consumes the released amount, giving zero net work over
the complete write/hold/phase-correct/read cycle.

This is balanced control accounting, not a microscopic autonomous battery or a
claim that switching, timing and control preparation are free. The existing
uniform spectral rule pi*(I-V)/2 implements V, but is distinct from the hold H.

## The 21-seam extension and its limit

For the same direct-sum amplitude bank, encode record j as

    z_j -> z_j*w tensor |one_hot_j>.

The actual 21 projectors annihilate N despite not commuting. Consequently the
57-dimensional code (36 carrier coordinates plus 21 memories) is invariant
under the existing g=0 many-seam Hamiltonian. Its exact compressed blocks are

    H_empty = K + (kappa-J)*sum P_e + 21*J*I,
    H_memory = (20*J+epsilon)*I_21.

The total occupation operator on this code is itself a projector. Therefore
its normalized expectation is at most one, even when all 21 record amplitudes
are nonzero. Nonzero amplitude in every channel is not simultaneous occupation
of every binary register.

At the existing fixture:

- one-hot memory energy: 41/4;
- fully occupied coherent ground energy: 21/4;
- separation: 5 energy units.

The all-filled bit string is absent from this encoding. Lossless compression
of the 21-dimensional memory sector into the fixed-carrier, rank-one all-filled
ground is impossible without additional retained degrees of freedom. This is
not a universal no-go: an enlarged history space, different encoding, or a
multi-excitation construction would be additional explicit structure to test.

These are exact code/operator identities, not a numerical diagonalization of
the 36*2^21-dimensional tensor space, and not calibrated mass values.

## Verification and updated next step

    python research/voevodsky/checkers/check_single_seam_memory_occupation.py

Fresh execution passed. Receipt: `results/single_seam_memory_occupation.json`.
The checker binds the immutable source snapshot, actual intrinsic coefficients
and preceding memory receipt by hashes. Three exact inputs test pure mismatch
and different coherent/mismatch superpositions, holding, occupation and balanced
write/read work.

Next: decide whether the intended resource is this persistent one-excitation
memory code or simultaneous bond occupations. For the latter, construct an
explicit many-excitation/history encoding that retains distinguishable source
amplitudes; do not equate 21 nonzero complex coordinates with 21 occupied bits.
Local implementation and control/battery dynamics remain separate gates. No new
particle mass, isotope binding, stability or electron five-cell result is claimed.
