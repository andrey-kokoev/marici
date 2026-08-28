# Common forcing plus terminal normalization rigidifies each theta tail

## The boundary-value problem

For fixed (z), put

\[
\alpha_+=\frac12+z,
\qquad
\alpha_-=\frac12-z.
\]

The labelled reciprocal tails satisfy

\[
(\partial_x+\alpha_+)T_+=-f,
\qquad
(\partial_x+\alpha_-)T_-=-f,
\]

where the same source current (f(x)>0) appears in both equations. Their
integral construction also supplies the terminal normalizations

\[
\lim_{x\to\infty}e^{\alpha_+x}T_+(x,z)=0,
\qquad
\lim_{x\to\infty}e^{\alpha_-x}T_-(x,z)=0.
\]

These are identities of the source tails, since the normalized quantities
are precisely the remaining endpoint integrals.

## Uniqueness theorem

Let \(\widetilde T_+\) satisfy the same forced equation as (T_+). Their
difference obeys

\[
(\partial_x+\alpha_+)(\widetilde T_+-T_+)=0.
\]

Therefore

\[
\widetilde T_+-T_+=C_+(z)e^{-\alpha_+x}.
\]

The common terminal normalization forces (C_+(z)=0). The identical argument
on the reciprocal sheet gives (C_-(z)=0). Hence

\[
\widetilde T_+=T_+,
\qquad
\widetilde T_-=T_-.
\]

This holds for every complex (z) for which the tails are defined; it does
not require a positivity estimate or a restriction to the critical seam.

## Rejection of the two hostile deformation modes

Consider

\[
\widetilde T_+=he^gT_+,
\qquad
\widetilde T_-=he^{-g}T_-.
\]

Requiring the original forcing gives

\[
\partial_x(he^g)T_+=(he^g-1)f,
\]

\[
\partial_x(he^{-g})T_-=(he^{-g}-1)f.
\]

The uniqueness theorem shows that any solution also preserving the terminal
normalizations must satisfy

\[
he^gT_+=T_+,
\qquad
he^{-g}T_-=T_-.
\]

Thus the radial gauge and rapidity shear are trivial on the source tails.
Equivalently, the only apparent freedom before imposing the terminal
condition is addition of a homogeneous mode. The completed endpoint condition
removes that mode.

This is a genuine canonical-section rigidity theorem at the continuous
labelled-tail level. It rejects divisor-changing deformations without
examining their zero locations.

## Why RH does not yet follow

The theorem rigidifies each source tail before discrete sampling. It does not
yet say that scalar aggregation cannot cancel:

\[
I_\pm(z)=\sum_{n\ge1}T_\pm(\log n,z),
\]

followed by

\[
S(z)=\frac12+P(z)(I_+(z)+I_-(z)).
\]

A rigid canonical section may still have zeros. The remaining problem is no
longer hostile modification of the individual tails. It is whether the
source-defined sampling and aggregation functor can map the rigid nonzero
tail packet to the scalar codiagonal off the seam.

The next impossible-construction target is therefore:

> No solution of the common-forcing, terminally normalized labelled tail
> system can satisfy the completed codiagonal boundary condition at an
> off-seam spectral parameter.

The distinction matters. Source rigidity proves that the object cannot be
silently modified by an extra divisor. Zero confinement still requires an
independent theorem about the canonical object's own global aggregation.

## Completion-sensitive falsifier

The terminal condition is stronger than ordinary decay. A homogeneous mode

\[
C_+e^{-\alpha_+x}
\]

may decay when \(\Re\alpha_+>0\), but its normalized terminal value is
(C_+\), not zero. Any completion topology that remembers only unnormalized
decay admits a false deformation. The boundary coordinate

\[
\lim_{x\to\infty}e^{\alpha_+x}T_+
\]

must therefore remain an explicit typed port. The reciprocal sheet has the
analogous port.

This supplies a concrete completion audit: if either normalized endpoint
functional is discontinuous or discarded, canonical-section rigidity is
lost at infinity.
