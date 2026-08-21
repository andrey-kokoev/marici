# Endpoint and zeta pole form an acyclic resolvent pair before positivity

Put `s=1/2+sqrt(x)`. The two elementary completed factors contribute

```
[1/s+1/(s-1)]/(2s-1)=1/[s(s-1)]=1/(x-1/4).           (1)
```

Thus the endpoint heat atom `e^(t/4)` is the resolvent pole at `x=1/4`, or
spectral value `lambda=-1/4` in the convention `1/(x+lambda)`.

Near `s=1`, write `epsilon=s-1`. The zeta logarithmic derivative has

```
zeta'(s)/zeta(s)=-1/epsilon+gamma_0+O(epsilon).        (2)
```

Its squared-coordinate contribution is

```
[-1/epsilon+gamma_0+O(epsilon)]/(1+2epsilon).          (3)
```

The polar parts of (1) and (3) cancel:

```
1/[epsilon(1+epsilon)]-1/[epsilon(1+2epsilon)]
=1/[(1+epsilon)(1+2epsilon)].                         (4)
```

Hence the completed sum is regular at `x=1/4`. The forbidden endpoint atom is
not part of the final spectral measure.

On the reflected branch `s->0`, the elementary `1/s` pole is instead canceled
by the pole of the gamma factor. The map `x=(s-1/2)^2` identifies the two
branches at `x=1/4`; functional reflection makes the zeta-pole and gamma-pole
descriptions two local presentations of one completed cancellation. Thus the
acyclic pair belongs to the full endpoint--gamma--zeta completion, even though
the `s->1` chart displays the zeta partner most directly.

## Mapping-cone interpretation

In the `s->1` chart, represent the endpoint line and the zeta-pole line as a
two-term complex

```
C_endpoint --identity--> C_pole.                       (5)
```

The complex is acyclic. Its graded resolvent trace is

```
+1/(x-1/4)-1/(x-1/4)=0.                               (6)
```

Regular terms in (4) survive as the finite completed coupling, but the pole
state itself disappears in the quotient. This is a source-derived acyclic
pair: it comes from the canonical factor `(s-1)zeta(s)`, not from inserting a
ghost sector to repair positivity after the fact.

## Consequence for reflection positivity

The endpoint fails the generator-shifted kernel because it was examined before
acyclic reduction. The correct order is:

1. combine endpoint and analytically continued zeta pole;
2. quotient their contractible pole pair;
3. form ordinary and shifted time-addition Grams on the reduced completed
   kernel.

Attempting to realize the prime Dirichlet series as a positive sector before
step 1 is invalid: that series exists only for `Re(s)>1` and does not itself
contain a separately available negative pole atom on the boundary.

## Scope boundary

This proves the algebraic/analytic pole cancellation and supplies a canonical
mapping-cone model for it. It does not construct the physical relative-chain
pushforward, prove positivity of the reduced kernel, or control the remaining
gamma--prime fluctuations. Those stay as the one-time reflection-positivity
gate.
