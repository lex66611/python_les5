subj = {}

with open('Ex_06.txt', encoding='utf-8') as f:
    for row in f:
        subj_info = row.split()
        name = subj_info[0].rstrip(':')

        subj[name] = subj_info[1:]

result = {}

for key, value in subj.items():
    result[key] = sum(
        [
            int(hours[:hours.index('(')])
            for hours in value
            if hours != '-'
        ]
    )

print(result)
