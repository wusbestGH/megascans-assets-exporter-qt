import json, os

class JsonSettings():
    def json_create_read(self):
        self.settings_json = "settings.json"
        self.settings_data = {}
        if os.path.exists(self.settings_json) and os.path.getsize(self.settings_json) > 0:
            with open('settings.json', 'r') as file:
                self.settings_data = json.load(file)
                print("Settings:", self.settings_data)
        else:
            with open('settings.json', 'w') as file:
                json.dump({}, file)
                print("Settings:", self.settings_data)

    def save_settings(self, data):
        print("Saving to JSON:", data)
        with open('settings.json', 'w') as file:
            json.dump(data, file)