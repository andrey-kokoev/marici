# C2 — full-space outgoing completeness and the five-mode decomposition

## Fixed Hilbert space and reference operator

Work on exactly the weighted eleven-dimensional core plus three weighted half-line chains. Whitening is unitary and does not change spectral type. Let H_D be the three free Dirichlet chains, let V include their three endpoint channels into the visible core coordinates, and P=VV*. The coupled operator is the bounded self-adjoint block operator with core K+P, leads H_D and endpoint couplings -V,-V*.

On the **same** Hilbert space choose

    H_ref=(K+P) direct-sum H_D.

Only the contact off-diagonal blocks differ between H and H_ref. Their range lies in the three core-port and three lead-endpoint coordinates, so H-H_ref has rank six and is trace class. No infinite lead cutoff is used.

The discrete sine transform diagonalizes each H_D as multiplication by E(k)=2-2cos(k), 0<k<pi. Its spectrum is purely absolutely continuous; the energy derivative is positive in the open interval and the two endpoints carry no atom. The finite core summand of H_ref has no absolutely continuous subspace. Therefore H_ac(H_ref) is exactly the full three-lead Hilbert space embedded by J.

## Wave operators: the trace-class scattering theorem

The Kato–Rosenblum theorem for self-adjoint operators differing by a trace-class operator states that

    Omega_±=s-lim_(t->±infinity) exp(itH) exp(-itH_ref) P_ac(H_ref)

exist, are isometries on H_ac(H_ref), and have range H_ac(H). All its hypotheses hold here: the operators are bounded self-adjoint on the same space and their difference has finite rank.

Since exp(-itH_ref)J=J exp(-itH_D), set W_+=Omega_+ J. Then on the **entire** free three-lead space,

    W_+=s-lim_(t->+infinity) exp(itH) J exp(-itH_D),
    W_+*W_+=I,       Ran(W_+)=H_ac(H).

This theorem does not eliminate singular-continuous spectrum. That separate input is supplied by C9's rational-Weyl spectral-measure proof.

## Full point-spectrum classification

The exact source core satisfies HK=K*H and its weighted quadratic form is nonnegative (fresh inertia (10,0,1)). The coupled energy is a sum of that core form, positive contact differences and positive lead differences. Hence H>=0 and there are no negative-energy eigenstates.

For an energy in (0,4), each lead solution is a linear combination of two nondecaying oscillatory solutions. Square summability forces both amplitudes to vanish. At E=0 or E=4 the lead solutions are respectively a+bn or (-1)^n(a+bn), again square summable only when zero. The lead endpoint equations then force the central port coordinates to vanish. A remaining core vector would be an invisible K eigenvector. C11's fresh cyclic-span certificate under K alone excludes every such nonzero vector, including at both thresholds.

For E>4, the square-summable lead solution has the unique tail

    psi_j,n=(-r)^n x_j,    E=2+r+r^(-1),    0<r<1.

Substitution into the core equation yields

    F(E)x=[E I-K-(1+r(E))P]x=0.

The weighted secular matrix is symmetric, and

    F'(E)=I+[r²/(1-r²)]P > 0

in the positive metric. Thus each weighted secular eigenvalue increases strictly with E. At E=4 (r=1), exact congruence elimination gives inertia (6 positive,5 negative,0 zero). At r=1/32 it gives (11,0,0), and positivity persists toward infinity by monotonicity. Precisely five roots occur for E>4, counted with multiplicity.

The checker additionally takes the **reported rational decay brackets as candidates**, recomputes their full eleven-dimensional endpoint inertias, and verifies a change of exactly one in each of five disjoint energy intervals. Together with the global count, this proves the five modes are distinct and simple, exhaust all above-band roots, and correspond to the reported modes. Stored pass flags or sector root counts are not used as proof.

At each root, normalize the full vector, not just the core. Its exact norm is

    ||x||_H² + [r²/(1-r²)] sum_j h_j |x_j|².

The five normalized full-tail modes span the full point subspace. Let P_b be their orthogonal spectral projection. C9 supplies P_sc(H)=0, so I=P_b+P_ac(H).

## The outgoing asymptote

For any initial state psi (in particular any initially central state), define

    phi_out=W_+*(I-P_b)psi.

Completeness gives (I-P_b)psi=W_+ phi_out. The defining strong limit of W_+ and unitarity of exp(-itH) then give

    ||exp(-itH)(I-P_b)psi-J exp(-itH_D)phi_out|| -> 0.

The bound component exp(-itH)P_b psi remains separate and need not have a time-independent central occupation, because distinct bound frequencies can beat. No claim that every normalized central state escapes with norm one is made.

## Verification boundary

`check_three_port_completeness.py` freshly replays the C9/C11 inputs and verifies the core and full secular inertias, all five candidate brackets, finite-rank contact difference and algebraic tail normalization. The wave-operator existence/completeness uses the stated trace-class theorem; the checker is not a mechanized proof of that theorem. No source-owner result file is rewritten, no source stationary solver is rerun, and no physical particle identification or larger-model spectator classification is imported.
