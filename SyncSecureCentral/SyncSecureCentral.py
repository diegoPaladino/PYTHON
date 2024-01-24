class AlarmSystem:
    def __init__(self, frequency):
        self.frequency = frequency
        self.electric_fence_active = False

    def remote_trigger(self, frequency):
        if frequency == self.frequency:
            self.activate_electric_fence()

    def activate_electric_fence(self):
        self.electric_fence_active = True
        print("Electric fence activated.")

    def deactivate_electric_fence(self):
        self.electric_fence_active = False
        print("Electric fence deactivated.")

# Exemplo de uso
security_center = AlarmSystem(433.92)  # Frequência em Hz
security_center.remote_trigger(433.92)
