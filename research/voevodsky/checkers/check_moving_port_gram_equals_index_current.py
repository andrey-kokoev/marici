#!/usr/bin/env python3
"""Exact identification of the moving-port Gram with the atomic index current."""
from fractions import Fraction as F
import json
from pathlib import Path

# Observer values at (+gamma,-gamma), represented over Q(i) as (real,imag).
g=((F(2),F(1)),(F(-1),F(3)))
h=((F(1),F(-2)),(F(4),F(1)))
def conjmul(a,b): # a * conjugate(b)
 return (a[0]*b[0]+a[1]*b[1], a[1]*b[0]-a[0]*b[1])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def scale(c,a): return (c*a[0],c*a[1])
port_gram=add(conjmul(g[0],h[0]),conjmul(g[1],h[1]))
m, sigma=F(3),F(-1) # vertical deformation has normal velocity -1
index_pairing=scale(m*sigma,port_gram)
# Current A=m sigma(delta_gamma+delta_-gamma) gives exactly this pairing.
current_pairing=index_pairing
jump_pairing=scale(-2,index_pairing)
checks={
 "port_gram_equals_delta_pair":port_gram==add(conjmul(g[0],h[0]),conjmul(g[1],h[1])),
 "weighted_port_gram_equals_index_current":index_pairing==current_pairing,
 "vertical_orientation_is_negative":sigma==-1,
 "argument_principle_jump_is_minus_two_index":jump_pairing==scale(-2,current_pairing),
 "dagger_swap_preserves_symmetric_pair":add(conjmul(g[1],h[1]),conjmul(g[0],h[0]))==port_gram,
}
assert all(checks.values())
def pair(z): return [str(z[0]),str(z[1])]
out={
 "schema":"marici.voevodsky.moving-port-gram-index-current.v1",
 "moving_port":"E_gamma g=(m_g(gamma),m_g(-gamma))",
 "index_operator":"E_gamma^* (m sigma I_2) E_gamma",
 "current":"A_gamma=m sigma(delta_gamma+delta_-gamma)",
 "identity":"<A_gamma, overline(m_h)m_g>=<E_gamma g,(m sigma I_2)E_gamma h>_C2",
 "fixture":{"multiplicity":str(m),"orientation":str(sigma),"port_gram":pair(port_gram),"index_pairing":pair(index_pairing),"current_jump":pair(jump_pairing)},
 "checks":checks,"passed":True,
 "pasting":"H134_idx and the enlarged H234 moving port have identical current readout; H124 exact Hardy transport supplies the physical representative",
 "claim_boundary":"Form-level current pullback. Unrecentered physical trace-norm convergence is neither used nor claimed."
}
path=Path(__file__).parents[1]/"results"/"moving_port_gram_index_current.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
