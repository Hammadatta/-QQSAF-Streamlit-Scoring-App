import json
import os


def test_each_domain_has_seven_controls():
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "qsaf_controls_all_domains.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    for domain, controls in data.items():
        assert len(controls) == 7, f"{domain} expected 7 controls, got {len(controls)}"
