from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import hashlib
import base64

def encrypt_aes_ocb(data, key):
    cipher = AES.new(key, AES.MODE_OCB)
    ciphertext, tag = cipher.encrypt_and_digest(pad(data.encode(), 16))
    return ciphertext + tag

def sha1_hash(data):
    sha1 = hashlib.sha1()
    sha1.update(data)
    return sha1.digest()

def generate_barcode(nomor_pengiriman, tanggal_kirim, kode_cabang):
    secret_key = get_random_bytes(32)  # 256-bit key for AES
    encrypted_data = encrypt_aes_ocb(f"{nomor_pengiriman}{tanggal_kirim}{kode_cabang}", secret_key)
    sha1_digest = sha1_hash(encrypted_data)

    barcode_data = encrypted_data + sha1_digest
    encoded_barcode = base64.b64encode(barcode_data).decode()

    return encoded_barcode

# Contoh penggunaan
nomor_pengiriman = "049515"
tanggal_kirim = "2055201065"
kode_cabang = "TEKNIK"
barcode_result = generate_barcode(nomor_pengiriman, tanggal_kirim, kode_cabang)
print("Barcode:", barcode_result)
