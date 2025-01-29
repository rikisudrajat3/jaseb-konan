from telethon import TelegramClient, errors
import asyncio

# Konfigurasi API Telegram Anda
api_id = 28408141  # Ganti dengan API ID Anda
api_hash = 'e1c6170feb7acc804128213a793cf82a'  # Ganti dengan API Hash Anda
phone_number = '+6285384897547'  # Nomor telepon yang terdaftar di Telegram

# Daftar grup tujuan dan pesan
groups = [
    'https://t.me/OpenBOCewekBispakPalembang',
    'https://t.me/infolokerpkl',
    'https://t.me/LPM_JUAL_BELI_NOKOS',
    'https://t.me/lpmmalay',
    'https://t.me/lpm_rpps',
    'https://t.me/lpm_jualan_nokoscnit',
    'https://t.me/lpmjualan_trade_dll',
    'https://t.me/lpm_cari_cp_rprl1',
    'https://t.me/Malaysian_Jobs',
    'https://t.me/lokersitubondo',
    'https://t.me/LPMRPRLSEBLINK',
    'https://t.me/LAPAKJUALBELIJB',
    'https://t.me/LPMCNIT2',
    'https://t.me/lpmcompany',
    'https://t.me/LPMHERO2',
    'https://t.me/BLPU_1',
    'https://t.me/LPMENTER',
    'https://t.me/LpmRodagat',
    'https://t.me/LowonganKerjaLuarnegeri',
    'https://t.me/lokersumaterabarat',
    'https://t.me/grupbebaspromosi',
    'https://t.me/lokerbandarlampung',
    'https://t.me/Info_loker_jatim',
    'https://t.me/GoldenBet66',
    'https://t.me/lpmtradeataujualbeli',
    'https://t.me/LPM_ISI_BOARD',
    'https://t.me/lokerkarawangdipantauhrd',
    'https://t.me/caribfandgf',
    'https://t.me/INDO_UAE_ph_spesial',
    'https://t.me/LPMJAE',
    'https://t.me/LPM_ROLEPLAYERd',
    'https://t.me/Chellyra_Lpm',
    'https://t.me/LPMHARIMAU',
    'https://t.me/roleplypromot',
    'https://t.me/lpm_cnit',
    'https://t.me/Lapak_BA',
    'https://t.me/lpm_cari_pacar_abang_rp',
    'https://t.me/lpmaaron',
    'https://t.me/lpm_roleplayer_2',
    'https://t.me/lpmgc',
    'https://t.me/lpm_cari_cp_pacar',
    'https://t.me/lpmWS',
    'https://t.me/loker_info',
    'https://t.me/promoterpps',
    'https://t.me/LAPAKPROMOTERPQ',
    'https://t.me/lokerbs',
    'https://t.me/lokerjabodetabekbaru',
    'https://t.me/loker_bandung_jabar',
    'https://t.me/infolokerkesehatanjabodetabek',
    'https://t.me/kumpulansitusgacor',
    'https://t.me/lapak_lpm_jualan_trade_jaseb',
    'https://t.me/lpm_sfs_pfp',
    'https://t.me/BIO_RPP_30',
    'https://t.me/LPM_Roleplayers',
    'https://t.me/LpmTradeJualan2',
    'https://t.me/BEBAS_SHARE_Link_Apk',
    'https://t.me/lpm_cari_pacar_teman_rprl',
    'https://t.me/promosi_lpm',
    'https://t.me/PEJUANG_RUPIAH46',
    'https://t.me/lpm_cari_cp_temen_rprl',
    'https://t.me/lokerindokambojaterkini',
    'https://t.me/LPMJUALANNYA',
    'https://t.me/lpm_sfs_rprl',
    'https://t.me/shareapplegit',
    'https://t.me/bebaspromosisepuasnya',
    'https://t.me/soundingan',
    'https://t.me/lowonganperkerjaanindonesia',
    'https://t.me/infolokerbekasicikarangg',
    'https://t.me/lpm_cari_pacar_abang',
    'https://t.me/grupappsd',
    'https://t.me/mabarmlnpubg',
    'https://t.me/lpm_wm',
    'https://t.me/loker_jakarta1',
    'https://t.me/lpm_roleplayer_sq',
    'https://t.me/BEBAS_SHERE_ALL_APP',
    'https://t.me/BEBAS_SHARE_Link_Apk01',
    'https://t.me/situsgacorrinfo',
    'https://t.me/LPMJESVIE',
    'https://t.me/Aplikasi_Penghasil_Uang8',
    'https://t.me/lpmbarunetesni',
    'https://t.me/lapakppromosi',
    'https://t.me/lpmprofneedss',
    'https://t.me/LPMBIXENTA',
    'https://t.me/lpm_rp_rasa_cc',
    'https://t.me/LPMLALISA',
    'https://t.me/LPMAHYEOON',
    'https://t.me/JualBeliAkunPapji',
    'https://t.me/LPMrendang',
    'https://t.me/lokerindokamboja',
    'https://t.me/lpm_bebasye',
    'https://t.me/LPMNANAMI',
    'https://t.me/MEHLPM',
    'https://t.me/Lpmjualangab',
    'https://t.me/LpmJualanm',
    'https://t.me/LPMHVFUN',
    'https://t.me/LPMHOONN',
    'https://t.me/LPMYOUNGHOON',
    'https://t.me/LPMKARANG',
    'https://t.me/loker67BMNpmbnlOnYOh',
    'https://t.me/lokersukabumicianjur',
    'https://t.me/lpm_sfs_isi_board',
    'https://t.me/lpmrpps',
    'https://t.me/lpm_cari_pacar_abang_teman',
    'https://t.me/LPMJUALBELIFF',
    'https://t.me/jualbeli_apkpremium',
    'https://t.me/LPMBRIGANZA',
    'https://t.me/FF_PROMOTE',
    'https://t.me/lpmbbgdkk',
    'https://t.me/LPMDEANN',
    'https://t.me/LPMSheina',
    'https://t.me/lpmhirminopmembsqcc',
    'https://t.me/lpmcien',
    'https://t.me/LPMBTS',
    'https://t.me/lpmwordingh',
    'https://t.me/LPMBBRIGHTVC',
    'https://t.me/Ardioan',
    'https://t.me/LPMBLACKHARRIER',
    'https://t.me/LPMVINIX',
    'https://t.me/LPMNYACIA',
    'https://t.me/LPM_SFS_MAIN_ACC_RP',
    'https://t.me/LPM_NEED_GF_ADEK_TEMEN',
    'https://t.me/LPMJOKIAJA',
    'https://t.me/onlpmm',
    'https://t.me/Lpmstoremalayy',
    'https://t.me/LPMBBG',
    'https://t.me/LPMAESPHENCTS',
    'https://t.me/LPMAQUATIC',
    'https://t.me/lpm_kerajaan',
    'https://t.me/LPM_CARI_CP_RPX',
    'https://t.me/altrdhcyndr',
    'https://t.me/Cari_fambest_lpm',
    'https://t.me/Lpm_Kyuu',
    'https://t.me/lpm_jualann',
    'https://t.me/grupgfbf',
    'https://t.me/lpmreacthwa',
    'https://t.me/fnjwsellenLPM',
    'https://t.me/LPM_ROLEPLAYER_FOREVER',
    'https://t.me/lpm_need_cp_gf_bf',
    'https://t.me/lpm_ootp',
    'https://t.me/Cpnskotapekalongan',
    'https://t.me/promosibisnisindo',
    'https://t.me/lpm_bebas_oot',
    'https://t.me/myrobin',
    'https://t.me/loker_bandungraya',
    'https://t.me/Lpm_roleplayfm',
    'https://t.me/LPM_FREELANCEE',
    'https://t.me/frreelancee',
    'https://t.me/LPMNEEDASSISTNKERJA',
    'https://t.me/sewa_waa',
    'https://t.me/jualbeliakunmlbbff',
    'https://t.me/indoph001',
    'https://t.me/Lowongan_Kerja_Indonesia',
    'https://t.me/JBBALI',
    'https://t.me/lokerkotabandarlampung',
    'https://t.me/IDFreelancers',
    'https://t.me/kerjaparuhwaktu2',
    'https://t.me/berbagiloker',
    'https://t.me/OpenBOCewekBispakDenpasar',
    'https://t.me/grouppromobisnisonlineindonesia',
    'https://t.me/LPMBEBASATHENS',
    'https://t.me/OpenBOCewekBispakDepok',
    'https://t.me/JBALLGAMEKEY',
    'https://t.me/lapakpromosi',
    'https://t.me/MUTUALANISTAGRAM',
    'https://t.me/salingberbagivideovirall',
    'https://t.me/Lpm_grup_Promote',
    'https://t.me/loker_jatimindo',
    'https://t.me/komunitas_umkm_indonesia',
    'https://t.me/LPMARMY',
    'https://t.me/IndoJobCambodia',
    'https://t.me/bahasAplikasiScam',
    'https://t.me/ptigpinternasional',
    'https://t.me/ngobrolbarengandy',
    'https://t.me/BisnisOnline_Bahagia',
    'https://t.me/TanteMedanCariBrondong',
    'https://t.me/freelancepanggilin',
    'https://t.me/promosionlineindonesia',
    'https://t.me/loker_jatim',
    'https://t.me/OpenBOCewekBispakBali',
    'https://t.me/OpenBOCewekBispakCirebon',
    'https://t.me/LAPAKJUALANRANDOM',
    'https://t.me/LPMASHTARTE',
    'https://t.me/httpstmejoinchatINqVtCk7PH',
    'https://t.me/LowonganKerjaOnline',
    'https://t.me/loker_JeparaJateng_resmi',
    'https://t.me/kapalpesiarluarnegeri',
    'https://t.me/pusatuntirtaserang',
    'https://t.me/LPMCW',
    'https://t.me/BAEIRENELPM',
    'https://t.me/lowonganmagangdantokuteiginou',
    'https://t.me/lpm_indonesia',
    'https://t.me/LPMFELLA',
]

