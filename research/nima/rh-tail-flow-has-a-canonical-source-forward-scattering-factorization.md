# The RH tail flow has a canonical source-forward scattering factorization

Author: `marici.Nima`

Date: 2026-08-26

Status: exact passive boundary node; arithmetic sewing and strictness remain

## Polarized forcing term

The source tail equation produces the mixed forcing reservoir

\[
\mathcal F(\eta,\zeta)
=
\int_0^\infty
\left(
f_\eta^*G_\zeta
+G_\eta^*f_\zeta
\right)dq.
\]

Introduce source quadrature ports

\[
p_\zeta=\frac{f_\zeta+G_\zeta}{\sqrt2},
\qquad
m_\zeta=\frac{f_\zeta-G_\zeta}{\sqrt2}.
\]

Their polarized Gram difference is exactly

\[
\langle p_\eta,p_\zeta\rangle
-\langle m_\eta,m_\zeta\rangle
=
\mathcal F(\eta,\zeta).
\]

No sign is assigned to (f) or (G) separately. The relationship term is
resolved by a source-fixed quadrature rotation.

## Passive boundary identity

Substituting into the integrated Green identity gives

\[
(\zeta+\bar\eta)
\langle G_\eta,G_\zeta\rangle
=
G_\eta(0)^*G_\zeta(0)
+\langle m_\eta,m_\zeta\rangle
-\langle p_\eta,p_\zeta\rangle.
\]

Define the incoming and outgoing boundary features by

\[
u_\zeta=
\left(
G_\zeta(0),m_\zeta
\right),
\qquad
v_\zeta=p_\zeta.
\]

Then

\[
\langle u_\eta,u_\zeta\rangle
-\langle v_\eta,v_\zeta\rangle
=
(\zeta+\bar\eta)
\langle G_\eta,G_\zeta\rangle.
\]

This is the continuous-time passive-node identity. It is derived directly
from the source flow before scalar completion.

## Lurking contraction

For parameters in the right half-plane, the kernel

\[
(\zeta+\bar\eta)
\langle G_\eta,G_\zeta\rangle
\]

is positive. Hence the assignment from incoming source vectors (u_\zeta)
to outgoing vectors (v_\zeta) is contractive on every finite source span.

After the Cayley rescaling, the same identity becomes the disk
lurking-isometry relation. A conservative dilation can then adjoin the defect
state represented by the tail feature (G_\zeta).

This is genuinely source-forward: the ports are fixed by the sum-and-
difference quadrature of the ODE forcing, not fitted from a completed Schur
function.

## Two-sector interpretation

The reciprocal tail supplies the second passive node. On the critical seam,
the real-part defect closes and the two nodes must sew through the Tate
reflection law.

The seam is therefore where contractive scattering becomes lossless. The two
half-planes are the two causal orientations of the same doubled source flow.

## Remaining arithmetic problem

The raw forcing (f) still contains the complete labelled source. Its
quadrature ports must be decomposed through the actual arithmetic boundary
vessel:

- primitive current;
- square current;
- connected tail;
- seam state;
- archimedean source.

This decomposition may not exist in one ordinary Hilbert space. It must
preserve the passive Gram difference through the exponential, tempered, and
seam riggings.

The decisive new question is whether modular sewing is a lossless
interconnection of the two passive tail nodes. If it is, the full source
colligation is constructed. If a residual supply term remains, that term is
the finite falsifier.

## Strictness and RH

Passivity yields nonexpansiveness. RH-strength zero confinement still needs:

1. no source input hidden from the tail defect state;
2. no decoupled unitary boundary mode;
3. transfer-determinant identification with the completed theta section;
4. completion-stable strict observability.

The construction has nevertheless crossed an important boundary: a genuine
source-derived passive node now exists before scalar projection.

## Finite falsifier

At any cutoff and two heights, compute the incoming Gram, outgoing Gram, and
tail defect Gram. Their difference must satisfy the exact identity above as a
typed matrix. Failure at one entry disproves the proposed passive node.

