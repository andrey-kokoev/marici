#[cfg(not(feature = "replication-prime"))]
const P: u64 = 2_305_843_009_213_693_951;
#[cfg(feature = "replication-prime")]
const P: u64 = 2_305_843_009_213_693_921;
const ORDER: usize = 25;

#[derive(Clone, Copy)]
struct Series([u64; ORDER]);

fn add(a: u64, b: u64) -> u64 {
    let (s, c) = a.overflowing_add(b);
    if c || s >= P {
        s.wrapping_sub(P)
    } else {
        s
    }
}
fn sub(a: u64, b: u64) -> u64 {
    if a >= b {
        a - b
    } else {
        P - (b - a)
    }
}
fn mul(a: u64, b: u64) -> u64 {
    ((a as u128 * b as u128) % P as u128) as u64
}
fn pow(mut a: u64, mut n: u64) -> u64 {
    let mut r = 1;
    while n > 0 {
        if n & 1 == 1 {
            r = mul(r, a)
        }
        a = mul(a, a);
        n >>= 1;
    }
    r
}
fn inv_scalar(a: u64) -> u64 {
    pow(a, P - 2)
}

impl Series {
    fn constant(x: u64) -> Self {
        let mut a = [0; ORDER];
        a[0] = x % P;
        Self(a)
    }
    fn linear(c: u64, slope: u64) -> Self {
        let mut a = [0; ORDER];
        a[0] = c % P;
        a[1] = slope % P;
        Self(a)
    }
    fn add(self, rhs: Self) -> Self {
        let mut r = [0; ORDER];
        for i in 0..ORDER {
            r[i] = add(self.0[i], rhs.0[i]);
        }
        Self(r)
    }
    fn sub(self, rhs: Self) -> Self {
        let mut r = [0; ORDER];
        for i in 0..ORDER {
            r[i] = sub(self.0[i], rhs.0[i]);
        }
        Self(r)
    }
    fn mul(self, rhs: Self) -> Self {
        let mut r = [0; ORDER];
        for i in 0..ORDER {
            for j in 0..ORDER - i {
                r[i + j] = add(r[i + j], mul(self.0[i], rhs.0[j]));
            }
        }
        Self(r)
    }
    fn inv(self) -> Self {
        let mut r = [0; ORDER];
        r[0] = inv_scalar(self.0[0]);
        for n in 1..ORDER {
            let mut s = 0;
            for i in 1..=n {
                s = add(s, mul(self.0[i], r[n - i]));
            }
            r[n] = sub(0, mul(r[0], s));
        }
        Self(r)
    }
    fn neg(self) -> Self {
        Series::constant(0).sub(self)
    }
    fn valuation(self) -> usize {
        self.0.iter().position(|x| *x != 0).unwrap_or(ORDER)
    }
}

fn permutations3() -> Vec<[usize; 3]> {
    vec![
        [2, 3, 4],
        [2, 4, 3],
        [3, 2, 4],
        [3, 4, 2],
        [4, 2, 3],
        [4, 3, 2],
    ]
}
fn permutations6() -> Vec<[usize; 6]> {
    fn rec(k: usize, a: &mut [usize; 6], out: &mut Vec<[usize; 6]>) {
        if k == 6 {
            out.push(*a);
            return;
        }
        for i in k..6 {
            a.swap(k, i);
            rec(k + 1, a, out);
            a.swap(k, i);
        }
    }
    let mut out = Vec::new();
    let mut a = [0, 1, 2, 3, 4, 5];
    rec(0, &mut a, &mut out);
    out
}
fn parity(p: &[usize; 6]) -> bool {
    let mut n = 0;
    for i in 0..6 {
        for j in i + 1..6 {
            n += usize::from(p[i] > p[j]);
        }
    }
    n % 2 == 1
}
fn index_pair(i: usize, j: usize) -> usize {
    match (i.min(j), i.max(j)) {
        (2, 3) => 3,
        (2, 4) => 4,
        (3, 4) => 5,
        _ => panic!(),
    }
}

