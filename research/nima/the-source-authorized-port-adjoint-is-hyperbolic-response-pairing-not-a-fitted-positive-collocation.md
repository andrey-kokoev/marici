# The source-authorized port adjoint is hyperbolic response pairing, not a fitted positive collocation

## Positive feasibility is not authority

For the scalar source cone, a positive metric \(G\) satisfying

\[
GB=C^*
\]

exists whenever \(CB>0\). The theta forcing passes this algebraic test.

But the construction of such a \(G\) contains free complement data. It does
not arise from the native affine source equation. The source distinguishes an
input coordinate from its accumulated response; it does not identify endpoint
evaluation with an interior forcing vector.

Therefore positive collocation remains a possible comparison theorem, not the
canonical source port geometry.

## Native response extension

Let \(u\) be the transported bulk state, \(c\) the fixed source input, and
\(r\) the accumulated response. The source equations are

\[
u'=-zu-fc,
\qquad
c'=0,
\qquad
r'=fu.
\]

On \(x=(u,c,r)^T\), the generator is

\[
M_z=
\begin{pmatrix}
-z&-f&0\\
0&0&0\\
f&0&0
\end{pmatrix}.
\]

The canonical port metric is

\[
J=
\begin{pmatrix}
1&0&0\\
0&0&1\\
0&1&0
\end{pmatrix}.
\]

Direct multiplication gives

\[
M_z^*J+JM_z
=
-2\operatorname{Re}(z)
\begin{pmatrix}
1&0&0\\
0&0&0\\
0&0&0
\end{pmatrix}.
\]

Thus the response extension is exactly \(J\)-conservative on the seam and has
a signed off-seam balance.

## Integrated Green law

Writing \(z=a+it\),

\[
\frac{d}{dq}
\left(
|u|^2+2\operatorname{Re}(c\overline r)
\right)
=
-2a|u|^2.
\]

Across a two-ended history,

\[
2a\int|u|^2\,dq
=
-2\operatorname{Re}
\left(
c\,\overline{r(+\infty)-r(-\infty)}
\right)
-
\left[
|u|^2
\right]_{-\infty}^{+\infty},
\]

with the endpoint term retained according to the declared tail boundary
condition.

This is the exact source Green identity sought by the port programme. The
forcing and response are adjoint through the hyperbolic evaluation pairing on

\[
U\oplus U^*,
\]

not through a fitted positive bulk metric.

## Determinant neutrality

The response coordinate is accumulated from \(u\) and does not feed back into
the bulk equation. At finite cutoff the extension is triangular in the
response direction. Its complementary diagonal block is the identity, or the
declared nonzero transport unit after normalization.

Therefore adjoining \(r\) does not change the scalar Schur divisor. It records
the missing Green flux without inventing a new two-way determinant correction.

This explains the earlier lift trilemma: the response lift is intentionally
one-way and determinant-neutral. Its purpose is conservation provenance, not
a new positive feedback mechanism.

## What a scalar zero supplies

A scalar Schur zero supplies a nonzero closed-loop pair \((u,c)\). The response
equation then constructs \(r\) uniquely up to its initial boundary value.

But scalar nullity does not force

\[
r(+\infty)-r(-\infty)=0.
\]

The two-atom hostile is exactly a scalar zero with nonzero response increment.
Hence the native Green identity still permits off-seam kernel states unless
global sewing terminates the hyperbolic response port.

## Boundary relation required

The completed source must provide a relation

\[
\Lambda_{\mathrm{src}}
\subset
(U\oplus U^*)_{-\infty}
\oplus
(U\oplus U^*)_{+\infty}
\]

that is maximal isotropic for the hyperbolic port form and compatible with
reciprocal sewing.

On the distinguished zero domain it must imply

\[
\operatorname{Re}
\left(
c\,\overline{r(+\infty)-r(-\infty)}
\right)
=0.
\]

Then the integrated identity gives

\[
a\int|u|^2=0.
\]

For a nonzero bulk kernel state, this forces \(a=0\).

## Positivity location

The complete metric remains indefinite on the input--response pair. Positivity
is needed only on the bulk energy

\[
\int|u|^2.
\]

Trying to make the whole port metric positive changes the canonical
input--response typing and may suppress legitimate boundary controls.

The RH mechanism is therefore a port-Hamiltonian or Krein boundary theorem:

- positive horizontal mass in the bulk;
- hyperbolic conservation at the external port;
- maximal isotropic global sewing;
- no residual response increment on a closed zero-state.

## Fourier and endpoint typing

The constant--delta wall and wall--jump Hadamard frame remain external
boundary ports. They can be included in the global isotropic relation without
being promoted to bulk states.

The primitive, square, and connected currents supply additional components of
the response coordinate in their distributional, Hilbert, and
determinant-class modalities. Their totalization must occur inside
\(\Lambda_{\mathrm{src}}\), not before it.

## Exact frontier

The source-authorized adjoint repair is now constructed locally. What remains
is one global boundary law:

\[
\text{completed reciprocal--archimedean sewing}
\Longrightarrow
\Lambda_{\mathrm{src}}\text{ is maximal isotropic and terminates the response
increment on the scalar-zero domain}.
\]

This must be derived from the full adelic boundary packet. Imposing it as a
boundary condition after locating the zeros would be circular.

## Hostiles

1. Replace the hyperbolic port metric by an arbitrary positive collocating
   metric.
2. Drop the response coordinate and infer flux zero from scalar nullity.
3. Feed \(r\) back into \(u\) merely to create a positive closed loop.
4. Ignore the endpoint \(|u|^2\) term in the integrated Green law.
5. Declare the response increment zero without constructing global sewing.
6. Scalarize primitive and square response strata before forming the boundary
   relation.

## Verdict

The native source does supply an exact port-adjoint structure: the forcing
input and accumulated response form a hyperbolic pair, and their extension is
determinant-neutral.

The remaining RH-bearing theorem is global maximal-isotropic sewing of that
response pair. If it closes the response increment on a scalar-kernel state,
the positive bulk mass forces the centered real part to vanish.
