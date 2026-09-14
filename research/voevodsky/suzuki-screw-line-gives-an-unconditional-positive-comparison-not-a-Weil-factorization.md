# Suzuki's screw line gives an unconditional positive comparison, not a Weil factorization

## Sources newly audited

- Masatoshi Suzuki, *The screw line of the Riemann zeta-function and its applications*, arXiv:2209.04658.
- Masatoshi Suzuki, *Screw functions of Dirichlet series in the extended Selberg class*, arXiv:2209.12832.
- Masatoshi Suzuki, *On the Hilbert space derived from the Weil distribution*, arXiv:2301.00421v3 (7 November 2025).
- Published precursor: *Aspects of the screw function corresponding to the Riemann zeta-function*, J. London Math. Soc. 108 (2023), 1448--1487, DOI 10.1112/jlms.12785.

Primary PDFs were downloaded to `temp/suzuki-screw.pdf`, `temp/suzuki-dirichlet-screw.pdf`, and `temp/suzuki-weil-hilbert.pdf` and converted to text.

## Why this is the closest positive carrier found in the expanded search

Suzuki defines a source-explicit function `S_t(z)` containing the endpoint, prime, gamma/Lerch, and completed-zeta logarithmic-derivative terms. For each fixed real `t`, he proves unconditionally

\[
S_t\in L^2(\mathbb R,dz).
\]

Thus

\[
K_S(t,u):=\frac12\langle S_t,S_u\rangle_{L^2(\mathbb R)}
\]

is an unconditional positive-definite kernel. Integrating `S_t` against compactly supported test functions also gives an unconditional positive quadratic form

\[
\|P_\varphi\|_{L^2(\mathbb R)}^2\ge 0.
\]

This is a genuine analytic Hilbert carrier, not merely an abstract GNS completion of an assumed-positive Weil form. It also retains all source sectors in the pointwise formula for `S_t`.

## Exact gate: equality with the arithmetic screw/Weil form is RH-equivalent

Let `g` be Suzuki's zero-free explicit screw candidate. Its increment kernel is

\[
G_g(t,u)=g(t-u)-g(t)-g(u)+g(0).
\]

Suzuki proves, under RH,

\[
\frac12\langle S_t,S_u\rangle_{L^2}=G_g(t,u).
\]

More sharply, the equality of the positive norm with the arithmetic form is itself equivalent to RH. In the 2025 paper, Theorem 4.4 states, on the zero-mean test subspace,

\[
\boxed{
\|P_\varphi\|_{L^2}^2=\langle\varphi,G_g\varphi\rangle
\quad\text{for all }\varphi
\iff \mathrm{RH}.
}
\]

Using the differential intertwiner `D`, this is transported to the Weil form. Therefore the unconditional norm is only a **positive comparison form**. Identifying it with the complete Weil pairing is precisely the missing theorem, not a prior positive factorization.

## Where the proof uses the zero geometry

Under RH, Suzuki's functions

\[
F_\gamma(z)=\frac{m_\gamma i(1+\Theta(z))}{2(z-\gamma)}
\]

form an orthonormal basis of the model space `K(Theta)`. Parseval then turns the `L^2` norm of the source-explicit screw line into the zero sum and hence into the Weil form.

Without RH, `Theta=E^\#/E` is not supplied as the required meromorphic inner function, the model-space orthonormal-basis step is unavailable, and the norm identity fails for a test localized at an off-axis zero. Suzuki's converse explicitly constructs such a test and obtains a negative arithmetic value, contradicting the positive `L^2` norm.

Accordingly, the missing equality is exactly an innerness/orthogonality statement encoding critical-line location.

## Relation to the requested rung-four factorization

The construction has the right superficial shape:

\[
\text{completed source}\longrightarrow S_t\in L^2(\mathbb R)
\longrightarrow \langle S_t,S_u\rangle\ge0.
\]

But its arithmetic comparison has the form

\[
W(D\varphi*D\varphi^*)
=?\|P_\varphi\|_2^2.
\]

The question mark is not a normalization defect: universal equality is RH-equivalent. Hence replacing the completed rung-four observer by Suzuki's norm would replace the target rather than prove it.

For the Gaussian family this still suggests a useful finite-width diagnostic: compute the explicit defect

\[
\Delta(\varphi)
:=W(D\varphi*D\varphi^*)-\|P_\varphi\|_2^2.
\]

Any source proof must show `Delta=0` (or a sign strong enough for the target) without invoking model-space innerness. Suzuki's converse predicts that off-critical zeros appear exactly as hostile directions of this defect.

## Generalization confirms the obstruction is structural

For a member `F` of the semi-extended Selberg class, arXiv:2209.12832 gives a zero-free endpoint--Euler--gamma formula for `g_F`. Theorem 5.1 proves

\[
\mathrm{GRH}(F)
\iff g_F\text{ is a screw function}
\iff G_{g_F}\succeq0.
\]

The paper explicitly says this kernel positivity is the associated Weil positivity and is “essentially nothing new.” Thus the increment-kernel maneuver does not weaken the global positivity gate; it repackages it uniformly across the Selberg class.

## Comparison with other audited routes

This route is stronger than the quasicrystal measure route in one respect: it gives an unconditional positive `L^2` object at fixed source parameter. It fails later, at exact identification with arithmetic polarization. The quasicrystal route fails earlier, because unsmoothed temperedness is already RH-equivalent.

It is also the analytic analogue of the semilocal mismatch:

- the ambient positive carrier exists;
- the arithmetic quotient/model subspace is nontrivial only after the decisive analytic condition;
- declaring the quotient identification loses the theorem to be proved.

## Disposition

Suzuki supplies the nearest known positive analytic comparison carrier, but not a noncircular Weil factorization. The exact obstruction is now localized:

\[
\boxed{
\text{source-explicit }L^2\text{ positivity}
\not\Rightarrow
\text{Weil positivity};
\quad
\text{their universal equality is RH-equivalent.}
}
\]

The nonredundant continuation is to derive and simplify `Delta` directly for the Gaussian observer family. That could yield a certifiable source-side remainder, even though it cannot vanish universally without proving RH.
