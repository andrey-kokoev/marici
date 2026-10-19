# A typed graded contact vertex—and its finite-code recurrence limit

[Contract](contracts/graded-contact-vertex.v1.json) · [checker](check_graded_contact_vertex.py) · [receipt](results/graded-contact-vertex.v1.json)

## Constructed result and new assumptions

There is now an explicit self-adjoint conversion operator, not merely a singlet projector or a proposed final-state map. It acts on a declared charged-fermion Fock code plus the preceding normalized relative photon modes, preserves charge, C, fermion parity and native rotations, and retains survival and spectator sectors.

**New postulates:** four charged CAR modes; a linear species swap fixing the vacuum; the imported relative photon sectors; and a Hermitian pair-conversion vertex. These are an extension of the theory, not consequences of the original L/G/N arrows. In particular, the source audit's exchange-sign ambiguity is resolved only **within this declared CAR extension**. No physical incoming species, electromagnetic calibration or native operation license is thereby established.

## 1. CAR determines the conditional pair sign

Order the four fermion modes as (- up,- down,+ up,+ down). The 16 occupation states are the full exterior algebra of this four-dimensional one-particle space. Explicit creation matrices satisfy

```
{a_i,a_j^dagger}=delta_ij I,
{a_i^dagger,a_j^dagger}=0.
```

Let S exchange the negative and positive species while preserving spin. Its exterior lift C_F=Gamma(S) is a linear unitary involution, fixes the vacuum, exchanges the corresponding creation operators and reverses the declared charge operator Q_F.

For the canonically ordered neutral pair,

```
|a,b>=a_-a^dagger a_+b^dagger |vac>,
C_F |a,b>=a_+a^dagger a_-b^dagger |vac>=-|b,a>.
```

Thus **minus swap is derived from CAR, canonical species ordering and the specified vacuum-fixed flip**; it was not inserted as a pair matrix by hand. This does not derive CAR or the flip from the native source. The four-dimensional neutral pair decomposes into C-even singlet and C-odd triplet using the previously verified source Clebsch–Gordan matrix.

## 2. Retained embeddings

Use the preceding opposite-Pauli encodings J_minus,J_plus. The one-particle map

```
B=[J_minus J_plus] : C4 -> C8
```

is isometric, and the candidate raw flip intertwines it with S. The checker constructs the neutral two-fermion exterior embedding explicitly into the 28-dimensional wedge-square of C8 and verifies its four-dimensional Gram matrix is I4. No two logical amplitudes are identified or averaged.

For an arbitrary ordered raw pair, let E_raw=J_minus tensor J_plus and R_raw=I64-E_raw E_raw^dagger. The retained completion is the linear map

```
x -> (E_neutral E_raw^dagger x, R_raw x).
```

Its norm is the norm of x because the two components are orthogonal and E_raw is isometric. The 60-dimensional ordered-raw complement is a separate spectator—not a second copy of the input, a measurement or a postselection. The typed 16-dimensional fermion Fock space also retains the twelve occupations outside the selected neutral pair.

The fixed native protocol still annihilates the positive code. These embeddings and their new coherent return are additional mathematical resources, not generated source preparations. Other parent geometry/controller records can be carried by an identity factor; no claim to have implemented their physical dynamics is made.

## 3. A concrete Hermitian vertex

Choose one of the certified equal-helicity photon sectors. The selected output modes are:

- one normalized two-photon scalar mode, C=+1;
- three normalized three-photon vector modes, C=-1.

They are the actual conditional relative-helicity wavefunctions from the preceding [two-](TWO-PHOTON-HELICITY.md) and [three-photon](THREE-PHOTON-HELICITY.md) constructions, not unsymmetrized triangle factors. The helicity choice itself remains an input.

Write |s>,|t_j> for the four orthonormal neutral CAR states. Define

```
V=g_s |gamma2,s><s| + g_t sum_j |gamma3,j><t_j|,
H_int=V+V^dagger.
```

This is an explicit 20-dimensional contact **code**: sixteen fermion occupation states plus four selected output states. It is a subspace of a larger fermion/photon theory, not a full local field interaction. Mixed fermion/photon states and the remaining photon Hilbert space are retained as uncoupled spectators in this finite-rank extension, not silently projected out.

