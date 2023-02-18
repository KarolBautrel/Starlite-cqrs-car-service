class CarUtils:

    def merge_events_to_one_list(self, nested_list):
        flatten_list = [item for sublist in nested_list for item in sublist]

        return flatten_list

    def sort_by_dates(self, events: list):

        sorted_events = sorted(events, key=lambda e: e.sequence_number)
        return sorted_events

    def prepare_list_data(self, nested_events):
        sorted_events_by_id = self.sort_events_by_ids(nested_events)
        prepared_data = self.sort_events_by_sequence_number(sorted_events_by_id)
        return prepared_data
    def sort_events_by_ids(self, nested_events):
        event_dict = {}
        for event_created in nested_events[0]:
            event_dict[event_created.car_id] = []
        for events in nested_events:
            for event in events:
                event_dict.get(event.car_id).append(event)

        return event_dict

    def sort_events_by_sequence_number(self, event_dict):
        for event_list in event_dict.values():
            event_list.sort(key=lambda e: e.sequence_number)
        return event_dict