# The Euler half-density is too contractive to resonate even on the seam

The strict-Schur feedback theorem reveals a second zero-mechanism obstruction.

For the prime-diagonal Euler carrier,
\[
S(z)e_p
=
p^{-1/2}e^{iz\log p}e_p.
\]
On the seam \(z=x\in\mathbb R\),
\[
|p^{-1/2}e^{ix\log p}|=p^{-1/2},
\]
so
\[
\|S(x)\|=2^{-1/2}<1.
\]
Thus the Euler half-density does not merely make the carrier strict off seam. It leaves a fixed contraction gap even on the seam:
\[
I-S(x)^{*}S(x)\ge\frac12 I.
\]

Any purely passive compression inherits this gap. If
\[
J:\mathcal B\to\ell^2(\mathcal P)
\]
is an isometry and
\[
G(z)=J^{*}S(z)J,
\]
then
\[
\|G(x)\|\le2^{-1/2}.
\]
For unitary reciprocal sewing \(C\),
\[
\|CG(x)\|<1,
\]
so
\[
\det(I-CG(x))\neq0
\]
on the seam as well.

More generally, a contractive colligation whose only dynamic channel is uniformly strict and whose direct feedthrough is also strict cannot acquire a unit-modulus transfer value. It cannot support any conservative feedback resonance.

Therefore the completed RH return cannot be a passive compression of the half-density Euler delays alone. A source-derived lossless channel must reach the boundary transfer on the seam.

The likely candidates are:

- the constant--delta wall carrier;
- reciprocal-sheet sewing;
- the archimedean endpoint channel;
- a direct boundary feedthrough \(D\);
- or a conservative dilation channel introduced before compression.

The correct transfer should have the boundary behavior
\[
\|G(z)\|<1
\quad
(\operatorname{Im}z>0),
\]
but permit
\[
\|G(x)\|=1
\]
at isolated real \(x\). In Schur theory this is an inner or partially inner boundary channel. Zeros then occur when its unitary boundary eigenphase matches the reciprocal sewing phase:
\[
1\in\sigma(C G(x)).
\]

This refines the role of the wall. It is not merely the receptacle for a divergent primitive trace. It may supply the lossless boundary direction absent from the attenuated prime carrier.

A block transfer can express the architecture:
\[
G(z)
=
D_{\mathrm{wall}}(z)
+
C_0(z)(I-S(z))^{-1}B_0(z).
\]
Here the Euler resolvent contributes arithmetic phase and prime-power propagation, while \(D_{\mathrm{wall}}\) supplies the source-normalized boundary scale capable of reaching unit modulus.

Passivity imposes a nontrivial coupling law. One cannot simply add a unitary \(D_{\mathrm{wall}}\) to a nonzero dynamic term and remain contractive. For a unitary colligation
\[
\begin{pmatrix}
A&B\\
C_0&D
\end{pmatrix},
\]
the identities
\[
A^{*}A+C_0^{*}C_0=I,
\qquad
B^{*}B+D^{*}D=I,
\qquad
A^{*}B+C_0^{*}D=0
\]
force exact energy exchange between the lossless wall and prime dynamics.

This identifies the next source theorem:

> The wall, archimedean endpoint, and prime-delay carrier form one conservative colligation whose transfer is strictly Schur off seam and has a controlled unitary boundary part on the seam.

The theorem must also prove that the unitary boundary part is not identically resonant. Its phase crossings should match the zeros of \(\xi\), including multiplicity.

The smallest hostile keeps the half-density Euler carrier and unitary sewing but supplies no lossless boundary feedthrough. The resulting determinant is zero-free everywhere, so spectral identification with \(\xi\) is impossible.

A second hostile appends an arbitrary unitary scalar phase chosen from \(\xi/|\xi|\). This creates the desired seam crossings but imports the zero data instead of deriving it from wall and archimedean source constructors.

Thus the zero mechanism has contracted once more: it must be the phase matching of a source-derived lossless boundary channel, modulated by a strictly passive Euler interior.
