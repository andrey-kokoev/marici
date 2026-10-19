# H9 actual exit dynamics and H10 participant-exchange covariance

## H9 — the stronger exit-intertwining claim is refuted

Use the same energy reference and epsilon=1 as the source exit model. Its exact matrices are stored in `pentachoron_exit_gate_bundle.zip`, member `pentachoron_exit_gate_results.json`, under `exact_matrices`:

    H_pre=HL=diag(Hi,M), Hi=LF+X,
    H_F=HR=diag(H0,M), H0=LF+Di*Di,
    X=D*D+Di*Di, M=D D*.

The proposed claim is **H_F U_exit = U_exit H_pre**, with the actual invertible memory encoder, not with H_F redefined by conjugation.

The archived exact rational diagonal entries give

    tr(H_pre)=136, tr(H_F)=120, tr(M)=16.

Any invertible intertwiner would make the two finite matrices similar and hence give equal traces. Their difference of sixteen refutes the claim for this source fixture, independently of the particular encoder. No floating eigensolver or historical assertion is needed for that trace obstruction. The v2 validator reconstructs these sums directly from the pinned archive bytes and checks tr(Hi)-tr(H0)=tr(M)=16. Its decisive calculation is the unequal exact HL/HR traces; the full matrix energy identities are source-reported, not freshly replayed here.

The source checker `pentachoron_exit_gate.py` separately records nonzero `Delta=N H0 N-H0` and the warning that motion supplies the native-energy remainder. We inspected that source; we did not rerun its full symbolic constructor. The comparison of stored matrices is a fresh exact certificate about those source-bound matrices, not a fresh producer replay.

H3 is not contradicted: transport to **a Hamiltonian defined by conjugation** is different from identification with the independently supplied outgoing native Hamiltonian. Nor does H9 refute energy conservation of the complete scattering model: kinetic energy and channel thresholds remain part of its ledger. No scalar energy shift is allowed in H9, since both sides use the same declared source reference.

## H10 — precise participant exchange, not output coincidence

**Disposition:** refuted within the explicit source-constructor admission scope below. The unchanged constructor fixes chirality to slots rather than transporting it with owners. [Exact local witness and limitation](PARTICIPANT-EXCHANGE-OBSTRUCTION.md). The following specification is retained so the negative result's scope remains visible.

This is covariance of two labelled descriptions of the same supplied encounter, not a claim that the two incident physical species are identical.

### Fixed source data and exchange

Use the unstrained two-endpoint open-hinge model in `pentachoron_open_product_flux_note.md`, with all eight C20 pairing sectors and C8 memory at each endpoint. Take the two participants' complete tagged source packets, including geometry, metric, cycle generator, chirality and spin-lift/phase conventions. Define tau by:

- swap participant tags L and R, carrying **all** attached data, including chirality, with their owner;
- retain geometric vertex names and ambient coordinate frame; do not actively reflect physical space or reset either body's spin frame;
- leave face names and the three-bit switched-face subset labels unchanged;
- exchange the ten cell slots by `(L,i,s)->(R,i,s)` and conversely; spin component s is unchanged in the common ambient trivialization;
- exchange memory rows by their owner and directed cycle-link labels, not by an independently fitted matrix; the four link labels are (L,1->2), (L,2->3), (R,1->2), (R,2->3), each with two spin components at the positive endpoint; at the negative endpoint the adjacent link labels are 2->3 and 3->4 for each owner (the owner-swap permutation is unchanged);
- retain the two geometric endpoint pose labels separately. The passive tag swap is not, by definition, the positive/negative exit exchange or a forced hinge-coordinate reflection.

This gives an explicit permutation X20 on cells, X8 on memory and X28=X20 direct-sum X8. Apply the same slot permutation to all fields and finite pairing sectors to obtain the unitary X on the whole retained Hilbert space. X²=I. The reference isometry here is fixed by record provenance; no solution-dependent phase or eigenspace fitting is allowed.

### Claim

Rebuild the exchanged encounter **independently from the exchanged tagged source packets**, using the same declared seam, switching, cycle and contact formulas and coefficients. Call its quadratic form q_tau and Hamiltonian H_tau. Do not define them by conjugating the original result.

**H10:** X maps the original form domain onto the exchanged form domain and

    q_tau(X psi, X phi)=q(psi,phi),
    H_tau X = X H,
    X exp(-itH)=exp(-itH_tau) X

for all form-domain pairs and all real t (the generator equation on its operator domain). In addition the independently reconstructed boundary couplings and memory encoder obey the corresponding X20/X8/X28 commuting equations. The comparison must preserve ordered switch products, not identify different switch orders. Applying tau twice must recover the original labelled packet and comparison map, X_tau X=I.

If an exchanged input is not admitted by the actual source constructor, record that as an admission-domain failure of this proposed exchange symmetry, not permission to supply a new frame/sign rule. That is part of the test. A nonzero independently computed coefficient defect, a domain mismatch, or a failure of round-trip comparison refutes the specified claim. Agreement of output probabilities cannot accept it.

### Bounded first test

Reconstruct X20, X8 and X28 from the fixed owner labels. Rebuild both endpoint seam/cycle/memory/switch blocks from tau-transformed inputs; check all generator-level commuting equations and domain/contact restrictions. A positive result must account for the source's participant-specific chirality and antipodal spin-lift conventions. Their transport is explicitly fixed above rather than assumed away.

H10 does not depend on H9 being true: a passive relabelling can preserve an encounter whose native energy changes at exit. It uses H1/H2/H3 as shared definitions, not already proved premises. The source-bound test refutes its explicit constructor-admission clause. A richer tag-aware comparison remains a separate possible successor, not an inferred impossibility.
