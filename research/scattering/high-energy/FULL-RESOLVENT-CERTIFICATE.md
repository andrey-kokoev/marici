# H7 — full coupled-resolvent certificate and unresolved inputs

## Fresh source findings

The source omitted-mode estimate gives a numerical block-LDL/Sturm count of 420 internal eigenvalues below 16. It explicitly says this is **not interval arithmetic**. Its quoted Delta>=8.929371797830 is a proposed omitted-block gap based on that spectral evidence. The later response128 source embeds 420 original directions plus 128 response directions. Neither fact is a certificate of the smallest singular value of the **full coupled outgoing operator** throughout [3.09,3.51].

The supplied response128 archive contains full retained downstream fields and a downstream sparse matrix, not a materialized full entrance-plus-downstream outgoing operator on all 12,250 raw internal directions per body and all radial nodes. H5's downstream checks cannot be reused as a full inverse bound. The source reconstruction scripts may permit generating the missing operator; that reconstruction has not been performed here.

The physical occupation matrix assigns zero mass to boundary traces and cannot itself be a positive solver norm. This prerequisite is now resolved in RADIAL-RESOLVENT-ENVELOPE.md: normalized entrance and downstream coefficients use Euclidean norms including unit-weight algebraic traces, with an explicit bound to downstream occupation. A bound on the full coupled inverse in this norm remains outstanding; no infinite-field physical L2 bound is inferred.

## Corrected-state and energy-reference follow-up

The rebuilt H6 cache now permits a [fresh corrected native-leakage audit](CORRECTED-RESIDUAL-NATIVE-TERM.md). The response128 span is not invariant under the raw native Hamiltonian; an interaction-only residual misses a nonzero native term. Raw radial/boundary actions remain to be reconstructed. The spectral parameter must also be bound correctly: K is in [3.09,3.51], E_op=e0+K excludes the common pose shift, and E_total=e0+K+CPOSE includes it. The quoted omitted threshold 16 uses the latter reference. The partial checker now includes CPOSE when reporting its uncertified gap candidate; omitting it would overstate that candidate.

## A sufficient uniform Schur certificate

Fix positive domain/range norms and orthonormal retained/complement coordinates in them. Suppose the source outgoing matrix has block form

    A(E) = [ B(E)   C(E) ]
           [ C(E)*  D(E) ],

where the omitted sector is closed, D(E) is Hermitian positive and imaginary outgoing boundary terms lie in B(E). This structure must be verified after the chosen coordinate transformation; it is not a generic assumption about arbitrary non-Hermitian matrices.

Suppose **certified** uniform bounds over the whole closed packet band give

    ||B(E)^(-1)|| <= gamma,
    D(E) >= Delta I,  Delta>0,
    ||C(E)|| <= eta.

Put delta=1/Delta and rho=gamma eta² delta. If rho<1, then

    S(E)=B(E)-C(E)D(E)^(-1)C(E)*

is invertible by a Neumann-series argument, with

    ||S(E)^(-1)|| <= s = gamma/(1-rho).

The block inverse is

    A^(-1) = diag(0,D^(-1))
             + [ I ; -D^(-1)C* ] S^(-1) [ I, -C D^(-1) ].

The column and row factors have norm at most sqrt(1+(eta delta)²). Therefore a valid full-operator bound is

    ||A(E)^(-1)|| <= C_full = delta + s [1+(eta delta)²].

For every approximate lifted state P y and forcing b,

    ||A(E)^(-1)b-Py|| <= C_full ||b-A(E)Py||.

The residual on the right is the **full corrected residual**, not a residual projected back into the response subspace. This bound is sufficient, not necessary: failure of rho<1 is inconclusive, not refutation of H7. A certified direct inverse bound on S can replace the Neumann condition if the coupling is too large.

## How to cover a continuous band

At certified centers E_i, one can combine an inverse bound c_i with a proven operator-modulus bound omega_i(r) for all |E-E_i|<=r. If c_i omega_i(r)<1, then

    ||A(E)^(-1)|| <= c_i/[1-c_i omega_i(r)].

A finite collection of such certified neighborhoods covering the entire closed band supplies a uniform certificate. Between open/closed channel thresholds, ordinary differentiable estimates may be available. At thresholds the square-root boundary symbol is continuous but need not be Lipschitz; use a valid square-root/Hölder modulus or explicit interval enclosure instead of dividing by a zero channel velocity. Merely scanning a finite number of energies leaves gaps.

## Explicit countercontrols

1. B=1, D=9 and C=3 give a singular full matrix [[1,3],[3,9]], although D has a strict positive gap and B is invertible. Thus the omitted-block gap plus a retained solve is not enough. Here rho=1, exactly outside the sufficient certificate.
2. A scalar affine A(E)=E-E_star is invertible at every energy in any finite sample that omits E_star, but singular at E_star inside the band. The checker chooses E_star between two actual packet nodes. Sampled inverses do not certify a uniform inverse.
3. For any omitted forcing/residual component, Pi r=0 does not imply r=0. The checker includes the exact two-coordinate residual (0,1) with Pi=diag(1,0).

These are counterexamples to inference shortcuts, **not counterexamples to the actual source H7**.

## Disposition and next bounded attempt

H7 remains open. The substantive result is the explicit full-coupled sufficient certificate and the separation of its missing source inputs. The [radial-envelope follow-up](RADIAL-RESOLVENT-ENVELOPE.md) now fixes a positive coefficient norm and the actual Green-preconditioned matching operator, with a conditional Bessel bound on its invariant closed radial block. The central low-sector and downstream matching rows have now been evaluated in CORRECTED-MATCHING-RESIDUAL.md, alongside a conditional omitted-sector envelope. Remaining work is to certify the spectral frame and Delta, extend residual coverage beyond the center, and certify coupling and inverse bounds over the packet band. The source matching matrix is generally nonsymmetric; the follow-up supplies the general two-off-diagonal Schur bound rather than assuming the Hermitian block structure used in the sufficient example above. The source's numerical inertia evidence is useful input but cannot be relabelled a certified lower bound.

The accompanying checker validates the exact rational certificate example and hostile examples, binds the source archives/notes, and records dimensions/band metadata. It does not establish H7, execute the full raw reconstruction, or certify a physical/continuum error.
