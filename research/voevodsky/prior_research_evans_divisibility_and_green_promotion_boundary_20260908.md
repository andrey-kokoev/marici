# Prior research: Evans divisibility and the Green-promotion boundary

Date: 2026-09-08

## Divisibility square already exists on the history carrier

The completed theta forcing has two source-derived stable histories

\[
u_-(q;z)=\int_{-\infty}^q e^{z(q-r)}\Phi(r)\,dr,
\qquad
u_+(q;z)=-\int_q^\infty e^{z(q-r)}\Phi(r)\,dr.
\]

Both solve `(partial_q-z)u=Phi`, and their seam mismatch is exactly

\[
u_-(0;z)-u_+(0;z)=\tau(z)=\xi(z)
\]

in the frozen source normalization.  Consequently the analytic matching operator satisfies the chain square

\[
C_{\rm match}(z)i_{\rm Ev}(z)=w\tau(z).
\]

At a Xi zero, the two histories glue to a nonzero two-ended augmented kernel state.  This closes the Koszul-to-Evans zero-state lift and preserves local multiplicity by parameter differentiation.

## Conservative promotion is the RH-bearing theorem

The Evans state solves the forced triangular history equation but not automatically the lower adjoint equations of the conservative maximal-isotropic Green pencil.  For the unchanged state, injectivity of the centered arithmetic incidence forces its arithmetic coordinate to be zero.  Promotion then requires

\[
V^\dagger u_z=0,
\qquad
B_\Sigma^\dagger u_z=0.
\]

Combined with the already closed Green identity, these equations force the centered real parameter to vanish.  Therefore the Evans-to-conservative chain map is not administrative G4 plumbing: it already contains the RH confinement step.

## Prime-shell form of the obstruction

The arithmetic adjoint residual is equivalent to a countable family of shell identities.  For consecutive primes `p_n<p_{n+1}`, define

\[
s_n=p_{n+1}^{1/2}b_{p_{n+1}}-p_n^{1/2}b_{p_n}.
\]

Then `B_Sigma^dagger u=0` requires

\[
\langle s_n,u\rangle_G=0
\]

for every shell, plus the limiting common-mode condition.  Each pairing decomposes into ordinary, derivative, wall, reciprocal, and linking ports.  The ordinary Evans-tail term has eventually strict negative real part, so nontrivial compensation is required shell by shell.  The single scalar identity `tau(z)=0` cannot supply this countable cancellation family.

## Smallest executable falsifier

At a finite cutoff and a tested Xi zero, evaluate

\[
\mathcal S_{p,q}(z)
=
\left\langle
q^{1/2}b_q-p^{1/2}b_p,
 u_z
\right\rangle_G
\]

for the last consecutive prime pair.  One nonzero value rejects promotion of the unchanged Evans state at that cutoff.  No current packet supplies the complete source-normalized Green port decomposition needed to execute this test without filling missing entries.

## Disposition

Prior research closes the independent incidence/divisibility square on the analytic Evans complex.  It also proves that extending this square to the conservative Green pencil is at least RH-strength and remains open.  The first missing executable input is the source-normalized shell Green pairing, not the Xi section, seam mismatch, or history state.

## Evidence

- `research/nima/the-two-sided-theta-history-mismatch-is-an-exact-evans-lift-of-the-xi-section.md`
- `research/nima/the-g4-chain-map-is-an-exact-divisibility-identity-plus-an-invertible-complement.md`
- `research/nima/the-evans-to-conservative-green-chain-map-already-contains-the-rh-confinement-step.md`
- `research/nima/the-full-adjoint-promotion-is-a-countable-family-of-prime-shell-green-cancellation-identities.md`
