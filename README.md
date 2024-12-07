# Carbon Emissions Tracker

A dynamic carbon emissions data retrieval system for MSCI AW companies, focusing on Scope 1 and Scope 2 emissions from CSR reports.

## Features

- Fetch carbon emissions data using ISIN or company name
- Process and standardize emissions data
- RESTful API for data access
- Mock data implementation for proof of concept

## Setup

1. Clone the repository:
```bash
git clone https://github.com/neil-72/carbon-emissions-tracker.git
cd carbon-emissions-tracker
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

## API Usage

### Get Emissions Data

```http
GET /api/emissions?identifier=YOUR_ISIN_OR_COMPANY_NAME
```

Example Response:
```json
{
  "company_info": {
    "identifier": "US0378331005",
    "name": "Example Corp"
  },
  "emissions_data": {
    "scope1": 1000.50,
    "scope2": 2000.80,
    "reporting_year": 2023
  },
  "metadata": {
    "source": "Mock Data",
    "units": "metric tons CO2e"
  }
}
```

## Next Steps

1. Implement actual data scraping from CSR reports
2. Add data validation and error handling
3. Implement caching system
4. Add user interface
5. Add tests

## License

MIT