# Traffic Light Controller for a 2-lane Avenue
class TrafficLight:
    def __init__(self):
        self.green_light = False
        self.red_light = True

    def switch_lights(self):
        self.green_light, self.red_light = self.red_light, self.green_light

    def get_status(self):
        return "Green" if self.green_light else "Red"

# Automated Fish Feeder for Tilapia Aquaculture
class FishFeeder:
    def __init__(self):
        self.feeding_schedule = {
            "morning": "07:00",
            "noon": "12:00",
            "evening": "18:00"
        }

    def check_schedule(self, current_time):
        for time in self.feeding_schedule.values():
            if current_time == time:
                return True
        return False

    def feed_fish(self, current_time):
        if self.check_schedule(current_time):
            print("Feeding fish...")
        else:
            print("No feeding schedule at this time.")

# Example Usage
if __name__ == "__main__":
    traffic_light = TrafficLight()
    print("Current traffic light status:", traffic_light.get_status())
    traffic_light.switch_lights()
    print("Updated traffic light status:", traffic_light.get_status())

    fish_feeder = FishFeeder()
    current_time = "18:00"
    fish_feeder.feed_fish(current_time)
