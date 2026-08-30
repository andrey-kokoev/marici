# Fourier–Tate is a Clark anti-isometry on the unitary seam and has a rank-one shear off it

## Question

What is the exact action of a scalar Fourier–Tate transition on the first
source jet and on the Clark polarization?

## Jet prolongation of the functional transition

Let a transformed scalar section have the form

\[
\widetilde F(s)=\gamma(s)F(1-s),
\]

where (gamma) is a nonzero scalar transition. Differentiation gives

\[
\widetilde F'(s)
=\gamma'(s)F(1-s)-\gamma(s)F'(1-s).
\]

Thus the induced first-jet map is

\[
A_\gamma(s)=
\begin{pmatrix}
\gamma(s)&0\\
\gamma'(s)&-\gamma(s)
\end{pmatrix}.
\]

The lower-left entry is forced by differentiating the transition. Omitting
it replaces the actual jet action by a bare reflection.

## Pullback of the Clark form

Normalize the Clark Hermitian symplectic form to

\[
H=\begin{pmatrix}0&i\\-i&0\end{pmatrix}.
\]

Writing (g=\gamma(s)) and (h=\gamma'(s)), direct multiplication gives

\[
A_\gamma^*HA_\gamma
=
-|g|^2H
-2\operatorname{Im}(\overline g h)
\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

Equivalently,

\[
A_\gamma^*HA_\gamma
=
-|\gamma|^2H
-2|\gamma|^2\operatorname{Im}
\left(\frac{\gamma'}{\gamma}\right)
\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

The first term is the expected orientation reversal. The second is a
rank-one amplitude-coordinate shear.

## Exact conformal criterion

The Fourier–Tate jet action is conformal for the Clark form if and only if

\[
\operatorname{Im}\left(\frac{\gamma'}{\gamma}\right)=0.
\]

When this holds, its multiplier is

\[
\chi(A_\gamma)=-|\gamma|^2.
\]

Scalar inversion of (gamma) does not by itself imply this derivative
condition.

## Unitary fixed seam

On the Real Fourier–Tate fixed seam, the source transition satisfies

\[
|\gamma(1/2+it)|=1.
\]

Differentiating the constant modulus along (t) gives

\[
\operatorname{Im}\left(\frac{\gamma'}{\gamma}ight)=0
\]

on that seam. Therefore

\[
A_\gamma^*HA_\gamma=-H.
\]

The full jet prolongation is an anti-isometry there, not merely the scalar
transition.

## Off-seam meaning

Away from the unitary fixed locus, the logarithmic derivative may have a
nonzero imaginary part. The jet action then fails to preserve the Clark form
up to scale by the explicit rank-one residual

\[
R_\gamma
=
-2|\gamma|^2\operatorname{Im}
\left(\frac{\gamma'}{\gamma}\right)E_{11}.
\]

This residual is a new boundary-metric component. It cannot be removed by
renaming the sheet sign. A source-derived connection, normalization, or
additional port must absorb it if off-seam Hermitian functoriality is
required.

## Arithmetic local factors

Grothendieck proved for the finite-prime transition that

\[
\gamma_p(1-\overline s)=\overline{\gamma_p(s)}^{-1}.
\]

Hence each local factor is unitary on the fixed seam and its prolonged first
jet is a Clark anti-isometry there. Cutoff products inherit the same result.

Off the seam, grade-by-grade inversion remains exact on the arithmetic line,
but it does not automatically imply vanishing of the jet shear. Arithmetic
line coherence and Hermitian jet coherence are distinct gates.

## Composition

On the seam, every Fourier–Tate transition has multiplier (-1), while two
successive reflections have multiplier (+1). Off the seam, rank-one shears
compose through the full triangular jet matrices; they cannot be represented
by multiplying scalar signs alone.

This locates the first place where the ordered lens contains strictly more
composition data than the determinant or anomaly line.

## Relation to higher arity

This is a unary and binary form-transport theorem. It does not authorize an
associator comparison. Aspect's hostile optical triads show that matched
one-particle matrices and pairwise invariants can leave a distinct Bargmann
three-cycle phase. Any ternary theta composition likewise needs its native
higher-arity invariant or a proved factorization theorem.

## Falsifier certificate

    {
      "code": "fourier_tate_jet_not_clark_conformal_off_seam",
      "transition": "gamma",
      "jet_matrix": [["gamma", 0], ["gamma_prime", "-gamma"]],
      "shear_coefficient": "-2 |gamma|^2 Im(gamma_prime/gamma)",
      "unitary_seam_shear": 0,
      "off_seam_extra_port_may_be_required": true
    }

## Disposition

The source-derived scalar Fourier–Tate transition prolongs to an exact
triangular jet action. It is a Clark anti-isometry on the unitary fixed seam
and differs from one off the seam by a single explicit rank-one shear.

## Claim boundary

This theorem assumes the scalar functional transition
(\widetilde F(s)=\gamma(s)F(1-s)) and differentiability of (gamma). It
does not prove boundedness on the completed tail space, identify a physical
adjoint incidence, control archimedean poles, or show that the off-seam shear
has the sign required by a completed Green inequality.
