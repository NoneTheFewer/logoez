import os

cmd = "git status -s"
result = os.popen(cmd)

for line in result.read().split("\n"):
	if line.find(".svg") > -1:
		print(line)
