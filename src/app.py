from flask import Flask, jsonify, request
from flask_cors import CORS  # Import flask_cors

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dữ liệu mẫu cho select options
select_options = [
    {"id": "1", "name": "Option 1"},
    {"id": "2", "name": "Option 2"},
    {"id": "3", "name": "Option 3"}
]

# Dữ liệu mẫu cho JSON objects
json_objects = {
    "1": {"name": "Phan Duc Dung", "age": 20, "address": "54A Nguyễn Chí Thanh"},
    "2": {"name": "Công ty Cổ phần Công nghệ và Truyền thông Reborn", "extraInfo": {"id": 1, "fieldName": "XYZ"}},
    "3": {"field1": "value5", "field2": "value6"}
}

@app.route('/api/select-options', methods=['GET'])
def get_select_options():
    return jsonify(select_options)

@app.route('/api/object/<string:object_id>', methods=['GET'])
def get_json_object(object_id):
    data = json_objects.get(object_id)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Object not found"}), 404

@app.route('/api/mapping', methods=['POST'])
def post_mapping():
    mapping_data = request.json
    # Xử lý dữ liệu mapping ở đây
    return jsonify({"status": "success", "mappedData": mapping_data})

if __name__ == '__main__':
    app.run(debug=True)
