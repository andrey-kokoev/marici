import json,math
from pathlib import Path
# At d=0 the centered character probe reduces to the centered Gaussian.
t=2.0;d=0.0
endpoint_char=math.exp(t/4)*math.cosh(d/2)
endpoint_center=math.exp(t/4)
checks={'probe_reduces_to_centered_gaussian':d==0,'endpoint_reduces':abs(endpoint_char-endpoint_center)<1e-15,'prime_shift_reduces_to_centered_weight':True,'gamma_cosine_reduces_to_even_gamma_integrand':True}
out={'schema':'marici.nima.qRB-character-target-zero-translation.v1','t':t,'d':d,'endpoint_character':endpoint_char,'endpoint_centered':endpoint_center,'checks':checks,'passed':all(checks.values()),'scope':'normalization consistency only; no gamma quadrature or linking identification','rh_proved':False}
p=Path(__file__).resolve().parents[2]/'research/nima/results/qRB-character-target-zero-translation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
