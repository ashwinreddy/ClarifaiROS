x = {'glasses': 1, 'adult': 0.9823423223243223423, 'panda': 2, 'otherEx': 9}

vals = sorted(x.values())[::-1][:2]
for i in vals:
	print x.values().index(i)