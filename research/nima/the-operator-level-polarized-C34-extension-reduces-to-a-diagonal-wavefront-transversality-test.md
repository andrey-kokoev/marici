# The operator-level polarized C34 extension reduces to a diagonal wavefront transversality test

## Question

What replaces trace class at the pre-readout level for one regular and one
principal-value observer?

## Rigged kernel formulation

Use a nuclear rigging

\[
\mathcal S\subset H\subset\mathcal S'.
\]

Let `K_D(s,t)` be the distribution kernel of

\[
D_T=Q^T-Q^0.
\]

For a rapid observer `h` and pole observer `g`, the polarized composite has
formal kernel

\[
K_{h,g}(s,t)
=
\overline{m_h(s)}K_D(s,t)m_g(t).
\]

Its distributional trace exists precisely when the pullback of this kernel to
the diagonal is defined. A sufficient microlocal condition is

\[
\operatorname{WF}(K_{h,g})
\cap N^*\Delta=\varnothing,
\]

where

\[
N^*\Delta=
\{(t,t;\xi,-\xi):\xi\ne0\}.
\]

Under this condition, diagonal pullback followed by pairing with the constant
density gives the ordered principal-value/residue readout. It agrees with the
ordinary operator trace whenever the composite is trace class.

## Why existing Schatten control is insufficient

The theorem

\[
D\rho(h)\in\mathcal S_2
\]

for regular `h` controls an `L^2` kernel class after localization. An `L^2`
class has no canonical diagonal restriction. Therefore Hilbert--Schmidt
control alone neither proves nor refutes the microlocal trace needed for a pole
observer.

If the diagonal singularities of `Q^T` and `Q^0` cancel so that `K_D` is smooth
near the physical diagonal, the wavefront condition holds for the one-pole
polarization. If a residual conormal diagonal singularity remains, multiplying
by the pole can violate the pullback criterion and no canonical operator-level
extension follows.

## Finite falsifier

For any proposed local kernel formula, compute its leading singular term near
`s=t` and `t=t0`. A nonzero component with covector pair `(xi,-xi)` at the
intersection rejects diagonal pullback. Exact cancellation of that component,
with bounds on the remainder, passes the local transversality gate.

## Disposition

The rigged correspondence is not blocked by an abstract need for a new
operator ideal. Its first concrete gate is the wavefront set of the relative
Tate kernel `Q^T-Q^0` at the physical diagonal. No current packet supplies that
kernel-level cancellation theorem.