from pathlib import Path


in1 = Path("D:/Coding/Python/in1.txt")
in2 = in1.with_name("in2.txt")
in1.replace(in2)
