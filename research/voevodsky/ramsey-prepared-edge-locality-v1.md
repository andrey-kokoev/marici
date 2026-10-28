# The actual uv edge loses prepared directions needed by the proton trace

## Prospective support and domain

The preceding whole-field audit found that every PN-pulled proton tangent observation has support on all36 neutron coordinates. This new attempt narrows the domain to the existing five-dimensional prepared image and declares the local support before testing.

Use the source reader's sector0, with incoming face F_buv and outgoing face F_cuv. Their actual patches incident to uv have both intrinsic axes selected, giving slots `[0,1,6,7]`. The source geometry identifies this edge as L1–U0. Under the explicitly supplied P marking A=a,B=b,C=u,D=v, the corresponding proton edge is CD.

This is a stronger local measurement than keeping only the edge-tangent axis: both plane coordinates of each adjacent patch are available. No coefficient or field coupling is refitted.

## Exact prepared-domain obstruction

Let B_N and B_P be the source full-five embeddings and Pi the native PN permutation. The desired two-row prepared observation in neutron coefficient coordinates is

    F = H_CD B_P Pi^-1.

Let A be B_N restricted to the four local coordinates. A local factorization would require L A=F. Its weighted Gram is exactly

    A* M_local A = diag(1/3, 1193/4485, 0, 0, 1/3).

Thus A has rank3. More importantly, the checker supplies explicit lost directions rather than relying only on the rank count:

    A e2 = A e3 = 0,
    F e2 != 0,  F e3 != 0.

Both components of each required observation are nonzero. Each prepared field B_N e2 and B_N e3 has norm1. Therefore no linear local readout on those four coordinates can produce F on the prepared domain.

Indeed the same indistinguishable-input witness also excludes a deterministic readout using only that local measurement on the full declared preparation family: the zero field and these nonzero fields have identical local data but different required output. This does not exclude another preparation restriction, an additional contextual input, or a different target observation.

## Explicit enlarged-support factorization

As a separate declared control, include the corresponding two patches in all three reader sectors. This gives12 intrinsic coordinates on three distinct geometric edges:

- L1–U0;
- L0–U1;
- L2–U2.

The resulting prepared matrix A_ext has rank5 and a positive diagonal weighted Gram. The exact decoder

    D = (A_ext* M_ext A_ext)^-1 A_ext* M_ext

satisfies D A_ext=I5. The constructed observation F D then satisfies `(F D) A_ext=F` exactly. The receipt retains the decoder and observation matrices.

This is an actual restricted-domain reconstruction, not a claim that the whole neutron field has been recovered. Nor does using the same abstract reader names u,v turn those three geometric edges into one edge. The repair is explicitly context-assisted and spatially enlarged.

## Consequence for the Ramsey branch

Both the whole-field and prepared-field versions of this particular edge-local readout now fail under the existing PN and full-five binding. That narrows what may be claimed from native retained incidence and full-field sewing: they do not automatically supply local scalar boundary data.

The parent conjecture remains open. A legitimate next candidate can retain the extra context observations rather than erase them. The enlarged12-coordinate instrument is not yet minimal: because the local measurement loses two independent prepared directions, at least two additional scalar linear observations are necessary for full prepared reconstruction. Testing which actual off-edge source coordinates supply those two directions is a nonredundant next step. Any such repair must keep its enlarged support explicit when constructing edge/vertex incidence witnesses.

## Verification

Contract: `contracts/ramsey-prepared-edge-locality-attempt.v1.json`.
Checker: `checkers/check_ramsey_prepared_edge_locality.py`.
Receipt: `results/ramsey-prepared-edge-locality-v1.json`.
Passing freeze: `scc-freezes/ramsey-prepared-edge-locality-v1.a9ef2a6a0aa3c6d4.json`.

Fresh direct hashes bind the geometric edge audit and full-five source. The source's reader patch indices are independently matched to the retained ordered triangle registry. The SCC challenge passes the exact obstruction-and-repair checks; it does not report that the local existence claim survived. No physical detector, net revision, graph verdict or Git checkpoint is asserted.
