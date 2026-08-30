# The source scalar boundary cone is exact, but its endpoint readout is not the adjoint input port

## Exact closed-loop cone

The doubled terminal-tail source already supplies

\[
A_z=
\begin{pmatrix}
\partial_q+z&0\\
0&\partial_q-z
\end{pmatrix},
\qquad
Bc=(fc,fc),
\]

\[
C(g_+,g_-)=g_+(0)+g_-(0),
\qquad
D=0.
\]

Form the block operator

\[
\mathcal D_{\mathrm{sc}}(z)
=
\begin{pmatrix}
A_z&B\\
C&D
\end{pmatrix}.
\]

Where \(A_z\) is invertible, its boundary Schur complement is

\[
S_\partial(z)
=
D-CA_z^{-1}B.
\]

The existing source calculation identifies \(S_\partial(z)\), up to the
audited nonvanishing line factor and separately typed archimedean channel,
with the completed bilateral theta scalar.

Thus the reciprocal scalar boundary cone exists. A scalar zero produces a
formal kernel state:

\[
c\ne0,
\qquad
\psi=-A_z^{-1}Bc,
\qquad
\mathcal D_{\mathrm{sc}}(z)
\binom{\psi}{c}=0.
\]

This closes scalar provenance and the algebraic zero-to-kernel implication.

## Adjoint-port test

Give the doubled bulk the source Hilbert metric. The adjoint input port is

\[
B^*(g_+,g_-)
=
\langle f,g_+\rangle+\langle f,g_-\rangle.
\]

The actual output port is endpoint evaluation:

\[
C(g_+,g_-)=g_+(0)+g_-(0).
\]

These are different functionals on the bulk graph domain.

Choose a smooth compactly supported \(g\) away from \(q=0\) with

\[
\langle f,g\rangle\ne0.
\]

Then

\[
C(g,0)=0,
\qquad
B^*(g,0)\ne0.
\]

Hence

\[
R_{\mathrm{port}}
=
C-B^*
\ne0.
\]

The scalar cone is not a selfadjoint one-port extension of the bulk operator
in the unaugmented source metric.

## Consequence for Green flux

The Schur kernel state supplied by a scalar zero need not satisfy a maximal
isotropic Green boundary condition. Algebraic kernel membership therefore
does not yet imply vanishing oriented flux.

This is the exact gap between:

\[
\Xi(z)=0
\Longrightarrow
\ker\mathcal D_{\mathrm{sc}}(z)\ne0
\]

and

\[
\ker\mathcal D_{\mathrm{sc}}(z)\ne0
\Longrightarrow
\mathfrak F_\partial=0.
\]

The first implication is available at scalar rank one. The second fails
without port closure.

## Why changing the bulk metric is not free

One could seek a positive metric \(G\) satisfying

\[
C=B^*G.
\]

But endpoint evaluation is distributional relative to the plain bulk Hilbert
metric, whereas \(B^*G\) is an interior pairing. Any such \(G\) must include
the complete graph boundary topology and its external wall--jump port.

Choosing \(G\) after imposing \(C=B^*G\) would fit the desired conservation
law. The metric must instead be derived from the full Green identity and shown
uniformly equivalent to the declared source graph topology.

## Boundary-packet repair

The complete port space must retain at least:

- endpoint value and jump;
- primitive distributional current;
- square Hilbert current;
- connected determinant-three tail;
- archimedean line;
- reciprocal variance.

Let

\[
\widetilde B:\mathcal U\to\mathcal K,
\qquad
\widetilde C:\mathcal K\to\mathcal U
\]

be the source incidences of this packet. The required closure law is

\[
\widetilde C=\widetilde B^\sharp,
\]

where \(\sharp\) is the adjoint in the complete polarized Green metrics, not
the plain \(L^2\) adjoint.

If this holds, the corresponding boundary relation is conservative on the
seam and dissipative with the centered sign off seam.

## Determinant constraint

A higher-rank repair cannot merely append observers. For

\[
\widetilde S=
\begin{pmatrix}
x&b\\
c&E
\end{pmatrix},
\]

one has

\[
\det\widetilde S
=
\det E\,
\det(x-bE^{-1}c).
\]

Therefore a two-way port repair changes the effective scalar boundary
coordinate. The blocks \(b,c,E\) and the compensating direct term must all
come from source operations, and \(\det E\) must be nonvanishing in the
claimed region.

A decoupled or triangular lift preserves the scalar determinant but cannot
repair the missing two-way flux law.

## Exact next theorem

The earliest missing identity is no longer construction of a scalar boundary
cone. It is the complete port-adjoint theorem:

\[
\widetilde C
=
\widetilde B^\sharp
\]

together with

\[
\det_{\mathrm{rel}}\widetilde S_\partial(z)
=
u(z)\Xi(z),
\qquad
u(z)\ne0.
\]

These two equations must hold for the same lifted packet. The first supplies
Green conservation; the second supplies divisor fidelity.

## Hostiles

1. Use endpoint evaluation as though it were \(B^*\) in plain \(L^2\).
2. Add a positive boundary observer only on the output side.
3. Repair adjointness by fitting a metric from \(C\).
4. Preserve determinant by forcing one coupling block to vanish.
5. Match the scalar determinant while allowing a vanishing complementary
   factor.
6. Infer flux zero from the existing scalar Schur kernel.

## Verdict

The source-derived scalar reciprocal boundary cone and its Schur determinant
are already exact. The obstruction is sharper: endpoint evaluation is not the
adjoint of bulk forcing, so the scalar kernel state is not yet a conservative
Green state.

The next RH-bearing constructor is the determinant-preserving complete
boundary packet that converts endpoint readout into the polarized adjoint of
source incidence.
