# Q-support, carrier endpoint, and marked-normal interfaces

Cubical Agda additions following the full-Q, carrier-endpoint, and marked-normal certificates:

- `agda/DGPyramidQSupport.agda` now requires seven separately supplied triangle terms and their assembly into the selected Morse primitive. It also requires a three-degree reduced Q complex, projection, inclusion, both chain-map laws, `p i = 1` degreewise, homotopy components, and all three equations expressing `d h + h d + i p = 1`. The unit roof coordinate and explicit primitive remain simultaneous fields.
- `agda/DGPyramidCarrierEndpoint.agda` records two independently weighted carrier homotopies, their exact midpoint-minus-endpoint boundaries, the nonzero exceptional relative image, and the exhaustive admissibility/divisibility equivalence. `unitCollapsedSquareImpossible` derives the unit-coefficient obstruction. A separate `PhysicalConnectorBridge` is required before carrier connectors may be treated as physical.
- `agda/DGPyramidMarkedNormalQ.agda` separates unit and all-long-normal fine sectors nominally, records the closed marked top class, its nonzero short-support transgression, sign-line action, and the independently framed order-two loop data. No physical parity selector is exported.
- `agda/DGPyramidArchitecture.agda` publicly imports all three interfaces.

These are certificate boundaries: the external finite checkers must instantiate their terms and equations. They do not duplicate the large matrices, certify the Python outputs automatically, or construct e, H_C, a physical discrepancy, a physical mixed-variance mate, or an admissible filler.

A fresh aggregate check with Agda 2.8.0.1/Cubical 0.9 under `--safe --cubical --guardedness` passed without warnings. No holes, postulates, Git operations, or analytic changes.
