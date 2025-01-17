from nornir_routeros.plugins.tasks import routeros_command


def test_routeros_command(nr):
    result = nr.run(
        task=routeros_command,
        path="/",
        command="ping",
        address="127.0.0.1",
        count=5
    )
    assert len(result["router1"]) == 1
    device_result = result["router1"][0]
    assert device_result.failed is False, str(device_result.result)
    assert device_result.changed is False
