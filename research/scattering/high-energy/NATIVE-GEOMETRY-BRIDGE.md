# AB1 cycle 2 — native geometry enclosure on binary centered vertices

Fresh inspection locates SVD outward normals in `geometric_normals` and the analytic strain/Pauli fold construction in `Native.matrix`. The checker replaces SVD normals by exact cofactor nullspace formulas for the saved binary centered vertices, ball-normalizes them, and verifies nonzero face volumes and strict outward orientation. This is an independent computation of the intended tangent normals, not an enclosure based on SVD's reported residual.

All 1,225 samples use exact rational strain nodes, exact angular phases and exact DC=atan(1/sqrt(5)). The checker verifies positive normalization/fold denominators and exact Pauli/edge constants, then encloses the complete native matrices. Comparison against the saved binary samples yields a maximum sample Frobenius error. The exact discrete Fourier transform is unitary, so the assembled operator perturbation is bounded by this maximum (via angle-block diagonal norm and maximum across strain slices), without multiplying by every grid point. Combined with the terminal-assembly certificate, strict perturbation transfers the inertia to this conditional native-geometry reference.

## Remaining reference boundary

The saved **binary centered vertices** remain fixed inputs. Their upstream ideal-source vertex construction and rounded centering have not been enclosed. Thus this certificate is not silently claimed for the original exact source geometry. True ground identification, retained spectral-frame transfer and full-band coupled inverse remain further gates. The native derivative dL is not used or certified here.

AB1 ends **inconclusively for full H7** after two cycles. It retains complete conditional native/terminal assembly progress, while original reference/frame/coupled-inverse obligations remain. Final 0.00/0.01/0.99 forecast is historical; active successor cost/forecast require a new explicit protocol. Neither AB1 nor predecessor budgets renew automatically.

Replay in the source environment:

    python research/scattering/high-energy/check_native_geometry_bridge.py --check
