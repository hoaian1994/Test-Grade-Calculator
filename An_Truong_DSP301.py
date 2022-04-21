from os import sep
import pandas as pd
import numpy as np

# Task 1:Read file content
filename = input('Please enter input file') 
try:
    content = open(filename + '.txt', 'r')
    print('This file was opened\n' +'**** ANALYZING ****')
except:
    print("Sorry, I can't find this filename\n" +'**** REPORT ****')

# Task 2: Print total valid line and Error line
valid = 0
invalid = 0
ans = dict()
for line in content:
    line = line.strip()
    # Code # 9 characters
    line1 = line.split(',')
    if len(line1[0]) != 9:
        print('Invalid line of data: N# is invalid\n' + line)
        invalid += 1
    # Code error
    elif line1[0] < 'N00000000' or line1[0] >'N99999999':
        print('Invalid line of data: N# is invalid\n' + line)
        invalid += 1
    #List error (len # 26):
    elif len(line1) != 26:
        print('Invalid line of data: does not contain exactly 26 values\n' + line)
        invalid += 1
    # valid line
    else:
        valid += 1
        ans[line1[0]] = line1[1:]
if invalid == 0:
    print('No errors found!')
print('**** REPORT ****')
print('Total valid lines of data: ' + str(valid))
print('Total invalid lines of data: ' + str(invalid))

# Task 3: Print characteristic score
# def Mark
def mark(answ, quesNo):
    ans_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(',')
    if answ == '':
        score = 0
    elif answ == ans_key[quesNo]:
        score = 4
    else:
        score = -1
    return score

# Using pandas and match
df = pd.DataFrame(ans)
for i in range(25):
    df.loc[i] = df.loc[i].apply(lambda x : mark(x, i))

# Count hight score
score = df.sum().T
hscore = score[score >80].count()
print('Total student of high scores: ' + str(hscore))

# Mean score
print('Mean (average) score: ' + str(score.mean()))

# Max score
print('Highest score: ' + str(score.max()))

# Min score
print('Lowest score: ' + str(score.min()))

# Range score
print('Range of scores: ' +str(score.max() - score.min()))

# Mean score
print('Lowest score: ' + str(score.median()))

# Skip data
x = df.T
sk = x[x == 0].count()

for i in range(24):
    if sk.loc[i] == sk.max():
        print('Question that most people skip: ' + str(i + 1) + ' - ' + str(sk.max()) + ' - ' + str(round(sk.max()/valid,2)))

# incorect data
icr = x[x == -1].count()
for i in range(24):
    if icr.loc[i] == icr.max():
        print('Question that most people answer incorrectly: ' + str(i + 1) + ' - ' + str(icr.max()) + ' - ' + str(round(icr.max()/valid,2)))

# Task 5: Write output file
tscore = dict(score)
content = []
for stu in tscore:
    content.append(stu + ', ' + str(tscore[stu]))
result = open('Expected Output/' + filename + '_grades.txt', 'w' )
result.write('\n'.join(content))
result.close()

