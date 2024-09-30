
# %%
text = "Это наш текст с частотами"
text

# %%
arr1 = {}

for symbol in text:
    if symbol in arr1:
        arr1[symbol] = arr1[symbol] + 1
    else:
        arr1[symbol] = 1

arr1


# %%

arr2 = {}
for key, val in arr1.items():
    if val not in arr2:
        arr2[val] = [key]
    else:
        arr2[val].append(key)

arr2

for key in sorted(arr2.keys()):
    print(key, ":", arr2[key])
