import time
import os
import subprocess
i = 0
a = 1
with open('output-urls.csv') as f:
	for line in f:
		i = i + 1
		with open('output-' + str(a) + '.csv', 'aw') as f:
			f.write(line)
			if i == 1000:
				i = 0
				a = a + 1
