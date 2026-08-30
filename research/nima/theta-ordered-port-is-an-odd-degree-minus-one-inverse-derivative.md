# The ordered theta port is an odd degree-minus-one inverse derivative

## Exact operator identities

On a rapidly decaying source core on the real line, define

\[
(Sh)(q)
=
\int_{\mathbb R}\operatorname{sgn}(v-q)h(v)\,dv.
\]

Let

\[
D=\frac{d}{dq}.
\]

Differentiating the kernel in \(q\) gives

\[
DS=-2I.
\]

Integration by parts in \(v\) gives, on the same core,

\[
SD=-2I.
\]

Thus the ordered port is exactly

\[
S=-2D^{-1}.
\]

With the Fourier convention under which \(D\) has multiplier \(i\xi\), \(S\) has the distributional multiplier

\[
-\frac{2}{i\xi}.
\]

The singularity at \(\xi=0\) exposes a possible ambiguity if only a one-sided inverse law is imposed.

## One-sided ambiguity and full uniqueness

Suppose \(T\) is another operator on the source core satisfying only

\[
DT=-2I.
\]

Then

\[
D(T-S)=0.
\]

Therefore \(T-S\) takes values in \(\ker D\), the constant mode. Equivalently, there is a functional \(\ell\) such that

\[
T=S+\mathbf 1\otimes\ell
\]

whenever the constant distribution \(\mathbf 1\) is admitted by the rigging.

The full signature removes this freedom. The second inverse law \(TD=-2I\) requires \(\ell D=0\), making \(\ell\) proportional to the integral functional on the Schwartz core. Reciprocal oddness requires \(\ell R=-\ell\), whereas the integral functional is reflection-even. Hence \(\ell=0\).

Thus \(DS=SD=-2I\) together with \(RSR=-S\) fixes \(S\) uniquely on the declared core. Primitive and square arithmetic currents are not ambiguities of \(S\); they can enter only through the arithmetic source incidence into the ordered pairing.

The archimedean boundary is also not a free constant-mode choice. It arises because Fourier transformation does not commute with half-line projection. Identifying that universal Hardy/Hilbert boundary with the completed endpoint current still requires a source-derived incidence theorem.

## Reciprocal character

Let reciprocal reflection act by

\[
(Rh)(q)=h(-q).
\]

Direct substitution gives

\[
SR=-RS,
\]

or equivalently

\[
RSR=-S.
\]

Hence \(S\) exchanges the two reflection characters:

\[
S:\mathcal H_+\longrightarrow\mathcal H_-,
\qquad
S:\mathcal H_-\longrightarrow\mathcal H_+.
\]

It is not an endomorphism of either scalar half-sector. This is the exact operator reason the odd forcing is visible before reciprocal trace and disappears under an even trace.

## Dilation degree

For the unitary dilation

\[
(U_a h)(q)=a^{1/2}h(aq),
\qquad a>0,
\]

a change of variables gives

\[
S U_a=a^{-1}U_a S.
\]

Equivalently,

\[
U_a^{-1} S U_a=a^{-1}S.
\]

The ordered port has dilation degree \(-1\). Any proposed Fourier–Tate boundary current representing this port must carry the same degree after its source and target riggings are accounted for.

## Complete operator signature

Before arithmetic incidence is introduced, the ordered port has the signature

\[
DS=SD=-2I,
\]

\[
RSR=-S,
\]

and

\[
U_a^{-1}SU_a=a^{-1}S.
\]

These three relations type it simultaneously as:

- an inverse derivative;
- an odd reciprocal-character morphism;
- a degree-\(-1\) dilation morphism.

This is stronger than identifying it merely as an oscillatory integral.

## Consequence for the three completed currents

The earlier conjecture that the primitive, square, and archimedean currents might all be renormalization data for \(S\) was too coarse.

At operator level, the full two-sided and reciprocal signature fixes \(S\). The three currents have different possible roles:

1. The archimedean endpoint may encode the Hardy/Hilbert boundary created by the failure of Fourier transform to commute with half-line projection.
2. The primitive current may specify how labelled valuation generators enter the source argument of the ordered pairing.
3. The square current may supply the first non-trace-class correction to that arithmetic incidence.
4. The trace-class tail may then extend without changing the operator identity of \(S\).

These roles are hypotheses to be tested, not consequences of the scalar cumulant decomposition.

## Source-level bridge now required

The remaining construction should not attempt to derive \(S\) again. It should construct an arithmetic incidence map

\[
I_{\mathrm{arith}}:\mathcal V_{\mathrm{Fock}}\longrightarrow\operatorname{Dom}S
\]

and a source-derived Hardy boundary incidence for the half-line projection. The completed ordered current must be induced by the fixed operator \(S\), not by an arbitrary constant-mode extension. The incidence must preserve the reciprocal character and dilation degree. It must also reproduce the primitive, square, and connected-tail cutoff currents without collapsing their types.

## Finite falsifiers

A proposed boundary realization \(J\) fails immediately if any of the following residuals is nonzero on its declared core:

\[
DJ+2I,
\]

\[
RJR+J,
\]

or

\[
U_a^{-1}JU_a-a^{-1}J.
\]

If the first residual has range only in the constant mode, the one-sided inverse test is inconclusive. The second inverse and reciprocal-odd tests must eliminate or type that residual; it cannot be accepted as a free endpoint choice.

A degree-zero or reflection-even current cannot represent the ordered theta port, regardless of scalar agreement after trace.

## Disposition

Fourier conjugation does not create an unrestricted new operator. It identifies the odd forcing port as the uniquely typed inverse derivative under the full signature. The RH frontier has moved from discovering the operator to constructing the labelled arithmetic and Hardy-boundary incidences and proving that completion preserves its odd degree-\(-1\) signature.
