"""Bare generation+packet cache key collides across independently edited sources."""
from hashlib import sha256
from pathlib import Path
import json
old=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
changed=old[:1]+(((1,0),2),)+old[2:]
packet=(0,1,0,0)
def H(x):return sha256(repr(x).encode()).hexdigest()
def evaluate(rows):return ((1,0),rows[1][1])
assert H(old)!=H(changed) and evaluate(old)!=evaluate(changed)
unsafe_key=lambda rows:(1,H(packet))
safe_key=lambda rows:(H(rows),1,H(packet))
assert unsafe_key(old)==unsafe_key(changed) and safe_key(old)!=safe_key(changed)
unsafe={unsafe_key(old):evaluate(old)}
assert unsafe[unsafe_key(changed)]!=evaluate(changed)
report={'passed':True,'unsafe_key':'bare generation1 + packet digest, collision','old_target':'x<=1','changed_target':'x<=2','safe_key':'complete ordered row manifest digest + generation + packet digest','safe_keys_distinct':True,'scope':'Synthetic two source branches; math cache isolation not historical execution, source trust or analytic role mapping.'}
out=Path(__file__).resolve().parents[1]/'results/cache-key-source-collision.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
