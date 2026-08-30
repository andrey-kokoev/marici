# 2885 — The Two Internal Bypasses Differ by a Canonical Marked Leray Packet

## Internal collision

Entry 2882 identified the physical collision

\[
x=\frac ap=1,
\qquad
\delta=\xi+\kappa=0.
\]

At fixed \(\delta\ne0\), the complete fiber differential is

\[
\omega
=
\frac1{2p^4(\xi+1)}
\frac{x+1}{(x-1)^2(x+3)\sqrt{k}}
\,dx.
\]

## Exact marked residue

Write

\[
r(x)=\frac{x+1}{x+3}.
\]

Because \(x=1\) is a double pole, its residue is

\[
\operatorname{Res}_{x=1}\omega
=
\frac1{2p^4(\xi+1)}
\left.
\frac d{dx}
\left(\frac{r(x)}{\sqrt{k(x)}}\right)
\right|_{x=1}.
\]

Using

\[
k(1)=16(\kappa+\xi)^2,
\qquad
k'(1)=-16(1+\kappa\xi),
\]

gives

\[
\operatorname{Res}_{x=1}\omega
=
\frac{
(\kappa+\xi)^2+2(1+\kappa\xi)
}
{64p^4(\xi+1)(\kappa+\xi)^3}.
\]

Near the collision,

\[
\operatorname{Res}_{x=1}\omega
\sim
\frac{1+\kappa}
{32p^4(\xi+\kappa)^3}.
\]

This is generically nonzero on \(-1<\kappa<1\).

## Relative-cycle difference

Let \(\Gamma_{\rm above}\) and \(\Gamma_{\rm below}\) be the two local
bypasses of the marked pole, with common endpoints and source orientation.
Their difference is the small Leray tube:

\[
\Gamma_{\rm above}-\Gamma_{\rm below}
=
\tau_{x=1}.
\]

Therefore

\[
I_{\rm above}-I_{\rm below}
=
2\pi i\operatorname{Res}_{x=1}\omega.
\]

The obstruction is thus a canonical supported coefficient packet, not an
arbitrary contour ambiguity.

## Interpretation

The source \(i\epsilon\) prescription selects one affine lift of this
two-route system. It does not make the alternative route equal, and it does
not erase the supported difference.

The architecture is

\[
\text{existing marked incidence}
+
\text{Leray residue coefficient}
+
\text{source boundary-value selection}.
\]

No new carrier cell is required.

## Next falsifier

Transport this local residue packet through the full occurrence atlas and the
relative de Rham/Gysin totalization. Determine whether it survives as a
physical supported costalk or becomes exact after all boundary ports and
orientation maps are included.

## Durable artifacts

- `research/benincasa/check_soft_internal_bypass_leray_difference.py`
- `research/benincasa/soft-internal-bypass-leray-difference.json`

