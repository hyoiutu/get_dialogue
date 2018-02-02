from collections import Counter
with open("input.dat", "r") as f:
  with open("output.dat", "r") as g:
    inputs = f.readlines()
    outputs = g.readlines()
unique_dialogue_pairs = list(set([(input_line, output_line) for input_line, output_line in zip(inputs, outputs)]))
"""
for input_line, output_line in zip(inputs, outputs):
      print(input_line, end="")
      print(output_line, end="")
      print("-----------")
"""
with open("unique_input.dat", "w") as f:
  with open("unique_output.dat", "w") as g:
    for input_line, output_line in unique_dialogue_pairs:
      f.write(input_line)
      g.write(output_line)
      print(input_line, end="")
      print(output_line, end="")
      print("-----------")
