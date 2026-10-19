# Native collective contacts coupled to the common endpoint parent

## One shared interaction

Starting from the common signed endpoint parent, use one neutral two-state record in every sector, with gap 1 and g=1/2:

    H_joint = H_endpoint tensor I + I tensor |1><1|
                - g P_contact,dressed tensor X.

The vacuum has no matter contact, the record is ready in |0>, and its energy is zero. This is an alternative to the 21 independent seam records, not their cumulative addition. No sector rest offset is inserted.

The coupling is the one-bit instance of the prior signed-record contact construction. The source contacts are retained:

- Proton: the full coherent all-face projector.
- Belt: the normalized equal-phase sum over its actual cross-face contact endpoints.
- Electron: the entire rank-two coherent projector (I+Q)/2, not a selected spin vector.

For a charged source, every contact matrix element i->j includes the endpoint shift q(e_j-e_i), exactly as the kinetic hopping. It preserves all site Gauss generators and leaves lead flux unchanged. Omitting this dressing would not define the same physical-space operator.

## Exact retained reductions

The proton remains on its twelve selected native modes. Its twelve unit-lead blocks are related by explicitly checked weighted-graph automorphisms preserving K, contact, metric, graph resistance and the transported electric diagonal. One 24-dimensional matter-plus-record block therefore suffices.

The belt's eighteen selected modes reduce to six amplitudes repeated across the three native sectors. The checker verifies the embedding/decoder, kinetic intertwiner, contact intertwiner and commutation with the sector projector. Contact vanishes on the remaining twelve selected-mode directions; their Hamiltonian remains nonnegative. The retained six modes plus one bit give a twelve-dimensional block. They are not replaced by six harmonic oscillators.

The electron keeps all four face-line amplitudes and both coherent spins. Its four unit-lead blocks each have eight complex dimensions. An exact rational realification uses coordinates x+i sqrt(3)y and metric diag(I,3I), so no numerical complex eigensolver is needed.

These are the selected native matter sectors of the preceding endpoint parent. Native raw complements outside those adapters have not acquired new field couplings by implication.

## Common-vacuum energies

Rational weighted-LDL certificates give:

| Sector | Ground energy |
|---|---:|
| Proton | 0.3438018922396275… |
| Electron | 0.2654635408568634… |
| Belt | **-0.0951011402073565…** |

The proton/electron ratio changes from approximately 1.16303 to **1.2951002278124655**, so this interaction does act on the charged ground states. It does not produce the required hierarchy.

All remaining charged lead-flux blocks have endpoint energy at least 1; the contact interaction is bounded below by -g. Their full energies are therefore at least 1/2, above the reported grounds. Nonzero neutral lead flux has energy at least beta, hence at least beta-g=1/10 after coupling. The belt's discarded selected-mode complement remains nonnegative. Thus the bounds concern the full integer lead lattice within these source sectors, not just a sampled flux window.

## Stronger failure: a negative belt sector for every nonzero coupling

Let u be the normalized coherent belt zero mode, and

    r=<u,P_contact u>=2386/4485.

Restrict a variational trial to u and record amplitudes (1,t). Since u has zero kinetic and endpoint-field energy, its normalized energy is

    E_trial(t) = (t²-2g r t)/(1+t²).

Choosing t=g r gives

    E_trial = -g² r²/(1+g² r²) < 0

for every real g!=0. The checker verifies the actual source overlap and this bound against the computed ground interval.

Therefore reducing the coupling cannot make the empty vacuum the global lowest sector: the belt sector stays below it. This is an energetic ordering result, not a claim of spontaneous creation—the present Hamiltonian conserves matter sector.

A shared scalar shift would move both vacuum and matter together and would not repair the relative ordering. A positive occupied-sector mechanism would have to be supplied as an actual operator, not chosen as an offset to cancel this result.

## Verification

```sh
python research/strominger/checkers/check_common_native_contact.py
```

Seven reported checks passed, alongside the exact closure, covariance, gauge-shift, charge-block and LDL assertions. Source hashes bind the parent, source contacts and checker dependencies. Shared stores were unchanged.

Receipt with full block matrices and rational intervals: `research/strominger/results/common-native-contact.json`.

The result replaces another guessed energy term with a tested compatible interaction. It also rules out this unoffset branch under a common ground-vacuum requirement, rather than hiding the negative belt energy.
