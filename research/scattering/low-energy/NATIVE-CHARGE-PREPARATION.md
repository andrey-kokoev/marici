# Native charge/preparation audit: a raw flip candidate, not a selected charge rule

[Contract](contracts/native-charge-preparation.v1.json) · [checker](check_native_charge_preparation.py) · [receipt](results/native-charge-preparation.v1.json)

## Result

The inspected native sources do **not select** a physical pair charge-conjugation operation or an incoming singlet fraction. This is a bounded source audit, not a claim that no future source operation can supply them.

There is nevertheless a constructive result: an explicit **complex-linear, rotation-equivariant unitary on all eight raw coordinates** flips two orthogonal opposite-Pauli-polarization codes while retaining the remaining four-dimensional complement. It is not a word of the fixed stored protocol. It must not be confused with the source's antiunitary spinor reversal, nor admitted as electromagnetic charge conjugation merely because it flips polarization.

## 1. What the current sources actually supply

All files are inspected read-only; no owner entrypoint is run.

| Source under `research/voevodsky/checkers/` | Relevant supplied fact | Boundary |
|---|---|---|
| `check_electron_charge_spin_frontier.py` | Normalized mode-flux/helicity operator and the binary-tetrahedral spinor trial | Explicitly no physical charge generator or mass law; the old proton is not sharp under the proposed common calibration |
| `check_electron_tetrahedral_spinor.py` | Four-face Pauli encoding; sharp negative polarization on the whole logical doublet; arbitrary integer Q_q=qN; both swap and minus swap commute with pair rotations | Explicitly no selected electromagnetic coupling, fermionic exchange or mass |
| `check_electron_pairing_coupling.py` | Pseudoreal C=-epsilon K, C^2=-I; existing negative Choi witness; declared neutral bilinear spinor vertex | The bilinear is a new operation, not native linear arrow grammar; antisymmetric contraction does not impose fermionic statistics |
| `check_geometric_cycle_reversal.py` | Invert a primitive triangle cycle while retaining its character: conjugated mode coefficients and a separate reversed protocol | Not a particle/antiparticle field operation or physical charge-conjugation law |

In particular the pairing source already distinguishes frozen complex-linear phase attachment from a state-dependent charged-phase attachment. Both can satisfy the retained coefficient constraints; those constraints do not select the latter. Conjugating a fixed mode is not automatically conjugating the freely varying amplitude or reversing its physical charge.

The current spinor store contains a field declaration, normals, face projectors and arrows—not a preparation density or a species-labelled field vacuum. The producer's sample spinors are verification examples, not an ensemble selection.

The audit records current-versus-historical checker pins for each inspected receipt without rewriting any of them. The previously reported spinor-producer mismatch remains visible. A stored passing receipt is not silently reinterpreted as a fresh execution of its owner program.

## 2. Opposite Pauli codes and an explicit full-raw linear flip

For the actual stored face projectors P_i=(I-n_i.sigma)/2, set Q_i=I-P_i and

```
J_minus=stack(P_i)/sqrt(2),
J_plus =stack(Q_i)/sqrt(2),
N_minus=J_minus J_minus†,
N_plus =J_plus J_plus†.
```

The checker verifies

```
J_minus†J_minus=J_plus†J_plus=I2,
J_minus†J_plus=0,
H J_minus=-J_minus,
H J_plus=+J_plus,
```

where H is the source block-Pauli observable. The two rank-two collective codes are orthogonal, although each uses the same eight raw coordinates.

Define R0=I8-N_minus-N_plus and

```
C_raw=J_plus J_minus†+J_minus J_plus†+R0.
```

Then C_raw is Hermitian, C_raw^2=I8, C_raw J_minus=J_plus and C_raw J_plus=J_minus. It is the identity on R0. No raw complement has been projected away.

Both J codes intertwine the same native U(q), so C_raw commutes with all 24 raw native actions. For any q, the **declared** signed-code observable

```
Q_q=q*(N_plus-N_minus)
```

also commutes with these rotations and is reversed by C_raw. This is another uncalibrated algebraic family, not an electromagnetic generator inferred from the old flux.

### Why this is not already a stored operation

The actual stored L/G/N stages preserve the negative code, as do all 24 native actions. Any word in that closed class preserves it. C_raw sends it to an orthogonal code, so no such word realizes C_raw. This excludes the fixed class only; it does not exclude every enlarged source theory. In fact the stored negative-code L and collective return annihilate J_plus entirely, as checked exactly. Supporting that positive code as a persistent preparation would require a different return or an enlarged protocol. The positive code and raw flip are explicit additional candidates whose physical licensing is still missing.

