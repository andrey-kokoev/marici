# Endpoint-sensitive short-normal cube interface

`agda/DGPyramidEndpointNormalCube.agda` records the target-side 64-grade continuation without identifying internal short normals with external Tor data.

The certificate includes support vertices, grade-indexed relative and remaining-face complexes, normal/face restriction maps, commuting reduction equations, cube-square witnesses, and the explicit mapping-fibre-to-shifted-boundary contraction boundary. It separately records the two original components, terminal full-normal contractibility, primitive positive and negative endpoint classes, their nontriviality, and their annihilation by full multiplication. Odd/even branch point types are distinct and reflection maps between them; branch loop data remain explicit.

Derived controls prove that full multiplication identifies the two formerly distinct components while separately proving that it cannot preserve either primitive endpoint normalization. Thus terminal contractibility is represented as forgetting, not selection.

`PartialMariciPacket` now requires this cube certificate and compatibility with the marked-normal certificate. `PhysicalMixedVarianceMateSpecification` now additionally requires normal-cube compatibility, external-Tor placement, endpoint-normalization compatibility, and branch-reflection transport.

A fresh aggregate build with Agda 2.8.0.1/Cubical 0.9 under `--safe --cubical --guardedness` passed without warnings. No concrete 64-vertex matrix import, external-Tor identification, parity selector, physical mate, filler, holes, postulates, or Git operation is claimed.
