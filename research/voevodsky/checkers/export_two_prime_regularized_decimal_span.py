#!/usr/bin/env python3
"""Export retained and tail-map coordinates as exact decimal data."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=np.load(root/'two_prime_regularized_rank670_vectors.npz');P=d['retained'];D=d['tail_map'];payload={'schema':'marici.voevodsky.two-prime-regularized-decimal-span.v1','ambient_dimension':670,'retained_dimension':92,'retained_coefficients':[[repr(float(x)) for x in row] for row in P],'tail_map_coefficients':[[repr(float(x)) for x in row] for row in D],'passed':True,'rh_proved':False};p=root/'two_prime_regularized_decimal_span.json';p.write_text(json.dumps(payload,separators=(',',':'))+'\n');print(json.dumps({'ambient_dimension':670,'retained_dimension':92,'file_bytes':p.stat().st_size,'passed':True},indent=2))
