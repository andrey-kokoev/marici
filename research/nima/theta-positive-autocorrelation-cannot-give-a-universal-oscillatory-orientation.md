# Positive autocorrelation cannot give a universal oscillatory orientation

## Status

Decisive no-go theorem for the unconditional sign route.

Grothendieck's doubled-tail calculation gives, for \(z=\sigma+it\),

\[
\rho(d)=2\int_0^\infty f(q)f(q+d)\,dq\ge 0,
\]

\[
K(z)=\int_0^\infty \rho(d)\sinh(zd)\,dd,
\]

and

\[
\operatorname{Re}K(\sigma+it)
=
\int_0^\infty
\rho(d)\sinh(\sigma d)\cos(td)\,dd.
\]

At a zero-state the Green identity is

\[
\sigma\int \mathcal N=-\operatorname{Re}K(\sigma+it).
\]

Thus an off-seam zero with \(\sigma\ne0\) requires

\[
\sigma\,\operatorname{Re}K(\sigma+it)<0.
\]

The question is whether positivity of the source autocorrelation can prohibit that sign.

## Universal sign is impossible

Fix \(\sigma>0\) and set

\[
g_\sigma(d)=\rho(d)\sinh(\sigma d),\qquad d\ge0.
\]

The theta decay makes \(g_\sigma\) integrable in the strip under consideration. Extend it evenly to the real line:

\[
\widetilde g_\sigma(d)=g_\sigma(|d|).
\]

Its Fourier transform is twice the cosine transform:

\[
\widehat{\widetilde g_\sigma}(t)
=
2\operatorname{Re}K(\sigma+it).
\]

Assume that

\[
\operatorname{Re}K(\sigma+it)\ge0
\]

for every real \(t\). Then \(\widetilde g_\sigma\) has a nonnegative Fourier transform, so it is positive-definite. Every positive-definite function satisfies

\[
|\widetilde g_\sigma(d)|\le \widetilde g_\sigma(0).
\]

But

\[
\widetilde g_\sigma(0)
=
\rho(0)\sinh(0)
=
0.
\]

Therefore \(\widetilde g_\sigma\) would vanish identically. This contradicts the nontrivial positive theta source, for which \(\rho(d)>0\) on a nonempty interval and hence \(g_\sigma(d)>0\) there.

Consequently, for every fixed \(\sigma>0\), the function

\[
t\longmapsto\operatorname{Re}K(\sigma+it)
\]

must take negative values. By the reciprocal symmetry, the corresponding reversed statement holds for \(\sigma<0\).

## Consequence

Source positivity determines the autocorrelation measure but does not orient its oscillatory cosine readout. Negative lobes are structurally unavoidable, not hostile defects.

The remaining statement would have to be conditional:

> Zeros of the even completed section never occur at frequencies where the odd forcing readout has the sign required by a nonzero off-seam state.

By the Green identity itself, that conditional statement is already zero confinement. It is not an independent explanation unless a separate source operation couples the even section and the odd current before either is scalarized.

## Pre-trace typing

Benincasa's Hadamard audit identifies the same distinction in the finite geometric model:

- the selected-sheet covector retains an odd endpoint component;
- the deck trace annihilates it.

Therefore the required coupling cannot be reconstructed after the deck trace. Its source order must pair the even and odd source channels before applying the physical readout. Tracing away the odd channel and then inferring its relation to the scalar section is inadmissible.

The occurrence labels have not yet been identified with the marked geometric sections, so this is a typing constraint rather than a transported theorem.

## Decisive next gate

The unconditional positivity lane is closed. A surviving advance must construct, independently of the zero set, a pre-trace source relation between \(\mathcal X(\sigma,t)\) and \(\operatorname{Re}K(\sigma+it)\).

Admissible candidates include a source-derived intertwiner, conservation law, or elimination identity on the joint even/odd carrier. Merely requiring the forbidden sign at zeros restates RH through the Green identity.

## Finite falsifier

For any proposed universal orientation theorem, fix one \(\sigma>0\). A single height \(t\) satisfying

\[
\operatorname{Re}K(\sigma+it)<0
\]

falsifies it. The existence theorem above guarantees such a height for every nontrivial positive theta source; numerical localization is only a witness, not part of the proof.
