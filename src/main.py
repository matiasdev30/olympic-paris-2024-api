from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datasource.datasource import DataSource
from datasource.extractor import DataExtractor
from exceptions.exceptions import DataSourceError, DataExtractorError

app = FastAPI()

# URLs base e cabeçalhos para os diferentes datasets
base_url_games = "https://www.espn.com/olympics/summer/2024/results/_/date/202407"
url_records = "https://www.espn.com/olympics/summer/2024/medals"
url_athlete_medals = "https://www.espn.com/olympics/summer/2024/medals/_/view/athletes"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Funções auxiliares para criar DataSource com URLs dinâmicas
def get_data_source_games(day: str) -> DataSource:
    url = f"{base_url_games}{day}"
    return DataSource(url, headers)

data_source_records = DataSource(url_records, headers)
data_source_athlete_medals = DataSource(url_athlete_medals, headers)

@app.get("/games")
async def get_games(day: str):
    try:
        data_source_games = get_data_source_games(day)
        html_content_games = data_source_games.fetch_html()
        games_container = data_source_games.parse_html_games(html_content_games)
        games_data = DataExtractor.extract_data_games(games_container)
        return {"games_data": games_data}
    except (DataSourceError, DataExtractorError) as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

@app.get("/records")
async def get_records_by_country():
    try:
        html_content_records = data_source_records.fetch_html()
        records_table = data_source_records.parse_html_records(html_content_records)
        records_data = DataExtractor.extract_records_team(records_table)
        return {"records_data": records_data}
    except (DataSourceError, DataExtractorError) as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

@app.get("/athlete_medals")
async def get_athlete_medals():
    try:
        html_content_athlete_medals = data_source_athlete_medals.fetch_html()
        athlete_medals_table = data_source_athlete_medals.parse_html_records(html_content_athlete_medals)
        athlete_medals_data = DataExtractor.extract_records_athlete(athlete_medals_table)
        return {"athlete_medals_data": athlete_medals_data}
    except (DataSourceError, DataExtractorError) as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

# Comando para rodar o servidor
# uvicorn main:app --reload
