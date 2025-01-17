from nornir_routeros.plugins.tasks import routeros_get


def test_no_ssl(nr_no_ssl):
    result = nr_no_ssl.run(
        task=routeros_get,
        path="/system/identity"
    )
    assert len(result["router1"]) == 1
    device_result = result["router1"][0]
    assert device_result.failed is False
    assert device_result.changed is False
