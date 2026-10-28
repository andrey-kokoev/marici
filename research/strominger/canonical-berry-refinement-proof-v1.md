# Canonical rank-one Berry refinement: proof (++)

## Frozen claim and convention

Let P:[0,1]->End(C^n) be C2, with P(t) a rank-one orthogonal projector and P(0)=P(1). For a partition pi=(0=t0<...<tm=1), set

    z_pi=Tr(P(t0) ... P(t_(m-1))),
    H_pi=z_pi/|z_pi| whenever z_pi is nonzero.

Use the existing convention A=-i v†v' and phase exp(i integral A). For a normalized frame v on the interval, the invariant closed-loop phase is

    H(P)=exp(i integral_0^1 A) * <v(1),v(0)>.

The endpoint factor has unit modulus since the endpoint projectors coincide. With a periodic frame it is one. This phase convention is the one frozen in the node; reversing it conjugates the answer. It must not be confused with silently reversing the ordering of the cyclic product.

**Theorem.** z_pi is nonzero for every sufficiently fine partition, and H_pi converges to H(P) as mesh(pi) tends to zero, without requiring nested or uniform partitions. In fact a loop-dependent constant M gives

    |H_pi-H(P)| <= M*mesh(pi).

The already established retained finite-packet reconstruction preserves H_pi at each sufficiently fine partition and hence preserves this numerical limit.

## 1. Horizontal frame exists on the whole interval

Set K=[P',P]. K is C1 and anti-Hermitian. Solve U'=K U, U(0)=I. Finite-dimensional linear ODE existence and uniqueness give a C2 unitary U. Differentiating P^2=P gives P P' P=0 and P'=P'P+PP', hence [K,P]=P'. Therefore

    d/dt(U† P U)=U†(P'+[P,K])U=0.

Choose a unit u0 in im P(0) and put u(t)=U(t)u0. Then P(t)u(t)=u(t), ||u(t)||=1 and

    u'=P'u,   <u,u'>=0.

This is a horizontal frame on the interval; it need not be periodic. No single projective coordinate chart is assumed. Closure of P gives u(0)=beta*u(1), with beta=<u(1),u(0)> and |beta|=1.

Define M=sup ||u''(t)||, finite by compactness. An intrinsic bound is

    M <= sup ||P''|| + (sup ||P'||)^2,

using u''=P''u+P'u'. The constant depends on the loop; no uniform bound over all C2 loops is asserted.

## 2. Neighbor overlaps are second-order close to one

For h_j=t_(j+1)-t_j, Taylor's integral remainder and horizontality give

    w_j=<u(t_j),u(t_(j+1))>,
    |w_j-1| <= M*h_j^2/2.

If M*mesh(pi)^2/2<1, all w_j are nonzero. For any nonzero complex w,

    |w/|w|-1| <= |w/|w|-w|+|w-1| <= 2|w-1|.

Thus, with eta_j=w_j/|w_j|,

    |eta_j-1| <= M*h_j^2.

If M=0 the same statements hold with zero error without a small-mesh restriction.

## 3. Cyclic trace retains the endpoint transition

Writing P(t_j)=u(t_j)u(t_j)† and multiplying the rank-one matrices gives

    z_pi=<u(t0),u(t1)> ... <u(t_(m-1)),u(t0)>
         =beta * product_(j=0)^(m-1) w_j.

The second equality uses u(t0)=beta*u(tm). In particular z_pi is nonzero under the preceding mesh condition, and

    H_pi=beta * product_j eta_j.

A telescoping product of unit complex numbers gives

    |product_j eta_j-1| <= sum_j |eta_j-1|
                         <= M sum_j h_j^2
                         <= M mesh(pi) sum_j h_j
                         = M mesh(pi).

This proves convergence to beta for every mesh-zero partition sequence, not just a finite family of examples.

## 4. Identify beta with the independently defined phase

For any normalized C2 frame v on the interval, define

    u(t)=exp(-i integral_0^t A_v) v(t),  A_v=-i v†v'.

It is horizontal. Consequently

    beta=<u(1),u(0)>=exp(i integral_0^1 A_v)<v(1),v(0)>=H(P).

A rephasing v(t)->exp(i chi(t))v(t) changes A_v to A_v+chi' and changes the endpoint factor by exp(i(chi(0)-chi(1))); these cancel. On an interval the required phase lift exists. Thus the comparison includes nonperiodic frames and projective chart crossings without discarding transition data.

## 5. Retained-cut readout comparison

At a finite partition, retain its ordered parameter samples and all matrix entries. Let S_pi be either existing retained promotion policy and R_pi its actual member recovery. The established interface gives R_pi S_pi=id on these source records. The product readout is Tr of the ordered recovered matrices, normalized only when nonzero.

Therefore the retained readout is EXACTLY H_pi in the mathematical interface. The preceding convergence theorem applies unchanged. No topology on an infinite tower object, native derivation of the analytic connection, or convergence of the whole growing record type is inferred. This clause concerns the numerical holonomy readout and its retained finite-source presentations.

## Controls and verification level

The independent executable controls compare overlap products with matrix traces, check nonuniform partitions and rephasing, and retain a pole-crossing real frame v(t)=(cos(pi*t),sin(pi*t)). That frame has zero local connection but v(1)=-v(0), so its closed phase is -1. Dropping the endpoint transition would incorrectly give +1. Reversing a generic latitude's ordering conjugates its nonreal phase and is distinguishable.

An annular added flat connection is outside this canonical projector-induced class; it remains a counterexample to determining arbitrary connections from projectors alone.

**Outcome ++ at written-proof level**, using standard finite-dimensional ODE theory, Taylor estimates and exact retained-readout recovery. Numerical checks are regressions, not the proof of the all-refinement quantifier. No new Agda proof or physical experiment is asserted. This settles only `refining-canonical-berry-cuts`, not full physical-domain coverage or the unformulated source-binding successor.
