# RB1 cycle 2 — ground/frame and source-assembly boundary audit

Fresh source inspection locates native matrix sampling, FFT projection and numerical Arnoldi/Ritz frame construction in `Internal`. The binary raw matrix certificate does not enclose exact native geometry samples, the FFT/kinetic assembly from those samples or intended strain/metric coefficients. The stored frame's ground label is based on rounded eigenvalues and a numerical grouping tolerance.

The checker independently ball-encloses H_bin v-e0_bin v and ||v|| for both saved ground-labelled columns, using the full block-tridiagonal raw binary H. For a Hermitian matrix, dist(e0_bin,spectrum(H_bin))<=||residual||/||v||. This is a rigorous eigenvalue-proximity certificate for that binary matrix, not a source ground-energy certificate.

Even zero residual does not establish a ground label: diag(-1,0,10) has a perfect eigenpair at 0 which is not lowest. The exact hostile control prevents silently promoting proximity into ground identity. The two nearby-eigenvalue statements need not even identify distinct eigenvalues without an additional orthogonality/coverage argument. Neither gives a retained-420 spectral-projector certificate.

The remaining source/frame obligations are explicit: enclosed native samples and assembly, complete low-spectrum coverage/ground identification, frame Gram control and spectral-subspace transfer. The full-band coupled outgoing matching inverse remains a separate requirement. No conditional packet-gap candidate is relabelled certified under these missing premises.

RB1 ends **inconclusively for full H7** after its two cycles. It retains exact pose transfer and binary eigenpair proximity as narrower certified progress. Final forecast 0.00/0.01/0.99 is historical; H7 stays open. Any further source/frame or coupled-inverse work requires an explicitly costed successor, not automatic renewal or replay of completed subgates.

Replay in the source environment with python-flint:

    python research/scattering/high-energy/check_ground_frame_bridge.py --check
