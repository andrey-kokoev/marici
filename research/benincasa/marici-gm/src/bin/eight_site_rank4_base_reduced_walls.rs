use serde_json::{json, Value};
use std::{collections::BTreeMap, fs};

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
            d = -d;
        }
        let mut a = n.unsigned_abs();
        let mut b = d as u128;
        while b != 0 {
            let r = a % b;
            a = b;
            b = r;
        }
        let g = a as i128;
        Self { n: n / g, d: d / g }
    }
    fn zero() -> Self {
        Self { n: 0, d: 1 }
    }
    fn one() -> Self {
        Self { n: 1, d: 1 }
    }
    fn add(self, other: Self) -> Self {
        Self::new(self.n * other.d + other.n * self.d, self.d * other.d)
    }
    fn neg(self) -> Self {
        Self {
            n: -self.n,
            d: self.d,
        }
    }
    fn sub(self, other: Self) -> Self {
        self.add(other.neg())
    }
    fn mul(self, other: Self) -> Self {
        Self::new(self.n * other.n, self.d * other.d)
    }
    fn div(self, other: Self) -> Self {
        Self::new(self.n * other.d, self.d * other.n)
    }
}

fn parse_region(name: &str) -> Option<Vec<usize>> {
    name.strip_prefix("g_").map(|digits| {
        digits
            .chars()
            .map(|c| c.to_digit(10).unwrap() as usize - 1)
            .collect()
    })
}

fn wall_coefficients(name: &str) -> (Vec<Rat>, Vec<Rat>) {
    let mut x = vec![Rat::zero(); N];
    let mut y = vec![Rat::zero(); N];
    if let Some(region) = parse_region(name) {
        for site in &region {
            x[*site] = Rat::one();
        }
        for edge in 0..N {
            if region.contains(&edge) != region.contains(&((edge + 1) % N)) {
                y[edge] = Rat::one();
            }
        }
    } else {
        x.fill(Rat::one());
        let edge = name
            .strip_prefix("G_minus_e")
            .unwrap()
            .chars()
            .next()
            .unwrap()
            .to_digit(10)
            .unwrap() as usize
            - 1;
        y[edge] = Rat::new(2, 1);
    }
    (y, x)
}

fn rank(mut matrix: Vec<Vec<Rat>>) -> usize {
    if matrix.is_empty() {
        return 0;
    }
    let mut row = 0usize;
    for column in 0..matrix[0].len() {
        let Some(pivot) = (row..matrix.len()).find(|r| matrix[*r][column].n != 0) else {
            continue;
        };
        matrix.swap(row, pivot);
        let p = matrix[row][column];
        for c in column..matrix[0].len() {
            matrix[row][c] = matrix[row][c].div(p);
        }
        for target in 0..matrix.len() {
            if target == row || matrix[target][column].n == 0 {
                continue;
            }
            let scale = matrix[target][column];
            for c in column..matrix[0].len() {
                matrix[target][c] = matrix[target][c].sub(scale.mul(matrix[row][c]));
            }
        }
        row += 1;
        if row == matrix.len() {
            break;
        }
    }
    row
}

struct ReducedWall {
    free: Vec<usize>,
    pivot_x_forms: BTreeMap<usize, Vec<Rat>>,
    base_relations: Vec<Vec<Rat>>,
}

