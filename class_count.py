import json
import glob
from PIL import Image
import numpy as np
from numpy import asarray

DATASET_LABELS_PATH = ""

def get_class_dist(path: str):
    image = Image.open(path)

    image = image.convert("RGB")

    image_np = asarray(image)
    assert len(image_np.shape) == 3

    unique = np.unique(image_np.reshape(-1, image_np.shape[2]), axis=0, return_counts=True)

    colors = unique[0]
    occurences = unique[1].tolist()

    results_dict = { }
    for color, pixels in zip(colors, occurences):
        results_dict[str(color.tolist())] = pixels

    return results_dict
        
def additive_merge(dict1: dict, dict2: dict) -> dict:
    out_dict = {**dict1, **dict2}
    for key, value in out_dict.items():
        if key in dict1 and key in dict2:
                out_dict[key] += dict1[key]
    return out_dict

if __name__ == "__main__":
    images = glob.glob(DATASET_LABELS_PATH + "*_labelTrainIds.png")

    results_list = []
    results_totals = {}


    count = 1
    for image_path in images:
        print(f"Doing {count}/{len(images)}: '{image_path}'")
        count += 1

        result = get_class_dist(image_path)

        results_list.append(result)
        results_totals = additive_merge(result, results_totals)
        
        with open("./results.json", 'w') as f:
            json.dump(results_list, f)
        with open("./results_totals.json", 'w') as f:
            json.dump(results_totals, f)