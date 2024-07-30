  Olympic Paris 2024 API

Olympic Paris 2024 API
======================

This project provides an API for accessing Olympic Games data for the Paris 2024 Olympics. The API fetches and processes data related to game results, medal records by country, and individual athlete medals.

Features
--------

*   **Fetch Game Results**: Retrieve results for specific dates of the Olympic Games.
*   **Overall Medal Leaders by Country**: Get the top medal-winning countries based on overall medal counts.
*   **Individual Medal Leaders by Country**: Retrieve the top individual athletes by medal count, categorized by gold, silver, and bronze.

Installation
------------

### Prerequisites

Ensure you have Python 3.8+ installed on your system.

### Clone the Repository

    git clone https://github.com/yourusername/your-repo.git
    cd your-repo

### Create a Virtual Environment

    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate

### Install Dependencies

    pip install -r requirements.txt

Usage
-----

### Run the API Server

To start the FastAPI server, use:

    uvicorn src.main:app --reload

The server will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### API Endpoints

*   **Fetch Game Results**
    *   **Endpoint**: `/games`
    *   **Method**: GET
    *   **Parameters**: `day` (in the format `YYYYMMDD`, e.g., `20240730`)
    *   **Example request**:
        
            curl "http://127.0.0.1:8000/games?day=20240730"
        
*   **Overall Medal Leaders by Country**
    *   **Endpoint**: `/medal-leaders/countries`
    *   **Method**: GET
    *   **Example request**:
        
            curl "http://127.0.0.1:8000/medal-leaders/countries"
        
*   **Individual Medal Leaders by Country**
    *   **Endpoint**: `/medal-leaders/athletes`
    *   **Method**: GET
    *   **Example request**:
        
            curl "http://127.0.0.1:8000/medal-leaders/athletes"
        

Error Handling
--------------

The API includes error handling for common issues like invalid parameters or data fetch errors. Errors are returned in the following format:

    {
      "detail": "Error description"
    }

Contributing
------------

Feel free to submit issues or pull requests if you have suggestions or improvements.

License
-------

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
