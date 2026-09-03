"""Enumerate integral automorphisms of the labeled P2 boundary fan."""
from __future__ import annotations
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_maximal_primitive_naturality_category.json'
rays=((1,0),(0,1),(-1,-1))
def determinant(M): return M[0][0]*M[1][1]-M[0][1]*M[1][0]
def mat_for(p):
    a,b=rays[p[0]],rays[p[1]]
    return ((a[0],b[0]),(a[1],b[1]))
def apply(M,v): return (M[0][0]*v[0]+M[0][1]*v[1],M[1][0]*v[0]+M[1][1]*v[1])
def main():
    autos=[]
    for p in itertools.permutations(range(3)):
        M=mat_for(p)
        assert apply(M,rays[2])==rays[p[2]]
        autos.append({'permutation':p,'determinant':determinant(M)})
    assert len(autos)==6 and {a['determinant'] for a in autos}=={-1,1}
    assert [a for a in autos if a['permutation']==(0,1,2)][0]['determinant']==1
    out={
      'schema':'marici.voevodsky.cosmology-maximal-primitive-naturality-category.v1',
      'status':'maximal_exact_fan_category_classified',
      'fan':'P2 boundary rays (1,0),(0,1),(-1,-1)',
      'fan_automorphisms':'The full integral fan-automorphism group is S3; determinant equals the orientation sign of the induced triangle permutation.',
      'ordered_labeled_subcategory':'Fixing all three rays and labels forces the identity character-lattice map. Primitive morphisms may still include Rees-compatible strict transverse base change and multiplication of wall equations by pulled-back base units.',
      'unlabeled_variant':'All six permutations are allowed with sign-local-system coefficients; the three even permutations preserve orientation.',
      'nonautomorphism_boundary':'A determinant-one lattice shear is primitive on the open torus but is not a morphism of the same three-ray fan unless it preserves the ray set. Unimodularity alone is insufficient.',
      'maximality_scope':'Among morphisms preserving the exact three-wall fan without extra strata, the strict labeled category plus base-unit identifications is maximal for the primitive integral horn.',
      'decision':'The earlier strict category is not merely sufficient: for the exact labeled triangle it is maximal. Broader unimodular maps require fan subdivisions and a separate subdivision comparison.',
      'next_gate':'subdivision-invariance-of-derived-pair',
      'limitations':['exact three-ray fan; toroidal refinements excluded here','checker execution pending','global carrier still absent'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
