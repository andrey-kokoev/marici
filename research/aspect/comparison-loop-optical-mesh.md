# Comparison-loop optical mesh

Each connected 20-mode Householder compiler is lowered to a sequence of two-mode real Givens rotations and terminal zero-or-pi phase shifts. Every rotation maps directly to a tunable two-mode beamsplitter. The two meshes occupy the two arms of the coherent path control.

The compiler emits all mode pairs, cosines, sines, terminal phases, control-arm labels, phase fixture, and reset identity. It reconstructs each route matrix from the emitted component list and rejects the mesh if the Frobenius residual exceeds 1e-10.

The preregistered acquisition plan uses six probes, X and Y control quadratures, 100000 effective trials per probe-quadrature, and 10000 bypass trials per route-probe. Total planned trials are 1320000.

The generated mesh packet is directly programmable in a generic two-mode interferometer API. Hardware-specific voltage, thermo-optic, electro-optic, or integrated-photonic calibration remains a separate binding.

