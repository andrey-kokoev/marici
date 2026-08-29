# Self-adjoint finite-rank homogenization forces the reverse arrow

## Algebraic theorem

Let \(H\) be a Hilbert space, let \(A=A^*\) on a declared domain, and let
\(F:\mathbf C^m\to H\) be a bounded finite-rank source coupling.  Every
self-adjoint block realization on \(H\oplus\mathbf C^m\) has the form

\[
T=
\begin{pmatrix}
A&F\\
F^*&D
\end{pmatrix},
\qquad
D=D^*.
\]

An eigenstate \((\psi,c)\) at spectral value \(\lambda\) must satisfy both

\[
(A-\lambda)\psi+Fc=0
\]

and

\[
F^*\psi+(D-\lambda)c=0.
\]

The first equation is the homogenized source equation.  The second is the
adjoint reverse arrow.  It is not optional: deleting it makes the block
operator non-self-adjoint unless the coupling itself vanishes.

## Consequence for the doubled tail

The maximal-isotropic cancellation boundary can make the oppositely oriented
Dirac principal part self-adjoint while preserving interference.  This solves
the boundary-form obstruction for the differential carrier.

It does not solve the source-channel obstruction.  If the constant source
channel is added as an interior Hilbert degree of freedom with bounded
coupling, its adjoint equation is forced.  The known tail witness shows that a
naive reverse condition can reject a genuine Evans zero-state.

Therefore a valid spectralization must do one of the following:

1. derive the reverse equation from reciprocal theta/Tate source structure;
2. choose a source-authorized auxiliary block \(D\) for which the reverse
   equation is exactly satisfied by every zero-state;
3. realize the source channel as a boundary relation rather than an interior
   bounded block;
4. add a larger neutral or quotient architecture and prove explicitly that
   the reverse residual cancels without changing the Evans divisor.

Option 2 cannot be fitted at observed zeros.  One fixed \(D\) must work across
the whole spectral family and be derived before zero inspection.

## Reduced determinant gate

For finite-dimensional blocks, eliminating the auxiliary channel produces the
Schur complement

\[
A-\lambda-F(D-\lambda)^{-1}F^*.
\]

This generally differs from the original triangular source equation.  Its
determinant can acquire auxiliary poles, hidden modes, or a singular-value
divisor.  The spectralization claim therefore needs a reduced determinant or
boundary incidence theorem showing equality with the framed Evans section up
to a source-fixed nowhere-zero factor.

Self-adjointness alone does not supply that theorem.

## Finite falsifier

Take

\[
A=0,
\qquad
F=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
D=0.
\]

The one-way triangular matrix

\[
T_\triangle=
\begin{pmatrix}
0&0&1\\
0&0&0\\
0&0&0
\end{pmatrix}
\]

contains the source arrow but is not self-adjoint.  Completing it to a
self-adjoint matrix necessarily inserts the transpose entry in the final row,
and the eigenproblem gains the reverse scalar equation.

Any proposed bounded self-adjoint block with a nonzero forward source arrow
and no reverse arrow is disproved by this three-dimensional witness.

## Frontier

The next finite calculation is the exact bordered operator for the doubled
tail with its constant channel.  It must report the auxiliary metric, block
\(D\), reverse equation, maximal-isotropic boundary domain, and reduced Evans
determinant.  An unnamed self-adjoint completion is insufficient.