fn solve(labels: &[String]) -> ReducedWall {
    let mut matrix = labels
        .iter()
        .map(|label| {
            let (mut y, x) = wall_coefficients(label);
            y.extend(x);
            y
        })
        .collect::<Vec<_>>();
    let mut row = 0usize;
    let mut pivots = Vec::new();
    for column in 0..N {
        let Some(pivot) = (row..matrix.len()).find(|r| matrix[*r][column].n != 0) else {
            continue;
        };
        matrix.swap(row, pivot);
        let p = matrix[row][column];
        for c in column..2 * N {
            matrix[row][c] = matrix[row][c].div(p);
        }
        for target in 0..matrix.len() {
            if target == row || matrix[target][column].n == 0 {
                continue;
            }
            let scale = matrix[target][column];
            for c in column..2 * N {
                matrix[target][c] = matrix[target][c].sub(scale.mul(matrix[row][c]));
            }
        }
        pivots.push(column);
        row += 1;
    }
    let free = (0..N).filter(|c| !pivots.contains(c)).collect::<Vec<_>>();
    let pivot_x_forms = pivots
        .iter()
        .enumerate()
        .map(|(r, pivot)| (*pivot, (0..N).map(|j| matrix[r][N + j].neg()).collect()))
        .collect();
    let base_relations = (row..matrix.len())
        .map(|r| (0..N).map(|j| matrix[r][N + j]).collect::<Vec<_>>())
        .filter(|relation| relation.iter().any(|entry| entry.n != 0))
        .collect();
    ReducedWall {
        free,
        pivot_x_forms,
        base_relations,
    }
}

fn main() {
    let rank4: Value = serde_json::from_str(
        &fs::read_to_string("../results/eight-site-rank4-universal-jacobian.json").unwrap(),
    )
    .unwrap();
    let mut patterns = BTreeMap::<String, usize>::new();
    let mut records = Vec::new();
    for item in rank4["classes"].as_array().unwrap() {
        let labels = item["labels"]
            .as_array()
            .unwrap()
            .iter()
            .map(|value| value.as_str().unwrap().to_string())
            .collect::<Vec<_>>();
        let solved = solve(&labels);
        assert_eq!(solved.free.len(), 4);
        assert_eq!(solved.base_relations.len(), 3);
        let base_rank = rank(solved.base_relations.clone());
        assert_eq!(base_rank, 3);
        let mut vanishing_pivots = Vec::new();
        let mut surviving_pivots = Vec::new();
        for (pivot, form) in &solved.pivot_x_forms {
            let mut augmented = solved.base_relations.clone();
            augmented.push(form.clone());
            if rank(augmented) == base_rank {
                vanishing_pivots.push(pivot + 1);
            } else {
                surviving_pivots.push(pivot + 1);
            }
        }
        let pattern = format!(
            "free:{};zero:{};survive:{}",
            solved
                .free
                .iter()
                .map(|i| (i + 1).to_string())
                .collect::<Vec<_>>()
                .join(","),
            vanishing_pivots
                .iter()
                .map(ToString::to_string)
                .collect::<Vec<_>>()
                .join(","),
            surviving_pivots
                .iter()
                .map(ToString::to_string)
                .collect::<Vec<_>>()
                .join(",")
        );
        *patterns.entry(pattern.clone()).or_default() += 1;
        records.push(json!({
            "canonical_key":item["canonical_key"],
            "free_edges":solved.free.iter().map(|i|i+1).collect::<Vec<_>>(),
            "pivot_edges_vanishing_mod_base":vanishing_pivots,
            "pivot_edges_surviving_mod_base":surviving_pivots,
            "reduced_pattern":pattern
        }));
    }
    let all_pivots_vanish = records.iter().all(|record| {
        record["pivot_edges_surviving_mod_base"]
            .as_array()
            .unwrap()
            .is_empty()
    });
    let packet = json!({
        "schema":"marici.eight_site_rank4_base_reduced_walls.v1",
        "orbit_count":records.len(),
        "all_four_pivot_edges_vanish_mod_source_base":all_pivots_vanish,
        "reduced_patterns":patterns,
        "records":records,
        "consequence":if all_pivots_vanish {"every rank-four wall reduces to an alternating four-edge model"} else {"the rank-four inventory contains multiple genuinely distinct base-reduced wall models"},
        "typing_correction":"companion discriminants must be reduced modulo the source base relations before physical or Leray analysis"
    });
    fs::write(
        "../results/eight-site-rank4-base-reduced-walls.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"orbits":records.len(),"patterns":patterns.len(),"all_pivots_vanish":all_pivots_vanish})
    );
}
