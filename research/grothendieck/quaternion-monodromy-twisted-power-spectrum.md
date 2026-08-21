# Quaternion-monodromy twisted power spectrum

## General sufficient condition

Let a finite group `M` act on an arbitrary finite group `K`.  If

`gcd(n,exp(K)*exp(M))=1`,

then the `n`-th power correspondence on `K semidirect M -> M` is compatible
with every fiber sum and fiber lift.  Indeed, the condition is coprime to the
exponent of the total semidirect product, so its global power map is a
permutation; the quotient power map on `M` is also a permutation.  The
restriction to each fiber is therefore a bijection onto the corresponding
target fiber.

For arbitrary nonabelian `K`, necessity of every visible monodromy prime is a
separate twisted-word question; the abelian proof by linear norms does not
apply automatically.

## First nonabelian monodromy control

Let `C3` act on `Q8` by cyclically permuting `i,j,k`.  For

`Q8 semidirect C3 -> C3`,

exact enumeration through index 24 gives global fiber compatibility exactly
when

`gcd(n,4*3)=1`.

Thus the first nonabelian-kernel monodromy control detects both the kernel
prime two and visible action prime three, agreeing with the product-exponent
spectrum.

## Scope and falsifier

The sufficient theorem is general.  The converse is proved here only for the
specific quaternion control by exhaustive finite enumeration.  A faithful
nonabelian-kernel action whose fiber spectrum omits a visible monodromy prime
would falsify the general converse, not the sufficient direction.  No ring
Adams operation or physical chain transfer is asserted.

