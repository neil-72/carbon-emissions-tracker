from flask import Flask, request, jsonify
from flask_restful import Api
from src.scraper import EmissionsScraper
from src.data_processor import DataProcessor

app = Flask(__name__)
api = Api(app)

scraper = EmissionsScraper()
processor = DataProcessor()

@app.route('/api/emissions', methods=['GET'])
def get_emissions():
    identifier = request.args.get('identifier')
    if not identifier:
        return jsonify({'error': 'No identifier provided'}), 400
    
    try:
        raw_data = scraper.fetch_emissions_data(identifier)
        processed_data = processor.process_data(raw_data)
        return jsonify(processed_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)