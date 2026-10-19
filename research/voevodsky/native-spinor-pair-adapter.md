# Dispersive/native continuation — iteration 2 of 3

## Off-center weighted-response follow-up

`slater-real-axis-native.md` now certifies the Slater real-axis dispersive part
at E=4 and combined optical flux using these source-compressed core energies,
with 19 checks. Relative native/orbital scale and couplings remain declared;
physical coupling is not admitted.

## Result

Constructed a **source-bound conditional native spinor-pair adapter**, not an
identification of the scalar eleven-state port core with an electron pair.
All **99 exact checks pass**. Both chiralities and both retained native doublets
are audited; metric, face/cell covariance, core energy compression, typed vertices
and complement retention are checked without floating tolerances.

A meaningful obstruction remains: two of the four encodings cannot use the old
ambient output rotation unchanged. They require a declared effective output
representation. Physical coupling, partner identity and calibration are not
thereby established.

## 1. Fresh retained inputs

Freshly read the off-center continuation and the native cycle checker's attachment
construction; rerun the source pentachoron cycle checker. Load its source-bound
receipt and the checked spin-interface and typed-output receipts.

The native single-object model here is the previously declared five-cell
full-spinor mismatch extension, dimension ten. It retains cell and face records.
It is not the original scalar port space, and its conditional extension is not
advertised as a physically forced electron state space.

For each chirality the cycle receipt exports two isometries

    W_0,W_1 : C^2 -> C^10,
    W_i^dagger W_i=I, W_0^dagger W_1=0.

Their images are the two orthogonal rank-two doublets of the rank-four lowest
mismatch space. Both are retained, not selected by local attachment recovery.
The corresponding forty-row face encodings are separately isometric.

## 2. Effective source transport must be calculated

With the actual all-cell source transport T, define

    D_i=W_i^dagger T W_i.

The checker verifies

    T W_i=W_i D_i,
    T_face F_i=F_i D_i,
    D_i^dagger D_i=I, det D_i=1, D_i^5=-I.

It would be wrong to replace D_i automatically by the local spin matrix S used
in every transported cell. The constant doublet has D_i=S, but the other doublet
has a different source-cycle trace. A same-dimensional encoding need not carry
the same representation.

The native-pair effective transport is

    D_pair=D_i tensor conjugate(D_i), D_pair^5=I.

The scalar projector is fixed pointwise and the vector projector commutes with
this transport. The scalar/vector decomposition therefore survives the native
adapter, rather than being assigned solely by channel names.

## 3. A pair encoding that retains the native complement

Declare a conjugate native partner; its physical positron identity is **not**
derived. The full native pair space has dimension 100. Define

    J_i=W_i tensor conjugate(W_i) : C^4 -> C^100.

Exact checks establish

    J_i^dagger J_i=I_4,
    (T tensor conjugate(T)) J_i=J_i D_pair.

The selected encounter pair has dimension four. The full low/low native pair
space has dimension sixteen, leaving twelve unselected low pair states. The full
native pair complement has dimension ninety-six. These coordinates remain in
the model; they are not deleted by a quotient or called resolved mismatch.

The associated native encounter projector is J_i J_i^dagger. It and its complement
are retained in factored form, avoiding an unnecessary dense 100x100 export.

## 4. Conditional source energy, not the old arbitrary core value

Reconstruct the native mismatch operator from its verified spectral decomposition:

    Q=W_0 W_0^dagger+W_1 W_1^dagger,
    L=(4-sqrt(6)) Q + (4+2sqrt(6)/3)(I-Q).

Both encodings have the old mismatch eigenvalue 4-sqrt(6). The checker verifies
that L commutes with the actual source transport.

For the predecessor's *optional, declared* cycle-defect extension,

    X=2I-T-T^dagger, H_native=L+X,

the two encoded energies are

    e_0=4-sqrt(6)+(3-sqrt(5))/2,
    e_1=4-sqrt(6)+(3+sqrt(5))/2.

Option 1 reuses the opposite-lift attachment encoding but is evaluated here under
the displayed-lift H_native, where it is an excited doublet. It is not assigned
the different energy of the opposite-lift Hamiltonian's ground state.

On the independently declared conjugate pair,

    (H_native tensor I+I tensor conjugate(H_native)) J_i=2 e_i J_i.

Thus a source-compressed core in this convention is 2e_i I_4, **not** the old
freely chosen 6I_4 scattering fixture. The shared overall pi/4 convention and
physical time/energy conversion remain outside this dimensionless calculation.
Relating these native energies to orbital hopping still needs an explicit scale.

## 5. Native-to-output vertices and pulled-back self-energies

Let B_c be the previously constructed typed orbital vertices. A conditional
coupling from full native records is

    A_c=B_c J_i^dagger,
    Sigma_native(z)=J_i Sigma_encounter(z) J_i^dagger.

The checker verifies recovery of the typed maps on J_i and zero action on the
retained native complement. Since that selected subspace is invariant under the
native operators, the complement is a genuine dark block for this **chosen**
vertex. It is not physically erased or proved incapable of other interactions.

The mathematical self-energy retains the actual orbital laws: pair endpoint,
vector triple convolution, and scalar Slater/Vandermonde channel as appropriate.
For example the scalar-record contribution is

    lambda_A^2 g_A(z) J_i P_s J_i^dagger,

not the vector triple response relabelled as a scalar. Its off-center real-axis
value remains the unresolved weighted orbital calculation from iteration 1.

## 6. Covariance exposes an additional physical choice

From each calculated D_i construct its vector action

    (R_i)_ab=tr(sigma_a D_i sigma_b D_i^dagger)/2.

Both typed endpoint maps intertwine D_pair with R_i tensor powers. The internal
epsilon scalar of the orbital-record channel is also invariant under R_i.
All these controls pass exactly.

But the original ambient output action R_S is not always R_i. The direct test is

| Chirality | Encoding option | Old ambient vector output remains covariant |
|---:|---:|---|
| +1 | 0 | yes |
| +1 | 1 | **no** |
| -1 | 0 | **no** |
| -1 | 1 | yes |

Changing the output representation to R_i makes a valid conditional adapter; it
does not prove actual native output objects carry that new action. Conversely,
choosing the ambient-compatible doublet is an additional selection, and need not
coincide with the predecessor's displayed-lift ground doublet in both chiralities.

This prevents declaring native/physical covariance merely because a pair
isometry exists.

## 7. What remains supplied or open

- A choice of native doublet, spin lift and output representation.
- A declared conjugate partner; no charge or positron model is derived.
- Relative native/orbital energy scale and every cross-channel coupling lambda.
- A physical mechanism realizing the additional cycle defect, if used.
- Physical multi-object output identification and empirical calibration.

No physical coupling is admitted by the new checker. It supplies an explicit,
source-bound conditional adapter and identifies its limits.

## 8. Next executable continuation

Certify the Slater weighted real-axis response, then use the source-compressed
core energies and an explicitly declared relative scale in the combined optical
calculation. Compare doublet/output-action choices rather than hiding them in a
single fitted core energy. That would extend the constructive conditional model;
it would still not determine physical coupling constants from covariance alone.

## Reproduction

```sh
python research/voevodsky/checkers/check_pentachoron_cycle_transport.py
python research/voevodsky/checkers/check_native_spinor_pair_adapter.py
```

Receipt: `results/native_spinor_pair_adapter.json`, retaining both encodings,
face records, effective transports/output actions, compressed energies, retained
space dimensions and exact source hashes.
