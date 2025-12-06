# I did part 1 in Google Sheets lol
# https://docs.google.com/spreadsheets/d/18c06S1i9Sy0OHJ_CNlxagE56dOkz1mWFAvlMwua2TpQ/edit?gid=0#gid=0

# pretty sure I could have used pandas to do this problem in like 5 lines but I
# don't know pandas. Maybe I'll try that after I solve it the caveman way.

with open("input.txt", "r") as f:
    lines = [r for r in f.read().split("\n") if r.strip() != ""]

cols = []

for line in lines:
    # split with no args splits on all whitespaces
    nums = line.split()

    for i in range(0, len(nums)):
        if i >= len(cols):
            cols.append({"maxlen": 0, "nums": [], "operator": ""})

        if nums[i] == "*" or nums[i] == "+":
            cols[i]["operator"] = nums[i]
        else:
            cols[i]["nums"].append(nums[i])

    for k in range(len(cols)):
        for num in cols[k]["nums"]:
            if len(num) > cols[k]["maxlen"]:
                cols[k]["maxlen"] = len(num)

# now we know more about the columns, loop over the original text again
numindex = 0
for line in lines:
    if lines[-1] == line:
        break

    end = 0
    for k in range(len(cols)):
        # split the line into "maxlen" chunks
        start = end
        end = end + cols[k]["maxlen"]

        sliced = line[start:end]

        end += 1  # for the space in between this and the next col

        cols[k]["nums"][numindex] = sliced.replace(" ", "X")

    numindex += 1

# cephalopods work in RTL
cols.reverse()

finaltotal = 0

for k in range(len(cols)):
    l = cols[k]["maxlen"] - 1

    operands = []

    while l >= 0:
        finalnum = ""
        for num in cols[k]["nums"]:
            finalnum += num[l]
        l -= 1

        operands.append(int(finalnum.strip("X")))

    if cols[k]["operator"] == "*":
        result = 1
    else:
        result = 0

    for o in operands:
        if cols[k]["operator"] == "*":
            result *= o
        else:
            result += o

    finaltotal += result

print(f"Final Total: {finaltotal}")
