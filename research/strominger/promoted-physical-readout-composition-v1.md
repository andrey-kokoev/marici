# Declared adapters composed with native physical readouts

## Constructed interface

The composition now has one explicit data path:

    analytic preparation -> retained records -> promotion 1 -> promotion 2
      -> retained triangle/chart -> recovered coefficients -> native readout history.

The native readout is parameterized by weights extracted from the recovered promoted data. It does not consume a parallel copy of the original coefficients or a precomputed final answer.

## Fresh formal theorem

`PromotedPhysicalReadoutComposition.agda` takes two declared adapter stages and their recovery witnesses, a preparation map, and the coefficient-algebra interface. It constructs actual native histories using `PhysicalDomainNativeReadouts` at the recovered record and proves that reflection, noise, inflow current and Berry contraction equal their original-source formulas after both promotions.

It also proves preservation of arbitrary supplied analytic readouts through recovery. This is preservation of an analytic interface, not native derivation of differentiation, integration or a physical constitutive law.

Adapter recovery laws are explicit hypotheses of this formal composition theorem. The existing Python incoming-family implementation is exercised independently below; no formal equivalence between Python execution and Agda is asserted.

## End-to-end executable controls

`check_promoted_native_readout_pipeline.py` executes the actual incoming-family adapter, the existing cone and chart, and standalone triangle recovery. It then constructs a finite interpreter of the native amplitude schema from recovered labelled factors and operator tokens. Its algebraic schema matches the formally proved readout recipes; it is not extracted Agda code.

For both existing endpoint policies:

- oscillator response/noise agree symbolically with the supplied source formulas;
- corrupting the bath coefficient inside the final promoted record changes the native-schema tree and its result, showing that a saved original source is not masking the mutation;
- the two inflow mirror states yield equal current but distinct retained factor histories;
- the three-line Berry contraction is exactly (1+i)/4 and agrees with independent matrix multiplication.

## Disposition

The bounded adapter-to-native-readout composition requested by the net is constructed and checked at both stated evidence levels: a fresh formal interface theorem and exact execution controls on the actual adapters. Do not restate this composition as a missing generic bridge.

The remaining governing issue is coverage of physical-domain source contracts, not whether these declared interfaces compose. None of this identifies the supplied analytic laws as native twelve-rule deductions or turns the three examples into exhaustive coverage.

Verification:

- `pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module PromotedPhysicalReadoutComposition -Fresh`: exit zero; execution `structured_command_execution:e_42200_1792523291522967700_52`; receipt `research/nima/results/agda-PromotedPhysicalReadoutComposition.json`.
- `uv run --with sympy python research/strominger/checkers/check_promoted_native_readout_pipeline.py`: exit zero; execution `structured_command_execution:e_42200_1792523339613128300_53`; receipt `research/strominger/results/promoted-native-readout-pipeline/verification.json`.
