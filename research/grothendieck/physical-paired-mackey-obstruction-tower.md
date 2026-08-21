# A physical paired Mackey correspondence has an eight-stage obstruction tower

Epistemic-graph event: 1351.

## Admission tower

A source claim of physical paired Mackey transfer along a quotient `q` must
pass the following stages in order.

1. **Geometric typing.** Source and target relative complexes, boundary
   matrices, orientations, regulators, and the geometric quotient are given.
2. **Readout factorization.** The frozen coefficient selector annihilates the
   quotient kernel, or an explicitly covariant replacement observable is
   sourced.
3. **Pairing adjunction.** A coefficient--Betti pairing and degreewise
   adjoint candidate `S` are fixed; its right radical `R` is computed rather
   than presumed zero.
4. **Visible boundary compatibility.** The defect
   `Omega=D_HS-SD_G` vanishes in `C(H)/R`.
5. **Radical existence.** The remaining class `[Omega]` vanishes in
   `H^(-1)(Hom(C(G),R))`.
6. **Canonicity.** The repair torsor under `H^0(Hom(C(G),R))` is trivial or
   a physical normalization selects one point.
7. **Naturality and composition.** The symmetry class in `H^1(Gamma,A)`
   vanishes and the selected stagewise maps obey the defect Leibniz law
   without hidden cancellation or annihilation.
8. **Mackey normalization.** Pull--push gives the correct `|ker q|` norm,
   with selector normalization and coefficient arithmetic audited separately.

Passing a later algebraic-looking calculation cannot fill an earlier missing
resource.  In particular, norm identities do not construct relative
complexes, and a terminal composite does not certify its stages.

## Weaker readout branch

A single scalar paired observable has a separate, weaker exit after Stage 3:
for its frozen cocycle `ell`, it is enough that

`ell Omega_(n+1)=0`.

This certifies only `ell S` on source homology.  It does not imply a Betti
homology map, representative-independent cohomology pullback, a chain map,
or a Mackey correspondence.  Exact-representative independence additionally
requires the anomaly classes `[alpha Omega]` to vanish.

## Current five-site verdict

The algebraic finite-deck system passes formal adjunction, composition, and
the unnormalized norm calculation.  The frozen positive selector fails
nontrivial branch descent.  More fundamentally, the source-derived physical
relative complexes and boundary matrices required at Stage 1 remain absent,
so Stages 3--8 cannot be promoted to physical statements.  The formal sheet
pairing cannot decide whether the actual physical radical is zero.

## Falsifier discipline

Each stage has a local falsifier: missing typed data; a selector nonzero on a
kernel fiber; pairing mismatch; nonzero visible `Omega`; nonzero radical
class; multiple unnormalized torsor points; nonzero `H^1` naturality class or
stagewise composition defect; or incorrect norm/selector scaling.  Recording
the first failed stage prevents stronger conclusions from being inferred
from downstream formal controls.
