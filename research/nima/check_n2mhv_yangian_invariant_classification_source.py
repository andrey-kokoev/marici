#!/usr/bin/env python3
"""Source-integrity census of the N2MHV Yangian-invariant classification table."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex';text=p.read_text(encoding='utf-8')
start=text.index(r'\begin{table}[t*]\vspace{-1.5cm}\caption{The complete classification of N$^2$MHV Yangian-invariant functions')
end=text.index(r'The configuration in \mbox{Table \ref{g2n_yangian_invariants}}',start)
block=text[start:end]
# Every classified row is written as a product whose second factor begins after an explicit \times.
product_rows=len(re.findall(r'\\times\s*\\left\[',block))
config_rows=len(re.findall(r'\$\}\}\$\}\}\}\}\\end\{array\}&',block))
# Robust independent landmarks: 14 canonical alpha_8 matrices terminate in the rightmost nonzero alpha_8.
alpha8_rows=len(re.findall(r'\\alpha_\{8\}',block))
checks={'declared_fourteen_classes':'precisely 14 cyclically-distinct Yangian-invariant functions' in text[start-1500:start],'fourteen_product_representatives':product_rows==14,'fourteen_canonical_coordinate_rows':alpha8_rows==14,'unique_starred_four_mass_class':'unique N$^2$MHV function which admits more than one solution' in text[end:end+1500],'quadratic_prefactor_psi_present':r'\psi\,' in block,'nonquadratic_prefactor_phi_present':r'\varphi' in block}
out={'schema':'marici.nima.n2mhv-yangian-invariant-classification-source.v1','source':str(p.relative_to(ROOT)),'table':'g2n_yangian_invariants','product_representatives':product_rows,'canonical_coordinate_rows':alpha8_rows,'checks':checks,'passed':all(checks.values()),'scope':'Source-integrity census of the 14 cyclic classes and unique starred four-mass branch; formulas are not all independently evaluated.'}
q=ROOT/'research/nima/results/n2mhv-yangian-invariant-classification-source.json';q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
