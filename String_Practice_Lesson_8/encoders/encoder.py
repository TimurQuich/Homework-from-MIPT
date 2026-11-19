import json

class JsonStrategy:
    def save(self, file_path, objects_list):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump({"objects": objects_list}, f, indent=4)


class CsvStrategy:
    def save(self, file_path, objects_list):
        if not objects_list:
            return
        headers = objects_list[0].keys()

        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            f.write(",".join(headers) + "\n")
            for obj in objects_list:
                row = [str(obj[key]) for key in headers]
                f.write(",".join(row) + "\n")


class HistEncoder:
    @staticmethod
    def encode(file_path, data):
        has_hu = len(data) == 6
        x_list, y_list, w_list, h_list, area_list = data[0], data[1], data[2], data[3], data[4]

        formatted_objects = []
        for i in range(len(area_list)):
            obj = {
                "x": int(x_list[i]),
                "y": int(y_list[i]),
                "w": int(w_list[i]),
                "h": int(h_list[i]),
                "area": int(area_list[i])
            }
            if has_hu:
                obj["hu"] = [round(float(m), 4) for m in data[5][i]]
            formatted_objects.append(obj)

        if file_path.endswith('.json'):
            strategy = JsonStrategy()
        elif file_path.endswith('.csv'):
            strategy = CsvStrategy()
        else:
            raise ValueError("The format doesn't fit")

        strategy.save(file_path, formatted_objects)
