use std::hint::black_box;

fn pow4(base: u64, exponent: u64) -> u64 {
    match exponent {
        0 => 1,
        1 => base,
        2 => base * base,
        _ => base * base * base,
    }
}

fn monomial(code: u64, x: u64, y: u64) -> u64 {
    let x_exp = code % 4;
    let quotient = code / 4;
    let y_exp = quotient % 4;
    let sum_exp = quotient / 4;
    pow4(x, x_exp) * pow4(y, y_exp) * pow4(x + y, sum_exp)
}

fn target(kind: u64, x: u64, y: u64) -> u64 {
    match kind {
        0 => 1,
        1 => x,
        2 => y,
        _ => x * y,
    }
}

fn signature_matches(code: u64, kind: u64) -> bool {
    (0..16).all(|point| {
        let x = point % 4 + 1;
        let y = point / 4 + 2;
        monomial(code, x, y) == target(kind, x, y)
    })
}

fn main() {
    let result: Vec<(u64, u64)> = (0..4)
        .map(|kind| {
            (0..(1_u64 << 16))
                .fold((0, 0), |(count, sum), prefix| {
                    let code = prefix % 64;
                    if signature_matches(code, kind) {
                        (count + 1, sum + code)
                    } else {
                        (count, sum)
                    }
                })
        })
        .collect();
    println!("{:?}", black_box(result));
}
