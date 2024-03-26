from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/update-water-level', methods=['POST'])
def update_water_level():
    data = request.json
    print("Nível Baixo: {}, Nível Médio: {}, Nível Alto: {}".format(data['lowLevel'], data['midLevel'], data['highLevel']))
    # Aqui você pode adicionar o código para processar e armazenar os dados
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
