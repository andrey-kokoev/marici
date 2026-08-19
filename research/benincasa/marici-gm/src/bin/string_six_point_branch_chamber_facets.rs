use serde_json::json;
use std::collections::{BTreeMap, BTreeSet};

const N: usize = 6;
const PAIRS: usize = 15;

fn pair_index(i: usize, j: usize) -> usize {
    let (a, b) = if i < j { (i, j) } else { (j, i) };
    let mut k = 0;
    for x in 1..=N {
        for y in x + 1..=N {
            if (x, y) == (a, b) { return k; }
            k += 1;
        }
    }
    unreachable!()
}

fn v(terms: &[(i64, usize, usize)]) -> Vec<i64> {
    let mut out = vec![0; PAIRS];
    for &(c, i, j) in terms { out[pair_index(i, j)] += c; }
    out
}

fn channel(mask: u8) -> Vec<i64> {
    let mut out = vec![0; PAIRS];
    for i in 1..=N { for j in i + 1..=N {
        if mask & (1 << (i - 1)) != 0 && mask & (1 << (j - 1)) != 0 {
            out[pair_index(i, j)] = 1;
        }
    }}
    out
}

fn canonical(mask: u8) -> u8 {
    let complement = 0b11_1111 ^ mask;
    mask.min(complement)
}

fn gcd(mut a: i128, mut b: i128) -> i128 {
    a = a.abs(); b = b.abs();
    while b != 0 { let r = a % b; a = b; b = r; }
    a
}

#[derive(Clone, Copy)]
struct Q { n: i128, d: i128 }
impl Q {
    fn new(mut n: i128, mut d: i128) -> Self {
        if n == 0 { return Self { n: 0, d: 1 }; }
        if d < 0 { n = -n; d = -d; }
        let g = gcd(n, d); Self { n: n / g, d: d / g }
    }
    fn sub(self, rhs: Self) -> Self { Self::new(self.n*rhs.d-rhs.n*self.d,self.d*rhs.d) }
    fn mul(self, rhs: Self) -> Self { Self::new(self.n*rhs.n,self.d*rhs.d) }
    fn div(self, rhs: Self) -> Self { Self::new(self.n*rhs.d,self.d*rhs.n) }
}

fn rank(rows: &[Vec<i64>]) -> usize {
    if rows.is_empty() { return 0; }
    let mut a: Vec<Vec<Q>> = rows.iter().map(|r| r.iter().map(|&x| Q::new(x as i128,1)).collect()).collect();
    let mut r = 0;
    for c in 0..a[0].len() {
        let Some(p) = (r..a.len()).find(|&i| a[i][c].n != 0) else { continue };
        a.swap(r,p);
        let pivot=a[r][c];
        for j in c..a[0].len() { a[r][j]=a[r][j].div(pivot); }
        for i in 0..a.len() { if i != r {
            let q=a[i][c];
            for j in c..a[0].len() { a[i][j]=a[i][j].sub(q.mul(a[r][j])); }
        }}
        r += 1;
        if r == a.len() { break; }
    }
    r
}

fn equivalent(a: &[i64], b: &[i64], relations: &[Vec<i64>]) -> bool {
    let base = rank(relations);
    for sign in [1i64,-1] {
        let mut rows=relations.to_vec();
        rows.push(a.iter().zip(b).map(|(&x,&y)| x-sign*y).collect());
        if rank(&rows)==base { return true; }
    }
    false
}

fn mask_label(mask: u8) -> String {
    (1..=N).filter(|&i| mask & (1 << (i-1)) != 0).map(|i| i.to_string()).collect::<Vec<_>>().join("")
}

fn main() {
    let permutations=[[2,3,4],[2,4,3],[3,2,4],[3,4,2],[4,2,3],[4,3,2]];
    let mut chambers=BTreeMap::new();
    let mut all_facets=BTreeSet::new();
    for p in permutations {
        let word=[1,p[0],p[1],p[2],5,6];
        let mut facets=BTreeSet::new();
        for start in 0..N { for len in 2..=4 {
            let mut mask=0u8;
            for k in 0..len { mask |= 1 << (word[(start+k)%N]-1); }
            facets.insert(canonical(mask));
        }}
        assert_eq!(facets.len(),9);
        all_facets.extend(facets.iter().copied());
        chambers.insert(word.iter().map(|x|x.to_string()).collect::<Vec<_>>().join(""),facets.iter().map(|&m|mask_label(m)).collect::<Vec<_>>());
    }

    let mut relations=Vec::new();
    for i in 1..=N {
        let mut row=vec![0;PAIRS];
        for j in 1..=N { if i!=j { row[pair_index(i,j)]=1; } }
        relations.push(row);
    }
    relations.push(v(&[(1,1,4)]));
    relations.push(v(&[(1,2,3)]));
    relations.push(v(&[(1,2,3),(1,2,5),(1,3,5)]));

    let factors=[
        ("A2",v(&[(1,1,2)])),
        ("A3",v(&[(1,1,3)])),
        ("A2*B24",v(&[(1,1,2),(1,2,4)])),
        ("A3*B34",v(&[(1,1,3),(1,3,4)])),
        ("Z*A2",v(&[(1,3,5),(1,1,2)])),
        ("Z*A2*B24",v(&[(1,3,5),(1,1,2),(1,2,4)])),
        ("A3/Z",v(&[(1,1,3),(-1,3,5)])),
        ("A3*B34/Z",v(&[(1,1,3),(1,3,4),(-1,3,5)])),
    ];
    let mut matches=BTreeMap::new();
    for (name,vector) in factors {
        let found=all_facets.iter().filter(|&&m|equivalent(&vector,&channel(m),&relations)).map(|&m|mask_label(m)).collect::<Vec<_>>();
        matches.insert(name,found);
    }
    let direct_count=matches.values().filter(|x|!x.is_empty()).count();
    let packet=json!({
        "schema":"marici.benincasa.string_six_point_branch_chamber_facets.v1",
        "gauge":"six real chambers represented by cyclic words (1,sigma(2,3,4),5,6)",
        "chambers":chambers,
        "facets_per_chamber":9,
        "branch_normals":["s14","s23","s23+s25+s35"],
        "momentum_conservation":"six row sums",
        "factor_facet_matches":matches,
        "direct_facet_factor_count":direct_count,
        "all_eight_are_direct_facets":direct_count==8,
        "classification":"unmatched factors are composite transition resonances, not single chamber facets under the frozen relations"
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-branch-chamber-facets.json",&text).unwrap();
    print!("{text}");
}
