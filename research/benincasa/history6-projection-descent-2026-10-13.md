# History6 endpoint/boundary iteration 3 — incidence/projection descent screen

Freshly read the spinor transport owner, endpoint checker/receipt and current work-net (pins v29). Reconstructed cyclic dual coordinates directly from the lines (Z_{j-1},Z_j) under Z_j=(lambda_j,x_j^T epsilon lambda_j). All original lambdas and dual x match exactly at three fixtures. Reconstructed adjacent x differences factor as lambda_j*tilde_lambda_j^T and total momentum vanishes.

Change the spinor projection on the same abstract four-dimensional twistor configuration by P=[I|B], keeping Q=[0|I]. Equivalently use coordinates GZ with G=[[I,B],[0,I]], determinant one. All 70 four-brackets are exactly preserved; no external projective invariant has been changed. Tests use B=2I, [[1,2],[3,5]], diag(2,3), and [[0,1],[-1,0]] at each of three fixtures. All twelve changed-frame endpoint/generalized-R localizations are nonsingular, and all twelve c6 values equal their baselines:

- 20088/137611;
- 28561/186493;
- 7812/49555.

Column representative rescaling and a projection-preserving determinant-one spinor frame are additional exact positive controls. At the first fixed twistor configuration, symbolic B=rho*I gives c6(rho)=20088/137611 identically as a rational function, with derivative zero. This is stronger than agreement at two sampled rho values, but not an arbitrary-GL4 proof.

## Retained failed frame

The initial rho=1 incidence inverse fails because line (Z1,Z2) has singular lambda projection, at all three fixtures. This candidate is recorded explicitly as undefined, not zero, and is not used for a ratio comparison. Changing to rho=2 provides twelve localized regular comparison frames without erasing the singular one. Rational simplification of the constant c6(rho) does not authorize evaluation at rho=1 in the original source domain.

## Boundary implication and continuation

No projection dependence was detected. The test therefore supplies **no obstruction** to an intrinsic projective-twistor coefficient, but it does not construct one or justify a boundary extraction. In particular, it does not couple the previous independent spinor/Z product bases, identify the positive six-dimensional external data with four-dimensional spinor kinematics, or supply a boundary-supercomponent map.

Next executable step: derive c6 as a four-bracket/intersection cross ratio from the source incidence identities, prove the expression rather than infer it from numerical invariance, and then evaluate it on the actual bosonized quotient by Y. Check localization and poles at b2=b4=0 before taking a weighted residue; do not silently use the external-fixed tensor convention for a coefficient that becomes Y-dependent.

Evidence: `checkers/check_history6_projection_descent.py`, `results/history6_projection_descent.json`. All scientific verdicts remain unchanged. Successor pins v30 and structural net/SCC validation are distinct from this exact projection screen. There is a nonredundant continuation; the physical boundary extraction objective remains open.
