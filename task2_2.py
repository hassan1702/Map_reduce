from mrjob.job import MRJob
from mrjob.step import MRStep

class TopCountriesByGoldMedals(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.map_country_medals,
                   reducer=self.count_medals),
            MRStep(mapper=self.map_sort_by_gold,
                   reducer=self.get_top_three_countries)
        ]

    def map_country_medals(self, _, line):
        athlete_info = line.split(" | ")
        athlete_country = athlete_info[1]
        medal_type = athlete_info[4]
        if medal_type in ['Gold', 'Silver', 'Bronze']:
            yield athlete_country, (medal_type, 1)

    def count_medals(self, country, values):
        gold_medals = 0
        silver_medals = 0
        bronze_medals = 0
        for medal_type, count in values:
            if medal_type == 'Gold':
                gold_medals += count
            elif medal_type == 'Silver':
                silver_medals += count
            elif medal_type == 'Bronze':
                bronze_medals += count
        yield country, (gold_medals, silver_medals, bronze_medals)

    def map_sort_by_gold(self, country, medal_counts):
        gold_medals, silver_medals, bronze_medals = medal_counts
        yield None, (gold_medals, country, silver_medals, bronze_medals)

    def get_top_three_countries(self, _, values):
        sorted_countries = sorted(values, reverse=True, key=lambda x: x[0])
        top_three_countries = sorted_countries[:3]

        for gold_medals, country, silver_medals, bronze_medals in top_three_countries:
            medal_counts = {"Gold": gold_medals, "Silver": silver_medals, "Bronze": bronze_medals}
            yield country, medal_counts

if __name__ == "__main__":
    TopCountriesByGoldMedals.run()
