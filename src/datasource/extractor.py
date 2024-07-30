from exceptions.exceptions import DataExtractorError

class DataExtractor:
    @staticmethod
    def extract_data_games(container):
        data = []
        try:
            tables = container.find_all('table', class_='olympics results results--post') + \
                     container.find_all('table', class_='olympics results results--in')
            for table in tables:
                title_row = table.find('tr', class_='column-group')
                event_title = title_row.find('th').text.strip() if title_row else "Título não encontrado"
                in_progress = 'results--in' in table.get('class', [])
                status = "In Progress" if in_progress else "Completed"
                date_row = table.find('tr', style='display: none;')
                date_text = date_row.find('th', class_='date').text.strip() if date_row else "N/A"
                teams = []
                winner = None
                rows = table.find_all('tr', class_='home')
                for row in rows:
                    is_winner = 'winner' in row.get('class', [])
                    medal_img = row.find('td').find('img')
                    medal = medal_img['alt'] if medal_img else "No Medal"
                    team_cells = row.find('td', class_='team')
                    if team_cells:
                        team_name = team_cells.find('abbr', class_='country_name--long').text.strip() if team_cells.find('abbr', class_='country_name--long') else "N/A"
                        team_abbr = team_cells.find('abbr', class_='country_name--abbrev').text.strip() if team_cells.find('abbr', class_='country_name--abbrev') else "N/A"
                        team_points = row.find_all('td')[-1].find('span', class_='point').text.strip() if row.find_all('td')[-1].find('span', class_='point') else "0"
                    else:
                        team_name = team_abbr = "N/A"
                        team_points = "0"
                    players_cell = row.find('td', class_='player')
                    player_names = players_cell.get_text(separator=', ').strip() if players_cell else "N/A"
                    team_info = {
                        'Team/Atleta': team_name,
                        'Abbreviation': team_abbr,
                        'Points': team_points,
                        'Players': player_names,
                        'Medal': medal,
                        'Status': 'Winner' if is_winner else 'Not Winner'
                    }
                    if is_winner:
                        winner = team_name
                    teams.append(team_info)
                data.append({
                    'Event': event_title,
                    'Date': date_text,
                    'Teams': teams,
                    'Status': status,
                    'Winner': winner
                })
        except Exception as e:
            raise DataExtractorError(f"Error extracting data: {e}")
        return data

    
    @staticmethod
    def extract_records_team(table):
        data = []
        try:
            rows = table.find('tbody').find_all('tr')
            medals_list = []

            for row in rows:
                team = row.find('td', class_='team')
                team_name = team.find('span', class_='country_name--long').text.strip() if team else "N/A"
                team_abbr = team.find('span', class_='country_name--abbrev').text.strip() if team else "N/A"
                
                # Assegure-se de capturar os valores corretos de medalhas (Ouro, Prata, Bronze)
                i = 0
                c = 0
                
                medals = {}
                for t in row.find_all('td', class_=""):
                    c += 1
                    if c == 1 : medals["G"] = t.text
                    if c == 2 : medals["S"] = t.text
                    if c == 3 : medals["B"] = t.text
                    if c == 4 : medals["Total"] = t.text

                    if c == 4:
                        medals_list.append(medals)
            c = 0
            for row in rows:
                    team = row.find('td', class_='team')
                    team_name = team.find('span', class_='country_name--long').text.strip() if team else "N/A"
                    team_abbr = team.find('span', class_='country_name--abbrev').text.strip() if team else "N/A"
                    
                    # Assegure-se de capturar os valores corretos de medalhas (Ouro, Prata, Bronze)

                    data.append({
                        'Team': team_name,
                        'Abbreviation': team_abbr,
                        'Medals' : medals_list[c]
                    })

                    c += 1


        except Exception as e:
            raise DataExtractorError(f"Error extracting records: {e}")
        return data
    
    @staticmethod
    def extract_records_athlete(table):
        data = []
        try:
            rows = table.find('tbody').find_all('tr')
            medals_list = []

            for row in rows:
                athlete_data = row.find('td', class_='team')
                athlete_name = athlete_data.text.strip() if athlete_data else "N/A"
                country_name = athlete_data.find('img')['title'] if athlete_data else "N/A"
                
                # Assegure-se de capturar os valores corretos de medalhas (Ouro, Prata, Bronze)
                c = 0
                medals = {}
                for t in row.find_all('td', class_=""):
                    c += 1
                    if c == 1: medals["G"] = t.text
                    if c == 2: medals["S"] = t.text
                    if c == 3: medals["B"] = t.text
                    if c == 4: medals["Total"] = t.text

                    if c == 4:
                        medals_list.append(medals)
            
            c = 0
            for row in rows:
                athlete_data = row.find('td', class_='team')
                athlete_name = athlete_data.text.strip() if athlete_data else "N/A"
                country_name = athlete_data.find('img')['title'] if athlete_data else "N/A"

                data.append({
                    'Athlete': athlete_name,
                    'Country': country_name,
                    'Medals': medals_list[c]
                })

                c += 1

        except Exception as e:
            raise DataExtractorError(f"Error extracting records: {e}")
        return data

