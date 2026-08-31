# Global exceptional Gysin map for the corner blow-up

## Construction

Blowing up the source corner `(u,v,p)=(0,0,0)` gives exceptional divisor `E=P^2`. Its normal bundle in the blow-up is `O_E(-1)`. If `H` denotes the primitive hyperplane class, then

`i^* i_*(1)=c1(N_{E/Bl})=-H`.

Thus the global blow-up supplies a canonical degree-shifting source morphism with primitive integral coefficient, up to the sign fixed by orientation. This is stronger than the local statement `Res_E(dlog p)=1`: a single affine logarithmic chart fixes a valuation but does not construct the connecting map, whereas the exceptional self-intersection constructs the global Gysin class.

## Claim boundary

The source-side class is `+/-H`. It has not been identified with the target class `Xi_log`. Such an identification requires a chain map from the exceptional divisor complex to the logarithmic circuit/residue complex. Equal primitivity and matching scalar normalization do not create that map.

The programme total complex must also record its grading shift explicitly; the codimension-one cohomological Gysin shift and the Cech/cone shift cannot be conflated silently.

## Disposition

The Gysin-map leaf is completed on the source side. The next leaf is the comparison `H -> Xi_log`: derive it from the strict transforms of the three ordered walls and verify the total grading, residue vector, and compatibility with the exceptional face. Only that comparison can promote the source pair to the required `(1,1)` horn column.

## Verification

- `research/voevodsky/check_cosmology_corner_blowup_global_gysin_map.py`
- `research/voevodsky/results/cosmology_corner_blowup_global_gysin_map.json`
