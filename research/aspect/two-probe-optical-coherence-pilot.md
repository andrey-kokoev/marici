# Two-probe optical coherence pilot

Exploratory Aspect-local pilot requested by the operator. No owner net or physical claim is promoted.

## Recovered sources

- `research/strominger/native-path-sector-calculus-v1.md`: actual native logical matrices a,b with ab=-ba; corrected route equality ab=-ba retains distinct words. The raw encoded identity is N, not I8.
- `research/strominger/joint-field-assembly-sewing-v1.md`: fixed 14-packet, 18-interface assembly with x_h=U_h z, 44 root coordinates, five-dimensional prepared embedding B0, and R_h U_h=Pi_h R0.
- Strominger reply event `ev-000000016291-30a1a355-9b0e-4fae-bf69-ed76572fed3f`: distinguish fixed-complex section recovery from unknown-complex selection.

## First ideal optical dictionary

Use two coherent arms carrying the same logical input psi. Let A=ab, B=ba and Z=-I. A balanced splitter and recombiner give output transfer matrices (A+B)/2 and (A-B)/2. Applying Z to the second arm replaces B by -B=A. Thus the corrected difference port is dark for every input, and the sum port carries full input power. Without correction, the ports exchange roles. Phase means relative arm phase here, not an isolated observable global phase.

Blocking the second arm yields one quarter of input power at each output, with the other half lost. Both arms absent also yield a dark difference port. Equal but wrong transforms in both arms likewise pass the agreement test. Monitor input/total output and validate individual transfers; darkness alone is not coherence certification. A single probe only checks equality on its state, not on every state. Use a spanning family for an operator claim.

`python research/aspect/checkers/check_two_route_optical_comparison.py` passes nine exact checks using the existing source matrices and Gaussian-rational arithmetic. This new check imports the source matrices but does not replay the inherited provenance/hash gates or the full native calculus suite. No actual optical device or noise tolerance is established. It tests an algebraic observation dictionary, not geometric higher fillers.

## Crucial two-probe rank boundary in the assembled fixture

The source equation R_h U_h=Pi_h R0 means two native five-coefficient readouts, pulled back to the root, see the SAME five-dimensional content, merely permuted. Their combined rank is five, not ten. Consistent readings leave a 39-dimensional kernel on the full 44-dimensional root. They cannot uniquely select that unrestricted field.

On the explicitly prepared subspace z=B0 c, a complete native readout recovers c (R0 B0=I). A second readout checks compatibility, rather than supplying independent missing coordinates. Scalar intensity readings need not recover even that prepared state.

These are deductions from the documented readout equations, not a fresh replay of the assembly checker. To obtain independent constraints on the unrestricted field requires different probe operators. Even unique state recovery on a fixed complex does not identify an unknown complex or its history.

## Next bounded experiment

Recover live fixture/readout matrices; declare the actual preparation subspace and two probe operators; compute combined rank, solution family and all 18 interface residuals. Include unchanged-connectivity controls replacing PN by identity, freezing bindings, and swapping dependent occurrences. Preserve both histories and all five prepared coefficients. Only then specify a physical optical/circuit plant and its dynamics, stability, loss and observation tolerances. Variable-complex discovery requires variable attachment mechanisms beyond this fixed-network pilot.
