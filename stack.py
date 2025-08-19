stack = []

print("Masukkan 20 elemen awal ke dalam stack:")
for i in range(20):
    elemen = input(f"Elemen ke-{i+1}: ")
    stack.append(elemen)

print("\nTop of stack saat ini:", stack[-1])

print("\nMasukkan 5 elemen tambahan untuk di-push ke stack:")
for i in range(5):
    elemen = input(f"Elemen tambahan ke-{i+1}: ")
    stack.append(elemen)

print("\nTop of stack setelah di-push:", stack[-1])

popped = stack.pop()
print("\nElemen yang di-pop:", popped)

print("Top of stack setelah pop:", stack[-1])
