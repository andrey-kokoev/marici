# A norm-preserving one-probe decoder that leaves the native assembly unchanged

## Constructed result

A newly synthesized control resolves all 36 raw coefficient coordinates using
one fixed complex-coordinate probe, while preserving the existing native metric
and fixing every locally admitted state pointwise. It commutes with L, G and N,
so it does not change the native collective return.

This advances the source-cycle result in `proton-single-probe-cycle-v1.md`.
That result ruled out making the **same transported slot cycle A** unitary
while retaining L as an orthogonal projector. The present control V is a
**different operator**, built explicitly from A, its native adjoint and L.
It does not evade or contradict that obstruction.

## Two initial constructions and their failure to protect assembly

Before testing, two Hermitian recipes were frozen:

    H_1=A+A^dagger,
    H_2=A^dagger A.

For either recipe choose the exact Cayley control

    V=(I-s H)(I+s H)^-1,  s=sqrt(-3).

Here s is an explicitly chosen imaginary scale. It is not a physical time,
source-selected coupling or derived clock. Because H is Hermitian, I+sH is
invertible and V is unitary in the unchanged native metric. Geometric source
covariance of H implies covariance of V.

Both recipes give a full 36-reading one-probe observation matrix. But exact
checks find

    rank[V,L]=24,
    rank[V,N]=2.

They preserve the norm yet move a collective input out of its collective line.
This rejects the stronger claim that native unitarity alone protects assembly.
Both outcomes remain stored in `results/proton-unitary-probe-repair-v1.json`;
neither recipe was silently replaced or reinterpreted as a native stage.

## Protect the admitted states before synthesizing the control

Let Q=I-L and define the separately preregistered recipe

    H=Q(A+A^dagger)Q,
    V=(I-s H)(I+s H)^-1.

H acts only on locally rejected directions. Exact calculation gives

    H^dagger=H, HL=LH=0,
    V^dagger V=I,
    VL=LV=L,
    VN=NV=N,
    VG=GV,
    VU_p=U_pV  for every source-generated geometric action U_p.

The unitary identity follows from the Hermitian Cayley transform; HL=LH=0
forces V to be identity on im L. The relation N=NL=LN then gives VN=NV=N.
Covariance follows because A and L commute with every U_p. The unchanged G
also commutes with this blockwise covariant recipe, checked directly against
its native coefficients.

Consequently inserting V before the native schedule leaves its full output
unchanged:

    NGLV=N.

The source still has the same 1,836 native transfers; this is an additional
chosen control, not a revised interpretation of those transfer entries.

## Recover the information the native schedule would reject

Use the same fixed probe (AB,x). On retained or reproducible raw input x,
collect

    y_(p,k)=e_(AB,x)^T U_p V^k x,
    p in A4, k=0,1,2.

There are 36 complex scalar readings. The observation matrix O has rank 36,
and the stored exact decoder D satisfies DO=I36. Independent rational
realification verifies the complete identity on all 72 rational basis vectors.

The local reason is retained, rather than inferred from one global rank:
for all twelve triangles and all three possible coordinate axes, the three
rows of I,V,V^2 restricted to that triangle have rank three. The twelve
geometric orientations carry the fixed probe through the twelve triangles,
so the local observation matrices assemble into full recovery.

On im L, V does nothing. On the two rejected directions per triangle it supplies
distinct probe responses; the three local readings can separate those rejected
contributions from the unchanged selected amplitude. The original native
one-probe observation had a twelve-dimensional kernel. Its explicit hidden
vector is detected by the new readings while its norm is conserved.

This is possible even though V preserves L: geometric rotations and controls
that are merely scalar functions of L cannot distinguish the two complementary
directions, whereas Q(A+A^dagger)Q has additional structure within that
complement. Preserving a subspace does not require acting as a single scalar
on its complement.

The raw record must remain available. If local selection has already discarded
Qx, then V(Lx)=Lx; the new control cannot recover that loss. An unchanged terminal
return is not itself a source of the additional readings.

## What task has actually been solved?

**Solved on this coefficient realization:** complete raw-input reconstruction
with one coordinate probe, native norm preservation and pointwise protection of
every admitted local state, using the explicitly extended control/readout
language. The 36 scalar readings are dimension-minimal for an arbitrary
36-complex-dimensional input.

**Not supplied:** physical access to V, exact complex-amplitude measurement,
retention or reproducibility of an arbitrary quantum input, or a law uniquely
selecting this Cayley synthesis. The adjoint, projection onto Q and chosen
scale are declared mathematical construction permissions, not operations
already executed by the original stage network. No physical energy or mass
is inferred from them.

The result is a feasibility construction: the earlier nonunitary decoder is
not the only algebraic way to obtain the missing information. The obstacle is
not conservation of norm or protection of the selected mode; physical control
access remains a distinct obligation.

## Exact verification

Both contracts were frozen before their respective tests:

- Unprotected recipes: SCC fingerprint
  `7bb8a1b7e88feede4f2312a47b04ebed980718d9291c9bc11c22003850302dba`.
- Protected recipe: SCC fingerprint
  `281e84cac181e0cab5092dd2d4add6b8d4b9a3513334ed90754217fbbc94d85a`.

    python research/voevodsky/checkers/check_proton_unitary_probe_repair.py
    python research/voevodsky/checkers/check_proton_protected_unitary_probe.py

Both fresh source reconstructions match the entire archived typed manifest.
Exact native identities, covariance, all 36 local observer ranks and full
decoders pass, with independent rational rank/inverse calculations. Receipts
retain full generators, controls, observation matrices, decoder matrices,
source hashes and the failed protection checks for the initial recipes.
Shared sources and stores remain unchanged.

Artifacts:

- `results/proton-unitary-probe-repair-v1.json`.
- `results/proton-protected-unitary-probe-v1.json`.
- Corresponding owner-local `inputs/` contracts and `scc-models/` manifests.

This is an exact finite-carrier construction, not a new proof-assistant theorem
or physical apparatus certification.
