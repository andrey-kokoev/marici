# The Schatten anomaly corridor between one and one half

Author: `marici.Grothendieck`

## 0. Operator stimulus and discovery

The operator proposed that:

1. the two half-planes first acquire a distinction;
2. scalar meaning or integrality is lost only afterward;
3. the observed zero seam occurs where the resulting two-plane geometry
   itself becomes undefined.

The prime operator gives an exact three-region realization of this ordering.
It also explains why the distinguished offset is `1/2` rather than `0` or
`1`.

## 1. Complete Schatten threshold law

On `ell^2(primes)` let

\[
P_s e_p=p^{-s}e_p,
\qquad \sigma=\operatorname{Re}s.
\]

For every finite `q>0`,

\[
\|P_s\|_{\mathcal S_q}^q
=\sum_p p^{-q\sigma}.
\]

Therefore

\[
\boxed{
P_s\in\mathcal S_q
\quad\Longleftrightarrow\quad
q\,\operatorname{Re}s>1.
}
\]

Two cases have direct meanings:

\[
P_s\in\mathcal S_1
\quad\Longleftrightarrow\quad
\operatorname{Re}s>1,
\]

\[
P_s\in\mathcal S_2
\quad\Longleftrightarrow\quad
\operatorname{Re}s>\frac12.
\]

The first is the Euler trace-class domain.  The second is the polarized
Hilbert--Schmidt domain.

## 2. The anomaly corridor

The strip

\[
\boxed{
\frac12<\operatorname{Re}s\le1
}
\]

has a precise operator type:

\[
P_s\in\mathcal S_2\setminus\mathcal S_1.
\]

Inside it:

1. the prime state is square-integrable;
2. pairwise products are trace class;
3. angles, quadratic energies, and the `det_2` cocycle are defined;
4. the ordinary linear trace and Euler Fredholm determinant are not defined.

Thus the two-plane Carrier already has a faithful Hilbert geometry, while
its naïve scalar all-prime readout has lost meaning.  Completion is not
creating the chamber geometry; it is repairing one unbounded scalar
observation inside geometry that still exists.

This is the exact ordered phenomenon anticipated by the operator.

## 3. Why the offset is exactly one half

The completed readout is built from two reciprocal/conjugate sheets, and its
physical comparison is quadratic:

\[
|X|^2,\qquad
F\overline F,\qquad
\operatorname{Tr}(P_sP_{\bar s}).
\]

Quadratic comparison doubles the convergence exponent:

\[
p^{-s}\overline{p^{-s}}=p^{-2\operatorname{Re}s}.
\]

The threshold is therefore

\[
2\operatorname{Re}s=1.
\]

Hence

\[
\boxed{
\operatorname{Re}s=\frac12
\text{ is the integrability boundary forced by a two-copy readout.}
}
\]

After centering by the reciprocal involution `s -> 1-s`, this boundary is
also its fixed seam.  The arithmetic and symmetry selections agree.

## 4. Three meanings of the two thresholds

\[
\begin{array}{c|c|c}
\text{region}&\text{operator type}&\text{meaning}\\
\hline
\operatorname{Re}s>1
&\mathcal S_1
&\text{Euler trace and scalar determinant exist}\\
\frac12<\operatorname{Re}s\le1
&\mathcal S_2\setminus\mathcal S_1
&\text{two-plane geometry exists; scalar trace needs completion}\\
\operatorname{Re}s=\frac12
&\partial\mathcal S_2
&\text{quadratic prime geometry degenerates}
\end{array}
\]

The line `Re(s)=1` is therefore the loss of naïve scalar meaning.  The line
`Re(s)=1/2` is the loss of the quadratic Carrier that can repair and compare
that meaning.

## 5. Completion as a trace anomaly

In the trace-class region,

\[
\zeta(s)=\det(I-P_s)^{-1}.
\]

In the anomaly corridor, only

\[
D_2(s)=\det{}_2(I-P_s)
\]

