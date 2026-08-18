const P: i64 = 32_003;

fn mm(a: i64, b: i64) -> i64 {
    ((a as i128 * b as i128) % P as i128) as i64
}

fn quartic(x: i64, y: i64, z: i64) -> (i64, i64, i64, i64) {
    let e = (x + y + z).rem_euclid(P);
    let a = mm((x - y - z).rem_euclid(P), (x - y + z).rem_euclid(P));
    let b = mm((x + y - z).rem_euclid(P), e);
    let q = (4 * mm(a, b) - mm((a + b - mm(e, e)).rem_euclid(P), (a + b - mm(e, e)).rem_euclid(P))).rem_euclid(P);
    (q, a, b, e)
}

fn main() {
    let mut found = 0;
    for x in 2_i64..20 {
        for y in 2_i64..20 {
            for z in 1_i64..P {
                let (q, a, b, e) = quartic(x, y, z);
                if q == 0 && a != 0 && b != 0 && e != 0 && x != y && x != z && y != z {
                    println!("schema=generic-q-zero-point-v1 field={P} x={x} y={y} z={z} Q={q} A={a} B={b} E={e}");
                    found += 1;
                    if found == 3 { return; }
                    break;
                }
            }
        }
    }
    panic!("fewer than three generic nonsoft Q-zero points found");
}
