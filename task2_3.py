from mrjob.job import MRJob
from mrjob.step import MRStep

class TopEventsByDecade(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.map_athlete_events,
                   combiner=self.combine_event_counts,
                   reducer=self.reduce_event_counts),
            MRStep(reducer=self.sort_and_select_top_events),
            MRStep(reducer=self.format_output)
        ]

    def map_athlete_events(self, _, line):
        athlete_info = line.split(" | ")
        competition_year = int(athlete_info[2])
        athlete_country = athlete_info[1]
        event_name = athlete_info[3] 
        medal_type = athlete_info[4].strip() 
        decade = (competition_year // 10) * 10
        
        yield (decade, athlete_country, event_name), 1

    def combine_event_counts(self, key, values):
        yield key, sum(values)

    def reduce_event_counts(self, key, values):
        decade, country, event = key
        yield decade, (sum(values), country, event)

    def sort_and_select_top_events(self, decade, event_data):
        sorted_events = sorted(event_data, reverse=True, key=lambda x: x[0])
        
        top_three_events = sorted_events[:3]
        
        decade_range = f"{decade}-{decade+9}"
        
        for medal_count, country, event in top_three_events:
            yield None, (decade_range, [country, event, medal_count])

    def format_output(self, _, decade_event_data):
        all_data = list(decade_event_data)
        all_data_sorted = sorted(all_data, reverse=True, key=lambda x: x[0])
        
        for decade_range, event_info in all_data_sorted:
            yield decade_range, event_info

if __name__ == "__main__":
    TopEventsByDecade.run()
