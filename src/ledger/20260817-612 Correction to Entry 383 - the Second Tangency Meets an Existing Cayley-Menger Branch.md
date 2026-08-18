---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Correction to Entry 383: the Second Tangency Meets an Existing Cayley--Menger Branch

## Retraction boundary

Entry 383 used
[
(u,v)=(r^{-1},s^{-1})
]
to transport three finite conductor--energy centers away from the first tested
point. That coordinate map is false. In the (x=1) marked chart the
source-defined map is
[
oxed{
u=rac{E}{x}=rac1r,
qquad
v=rac{ell_3}{x}=rac{2r+2s-1}{r}.
}
]
The identity (v=s^{-1}) happens to hold at
((r,s)=(1,rac12)), so Entry 382 remains valid. The other three center
computations and the corresponding table in Entry 383 are retracted.

## Corrected centers

The four finite centers are
[
(1,2),quad(2,4),quadleft(rac23,0ight),quad(-1,0)
]
in ((u,v)). The same frozen weight
[
(w_{111},w_{101},w_{110};w_6,w_7,w_8,w_9)
=(1,0,0;0,0,0,0)
]
was rerun at the corrected points with the same two blowup charts, finite
field, frame, sampling bounds, and rational reconstruction.

| source center | corrected ((u,v)) | raw minima | weighted minima | bad masks | nonzero coordinates |
|---|---:|---:|---:|---:|---:|
| ((1,rac12)) | ((1,2)) | ((-2,-1)) | ((-1,0)) | ((120,120)) | 54 |
| ((rac12,1)) | ((2,4)) | ((-2,-1)) | ((-1,0)) | ((120,120)) | 54 |
| ((rac32,-1)) | ((rac23,0)) | ((-1,0)) | ((-1,0)) | ((0,0)) | 28 |
| ((-1,rac32)) | ((-1,0)) | ((-1,0)) | ((-1,0)) | ((0,0)) | 28 |

Thus the transported one-step weight still suffices for logarithmic
valuations at every corrected center.

## The residual direction at the second center

At ((u,v)=(2,4)), reconstructed denominators contain the exceptional
direction
[
ho=1
]
in addition to (ho=0). It occurs only in the tangent components from the
first and third marked rows to (e_6,e_7,e_8,e_9).

This factor is derived from the already frozen Cayley--Menger branch
coefficient. The source geometry has
[
c=-u,
qquad
y=rac{u+v-2}{2},
]
hence
[
c+y=rac{v-u-2}{2}.
]
At the center its strict transform is
[
v-u-2=t(ho-1),
]
so its exceptional point is exactly (ho=1).

No new divisor has been added after seeing the target. The failed narrower
statement was that the conductor--energy tangent direction alone generated
all denominators. The surviving statement is that the complete frozen source
support, including its Cayley--Menger branch divisor, generates them.

## Corrected verdict

Entry 383 is superseded by
[
oxed{	ext{the single marked weight }w_{111}=1	ext{ is logarithmic at all
four corrected finite tangencies.}}
]
However,
[
oxed{	ext{the second center also requires the already existing
Cayley--Menger direction }c+y=0.}
]
There is no unknown residual support factor and no new carrier datum.

## Epistemic boundary and next falsifier

This correction still concerns only the canonical seven-coordinate
generic-fiber de Rham projection. It does not test the five exact-lift-gauge
coordinates, the four elliptic modulus base points, the full discriminant
extension, or the physical relative chain.

The next test remains the four projective elliptic base points, now with the
complete frozen source support rather than a conductor-only tangent set.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`;
- `research/benincasa/corrected-all-marked-tangencies-certificate.json`;
- `research/benincasa/marici-gm/src/bin/triple_soft_exceptional_resolution.rs`;
- Entries 382--383.
