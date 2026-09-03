# Material-dispersion source acquisition specification

## Question

What exact external evidence package is required to unblock source-derived material-dispersion validation?

## Claim boundary

This packet specifies acquisition and admission tests. It contains no material coefficient, uncertainty, validity claim, or independent measurement.

## Required primary-source capture

Acquire through an admitted external-research surface:

1. a stable bibliographic locator and publication metadata;
2. the publisher or repository artifact containing the formula;
3. page, equation, table, or machine-readable row locators;
4. the independent variable and its units;
5. every coefficient exactly as printed;
6. material composition, specimen, temperature, pressure, polarization, and preparation conditions;
7. the stated validity band and every exclusion near absorption or resonance;
8. reported uncertainty, covariance, fit residuals, or an exact quotation that these are absent.

Store source excerpts only within copyright and publication authority. A locator plus exact page/equation references is sufficient when redistribution is not authorized.

## Integrity checks

Before transcription into a checker:

- compare formula typography against coefficient-table conventions;
- distinguish squared resonance wavelengths from unsquared pole parameters;
- verify whether wavelength is vacuum, air, or medium wavelength;
- verify whether the formula returns \(n\), \(n^2\), susceptibility, or phase;
- normalize units by an explicit conversion map;
- compute poles from the printed formula and compare them with the stated validity band;
- preserve all significant digits without assigning probabilistic meaning to them.

A second reader or source rendering should confirm transcription. OCR output is provisional until checked against the rendered equation and table.

## Uncertainty disposition

The acquired source enters one of three typed cases:

1. **reported parameter uncertainty:** propagate the stated intervals or covariance under their declared confidence semantics;
2. **reported residual bound without parameter covariance:** validate nominal coefficients and propagate the residual bound, without inventing coefficient independence;
3. **nominal coefficients only:** permit exact evaluation of the printed nominal model, but prohibit robust physical enclosure.

Printed precision is not an uncertainty model.

## External capability requirement

The current Site inventory has no external-research, browser, publication, or network-fetch binding. Repository search found no local material source. Shell or direct network fallback is not authorized. Acquisition therefore requires one of:

- activation of a Site-admitted external scholarly-search and fetch surface;
- an operator-supplied publication or dataset placed in an admitted artifact location;
- a graph communication carrying a durable source artifact reference from an authorized researcher.

## Acceptance record

The acquisition result should record artifact digest, locator, access timestamp, exact extracted fields, unresolved ambiguities, and redistribution boundary. It certifies provenance of the transcription, not truth of the material model.

## Disposition

The acquisition protocol is complete, but execution is blocked by absence of a source artifact and admitted external capability. The research leaf should remain branch-locally blocked rather than filled with remembered coefficients.
