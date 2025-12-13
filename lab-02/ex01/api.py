from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400
    plain_text = data.get("plain_text")
    key = data.get("key")
    if plain_text is None or key is None:
        return jsonify({"error": "plain_text and key are required"}), 400
    try:
        key = int(key)
    except (ValueError, TypeError):
        return jsonify({"error": "key must be an integer"}), 400
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({"encrypted_message": encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400
    cipher_text = data.get("cipher_text")
    key = data.get("key")
    if cipher_text is None or key is None:
        return jsonify({"error": "cipher_text and key are required"}), 400
    try:
        key = int(key)
    except (ValueError, TypeError):
        return jsonify({"error": "key must be an integer"}), 400
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({"decrypted_message": decrypted_text})

# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)