fn entry(alpha: [usize; 3], beta: [usize; 3], vars: [Series; 6]) -> Series {
    let mut pos = [0usize; 5];
    for (i, x) in beta.iter().enumerate() {
        pos[*x] = i;
    }
    let mut result = Series::constant(1);
    for t in 0..3 {
        let i = alpha[t];
        let mut mon = vars[i - 2];
        for j in alpha.iter().skip(t + 1) {
            if pos[i] > pos[*j] {
                mon = mon.mul(vars[index_pair(i, *j)]);
            }
        }
        result = result.mul(mon.sub(mon.inv()));
    }
    result
}
fn determinant(vars: [Series; 6]) -> Series {
    let basis = permutations3();
    let matrix: Vec<Vec<Series>> = basis
        .iter()
        .map(|a| basis.iter().map(|b| entry(*a, *b, vars)).collect())
        .collect();
    let mut det = Series::constant(0);
    for p in permutations6() {
        let mut term = Series::constant(1);
        for r in 0..6 {
            term = term.mul(matrix[r][p[r]]);
        }
        det = det.add(if parity(&p) { term.neg() } else { term });
    }
    det
}

fn monomial(vars: [Series; 6], mask: [bool; 6]) -> Series {
    let mut r = Series::constant(1);
    for i in 0..6 {
        if mask[i] {
            r = r.mul(vars[i]);
        }
    }
    r
}
fn predicted(vars: [Series; 6], letters: &[(&str, [bool; 6], usize)]) -> Series {
    let mut r = Series::constant(1);
    for (_, mask, e) in letters {
        let m = monomial(vars, *mask);
        let s = m.sub(m.inv());
        for _ in 0..*e {
            r = r.mul(s);
        }
    }
    r
}

fn probe(mask: [bool; 6], branch: u64, seed: u64) -> usize {
    let constants = [
        3 + seed,
        5 + seed,
        7 + seed,
        11 + seed,
        13 + seed,
        17 + seed,
    ];
    let pivot = mask.iter().position(|x| *x).unwrap();
    let mut product = 1;
    for i in 0..6 {
        if mask[i] && i != pivot {
            product = mul(product, constants[i] % P);
        }
    }
    let base = mul(branch, inv_scalar(product));
    let slope = inv_scalar(product);
    let mut vars = [Series::constant(0); 6];
    for i in 0..6 {
        vars[i] = Series::constant(constants[i] % P);
    }
    vars[pivot] = Series::linear(base, slope);
    determinant(vars).valuation()
}

fn main() {
    let letters = [
        ("x2", [true, false, false, false, false, false], 2usize),
        ("x3", [false, true, false, false, false, false], 2),
        ("x4", [false, false, true, false, false, false], 2),
        ("y23", [false, false, false, true, false, false], 2),
        ("y24", [false, false, false, false, true, false], 2),
        ("y34", [false, false, false, false, false, true], 2),
        ("y23y24y34", [false, false, false, true, true, true], 1),
        ("x2x3y23", [true, true, false, true, false, false], 1),
        ("x2x4y24", [true, false, true, false, true, false], 1),
        ("x3x4y34", [false, true, true, false, false, true], 1),
        ("x2x3x4y23y24y34", [true, true, true, true, true, true], 2),
    ];
    let mut total = 0;
    println!("{{\"schema\":\"marici.benincasa.string_six_point_dense_kernel.v1\",\"prime\":{P},\"letters\":[");
    for (i, (name, mask, expected)) in letters.iter().enumerate() {
        let plus = probe(*mask, 1, 0);
        let minus = probe(*mask, P - 1, 2);
        assert_eq!(plus, minus);
        assert_eq!(plus, *expected);
        total += plus;
        println!(
            "{}{{\"letter\":\"{}\",\"valuation_plus\":{},\"valuation_minus\":{}}}",
            if i == 0 { "" } else { "," },
            name,
            plus,
            minus
        );
    }
    let mut ratios = Vec::new();
    for seed in 0..6 {
        let c = [
            3 + seed,
            5 + seed,
            7 + seed,
            11 + seed,
            13 + seed,
            17 + seed,
        ];
        let vars = c.map(|x| Series::constant(x));
        let d = determinant(vars).0[0];
        let q = predicted(vars, &letters).0[0];
        ratios.push(mul(d, inv_scalar(q)));
    }
    assert!(ratios.iter().all(|x| *x == ratios[0]));
    println!("],\"total_valuation\":{},\"expected_total_degree\":18,\"constant_quotient\":{},\"quotient_samples\":6,\"complete\":{}}}",total,ratios[0],total==18);
}
