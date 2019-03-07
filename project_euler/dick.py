superleague = {
'olympiakos': 54,
'atromitos': 43,
'aek': 43,
'Aris': 37,
'pao': 31
}

print "h vathmologia twn 5 omadwn"
for x in superleague:
    print (superleague[x])

superleague.pop('pao')
print(superleague)

superleague.popitem()
print(superleague)

superleague.update({"Aris":37})
print(superleague)
