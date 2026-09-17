#!/usr/bin/env python3
"""Cache directed quadrature nodes, weights, q values, and critical transform F_w."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb,acb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb,acb
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
flint.ctx.prec=256;root=Path(__file__).parents[1]/'results';vv=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];vv[1::2]=0;v=[arb(repr(float(x))) for x in vv];L=arb('.75');pi=arb.pi();qR=(acb(arb('.25'),arb(125))).digamma().real/2-pi.log()/2;rows=[];Q=72
for panel in range(250):
 for j in range(Q):
  z,ww=arb.legendre_p_root(Q,j,weight=True);u=arb(panel)+(z+1)/2;x=L*u;Fw=arb(0)
  for n in range(0,150,2):Fw+=v[n]*2*L*((2*n+1)/(2*L)).sqrt()*((-1)**(n//2))*(pi/(2*x)).sqrt()*x.bessel_j(arb(n)+arb('.5'))
  q=(acb(arb('.25'),u/2)).digamma().real/2-pi.log()/2;rows.append([str(x),str(ww/2*(q-qR)*Fw/pi)])
out={'schema':'marici.voevodsky.L075-critical-frequency-node-cache.v1','precision_bits':flint.ctx.prec,'gauss_order':Q,'node_count':len(rows),'rows':rows};p=root/'L075_critical_frequency_node_cache.json';p.write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps({'schema':out['schema'],'node_count':len(rows),'path':str(p)}))
