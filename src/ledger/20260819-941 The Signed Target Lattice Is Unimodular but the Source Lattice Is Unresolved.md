# 941 — The Signed Target Lattice Is Unimodular but the Source Lattice Is Unresolved

## Question

Entry 940 proves rational rank twelve.  Does its branch construction also
produce a source-normalized integral lattice?

The target and source factors must be tested separately.

## Target calculation

In the fixed labelled target basis, the diagonal and off-diagonal branch
columns are

\[
B_+=
\begin{pmatrix}1&0\\-1&1\end{pmatrix},
\qquad
B_-=
\begin{pmatrix}1&0\\1&1\end{pmatrix}
\]

on the (X=+1) and (X=-1) sheets respectively.  Both have determinant one.
Moreover,

\[
B_-=B_+
\begin{pmatrix}1&0\\2&1\end{pmatrix},
\qquad
\det
\begin{pmatrix}1&0\\2&1\end{pmatrix}=1.
\]

Thus the target branch lattice is source-derived, integral, and unimodular;
the sheet change is an integral shear.

## Remaining obstruction

The six source coordinates are labelled, but the six branch generators carry
nonunit Laurent functions of the kinematic variables.  Rational independence
therefore does not prove saturation over the source Laurent ring.  Clearing
their denominators would choose a lattice after seeing the answer and is not
admissible.

Consequently the established statement is

\[
\boxed{
L_{\rm target}\simeq\mathbb Z^2
\text{ canonically, while }
L_{\rm source}^{\rm branch}
\subseteq L_{\rm source}
\text{ has unknown saturation index.}
}
\]

In particular, Entry 940 does not yet establish an integral Betti lattice for
the rank-twelve coefficient object.

## Next falsifier

Form the source-derived (6\times6) generator matrix over the frozen Laurent
coefficient ring.  Compute its determinantal/Fitting ideal and Smith data
after localization only at predeclared source units.  Unit ideal proves
saturation; a nonunit factor identifies the exact supported lattice defect.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_signed_lattice.rs`;
- packet:
  `research/benincasa/string-six-point-signed-lattice.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_signed_lattice`;
- allocator claim:
  `seqclaim-b063b8053cc32e894de174d9`.
- epistemic event:
  `ev-000000000558-81e6588b-fb96-40ec-a95e-d495f86db30a`.
