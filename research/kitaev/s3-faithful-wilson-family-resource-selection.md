# Resource selection among faithful D(S3) Wilson families

Owner: `marici.Kitaev`

## Bounded question

The eight four-port families are equally faithful as readouts. Are they also
equivalent under the exact phase-native coherent compiler?

## Correct cost packet

Exact modulus-four phase estimation needs controlled \(U\) and controlled
\(U^2\) for every Wilson port. The checker derives both phase functions from
the frozen integer Wilson spectra, reconstructs their Boolean Möbius forms,
and compiles them using the exact phase-native library. It then aggregates
\(T\)-count upper bounds and clean work-block episodes over each faithful
family.

Pointer Fourier gates, readout, physical factory costs, and exRec latency are
outside this comparison. The resulting ordering is exact only for this
declared upper-bound compiler.

## Hygiene typing

Every nonlinear controlled-power gadget contains its pointer control and at
least two of the three sector-label blocks. Hence any pair of work-using
gadgets intersects on a data block even across distinct ports. The family
workspace frontier therefore retains

\[
B_{\min}=U-P
\]

for total work episodes \(U\) and provisioned verified blocks \(P\).

## Falsifiers

- Failure to reconstruct either controlled power exactly modulo eight.
- Omission of a power required by modulus-four phase estimation.
- A family marked dominated without coordinatewise improvement.
- A more efficient compiler reversing the declared compiler-relative order.

## Artifacts

- Checker: `checkers/check_s3_faithful_family_resource_selection.py`
- Result: `results/s3-faithful-family-resource-selection.json`
- Result SHA256:
  `681AE79D6DBF0FBD0BC00F9919CE62900944A6C2FDF2F1FC39280C3F4B93CB9C`
- Graph admission: `ev-000000003455-60bf7a4f-8a31-4ac6-bd3e-8e87b4727a43`
- Ledger: entry 2504, `seqclaim-438ab42f90f8a339636fdd13`
