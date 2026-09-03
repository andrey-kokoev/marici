"""Static contract audit: the old interval moments cannot accept a != 2 log 2 coherently."""
from pathlib import Path
import json,re
src=Path(__file__).with_name('preconditioned_spline_weil.py').read_text()
body=src[src.index('def integral_shift'):src.index('\ndef arch',src.index('def integral_shift'))]
findings={
 'boundary_uses_a': 's=scale(F(m),a)' in body,
 'exponential_hardcodes_base_two': 'F(2)**(-q*m)' in body,
 'comment_assumes_a_equals_2log2': 'exp(c*m*a)=2^((4n+d)m)' in body,
}
assert all(findings.values())
print(json.dumps({'schema':'marici.nima.scale-covariant-kernel-no-go.v1','status':'passed','findings':findings,'bold_conjecture':'passing a_c=log 2 to the old integral_shift implements scale-covariant preconditioning','disposition':'falsified','residual':'a changes support boundaries while exponential endpoint factors remain specialized to a=2 log 2; the resulting intervals do not enclose a single coherent integral','invalid_execution':'structured_command_execution:e_11792_1788312348687035200_18'},sort_keys=True))
