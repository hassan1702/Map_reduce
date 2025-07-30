from mrjob.job import MRJob
from mrjob.step import MRStep

class SortAthletesByID(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.map_athlete_data, reducer=self.collect_athlete_data),
            MRStep(reducer=self.sort_athletes)
        ]

    def map_athlete_data(self, _, line):
        athlete_info = line.split(" | ")
        athlete_id = int(athlete_info[0])
        athlete_country = athlete_info[1]
        competition_year = athlete_info[2]
        event_name = athlete_info[3]
        medal_type = athlete_info[4]
        athlete_details = [athlete_country, competition_year, event_name, medal_type]
        yield athlete_id, athlete_details

    def collect_athlete_data(self, athlete_id, details):
        for detail in details:
            yield None, (athlete_id, detail)

    def sort_athletes(self, _, athlete_data):
        sorted_athletes = sorted(athlete_data, key=lambda x: x[0])
        for athlete_id, detail in sorted_athletes:
            yield athlete_id, detail

if __name__ == "__main__":
    SortAthletesByID.run()
