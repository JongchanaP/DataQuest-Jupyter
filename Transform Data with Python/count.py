import read
from collections import Counter
df = read.load_data()

tmpstr = df['headline'].str.cat(sep=' ')
tmpword = tmpstr.split()
tmpcount100 = Counter(tmpword).most_common(100)

print(tmpcount100)
