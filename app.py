from flask import Flask, request, render_template_string
import base64

app = Flask(__name__)

# Secret key for encryption (this is a bad practice)
SECRET_KEY = "supersecretkey"

def encrypt_data(data):
    # Simple XOR encryption (this is a very weak form of encryption)
    encrypted = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(data, SECRET_KEY))
    return base64.b64encode(encrypted.encode()).decode()

def decrypt_data(encrypted_data):
    encrypted = base64.b64decode(encrypted_data).decode()
    decrypted = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(encrypted, SECRET_KEY))
    return decrypted

@app.route('/')
def home():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <title>Crypto Failure App</title>
          </head>
          <body>
            <h1>Encrypt and Decrypt Data</h1>
            <form action="/encrypt" method="post">
              <label for="data">Data to Encrypt:</label><br>
              <input type="text" id="data" name="data"><br><br>
              <input type="submit" value="Encrypt">
            </form>
            <form action="/decrypt" method="post">
              <label for="encrypted_data">Encrypted Data to Decrypt:</label><br>
              <input type="text" id="encrypted_data" name="encrypted_data"><br><br>
              <input type="submit" value="Decrypt">
            </form>
          </body>
        </html>
    ''')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.form['data']
    encrypted_data = encrypt_data(data)
    return f"Encrypted Data: {encrypted_data}"

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_data = request.form['encrypted_data']
    decrypted_data = decrypt_data(encrypted_data)
    return f"Decrypted Data: {decrypted_data}"

if __name__ == '__main__':
    app.run(debug=True)