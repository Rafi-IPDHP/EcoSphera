import pandas as pd

auth = 'user'

def search():
    bank_sampah = pd.read_csv('data_bank_sampah.csv', sep=';')

    print('\n' + 30 * '=')
    choice = int(input('\n[1]Nama Bank Sampah\n[2]Nama Pengelola Bank Sampah\n[3]Lokasi Bank Sampah\n[4]Harga Sampah Organik\n[5]Harga Sampah Non Organik\n[6]Kembali\nCari Bank Sampah berdasarkan kategori: '))

    if(choice == 1):
        nama_bank = input('Masukkan nama bank sampah yang ingin dicari (q untuk quit): ')

        data_bank = bank_sampah[bank_sampah['nama bank sampah'].str.contains(nama_bank, case=False, na=False)]

        if(nama_bank == 'q'):
            choiceAdmin()
        else:
            if not data_bank.empty:
                print('\n')
                print(data_bank)
                search()
            else:
                print("\nTidak ada hasil yang mendekati nama bank sampah tersebut.")
                search()
    elif(choice == 2):
        nama_pengelola = input('Masukkan nama pengelola bank sampah yang ingin dicari (q untuk quit): ')

        data_bank = bank_sampah[bank_sampah['nama pengelola'].str.contains(nama_pengelola, case=False, na=False)]

        if(nama_pengelola == 'q'):
            choiceAdmin()
        else:
            if not data_bank.empty:
                print('\n')
                print(data_bank)
                search()
            else:
                print("\nTidak ada hasil yang mendekati nama pengelola bank sampah tersebut.")
                search()
    elif(choice == 3):
        lokasi = input('Masukkan lokasi bank sampah yang ingin dicari (q untuk quit): ')

        data_bank = bank_sampah[bank_sampah['lokasi'].str.contains(lokasi, case=False, na=False)]

        if(lokasi == 'q'):
            choiceAdmin()
        else:
            if not data_bank.empty:
                print('\n')
                print(data_bank)
                search()
            else:
                print("\nTidak ada hasil yang mendekati lokasi bank sampah tersebut.")
                search()
    elif(choice == 4):
        harga_organik = input('Masukkan harga sampah organik yang ingin dicari (q untuk quit): ')

        data_bank = bank_sampah[bank_sampah['harga sampah organik'].str.contains(int(harga_organik), case=False, na=False)]

        if(harga_organik == 'q'):
            choiceAdmin()
        else:
            if not data_bank.empty:
                print('\n')
                print(data_bank)
                search()
            else:
                print("\nTidak ada hasil yang mendekati harga sampah tersebut.")
                search()
    elif(choice == 5):
        harga_non_organik = input('Masukkan harga sampah non organik yang ingin dicari (q untuk quit): ')

        data_bank = bank_sampah[bank_sampah['harga sampah non-organik'] <= int(harga_non_organik)]

        if(harga_non_organik == 'q'):
            choiceAdmin()
        else:
            if not data_bank.empty:
                print('\n')
                print(data_bank)
                search()
            else:
                print("\nTidak ada hasil yang mendekati harga sampah tersebut.")
                search()
    elif(choice == 6):
        choiceAdmin()
    else:
        print('Silakan pilih kategori berdasarkan angka yang tersedia!')
        search()