## 3. The existing antiunitary reversal is a different map

The inspected pairing source defines Theta=-epsilon K, where epsilon=[[0,1],[-1,0]] and K conjugates coefficients. The checker binds that actual source expression by AST inspection and replays its algebra:

```
Theta(i z)=-i Theta(z),
Theta^2=-I,
Theta U(q)=U(q) Theta.
```

Its blockwise raw lift sends J_minus z to J_plus Theta(z), unlike C_raw, which sends J_minus z to J_plus z. Both flip the Pauli code, but only one is complex-linear. The source already proves that the unknown-spinor density transformation epsilon rho^T epsilon† is not completely positive: the normalized Choi matrix has Bell-state expectation -1/2. This audit **replays**, rather than claims to discover, that witness.

This does not prohibit a unitary charge-conjugation operator on an appropriately enlarged particle/antiparticle field space. It forbids treating this particular one-spinor antiunitary as a deterministic quantum channel by renaming it.

## 4. Pair exchange does not yet choose charge parity

For the same-spinor pairing convention, S swaps the two logical spin factors and commutes with every U tensor U. The inspected source explicitly leaves both S and -S available as algebraic exchange conventions. In the singlet/triplet basis,

```
S = -Ps+Pt,
-S= +Ps-Pt.
```

Both are unitary involutions. A candidate single-particle charge flip exchanges the species labels; returning a neutral pair to a fixed species order additionally requires an exchange/statistics convention. The missing fermionic reordering rule cannot be inferred from an antisymmetric spin contraction alone. The present algebra does not identify S or -S with physical pair C.

If one **additionally imports** photon charge parity C_gamma=(-1)^n and conservation of this C, the two choices give opposite conditional selectors:

| Declared pair operation | Singlet C | Triplet C | Conditional two-/three-only selector |
|---|---:|---:|---|
| -S | +1 | -1 | singlet -> two, triplet -> three |
| +S | -1 | +1 | singlet -> three, triplet -> two |

The checker constructs both conditional selector maps into the normalized two-/three-photon code sectors and verifies W†W=I and W*C_pair=C_out*W. This table is an underdetermination witness, not two predictions. Under the finite native symmetry both spin-sector target maps exist. Adding an independently identified continuous total-J=1 source and exclusive two-/three-real-photon outputs would make the +S triplet assignment incompatible with the preceding two-photon exclusion. That is an extra compatibility test, not a derivation of fermionic statistics, physical charge C or a native contact operator.

## 5. Even a selected sign would not supply preparation weights

For every 0<=p<=1,

```
rho(p)=p*Ps+(1-p)*Pt/3
```

is a normalized positive rotation-invariant logical pair density with singlet weight p. Exact examples p=0,1/4,1/2,1 are checked. Encoding one factor in J_minus and one in J_plus gives zero total **Pauli** polarization for all these choices, so that readout cannot select p either. It is not calibrated electric neutrality.

Under the additional -S selector the conditional two-output weight would be p; under +S it would be 1-p. The often-used I4/4 is just the p=1/4 choice, not a source consequence of rotation invariance or unpolarized one-body marginals. Indeed every rho(p) has unpolarized one-body marginals; singlet/triplet correlations differ. No 1:3 count ratio, lifetime, cross section or 372 law follows.

## 6. Explicit extension now constructed; outgoing completion next

The [graded contact construction](GRADED-CONTACT-VERTEX.md) now postulates four charged CAR modes and a vacuum-fixed species flip, derives minus-swap within that extension, retains the raw complement and constructs a self-adjoint symmetry-compatible conversion vertex. This does not select statistics or physical C in the original source. Two independent coefficients remain; exact finite-code dynamics exhibits survival and recurrence, not irreversible annihilation. The [Jacobi completion](CONTACT-ESCAPE-CONTINUUM.md) now tests conditional escape and retained bound clouds; next bind its dispersion, coupling measure and localized preparation to actual photon/source data without deleting records. Simply inserting -swap, I4/4 or a singlet projector and calling it native annihilation would bypass the audited gaps.

The existing source pairing audit already says the native linear grammar lacks a binary neutral-output vertex. The new typed vertex is therefore an explicit added resource, not something generated by relabelling the old mode flux. Source licensing, physical species/preparation, full wavepackets and calibrated rates remain open. C1–C12, exhausted C12 effort and paused high-energy execution are unchanged; owner files and historical warnings are preserved.

```sh
python -S research/scattering/low-energy/check_native_charge_preparation.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_native_charge_preparation.py
```
