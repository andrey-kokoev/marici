# Holomorphic feature closure retains completed cross-spectral packets

## Strength

Convergence and relative-comparison theorem on compact spectral subsets of the declared upper-half-plane region. The actual holomorphic feature closure, unlike arbitrary L2, supports bounded spectral evaluation. An additional feature-degree scale controls evaluation across unbounded memory lengths. On that strengthened scale the full cross-spectral relative packets, not only diagonal integrated forms, extend by continuity.

No claim is made at the spectral-region boundary, on arbitrary L2 functions, or for arbitrary projective-limit source families.

## 1. The relevant closed feature subspace

Let Omega be the interior of the fixed spectral disk and H=L2(R_+,C^2). The normalized features are H-valued functions

    F_f(z)(t)=A_Cl h_f(z) exp(i z t).

For the admitted finite compact shell forcings these are holomorphic in z as H-valued functions on Omega: on spectral compacta the positive imaginary gap controls all t-derivatives of the exponential, and the traces are entire. They lie in the vector-valued Bergman space A2(Omega;H), a closed subspace of L2(Omega;H).

Take the closure of the source feature span and its constant-signature transforms inside this space. The normalized two-sheet J preserves holomorphicity. This is the feature envelope used below; arbitrary nonholomorphic L2 vectors are not introduced by completion.

For K compactly contained in Omega, choose delta>0 such that every disk of radius delta about a point of K is contained in Omega. Vector-valued submean estimates give

    sup_(z in K) ||F(z)||_H <= C_K ||F||_A2,
    C_K=1/(sqrt(pi) delta).

Thus evaluation extends boundedly to the whole chosen feature closure, uniformly on K.

## 2. The Clark fibre structure survives closure

At each z, the values of finite features lie in the closed two-dimensional subspace

    {v exp(i z t):v in C^2} of H.

Continuity of evaluation preserves this property under feature closure. Hence every completed feature still has a unique amplitude hhat(z) with F(z,t)=hhat(z) exp(i z t). Its amplitude is holomorphic: for example integrating F(z,t) against exp(-t) gives hhat(z)/(1-i z), and this bounded H-functional is holomorphic.

Consequently the full cross-spectral pairing retains the exact formula

    <F(w),J G(z)>_H
      = hhat_F(w)^* J hhat_G(z)/[-i(z-conjugate(w))].

It is bounded by C_K^2 ||F|| ||G|| for w,z in K. The denominator remains attached to that pair and does not vanish because the original region has a positive imaginary gap.

This is not an inverse map from arbitrary entire amplitudes to weighted forcing. No such inverse or closed-range assertion is needed.

## 3. Unbounded feature counts need their own weight

The previous depth weight b_s(k)=(2 lambda s)^k k! controls active seam count k, not the number m of retained feature slots in memory and seam letters. Evaluation on m slots can cost C_K^m even when k is fixed.

For b>=1 strengthen the shape norm by b^m, retaining the original memory/seam weights and b_s(k). Call the resulting l1 scale Y_(s,b). Count all evaluated feature slots, including those of a retained root factor when its spectral evaluation is requested; never duplicate that root factor.

Choose b>=max(1,C_K). Then evaluation of every ordered slot tuple in K is contractive from this weighted scale to its fibre-valued shape carrier. Permitted normalization preserves total feature count, and the differential moves a feature from seam to memory without changing that count. Therefore their earlier bounds persist unchanged.

Balanced tensor concatenation adds feature counts, so b^(m+n)=b^m b^n. Its only previously required loss is in the depth radius:

    ||x tensor_balanced y||_(s,b)
      <= ||x||_(2s,b) ||y||_(2s,b).

Take the intersection over integer s,b>=1 for one complete locally convex receiver supporting all these operations and all compact-interior evaluation families. This is explicitly a stronger topology than the earlier depth-only scale.

## 4. Full relative packets extend

Assign spectral arguments to the ordered output feature slots, and transport those labels consistently through each permitted normalization. On every finite record the source current theorem gives

    q_external(w,z)+T_chi(w,z)=N_chi^*q_coarse(w,z),

with each pairwise denominator, signature channel, root factor, and ordered slot retained. Distinct shapes contribute only when their prescribed types match or when the source constructor declares a new match.

The slotwise evaluation bound and the l1 new-match estimate now give uniform bounds on K for all these packet forms. Their sums converge absolutely on Y_(s,b), and finite-record identities extend by density. The relative nested-cut law and pentagon consequently hold for the full pairwise-indexed packet on compact spectral interiors, not merely after diagonal integration.

This extends the TOTAL source-current packet. Separate bulk and forcing integrals remain separately labelled on finite sources, but continuity of their individual completed integral maps is not proved merely by boundedness of their sum. Their separate convergence is an additional task; no cancellation is silently used to claim absolute convergence of each channel.

## 5. Source approximation

For a source path with n events, at most n features occur. Replacing the earlier source weight a^n by (b a)^n pays for the new b^m factor. The prior path-length and theta-tail arguments therefore give continuous maps into Y_(s,b), and quantitative convergence on the extra-path-length domain, for each fixed s,b.

Endpointwise separation remains valid on this stronger summable source domain because its finite endpoint corners and faithful maps are unchanged. This does not establish that every previously admitted source vector lies in every stronger scale space.

## 6. Boundary hostile

On a disk of radius R, scalar normalized monomials have boundary evaluation squared proportional to (n+1)/(pi R^2). It is unbounded with n. At interior radius fraction sqrt(t), the Bergman evaluation bound is proportional to

    sum_(n>=0) (n+1)t^n = 1/(1-t)^2,  t<1.

Thus a compact-interior margin is substantive, not a removable convention. No extrapolation to boundary spectral evaluation or the real axis is authorized.

## Verification

`uv run python research/voevodsky/checkers/check_holomorphic_packet_evaluation_bounds.py`

Passed exact interior-series remainder identities, the boundary negative control, and feature-degree weight tests. The H-valued holomorphic closure and extension claims follow from the proofs above, not from numerical Clark samples.
