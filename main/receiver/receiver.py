from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))


@app.route('/add_record', methods=['POST'])
def add_record():
    data = request.get_json()
    new_record = Record(text=data['text'])
    db.session.add(new_record)
    db.session.commit()
    return jsonify({'message': 'запись добавлена'})


@app.route('/get_records', methods=['GET'])
def get_records():
    records = Record.query.all()
    result = []
    for record in records:
        result.append({'id': record.id, 'text': record.text})
    return jsonify(result)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8080)
