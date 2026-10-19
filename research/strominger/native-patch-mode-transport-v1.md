# A source-based PN boundary field map

## Geometry alone does not rotate the native modes into one another

For a patch mode `z=r+i sqrt(3)s`, define the scale/phase invariant

```
rho = |z.z|^2 / (z* z)^2
    = ((r.r-3 s.s)^2 + 12(r.s)^2) / (r.r+3 s.s)^2.
```

A real spatial isometry, even followed by an arbitrary nonzero complex scalar,
preserves rho. All P patches have rho=16/25. The 18 native N patches have
rho=823849/1423249 (12 patches) or 3806401/4405801 (6 patches). None matches P.

Thus a real rotation plus scalar phase cannot sew these selected patch lines.
The geometry requires a different internal complex-component transformation,
or a non-isometric geometric deformation.

## Exact complex patch transport

Use each patch's derived orthonormal plane axes and normalize its native
cyclic mode to a two-component vector. For normalized source v and target w,

```
F(z) = [[z0, -conjugate(z1)], [z1, conjugate(z0)]]
U    = F(w) F(v)*.
```

Exact radical arithmetic verifies U*U=I, det(U)=1, Uv=w and transport of the
rank-one projectors for all 18 native target patches. No numerical square
roots or fitted phases are used. The chosen corner phases and intrinsic axis
conventions remain explicit inputs. SU(2) here describes internal two-component
linear algebra, not an independently derived physical spin interaction.

## Incoming face: geometry also fixes unequal patch weights

The N-reader attachment identifies three actual belt patches with the shared
incoming face `buv`. P's normalized face mode distributes norm equally across
these three patches. The native N conditional face mode has probabilities

```
(1193/4485, 2099/4485, 1193/4485),
```

not (1/3,1/3,1/3). Therefore three independent patch unitaries are insufficient:
they cannot change patch norms.

An additional real rotation mixes the symmetric outer-patch amplitude and the
middle-patch amplitude, fixing the antisymmetric outer combination. Its angle
is computed directly from the source and target normalized weight vectors.
This is a stated minimal-mixing extension convention, not a physical law
selected uniquely by the coefficients.

Combining that rotation with the local U maps gives an explicit 6-by-6 unitary
for the incoming face. It exactly maps the normalized P face mode to the
normalized native N face mode and intertwines their rank-one face projectors.
The receipt retains every matrix entry in exact multiradical arithmetic.

## What has and has not been sewn

There is now a concrete mode-compatible transport on all **six tangential
components** of the shared face, using native mode geometry and native relative
weights. It is more than an arbitrary embedding of five coefficients.

A full P face has nine ambient components. Restricting to tangential components
loses three normal directions on general inputs, although all selected local
cyclic modes are tangential. Extending this face map to all 36 amplitudes must
route those normal directions and the other patches, preserve the global
weights, and check both L/G operators—not merely the conditional face return.
NE and the observed whole-path five-cycle are not yet reproduced by these
partial boundary maps.

The field connection is therefore still partial. Production/viewer unchanged.

```sh
python research/strominger/checkers/check_native_patch_mode_transport.py
```

Evidence: `results/native-patch-mode-transport/verification.json`.