def crud():
    bank_sampah = pd.read_csv('data_bank_sampah.csv', sep=';')
    header = ['nama bank sampah', 'nama pengelola', 'lokasi', 'kontak pengelola', 'harga sampah organik', 'harga sampah non-organik']

    print('\n' + 30 * '=')
    choice = int(input('\n[1]Tambah data bank sampah\n[2]Lihat data bank sampah\n[3]Update data bank sampah\n[4]Hapus data bank sampah\n[5]Kembali\nSilakan pilih fitur berdasarkan angka: '))

    if(choice == 1):
        nama_bank = input('\nMasukan nama bank sampah: ')
        nama_pengelola = input('Masukkan nama pengelola: ')
        lokasi = input('Masukkan lokasi bank sampah: ')
        kontak = int(input('Masukkan kontak pengelola bank sampah: '))
        organik = int(input('Masukkan harga sampah organik: '))
        non_organik = int(input('Masukkan harga sampah non organik: '))

        data = [[nama_bank, nama_pengelola, lokasi, kontak, organik, non_organik]]

        new_data =  pd.DataFrame(data, columns=header)
        new_data.to_csv('data_bank_sampah.csv', mode='a', sep=';', header=False, index=False)

        print('\nData bank sampah berhasil dibuat!!!')
        crud()
    elif(choice == 2):
        print(bank_sampah)
        crud()
    elif(choice == 3):
        print('\n')
        print(bank_sampah)
        selected_bank = input('\nPilih bank sampah yang ingin di update berdasarkan nomor bank sampah (q jika tidak ada): ')

        if(selected_bank == 'q'):
            crud()
        elif( int(selected_bank) in bank_sampah.index):
            data_dipilih = bank_sampah.iloc[int(selected_bank)]

            nama_bank = data_dipilih['nama bank sampah']
            nama_pengelola = data_dipilih['nama pengelola']
            lokasi = data_dipilih['lokasi']
            kontak = data_dipilih['kontak pengelola']
            harga_organik = data_dipilih['harga sampah organik']
            harga_non_organik = data_dipilih['harga sampah non-organik']

            print('\nSilakan isi data terbaru, kosongkan jika tidak ada perubahan')
            new_nama_bank = input(f'Masukkan nama bank sampah baru ({nama_bank}): ') or nama_bank
            new_nama_pengelola = input(f'Masukkan nama pengelola baru ({nama_pengelola}): ') or nama_pengelola
            new_lokasi = input(f'Masukkan lokasi bank sampah baru ({lokasi}): ') or lokasi
            new_kontak = input(f'Masukkan kontak baru pengelola bank sampah ({kontak}): ') or kontak
            new_harga_organik = input(f'Masukkan harga baru sampah organik ({harga_organik}): ') or harga_organik
            new_harga_non_organik = input(f'Masukkan harga baru sampah non organik ({harga_non_organik}): ') or harga_non_organik

            bank_sampah.loc[int(selected_bank), ['nama bank sampah', 'nama pengelola', 'lokasi', 'kontak pengelola', 'harga sampah organik', 'harga sampah non-organik']] = [new_nama_bank, new_nama_pengelola, new_lokasi, int(new_kontak), int(new_harga_organik), int(new_harga_non_organik)]

            bank_sampah.to_csv('data_bank_sampah.csv', index=False, sep=';')

            print('\nData berhasil diperbarui!!!')
            crud()
        else:
            print('\nData belum ada, silakan masukkan data dengan benar!')
            crud()
    elif(choice == 4):
        print('\n')
        print(bank_sampah)
        print('\n')
        delete_index = input('Pilih nomor bank sampah yang ingin dihapus (q jika tidak ada): ')

        if(delete_index.lower() == 'q'):
            crud()
        else:
            delete_bank_sampah = bank_sampah.drop(index=int(delete_index))
            delete_bank_sampah.to_csv('data_bank_sampah.csv', sep=';', index=False)
            print('\n' + 'Data bank sampah berhasil dihapus!!!')
            crud()
    elif(choice == 5):
        choiceAdmin()


def ecoscalc():
    bank_sampah = pd.read_csv('data_bank_sampah.csv', sep=';')

    print('\n' + 30 * '=')
    print(bank_sampah)
    selected_bank = input('\nPilih bank sampah berdasarkan nomor bank sampah (q jika tidak ada): ')

    if(selected_bank == 'q'):
        choiceAdmin()
    elif int(selected_bank) in bank_sampah.index:
        data_dipilih = bank_sampah.iloc[int(selected_bank)]
        
        harga_organik = data_dipilih['harga sampah organik']
        harga_non_organik = data_dipilih['harga sampah non-organik']

        input_organik = int(input('\nMasukkan berat sampah organik(kg): '))
        input_non_organik = int(input('Masukkan berat sampah non-organik(kg): '))

        print(f'\nTotal harga sampah organik anda adalah Rp.{harga_organik * input_organik}')
        print(f'Total harga sampah non-organik anda adalah Rp.{harga_non_organik * input_non_organik}')

        next_step = int(input('\n[1]Ya\n[2]Tidak\nApakah anda ingin menghitung lagi? '))

        if(next_step == 1):
            ecoscalc()
        elif(next_step == 2):
            if(auth == 'admin'):
                choiceAdmin()
            elif(auth == 'user'):
                choiceUser()
        else:
            print('Silakan pilih berdasarkan pilihan yang tersedia!')

    else:
        print('\nData belum ada, silakan masukkan data dengan benar!')
        ecoscalc()


