# 1028 — The Loaded Corner Matrix Is a Boundary Differential

## Retyping forced by the loaded paths

Entries 1023--1027 reject treating Entry 967's matrix \(C\) as a map from six
corner cohomology classes into hexagon vertex cocycles. Entry 966 supplies the
missing native typing.

The six source occurrences are loaded paths:

- four local host paths;
- two ordered pivot-transition paths.

Their loaded boundaries are exactly the six columns of \(C\). The two
nonlocal columns use the bar identity

\[
M_AM_B-1=(M_A-1)+M_A(M_B-1),
\]

so their intermediate pivot endpoints cancel before projection to the dense
chamber frame.

Therefore the source-defined object is the two-term complex

\[
\boxed{
\mathcal P_{\rm load}:
\quad
R^6_{\rm paths}\xrightarrow{C}R^6_{\rm chambers}.
}
\]

Here \(C\) is a differential, not a degree-zero comparison map.

## Generic and supported behavior

Entry 967 proves

\[
\det C
=
\pm f_1f_2^2f_3f_4^2.
\]

Over the Laurent polynomial domain, \(C\) is injective. Hence

\[
H_1(\mathcal P_{\rm load})=0,
\qquad
H_0(\mathcal P_{\rm load})=\operatorname{coker}C.
\]

After inverting the four Fitting factors the complex is acyclic. Its
remaining coefficient object is supported exactly on

\[
\operatorname{Fitt}_0(\operatorname{coker}C)
=
(f_1f_2^2f_3f_4^2).
\]

Thus the determinant calculated in Entry 967 is naturally the Fitting
support of a relative loaded-path complex. It is not the determinant of a
map between two rank-six cohomology groups.

## Resolution of the cocycle obstruction

Entries 1024 and 1025 found

\[
\operatorname{rank}(\delta C)=5.
\]

That is no longer a defect: boundaries of loaded paths are not required to
be vertex cocycles of a second, independently imposed hexagon cochain
differential. The previous obstruction arose from assigning \(C\) the wrong
variance.

Likewise, Entry 1027's split cone is unnecessary. It tried to force path
boundaries to become cocycles after forgetting their degree-one generators.

## Narrow conclusion

\[
\boxed{
\text{the six-point corner object is a supported loaded-path cokernel,
not six global rank-one hexagon classes.}
}
\]

This is a coefficient object on the existing chamber/incidence carrier. It
adds no carrier cell and directly explains why the complex is generically
exact but acquires support on the composite source walls.

The result does not yet identify this cokernel with the frozen dense-to-block
source module. That requires a chain map between two presentations, not a
comparison of their determinants.

## Next falsifier

Construct the dense-to-block source module as a two-term presentation

\[
R^6\xrightarrow{P_{\rm src}}R^6
\]

in the same occurrence ordering. Seek unimodular or Laurent-unit chain
gauges \(U_1,U_0\) satisfying

\[
U_0C=P_{\rm src}U_1.
\]

Compare presentation modules, Fitting filtrations, and first normal grades.
Equal determinants are insufficient. Failure of this presentation
equivalence would localize the remaining obstruction inside the coefficient
object without changing the carrier.

## Durable evidence

- packet:
  'research/benincasa/string-six-point-loaded-boundary-complex.json';
- allocator claim:
  'seqclaim-71b329d619a86ec178d9cecf'.
- epistemic event:
  'ev-000000000647-81d820e4-a978-41dc-b61c-548fb7c031d8'.
