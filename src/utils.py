from exceptions.exceptions import DataPrinterError


class DataPrinter:
    @staticmethod
    def print_data(data):
        if not isinstance(data, list):
            raise DataPrinterError("Data must be a list.")

        for entry in data:
            print(f"Event: {entry['Event']}")
            print(f"Date: {entry['Date']}")
            print(f"Status: {entry['Status']}")
            print("Teams:")
            for team in entry['Teams']:
                print(f"  Team/Atleta: {team['Team/Atleta']}")
                print(f"  Abbreviation: {team['Abbreviation']}")
                print(f"  Points: {team['Points']}")
                print(f"  Players: {team['Players']}")
                print(f"  Medal: {team['Medal']}")
                print(f"  Status: {team['Status']}")
                print()
            if entry['Winner']:
                print(f"Winner: {entry['Winner']['Team/Atleta']}")
                print()
            print("="*40)
            print()
