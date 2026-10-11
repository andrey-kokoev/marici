# Typed deuterium rim channels and the exact breakup test

## Port construction

The preceding two-rim trace T has scalar input and output. The electron's retained boundary-cell state is a spinor doublet, so an attachment cannot silently identify it with that scalar.

Reuse the tensor spin-lift construction already tested in `electron-pairing-coupling.md`. For the belt coefficient sector define

    T_spin=T tensor I_2,
    E_spin=E tensor I_2.

The selected carrier is now twelve-dimensional and the two rim ports together have four spin components. The exact identity T_spin E_spin=I_4 holds. The effective same-species rim energy is

    c ||s_lower-s_upper||^2,
    c=1499960093/591106225.

It is covariant under a common SU(2) spin rotation. This is a declared enlargement of the scalar belt, not a derivation of neutron spin. It constructs a compatible coefficient type while retaining both spin components and the source stiffness.

## Charge forbids the naive linear attachment

If proton and electron spinors have phase weights +1 and -1, a fixed neutral linear difference p-e is not covariant. An exact phase control demonstrates the failure.

The already constructed field-dependent phase link has weight two. With such a link D, p-D e has weight +1 and its norm is invariant. But the earlier source equations did not select that link over a frozen frame, so it remains an interaction input.

The alternative is to keep each species in its own charged copy and form charge-preserving density or pair interactions. The existing neutral bilinear singlet

    p_0 e_1-p_1 e_0

is rotation invariant and has phase weight zero for opposite charges. This is the binary vertex already recorded in entry 4316, not a newly discovered nuclear force. A direct-sum off-diagonal species hopping would instead convert particle labels and cannot stand in for a constituent-preserving binding law.

The lifted rim maps therefore solve the representation mismatch, but selecting and sourcing the charged constituent interaction remains a separate step.

## Breakup in the current common-vacuum model

The existing exterior graph has separate proton and belt internal blocks. Its shared connection is the exterior charge coordinate. After grounding that coordinate, the minimum field quadratic separates exactly:

    E(Q_p,Q_b)=F_p(Q_p)+F_b(Q_b)
              + eta (Q_p+Q_b)^2/2.

Here F includes each carrier's relaxed matter and internal/lead electric energy. There is no cross-carrier hopping, spatial-separation variable or attractive density term hidden in this graph.

For one unit of each internal norm-charge, compare with separate unit preparations and independent exterior reservoirs:

    E_pair-[E_p+E_b]=eta>0.

The checker evaluates this exactly for all three previously recorded electric coefficients; no assumption of the original coherent profile is needed because the independently relaxed carrier energies cancel.

For a breakup comparison retaining the **same total exterior charge -2 in one reservoir**, the exterior term also cancels. The pair-minus-breakup difference is then exactly zero. The graph has no geometric separation-dependent interaction, so it does not distinguish a bound pair from a separated pair in that account.

Changing from two reservoirs to one and calling the difference binding would change the comparison system. Keeping the actual exterior energy shows either repulsion or cancellation, not attraction.

If the field were instead assigned physical electric charges q_p=1 and q_n=0, this exterior cross term would vanish. The neutron's positive internal norm cannot simultaneously be used as a positive electric charge. The present norm-charge completion supplies neither nuclear binding nor a charged/neutral electromagnetic identification.

## The remaining interaction is now explicit

The next required source object is a number- and charge-preserving **cross-carrier interaction**. It must operate on the typed constituent ports, and the composite and breakup energies must use identical field, boundary and reservoir data. A proposed attraction must also be bounded below; merely appending a negative contact constant would not derive a binding law.

The positive rim stiffness is available as a compatibility term and response operator. The existing neutral spinor vertex is available as a typed pair operation. Neither supplies a selected nuclear interaction coefficient or distance-dependent attractive law by itself.

## Verification

    python research/voevodsky/checkers/check_deuterium_typed_rim_binding.py

Result: `research/voevodsky/results/deuterium_typed_rim_binding.json`.

Exact checks cover the tensor-lift trace and extension, spin covariance controls, opposite-phase failure and charged-link repair, inherited singlet invariance, and breakup-energy cancellation/repulsion. No measured binding is inserted.
