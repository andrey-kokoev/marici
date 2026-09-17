#!/usr/bin/env python3
"""Audit the overlap span against the pull-push transfer axioms found in PDF sources."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=json.loads((R/'relative-pair-gysin-gate-certificate.json').read_text())
t=json.loads((R/'overlap-coefficient-type-gate-certificate.json').read_text())
assert p['common_open_locally_closed_in_both']
assert not p['common_open_closed_in_U12'] and not p['common_open_closed_in_U23']
assert not p['proper_gysin_correspondence']
assert p['canonical_six_functor_bang_span']
assert not t['canonical_full_sector_transition']
out={'schema':'marici.benincasa.PS1M8-transfer-structure-admissibility.v1','prospective_action':'PS1M8_admit_overlap_span_as_transfer','resolution':'-+','source_locators':{'transfer_axioms':'1212-3563v1:p133-135','base_change':'1212-3563v1:p134','universal_span_theory':'1212-3563v1:p135','proper_base_change':'dag1:p312-315'},'required_shape':'contravariant pullback along an admitted smooth class followed by covariant pushforward along an admitted proper/transfer class, stable under Cartesian base change','actual_shape':{'common_open_locally_closed':True,'closed_in_sector_12':False,'closed_in_sector_23':False,'proper_pushforward_leg':False,'bang_extension_available':True},'verdict':'The common-open span is not admissible as the required Gysin/transfer correspondence because neither sector leg supplies the proper covariant map. Base change can prove compatibility only after admissibility; it cannot manufacture the missing pushforward or reverse its variance.','consequence':'The PDF correspondence formalism does not authorize the PS1M overlap map. The executable comparison branch is exhausted on frozen data.','reopening_inputs':['new compactification/proper closure with source-controlled boundary terms','source joint-pole/excess class','new relative chain incidence'], 'passed':True}
(R/'results/PS1M8_transfer_structure_admissibility.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