survives canonically.  It removes the undefined linear trace while retaining
every cyclic contribution of degree at least two.  The omitted channel is
recovered by the completion-selected section

\[
\mathcal T(s)
=\frac{2\pi^{s/2}\xi(s)}{s\Gamma(s/2)}D_2(s),
\]

which continues

\[
(s-1)\exp\left(\sum_p p^{-s}\right).
\]

Thus

\[
\boxed{
\text{completion is a renormalized scalar trace inside an already valid
quadratic prime geometry.}
}
\]

## 6. Zeros and loss of trivialization

The nonvanishing `det_2` factor proves that the quadratic prime geometry
itself has no interior determinant defect.  Any zero is carried by the
completion-selected anomaly section `T`.

Accordingly, RH becomes:

\[
\boxed{
\text{the repaired scalar trace never loses its determinant-line
trivialization before the quadratic Carrier reaches its own boundary.}
}
\]

Critical-line zeros are then boundary phase defects.  An off-line zero would
mean that the scalar anomaly section failed while the ambient two-plane
Hilbert geometry was still perfectly meaningful.

## 7. Why higher Schatten classes do not move the physical seam

At `Re(s)=1/2`, the operator belongs to `S_q` for every `q>2`.  Therefore the
prime sequence still supports higher-copy regularized geometry beyond the
Hilbert--Schmidt threshold.

This does not automatically move the seam.  The observed Carrier is a
two-sheet complex amplitude with a quadratic norm and phase pairing.
`S_2` is the ideal canonically attached to angles between polarizations,
Fock implementability, and determinant-line cocycles.  Higher `S_q` classes
describe higher-copy observables, not the faithful two-plane readout.

This is also a falsifier: if the physical construction actually requires a
three-copy or higher primitive comparison, then `1/2` is not selected by
Schatten integrability alone.  The two-copy typing must be derived from the
completed real/reciprocal Carrier, not chosen because it gives the desired
line.

## 8. The oval-to-circle statement

Inside the anomaly corridor the natural local metric is quadratic.  In that
metric a small constant-norm link around a determinant-section zero is a
circle:

\[
\|\tau\|_{\mathcal L}=\epsilon.
\]

Nonorthogonal source coordinates, or a plot mixing the trace-class and
Hilbert--Schmidt scales, display that circle as an oval.  Its winding is the
integral determinant-line charge.

Thus the operator's oval observation, half-plane distinction, and
integrality intuition are three views of one typed structure:

\[
\boxed{
\text{a scalar trace anomaly living inside a quadratic polarized chamber.}
}
\]

## 9. Deutsch--Popperian conjecture

\[
\boxed{
\begin{array}{l}
\textbf{Schatten anomaly localization conjecture.}\\
\text{The completed theta/Euler source canonically renormalizes the}\\
\mathcal S_1\text{ trace anomaly throughout the }\mathcal S_2\text{
chamber,}\\
\text{and the resulting determinant-line section can lose
triviality only}\\
\text{where the }\mathcal S_2\text{ Carrier itself reaches its fixed
boundary.}
\end{array}
}
\]

This explains why the zero seam is `1/2`, why the Euler formula fails earlier
at `1`, and why zeros should be phase defects rather than vanished source
states.

## 10. Remaining theorem and falsifier

The missing theorem is nonvanishing of `T` in the anomaly corridor, derived
from the completed source.  The Schatten classification alone does not
provide it: holomorphic sections of determinant lines can vanish inside a
valid `S_2` chart.

The sharp falsifier is a source-admissible completion whose anomaly section
has an interior Maslov crossing while `P_s` remains Hilbert--Schmidt.  The
hostile quartet shows this is possible for generic symmetric entire
functions; theta arithmetic must exclude it.

## 11. Scope

The Schatten threshold law, anomaly corridor, regularized determinant, and
factor isolation are exact.  The interpretation supplies a hard-to-vary
explanation and a sharply typed theorem target.  It does not prove the
anomaly localization conjecture or RH.
