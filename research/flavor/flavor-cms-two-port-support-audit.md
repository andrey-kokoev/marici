# CMS two-port experiment-support audit: WP659

## Required experimental object

WP658 requires one common-constructor experiment containing two simultaneous
decay-width records, a background sideband, two independent efficiency
controls, a joint covariance, and a finite-width response.

## Published candidates

CMS B2G-23-009 searches for a singly produced vectorlike \(T\) decaying to a
top quark and either the Standard Model Higgs or a new neutral scalar. It uses
signal, validation, and control regions. However, the Higgs interpretation
assumes a 25% branching fraction, while the new-scalar interpretation assumes
exclusive \(T\to t\phi\). Its published output is a limit on production
cross section times branching fraction in the narrow-width approximation, not
a simultaneous two-partial-width fit.

Source:
https://cms-results.web.cern.ch/cms-results/public-results/publications/B2G-23-009/index.html

CMS B2G-22-001 combines hadronic and semileptonic searches for
\(T'\to t\phi\), includes finite-width Higgs benchmarks, and publishes a
HEPData record. It likewise reports production cross section times one decay
branching fraction rather than independently varying the two WP651 vertex
widths in one constructor frame.

Source:
https://cms-results.web.cern.ch/cms-results/public-results/publications/B2G-22-001/

## Coverage result

Both analyses establish that the exotic scalar port is experimentally
meaningful. Neither supplies:

- a simultaneous standard-plus-exotic two-width parameterization;
- two independently calibrated efficiency controls for those two widths;
- a public joint covariance typed to the two messenger-vertex magnitudes;
- a common likelihood in which production and both decay factors are
  separately identifiable.

The current experimental readout remains \(\sigma\mathcal B\). It constrains
a product and does not kill WP651's constructor factorization kernel.

## Disposition

No published candidate inspected realizes WP658's five-record instrument.
This is an experiment-support closure, not an algebraic gap. The smallest
falsifier is a published likelihood with both partial widths free in one
constructor frame and independent controls plus joint covariance.

Reproduce with: uv run python research/flavor/checkers/wp659_cms_two_port_support_audit.py

Generated result: results/wp659_cms_two_port_support_audit.json.
