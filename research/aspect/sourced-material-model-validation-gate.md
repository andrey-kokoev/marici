# Sourced material-model validation gate

## Question

Can a published optical-material dispersion model be promoted into the attachment-margin calculation with verified coefficients, units, validity band, and uncertainty?

## Claim boundary

This packet is an authority audit. It does not admit coefficients recalled from memory, infer parameter uncertainty from printed decimal precision, or claim validation against independent measurements.

## Required source object

A model is admissible only when the durable source supplies or supports:

1. bibliographic identity and stable locator;
2. exact formula and independent-variable convention;
3. units for wavelength, frequency, refractive index, phase, and path length;
4. coefficient values and the material/specimen conditions to which they apply;
5. stated validity band and excluded resonances;
6. uncertainty, covariance, residual data, or an explicit statement that these are unavailable;
7. temperature, pressure, polarization, and composition conditions where relevant.

Transport into the continuous-mode certificate then requires a recorded conversion from the source variable to the repository's frequency coordinate and outward propagation of every admitted uncertainty.

## Repository search result

A bounded repository search for `Malitson`, `Sellmeier`, and characteristic fused-silica coefficient strings returned no material source, coefficient table, or independent validation dataset. The first repository-root search encountered the Windows `NUL` device and was narrowed to `research/`; the narrowed search completed with zero matches.

The active Site exposes no external-research or network-fetch MCP binding. Under the MCP-only policy, this session therefore lacks authority to retrieve and verify a publication or independent measurement dataset. Remembered coefficient values are not evidence and are not entered into a checker.

## Nonfabrication result

Printed decimal digits do not define uncertainty intervals. In particular, treating the last displayed digit as a standard error or interval radius would fabricate metrology. If a source reports nominal coefficients without covariance or residual bounds, two result types must remain distinct:

- exact evaluation of the printed nominal formula;
- robust enclosure of the physical material response.

Only the first is available from nominal coefficients alone.

## Decomposition

The original leaf combines two authority-dependent objectives that must be separated:

1. acquire and archive a published model plus its stated domain and uncertainty information;
2. acquire an independent dataset and validate prediction residuals without fitting and testing on the same records.

After those objects exist, the derivative/pole checker from the one-pole prototype can be generalized to the sourced formula. If uncertainty is absent, the resulting certificate must remain nominal-model-only and cannot supply a robust physical margin.

## Disposition

The validation claim is not presently testable from repository evidence or admitted external capabilities. The leaf is split into source acquisition and independent-validation branches. No physical coefficient, uncertainty interval, or agreement claim is admitted in this packet.
