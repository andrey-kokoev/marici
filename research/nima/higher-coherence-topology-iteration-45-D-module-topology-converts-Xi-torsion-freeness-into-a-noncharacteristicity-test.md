# Higher-coherence topology iteration 45: D-module topology converts Xi-torsion-freeness into a noncharacteristicity test

## Candidate topology

Promote the labelled theta module, common-history target, and codiagonal to
modules over the spectral differential-operator sheaf `D_U`. Let

\[
0\to K\xrightarrow C H\to Q\to0
\]

be a strict sequence of `D_U`-modules. The spectral connection from iteration
44 is then part of the module structure rather than extra data.

## Important distinction

A coherent `O_U`-module with an everywhere regular connection is locally free
and has no divisor torsion. A coherent `D_U`-module need not be `O_U`-coherent:
it may have a submodule supported on a divisor, such as a delta module.

Therefore holonomicity alone does not remove the class

\[
[H_{\rm border}]\in Q[\tau].
\]

It gives that class a geometric interpretation as a possible
Xi-divisor-supported `D`-module sector.

## Characteristic test

Let `i:Z=V(\tau)\hookrightarrow U`. If `i` is noncharacteristic for `Q`, then
derived restriction to `Z` is exact in the relevant degree and no conormal
component of `Char(Q)` lies over `Z`. In the one-parameter setting this excludes
the divisor-supported torsion responsible for

\[
\operatorname{Tor}_1^O(Q,O_Z).
\]

Thus a strict noncharacteristic codiagonal would imply

\[
[H_{\rm border}]=0,
\]

and hence produce the desired labelled lift.

Conversely, a nonzero specialization class predicts a characteristic or
singular component over the Xi divisor. The topology makes this obstruction
microlocally visible rather than erasing it.

## Finite-cutoff test

At every finite prime/grade cutoff, construct the differential presentation of
`C_X` and its cokernel `Q_X`. Compute the principal symbols and test whether the
conormal covector `d tau` belongs to `Char(Q_X)` over a Xi zero.

A positive result must be uniform in the cutoff. Noncharacteristicity at every
finite stage does not by itself pass to the Köthe limit: characteristic
components may accumulate when strictness or a uniform symbol estimate fails.

## Relation to seam support

Kashiwara equivalence canonically describes modules already known to be
supported on a seam or divisor. It does not prove that a generic reciprocal
comparison is supported there. Polynomial reciprocal hostiles remain
holonomic while possessing off-seam zeros.

Similarly, identifying a Xi-supported cokernel sector would record the torsion
class, not establish confinement to the critical seam `Re(z)=0`. The Xi divisor
and critical seam are distinct loci.

## Analytic requirements

The infinite labelled carrier is naturally a nuclear Fréchet or ind/pro
`D`-module, not an ordinary coherent finite-rank module. To use the standard
noncharacteristic theorem one needs either:

1. a finite coherent `D`-module presentation capturing the source-generated
   residual sector; or
2. a uniform strict noncharacteristic estimate stable under the projective
   Köthe limit.

Neither is currently available.

## Verdict for topology 45

`D`-module topology sharpens the promising connection route into a concrete
microlocal gate: prove the Xi divisor noncharacteristic for the strict
codiagonal cokernel. Holonomicity and crystal structure alone are insufficient,
because divisor-supported delta sectors are allowed.

The next nonredundant topology to test is microlocal/analytic-wavefront topology,
asking whether positivity and reciprocal propagation exclude the conormal
component that would carry the Xi-torsion class.