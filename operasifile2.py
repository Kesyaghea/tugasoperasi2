class Bahasa:
    def baca_file(self, nama_file):
        try:
            with open(nama_file, "r") as file:
                teks = file.read()
                print(teks)
        except FileNotFoundError:
            print(f"File {nama_file} tidak ditemukan")

    def tulis_file(self,nama_file):
            teks = input("\n")
            with open(nama_file,"w") as file:
                file.write(teks)
                print(f"Teks sudah ditambahkan di {nama_file}")

            



