# High derivatives at one time amplify every hidden off-axis pole

Consider a positive background heat atom and a small conjugate off-axis pair:

```
Theta(t)=A e^(-lambda_0 t)
 +epsilon Re[e^(-(lambda-i b)t)],                     (1)
```

with `A>0`, `lambda_0>0`, `epsilon!=0`, and `b!=0`. Its alternating
derivatives at a fixed `t_0` are

```
D_k(t_0)=A lambda_0^k e^(-lambda_0 t_0)
 +epsilon Re[(lambda-i b)^k e^(-(lambda-i b)t_0)].     (2)
```

Write

```
R=sqrt(lambda^2+b^2),
theta=arg(lambda-i b).                                 (3)
```

The defect amplitude relative to the positive atom is

```
|epsilon|/A * exp[-(lambda-lambda_0)t_0]
                  *(R/lambda_0)^k.                    (4)
```

If `R>lambda_0`, this ratio grows exponentially with derivative order. The
phase `k theta+b t_0+arg(epsilon)` visits a negative cosine sector infinitely
often (periodically or densely), so some `D_k(t_0)` is negative. A hidden
off-axis pair therefore cannot pass the complete derivative hierarchy at one
time even when it leaves `Theta(t)` pointwise positive.

## Detection latency

The amplitude becomes order one near

```
k_detect approximately
 [log(A/|epsilon|)+(lambda-lambda_0)t_0]
 /log(R/lambda_0).                                     (5)
```

An additional bounded phase wait selects a negative cosine. Formula (5) is
the one-time derivative latency. It quantifies why finite derivative checks
cannot prove RH, while the all-order sequence does reject every fixed
off-axis defect.

For an off-critical Xi zero with centered spectral ordinate
`gamma=beta-i alpha`, the squared heat rate is

```
gamma^2=(beta^2-alpha^2)-2i alpha beta,                (6)
```

whose modulus is `alpha^2+beta^2`. Relative to a lower real squared ordinate,
high derivative order eventually amplifies the quartet despite its
`e^[-(beta^2-alpha^2)t_0]` suppression.

## Arithmetic horizon of the Laguerre source

The source expression for `D_k(t_0)` contains
`L_k^(-1/2)(y_n)` with `y_n=(log n)^2/(4t_0)`. Its oscillatory/turning region
has `y_n=O(k)`, hence

```
log n=O(sqrt(k t_0)),
n=exp[O(sqrt(k t_0))].                                 (7)
```

Thus increasing derivative order probes a subexponentially expanding prime
horizon. Making `t_0` small suppresses primes at every fixed order but cannot
make the complete hierarchy an archimedean perturbation uniformly in `k`:
the sensitive prime range inevitably moves outward with order.

This is an explanatory latency theorem, not a finite proof. It shows why the
one-time all-order formulation retains the full divisor information that
order-zero heat positivity lost.
