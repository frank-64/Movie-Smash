import gzip

path = "C:/Users/Frankie/PycharmProjects/Django-Website/name.basics.tsv.gz"
f = gzip.open(path, 'rb')
print(f.read())
