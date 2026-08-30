# The octahedral pure/mixed splitting separates reflection from the defect

Date: 2026-08-23

Write the primitive oriented boundary of the conductor cross-polytope as

\[
F_{\partial}=F_{\rm pure}+F_{\rm mixed},
\]

where \(F_{\rm pure}\) contains the all-positive and all-negative faces and
\(F_{\rm mixed}\) contains the other six sign faces. Coefficients are the
orientation products \(s_0s_1s_2\).

Exact cellular evaluation gives

\[
dF_{\rm mixed}=-dF_{\rm pure}.
\]

Both sides are supported on exactly

\[
\{0,2\},\{2,4\},\{4,0\}
\sqcup
\{1,3\},\{3,5\},\{5,1\},
\]

with unit coefficients and no cross-sheet residue. These are the six
literal short-facet edges.

Thus the octahedral carrier separates the two jobs canonically:

- the two pure faces fill the source-versus-literal reflection mismatch;
- the six mixed faces form a relative carrier whose boundary is exactly the
  six-term short-facet defect, up to the forced global orientation.

This closes Entry 251's global comparison at the integral cellular-carrier
level. It does not construct the loaded six-functor map: each mixed face
still needs its occurrence/normal/Tor/Čech Beck--Chevalley transformation,
and the primitive interior counit must be compared with the based generic
top.

Evidence:

- `research/nima/checkers/check_tate_octahedral_pure_mixed_boundary.py`.
- Entries 251, 253, 255, 257, and 258.
