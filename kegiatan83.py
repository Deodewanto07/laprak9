try:
    nama = input("Nama File: ")
    handle = open(nama, "r")
    total_byte = 0
    for line in handle:
        total_byte += len(line.strip())
    print(f"{total_byte/1000} KB")
except:
    print("File tiidak ditemukan!") 