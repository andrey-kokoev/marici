# Nodal Component Perfectness No-Go and the Relative Exceptional BM Repair

Date: 2026-08-15  
Status: two scoped no-go theorems proved, with a positive constructible
relative-pair control. Neither theorem obstructs a normalization--conductor
logarithmic/Borel--Moore kernel. The literal entry-143 comparison, physical
mapping fiber, and parity remain unconstructed. The bounded problem
situation was admitted to the epistemic graph by event
`ev-000000000094-3f32b609-f1db-41d2-a77a-aee57c5fbc05`; admission records
policy-valid provenance and does not certify truth.

## Singular nodal component is not a Cartier kernel

Let
\[
A=k[h,p]/(hp),
\qquad
M=A/(p).
\]
The component inclusion \(\operatorname{Spec}M\hookrightarrow
\operatorname{Spec}A\) has the exact alternating matrix-factorization
resolution
\[
\cdots\xrightarrow{p}A\xrightarrow{h}A\xrightarrow{p}A
\longrightarrow M\longrightarrow0.
\]
Exactness follows from
\[
\operatorname{ann}(p)=(h),
\qquad
\operatorname{ann}(h)=(p).
\]

After tensoring with \(M=k[h]\), the \(p\)-differentials vanish and the
\(h\)-differentials remain injective. Consequently
\[
\operatorname{Tor}_0^A(M,M)=M,
\qquad
\operatorname{Tor}_{2j+1}^A(M,M)=k,
\qquad
\operatorname{Tor}_{2j}^A(M,M)=0\quad(j\ge1).
\]
Dually,
\[
\operatorname{Ext}_A^0(M,M)=M,
\qquad
\operatorname{Ext}_A^{2j}(M,M)=k,
\qquad
\operatorname{Ext}_A^{2j+1}(M,M)=0\quad(j\ge0).
\]

Thus the positive Tor and Ext tails continue indefinitely. The singular
component inclusion has infinite projective dimension and is neither a
Cartier nor a perfect finite-amplitude Gysin kernel:
\[
\boxed{
\operatorname{Spec}(A/(p))\hookrightarrow\operatorname{Spec}A
\text{ cannot supply the required finite two-grade endpoint Gysin.}
}
\]
This does not obstruct replacing the singular inclusion by a strict Cartier
divisor on a smooth blowup or by a normalization/log conductor object.

## Bare coherent exceptional ideal has zero trace

Now let
\[
q:E=\mathbb P^1\longrightarrow\operatorname{Spec}k
\]
be the exceptional fibre and let \(C\subset E\) be the marked conductor
point. The bare coherent conductor ideal is
\[
J_E=\mathcal O_E(-C)=\mathcal O_{\mathbb P^1}(-1).
\]
Standard line-bundle cohomology gives
\[
Rq_*J_E=0.
\]
The internal-Hom dual variant also fails:
\[
R\mathcal Hom(\mathcal O(-1),\mathcal O(-2)[1])
=\mathcal O(-1)[1],
\qquad
Rq_*\mathcal O(-1)[1]=0.
\]
The tensor variant is not primitive:
\[
\mathcal O(-1)\otimes\mathcal O(-2)[1]
=\mathcal O(-3)[1],
\qquad
\operatorname{rk}R^1q_*\mathcal O(-3)=2.
\]
Likewise an unshifted map
\(\mathcal O(-1)\to\mathcal O(-2)\) would be a section of
\(\mathcal O(-1)\), hence is zero.

The actual relative dualizing complex behaves differently:
\[
\omega_E[1]=\mathcal O(-2)[1],
\qquad
\operatorname{rk}R^1q_*\mathcal O(-2)=1.
\]
Therefore the scoped conclusion is
\[
\boxed{
J_E=\mathcal O(-1)\text{ is not a proper unit-trace kernel;}
\text{ the relative dualizing object is essential.}
}
\]

## Positive control: the relative/log pair

