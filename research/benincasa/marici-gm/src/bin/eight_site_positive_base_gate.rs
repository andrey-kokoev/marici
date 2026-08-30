use serde_json::{json, Value};
use std::{collections::BTreeSet, fs};

const N: usize = 8;

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
fn max_rat(left: Option<Rat>, right: Rat) -> Option<Rat> {
    Some(left.map(|value| if value.le(right) { right } else { value }).unwrap_or(right))
}
fn min_rat(left: Option<Rat>, right: Rat) -> Option<Rat> {
    Some(left.map(|value| if right.le(value) { right } else { value }).unwrap_or(right))
}

// Solve a*x+b*y+d >= 0 exactly.  Fourier--Motzkin eliminates y,
// then reconstructs one rational witness.
fn feasible_two(inequalities: &[(Rat, Rat, Rat)]) -> Option<(Rat, Rat)> {
    let mut reduced = Vec::<(Rat, Rat)>::new();
    let positives = inequalities.iter().filter(|(_, b, _)| b.cmp0() > 0).collect::<Vec<_>>();
    let negatives = inequalities.iter().filter(|(_, b, _)| b.cmp0() < 0).collect::<Vec<_>>();
    for (a, _b, d) in inequalities.iter().filter(|(_, b, _)| b.cmp0() == 0) {
        reduced.push((*a, *d));
    }
    for (ap, bp, dp) in &positives {
        for (an, bn, dn) in &negatives {
            reduced.push((
                bn.neg().mul(*ap).add(bp.mul(*an)),
                bn.neg().mul(*dp).add(bp.mul(*dn)),
            ));
        }
    }
    let (mut lower_x, mut upper_x) = (None, None);
    for (a, d) in &reduced {
        match a.cmp0() {
            1 => lower_x = max_rat(lower_x, d.neg().div(*a)),
            -1 => upper_x = min_rat(upper_x, d.neg().div(*a)),
            _ if d.cmp0() < 0 => return None,
            _ => {}
        }
    }
    if matches!((lower_x, upper_x), (Some(lower), Some(upper)) if !lower.le(upper)) {
        return None;
    }
    let x = lower_x.or(upper_x).unwrap_or(Rat::z());
    let (mut lower_y, mut upper_y) = (None, None);
    for (a, b, d) in inequalities {
        let constant = a.mul(x).add(*d);
        match b.cmp0() {
            1 => lower_y = max_rat(lower_y, constant.neg().div(*b)),
            -1 => upper_y = min_rat(upper_y, constant.neg().div(*b)),
            _ if constant.cmp0() < 0 => return None,
            _ => {}
        }
    }
    if matches!((lower_y, upper_y), (Some(lower), Some(upper)) if !lower.le(upper)) {
        return None;
    }
    Some((x, lower_y.or(upper_y).unwrap_or(Rat::z())))
}

