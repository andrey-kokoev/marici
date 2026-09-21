# Window arithmetic defects are transported-tail boundaries, not feature-cutoff commutators

## Result

The window residual has an exact source-defined boundary formula using the already prescribed four oriented tails. It satisfies a transport equation, is additive under refinement, and has uniform compact-spectral bounds including total variation over arbitrarily fine partitions.

Thus existing transported tail data captures the defect. It is not determined by finitely many local endpoint jets on the general forcing domain, and forcing localization is not multiplication by a cutoff in the arithmetic operator's feature coordinate.

This explains the failed even-port attachment comparison without fitting a correction to a Gram matrix. It does not identify the residual with an arithmetic gamma/prime channel or establish semilocal operator equivalence.

Inputs:

- `window-moment-defects-obstruct-the-even-port-arithmetic-attachment-comparison.md`;
- `../voevodsky/clark-source-interface-domain-and-positivity-audit.md`;
- `../voevodsky/a-subtracted-gamma-shift-operator-completes-the-one-slot-euler-green-form.md`.

## 1. Start with the existing four tails

For f in H_beta and sigma=+/- define

`G_(sigma,j)(z;a)=integral_a^infinity exp(sigma i z(x-a)) x^j f(x) dx`, j=0,1.

Their source ODE is

`partial_a G_(sigma,j)=-sigma i z G_(sigma,j)-a^j f(a)`.

Remove the transport phase only to express their endpoint traces:

`H_(sigma,j)(z;a)=exp(sigma i z a) G_(sigma,j)(z;a)`.

Then partial_a H_(sigma,j)=-a^j exp(sigma i z a) f(a). In particular put

`C_f(z;a)=[H_(+,0)+H_(-,0)]/2`,

`M_f(z;a)=[H_(-,1)-H_(+,1)]/2`.

These are respectively the cosine tail and the tail of -i x sin(zx)f(x). At a=0 they are the even trace X_f and the moment trace i X_f'.

Let L_z=L(1/2-i z) be the independently prescribed Euler arithmetic multiplier. Define the transported residual state

`B_f(z;a)=M_f(z;a)-L_z C_f(z;a)`.

It is a fixed linear combination of the existing tail state and the already fixed arithmetic multiplier. No window-dependent Green metric or independently adjustable forcing channel is introduced.

## 2. Transport equation and exact window formula

Set

`r_z(x)=-i x sin(zx)-L_z cos(zx)`.

The tail ODE gives

`partial_a B_f(z;a)=-r_z(a) f(a)`,

`B_f(z;infinity)=0`.

Consequently, for the forcing window f_[a,b]=1_[a,b] f,

`R_(f_[a,b])(z)=i X_(f_[a,b])'(z)-L_z X_(f_[a,b])(z)
 = B_f(z;a)-B_f(z;b)`.

This derives the residual from actual tail transport. At a new internal cut c,

`R_[a,b]=R_[a,c]+R_[c,b]`

because the SAME transported B_f(z;c) occurs with opposite signs. Resetting that state at each cut would destroy the identity.

For the prepared full theta state, the admitted arithmetic graph identity says B_Phi(z;0)=0; the infinity state also vanishes. Interior states need not vanish. The full-state identity is therefore consistent with nonzero individual window defects.

## 3. An operator-valued boundary trace and bounds

Fix a compact Euler spectral set K with

`gamma<eta<=Im z<=Y<beta`, `|z|<=Z`.

Put epsilon=beta-Y>0, delta=eta-gamma>0, and L_K=sup_K |L_z|. This is finite on the Euler chart. Let e_z(u)=exp(i z u), and use the arithmetic graph domain D_gamma with unrestricted endpoint trace.

Define

`mathcal B_a(f)(z)=sqrt(2) B_f(z;a) e_z`.

This is a linear map into C(K;D_gamma). Since

`||e_z||_(D_gamma)<=sqrt(1+Z^2)/sqrt(2 delta)`

and

`|r_z(x)|<=(1+L_K)(1+x) exp(Yx)`,

Cauchy--Schwarz gives

`||mathcal B_a(f)||_(C(K;D_gamma))
 <= C_K exp(-epsilon a) ||f||_beta`,

where

`C_K=(1+L_K)sqrt(1+Z^2)/sqrt(2 epsilon delta)`.

The same estimate controls total variation on the tail. For any finite partition a=a_0<...<a_N=b,

