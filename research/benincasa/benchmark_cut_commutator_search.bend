from ./search_cut_commutator_calibration import (search_depth, encode_scale)

def main():
  return (encode_scale(search_depth(0, 16), 100), encode_scale(search_depth(1, 16), 100), encode_scale(search_depth(2, 16), 100), encode_scale(search_depth(3, 16), 100))
