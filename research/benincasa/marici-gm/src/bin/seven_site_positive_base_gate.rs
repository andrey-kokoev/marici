use serde_json::{json, Value};
use std::{collections::BTreeSet, fs};

const N: usize = 7;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rat {
    n: i128,
    d: i128,
}
impl Rat {
    fn new(mut n: i128, mut d: i128) -> Self {
        assert_ne!(d, 0);
        if d < 0 {
            n = -n;
            d = -d
        }
        let (mut a, mut b) = (n.unsigned_abs(), d as u128);
        while b != 0 {
            let r = a % b;
            a = b;
            b = r
        }
        let g = a as i128;
        Self { n: n / g, d: d / g }
    }
    fn z() -> Self {
        Self { n: 0, d: 1 }
    }
    fn o() -> Self {
        Self { n: 1, d: 1 }
    }
    fn add(self, x: Self) -> Self {
        Self::new(self.n * x.d + x.n * self.d, self.d * x.d)
    }
    fn neg(self) -> Self {
        Self {
            n: -self.n,
            d: self.d,
        }
    }
    fn sub(self, x: Self) -> Self {
        self.add(x.neg())
    }
    fn mul(self, x: Self) -> Self {
        Self::new(self.n * x.n, self.d * x.d)
    }
    fn div(self, x: Self) -> Self {
        Self::new(self.n * x.d, self.d * x.n)
    }
    fn cmp0(self) -> i8 {
        self.n.signum() as i8
    }
    fn le(self, x: Self) -> bool {
        self.n * x.d <= x.n * self.d
    }
    fn text(self) -> String {
        if self.d == 1 {
            self.n.to_string()
        } else {
            format!("{}/{}", self.n, self.d)
        }
    }
}

fn parse_region(name: &str) -> Option<BTreeSet<usize>> {
    name.strip_prefix("g_").map(|d| {
        d.chars()
            .map(|c| c.to_digit(10).unwrap() as usize - 1)
            .collect()
    })
}
fn row(name: &str) -> Vec<Rat> {
    let mut out = vec![Rat::z(); 2 * N];
    if let Some(region) = parse_region(name) {
        for s in &region {
            out[N + *s] = Rat::o()
        }
        for e in 0..N {
            if region.contains(&e) != region.contains(&((e + 1) % N)) {
                out[e] = Rat::o()
            }
        }
    } else {
        for x in &mut out[N..] {
            *x = Rat::o()
        }
        let e = name
            .strip_prefix("G_minus_e")
            .unwrap()
            .chars()
            .next()
            .unwrap()
            .to_digit(10)
            .unwrap() as usize
            - 1;
        out[e] = Rat::new(2, 1)
    }
    out
}
fn rref(mut matrix: Vec<Vec<Rat>>, columns: usize) -> (Vec<Vec<Rat>>, usize) {
    let mut r = 0;
    for c in 0..columns {
        let Some(p) = (r..matrix.len()).find(|i| matrix[*i][c].n != 0) else {
            continue;
        };
        matrix.swap(r, p);
        let q = matrix[r][c];
        for j in c..matrix[r].len() {
            matrix[r][j] = matrix[r][j].div(q)
        }
        for i in 0..matrix.len() {
            if i == r || matrix[i][c].n == 0 {
                continue;
            }
            let q = matrix[i][c];
            for j in c..matrix[i].len() {
                matrix[i][j] = matrix[i][j].sub(q.mul(matrix[r][j]))
            }
        }
        r += 1;
        if r == matrix.len() {
            break;
        }
    }
    (matrix, r)
}
fn base_relations(labels: &[String]) -> Vec<Vec<Rat>> {
    let (wall, rank) = rref(labels.iter().map(|x| row(x)).collect(), N);
    let residual = wall[rank..]
        .iter()
        .map(|r| r[N..].to_vec())
        .filter(|r| r.iter().any(|x| x.n != 0))
        .collect::<Vec<_>>();
    if residual.is_empty() {
        return residual;
    }
    let (reduced, rank) = rref(residual, N);
    reduced[..rank].to_vec()
}
fn same_sign(row: &[Rat]) -> Option<Vec<Rat>> {
    if row.iter().all(|x| x.cmp0() >= 0) && row.iter().any(|x| x.cmp0() > 0) {
        Some(vec![Rat::o()])
    } else if row.iter().all(|x| x.cmp0() <= 0) && row.iter().any(|x| x.cmp0() < 0) {
        Some(vec![Rat::new(-1, 1)])
    } else {
        None
    }
}
fn two_row_certificate(a: &[Rat], b: &[Rat]) -> Option<Vec<Rat>> {
    if let Some(c) = same_sign(b) {
        return Some(vec![Rat::z(), c[0]]);
    }
    for sign in [Rat::o(), Rat::new(-1, 1)] {
        let (mut lower, mut upper): (Option<Rat>, Option<Rat>) = (None, None);
        let mut ok = true;
        for i in 0..N {
            let constant = sign.mul(a[i]);
            match b[i].cmp0() {
                1 => {
                    let bound = constant.neg().div(b[i]);
                    lower = Some(
                        lower
                            .map(|x| if x.le(bound) { bound } else { x })
                            .unwrap_or(bound),
                    );
                }
                -1 => {
                    let bound = constant.neg().div(b[i]);
                    upper = Some(
                        upper
                            .map(|x| if bound.le(x) { bound } else { x })
                            .unwrap_or(bound),
                    );
                }
                _ => {
                    if constant.cmp0() < 0 {
                        ok = false;
                        break;
                    }
                }
            }
        }
        if ok
            && match (lower, upper) {
                (Some(l), Some(u)) => l.le(u),
                _ => true,
            }
        {
            let t = lower.or(upper).unwrap_or(Rat::z());
            return Some(vec![sign, t]);
        }
    }
    None
}
fn certificate(relations: &[Vec<Rat>]) -> Option<Vec<Rat>> {
    match relations.len() {
        0 => None,
        1 => same_sign(&relations[0]),
        2 => two_row_certificate(&relations[0], &relations[1]),
        n => panic!("unexpected base-relation rank {n}"),
    }
}

