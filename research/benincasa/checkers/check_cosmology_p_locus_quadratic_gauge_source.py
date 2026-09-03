#!/usr/bin/env python3
"""DPC source-authority census for the quadratic p-locus gauge."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
prior=json.loads((R/'cosmology_p_locus_residual_rational_gauge.json').read_text());conn=json.loads((B/'bivariate_soft_gram_connection.json').read_text());assert prior['passed']
Dcompact='-4*u^4+12*u^3+u^2-12*u+4'
owned=[];typed=[]
cover_terms=('radicand','two-cover','two cover','double cover','sqrt(','square root','quadratic cover')
base_terms=('p=x+y+3z','v=2u','p-locus','p locus')
for p in B.glob('**/*'):
 if not p.is_file() or p.suffix not in ('.json','.py','.md') or p.stat().st_size>=1_000_000:continue
 if p.name in {'check_cosmology_p_locus_residual_rational_gauge.py','cosmology_p_locus_residual_rational_gauge.json','cosmology-p-locus-residual-rational-gauge.md','check_cosmology_p_locus_quadratic_gauge_source.py','cosmology_p_locus_quadratic_gauge_source.json'}:continue
 t=p.read_text(errors='ignore').lower();compact=t.replace(' ','')
 if Dcompact in compact:owned.append(str(p.relative_to(ROOT)))
 if any(x in t for x in cover_terms) and any(x.replace(' ','') in compact for x in base_terms):typed.append(str(p.relative_to(ROOT)))
assert owned==[] and typed==[]
out={'schema':'marici.benincasa.cosmology-p-locus-quadratic-gauge-source.v1','conjecture':'an existing source-authorized two-cover supplies sqrt(D) on the principal p divisor','required_square_class':'D=-4u^4+12u^3+u^2-12u+4 modulo squares in Q(u)','required_base_map':'p=0 identified with v=2u','preexisting_exact_D_artifacts':owned,'preexisting_cover_artifacts_with_typed_p_base_map':typed,'generic_discriminant_artifacts_promoted':False,'reason_generic_candidates_fail':'their variables and bases lack a declared map to the p divisor; equal cover degree does not identify square classes','connection_source_field':conn['interpretive_boundary'][0],'connection_physical_compatibility_boundary':conn['interpretive_boundary'][2],'conjecture_disposition':'falsified under the active source envelope','quadratic_gauge_source_authorized':False,'formal_minimal_enlargement':'adjoin y with y^2=D(u) on p=0','next_conjecture':'the minimal gauge cover y^2=D is a smooth genus-one curve and therefore introduces an elliptic, not rational, extension','next_falsifier':'compute squarefreeness and branch count of D, then apply the double-cover genus formula','passed':True};(R/'cosmology_p_locus_quadratic_gauge_source.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
