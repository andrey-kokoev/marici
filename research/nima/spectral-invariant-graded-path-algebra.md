# Same-mode states form an invariant graded subalgebra, not a lossless quotient

## Structural result

On the declared product of the two retained triangle occurrence spaces,

    G = C_left tensor C_right^-1,
    D = (I+G+G^2)/3.

The existing same-mode spectral projection is EXACTLY this relative-slot group average. Each eigenpair (lambda,mu) has G-eigenvalue lambda/mu, so averaging retains precisely lambda=mu.

This is a new checked identification within the existing coefficient representation. It is not physical gauge admission. Relative rotations preserve each abstract triangle context but are not asserted to be automorphisms of the original seam-marked seed as one graph.

## Three orbit coordinates

With left slots (AB,BC,CA) and right slots (BA,AD,DB), the relative rotation has three size-three orbits, indexed by q=i+j mod 3:

| q | Occurrence pairs |
|---|---|
|0|(AB,BA), (BC,DB), (CA,AD)|
|1|(AB,AD), (BC,BA), (CA,DB)|
|2|(AB,DB), (BC,AD), (CA,BA)|

D averages coefficients within each orbit. Its image consists of functions constant on each orbit, hence has dimension three.

This does NOT contradict the earlier absence of a partition of occurrence pairs BY EIGENMODE. These are relative-rotation orbits. Their indicator vectors form a different basis of the same invariant space; the three same-mode spectral channels are Fourier combinations of these orbit coordinates. Each orbit label is not one eigenvalue.

Occurrence IDs, endpoints and full histories are still retained separately. Passing to orbit coefficients is an observation/representation operation, not permission to merge primitive records.

## A correctly typed graded product

The pilot follows each triangle within its own retained context. At length m, a start slot (i,j) specifies a pair of m-step paths. This is the deterministic product of the two chosen cycle contexts, not the unrestricted seed path language allowing branch changes at shared vertices.

Let x_m denote coefficients on those length-m paths and y_n coefficients on length-n paths. Endpoint-compatible concatenation gives

    (x_m * y_n)(i,j) = x(i,j) y(i+m,j+m),
    output length = m+n.

Slot indices are taken modulo three; actual path length is NOT. Every composed row keeps its start and end endpoint tuples, the two complete primitive words, and its parent packets.

The shift obeys tau_m tau_n=tau_(m+n) and distributes over pointwise multiplication. Hence the graded product is associative. The constant-one packet at grade zero supplies the identity on coefficient/path values. Parenthesization records remain different even when the flattened path and coefficients agree.

A grade-three constant-one loop has the same endpoint action and coefficient effect as grade-zero identity, but different retained length and words. The checker explicitly refuses to infer an empty history from the three-step coefficient period. These packet structures are mathematical path data, not newly allocated physical execution events or a claim to bypass another ledger's ancestry bound.

## Closure and the smaller algebra

Relative rotation G is a grade-preserving automorphism of this product: it commutes with the simultaneous path shift and preserves pointwise multiplication. Its fixed elements therefore form a graded subalgebra.

For invariant inputs, write x(i,j)=u(q), y(i,j)=v(q). Their three-coordinate product is

    (u_m * v_n)(q) = u(q) v(q+2m mod 3),
    output length = m+n.

This is an exact three-coordinate description PER GRADE. It is generally noncommutative, and the full graded algebra is not merely one three-dimensional state space. The stored path length and provenance cannot be reduced to m mod 3 even though the coefficient shift can.

Thus a genuinely restricted input interface containing only invariant states can recursively compose inside that sector under this declared operation. This is stronger than the earlier one-step observation-rank result, but it remains scoped to this operation family.

## Why arbitrary inputs cannot be projected first

The group average has the algebraic conditional-expectation/bimodule property:

    D(a*x)=a*D(x), D(x*a)=D(x)*a when D(a)=a.

No C*-algebra, measurement or probabilistic conditional expectation is being supplied here; these are identities of the graded coefficient algebra.

For arbitrary x=d+r and y=e+s with d=Dx, e=Dy,

    D(x*y)=d*e + D(r*s).