Give \(E=\mathbb P^1\) its oriented top cell and take the marked conductor
point \(C\) as the full zero-cell subcomplex. Then
\[
C_*^{\mathrm{BM}}(E,C)
=[\,\mathbb Z\langle[E,C]\rangle\,]
\]
in top degree, and
\[
H_2^{\mathrm{BM}}(E,C;\mathbb Z)\cong\mathbb Z.
\]
Its oriented generator is primitive. Thus the no-go is specific to the bare
coherent ideal; the relative/log/constructible pair retains exactly the
rank-one Borel--Moore top class needed for a possible extraordinary trace.

This positive control is not yet a map to the physical endpoint. It neither
identifies \([E,C]\) with a literal entry-143 state nor supplies the required
Beck--Chevalley cell.

## Combined boundary

The two shortcuts fail for complementary reasons:

- the singular component has too much derived self-intersection: infinite
  two-periodic Tor/Ext;
- the bare coherent exceptional ideal has too little pushforward:
  \(Rq_*\mathcal O(-1)=0\).

A valid construction must pass between these extremes. It must retain the
finite normalization--conductor boundary and the relative oriented top
class, while using the genuine relative dualizing complex rather than the
singular inclusion or bare ideal.

The smallest admissible repair is therefore a
normalization--conductor divisorial log/constructible Borel--Moore kernel
\[
\mathcal K_{v_+}^{\log,\mathrm{BM}}
\simeq
C_*^{\mathrm{BM}}(E,C)\otimes\omega_{E/C}[1],
\]
realized on a smooth proper modification, together with:

- both conductor Tor grades as boundary data, not as the unbounded singular
  self-Ext algebra;
- the primitive relative BM orientation;
- the Grothendieck-duality counit from the relative dualizing factor;
- a support-typed Beck--Chevalley map to the literal entry-143 endpoint
  costalk.

The last item remains the earliest spatial gap. Until it and the polarity
endpoint, generic \(Q\) leg, and endpoint connector cells exist, the physical
mapping fiber is uninstantiated. Hence \(p_{\partial,Q}\), its parity, and its
Bockstein are undefined.

## Falsifiers and counterevidence

The nodal no-go is falsified if the displayed matrix factorization terminates,
if either annihilator identity fails, or if the positive odd Tor/even Ext
tails vanish eventually.

The coherent exceptional no-go is falsified if
\(Rq_*\mathcal O(-1)\neq0\), if the dual variant acquires a unit, or if the
tensor variant has primitive rank-one rather than rank-two \(R^1\).
The positive control is falsified if
\(H_2^{\mathrm{BM}}(\mathbb P^1,C;\mathbb Z)\) is not primitive rank one.

A future log/constructible extraordinary trace would not contradict either
no-go. Conversely, the existence of the relative top class alone does not
construct its entry-143 comparison.

## Provenance and validation

Exact certificates:

- research/voevodsky/check_d03_nodal_component_gysin_no_go.rs, SHA-256
  e26bb4e58f38501e8b0303cafdf41f08024dc5740e4c0216193ccb3f93a391a9;
- research/voevodsky/check_d03_exceptional_p1_coherent_trace_no_go.rs,
  SHA-256
  11aa87861947a3b0a4afa074f5e303c6ab4950ab01c318c4bedc3b9cd8763694.

For both certificates, the independent delegated audit reported:

- rustfmt check: PASS;
- metadata compilation with rustc and warnings denied: PASS;
- runtime: **not executed**, because the delegated worker did not have the
  required MSVC libraries.

The claims above are sourced from the checked programs and their metadata
validation, not from a claimed runtime execution.

Relevant ledger inputs are entries 93, 143, 168, 173, 176, and 186.

## Next experiment

Construct the relative/log BM kernel on the smallest smooth proper
normalization--conductor modification. Compute its dualizing trace and then
build the literal entry-143 Beck--Chevalley comparison. Test both conductor
Tor grades and the relative top generator before adding the polarity
endpoint, generic \(Q\) leg, mapping fiber, or parity.

## Outcome contract

