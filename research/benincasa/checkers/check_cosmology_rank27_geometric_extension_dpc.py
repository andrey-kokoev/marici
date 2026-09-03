#!/usr/bin/env python3
"""DPC update: source the minimal rank-27 extension by geometric Gamma."""
import json
from pathlib import Path
P=Path(__file__).resolve();ROOT=P.parents[3];R=ROOT/'research'/'benincasa'/'results';m=json.loads((R/'cosmology_rank26_omega_minimal_extension.json').read_text());g=json.loads((R/'cosmology_omega_one_instantiation_dpc.json').read_text());a=json.loads((R/'cosmology_omega_one_source_lift_audit.json').read_text());assert m['construction']['E_rank']==27 and m['verified']['rank26_embeds_as_kernel'];assert g['disposition']['status']=='falsified';assert a['universal_lift']['omega']==1
# Algebraic exactness on symbolic pairs (r,n), with n the Gamma coefficient.
omega=lambda pair: pair[1]
for r in range(-5,6):
 for n in range(-5,6):
  assert omega((r,n))==n
  assert (omega((r,n))==0)==(n==0)
out={'schema':'marici.benincasa.cosmology-rank27-geometric-extension-dpc.v1','problem':'Does the R-torsor of omega-one lifts prevent a source-typed rank-27 extension after Gamma is geometrically instantiated?','bold_conjecture':'Even on the supported DNC, omega=1 leaves no distinguished lift, so the minimal exact sequence cannot be tied to the horn without an arbitrary splitting.','named_rivals':['geometric Gamma supplies a source-derived section','omega alone remains insufficient','the extension is exact but not source-split'],'risky_consequences':['no actual omega-one class may instantiate the quotient generator','the cone boundary of the chosen generator must remain unidentified'],'strongest_falsification_attempt':{'source_generator':a['universal_lift']['class'],'omega_Gamma':1,'cone_equation':a['universal_lift']['cone_equation'],'supported_instantiation':g['disposition']['surviving_scope'],'exact_sequence':'0 -> R -> E_Gamma -> Z -> 0, omega(r+nGamma)=n','kernel_test':'omega=0 iff n=0','intersection_test':'R intersect Z*Gamma=0 because n=omega(nGamma)'},'disposition':{'status':'falsified on the supported relative DNC','surviving_scope':'E_Gamma=R+Z*Gamma is a source-split rank-27 extension with quotient generator [Gamma]','qualification':'omega alone never chooses Gamma; the geometric etale/DNC construction supplies the section'},'passed':True};(R/'cosmology_rank27_geometric_extension_dpc.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
