# Three compiled seven-point positroid cells collapse under CZ

The attempted adjacent-facet orientation check found a sharper obstruction than an orientation sign. The current `seven-point-positroid-compiler.json` assigns codimension-two source positroids to all six matched seven-point histories. Three assignments (histories 1, 3, 5) impose TWO neighboring vanishing cyclic minors. They force a parallel triple of source columns: respectively (2,3,4), (7,1,2), and (4,5,6).

For the fixed strictly positive moment-curve external matrix `Z_j=(1,j,j²,j³,j⁴,j⁵)`, `ker Z^T` is spanned by

    k=(1,-6,15,-20,15,-6,1).

If the triple columns are parallel to a vector `d`, then for every scalar `h`

    C_h=C+h*d*k^T

has the SAME `CZ`, and the triple remains parallel. Starting from an interior positive source point, sufficiently small nonzero `h` leaves every other strictly positive ordered minor positive. The checker supplies explicit rational source matrices and their distinct positive companions at `h=1/10000` for all three assignments, retaining exactly their prescribed zero minors.

Consequently these compiled source cells have at least one-dimensional fibres and cannot provide locally invertible **eight-dimensional image charts** for their alleged top-dimensional canonical forms. This conclusion is not a numerical Jacobian accident; it follows from a source kernel direction and the parallel-triple equations. At a checked shared face, history-zero's inward image Jacobian is `7200/2401` while history-one's is zero; history one's tested interior image Jacobians also vanish, as the fibre argument predicts.

**Correction of claim status:** the rank-table compilation is a combinatorially valid source positroid assignment, but the identification of all six such assignments with full-dimensional NNMHV positive-geometry history cells is FALSE for this positive external data. A complete eight-form cannot be obtained by locally pushing forward a seven-dimensional image as if it were a nondegenerate chart. The earlier rational-kinematics parity-superamplitude matching concerns different, already sourced expressions; this result does not contradict those coefficient equalities. It blocks using the naive `omitted label i => Delta_(i,i+1)=0` rule as the desired universal seven-point positive-cell compiler.

The history-zero separated-pair chart remains an eight-dimensional local chart, and its source cyclic double residue remains valid as a calculation **for that source cell**. Its identification with the history-zero canonical form still needs a same-Z form comparison; no global six-cell triangulation is now claimed.

**Next construction gate:** replace triple-parallel rank tables by eight-dimensional cells whose `CZ` map is generically finite, derived from actual on-shell diagrams or a separately certified image/form identity. Test the replacement at a positive `Z` using the fibre-kernel obstruction BEFORE matching scalar amplitudes. The eight-point classified seed matching also needs this image-rank gate independently; matched fermionic coefficients alone do not establish a positive image triangulation.

Run `uv run --with sympy python research/nima/checkers/check_seven_point_triple_fibre_obstruction.py`; packet `research/nima/results/seven-point-triple-fibre-obstruction.json`.
