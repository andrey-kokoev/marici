#!/usr/bin/env python3
"""Falsify discriminant-based repair of the kappa=1 conductor pole."""
import json
from fractions import Fraction
from pathlib import Path
# Delta_a2=64 p^4 (k-1)(k+1)(xi-1)(xi+1)
val_discriminant=1
val_sqrt=Fraction(1,2)
val_conductor=-2
assert val_conductor+val_discriminant==-1
assert val_conductor+val_sqrt==Fraction(-3,2)
out={'schema':'marici.benincasa.cosmology-discriminant-collision-cancellation-dpc.v1','problem':'Can the existing exceptional discriminant supply the missing collision vanishing and regularize the conductor map at kappa=1?','bold_conjecture':'The exceptional branch discriminant, or its square root from the source cover, provides enough kappa-minus-one valuation to cancel the conductor double pole.','named_rivals':['the discriminant has only a simple zero','its square root has half-order rather than integral order two','a distinct source degeneration is required'],'risky_consequences':['the discriminant-derived factor must have valuation at least two','the corrected coefficient must have nonnegative valuation'],'strongest_falsification_attempt':{'exceptional_discriminant':'64 p^4 (kappa-1)(kappa+1)(xi-1)(xi+1)','discriminant_valuation':1,'square_root_valuation':'1/2','conductor_valuation':-2,'valuation_after_full_discriminant':-1,'valuation_after_square_root':'-3/2'},'disposition':{'status':'falsified','residual':'neither the discriminant nor its square root regularizes the conductor coefficient','surviving_scope':'the kappa=1 degeneration requires a new source factor of additional valuation at least one beyond the full discriminant, or at least three halves beyond its square root; no such factor is materialized'},'passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_discriminant_collision_cancellation_dpc.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
