#!/usr/bin/env python3
"""Complex physical residual-Gram scout on selected E2.1 contour points."""
# This evaluator is intentionally pending: it records the exact continuation formula
# required for Gate 3 without treating the real-only np.real frequency synthesis as analytic.
import json
from pathlib import Path
out={'schema':'marici.voevodsky.gate3-complex-physical-residual-E21-formula.v1','required_changes_from_real_evaluator':['use fixed topological panel order under complex L','replace support comparisons by panel incidence','remove np.real from Fourier synthesis and use transpose, not conjugate transpose','evaluate PAZ from degree32 F,B blocks and Y=Q^T D','bound quadrature uniformly on the contour'],'passed':False,'reason':'the existing physical residual checker is real-only; naively substituting complex L would silently destroy holomorphy','rh_proved':False};p=Path(__file__).parents[1]/'results'/'gate3_complex_physical_residual_E21_formula.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
