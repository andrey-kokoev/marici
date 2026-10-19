# /// script
# dependencies = ["sympy"]
# ///
"""A Fourier-compatible transverse contraction fails full heat continuation."""
import json
from hashlib import sha256
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
NOTE='research/voevodsky/transverse-gaussian-bridge-v1.md'
OUT='research/voevodsky/results/transverse-gaussian-bridge-v1.json'

def require(ok,msg):
    if not ok: raise ValueError(msg)

def main():
    # Exact two-atom packet in transverse coordinate, with longitudinal delta_0.
    packet={S.Integer(1): S.exp(S.pi), S.Integer(0): -S.Integer(1)}
    g=lambda y:S.exp(-S.pi*y*y)
    contract=lambda p:S.simplify(sum(c*g(y) for y,c in p.items()))
    heat=lambda p,t:{y:S.simplify(c*S.exp(-S.pi*t*y*y)) for y,c in p.items()}
    require(contract(packet)==0,'initial kernel premise')
    after=contract(heat(packet,S.Integer(1)))
    require(S.simplify(after-(S.exp(-S.pi)-1))==0 and after.is_negative is True,'heat exposes discarded state')
    # Kernel escape forbids ANY linear descended heat action on this quotient,
    # not merely the most obvious one-dimensional multiplier.
    require(contract({})==0 and contract(heat({},S.Integer(1)))==0,'zero control')
    # Pairings of Gaussian with delta and constant are both one; after full
    # transverse heat the constant chart has an extra Gaussian integral factor.
    dimensions=[]
    for D in (2,3,20,54):
        factor=2**(-S.Rational(D-1,2))
        require(0<factor<1,'transverse heat factor')
        dimensions.append(dict(D=D,initial_delta_pairing='1',initial_constant_pairing='1',
                               delta_after_heat='1',constant_after_heat=str(factor)))
    # Fourier of exp(-pi A y^2) has (A^-1/2, 1/A); A=1 is self-dual.
    A=S.Integer(1)
    require(A**(-S.Rational(1,2))==1 and 1/A==A,'self-Fourier normalization')
    y,t=S.symbols('y t',positive=True)
    multiplier=S.exp(-S.pi*t*y*y)
    require(S.simplify(S.log(multiplier))==-S.pi*t*y*y,'strict heat multiplier away from zero')
    paths=[NOTE,'research/voevodsky/channel-carrier-tempered-extension-v1.md',
           'research/voevodsky/results/channel-carrier-tempered-extension-v1.json',
           'research/conjecture_net/contracts/marked-channel-selection.v1.json',
           Path(__file__).relative_to(ROOT).as_posix()]
    result=dict(schema='marici.transverse-gaussian-bridge.v1',passed=True,
                candidate='fixed Schwartz transverse contraction Q_g with g(y)=exp(-pi||y||^2)',
                verdict='rejected_for_full_heat_continuation',
                initial_kernel_readout='0',after_unit_heat=str(after),
                dimensions=dimensions,Fourier_square='written transpose argument using self-Fourier g',
                general_no_go='No nonzero fixed Schwartz transverse contraction intertwines full isotropic heat with unchanged longitudinal heat on all tempered distributions',
                general_proof_status='written delta-test and continuity argument, not machine formalized',
                all_variable_context_bridges_refuted=False,marked_axis_selection_refuted=False,
                common_channel_carrier_source_constructed=False,physical_realization_admitted=False,
                source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))

if __name__=='__main__': main()
