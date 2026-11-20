"""Resolve frame and generator from two flag equations using a closed formula for a single-generator matching; no quotient or matching enumeration."""
I=set(range(6));names=('12','13','14','23','24','34');entry=frozenset(map(frozenset,((0,1),(2,4),(3,5))));exit=frozenset(map(frozenset,((0,5),(1,4),(2,3))))
def partition(hub,chart,a,d):
 back={v:k for k,v in chart.items()};block=lambda *xs:frozenset(back[x%5] for x in xs)
 if hub in d:
  x,=[chart[v] for v in d if v!=hub];return frozenset((d,block(x+a,x+3*a),block(x+2*a,x+4*a)))
 x,y=[chart[v] for v in d]
 if (y-x)%5 in (a,-a%5):
  if (y-x)%5!=a:x,y=y,x
  z=(x+2*a)%5
 else:z=(3*(x+y))%5
 zlabel=back[z];remainder=I-set(d)-{hub,zlabel};return frozenset((d,frozenset((hub,zlabel)),frozenset(remainder)))
hits=[]
for hub in (2,3):
 for sign in (1,-1):
  chart={5-hub:0,0:1,1:4,5:2*sign%5,4:-2*sign%5};a,=[a for a in range(1,5) if partition(hub,chart,a,frozenset((0,1)))==entry];ok=partition(hub,chart,a,frozenset((1,4)))==exit;print('hub',names[hub],'relative sign',sign,'entry fixes generator',a,'opposite-row exit passes',ok)
  if ok:hits.append((hub,sign,a))
assert hits==[(2,-1,3)]
