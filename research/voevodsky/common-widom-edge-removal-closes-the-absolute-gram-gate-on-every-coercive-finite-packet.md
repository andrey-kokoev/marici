# Common Widom-edge removal closes the absolute-Gram gate on every coercive finite packet

## Objective

Advance the remaining prolate-to-Tate absolute-Gram gate using the existing
common-edge construction rather than seeking convergence of the raw physical
legs.

## Input already available

Fix a finite observer packet \(E\). Let \(G_\Lambda^T,G_\Lambda^0\succeq0\)
be the Tate and pure-reference positive regulated Grams after the declared
two-channel volume-bulk removal, and let

\[
D_\Lambda=G_\Lambda^T-G_\Lambda^0.
\]

The centered regulator comparison gives

\[
D_\Lambda\to W
\]

in matrix norm. The classical reference Widom law and boundedness of
\(D_\Lambda\) imply that both positive Grams have the same leading edge:

\[
L_\Lambda^{-1}G_\Lambda^{T,0}\to G_{edge}.
\]

Work after quotienting the edge-null directions and assume
\(G_{edge}>0\) on the resulting packet.

## Exact common edge

Define

\[
C_\Lambda
=G_\Lambda^T-(D_\Lambda)_+
=G_\Lambda^0-(D_\Lambda)_-.
\]

Since \((D_\Lambda)_\pm\) remain bounded while the common edge grows like
\(L_\Lambda G_{edge}\), one has \(C_\Lambda\succeq0\) for all sufficiently
large \(\Lambda\).

Set

\[
E_\Lambda=C_\Lambda^{1/2},
\quad
R_{\Lambda,+}=(D_\Lambda)_+^{1/2},
\quad
R_{\Lambda,-}=(D_\Lambda)_-^{1/2}.
\]

Then

\[
\Phi_\Lambda^T=(E_\Lambda,R_{\Lambda,+}),
\qquad
\Phi_\Lambda^0=(E_\Lambda,R_{\Lambda,-})
\]

have exactly the original positive Grams. The first slot is a literally common
positive edge feature. Removing that common slot leaves

\[
\Phi_\Lambda^{bdry}
=(R_{\Lambda,+},R_{\Lambda,-}).
\]

Its ordinary and signed Grams are

\[
(\Phi_\Lambda^{bdry})^*\Phi_\Lambda^{bdry}
=|D_\Lambda|,
\]

\[
(\Phi_\Lambda^{bdry})^*J\Phi_\Lambda^{bdry}
=D_\Lambda.
\]

## Absolute-Gram convergence

Absolute value is continuous on finite-dimensional Hermitian matrices. Hence

\[
D_\Lambda\to W
\quad\Longrightarrow\quad
|D_\Lambda|\to|W|.
\]

Therefore

\[
\boxed{
(\Phi_\Lambda^{bdry})^*\Phi_\Lambda^{bdry}
\to |W|.}
\]

The square-root legs converge as well:

\[
R_{\Lambda,\pm}\to W_\pm^{1/2}.
\]

After identifying the finite Weil matrix with the restriction of the global
Tate operator \(A_S\), this is exactly

\[
K_\Lambda|_E\to |A_S||_E.
\]

Thus the necessary-and-sufficient absolute-Gram criterion is closed on every
fixed coercive finite packet.

## Physical realization

Any physical regulated feature with Gram \(G_\Lambda^T\) is related to the
canonical feature \((E_\Lambda,R_{\Lambda,+})\) by a partial isometry on its
observer-generated range. Likewise for the reference feature. Hence packetwise
physical embeddings of the common edge and residual legs exist up to unitary
freedom.

What is not proved is that all packets select one pre-existing common closed
physical bulk subspace without these packet-dependent polar transports.

## Updated gate boundary

The absolute-Gram gate now separates into two levels.

### Closed

For every fixed finite packet after the edge-null quotient:

- exact common positive edge removal;
- positive residual two-polarity feature;
- operator-norm convergence of its absolute Gram to \(|W|\);
- packetwise physical realization up to partial isometry.

### Open

- compatibility under packet enlargement, since compression does not commute
  with Jordan positive parts;
- a global closed physical residual feature on the completed source;
- Mosco convergence of the global positive forms;
- a packet-independent physical identification of the common Widom edge;
- exact-intersection/Sonin and endpoint Green channels, treated separately.

## Consequence

Residual channel 2 should no longer be described simply as “absolute-Gram
open.” Its finite observer content is solved. The remaining issue is global
functorial assembly:

\[
\boxed{
\text{finite-packet absolute Gram: closed;
completed packet-natural Mosco theorem: open}.}
\]

## Repository dependencies

- `a-common-coercive-widom-edge-allows-exact-positive-reference-removal-on-every-finite-observer-packet.md`
- `bounded-relative-gram-convergence-transfers-the-reference-widom-law-to-the-tate-regulator.md`
- `every-finite-observer-packet-has-a-canonical-convergent-two-polarity-positive-boundary-from-the-centered-gram-matrix.md`
- `prolate-to-tate-bulk-removal-is-exactly-the-absolute-gram-gate-and-is-not-closed-by-signed-sewing.md`
