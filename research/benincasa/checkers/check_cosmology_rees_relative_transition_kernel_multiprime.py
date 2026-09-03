#!/usr/bin/env python3
"""Multi-prime stability audit for the A4-to-A5 global quotient transition."""
import contextlib,io,json,runpy
from pathlib import Path
P=Path(__file__).resolve();src=P.with_name('check_cosmology_rees_relative_transition_kernel.py')
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(src))
certs=[g['transition'](4,5,p) for p in (101,103,107)];pairs={(x['kernel_dim'],x['cokernel_dim'],x['image_rank']) for x in certs};stable=len(pairs)==1;k,c,r=next(iter(pairs));out={'schema':'marici.benincasa.cosmology-rees-relative-transition-kernel-multiprime.v1','certificates':certs,'stable_across_primes':stable,'rational_rank_lower_bound':r,'rational_kernel_upper_bound':k,'rational_cokernel_upper_bound':c,'euler_difference':c-k,'exact_characteristic_zero_dimensions':None,'scope':'three finite fields; stable ranks do not supply a characteristic-zero upper bound on rank or exact kernel lift'};(P.parents[1]/'results'/'cosmology_rees_relative_transition_kernel_multiprime.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