message = (
    "Kalian butuh freelance? 3-5 menit langsung cuan\n"
    "🔹 Tidak perlu KTP ✓ \n"
    "🔹 Tidak ada modal pendaftaran atau modal apapun ✓ \n"
    "🔹 Hanya membutuhkan apk WhatsApp ✓ \n\n"
    "Kerja nya seperti apa??\n\n"
    "HANYA MENAMBAHKAN MEMBER KE GRUP WHATSAPP YANG TELAH DI SEDIAKAN\n\n"
    "Gaji 40k hingga 800k sekali kerja💸💸💸 \n"
    "PASTI ADA BIMBINGAN BAGI YANG BELUM PAHAM \n\n"
    "Link grup Telegram:\n"
    "https://t.me/akatsukiws\n"
    "https://t.me/akatsukiws\n"
    "https://t.me/akatsukiws\n"
    "https://t.me/akatsukiws\n"
    "Bukti payment:\n"
    "https://t.me/octocraft21"
)

async def send_messages():
    # Inisialisasi klien Telethon
    async with TelegramClient('session_userbot', api_id, api_hash) as client:
        print("Menghubungkan ke Telegram...")
        await client.connect()

        if not await client.is_user_authorized():
            print("Anda belum login. Silakan masukkan kode otentikasi.")
            await client.send_code_request(phone_number)
            code = input("Masukkan kode otentikasi: ")
            await client.sign_in(phone_number, code)

        total_groups = len(groups)  # Jumlah grup yang ada
        wait_time = 70 * 60 // total_groups  # Waktu tunggu dibagi dengan jumlah grup

        for i in range(10):  # Mengirim total 10 iterasi pesan
            success_count = 0
            failed_groups = []

            for group in groups:
                try:
                    # Kirim pesan ke grup
                    print(f"Mengirim pesan ke grup: {group}")
                    await client.send_message(group, message)
                    print(f"Pesan berhasil dikirim ke {group}")
                    success_count += 1
                except errors.FloodWaitError as e:
                    print(f"FloodWaitError: Harus menunggu {e.seconds} detik sebelum mencoba lagi.")
                    await asyncio.sleep(e.seconds)
                except errors.ChatWriteForbiddenError:
                    print(f"Gagal mengirim pesan ke {group}: Anda tidak memiliki izin.")
                    failed_groups.append(group)
                except Exception as e:
                    print(f"Gagal mengirim pesan ke {group}: {e}")
                    failed_groups.append(group)

                # Tambahkan jeda 20 detik antara pengiriman pesan ke setiap grup
                print("Menunggu 20 detik sebelum mengirim ke grup berikutnya...")
                await asyncio.sleep(11)

            # Laporan hasil pengiriman
            print(f"Iterasi {i+1}: {success_count} pesan berhasil dikirim.")
            if failed_groups:
                print("Pesan gagal dikirim ke grup berikut:")
                for failed_group in failed_groups:
                    print(f"- {failed_group}")

            # Jeda antar grup yang berhasil dikirimi pesan
            if success_count > 0:
                print(f"Menunggu {wait_time / 60:.0f} menit sebelum mengirim pesan berikutnya...")
                await asyncio.sleep(wait_time)  # Tunggu sesuai jumlah grup

            if i < 9:  # Tunggu 70 menit sebelum iterasi berikutnya
                print("Menunggu 70 menit sebelum mengirim pesan berikutnya...")
                await asyncio.sleep(4200)  # 4200 detik = 70 menit

# Jalankan fungsi utama
if __name__ == "__main__":
    asyncio.run(send_messages())
