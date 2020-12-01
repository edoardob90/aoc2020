#!/usr/local/bin/wolframscript

input = Import["input.txt", "List"];

(* Takes ~ 17 ms *)
Print[
With[{l = Union[Permutations[input, {2}]]},
  Times @@@ l[[Position[Total /@ l, 2020][[1]]]]
  ]
]

(* Takes ~ 4 s *)
Print[
With[{l = Union[Permutations[input, {3}]]},
  Times @@@ l[[Position[Total /@ l, 2020][[1]]]]
  ]
]
