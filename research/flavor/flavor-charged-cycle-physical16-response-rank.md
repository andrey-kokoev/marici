# Charged-cycle physical16 response rank

## Bounded question

After lifting WP644 through the frozen three-generation messenger tensors and
quotienting legal rephasings, what is the rank of the induced response on the
faithful `physical16` coordinate?

## Tensor lift

WP492 freezes identical up/down tensor shapes:

- the same normalized cyclic entrance vector;
- componentwise connector incidence;
- the same oriented-port dot;
- identity messenger masses on the row and port labels.

WP635's cross-edges are scalar normalizations multiplying identity
intertwiners at the corresponding stages. Therefore the WP644 loop changes
only the scalar normalization of the existing neutral route. It introduces no
new generation tensor:

\[
\delta Y_u=\kappa_uY_u,
\qquad
\delta Y_d=\kappa_dY_d.
\]

The coefficients contain the finite WP644 kernel and the ratios of charged to
neutral scalar normalizations. They remain free source coordinates.

## Quotient rephasings first

Write \(\kappa_q=a_q+ib_q\). At first order,

\[
\delta Y_q=a_qY_q+ib_qY_q.
\]

The imaginary direction is a common right-handed quark rephasing and is
vertical under the full weak-basis groupoid. The physical tangent retains only
the two real dilation coordinates \(a_u,a_d\).

For a nondegenerate sheet, use logarithmic masses followed by nine CKM moduli
and signed \(J\):

\[
(\log m_u,\log m_c,\log m_t,
\log m_d,\log m_s,\log m_b,|V_{ij}|,J).
\]

The exact response Jacobian is

\[
D_{\rm loop}=
\begin{pmatrix}
1&0\\1&0\\1&0\\0&1\\0&1\\0&1\\
0&0\\\vdots&\vdots\\0&0
\end{pmatrix},
\]

with ten zero readout rows. Its rank is two. The loop changes the common up
and down mass scales, but leaves all within-sector mass ratios, CKM moduli, and
signed Jarlskog coordinate unchanged.

`physical16` is a faithful sixteen-entry embedding, not a sixteen-dimensional
manifold chart: CKM unitarity constrains its nine moduli and signed \(J\) to
four intrinsic mixing coordinates. The quark quotient has intrinsic dimension
ten. Hence rank two has intrinsic codimension eight. The number fourteen is
only the ambient sixteen-entry rank deficit and must not be called a physical
tangent dimension.

## Complete-ensemble result

The argument depends only on nondegeneracy and the frozen tensor shapes, not
on fitted numerical values. All 1,210 stored sheets are nondegenerate members
of the admitted fitted domain, so each carries the same rank-two tangent
response. There is no sheet on which the loop gains a mixing or CP direction.

This rank deficiency is not selector authority. The source coefficients
\(a_u,a_d\) are free and can move either common scale in either infinitesimal
direction. The finite operation is locally invertible on its two scale
coordinates and imposes no fixed locus or proper image on the other fourteen
coordinates.

## Classification

The charged loop is a source-derived neutral backreaction and instrument
enrichment. It is neither a texture rigidifier nor a `physical16` selector.
Its first nonfaithful arrow is the frozen tensor-shape map: all charged-loop
source variations are compressed to two physical dilation directions after
the weak-basis quotient.

The smallest exact selector falsifier is the pair \((a_u,a_d)=(\epsilon,0)\)
and \((-\epsilon,0)\), both legal and producing opposite up-scale responses
from the same flavor sheet. A progressive reopening requires source dynamics
that fixes \(a_u,a_d\) independently and introduces a non-aligned generation
tensor with a proper, ensemble-stable `physical16` image.

## Reproduction

Run:

    uv run --with sympy python research/flavor/checkers/wp645_charged_cycle_physical16_response_rank.py

The generated result is
`research/flavor/results/wp645_charged_cycle_physical16_response_rank.json`.
