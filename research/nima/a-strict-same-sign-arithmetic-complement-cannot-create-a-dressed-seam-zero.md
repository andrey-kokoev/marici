# A strict same-sign arithmetic complement cannot create a dressed seam zero

## Seam characteristic

Let the boundary value of the three-port characteristic be

\[
M_{\theta U}
=
C^\dagger R_+C
+
\begin{pmatrix}0&0\\0&D_U\end{pmatrix},
\qquad
C=(V\;B_\Sigma).
\]

Assume the passive seam signs

\[
W:=\operatorname{Im}R_+\ge0,
\qquad
D_I:=\operatorname{Im}D_U\ge\delta I
\]

with \(\delta>0\) on the arithmetic source.

## Kernel calculation

Suppose

\[
M_{\theta U}
\binom c x=0.
\]

Taking the imaginary part of the quadratic pairing gives

\[
\left\|W^{1/2}(Vc+B_\Sigma x)\right\|^2
+
\langle x,D_Ix\rangle
=0.
\]

Both terms are nonnegative, and the second is strict. Therefore

\[
x=0
\]

and

\[
W^{1/2}Vc=0.
\]

For a nonzero kernel state, \(c\ne0\), so the bare theta direction itself must
be radiation-dark.

Substitution into the full block equation further requires

\[
V^\dagger R_+V=0,
\qquad
B_\Sigma^\dagger R_+V=0.
\]

Thus an arithmetic state does not participate in a same-sign seam kernel.

## Schur consequence

When

\[
Q_U=D_U+B_\Sigma^\dagger R_+B_\Sigma
\]

is invertible, a zero of the dressed scalar reconstructs

\[
x=-Q_U^{-1}B_\Sigma^\dagger R_+Vc.
\]

The kernel calculation forces this reconstructed vector to vanish. Hence

\[
F_\theta=0
\quad\Longrightarrow\quad
B_\Sigma^\dagger R_+V=0
\quad\text{and}\quad
V^\dagger R_+V=0.
\]

The arithmetic Schur correction cannot create a zero by cancelling a nonzero
bare theta Weyl value under the strict same-sign assumptions.

## Relation to closure of the incidence range

Although

\[
\Phi\in\overline{\operatorname{ran}B_\Sigma},
\]

approximating it requires source norm tending to infinity. The strict
\(D_I\) term charges that cost and excludes arithmetic cancellation in an
actual seam kernel. This is the energy version of the closure-range result.

## Architectural alternatives

For arithmetic dressing to create or move seam zeros, at least one assumption
must change through a source-derived constructor:

1. \(D_I\) loses strictness on a controlled arithmetic line at the intended
   divisor;
2. the history and arithmetic imaginary parts have opposite or indefinite
   signs;
3. the zero is a non-self-adjoint Evans event rather than a kernel of the
   passive boundary characteristic;
4. the arithmetic data enters the bare theta boundary relation before the
   positive decomposition;
5. a singular boundary value invalidates the ordinary quadratic-form
   argument.

## Implication for the Cayley candidate

The strict prime-delay Cayley law remains a valid zero-free complement, but it
cannot be the mechanism producing arithmetic phase-matched Xi zeros in a
same-sign passive seam pencil. Under that law, every zero must already be a
bare theta dark point satisfying the additional arithmetic orthogonality
condition.

Therefore an identity

\[
F_\theta=E_\theta\tau
\]

would not derive the Xi divisor from arithmetic feedback; it would require the
bare theta Weyl section to carry that divisor already, with arithmetic dressing
nonvanishing there.

## Disposition

Strict same-sign passivity reduces every three-port seam kernel to the bare
theta radiation-dark line and sets its arithmetic source vector to zero. The
current Cayley complement can control nondivisor directions but cannot create
the Xi zero set. G4 must either accept a theta-first Evans divisor with
arithmetic provenance only, or construct a different seam sign/degeneracy
mechanism. No RH conclusion is authorized.
