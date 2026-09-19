# The six middle-facet edges exist at mixed strengths but do not yet form one cone-package tetrahedron

The four labels in `[S,A,C,G]` are currently roles, not four registered objects
of one category.  Reading the existing source, resolvent, determinant, and
Green constructions gives the following edge audit.

| edge | strongest current constructor | current strength |
|---|---|---|
| `SA` | theta/source forcing into the full-line translation resolvent, with endpoint cross-entry | closed operator/rigged resolvent chart |
| `AG` | Poisson/Green boundary map and its upper/lower Hardy boundary values | closed local Green chart |
| `SC` | graded Euler--theta compilation into the completed scalar determinant line | determinant-line functor/shadow |
| `CG` | determinant cofactor covector compared with the rigged Green transpose | required mate; not constructed |
| `SG` | source forcing `B_f` and canonical rigged transpose `B_f^times` | boundary dual pair; bulk mate only locally represented |
| `AC` | relative Fredholm determinant of the analytic Schur return and sharp/conjugate transition | scalarized determinant of an operator family |

This table reveals two separate typing defects.

First, the dual pair `SA <-> CG` is asymmetric: `SA` has an independently
constructed source-to-resolvent realization, while `CG` remains exactly the
cofactor-to-Green mate problem.  Reflection therefore predicts the missing
constructor but does not supply it.

Second, the pair `SC <-> AG` is not objectwise comparable.  `SC` lands in a
one-dimensional determinant line, whereas `AG` retains a Green state complex.
Their scalar sections can agree only after determinant/readout, which is too
late to define a shared tetrahedral edge.

The two fixed edges also fail at full strength:

- `SG` carries a canonical rigged transpose on the boundary, but no global
  bidual cone-package equivalence with the required completed graph domains;
- `AC` carries Fredholm determinant conjugation, but determinant conjugation is
  merely the scalar shadow of a putative adjoint equivalence of cones.

Consequently no one of the four triangular faces `SAC`, `SAG`, `SCG`, and
`ACG` is yet a literal triangle in a common cone-package category, even though
several scalar or local-operator triangles commute.

The minimal repair is not to add more scalar identities.  It is to choose
concrete flagged cone-package objects `X_S,X_A,X_C,X_G`, lift `SC` and `AC`
from determinant shadows, and construct `CG` independently.  The edge audit
makes `CG` the unique wholly absent edge, while `SC`, `SG`, and `AC` are
strength-deficient edges.
