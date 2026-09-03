import itertools,json
from pathlib import Path
base=Path(__file__).parents[1];d=json.loads((base/'results'/'rh_quarter_extremal_two_label_hall_factorization.json').read_text())
pos=[(tuple(x['label']),int(x['coefficient'])) for x in d['comparable_positive_neighborhood']];neg=[(tuple(x['label']),int(x['coefficient'])) for x in d['normalized_demands']];signed=[(K,v) for K,v in pos]+[(K,-v) for K,v in neg]
U=set(range(8));complements={K:tuple(sorted(U-set(K))) for K,_ in signed};star_centers=set.intersection(*(set(v) for v in complements.values()));varying=sorted(set.union(*(set(v) for v in complements.values()))-star_centers)
zero_proper=[]
for r in range(1,len(signed)):
 for I in itertools.combinations(range(len(signed)),r):
  if sum(signed[i][1] for i in I)==0:zero_proper.append(I)
three_signed_zero=[]
for I in itertools.combinations(range(5),3):
 vals=[abs(signed[i][1]) for i in I]
 for eps in itertools.product((-1,1),repeat=3):
  if sum(e*v for e,v in zip(eps,vals))==0:three_signed_zero.append({'indices':I,'signs':eps})
# A direct quadratic Plucker relation on four varying indices requires off-diagonal pairings.
# The observed support contains only diagonal complementary products indexed by one q each.
diagonal_support=[{'A_complement':complements[K],'B_label':K} for K,_ in signed]
checks={'five_complements_form_one_star':star_centers=={1} and varying==[3,4,5,6,7],'no_proper_source_signed_cancellation':not zero_proper,'no_three_term_unit_signed_cancellation':not three_signed_zero,'strict_remainder_retained':sum(v for _,v in signed)==int(d['normalized_slack'])>0}
result={'schema':'marici.strominger.rh_quarter_extremal_plucker_remainder_test.v1','status':'passed' if all(checks.values()) else 'failed','verdict':'The extremal five-term support is not a direct Plucker or Desnanot-Jacobi identity: all A-complement labels form the star {1,q}, while the available products are only diagonal A_{1q}B_{K_q}; a quadratic Plucker relation requires off-diagonal cross-pair products absent from the Hall slack. No proper source-signed subset or three-term unit-signed combination cancels at the exact specialization.','star_center':[1],'varying_indices':varying,'diagonal_support':diagonal_support,'normalized_remainder':d['normalized_slack'],'checks':checks,'scope':'Rules out a direct identity using only the five observed source monomials. It does not rule out an enlarged identity introducing additional minors whose remainder is separately positive.'}
(base/'results'/'rh_quarter_extremal_plucker_remainder_test.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
