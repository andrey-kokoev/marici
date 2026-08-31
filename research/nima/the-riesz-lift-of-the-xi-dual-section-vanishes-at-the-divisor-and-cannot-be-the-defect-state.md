# The Riesz lift of the Xi dual section vanishes at the divisor and cannot be the defect state

## Tempting construction

Suppose the theta determinant line \(\mathcal L_\theta\) is given a Hermitian
metric.  The Mellin dual section

\[
\tau_s\in\mathcal L_{\theta,s}^*
\]

then has a Riesz representative

\[
r_s\in\mathcal L_{\theta,s}
\]

satisfying

\[
\tau_s(\ell)=
\langle r_s,\ell\rangle.
\]

One might try to send \(r_s\) through the retained incidence and use it as the
G4 defect state.

## Divisor collapse

At an Xi zero \(s_0\), the one-dimensional dual covector vanishes:

\[
\tau_{s_0}=0.
\]

Nondegeneracy of the metric forces

\[
r_{s_0}=0.
\]

Every bounded linear incidence \(J_s:\mathcal L_{\theta,s}\to H_s\) then gives

\[
J_{s_0}r_{s_0}=0.
\]

Thus the Riesz lift produces the zero vector exactly where a nonzero defect
state is required.

## Normalization would divide by Xi

Choose a local nonvanishing frame \(e_s\) and write

\[
\tau_s(e_s)=\xi(s).
\]

The Riesz representative is proportional to

\[
\overline{\xi(s)}e_s
\]

for the Hermitian metric convention.  Recovering \(e_s\) from \(r_s\) requires
division by \(\xi(s)\) or its conjugate norm.  That normalization is singular
at the divisor and is not holomorphic.

Consequently neither Riesz normalization nor unit-norm rescaling constructs a
holomorphic nonzero Xi kernel state.

## Section versus residue

The Koszul cohomology at a zero is the fibre

\[
\mathcal L_{\theta,s_0}
\]

or, locally, the torsion module \(\mathcal O/(\xi)\).  This residue is not the
value of the vanishing dual section.  It is represented by a nonvanishing
carrier frame modulo multiplication by \(\xi\).

A map to the Green kernel must therefore act on the carrier line or the
Koszul residue module, not on \(\tau\) viewed as a vector.

## Required independent incidence

The defect map

\[
i_s:\mathcal L_{\theta,s}\to H_s
\]

must be constructed independently of the scalar value \(\tau_s\).  It must
remain injective at Xi zeros and satisfy

\[
C(s)i_s=w_s\tau_s.
\]

At the divisor, the right side vanishes while \(i_s\) remains nonzero.  This
is precisely why the divisibility square is stronger than a Riesz
representation of the Mellin functional.

## Hostile test

Any proposed defect vector of the form

\[
\psi_s=T_s\tau_s^\sharp
\]

with \(T_s\) bounded and \(\tau_s^\sharp\) a metric dual fails immediately:

\[
\xi(s_0)=0
\Longrightarrow
\psi_{s_0}=0.
\]

If \(T_s\) has a pole cancelling that zero, the pole must be derived from an
independent source complex; otherwise it is division by the Xi section.

## Disposition

Metric duality cannot construct the missing Xi defect projection.  The
required nonzero state belongs to the carrier-line residue, not to the
vanishing Mellin covector.  G4 still requires an independent source incidence
of the Koszul carrier line into the closed Green domain.  No RH conclusion is
authorized.
