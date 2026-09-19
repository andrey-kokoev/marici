# The two-phase four-presentation packet is an eight-component tangent-valued observer, not yet an A(n,2,4) chart

## Candidate identification

For a point `Y` of `G(2,6)`,

\[
T_YG(2,6)\simeq\operatorname{Hom}(Y,\mathbb R^6/Y),
\qquad
\dim Y=2,
\qquad
\dim(\mathbb R^6/Y)=4.
\]

Choose the reciprocal sheets as a basis of `Y` and the four systems
`S,A,C,G` as a basis of the quotient. The corrected packet then has the formal
shape

\[
\Theta(b_z)=
\begin{pmatrix}
S_+(b_z)&A_+(b_z)&C_+(b_z)&G_+(b_z)\\
S_-(b_z)&A_-(b_z)&C_-(b_z)&G_-(b_z)
\end{pmatrix}.
\]

Hence `Theta(b_z)` is naturally typed as an eight-component tangent-valued
observer.

## Rank test

Eight entries do not by themselves give an eight-dimensional chart. On the
retained Xi lane the source family is parametrized locally by the complex
spectral coordinate `z`. Before additional independent source deformations are
introduced, its real tangent rank satisfies

\[
\operatorname{rank}_{\mathbb R}D\Theta\le2.
\]

Moreover reciprocal symmetry relates the two rows, and the lower sewing cells
relate the four columns. These constraints can only lower the rank. Variation
of the cutoff `n` refines a cellulation and does not add tangent dimensions to
`A_(n,2,4)`.

Therefore the present packet maps a low-dimensional spectral family into an
eight-dimensional tangent carrier; it does not provide a local chart or an
open positive cell of the amplituhedron.

## What survives

The `2 by 4` typing remains useful:

- rows record reciprocal phase;
- columns record the four-system presentation;
- minors record phase/presentation incidence;
- the rung-four residual can be sought as a distinguished minor, determinant-
  line coordinate, or canonical-form residue.

This realizes

\[
\Theta:\mathcal Z_{\Xi}\longrightarrow T\mathcal A_{n,2,4}
\]

as an observer map from the spectral locus `Z_Xi`, rather than an equivalence
of source and target geometries.

## Promotion gate

A genuine amplituhedron chart requires eight independently variable,
source-derived deformation coordinates `q_{\sigma X}` satisfying

\[
\det\left(
\frac{\partial\Theta_{\sigma X}}
     {\partial q_{\tau Y}}
\right)\ne0,
\]

plus positivity and canonical-residue compatibility. No such eight-parameter
source deformation is present in the corrected one-parameter spectral lane.

## Next bounded test

Express the known final residual

\[
\mathcal R_p(b_z)
=(1-p^{-2\operatorname{Re}z})E_p(b_z)
\]

as a `2 by 2` minor or determinant-line pairing of columns of `Theta`. If this
cannot be done from the existing column definitions, the shared `2 by 4`
signature is representational rather than boundary-generating.