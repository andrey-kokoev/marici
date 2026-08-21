# The QED cut supplies its own cross-angle spin connection

The experimental tomography obstruction does not reappear in the theoretical
Cutkosky construction. Let \(A_L^r\) and \(A_R^r\) be the two tree amplitudes
meeting an on-shell intermediate \(e^+e^-\) state, with \(r\) denoting its
spin fiber. The cut contains

\[
K_{LR}=\sum_r A_L^r(A_R^r)^*.
\]

Under a momentum-dependent unitary change of intermediate spin frame,

\[
A_L\mapsto A_LU,\qquad A_R\mapsto A_RU,
\]

the pairing is unchanged. Equivalently, covariant spin completeness replaces
the shared intermediate-state sum by Dirac numerators such as
\(\sum_ru_r(k)\bar u_r(k)=\slashed{k}+m\). No spinor phase or basis survives.

If the two sides were transformed independently, the pairing would change.
Thus the equality of their spin fibers is exactly the comparison datum that
was missing from independent experimental angular bins. In the source theory
it is provided by cut gluing, not chosen afterward.

This establishes the typing of the nonforward connection:

\[
\boxed{
\text{common on-shell cut fiber}
\longrightarrow
\text{canonical cross-angle pairing}.
}
\]

The remaining work is analytic rather than categorical: construct the explicit
fixed-\(t\) phase-space discontinuities, determine the required subtractions,
and evaluate the moments that yield \(f_2,f_3,h_3\).

Reproduce the finite spin-frame audit with
`research/nima/check_cutkosky_spin_frame_connection.py`.

Relevant amplitude-level source: Bernicot, *Light-by-light scattering
amplitudes from generalized unitarity in massive QED*,
https://arxiv.org/abs/0804.0749.
