class CarUtils:



    def merge_events_to_one_list(self, nested_list):
       flatten_list = [item for sublist in nested_list for item in sublist]

       return flatten_list
    def sort_by_dates(self, events:list):
        sorted_events =  sorted(events, key = lambda e:e.created)

        return sorted_events