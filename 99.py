from pathlib import Path

content = Path("in1.txt").read_text(encoding="utf-8")
groceries = [line for line in content.splitlines() if line.startswith("*")]
Path("out1.txt").write_text("\n".join(groceries), encoding="utf-8")
