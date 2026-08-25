# Positive symmetric powers fix prime signs but do not orient completion

Author: `marici.Nima`

## 1. The finite question

After labelled prime transport is closed, the remaining finite question is:

\[
\text{Which source operation forbids sign-changing edge weights while
commuting with prime transport and completion?}
\]

The actual finite-place answer is the positive symmetric-power, or bosonic
Fock, operation.  It distinguishes an honest local Euler source from a
virtual signed perturbation.  It does **not** orient the completed Weil form.

## 2. Honest local source

Give the unramified prime label \(p\) a one-dimensional positive generator
\(V_p\), and form

\[
\operatorname{Sym}(V_p)=\bigoplus_{k\ge0}\operatorname{Sym}^k(V_p).
\]

With \(x=p^{-s}\), its graded trace is

\[
Z_p(x)=\sum_{k\ge0}x^k=\frac1{1-x}.
\]

The plethystic logarithm recovers the primitive positive generator,

\[
\operatorname{PLog}Z_p=x,
\]

while the ordinary logarithm generates its Adams/prime-power orbit,

\[
\log Z_p(x)=\sum_{k\ge1}\frac{x^k}{k}.
\]

Applying \(-\partial_s\) gives

\[
-\partial_s\log Z_p(p^{-s})
=\sum_{k\ge1}(\log p)p^{-ks}.
\]

Hence every connected prime-power coefficient is

\[
\Lambda(p^k)=\log p>0.
\]

The sign is not inferred from zeros, Herglotz positivity, or the Weil
criterion.  It is forced by an honest positive generator followed by
symmetric powers.

## 3. Adams coherence and labelled transport

The Adams operation \(\psi^k\) sends the primitive label \(x_p\) to
\(x_p^k\).  On the labelled module this is the transport

\[
e_p\longmapsto e_{p^k}.
\]

Thus symmetric-power formation commutes with prime-power transport:

\[
\log\operatorname{Sym}(V_p)
=\sum_{k\ge1}\frac{\psi^k[V_p]}{k}.
\]

It does not create a primitive at \(pq\) for distinct primes.  The state
\(e_{pq}\) may occur as a tensor/path state in
\(\operatorname{Sym}(V_p)\otimes\operatorname{Sym}(V_q)\), but its
plethystic logarithm has no mixed primitive term.  This is exactly the typing
needed to retain \(\Lambda(pq)=0\).

## 4. Exact hostile-source exclusion

A sign-reversed local edge would require a negative primitive multiplicity.
For the smallest hostile source,

\[
\widetilde Z_p(x)=\operatorname{Sym}(-V_p)=1-x.
\]

Its coefficient of \(x\) is negative, so it is not the graded dimension or
positive trace of an honest Hilbert-space source.  More generally,
independently changing one prime-power coefficient breaks the Adams relation
that all \(p^k\) arise from the same primitive \(V_p\).

There is also an exact scalar hostile completion.  Put

\[
H_{N,\varepsilon}(s)
=\exp\!\left(\varepsilon
\left(N^{s-1/2}+N^{1/2-s}\right)\right).
\]

Then

\[
H_{N,\varepsilon}(1-s)=H_{N,\varepsilon}(s),
\]

and the factor is entire and zero-free for every real \(\varepsilon\).
Negative \(\varepsilon\) reverses the paired local current while preserving
the scalar functional equation.  It is excluded by positive symmetric-power
provenance, not by reciprocal symmetry or scalar completion.

## 5. Endpoint character and coupled cancellation

Let \(\epsilon(e_r)=1\) be the augmentation character.  The correct
endpoint-vanishing edge directions are

\[
d_N=e_1-e_N\in\ker\epsilon.
\]

They obey the exact path relation

\[
d_{MN}=d_M+S_Md_N=d_N+S_Nd_M.
\]

This simultaneously:

1. makes every edge defect vanish at the endpoint character;
2. retains \(e_{pq}\) as a path state;
3. leaves its connected primitive coefficient zero when \(p\ne q\).

The source operation therefore commutes with labelled transport and with the
algebraic endpoint cancellation.  Completion still requires the one coupled
counterterm

\[
C_Y=Q_{\rm endpoint+gamma}^{(Y)}-2A_YI.
\]

Positive symmetric powers determine \(a_{p^k}>0\), hence the sign of the
edge-energy summands.  They impose no sign on \(C_Y\), no monotonicity of
\(C_Y\) in \(Y\), and no positivity of its renormalized limit.

## 6. Disposition

The finite question has a precise but insufficient answer:

\[
\boxed{
\text{positive symmetric powers forbid signed prime weights,
but do not orient the completed form}.}
\]

After this source operation is imposed, the only remaining sign problem is
the coupled endpoint--gamma renormalization.  Proving its completed
orientation is the RH-equivalent Weil/Pick problem unless a new source law
controls \(C_Y\) before scalar projection.

Therefore the prime-transport orientation programme closes.  It delivered:

- exact arithmetic provenance;
- infinite labelled transport closure;
- preservation of connected-versus-path typing;
- a source-local exclusion of signed prime weights; and
- no independent orientation mechanism for the completed kernel.

It should not be enlarged or repackaged as an RH explanation.
