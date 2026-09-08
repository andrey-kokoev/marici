# Image-line resolution of the determinantal face

## Question

Can projective factor information be retained without the impossible global scalar normalization?

## Claim boundary

Let X be the affine two-by-two rank-at-most-one matrix variety over any field. Define Y inside X times P^1 by requiring both columns of W to lie in the line ell. In homogeneous coordinates [r0:r1], the equations are r0 W10-r1 W00=0 and r0 W11-r1 W01=0. This is an algebraic incidence construction, not a physical selection rule or a time-dependent process.

On r0 nonzero use ell=[1:t] and write W=[[x,y],[tx,ty]]. This chart is A^3 with coordinates t,x,y. On r1 nonzero use ell=[s:1] and W=[[su,sv],[u,v]]. On the overlap s=1/t,u=tx,v=ty. The checker verifies these identities and rejects an incorrect fiber transition. Hence Y is the total space of O(-1) plus O(-1) over P^1 and is smooth of dimension three.

The projection Y -> X is projective, because the incidence locus is closed in X times P^1. Over a nonzero rank-one matrix its image line is unique, and nonzero-column charts give a regular inverse. Over W=0 every line is allowed, so the exceptional fiber is P^1. Its normal bundle is O(-1) plus O(-1). The exceptional set has codimension two in Y; this is a small resolution, not a divisor blowup description. The checker also verifies derivative rank two along the exceptional curve, consistent with its contracted tangent direction.

## Disposition

The construction resolves the matrix singularity while retaining a line-valued factor: the tautological line L on Y and a map k^2 -> L whose composite with L -> k^2 is W. It does not pick a nonzero vector of L. Restriction of L to the exceptional P^1 is O(-1), so L is not globally trivial; a scalar frame is still unavailable. Moreover any global triangle section over Y would restrict over X minus its vertex to the section already proved impossible. Thus resolving the singularity and choosing scalar triangle factors remain different operations.

The competing construction retaining the row line instead of the image line has not been identified with Y over X. A bounded next test is their fiber product: determine its exceptional locus and whether the two choices are related by an isomorphism or a birational modification. No uniqueness of the chosen resolution or source-derived preference for an image line is asserted.
