# Half-offset decay is RH-equivalent after divisor factorization

## Scope

This packet audits the explanatory status of the weighted residual gate after
the completed divisor has already been extracted. It does not claim a new
proof of RH.

## Divisor-side signal

Center the critical strip at the seam and write an off-seam zero pair with
horizontal displacement \(a\), where \(0<a<1/2\), and vertical frequency
\(b\). Its two-sided Poisson/Fourier contribution contains a mode of the form

\[
r_{a,b}(x)=e^{-a|x|}e^{-ibx}.
\]

For \(0\leq\alpha<1/2\), define the residual seminorm

\[
\|r\|_\alpha=\sup_{x\in\mathbb R}e^{\alpha|x|}|r(x)|.
\]

The elementary calculation is exact:

\[
\|r_{a,b}\|_\alpha<\infty
\quad\Longleftrightarrow\quad
\alpha\leq a.
\]

Consequently, every off-seam mode fails at least one authorized seminorm:
choose \(a<\alpha<1/2\). A mode whose first legal decay rate is \(1/2\)
passes every seminorm with \(\alpha<1/2\).

## The audit verdict

Once the residual has been decomposed into divisor modes, the assertion

\[
r\in\bigcap_{0\leq\alpha<1/2}L^\infty(e^{\alpha|x|}dx)
\]

excludes exactly the off-seam decay rates. Subject to the already-declared
divisor expansion and absence of cancellations between identical frequencies,
this is RH expressed as Fourier decay. It is a sharp detector, not an
independent orientation law.

The same warning applies to any norm, spectral gap, or completion statement
whose proof first factors the completed section or inspects its zero divisor.
Such a statement may be equivalent, useful, and computationally hostile
without explaining why the source satisfies it.

## What remains noncircular

The source-side problem is narrower and stronger. Construct the coupled
low-grade packet before divisor factorization:

- primitive Euler grade;
- square Euler grade;
- endpoint correction;
- gamma correction;
- seam current;
- projective-infinity current.

Then prove directly from their labelled bonding maps that the resulting
residual belongs to every weighted space below the half-offset. The proof may
not divide by the completed section, invoke Hardy/Blaschke factorization,
inspect zero locations, assume Herglotz positivity, or use the Weil/Pick
criterion.

The connected grades \(k\geq3\) have already passed a stronger uniform Bohr
gate. Therefore all RH-bearing content of this route is concentrated in the
coupled low-grade packet above.

## Finite falsifier

Keep the same harmless almost-periodic channel and compare

\[
r_{\mathrm{safe}}(x)=e^{-|x|/2},
\qquad
r_{\mathrm{hostile}}(x)=e^{-|x|/2}+e^{-|x|/4}\cos(bx).
\]

At any sequence of points where \(|\cos(bx)|=1\), the hostile term makes the
\(\alpha=0.49\) weighted magnitude grow exponentially. The safe residual is
bounded. Hence the low-grade packet alone can change the verdict while the
already-closed connected Euler tail remains identical.

## Decision

Do not treat the half-offset weighted norm as the missing RH explanation after
divisor factorization. Retain it as the exact acceptance test for a future
pre-divisor source theorem. If no source-local proof controls the coupled
low-grade bonding maps, this route closes at an RH-equivalent reformulation.

