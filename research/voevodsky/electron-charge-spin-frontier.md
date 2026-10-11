# Electron frontier: a spinorial construction and a charge-readout obstruction

## Question

Operator direction: “let's push as far as we can with electron.” Test whether the four-face negative-flux trial can acquire a definite charge and spin one-half without hiding amplitude changes or replacing the source by a desired scalar.

Active SCC obligations: **forward realization** and **readout compatibility**. The old vector fixture is kept fixed in the first test. The second test explicitly declares a new spinor carrier; it is not a downstream reinterpretation of that fixture.

## Governing conjecture and rivals

**Conjecture:** the existing smaller negative mode already supplies a source-generated unit-charge, spin-half electron carrier.

**Rivals:** its flux is amplitude-dependent polarization; three stages are mistaken for three independently occupied channels; the rotation character is integer-spin; or a spinor can be constructed only after a genuine carrier enlargement.

**Risky consequences:** a common normalized operator must give sharp opposite charges on the original proton and the candidate; serial return must not manufacture amplitude; spin transport must retain a minus sign around a full rotation; and an enlarged construction must preserve both logical spin states rather than imposing a one-dimensional coherent line.

## 1. Definite polarization: succeeds for the candidate, fails for the old proton

For the source tetrahedron, let A be a whole-face oriented area vector. It has length 2 sqrt(3). The Hermitian local operator

\[
H=\frac{i[A]_\times}{2\sqrt3}
\]

has eigenvalues −1, 0, +1. In the fixed original coordinates, the previously tested radial flux is

\[
Q(w)=\frac{w^\dagger H w}{48},
\]

summed over local modes. This identity holds for both the whole-face and centroid-edge subdivisions, because their solid-angle/area ratios agree.

The four-face negative candidate is an eigenstate of H with eigenvalue −1 and zero variance. Its reference squared norm is 48, explaining its unnormalized flux −1.

The original proton has squared norm 80 and flux +1, but its normalized H expectation is **3/5**, with variance **16/25**. Each of its twelve local mode selectors fails to commute with H; the squared commutator norm is **32/25**. No common scalar calibration can remove nonzero variance.

Thus the earlier +1/−1 flux comparison does not establish sharp electric charges of the original two coefficient states. This is a specific failure of that readout, not a failure of the geometric flux calculation.

Projection onto the positive and negative circular channels gives squared norms 64 and 16, respectively. Each projected twelve-mode protocol retains 1836 transfers, one coherent line, and the deletion certificate. The projectors and selected modes change; this does not silently replace the original proton.

## 2. Three negative channels: distinguish copies from stages

Three independently retained channels of flux −1/3 have total −1. Using the existing three-axis protocol for twelve whole-face placements gives **1836 transfers**, rather than the four-face core's 228.

An isometric combiner can map three phase-aligned inputs to one field with sqrt(3) times their individual amplitude. Its bright-channel fraction is

\[
\frac{|z_1+z_2+z_3|^2}{9}
\]

for unit input phases. The phases 1, ω, ω² instead give zero in that channel; the other outputs cannot be discarded as absent input.

Three serial returns do not supply those inputs: N³=N. Their flux remains −1/3. Obtaining the compressed four-face core requires actual additional input records, phase alignment and a declared adapter—not counting the three protocol stages as three particles.

## 3. The vector carrier cannot supply spin half by rephasing

The old coefficients transform as spatial vectors. The central element of the double cover of rotations acts as +1. In a spinor it acts as −1.

Any rotation-equivariant linear map T from the old carrier to a spinor would obey T=−T, hence T=0. A phase convention cannot repair this.

The circular modes do satisfy the null condition v·v=0. Over the complex numbers they admit quadratic Cartan roots, up to sign. In Pauli-compatible coordinates the map is

\[
(a,b)\longmapsto(a^2-b^2,\ i(a^2+b^2),\ -2ab).
\]

Retaining that root and its double-cover transport is a new carrier operation. The checker verifies the null polynomial exactly and constructs all 24 binary tetrahedral rotations with exact coefficients. Their rotation quotient has 12 elements.

A further obstruction determines the coherent rank: the central −1 is a commutator in the binary tetrahedral group. Every one-dimensional character sends a commutator to +1. A spinorial coherent return therefore cannot retain the old single-line symmetry contract; the smallest logical carrier is a doublet.

## 4. Explicit spinorial doublet on the four faces

Let n_i be the four outward unit face normals and let σ denote the Pauli matrices. Define

\[
P_i=\frac{I-n_i\cdot\sigma}{2}.
\]

