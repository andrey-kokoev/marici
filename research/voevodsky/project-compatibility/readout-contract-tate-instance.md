# First non-scalar-unit instance: the existing integral Tate bridge

## Fresh evidence

Read Nima's `rs2-the-canonical-c3-tate-bridge-exists.md` and `cross-sector-tate-naturality-closes-on-coefficients-but-not-yet-on-support.md`, plus the RS2 checker. Freshly compiled and ran `research/voevodsky/check_weighted_three_road_star.rs`; output is retained as `temp/readout-weighted-three-road-star.json`.

Its result is CONDITIONAL/INCONCLUSIVE, not a passed physical realization. Exact chain/sign checks pass, but the unlocalized Tate realization test fails because bottom homology differs. The later prose records independently proved local traces and purity, which this coefficient checker alone does not implement. The inspected package still does not supply the global supported comparison alpha_plus; this audit does not assert that no later research could supply it.

## Actual source coefficient data

The retained integral augmentation lattice is I_Z with basis a=e1-e0,b=e2-e1. The existing source matrices are

    g=[[0,-1],[1,-1]], s=[[1,0],[1,-1]],
    M=g-1=[[-1,-1],[1,-2]].

Its intended coefficient readout is

    O:I_Z -> T=I_Z/M I_Z, T=Z/3.

In these audit coordinates O(x,y)=x+y mod3. This is the source's Tate coefficient, not an arbitrary new scalar observable. The cosmological norm-homology presentation is ker(N)/im(N) in F3[C3]; the existing bridge identifies it with the same quotient. Rotation is trivial and reflection is negative on both quotient presentations.

The scalar cosmological period kills this syndrome, as the source explicitly records. A contract for that zero scalar readout is not a substitute for the nonzero supported coefficient readout being tested. Physical identification of the two sectors is not implied.

## Contract obligations at coefficient level

Take the two port readings to be the cosmological and road quotient classes. After the canonical bridge identifies their reading types,

    F(v)=(O(v),O(v)), Y=T direct_sum T,
    H(a,b)=b-a, K=ker(H).

K is the independently declared equality of the two class readings. Then im(F)=K and the intended readout is recovered by either projection. Full source recovery is unnecessary: ker(F)=M I_Z is nonzero.

The actual integral presentation supplies the exact sequence

    0 -> Z^2 --M--> Z^2 --F--> T^2 --H--> T ->0.

Indeed det(M)=3 gives injectivity; im(M)=ker(O); every diagonal class has a source representative and H is surjective. To verify the kernel explicitly, if x+y=3k, then

    M*(-x+k,-k)=(x,y).

This uses divisibility of x+y on the kernel, not inversion of3 in the coefficient ring. The quotient bridge is D3-equivariant. We do not infer a D3 chain action on this entire displayed resolution without specifying its appropriate orientation twists.

These coefficient outputs are finite and complete in their discrete topology. This does NOT establish continuity or realization of the physical supported/Rees comparison: its topology and geometric maps are additional source data.

## The actual supported obstruction survives the contract test

The weighted checker works over

    R0=Z[q0^+-1,...,q5^+-1], u_j=q_j-1,
    raw source K(u4,u0,u2),
    H0=M_support=R0/(u4,u0,u2).

This module is nonzero: evaluating all q_j at1 gives a quotient to Z. The proposed global localization that makes the incidence weights into units inverts u4,u0,u2. Inverting even ONE of these annihilators kills M_support.

Consequently the forgetful/localization comparison sends its nonzero supported class to zero. No readout preserving that class can factor through this comparison. In the contract's language, ker(F_localization) is not contained in ker(O_support). This is an obstruction on the existing source module, not the earlier n->3n toy.

Separate support-Cech localization summands are not the same operation as globally inverting the normals in R0. The checker's legal support masks must be retained.

As a contrast, completion of M_support for the ideal J=(u4,u0,u2) leaves it unchanged, because J M_support=0 and every M_support/J^n M_support equals M_support. This elementary completion statement does not identify that adic topology with the source's full filtered/Rees topology. Neither it nor discrete coefficient completeness proves the missing alpha_plus exists.

## Disposition

The four-part contract distinguishes two genuinely different outcomes:

- integral coefficient comparison: supplied, compatible and faithful to the predeclared Tate readout;
- global supported comparison: not supplied by the inspected package, and the proposed global-inversion shortcut demonstrably destroys the required class.

No normal or integer3 is inverted by this audit. It does not identify Carriers or physical observables, replace owner research, or turn a conditional coefficient checker into a geometric theorem.

Next inspect the existing local Cousin/purity maps and their overlap data: determine the precise missing global realization witness rather than re-prove coefficient matching or introduce a new Gaussian model. Keep the frozen triangle physical-admission gates parallel.

## Verification

`check_readout_contract_tate.py` reads the actual RS2 matrices without executing its output-writing code, checks both quotient presentations and their D3 action, verifies integral kernel witnesses and compatible-output exactness on finite controls, and records the fresh weighted checker's conditional status and failing support test. General module and completion statements are written arguments, not machine-formalized proofs.
