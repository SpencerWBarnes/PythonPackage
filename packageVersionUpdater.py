currentVersion = ''
try:
  with open('packageVersion.txt', 'r') as packageV:
    currentVersion = packageV.read()
finally:
  if (currentVersion == ''):
    currentVersion = '0.0.1'

  newVersion = currentVersion.split('.')
  newVersion[-1] = str(int(newVersion[-1])+1)
  newVersion = '.'.join(newVersion)

  with open('packageVersion.txt', 'w+') as packageV:
    packageV.write(newVersion)