def choiceAdmin():
    print('\n' + 30 * '=')
    choice = int(input('\n[1]EcosCalc\n[2]CRUD Bank Sampah\n[3]Search Bank Sampah\n[4]Rating Bank Sampah\n[5]Logout\n[6]Exit\nSilakan pilih fitur berdasarkan angka: '))

    if(int(choice) == 1):
        ecoscalc()
    elif(int(choice) == 2):
        crud()
    elif(int(choice) == 3):
        search()
    elif(int(choice) == 5):
        print('\nLogout berhasil!!!')
        login()
    elif(int(choice) == 6):
        pass
    else:
        print('Silakan pilih berdasarkan angka atau pilihan yang tersedia')
        choiceAdmin()


def choiceUser():
    bank_sampah = pd.read_csv('data_bank_sampah.csv', sep=';')

    print('\n' + 30 * '=')
    choice = int(input('\n[1]EcosCalc\n[2]Lihat Bank Sampah\n[3]Search Bank Sampah\n[4]Rating Bank Sampah\n[5]Logout\n[6]Exit\nSilakan pilih fitur berdasarkan angka: '))

    if(choice == 1):
        ecoscalc()
    elif(choice == 2):
        print('\n', bank_sampah)
        choiceUser()
    elif(choice == 5):
        login()
    elif(choice == 6):
        pass
    else:
        print('Silakan pilih berdasarkan angka atau pilihan yang tersedia')


def choicePengelola():
    print('\nFitur ini masih dalam pengembangan!!!')
    pass


def login():
    users = pd.read_csv('users.csv', sep=';')

    print('\n' + 30 * '=')

    print('\nSilakan masuk ke akun anda!\n')
    uname = input('Masukkan username: ')
    pw = input('Masukkan password: ')

    validate = users[(users['username'] == uname) & (users['password'] == pw)]

    if(not validate.empty):
        print('\n' + 30 * '=')
        print('Login berhasil!!!')
        role = validate.iloc[0]['role']
        if(role == 'admin'):
            auth = 'admin'
            choiceAdmin()
        elif(role == 'user'):
            auth = 'user'
            choiceUser()
        elif(role == 'pengelola'):
            auth = 'pengelola'
            print('Fitur ini masih dalam pengembangan!')
            choicePengelola()
        else:
            print('laahh siapa dong ini')
    else:
        print('Username atau password salah! Silakan coba lagi!')
        login()


def register():
    users = pd.read_csv('users.csv', sep=';')

    print('\n' + 30 * '=')

    regisChoice = int(input('\n[1]User\n[2]Pengelola\n[3]Kembali\n[4]Exit\nSilakan pilih register sebagai: '))

    if(regisChoice == 1 or regisChoice == 2):
        def regis2():
            uname = input('\nMasukkan username: ')
            pw = input('Masukkan password: ')
            
            notUnique = users[(users['username'] == uname)]
            if(not notUnique.empty):
                print('\nUsername sudah terdaftar! Silakan pakai username baru!')
                regis2()
            else:
                header = ['username', 'password', 'role']

                if(regisChoice == 1):
                    user = [[uname, pw, 'user']]
                elif(regisChoice == 2):
                    user = [[uname, pw, 'pengelola']]

                new_user = pd.DataFrame(user, columns=header)
                new_user.to_csv('users.csv', mode='a', sep=';', header=False, index=False)

                print('\nSelamat akun anda telah berhasil dibuat!!! Silakan login terlebih dahulu!')
                login()
        regis2()
    elif(regisChoice == 3):
        choice1()
    elif(regisChoice == 4):
        pass
    else:
        print('Silakan pilih berdasarkan angka yang tersedia!!!')


def choice1():
    print('\n' + 30 * '=')
    print('Selamat Datang di EcoSphera!!!')
    
    choice = int(input('\n[1]Register\n[2]Login\n[3]Exit\nSilakan pilih Login atau Register: '))

    if(choice == 1):
        register()
    elif(choice == 2):
        login()
    elif(choice == 3):
        pass
    else:
        print('Silakan pilih 1, 2 atau 3!!!')


choice1()