fn main() {
    let inventory: Value = serde_json::from_str(
        &fs::read_to_string("../results/seven-site-full-source-inventory.json").unwrap(),
    )
    .unwrap();
    let mut records = Vec::new();
    let mut blocked = [0usize; 7];
    let mut open = [0usize; 7];
    for orbit in inventory["all_orbits"].as_array().unwrap() {
        let labels = orbit["representative"]
            .as_array()
            .unwrap()
            .iter()
            .map(|v| v.as_str().unwrap().to_string())
            .collect::<Vec<_>>();
        let relations = base_relations(&labels);
        let cert = certificate(&relations);
        // Six wall equations split into signed-energy pivot rank plus the
        // independent induced base-relation rank.
        let wall_rank = 6 - relations.len();
        if cert.is_some() {
            blocked[wall_rank - 1] += 1
        } else {
            open[wall_rank - 1] += 1
        }
        records.push(json!({"canonical_key":orbit["canonical_key"],"wall_rank":wall_rank,"base_relation_rank":relations.len(),"base_relations":relations.iter().map(|r|r.iter().map(|x|x.text()).collect::<Vec<_>>()).collect::<Vec<_>>(),"positive_cone_obstructed":cert.is_some(),"gordan_row_coefficients":cert.map(|c|c.iter().map(|x|x.text()).collect::<Vec<_>>())}));
    }
    let packet = json!({"schema":"marici.seven_site_positive_base_gate.v1","criterion":"Gordan alternative: a nonzero nonnegative vector in the row span of the induced X-base relations excludes every strictly positive X vector","orbit_count":records.len(),"blocked_by_wall_rank":{"4":blocked[3],"5":blocked[4],"6":blocked[5]},"positive_open_by_wall_rank":{"4":open[3],"5":open[4],"6":open[5]},"orbits":records});
    fs::write(
        "../results/seven-site-positive-base-gate.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"blocked":packet["blocked_by_wall_rank"],"positive_open":packet["positive_open_by_wall_rank"]})
    );
}