The mixed terms vanish, but D(r*s) need not. In an exact grade-one hostile, both r and s have zero D-projection, while their product at grade two has orbit-coordinate vector (2/9,0,0). Its fixed-denominator aggregate is the earlier 2/243.

Therefore ker(D) is not an ideal and D is NOT an algebra homomorphism onto the invariant subalgebra. The three-channel state is a closed SECTOR, not a quotient that can replace every full input without changing future responses. This is the precise obstruction behind the prior residual-residual effect.

## Source seam/reference audit

Extract reciprocal endpoint pairs directly from the six packet records. The unique unordered pair is {AB,BA}; in the ordered left/right occurrence-pair carrier its marker is the coordinate vector at (AB,BA). This extraction uses no matrix amplitude, scalar gluing convention or inverse law. The checker verifies all 24 vertex renamings and deletion of either seam occurrence.

Relative rotation takes this marker through

    (AB,BA) -> (CA,AD) -> (BC,DB) -> (AB,BA).

Only the first is reciprocal. Therefore the relative-rotation average does not preserve the exact seam address as a marked feature. In contrast, the actual seed automorphism (AB)(CD), with the corresponding exchange of triangle factors, DOES preserve the reciprocal marker. The two transformations must not be called the same source symmetry.

### Conditional seam-coordinate reader

In the already declared coefficient representation, let h read the coefficient at the retained (AB,BA) address. Exact checks give

    hD != h, hR != 0.

The coefficient states supported at (AB,BA) and (CA,AD) have the SAME D-projection, but their h-readings are 1 and 0. Their source graph and seam metadata can be identical. Consequently retaining the marker as a label does not recover the missing seam coefficient of a general state.

This uses the source marker to define an address-specific coefficient reader. The source supplies the marker, not an assertion that this reader is a physical instrument.

### Reuse of the existing endpoint-comparison reader

No new response law is needed for a second conditional control. Use the seam marker as the probe y in the already tested

    J(x,y)=x^T M y/81, M=C_left tensor C_right.

M maps this probe to its predecessor address (CA,DB). For x supported at that predecessor and x'=Dx, the current D-readings agree, while

    J(x,seam)=1/81, J(x',seam)=1/243.

The coefficient rule, endpoint incidence and denominator remain unchanged. Preparation of the seam-addressed probe is an explicit assumption; identifying an available address does not establish preparation authority or calibration.

### Precise boundary

The seam does not disprove the existence or closure of the invariant subalgebra. If preparations are restricted to im(D), the seam value is exactly the orbit-0 coefficient and is recoverable from the three-coordinate state. Nor does source retention require any particular active numerical observation: the original marker is still exactly recoverable from the stored endpoints.

What fails is a stronger claim: that relative-rotation averaging is a lossless, seam-respecting replacement for ARBITRARY coefficient inputs once seam-addressed observations/probes are permitted. To support that interface, retain the needed residual information or independently justify an invariant-preparation restriction. Do not erase the seam marking, declare its other orbit members reciprocal, or equate a stored marker with its state-dependent response.

## Combined interpretation

There are now two justified mathematical regimes:

1. **Invariant preparation contract:** if inputs really belong to im(D), three coefficients per path grade suffice for this composition law, with histories retained separately.
2. **General preparation contract:** retain the other six coefficient directions as well. Their joint products can feed the visible sector even though each is individually invisible to same-mode probes.

Which regime is admitted physically is not settled by the group average. No preparation, coupling strength, new observer or preferred eigenmode was chosen to make this result work.

## Verification

    python research/nima/checkers/check_spectral_invariant_path_algebra.py

Fresh exact arithmetic verifies the group-average identity and all three orbits; 243 basis-pair/length-residue tests check automorphism, invariant closure, orbit-coordinate multiplication and bimodule identities. Another 64 graded path fixtures check associativity with retained parenthesizations. Unit/three-step-loop distinction, noncommutativity, and the hidden-product hostile are also checked. The shift and automorphism identities explain the all-length result beyond these finite regressions.

The seam follow-up additionally checks source reciprocity, all 24 vertex renamings, two deletion controls, the three marker images, preservation by the actual seed factor exchange, the hD/hR obstruction, the fixed-reader seam-probe hostile and recoverability on invariant inputs.

Report: `results/spectral-invariant-path-algebra.json`.
