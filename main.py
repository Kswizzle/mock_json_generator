import json
import random
from fake_mapping import mapping
import numpy as np

NEB_DURATION = 300
STUDY_DURATION = 3600
BACKGROUND_DURATION = 300

EPOCH_START = 1641686248
EPOCH_END = 1670543872

def get_key_times(neb_start):
    template = {
            "NebStart": neb_start,
            "NebEnd": neb_start + NEB_DURATION,
            "DepStart": neb_start - BACKGROUND_DURATION,
            "DepEnd": neb_start + STUDY_DURATION
        }
    return template



def make_json():
    locations = list(mapping.keys())

    site_chosen = locations[random.randint(0, len(locations)-1)]
    print(site_chosen)
    site_data = mapping[site_chosen]
    start_time = random.randint(EPOCH_START, EPOCH_END)
    neb_mac = mapping[site_chosen]['devices'][0]
    sensors_macs = mapping[site_chosen]['devices'][1:]

    eACH_dic = dict(zip(sensors_macs, [random.uniform(0,10) for x in range(0,len(sensors_macs))]))
    eACH_score = np.array(list(eACH_dic.values())).mean()
    mock_json = {
        "id": neb_mac,
        "sensors": {
            "time": start_time,
            "location": site_chosen,
            "device_eACH": eACH_dic,
            "zone_eACH": eACH_score,
            "zone": mapping[site_chosen]["zone"],
            "site": mapping[site_chosen]["site"],
            "zone_id": mapping[site_chosen]["zone_id"],
            "site_id": mapping[site_chosen]["site_id"],
            "key_times": get_key_times(start_time),
            "occupancy": int(random.randint(0, 20)),
            "stay_safe_time": round(random.uniform(10.5, 300), 2),
            "stay_safe_occupancy": round(random.uniform(2, 50), 2),
            "vent_per_person":round(random.uniform(10.5, 75.5), 2),
            "infection_risk": round(random.uniform(10.5, 75.5), 2)
            },
        "type": "result"
    }
    print(mock_json)
    return mock_json

make_json()

dumm_list = []
for time in range(50):
    dumm_list.append(make_json())
with open("DummyData.json", 'r+') as dummyData_file:
    dummyJSON = {
        'DummyData': dumm_list
    }
    json.dump(dumm_list, dummyData_file, indent = 4)
