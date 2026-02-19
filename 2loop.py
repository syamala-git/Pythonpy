greet = "Good Morning"
if greet == "Morning":
    print(greet)
else:
    print("Value does not match")

print("if else completed")

print("******FOR LOOP*****")
al = [1, 2, 3, 4, 5]
for i in al:
    print(i*2)

j=0
for k in range(1,6):
    j = j+k*2
print(j)

print("******SKIP FIRST INDEX*****")
for m in range(10):
    print(m)

print("******WHILE LOOP*****")

it=4
while it >= 1:
    if it!=3:
        print(it)
    it = it-1

print("******BREAK*****")
it=7
while it >= 1:
    if it == 3:
        break
    print(it)
    it = it-1

print("******CONTINUE*****")
it=7
while it >= 1:
    if it == 6:
        it = it - 1
        continue # rest of the steps are skipped

    if it == 3:
        break
    print(it)
    it = it - 1