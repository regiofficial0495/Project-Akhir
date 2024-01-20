<?php

function generateKey() {
    return bin2hex(random_bytes(16)); // 128-bit key for AES-256
}

function encryptAESCTR($data, $key) {
    $nonce = random_bytes(16); // 128-bit nonce for AES-256 CTR
    $ciphertext = openssl_encrypt($data, 'aes-256-ctr', $key, OPENSSL_RAW_DATA, $nonce);
    return base64_encode($nonce . $ciphertext);
}

function decryptAESCTR($ciphertext, $key) {
    $ciphertext = base64_decode($ciphertext);
    $nonce = substr($ciphertext, 0, 16);
    $ciphertext = substr($ciphertext, 16);
    return openssl_decrypt($ciphertext, 'aes-256-ctr', $key, OPENSSL_RAW_DATA, $nonce);
}

function saveToWatermark($data, $watermarkFile) {
    file_put_contents($watermarkFile, json_encode($data));
}

function readFromWatermark($watermarkFile) {
    return json_decode(file_get_contents($watermarkFile), true);
}

// Contoh penggunaan
$dataToEncrypt = ["username" => "admin", "password" => "lupapassword"];
$key = generateKey();

// Enkripsi data JSON
$encryptedData = encryptAESCTR(json_encode($dataToEncrypt), $key);

// Simpan ke watermark
$watermarkFile = 'watermark.json';
saveToWatermark(["encrypted_data" => $encryptedData, "key" => $key], $watermarkFile);

// Baca dari watermark
$watermarkData = readFromWatermark($watermarkFile);
$storedEncryptedData = $watermarkData["encrypted_data"];
$storedKey = $watermarkData["key"];

// Dekripsi data JSON
$decryptedData = json_decode(decryptAESCTR($storedEncryptedData, $storedKey), true);

// Tampilkan hasil
echo "Original Data:\n";
print_r($dataToEncrypt);
echo "\nDecrypted Data:\n";
print_r($decryptedData);
