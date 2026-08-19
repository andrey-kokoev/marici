# 953 — The Common Conserved Kinematic Ring Repairs the Branch-to-Dense Comparison

## Correction to Entry 951

Entry 951 required the sparse block variables (Z,Q) to be functions of the
six generators appearing explicitly in the dense momentum kernel.  That is
the wrong comparison requirement.

Entry 905 had already placed the dense and block presentations over the
common nine-dimensional conserved six-point kinematic ring and constructed

\[
\boxed{T=M_{\rm block}K_{\rm dense}.}
\]

Therefore Entry 951 is superseded.

## Source dictionary

For the labelled (s_{14}) block used by the branch calculation,

\[
X=e^{i\pi s_{23}},
\qquad
Y=e^{i\pi s_{25}},
\qquad
Z=e^{i\pi s_{35}},
\qquad
Q=e^{i\pi s_{235}},
\]

and

\[
s_{235}=s_{23}+s_{25}+s_{35}
\quad\Longrightarrow\quad
Q=XYZ.
\]

The dense kernel happens to display only

\[
(s_{12},s_{13},s_{14},s_{23},s_{24},s_{34}),
\]

whereas the block presentation also uses (s_{25},s_{35}) and its cyclic
partners.  Both are functions on the same conserved kinematic space.  No
direct map into the smaller displayed dense subring is needed.

## Typed comparison

The correct diagram is

\[
R_{\rm dense}\longrightarrow R_{\rm kin}
\longleftarrow R_{\rm block},
\]

followed by the canonical rational basis transition (T).  Entry 905 proves
that

\[
K_{\rm block}T=K_{\rm dense}
\]

and that the divisor of (T) is supported only on existing factorization
channels.

Thus

\[
\boxed{
\text{branch-to-dense comparison is typed over }R_{\rm kin};
\text{ Entry 951's obstruction is retracted.}
}
\]

## Epistemic consequence

The correction strengthens, rather than weakens, Entry 950: the six extra
global valuations can be compared through a source-derived Hecke-type basis
modification on existing channel walls.  No missing carrier or arbitrary
root choice is involved.

## Next falsifier

Pull the branch maximal-minor divisor through the explicit (s_{14})-block
component of (T), retaining the (s_{25},s_{35},s_{235}) valuations.  Test
matrix-level residue coherence, not merely equality of total divisor degree.

## Durable verification

- corrected checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_support_map_type_gate.rs`;
- corrected packet:
  `research/benincasa/string-six-point-support-map-type-gate.json`;
- transition packet:
  `research/benincasa/string-six-point-basis-transition-divisor.json`;
- allocator claim:
  `seqclaim-47e7f21dce76ae74434b7277`.
- epistemic event:
  `ev-000000000569-8de33e66-68c9-4c6b-bc50-0ba8c5f467d8`.
