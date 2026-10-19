# Pivot/normal covariance and physical contour — iteration 5

Freshly read pins v44, the split-divisor receipt, and the owning history6 quotient boundary word. Constructed conditional ordered-residue lifts at both added divisors and their common center; none is silently selected as a physical cycle.

## Owning corner and six conditional flags

The stored corner word is b2 then b4 with b3!=0, deletion parity-1, K0 coefficient-1 and B22 coefficient0. Both split denominators are regular there. Completing this word with b3 gives a definite conditional triple flag, but the two-deletion word does not authorize arbitrary lifts at the excluded centers.

For fixed normal order db2 wedge db3 wedge db4, all six nested radius flags have total period1. If b3 is innermost, their split periods are(0,1); if b2 or b4 is innermost, they are(1,0). Each raw source-eight-form residue also retains the actual deletion parity computed from (b1,...,b8). In particular b2,b4,b3 has raw coefficients(1,0), reproducing the completed stored corner with its signs.

After correcting these orientation factors, two of the six adjacent flag exchanges still have nonzero opposite split differences. They swap the innermost b3 with b2 or b4 and encounter the added p36 or p58 wall respectively. Other adjacent exchanges agree. Thus the issue is not orientation anticommutation: the split contour class changes, while the sum does not.

## Second exceptional center

At b3=b4=0 with b2 nonzero, rho=b3/b4 and radial-first normal order give

    K0=-drho/(1+rho), B22=-drho/[rho(1+rho)]

up to the common center current. Their residues at0,-1,infinity are (0,-1),(-1,+1),(+1,0). This is the second local incidence-current extension, with grade1-2=7-8 and unchanged fermionic degree8, not a selected physical contour.

## Triple center and projective normal fiber

For b2=r*T,b3=s*T,b4=T, the triple-normal Jacobian is T². The radial-first normal three-form has the projective two-form coefficients

    K0=(r+s+1)/[r(r+s)(s+1)],
    B22=1/[s(r+s)(s+1)],
    sum=1/(r*s).

Moving the three source normals across b1 contributes-1. The conditional direction-retaining E7 therefore has codomain an ordered external codim3 holomorphic current valued in these projective two-forms, with coefficient -A3 where A3=N/(b1*b5*b6*b7*b8*J)|center. Its grade2-3=-1 equals7-8; the same full degree8 numerator and normalization are retained. This is an explicitly localized extension, not a new physical admission.

The added lines r+s=0 and s+1=0 meet at [b2:b3:b4]=[1:-1:1], away from all canonical coordinate lines and outside positivity. In oriented normals u=r+s,v=s+1 the displayed forms have double residues(1,-1); their sum has zero residue. With the E7 source sign this is(-A3,+A3). Omitting the double extra-pole locus would lose real split data.

The earlier rank-two P1 contour theorem applies to each double center only. It must not be promoted to the P2 complement of the triple center, which can have additional two-cycle classes and kernel relations.

## Next executable continuation

Compute the resolved projective line-arrangement complement, its integral two-cycle/period lattice and the forgetful map to the canonical complement. Determine the additional lift data and relations needed to compare the two P1 centers and the extra-line intersection before proposing a source-admitted physical prescription. Do not fit a flag or extra cycle from desired cancellation.

Evidence: `checkers/check_history6_current_ordered_lifts.py`, `results/history6_current_ordered_lifts.json`. Fresh checker passes. Scientific verdicts unchanged; successor pins v45 and structural net/SCC checks are separate. Physical cycle admission, global gluing and the ordinary blowdown seven-form remain unavailable/open as previously scoped.
