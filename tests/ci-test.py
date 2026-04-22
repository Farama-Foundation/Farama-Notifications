import sys
from pathlib import Path


def test_gymnasium_robotics_notifications(notifications):
    expected_versions = {
        "1.2.1",
        "1.2.2",
        "1.2.3",
        "1.2.4",
        "1.3.0",
        "1.3.1",
        "1.3.2",
        "1.4.0",
        "1.4.1",
        "1.4.2",
    }
    expected_message = "AdroitHandRelocateDense-v1, AdroitHandHammerDense-v1, AdroitHandDoorDense-v1 environment's reward functions were updated in v1.2.1 without an environment version update. Therefore, use gymnasium-robotics==1.2.0 for v1 reproducibility or use v2 in gymnasium-robotics>=1.4.3. See https://github.com/Farama-Foundation/Gymnasium-Robotics/pull/220 for more details"

    assert "gymnasium_robotics" in notifications, "gymnasium_robotics notifications must be present."
    assert set(notifications["gymnasium_robotics"]) == expected_versions, (
        "gymnasium_robotics notifications must match the affected versions."
    )

    for version in expected_versions:
        assert notifications["gymnasium_robotics"][version] == expected_message, (
            f"gymnasium_robotics {version} warning text must match expected message."
        )


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

    from farama_notifications import notifications

    assert isinstance(
        notifications, dict
    ), f"notifications must be a dict, got {type(notifications)}."

    for package in notifications:
        assert isinstance(
            notifications[package], dict
        ), f"package notifications must be a dict of versions, got {type(notifications[package])}."

        for version in notifications[package]:
            assert isinstance(
                notifications[package][version], str
            ), f"notifications for each package-version combination must be a string, got {type(notifications[package][version])}."

    test_gymnasium_robotics_notifications(notifications)
