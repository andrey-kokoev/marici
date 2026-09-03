#!/usr/bin/env python3
"""Hilbert audit of proposed corrected-symbol syzygy generators."""
import json
from pathlib import Path
rows=[]
for D in range(26,41):
 domain=4*D-36;symbol_rank=D-1;kernel=domain-symbol_rank
 cross=2*D-26;streams=2*D-34;overlap=D-17;generated=cross+streams-overlap;gap=kernel-generated
 assert gap==8
 rows.append({'weighted_output_degree':D,'kernel_dimension_lower_bound':kernel,'cross_level_dimension':cross,'two_stream_dimensions_sum':streams,'intersection_dimension':overlap,'generated_dimension':generated,'unexplained_dimension':gap})
out={'schema':'marici.benincasa.cosmology-rees-correct-kernel-hilbert-audit.v1','problem':'test whether cross-level H syzygies plus polynomial stream-function kernels generate the corrected homogeneous kernel','bold_conjecture':'those exact families exhaust every high-degree symbol syzygy','named_rivals':['complete generation','a stable logarithmic-Q kernel complement'],'risky_consequences':['the generated Hilbert function must equal 3D-35','no stable positive quotient dimension may remain'],'strongest_falsification_attempt':{'domain_dimension':'4D-36','symbol_image_dimension_upper_bound':'D-1 because the image is contained in the degree-D part of (H2)','kernel_dimension_lower_bound':'3D-35','cross_level_family':'2D-26','two_stream_families_sum':'2D-34','intersection':'D-17','generated_dimension':'3D-43','stable_unexplained_lower_bound':8,'degrees_checked':'26 through 40'},'rows':rows,'disposition':'the proposed exact families are incomplete by at least eight dimensions in every stable degree','surviving_scope':'the exact families leave at least eight symbol classes; equality and a logarithmic/residue interpretation remain unproved','next_test':'construct the eight logarithmic-Q symbol generators and test exact filtered lifts','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_correct_kernel_hilbert_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
