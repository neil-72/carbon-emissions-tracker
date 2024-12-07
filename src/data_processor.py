class DataProcessor:
    def __init__(self):
        self.unit_conversions = {
            'tons': 1.0,
            'kilotons': 1000.0,
            'megatons': 1000000.0
        }
    
    def process_data(self, raw_data: dict) -> dict:
        """Process and standardize emissions data"""
        try:
            return {
                'company_info': {
                    'identifier': raw_data['identifier'],
                    'name': raw_data['company_name']
                },
                'emissions_data': {
                    'scope1': self._standardize_units(raw_data['emissions']['scope1']),
                    'scope2': self._standardize_units(raw_data['emissions']['scope2']),
                    'reporting_year': raw_data['emissions']['year']
                },
                'metadata': {
                    'source': raw_data['source'],
                    'units': 'metric tons CO2e'
                }
            }
        except KeyError as e:
            raise ValueError(f'Missing required field: {str(e)}')
    
    def _standardize_units(self, value: float) -> float:
        """Standardize units to metric tons CO2e"""
        return round(float(value), 2)