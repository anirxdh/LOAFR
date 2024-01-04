from src.logfile import Logfile
import datetime

class Hnl:
    
    def __init__(self):
        self.output = ""
        return

    def apply_transform(self, data, event, high, low):
        for start, end in self.find_low_high_interval(data, event, high, low):
            duration = end - start
            self.output += f"Duration: {duration}, Start: {start}, End: {end}\n"
        return self.output
    
    def find_low_high_interval(self, data, event, high, low) -> (datetime, datetime):
        interval_started = False
        start_time = None
        for line in data.split('\n'):
            timestamp, _, _, event_type, value = Logfile.parse_line(line)
            if event_type.strip() == event.strip():
                if float(value[0]) <= low and not interval_started:
                    interval_started = True
                    start_time = timestamp
                elif float(value[0]) >= high and interval_started:
                    end_time = timestamp
                    yield start_time, end_time
                    interval_started = False
                    start_time = None
        return