`sum_i ||mathcal B_(a_i)(f)-mathcal B_(a_(i+1))(f)||_(C(K;D_gamma))
 <= C_K exp(-epsilon a) ||f||_beta`.

Indeed each increment is the integral of its source density, and the sum is bounded by the integral of the uniform density majorant on [a,b]. This avoids a partition-size constant. The resulting transport state is locally absolutely continuous; its differential identity holds almost everywhere for general H_beta forcings.

The operator-valued defect of a window is exactly

`W_(f_[a,b])-L_ar U_(f_[a,b])
 =mathcal B_a(f)-mathcal B_b(f)`.

Thus it has the declared arithmetic graph-domain meaning, rather than being merely a scalar identity at sampled spectral points.

## 4. Why a feature-cutoff commutator is a different operation

For a bounded Lipschitz function chi of the FEATURE coordinate u,

`[T_h,M_chi]g(u)=[chi(u+h)-chi(u)]g(u+h)`.

On the arithmetic graph core this gives an actual commutator formula for L_ar=U+G-V. The gamma part is

`[G,M_chi]g
 =-(1/2) integral_0^infinity exp(-t/4)
   [chi(u+t/2)-chi(u)] T_(t/2)g / [1-exp(-t)] dt`.

The identity terms commute, and the Lipschitz difference cancels the small-t singularity. Put M=||chi||_infinity, H=||chi'||_infinity and c=1/4+gamma/2. The integral estimates give a bounded extension on H_gamma with

`||[L_ar,M_chi]||
 <=2M(||U||+||V||)+e H/4
   +M exp(-c)/[c(1-exp(-1))]`.

The U and V terms use their existing absolutely convergent shift constructions. Multiplication by such chi preserves D_gamma, so the commutator identity is justified first there and then extended by the bound.

But this is NOT forcing localization. At a fixed z,

`U_z(chi f)=sqrt(2) X_(chi f)(z)e_z`

is still a scalar multiple of the whole exponential state, whereas

`M_chi U_z(f)=sqrt(2) X_f(z) chi(u)e_z(u)`

is generally not. If a feature multiplier intertwined every forcing-window multiplication at z=i y, nonzero X_f would force that feature multiplier to be constant. Requiring the identity for all f would then force the forcing multiplier to be the same constant, since cosh(yx)>0. A nontrivial window cannot satisfy this.

A sharp characteristic cutoff in u also need not preserve D_gamma: its jumps can create distributional derivatives. Neither changing coordinates silently nor ignoring that graph-domain issue supplies the desired window commutator.

## 5. Transported boundary state is not a finite local endpoint jet

The boundary formula uses tails extending beyond each cut, not merely values of f and its derivatives at a and b.

There can be no universal finite-endpoint-jet formula for R_[a,b] on the admitted forcing domain. Fix z=i y in the Euler chart. The density becomes

`r_(i y)(x)=cosh(yx)[x tanh(yx)-L(1/2+y)]`.

Its bracket is strictly increasing and is not identically zero on an interval. Choose a nonnegative smooth bump supported strictly inside a subinterval where this density has one nonzero sign. Every endpoint derivative of that bump is zero, but its residual integral is nonzero.

This rules out even a universal formula using all endpoint jets for general smooth forcings without their transported state. It does not rule out additional special identities for the one fixed theta function. What is already available, without such an identity, is the explicit four-tail boundary state above.

## 6. Relation to the paired attachment

The previous exact form defect was

`Delta(f,g;w,z)=2[conjugate(X_f(w)) R_g(z)
                    +conjugate(R_f(w)) X_g(z)]/[-i(z-conjugate(w))]`.

For window forcings, insert the transported boundary differences from section 2. Every spectral denominator, actual edge label and moment port remains attached to its slot. The boundary states telescope under chamber refinement and have the uniform variation control in section 3.

This does not make Delta zero. It identifies the missing data when the two Clark sheets are replaced by the single even port together with the arithmetic graph condition. Retaining the moment port, or equivalently U together with W-L_ar U, retains the already existing source information. It is not an independently fitted arithmetic channel.

A full semilocal operator comparison or an arithmetic interpretation of this residual remains separate. In particular the bulk/forcing tail-current split has not been relabelled gamma/prime.

## Verification

`uv run --with sympy python research/nima/checkers/check_window_residual_tail_transport.py`

The checker verifies the phased tail ODE calculation, its residual source density, refinement telescoping, and the feature-translation commutator identity. The compact-spectral operator bounds and the no-local-jet argument are the proofs above.
