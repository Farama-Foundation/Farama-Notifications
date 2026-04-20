# notifications are a dict of dicts
notifications = dict()

###############################################################
# Example notification for project/version, follow this format
###############################################################
# notifications["project_name"] = dict()
# notifications["project_name"]["version_number"] = "Notification message."

GYMNASIUM_ROBOTICS_ADROIT_WARNING = (
    "The AdroitHandRelocateDense-v1, AdroitHandHammerDense-v1, "
    "AdroitHandDoorDense-v1 environments versions have bug and should be used "
    "for reproducibility, use gymansium-robotics==1.2.0 if you want to test "
    "those environments or use version 2 of the environments with "
    "gymansium-robotics>=1.4.3, see "
    "https://github.com/Farama-Foundation/Gymnasium-Robotics/pull/220 for more details"
)

GYMNASIUM_ROBOTICS_ADROIT_VERSIONS = {
    version: GYMNASIUM_ROBOTICS_ADROIT_WARNING
    for version in (
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
    )
}

notifications["gymnasium_robotics"] = GYMNASIUM_ROBOTICS_ADROIT_VERSIONS
