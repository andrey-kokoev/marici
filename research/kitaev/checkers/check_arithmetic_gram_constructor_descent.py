#!/usr/bin/env python3
"""Exact adjacent-collapse and discrete-port compiler for Gram constructors."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "kitaev" / "results" / "arithmetic-gram-constructor-descent.json"


def is_prime_power(n: int) -> bool:
    factors = sp.factorint(n)
    return len(factors) == 1


def patterns(labels: range, constructors: dict[str, callable]) -> set[tuple[int, ...]]:
    return {tuple(int(fn(n)) for fn in constructors.values()) for n in labels}


def main() -> None:
    a0, ad, fn, fn1 = sp.symbols("A0 Ad f_n f_n1", real=True)
    input_norm = sp.expand(2 * (a0 - ad))
    output_norm = sp.expand(a0 * (fn1**2 + fn**2) - 2 * fn1 * fn * ad)
    decomposition = sp.expand(a0 * (fn1 - fn) ** 2 + 2 * fn1 * fn * (a0 - ad))
    assert sp.expand(output_norm - decomposition) == 0

    # Exact persistent-jump outputs.
    parity_output = sp.expand(output_norm.subs({fn: 1, fn1: -1}))
    divisibility_output = sp.expand(output_norm.subs({fn: 0, fn1: 1}))
    assert parity_output == 2 * (a0 + ad)
    assert divisibility_output == a0

    parity_pairs = [(n, n + 1) for n in range(1, 9)]
    div3_pairs = [(3 * k - 1, 3 * k) for k in range(1, 9)]
    prime_pairs = [(p - 1, p) for p in list(sp.primerange(5, 50))[:8]]
    prime_power_pairs = [(2 ** (2 * m) - 1, 2 ** (2 * m)) for m in range(2, 10)]
    for left, right in parity_pairs:
        assert (-1) ** left != (-1) ** right
    for left, right in div3_pairs:
        assert left % 3 != 0 and right % 3 == 0
    for left, right in prime_pairs:
        assert not sp.isprime(left) and sp.isprime(right)
    for left, right in prime_power_pairs:
        assert not is_prime_power(left) and is_prime_power(right)
        m = int(math.log2(right)) // 2
        assert left == (2**m - 1) * (2**m + 1)
        assert math.gcd(2**m - 1, 2**m + 1) == 1

    # Finite discrete-port synthesis on a certified horizon.
    families = {
        "parity": {"parity": lambda n: n % 2},
        "divisible_by_3": {"div3": lambda n: n % 3 == 0},
        "parity_and_div3": {"parity": lambda n: n % 2, "div3": lambda n: n % 3 == 0},
        "prime_and_prime_power": {"prime": sp.isprime, "prime_power": is_prime_power},
    }
    port_results = {}
    for name, constructors in families.items():
        pats = patterns(range(2, 101), constructors)
        port_results[name] = {
            "realized_patterns": [list(p) for p in sorted(pats)],
            "pattern_count": len(pats),
            "minimum_binary_bits_on_horizon": math.ceil(math.log2(len(pats))),
        }
    assert port_results["parity"]["minimum_binary_bits_on_horizon"] == 1
    assert port_results["divisible_by_3"]["minimum_binary_bits_on_horizon"] == 1
    assert port_results["parity_and_div3"]["minimum_binary_bits_on_horizon"] == 2
    assert port_results["prime_and_prime_power"]["pattern_count"] == 3
    assert port_results["prime_and_prime_power"]["minimum_binary_bits_on_horizon"] == 2

    result = {
        "schema": "marici.kitaev.arithmetic-gram-constructor-descent.v1",
        "adjacent_formula": {
            "input_norm_squared": "2(A0-A(delta_n)) -> 0",
            "output_norm_squared": "A0|f(n+1)-f(n)|^2 + 2 Re(conj(f(n+1))f(n))(A0-A(delta_n))",
            "necessary_for_bounded_descent_when_f_is_bounded": "f(n+1)-f(n) -> 0",
        },
        "non_descent_witnesses": {
            "parity": {"pairs": parity_pairs, "jump_magnitude": 2, "output_limit": "4A0"},
            "divisible_by_3": {"pairs": div3_pairs, "jump_magnitude": 1, "output_norm_squared": "A0"},
            "prime_type": {"pairs": prime_pairs, "infinite_proof": "for every prime p>3, p-1 is composite; infinitely many primes exist", "jump_magnitude": 1},
            "prime_power_type": {"pairs": prime_power_pairs, "infinite_proof": "2^(2m)-1=(2^m-1)(2^m+1) has coprime nontrivial factors for m>=2, while 2^(2m) is a prime power", "jump_magnitude": 1},
        },
        "mellin_control": {
            "constructor": "f_t(n)=n^(it)",
            "bound": "|(n+1)^(it)-n^(it)| <= |t| log(1+1/n) <= |t|/n",
            "adjacent_condition_passes_for_fixed_t": True,
            "full_Gram_boundedness_proved": False,
        },
        "full_descent_criterion": {
            "finite_kernel": "K_N=(K(n,m))",
            "diagonal": "D_f,N=diag(f(1),...,f(N))",
            "necessary_and_sufficient": "exists C independent of N with D_f,N^* K_N D_f,N <= C^2 K_N for every N",
            "adjacent_continuity_is_sufficient": False,
        },
        "first_invalid_constructor": {
            "code": "arithmetic_constructor_does_not_descend_to_gram_completion",
            "constructor": "parity",
            "labels": [1, 2],
            "input_gram_norm_squared": "2(A0-A(log 2)); asymptotic copies use (n,n+1) and tend to 0",
            "output_gram_norm_squared": "2(A0+A(log(1+1/n))) -> 4A0",
            "adjacent_value_jump": 2,
            "requires_discrete_port": True,
        },
        "discrete_port_compiler": {
            "rule": "quotient labels by equality of all admitted non-descending constructor attributes; encode the realized joint patterns",
            "finite_horizon_2_to_100": port_results,
            "typed_prime_power_label": "a Boolean port suffices only for the predicate; constructors using base or exponent require those typed values",
        },
        "authority_trichotomy": {
            "descends": "no new port required for this constructor",
            "fails_to_descend": "retain a jointly faithful discrete source port if the constructor is admitted",
            "not_operative": "no authority to demand preservation",
        },
        "verdict": "Adjacent collapse forbids every bounded admitted diagonal constructor with persistent adjacent jumps. Parity, fixed-prime divisibility, prime type, and prime-power type have exact infinite witnesses; fixed Mellin characters pass the necessary adjacent test but still require the global kernel inequality. Minimal discrete repair is the code of joint values of the admitted non-descending attributes, not a universal copy of the integer label.",
    }
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
