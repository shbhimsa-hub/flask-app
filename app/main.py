from flask import Blueprint, request, jsonify
from .models import db, DataRecord

main_bp = Blueprint('main', __name__)
@main_bp.route("/", methods=["GET"])
def healthcheck():
    return {"status": "up"}, 200


@main_bp.route('/data', methods=['POST'])
def handle_data():
    data = request.get_json()

    if not data or 'key' not in data or 'value' not in data:
        return jsonify({'error': 'Missing "key" or "value" in request'}), 400

    record = DataRecord.query.filter_by(key=data['key']).first()

    if record:
        record.value = data['value']
        message = 'Updated existing record.'
    else:
        record = DataRecord(key=data['key'], value=data['value'])
        db.session.add(record)
        message = 'Inserted new record.'

    try:
        db.session.commit()
        return jsonify({'message': message, 'key': record.key, 'value': record.value}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@main_bp.route('/data', methods=['GET'])
def list_data():
    records = DataRecord.query.all()
    result = [
        {"key": record.key, "value": record.value}
        for record in records
    ]
    return jsonify(result), 200
