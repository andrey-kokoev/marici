# G2 selected constructor is strict Adams action, not prime multiplication

Date: 2026-09-08

## Specification correction

The generic coherence packets discussed a possible multiplicative assembly
`e_p star e_q` with a `pq` target.  The selected retained RH constructor does
not admit that operation.  Its nontrivial monoid action is Adams grade
reindexing within one prime fibre:

\[
S_re_{p,k}=e_{p,rk}.
\]

Distinct primes assemble by labelled direct sum.  Therefore no source rule for
a primitive `pq` object is missing from the selected G2 theory.

## Strict lifted action

For the retained closed graph `Jx=(x,Ax,Cx)`, define

\[
\widetilde S_rJx=JS_rx.
\]

Since the source action obeys

\[
S_sS_r=S_{sr},\qquad S_1=I,
\]

the lifted action obeys the same identities strictly.  Thus associativity,
unitors, triangle, pentagon, and the grade-six diamond require no additional
phase or higher cell.

The weighted analytic realization is compatible:

\[
\mathcal I S_r=M_{\rho_r}U_r\mathcal I,
\qquad
M_{\rho_s}U_sM_{\rho_r}U_r=M_{\rho_{sr}}U_{sr}.
\]

Reciprocal reflection, moving-seam Fourier transport, Green pullback, and
prime/grade cutoffs have explicit naturality formulas.  The source identity
coordinate transports these formulas to the completed graph without an
output-only pseudoinverse.

## Dagger qualification

Grade division is the adjoint in the unweighted labelled pairing:

\[
S_r^*=D_r,
\qquad D_rS_r=I,
\qquad S_rD_r=P_{r\mid k}.
\]

This does not make weighted Adams an invertible coherence equivalence.  It
supplies the correct partial adjoint while the forward operation remains a
directed contraction in the weighted realization.

## Review verdict

For the selected constructor system:

- distinct-prime binary assembly is strict labelled direct sum;
- Adams composition is a strict source monoid action;
- structural coherence is source-unitary and depth independent;
- weighted realization has exact semigroup and cutoff compatibility;
- the completion is inherited through the retained closed graph.

Accordingly G2 is a coherent closure candidate on this architecture.  The
previously listed multiplicative-`pq` and arbitrary two-atom mixed-cell gates
apply only to a stronger constructor theory that is not admitted here.

This review does not mutate the ledger or establish G4/RH.

## Durable inputs

- `research/nima/the-retained-graph-lifts-adams-reindexing-to-completed-constructor-coherence.md`
- `research/nima/rh-g1-4-prime-diagonality-is-exact-on-the-retained-labelled-carrier.md`
- `research/voevodsky/retained_direct_sum_closes_structural_not_incidence_coherence_20260908.md`
- `research/voevodsky/weighted_adams_is_a_directed_contraction_not_a_coherence_equivalence_20260908.md`
