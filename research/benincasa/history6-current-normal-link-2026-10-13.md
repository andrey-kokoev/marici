# Pivot/normal covariance and physical contour — iteration 3

Freshly read pins v42, contour-lattice/current/directional receipts, and the owning source canonical-coordinate/residue passage. This turn lifts direction contours from actual oriented source normal-link tori and locates the split-pole wall.

## Source forms and blowup orientation

Freeze the six base coordinates in their declared order, write x=b2,y=b3,B=b4!=0. Moving dx,dy to the front of the source eight-form has parity+1. Its split two-normal forms are

    Omega0=(B+x+y)/[x(x+y)(B+y)] dx wedge dy,
    OmegaB=B/[y(x+y)(B+y)] dx wedge dy,
    Omega0+OmegaB=dx wedge dy/(xy).

Under x=rho*T,y=T, dx wedge dy=T drho wedge dT. The radial-first residue is therefore the previously constructed pair -drho/[rho(1+rho)], -drho/(1+rho). Ordered torus angles (theta2,theta3) become (thetaT,thetaR)=(theta3,theta2-theta3), with determinant-1. Thus the ordered source torus integral is minus the radial-first direction period, not an independently fitted sign.

## Actual torus lifts and wall crossing

Choose |b2|=epsilon2, |b3|=epsilon3, both small, and epsilon3<|b4| to exclude b3+b4=0. The source orientation is (theta2,theta3) in both cases.

- epsilon2<epsilon3: |rho|<1, direction circle C0; exceptional split periods(-1,0), ordered source torus periods(1,0).
- epsilon2>epsilon3: |rho|>1, direction circle C0+Cminus1=-Cinfinity; exceptional split periods(0,-1), ordered source torus periods(0,1).

Both total source periods are1, but the split wall crossing is(-1,+1). The reverse triangle inequality |b2+b3|>=|epsilon2-epsilon3| makes each chamber torus admissible in the local split-pole complement. At equal radii the torus intersects b2+b3=0 at antipodal phases with both b2,b3 nonzero. The wall is real contour data, not a coordinate sign ambiguity; the central direction loop accounts for the difference. The source residue along that divisor is opposite and nonzero for the two splits and cancels only in their sum.

Direct two-variable iterated residues reproduce both torus integrals. Raw differential residue order b2-first gives(1,0), b3-first gives(0,-1), matching the earlier signed route table; reversing residue order must not be confused with keeping the torus orientation fixed and changing its radius hierarchy. An arbitrary quadratic holomorphic fermionic/Jacobian-prefactor jet contributes only its center value in either chamber; the same local residue argument holds for analytic prefactors.

## Source authority clarification

The freshly read source explicitly calls Gamma_sigma the **cell** at line1175 (`grassmannian_geometry_of_momentum_conservation_subsection`). Its canonical-coordinate integral and ambient top-form residue representation do not, by that symbol alone, prescribe a contour around the extra weighted split pole at this center. References in earlier checkpoint prose to an owning Gamma prescription mean a needed source-cycle identification, not evidence that Gamma already selects one of these radius chambers. No physical selection has been supplied here.

## Next executable continuation

Classify the b2+b3 divisor against the actual active-cell canonical Plucker denominators and the split decoration. Track it under source chart/pivot changes and determine its positive versus complex locus, then formulate the additional relative-cycle/contour datum required for physical admission. The two link classes are now explicit; choosing one remains distinct from their algebraic construction. No global gluing, ordinary blowdown seven-form or weighted-sector promotion follows.

Evidence: `checkers/check_history6_current_normal_link.py`, `results/history6_current_normal_link.json`. Initial conversion of a SymPy Boolean to int failed; replacing it by an explicit branch yielded a fresh passing rerun without changing formulas. Scientific verdicts unchanged; pins v43 and structural net/SCC checks are separate from the source-form/contour computation.
