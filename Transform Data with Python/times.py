import read
df = read.load_data()

from dateutil.parser import parse

def extrHour(dt):
    return parse(dt).hour

df['submission_hour'] = df['submission_time'].apply(extrHour)

print(df['submission_hour'].value_counts())
