# Pure-sector readout versus classical-mixture tomography in D(S3)

Owner: marici.Kitaev

## Bounded question

Does the three-setting normalized-monodromy family remain faithful when the
admitted state domain expands from one unknown simple sector to an arbitrary
classical mixture of the eight sectors?

No. Vertex separation and simplex tomography are different rank problems.

## Exact collisions

For the pure-label family

    (Im twist, mu_D, mu_F),

including normalization gives a 4 by 8 affine readout matrix of rank four and
kernel dimension four. Two exact convex collisions are

    1/2 A + 1/2 B  =readout  F,

and

    1/2 D + 1/2 E  =readout  2/3 C + 1/3 F.

These are ideal algebraic collisions. More samples cannot resolve them.
The three settings remain jointly faithful on the eight pure vertices; the
failure appears only after enlarging the state domain to their convex hull.

## Minimum mixture tomography

Freeze the ten real atomic settings

    Re twist, Im twist, mu_A, ..., mu_H.

To reconstruct an arbitrary probability vector on eight sectors, the
normalization row plus probe rows must have rank eight. Exhaustive enumeration
gives:

- no family with fewer than seven real settings has rank eight;
- exactly 21 seven-setting families have rank eight;
- one minimum witness is
  (mu_B,mu_C,mu_D,mu_E,mu_F,mu_G,mu_H);
- its normalization-augmented determinant is -81.

The maximum augmented rank at k settings is exactly k+1 for k=0,...,7.
Thus seven settings are both dimensionally necessary and constructively
sufficient on the frozen surface.

## Interpretation

Pure-sector identification asks which one of eight vertices was supplied.
Mixture tomography asks for seven independent probabilities. Calling both
tasks sector readout hides a four-dimensional kernel in the three-setting
instrument.

This theorem concerns classical superselection mixtures. It does not assert
that coherent superpositions of inequivalent topological charges are
operationally admissible, nor does it perform tomography inside an anyon's
internal representation space.

Carrier geometry supplies the list of sector labels and allowed reference
links. The coefficient lens supplies the convex state domain, affine effects,
rank, and tomography criterion.

## Verification

Command:

    uv run --with sympy python -u research/kitaev/checkers/check_s3_sector_mixture_tomography.py

Seven gates pass. The checker certifies both convex collisions, computes the
four-dimensional kernel, exhausts all subsets of the ten-setting surface, and
verifies the selected determinant. Fresh stdout matches the saved JSON.

## Boundary and falsifiers

The seven-setting minimum is relative to real scalar settings and an arbitrary
classical mixture domain. Multi-outcome effects, adaptive protocols, prior
sparsity, known support, or a different cost model alter the optimization.

The packet is falsified by failure of either displayed collision, rank other
than four for the three-setting affine map, a rank-eight family of at most six
settings, or failure of every seven-setting family.