~~~json
{
  "claim": "For the nodal ring A=k[h,p]/(hp), the component A/(p) has an infinite 2-periodic resolution with nonzero positive odd Tor and positive even Ext, so its inclusion is not a Cartier/perfect finite Gysin kernel. On the smooth exceptional E=P1 with marked conductor C, the bare coherent ideal O(-C)=O(-1) and its internal-Hom dual push forward to zero, while the tensor dual has rank-two R1; only the true dualizing O(-2)[1] has primitive rank-one trace. The relative constructible pair (E,C) retains a primitive BM top class.",
  "status": "falsified",
  "scope": "naive singular-component finite Gysin and bare coherent exceptional-ideal unit trace only; normalization-conductor relative/log/constructible BM kernels are not obstructed",
  "factorization": {
    "nodal_ring": "A=k[h,p]/(hp)",
    "component": "M=A/(p)",
    "resolution": "infinite 2-periodic with d_odd=p and d_even=h",
    "Tor": "Tor0=M, positive odd=k indefinitely, positive even=0",
    "Ext": "Ext0=M, positive even=k indefinitely, odd=0",
    "finite_projective_dimension": false,
    "finite_Cartier_Gysin": false,
    "exceptional_pair": "(E,C)=(P1,point)",
    "coherent_ideal": "J_E=O(-1)",
    "Rp_star_J_E": 0,
    "internal_Hom_dual_pushforward": 0,
    "tensor_dual_R1_rank": 2,
    "dualizing_O_minus_2_shift_1_R1_rank": 1,
    "relative_BM_H2_rank": 1,
    "relative_BM_top_primitive": true,
    "literal_entry143_BC_map": "unconstructed",
    "physical_mapping_fiber": "unconstructed",
    "physical_p_partial_Q": "undefined",
    "physical_Bockstein": "undefined"
  },
  "checker_validation": {
    "nodal_component_sha256": "e26bb4e58f38501e8b0303cafdf41f08024dc5740e4c0216193ccb3f93a391a9",
    "exceptional_p1_sha256": "11aa87861947a3b0a4afa074f5e303c6ab4950ab01c318c4bedc3b9cd8763694",
    "rustfmt_check": "PASS for both",
    "rustc_metadata_D_warnings": "PASS for both",
    "runtime": "NOT EXECUTED: MSVC libraries unavailable under delegated worker"
  },
  "evidence_refs": [
    "research/voevodsky/check_d03_nodal_component_gysin_no_go.rs",
    "research/voevodsky/check_d03_exceptional_p1_coherent_trace_no_go.rs",
    "src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md",
    "src/ledger/20260815-168 Full Rees First-Flip Occurrence Kernel and the External Normal Gate.md",
    "src/ledger/20260815-173 Component-Supported Semistable Node and the vplus Coefficient Counit.md",
    "src/ledger/20260815-176 Central Exceptional Relative Cap and the Conditional Parity Test.md",
    "src/ledger/20260815-186 Direct Affine-Node Endpoint Descent No-Go and the Extraordinary Trace Gate.md"
  ],
  "unconstructed": [
    "normalization-conductor divisorial log/constructible BM kernel",
    "relative-dualizing extraordinary trace on the selected proper component",
    "literal entry-143 Beck-Chevalley endpoint map",
    "polarity endpoint, generic Q leg, and endpoint connectors",
    "physical mapping fiber, p, parity, and Bockstein"
  ],
  "counterevidence": [
    "The singular component retains infinitely many derived self-intersection grades.",
    "The bare coherent exceptional ideal has zero derived pushforward.",
    "The tensor dual has rank-two rather than primitive rank-one R1.",
    "The relative pair has a primitive top class, but no target comparison map."
  ],
  "minimal_repair": "Use a smooth proper normalization-conductor modification with the relative/log constructible pair (E,C), its true dualizing complex, both conductor boundary grades, and a Beck-Chevalley map to the literal entry-143 endpoint costalk.",
  "next_experiment": "Construct that relative/log BM kernel and literal endpoint Beck-Chevalley map before defining the physical mapping fiber or parity."
}
~~~
