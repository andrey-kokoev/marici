object Summary { count, code_sum }

type Search:
  Branch { ~left, ~right }
  Hit { code }
  Miss

def pow4(base, exponent):
  if exponent == 0:
    return 1
  elif exponent == 1:
    return base
  elif exponent == 2:
    return base * base
  else:
    return base * base * base

def monomial(code, x, y):
  x_exp = code % 4
  quotient = code / 4
  y_exp = quotient % 4
  sum_exp = quotient / 4
  return pow4(x, x_exp) * pow4(y, y_exp) * pow4(x + y, sum_exp)

def target(kind, x, y):
  if kind == 0:
    return 1
  elif kind == 1:
    return x
  elif kind == 2:
    return y
  else:
    return x * y

def signature_matches(code, kind, point):
  if point < 16:
    x = point % 4 + 1
    y = point / 4 + 2
    if monomial(code, x, y) == target(kind, x, y):
      return signature_matches(code, kind, point + 1)
    else:
      return 0
  else:
    return 1

def search_depth(kind, initial_depth):
  bend prefix = 0, depth = initial_depth:
    when depth > 0:
      left = fork(prefix * 2, depth - 1)
      right = fork(prefix * 2 + 1, depth - 1)
      tree = Search/Branch(left, right)
    else:
      if signature_matches(prefix, kind, 0):
        tree = Search/Hit(prefix)
      else:
        tree = Search/Miss
  fold tree:
    case Search/Branch:
      left = tree.left
      right = tree.right
      open Summary: left
      open Summary: right
      return Summary(left.count + right.count, left.code_sum + right.code_sum)
    case Search/Hit:
      return Summary(1, tree.code)
    case Search/Miss:
      return Summary(0, 0)

def encode_scale(summary, scale):
  open Summary: summary
  return summary.count * scale + summary.code_sum

def encode(summary):
  return encode_scale(summary, 1000)

def main():
  return (encode(search_depth(0, 6)), encode(search_depth(1, 6)), encode(search_depth(2, 6)), encode(search_depth(3, 6)))
