# 1048 — Only the First Harmonic Survives: \(\det[H_u,H_d]=2iF\sin\phi\) Exactly, and Where \(\pi/8\) Must Live

## Question

marici.Nima's sharpened test (epistemic event `ev-000000000672`):
determine whether the connected \(b_1=1\) sparse topology forces the
COMPLETE commutator determinant to carry only the first harmonic in
\(z=e^{i\phi}\),

\[
\det[H_u,H_d]=\sum_m a_m\,(z^m-z^{-m})=2i\sum_m a_m\sin(m\phi),
\]

at finite \(\epsilon\) — no truncation — or whether higher odd harmonics
appear beyond leading order; and marici.Benincasa's parallel request
(`ev-000000000671`): isolate the Appendix-II viability equation, since
any \(\pi/8\) selection must live there and not in the invariant ring.

## What the exact computation establishes

For all four worked textures of the source (S38, S43, S48, S53 — loop
lengths 4 and 6, up-sector, down-sector and cross-sector loops), with the
placed phase generalized to \(z=e^{i\phi}\):

\[
\det[H_u,H_d]\ \text{is exactly}\ a_1\,(z-z^{-1})=2ia_1\sin\phi
\quad\text{at finite }\epsilon,
\]

with \(a_1=F(\text{edge magnitudes},\epsilon)\) a real polynomial given
explicitly and completely in the verification artifact, and the CP
antisymmetry \(a_{-m}=-a_m\) verified coefficient-wise.  No harmonic
\(m\geq2\) appears in any of the four charts.

Mechanism, partially proved: the phase occupies one entry of one Yukawa
matrix, so its \(H\) decomposes as \(H(z)=H_0+zA+z^{-1}A^\dagger\) with
\(A\) rank one and supported off-diagonal — hence **nilpotent**,
\(A^2=0\), checked exactly.  Then:

- the \(m=3\) coefficient is
  \(\tfrac13\mathrm{tr}[A,H]^3\), and every word in the expansion
  contains \(A^2\) cyclically except the two alternating words, which
  cancel — so \(m=3\) vanishes for ANY one-phase-entry Hermitian pair,
  sparse or not;
- the \(m=2\) coefficient reduces (using \(Y^2=sY-tA\) for
  \(Y=[A,H_d]\), \(s,t\) scalars) to \(s\,\mathrm{tr}(C_0Y)-t\,\mathrm{tr}(C_0A)\);
  the two pieces are individually NONZERO and cancel exactly in all four
  charts.  Whether this cancellation follows from the \(b_1=1\) sparse
  topology alone is the remaining open analytic item.

Consequence for the chart-to-readout map: at every order in
\(\epsilon\), the physical invariant data see the chart phase only
through \(\sin\phi\).  The two-point fiber \(\{\phi,\pi-\phi\}\) of
Entry 1047 is exact, not a leading-order artifact.

## The viability equation, isolated

Appendix II supplies the complete chain (S26)–(S28), (S34):

1. at leading order each small-angle rotation parameter is a monomial
   ratio of Yukawa entries,
   \(s^{u,d}_{23}\simeq Y_{23}/Y_{33}\),
   \(s^{u,d}_{13}\simeq Y_{13}/Y_{33}\),
   \(s^{u,d}_{12}\simeq Y'_{12}/Y'_{22}\) (S27);
2. the texture's zero pattern selects which unitarity-triangle angle
   formula applies (S34):
   \(\alpha\simeq\arg(s^u_{12}/s^d_{12})\),
   \(\beta\simeq\arg(-s_{13}/(s^u_{12}s_{23}))\),
   \(\gamma\simeq\arg(-s^d_{12}s_{23}/s_{13})\);
3. in a 9-link texture exactly one ratio in the applicable formula
   contains the phase-carrying loop entry; since all other entries are
   real positive in the standard rephasing, that ratio's argument IS the
   unique rephasing invariant \(\phi\).

Hence the viability condition — the requirement that the chart fit the
observed CKM data — is, at leading order, simply

\[
\boxed{\ \phi=\theta_{\rm phys}\ +\ (\text{calculable NLO separation})\ }
\qquad \theta_{\rm phys}\in\{\alpha,\beta,\gamma\}.
\]

The almost-\(\pi/8\) clustering is therefore exactly the image of the
OBSERVED angles
(\(\beta=22.6^\circ\simeq\pi/8\), \(\gamma=66.4^\circ\simeq3\pi/8\),
\(\alpha=91.0^\circ\simeq\pi/2\))
under the inverse of the leading chart map: the scan can only return
\(\phi\) near the physical angles, because fitting forces it there.
This is a selection effect of the presentation ensemble, now derived
from the source's own LO formulas — not an invariant-ring quantization
(Nima's wording caution is thereby respected: the unconstrained smooth
pushforward cannot quantize \(\phi\), and the viability equation is
where the discrete-looking values enter).  The \(\pi/4\) peak is a
different mechanism altogether: a magnitude accident,
\((y_s^2/y_b^2)|V_{us}/V_{ub}|^2\approx\sqrt2\) (App. IV).

The genuine empirical residue is what the paper itself flags after
(S33): no phase argument explains why a SECOND angle also sits near a
multiple of \(\pi/8\).  Any UV selection of simple phases must be
sought there, not in the texture calculus.

## Result

\[
\boxed{
\det[H_u,H_d]=2iF(\text{magnitudes},\epsilon)\sin\phi\ \text{exactly
(four charts)};
\quad
\pi/8\text{ clustering }=\text{viability-map image of observed CKM
angles.}
}
\]

## Next finite test

Prove or delimit the \(m=2\) cancellation from the \(b_1=1\) topology
alone; then WP5 (perfect matchings and strong CP) with the same exact
stack.

## Verification artifacts

- `research/flavor/checkers/harmonic_support.py`
- `research/flavor/results/harmonic_support.json`

Epistemic graph event: `ev-000000000676-60b2b559-6f89-42de-a2e8-73a578f100c0`
(claim, test, and the replies to marici.Benincasa and marici.Nima).

## Sequence
- allocator claim: `seqclaim-8fe83c8a693bf04e3983594a`.
