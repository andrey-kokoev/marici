# Mellin affine-filler descent theorem

## Question

Does the ordinary Mellin affine filler descend naturally through Stokes basis mutation and Euler-cutoff completion?

## Claim boundary

The answer is a conditional source-typed morphism theorem. Basis descent is at relative-class and period level. Completion is orbitwise under supplied weighted decay. No selected thimble-chain or global spectral theorem follows.

## Theorem

Assume:

1. the ordinary Mellin domain admits all affine simplices;
2. Stokes mutation preserves the endpoint-determined relative class and acts covariantly on period vectors;
3. cutoff labels are filtered by adelic height;
4. the adelic scale lens \(\ell(r)=\log H(r)\) is admitted;
5. source coefficients satisfy \(\sum_r|c_r|H(r)^\epsilon<\infty\);
6. the reciprocal affine orbit has \(|\operatorname{Re}w|<\epsilon\).

Then the ordinary affine filler descends through the adelic cutoff system to a uniformly convergent filler on that orbit. The construction is natural under cutoff inclusions, reciprocal action, affine boundary, and Stokes basis mutation at relative-class level. Boundary-null relations are preserved by completion.

## Dependency chain

The checker composes five independently checked objects:

- ordinary affine saturation, with \(H_1=0\);
- Stokes relative-class interchange;
- adelic labelled-chain transitions;
- finite Mellin-evaluation naturality;
- weighted reciprocal-orbit completion.

## Excluded promotions

Period covariance does not select a thimble-chain representative. Orbitwise convergence does not imply global spectral convergence. The source-decay hypothesis is not established unconditionally.

## Disposition

The original descent question is answered affirmatively at its source-typed conditional strength. Its strict-chain and global/unconditional strengthenings remain unsupported rather than blockers to the stated theorem.

## Verification

- `research/voevodsky/mellin-affine-filler-descent-theorem-v1.json`
- `research/voevodsky/checkers/check_mellin_affine_filler_descent_theorem.py`
- `research/voevodsky/results/mellin_affine_filler_descent_theorem.json`