The arity is fixed explicitly: exactly one fermion of each species is consumed, with no remaining fermions in the output. In operator terms the source bras include the vacuum projection after the two annihilators. Consequently the vacuum and four-fermion state are not alternative source ports for this vertex. A full field-theory polynomial vertex without that projection would also act on higher occupations and is **not** constructed here.

For arbitrary complex g_s,g_t the checker verifies self-adjointness and commutation with total Q, total C, fermion parity and all 24 diagonal native rotations. The resonant **declared** free labels give each fermion energy M/2 and each selected photon output total energy M; this free-label operator also commutes with H_int. Checks use the declared test label M=3, not a calibrated mass or clock. The total finite-code trial H0+H_int is nonnegative: its active eigenvalues are M +/- |g_s| and M +/- |g_t|, and all tested magnitudes are strictly below M; spectators have the nonnegative free labels. This is not a full field-theory stability result.

Between these particular neutral-pair and output codes the complex intertwiner dimension is two. This follows from one singlet plus one irreducible triplet on each side and is checked by the native character inner product. It is **not** a classification of all interactions on the full Fock space. Symmetry leaves g_s and g_t independent; a common coefficient would be another hypothesis, not a result. Neither coefficient is fixed by the encounter geometry yet.

## 4. Exact dynamics: survival cannot be erased

On each active two-level block, for real positive g and with hbar=1,

```
exp(-it H_int)|in> = cos(g*t)|in> - i*sin(g*t)|out>.
```

For a complex coupling the outgoing sine amplitude also carries g/|g|. This unitary preserves coherent phases; it does not implement an irreversible projection.

Two exact interaction-picture examples at dimensionless t=pi/2 are checked:

| Couplings | Singlet survival / two / three | Triplet survival / two / three |
|---|---|---|
| g_s=1, g_t=2 | 0 / 1 / 0 | 1 / 0 / 0 |
| g_s=2, g_t=1 | 1 / 0 / 0 | 0 / 0 / 1 |

Both satisfy the same typing and symmetry conditions. All triplet components behave identically. In either example the contact propagator returns to I at t=2*pi. The checker verifies exact unitarity and U(pi/2)^4=I, including spectator states. The commuting free labels add phases but do not change the displayed populations.

These are reversible finite-mode transfers, not candidate fitted branching laws, rates or lifetimes. Deleting survival and renormalizing the remaining photon counts would discard a real outcome and create a protocol-dependent apparent ratio. The new constructor explicitly forbids that promotion.

More generally a finite-dimensional closed self-adjoint Hamiltonian gives recurrent/quasiperiodic motion. An initially occupied incoming subspace cannot have strictly irreversible complete release under that finite closed evolution. This is a limitation of this contact-code model, not a no-go for a spatial source theory with outgoing continua and retained records.

## 5. Next executable gate

The [Jacobi escape completion](CONTACT-ESCAPE-CONTINUUM.md) now supplies a declared infinite half-line model: weak active couplings give complete local release, whereas a positive stronger example retains bound norm 1/sqrt(5) despite local pair probability tending to 1/5. This is not yet physical photon dispersion or native encounter dynamics. Next bind/replace its band and coupling envelope using actual photon phase space and source data, including ultraviolet and threshold tests. Keep a self-adjoint total Hamiltonian and all continua/records; do not repair recurrence by nonunitary deletion. Merely appending infinitely many uncoupled modes does not help: the finite active subspace would remain invariant. The outgoing dynamics must actually carry amplitude away from the contact region. The continuum form factors, channel thresholds, encounter support and g_s/g_t must be independently supplied or source-derived, not fitted to a desired ratio.

This separates two questions: the typed reversible vertex now exists conditionally; native encounter implementation and annihilation/capture-versus-escape dynamics still do not. The [total-momentum successor](TOTAL-MOMENTUM-PACKET.md) now constructs full imported photon packets; the [covariant successor](COVARIANT-ESCAPE-LIFT.md) now adds active lab dynamics under velocity/mass postulates. Local source support, physical incident preparation and dimensional calibration remain open. C1–C12, exhausted C12 budget, paused high-energy execution and owner warnings are unchanged. No physical outcome or branching ratio is admitted.

```sh
python -S research/scattering/low-energy/check_graded_contact_vertex.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_graded_contact_vertex.py
```
