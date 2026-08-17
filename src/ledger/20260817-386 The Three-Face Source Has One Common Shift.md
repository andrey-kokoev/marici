# The Three-Face Source Has One Common Shift

## Result

The source-grading uncertainty left in Entry 385 is smaller than stated.
The three terms of the pre-quotient boundary

\[
d(H_{\rm Morse}p-\widetilde\xi h_3)
=q_Jp-d\widetilde\xi\,h_3
\]

do not carry three independently missing occurrence shifts. They
necessarily have one common multidegree.

Indeed, the established homogeneous identities are

\[
dH_{\rm Morse}=q_J-x_3\widetilde\xi,
\qquad
dh_3=x_3p.
\]

Writing \(\tau=\deg(\widetilde\xi)\) and
\(\rho=\deg(p)\), they force

\[
\deg(q_J)=\deg(H_{\rm Morse})=\epsilon_3+\tau,
\qquad
\deg(h_3)=\epsilon_3+\rho.
\]

Therefore

\[
\boxed{
\deg(H_{\rm Morse}p)
=\deg(q_Jp)
=\deg(d\widetilde\xi\,h_3)
=\epsilon_3+\tau+\rho.
}
\]

The same statement holds for
\(H_{\rm Morse}p-\widetilde\xi h_3\). Thus the degree-zero endpoint
question is controlled by one source degree \(\sigma\), not three.

## Reduction of the endpoint Hom

Entry 384 gives

\[
K_{\partial}:
R\langle e_2\rangle
\xrightarrow{(-x_0,x_1)}
R\langle e_3,e_4\rangle
\]

with

\[
\deg(e_2)=-\epsilon_4,\quad
\deg(e_3)=-\epsilon_0-\epsilon_4,\quad
\deg(e_4)=-\epsilon_1-\epsilon_4
\]

and \(H_0(K_\partial)\simeq(x_0,x_1)\). Taking the
degree-\(\sigma\) slice gives

\[
\boxed{
H_0(K_\partial)_\sigma
\simeq
(x_0,x_1)_{\sigma+\epsilon_0+\epsilon_1+\epsilon_4}.
}
\]

Consequently:

- the endpoint deformation group vanishes if that fine-graded ideal slice
  is empty;
- if the slice is nonempty, its monomial basis gives the complete list of
  homogeneous endpoint coefficients; and
- no independent choices of shifts for the Morse, generic, and endpoint
  terms remain.

## The one datum still absent

The generic normalization

\[
q_J\longmapsto x_3q_{03}^{Q}
\]

identifies \(\sigma=\epsilon_3+\deg(q_{03}^{Q})\).
What the current records do not state is the relative occurrence shift of
the literal Entry-143 generator \(q_{03}^{Q}\) against \(e_3,e_4\).
Entry 352 supplies the incidence module and its cohomological degree, but
does not print this fine occurrence shift. Without that one comparison,
assigning zero or nonzero to the displayed ideal slice would be an invention.

This is now the exact lookup/construction:

\[
\Delta_{Q/\partial}
=\deg(q_{03}^{Q})-\deg(e_3)
\]

in the ringed incidence module. Once \(\Delta_{Q/\partial}\) is read
from the literal generator labels, the endpoint graded Hom is decided by a
single monomial-membership test.

## Meta-level consequence

Multigrading has reduced the apparent deformation problem twice:

1. Entry 385 removed all higher-Rees perturbations of the fixed
   generic/lower coefficient.
2. The present calculation collapses three allegedly missing source shifts
   to one target-relative offset.

The remaining uncertainty is therefore not a family of algebraic
extensions. It is one omitted piece of bookkeeping in the common target
grading. The next search should inspect the literal Entry-143 generator
labels for \(q_{03}^{Q},e_3,e_4\), not build another Hom complex.

## Evidence

research/voevodsky/check_d03_common_source_shift_gate.py verifies the
source-degree identity, the homogeneous endpoint-road shifts, and the
formula for the deciding ideal slice.

## Outcome contract

~~~json
{
  "claim": "The D03 three-face source terms have one common occurrence degree. The degree-zero endpoint Hom is the single shifted slice (x0,x1)_{sigma+eps0+eps1+eps4}; only the relative fine degree of q03^Q against the endpoint-road generators remains to decide it.",
  "status": "proved_one_common_shift_target_offset_open",
  "closed": [
    "independence of the three source shifts",
    "parametric degree-zero endpoint Hom"
  ],
  "not_closed": [
    "relative occurrence shift of q03^Q versus e3,e4",
    "zero/nonzero value of the resulting ideal slice",
    "endpoint connector parity",
    "full mixed-variance realization"
  ],
  "next_experiment": "Read the fine occurrence labels of q03^Q, e3, and e4 in the literal Entry-143 ringed incidence generator table and evaluate the single ideal slice."
}
~~~
