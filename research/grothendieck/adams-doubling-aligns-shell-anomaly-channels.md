# Adams doubling exactly aligns the linear and quadratic shell defects

> **Scope correction.** The Adams identity and prime-shell phase alignment
> below are exact. They do not identify gamma resolvent dependence with
> shell-center time evolution.

Let the prime-zeta linear channel be

```
C_1(s)=sum_p p^(-s).
```

The quadratic determinant channel is not independent:

```
C_2(s)=(1/2)sum_p p^(-2s)=(1/2)C_1(2s).             (1)
```

On the critical line `s=1/2+iT`, the doubled argument is `2s=1+2iT`.
Thus the quadratic channel at height `T` is one half of the linear prime-zeta
channel on the `Re(s)=1` boundary at height `2T`.

This identity repairs the shell-frequency parity mismatch. The leading
quarter-shifted radial defect of the linear channel at doubled height is

```
L_k(2T)=[sinc(T)-1]e^(-2iTk-iT/2)/k,                (2)
```

which equals the quadratic radial defect `Q_k(T)` exactly. Hence

```
(1/2) L_k(2T) = quadratic determinant contribution.  (3)
```

Every resonance at `T=n pi`, including the odd ones invisible to `L_k(T)`,
is present with the correct phase after Adams doubling.

## Mapping-cone interpretation

The required two-channel object should therefore be the relative cone of the
second Adams map, not a numerical `2x2` coupling at fixed height. Its two legs
live at `s` and `2s`; the coefficient `1/2` is forced by the determinant
logarithm/orbit normalization. The cone can organize shell-compression
artifacts because the defects agree before scalarization; resolved
within-shell data is still required before gamma comparison.

This does not yet continue `C_1` through `Re(s)=1` or produce Xi zeros. It
replaces an impossible same-height cancellation with a source-defined
arithmetic correspondence that has exactly the missing frequency content.
The next gate is to combine this Adams cone with the gamma/endpoint reference
so that its common logarithmic singularity at `2s=1` receives a canonical
finite part and the resulting determinant remains reflection compatible.

## Falsifier

A two-channel proposal fails if it couples `C_1(s)` directly to `C_2(s)` as
same-height scalars and omits the map `s->2s`. Such a model cannot see the odd
quadratic shell resonances. Conversely, invoking Adams doubling without the
forced factor `1/2` fails the finite Euler logarithm.
