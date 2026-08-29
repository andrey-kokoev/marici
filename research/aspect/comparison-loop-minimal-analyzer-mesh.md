# Minimal analyzer mesh

The earlier 54-rotation route meshes solve a stronger problem than the experiment asks: they compile a particular full 20-mode Householder unitary.

The comparison experiment needs only a unitary that prepares the normalized analyzer from the first mode. Its inverse then maps the analyzer amplitude back to the first detector port. A real normalized vector in 20 dimensions needs at most 19 adjacent two-mode rotations.

Both routes therefore compile in 19 rotations. The coherent comparison uses 38 tunable rotations total rather than 108. Under the same 0.01 aggregate rotation budget, the uniform per-element bound relaxes from approximately 9.26e-5 to 2.63e-4 radians.

This compiler preserves the requested analyzer and inverse readout. It does not claim to reproduce the arbitrary action of the earlier Householder completion on the analyzer's orthogonal complement. That complement is operationally irrelevant to the frozen single-analyzer measurement.

