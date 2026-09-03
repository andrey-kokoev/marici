# DPC: second-jet interface

## Problem

Does the symmetric `(x,y,z)` Hessian define a nonzero second-jet class in the existing relation quotient?

## Bold conjecture

At least one Hessian component survives the unchanged `T/S_K/Q` image and defines a second-order Bockstein candidate.

## Named rivals

All six components may remain exact; raw Hessians may exist without a second-order connecting quotient; or interpolation and polarization may fail to define a symmetric Hessian.

## Risky consequences and strongest falsification

All six symmetric components materialize. Each has 3,244 nonzero rows among 21,964 raw A12 relations. The complete unchanged source image has rank 8,793 over `F_32003`. Reduction of six components on all 1,224 seed targets gives 7,344 zero residuals and no nonzero residual.

The interface remains incomplete: no second-order extension, quotient, admissible primitive rule, or geometric comparison exists.

## Disposition

The bold conjecture is rejected as a typed Bockstein claim. The modular calculation supplies no surviving witness in the unchanged quotient, but one-prime vanishing does not prove rational exactness. The first missing typed object is a sourced second-order jet complex specifying its extension and admissible primitives.

The next discriminating test is exact rational membership for the 7,344 bounded Hessian targets. This remains an algebraic diagnostic and does not manufacture the missing second-order interface.

## Verification

- `research/voevodsky/check_cosmology_second_jet_interface_audit.py` — exit 0
- `research/voevodsky/results/cosmology_second_jet_interface_audit.json`