fn certificate(relations: &[Vec<Rat>]) -> Option<Vec<Rat>> {
    if relations.is_empty() {
        return None;
    }
    assert!(relations.len() <= 3, "C8 base-relation rank exceeded frozen bound");
    for fixed in 0..relations.len() {
        for fixed_value in [Rat::o(), Rat::new(-1, 1)] {
            let free = (0..relations.len()).filter(|index| *index != fixed).collect::<Vec<_>>();
            let mut inequalities = Vec::new();
            for site in 0..N {
                inequalities.push((
                    free.first().map(|index| relations[*index][site]).unwrap_or(Rat::z()),
                    free.get(1).map(|index| relations[*index][site]).unwrap_or(Rat::z()),
                    fixed_value.mul(relations[fixed][site]),
                ));
            }
            let Some((x, y)) = feasible_two(&inequalities) else { continue };
            let mut coefficients = vec![Rat::z(); relations.len()];
            coefficients[fixed] = fixed_value;
            if let Some(index) = free.first() { coefficients[*index] = x; }
            if let Some(index) = free.get(1) { coefficients[*index] = y; }
            let image = (0..N).map(|site| {
                coefficients.iter().enumerate().fold(Rat::z(), |sum, (index, coefficient)| {
                    sum.add(coefficient.mul(relations[index][site]))
                })
            }).collect::<Vec<_>>();
            if image.iter().all(|value| value.cmp0() >= 0)
                && image.iter().any(|value| value.cmp0() > 0) {
                return Some(coefficients);
            }
        }
    }
    None
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn fourier_motzkin_reconstructs_and_rejects_exactly() {
        let feasible = [
            (Rat::o(), Rat::z(), Rat::new(-1, 1)),
            (Rat::z(), Rat::o(), Rat::new(-2, 1)),
            (Rat::new(-1, 1), Rat::new(-1, 1), Rat::new(5, 1)),
        ];
        let (x, y) = feasible_two(&feasible).unwrap();
        assert!(feasible.iter().all(|(a, b, d)| a.mul(x).add(b.mul(y)).add(*d).cmp0() >= 0));
        let impossible = [
            (Rat::o(), Rat::z(), Rat::new(-1, 1)),
            (Rat::new(-1, 1), Rat::z(), Rat::z()),
        ];
        assert!(feasible_two(&impossible).is_none());
    }

    #[test]
    fn rank_three_projective_normalization_finds_certificate() {
        let relations = vec![
            vec![Rat::o(), Rat::new(-1, 1), Rat::z(), Rat::z(), Rat::z(), Rat::z(), Rat::z(), Rat::z()],
            vec![Rat::z(), Rat::o(), Rat::new(-1, 1), Rat::z(), Rat::z(), Rat::z(), Rat::z(), Rat::z()],
            vec![Rat::o(), Rat::o(), Rat::o(), Rat::o(), Rat::o(), Rat::o(), Rat::o(), Rat::o()],
        ];
        let witness = certificate(&relations).unwrap();
        let image = (0..N).map(|site| witness.iter().enumerate().fold(Rat::z(), |sum, (row, coefficient)| {
            sum.add(coefficient.mul(relations[row][site]))
        })).collect::<Vec<_>>();
        assert!(image.iter().all(|value| value.cmp0() >= 0));
        assert!(image.iter().any(|value| value.cmp0() > 0));
    }
}

fn main() {
    let inventory: Value = serde_json::from_str(
        &fs::read_to_string("../results/eight-site-full-source-inventory.json").unwrap(),
    )
    .unwrap();
    let mut records = Vec::new();
    let mut blocked = [0usize; 8];
    let mut open = [0usize; 8];
    for orbit in inventory["all_orbits"].as_array().unwrap() {
        let labels = orbit["representative"]
            .as_array()
            .unwrap()
            .iter()
            .map(|v| v.as_str().unwrap().to_string())
            .collect::<Vec<_>>();
        let relations = base_relations(&labels);
        let cert = certificate(&relations);
        // Seven wall equations split into signed-energy pivot rank plus the
        // independent induced base-relation rank.
        let wall_rank = 7 - relations.len();
        if cert.is_some() {
            blocked[wall_rank - 1] += 1
        } else {
            open[wall_rank - 1] += 1
        }
        records.push(json!({"canonical_key":orbit["canonical_key"],"wall_rank":wall_rank,"base_relation_rank":relations.len(),"base_relations":relations.iter().map(|r|r.iter().map(|x|x.text()).collect::<Vec<_>>()).collect::<Vec<_>>(),"positive_cone_obstructed":cert.is_some(),"gordan_row_coefficients":cert.map(|c|c.iter().map(|x|x.text()).collect::<Vec<_>>())}));
    }
    let packet = json!({"schema":"marici.eight_site_positive_base_gate.v1","criterion":"Gordan alternative: a nonzero nonnegative vector in the row span of the induced X-base relations excludes every strictly positive X vector","certificate_solver":"exact rational Fourier-Motzkin after projective coefficient normalization; complete for base-relation rank at most three","orbit_count":records.len(),"blocked_by_wall_rank":{"4":blocked[3],"5":blocked[4],"6":blocked[5],"7":blocked[6]},"positive_open_by_wall_rank":{"4":open[3],"5":open[4],"6":open[5],"7":open[6]},"orbits":records});
    fs::write(
        "../results/eight-site-positive-base-gate.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"blocked":packet["blocked_by_wall_rank"],"positive_open":packet["positive_open_by_wall_rank"]})
    );
}
