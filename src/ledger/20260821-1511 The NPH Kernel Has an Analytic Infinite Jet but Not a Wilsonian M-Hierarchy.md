# 1511 — The NPH Kernel Has an Analytic Infinite Jet but Not a Wilsonian \(M\)-Hierarchy

## Status

Exact local completion result for Entry 1510.

## Regular germ

Multiply the denominator of Entry 1510's transported kernel by \(x\):

\[
D_b(x)
=
(x+i)
+
b e^{-2ix}(x-i).
\]

At zero momentum,

\[
D_b(0)=i(1-b).
\]

Physical Bogoliubov normalization requires \(|b|<1\), so \(D_b(0)\neq0\). The transported kernel therefore has a convergent analytic germ around \(x=0\):

\[
\kappa_b(x)
=
\sum_{n\ge0}c_n(b)x^n.
\]

Thus the fixed-time NPH kernel does belong locally to an infinite-jet completion of the boundary-operator algebra. Entry 1510's obstruction is specifically finite-order.

## Wrong controlling scale for Wilsonian locality

Let

\[
q=\frac{p_0}{M}
=
\frac{k}{a_0M},
\qquad
\mu=\frac{M}{H}.
\]

Then

\[
x=\frac{p_0}{H}=\mu q,
\]

and the transported phase is

\[
e^{-2ix}=e^{-2i\mu q}.
\]

Consequently, the \(q\)-jet contains coefficients with powers

\[
\mu^n=\left(\frac{M}{H}\right)^n.
\]

For \(M/H\gg1\), these coefficients are not naturally ordered by powers of the Wilsonian parameter \(q=p_0/M\). The actual variation scale is

\[
\Delta q\sim\frac{H}{M},
\]

not order one in \(q\).

Therefore:

\[
\boxed{
\text{analytic infinite-jet completion}
\not\Rightarrow
\text{controlled Wilsonian derivative expansion in }p_0/M.
}
\]

This derives the second-scale warning of Easther–Kinney–Peiris: restoring hypersurface independence requires \(H\) inside the coefficient architecture.

## Pole and radius typing

The scalar kernel germ extends until it meets a zero of

\[
D_b(x)=0.
\]

These zeros bound the radius of that scalar chart's Taylor series. They remain projective chart degenerations unless the underlying solution line or its physical pairing also becomes singular.

The completed coefficient object should therefore be treated as an atlas:

\[
\text{projective solution line}
\quad\leftrightarrow\quad
\{\text{local Riccati kernel charts}\},
\]

not as one globally regular scalar kernel.

## Architectural result

The common coefficient envelope has at least two filtrations:

1. a **boundary-jet filtration** by powers of \(p_0/M\);
2. a **background/adiabatic filtration** involving \(H/M\) and the phase \(p_0/H\).

NPH is simple in the second description and highly nonlocal in the first. Fixed-time BEFT is native to the first.

This is another instance of:

\[
\text{same object}
\quad+\quad
\text{inequivalent useful filtrations},
\]

with no implication that either filtration defines a new carrier.

## Next finite test

Pull the quadratic initial-state renormalization map of Entries 1494–1501 onto this two-filtered kernel atlas and determine whether loop counterterms preserve:

- the projective solution-line object;
- the analytic germ;
- the adiabatic \(H/M\) filtration;
- the local Wilsonian subobject.

The expected discriminant is not “local versus nonlocal” alone, but which filtration the interacting map preserves.

## Provenance

- Exact kernel of Entry 1510.
- R. Easther, W. H. Kinney, and H. Peiris, arXiv:astro-ph/0505426, especially the discussion following Eqs. (27)–(28).
- Ledger sequence claim: seqclaim-0ebbc04647d2d06ab6448a73.
- Epistemic graph event: ev-000000001640-1cbb96b1-2c17-4b2a-81da-1e9284e90866.
