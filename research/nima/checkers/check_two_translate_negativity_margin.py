"""Exact decimal-rational robustness margin for the corrected N=3 two-translate obstruction."""
from fractions import Fraction as F
import json
d=(F('0.000011790450740162717'),F('0.000011906013635010338'))
c=(F('0.004366227496'),F('0.004366339865'))
coherent=(d[0]+c[0],d[1]+c[1])
disagreement=(d[0]-c[1],d[1]-c[0])
margin=c[0]/d[1]
assert coherent[0]>0 and disagreement[1]<0 and margin>F(300)
inflated=(F(100)*d[0]-c[1],F(100)*d[1]-c[0])
assert inflated[1]<0
print(json.dumps({'schema':'marici.nima.two-translate-negativity-margin.v2','status':'passed','correction':'N=1 generalized-tail result retracted; these are corrected N=3 intervals','coherent_interval':[str(x) for x in coherent],'disagreement_interval':[str(x) for x in disagreement],'cross_to_diagonal_lower_ratio':str(margin),'ratio_exceeds_300':True,'disagreement_negative_after_100x_diagonal_inflation':True,'bold_conjecture':'the corrected negative determinant is removable by modest baseline correction','disposition':'falsified','residual_conjecture':'the corrected N=3 obstruction is the disagreement packet g-tau_delta g; independent reproduction must use N=3'},sort_keys=True))
