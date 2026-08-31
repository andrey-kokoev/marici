# G4 corrected constructor frontier after determinant-variance and line-section audits

## Objects now separated

G4 involves four distinct objects that earlier packets partially conflated.

### Euler carrier

The reciprocal \(\det_3\) carrier is regular and zero-free on its native
charts.  Primitive and square data are anomaly-line frames.  The Euler block
enters the completed determinant line contravariantly because

\[
\det(I-L)^{-1}=\zeta.
\]

### Theta divisor section

The theta Mellin--Poisson functional is a holomorphic dual-line section

\[
\tau\in H^0(\mathcal L_\theta^*)
\]

whose scalar coordinate is \(\xi\).  It is not an everywhere-invertible
trivialization on a region containing Xi zeros.

### Theta Koszul complex

The dual section defines

\[
K_\tau:
\mathcal L_\theta\xrightarrow{\tau}\mathcal O.
\]

Its local cokernel length is the Xi zero multiplicity.  This is a genuine
completed divisor complex, but it contains determinant-line residue rather
than a Green-domain state.

### Closed Green boundary pencil

The maximal-isotropic boundary pencil \(C_{\rm FP}(s)\) has an exact Schur
kernel reduction to \(I-K_{\rm rel}(s)\).  Its relative \(\det_2\) charts glue
reciprocally, and its kernel traces have zero boundary flux on the declared
domain.

## Corrections now enforced

1. The ordinary closed-loop determinant has the wrong Euler variance; only a
   graded determinant line can carry the inverse Euler character.
2. A holomorphic analytic return cannot be similar on an open complex chart
   to a nonconstant positive self-adjoint G3 Schur return.
3. The relative first-trace anomaly is not the primitive Euler current.
4. Reciprocal \(\det_2\) charts glue without inserting a separately convergent
   first trace.
5. Scalar \(\det_3\) convergence does not produce a trace-class holomorphic
   Fock state on the critical strip.
6. The Mellin functional carries the divisor as a dual section; it does not
   trivialize it away.

## Closed finite and chartwise statements

The following calculations are exact on their declared domains:

- finite Euler/Fock readout
  \(\operatorname{Tr}\Gamma(L_X)=\zeta_X\);
- finite det2/det3 anomaly signs;
- finite ordinary and graded Schur factorizations;
- centred seam trace-class return;
- \(\mathcal S_2\) reciprocal relative determinant gluing;
- cone-kernel/relative-collision equivalence;
- algebraic multiplicity of a relative determinant zero;
- maximal-isotropic vanishing of boundary flux;
- Xi multiplicity as the local length of \(K_\tau\).

## Two unresolved identities

### Divisor-to-state square

Construct source maps

\[
i:\mathcal L_\theta\to H_1,
\qquad
w:\mathcal O\to H_0
\]

such that

\[
C_{\rm FP}(s)i(s)=w(s)\tau_s.
\]

Injectivity of \(i\) then sends every Xi zero to a nonzero closed boundary
state.

### Green readback

The retained history metric now constructs the reverse incidence
\(B^\dagger\), so the paired pencil and vector-level forcing cancellation are
defined. The remaining problem is characteristic compatibility with the
natural Xi history.

For the column-only natural history, the exact identity is

\[
2\left(\operatorname{Re}s-\frac12\right)
\|u_s\|^2
=
-2\operatorname{Re}
\bigl(c_s\langle u_s,\Phi\rangle\bigr)
-\Sigma(\operatorname{Tr}_\partial u_s,
        \operatorname{Tr}_\partial u_s).
\]

Maximal isotropy kills the boundary flux but not the forcing residual. The
paired pencil cancels that residual only by imposing its lower adjoint source
equation. Proving that the Xi-derived history satisfies that equation off the
seam already contains the RH-bearing confinement.

## Complement and multiplicity requirement

The divisibility square must extend to a holomorphic splitting

\[
C_{\rm FP}(s)
\sim
\begin{pmatrix}
a(s)\tau_s&*\\0&C_Q(s)
\end{pmatrix},
\]

with \(a\) nowhere zero and \(C_Q\) holomorphically invertible with
cutoff-uniform compact-local inverse bounds.  This proves both directions and
preserves local module lengths.

A pointwise kernel injection alone proves only

\[
\xi(s)=0\Longrightarrow\ker C_{\rm FP}(s)\ne0.
\]

It does not exclude additional cone divisors or preserve multiplicity.

## Exact RH-bearing chain

Once the two identities and complement theorem are proved, the argument is:

\[
\xi(s)=0
\Longrightarrow
0\ne\psi\in\ker C_{\rm FP}(s)
\Longrightarrow
\left(\operatorname{Re}s-\frac12\right)
\mathcal N_s(\psi)=0
\Longrightarrow
\operatorname{Re}s=\frac12.
\]

Every arrow is currently typed.  The first and the exact bulk-form readback
remain unproved.

## Status

G4 is not closed.  Scalar Xi provenance, relative determinant charts, cone
kernel reduction, and maximal-isotropic boundary closure are established.
The unresolved RH content is concentrated in the divisor-to-state square and
the identification of the cone Green bulk with the retained G3 form.  No
ledger mutation or RH conclusion is authorized.
