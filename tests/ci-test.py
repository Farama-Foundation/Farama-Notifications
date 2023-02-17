from Farama_Notifications.notifications import notifications

if __name__ == "__main__":
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
            ), f"notifications for each package-version combindation must be a string, got {type(notifications[package][version])}."
