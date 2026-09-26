# Primary operator recovered: the missing map is contact extraction, not an unspecified observable

## Direct primary-source read

Read the local arXiv:2401.05207 source `temp/triangle-measure-primary-2401.05207-source/GeomCosmoCorr.tex`, lines625–729, labels eq:PD1, eq:PD2, eq:Oav, eq:OavP, eq:CC and eq:CC2.

The source explicitly declares:

    P[Phi]=|Psi[Phi]|^2 / integral |Psi|^2,
    O_phys[Phi]=product_j Phi(p_j),
    <O_phys>=integral P O_phys.

Its perturbative distribution contains a Gaussian free factor and higher wavefunction-coefficient insertions. Erased-edge reciprocal two-point factors arise after Gaussian contractions. Ledger2211 identifies their covariance susceptibility, and ledger2218/2219 require an independently frozen contact-normal extraction to remove other contributions.

Thus the physical operator is not absent. What has not been supplied in the inspected evidence is a norm-controlled lift of the selected contact-normal perturbative coefficient to a fixed observable in the three independent real-mode Gaussian Hilbert space used in our controls.

## The diagram that must actually be constructed

Keep distinct:

    (normalized interacting state, boundary-field operator)
        -> perturbative expectation coefficients
        -> labelled graph/deletion coefficients
        -> contact-normal associated grade
        -> retained mixed response packet.

The previous Gaussian polynomial O_C is a realization of the last packet's covariance moments. It is not identified by the primary source with O_phys. Separate per-mode parity of O_phys is not supplied by the source: products of boundary fields and interaction insertions have their own momentum and symmetry constraints. Arbitrary Gaussian-invisible additions are likewise not automatically admissible.

Consequently neither the conditional uniqueness theorem nor the all-bounded-test norm bound for O_C can be imported to the full physical operator without this extraction/lift map and its topology.

## Exact normalization control

Take a real Gaussian mu_g of variance g and a positive perturbative weight1+lambda V for lambda>=0, with V=X^2. For a fixed O=X^2,

    P_(g,lambda)=mu_g(1+lambda V)/(1+lambda E_g V),
    E_P O=(g+3lambda g^2)/(1+lambda g).

Its first interaction coefficient is

    [lambda] E_P O=Cov_g(O,V)=2g^2,

not the unnormalized insertion E_g(OV)=3g^2. Its logarithmic covariance response is4g^2, not6g^2. In general the coefficient is

    E_g(OV)-E_g O E_g V.

The subtraction can depend on g, so folding a normalized perturbative coefficient into a fixed Gaussian test requires proof. A polynomial with the same expectation, such as (2/3)X^4 in this example, is a moment realization, not the physical operator X^2 or an equality of their measurement norms.

This is a type-checking control, not a replacement action or a new cosmological counterterm. It does not contradict the normalized score identity for a fixed observable and its declared measure.

## Disposition of earlier results

- Source contact covariance susceptibilities and algebraic score recovery remain established in their declared scope.
- The finite Gaussian score metrics and all exact controls remain valid for that model.
- Source physical-operator identification is now explicit, not globally missing.
- The lift from a graph/contact-normal perturbative coefficient to a normed observable remains an open source-level comparison.
- The canonical lift's L2 collapse is conditional evidence, not a no-go for all physical measurements.

## Next executable task and handoff

Derive the lowest nontrivial normalized contact extraction before Gaussian contraction, retaining the normalization subtraction, field insertions, momentum labels and source contact-normal map. Test whether it commutes with covariance differentiation at that level and whether it has a bounded Hilbert-space realization. Start from the existing primary formulas rather than a new toy family.

Ask the owner for the precise operator-level contact extraction intended by ledger2216/2219 and any separately even lift theorem. The request is asynchronous while the owner is offline; local reconstruction remains active. No source artifact is edited or owner adoption presumed.

## Verification

`uv run --with sympy python research/voevodsky/project-compatibility/check_contact_primary_typing.py` hashes the read primary source, checks the exact positive-weight normalization control and its covariance derivative, and verifies the relevant primary equation labels. It does not prove the missing contact-operator map.
