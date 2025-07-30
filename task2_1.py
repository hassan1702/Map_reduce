from mrjob.job import MRJob
from mrjob.step import MRStep

class TopAthletesByMedal(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.map_athlete_medals,
                   reducer=self.count_medals),
            MRStep(mapper=self.map_sort_by_medal,
                   reducer=self.get_top_three)
        ]

    def map_athlete_medals(self, _, line):
        athlete_info = line.split(" | ")
        athlete_id = int(athlete_info[0])
        medal_type = athlete_info[4]
        if medal_type in ['Gold', 'Silver', 'Bronze']:
            yield (athlete_id, medal_type), 1

    def count_medals(self, key, values):
        athlete_id, medal_type = key
        total_medals = sum(values)
        yield (medal_type, athlete_id), total_medals

    def map_sort_by_medal(self, key, total_medals):
        medal_type, athlete_id = key
        yield medal_type, (total_medals, athlete_id)

    def get_top_three(self, medal_type, values):
        medal_type = medal_type.upper()
        values = list(values)
        values.sort(reverse=True)
        top_three_athletes = values[:3]
        for total_medals, athlete_id in top_three_athletes:
            yield medal_type, [athlete_id, total_medals]

if __name__ == "__main__":
    TopAthletesByMedal.run()