Each P_i selects negative polarization on its face. The tetrahedral identity sum n_i=0 gives

\[
\sum_iP_i=2I.
\]

Consequently the map

\[
Jz=\frac1{\sqrt2}(P_0z,P_1z,P_2z,P_3z)
\]

is an isometry from a two-component logical spinor into eight raw complex coordinates. Its collective projector is

\[
N=JJ^\dagger,\qquad N_{ij}=\frac12P_iP_j.
\]

It satisfies N²=N and trace N=2. Under the combined face permutation and binary rotation U, the encoded logical action is exactly U. The central full-rotation lift acts as −I, not +I. This is an explicit spinorial doublet, rather than a scalar phase label attached to the old vector.

For the declared three-stage realization

\[
L=\operatorname{diag}(P_i),\qquad G=N,
\]

with N as the return stage, NGL=N. Its nonzero supports are:

| Stage | Transfers |
|---|---:|
| L | 16 |
| G | 64 |
| N | 64 |
| Total | **144** |

The two equal matrices G and N act between different typed stages; their records are not identified. This is a supplied protocol, not a claim of minimum support. All 144 arrows occur in positive closed three-step cycles. There are 128 such cycles, with total trace 2, so every proper fixed-weight edge deletion lowers that trace.

The polarization operator diag(n_i·σ) equals −I on the entire encoded doublet. Both logical spin states have the same sharp negative polarization.

## 5. Do not erase the changed readout

The new Pauli polarization is quadratic in the spinor. Mapping the spinor through the quadratic Cartan map and applying the old vector flux gives a quartic quantity instead.

For a unit logical state, the tetrahedral second-moment identity gives

\[
\sum_i\|J_i z\|^4=\frac13.
\]

The literal Cartan image therefore has old radial flux **−1/(24 sqrt(3))** in the original tetrahedral coordinates, independently of logical spin direction—not −1. No conversion factor was fitted to force agreement.

The new −1 polarization, the old amplitude-calibrated radial flux and electromagnetic charge remain different typed readouts until an explicit common coupling identifies them.

## 6. Charge, mass and exchange are underdetermined by this return

Three exact controls keep the same coherent doublet and all rotation transports:

- **Charge:** Q_q=qN commutes with the rotations for every scalar q. Every integer q gives a periodic U(1) action; tested values −2, −1, 0, 1 and 2 all preserve the construction. Negative Pauli polarization does not select one of these gauge charges.
- **Energy:** E_m=mI+(I−N) has the same rank-two lowest eigenspace, energy m and gap 1 for every real m. Distinct positive rational choices pass without changing the return. Symmetry and support therefore cannot determine electron mass.
- **Exchange:** both swap and minus swap commute with U⊗U. The symmetric three-dimensional and antisymmetric one-dimensional two-spinor sectors are both invariant. Rotation transport does not choose the fermionic sector.

These are explicit competing realizations, not merely absent calculations.

## Disposition and stopping conditions

The original conjecture is rejected: the four-face vector mode was not already a source-generated electron.

A declared extension does construct a spinorial doublet with sharp negative polarization and an exact 144-transfer return. The first missing source operation is the generation of that two-component carrier and its double-cover transport. Its acceptance test is an explicit typed constructor from the retained assembly, including the coherent-rank change and phase action.

The physical readout branch stops at the missing electromagnetic U(1) coupling; the old flux fails the common sharp-charge test. The mass branch stops at the missing energy functional and scale selector. The support ratio 1836/144=51/4 is not the electron mass ratio. Spinorial rotation alone does not supply fermionic exchange or an exclusion rule.

These missing inputs are not replaced by new normalization choices or further hypothetical attachment layers.

## Reproduction

Dependency-free exact checkers:

```text
python research/voevodsky/checkers/check_electron_charge_spin_frontier.py
python research/voevodsky/checkers/check_electron_tetrahedral_spinor.py
```

The first passes 14 checks and the second 16. Results and the spinor coefficient store are in:

- `results/electron_charge_spin_frontier.json`
- `results/electron_tetrahedral_spinor.json`
- `results/electron_tetrahedral_spinor_store.json`

Owner-local SCC manifest: `scc-models/electron-charge-spin-frontier.json`. Its local check passed both executables (`structured_command_execution:e_19096_1791555345666862900_6`); SCC supplied exit-code orchestration, not an additional proof. Initial global `models` and `dashboard` inspection returned exit 1 while listing stale/missing models elsewhere; that is not evidence against this local calculation. No visualization, original source fixture, or other owner's workspace was changed.
