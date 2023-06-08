import pytest

from serviceCalls.debrdige_service import DeBridge
from serviceCalls.helper import de_bridge_keys_data

networks = list(de_bridge_keys_data().keys())


def test_get_supported_chains():
    DeBridge().get_supported_chains()


def test_estimate_bridge():
    DeBridge().EstimateBridge().estimate_bridge_not_query()


@pytest.mark.parametrize("src_nets", networks)
@pytest.mark.parametrize("dst_nets", networks)
def test_estimate_bridge_native_to_not_native(src_nets, dst_nets):
    src_net = de_bridge_keys_data()[src_nets].get('net')
    dst_net = de_bridge_keys_data()[dst_nets].get('net')
    src_native_token = de_bridge_keys_data()[src_nets].get('nativeToken')
    dst_not_native_token = de_bridge_keys_data()[dst_nets].get('notNativeToken')
    DeBridge().EstimateBridge().estimate_bridge_native_to_not_native(src_net=src_net, dst_net=dst_net,
                                                                     src_native_token=src_native_token,
                                                                     dst_not_native_token=dst_not_native_token)


@pytest.mark.parametrize("src_nets", networks)
@pytest.mark.parametrize("dst_nets", networks)
def test_estimate_bridge_stablecoin_to_not_native(src_nets, dst_nets):
    src_net = de_bridge_keys_data()[src_nets].get('net')
    dst_net = de_bridge_keys_data()[dst_nets].get('net')
    src_stable_coin = de_bridge_keys_data()[src_nets].get('stableCoin')
    dst_not_native_token = de_bridge_keys_data()[dst_nets].get('notNativeToken')
    DeBridge().EstimateBridge().estimate_bridge_stablecoin_to_not_native(src_net=src_net, dst_net=dst_net,
                                                                         src_stable_coin=src_stable_coin,
                                                                         dst_not_native_token=dst_not_native_token)


@pytest.mark.parametrize("src_nets", networks)
@pytest.mark.parametrize("dst_nets", networks)
def test_estimate_bridge_not_native_to_native(src_nets, dst_nets):
    src_net = de_bridge_keys_data()[src_nets].get('net')
    dst_net = de_bridge_keys_data()[dst_nets].get('net')
    dst_native_token = de_bridge_keys_data()[dst_nets].get('nativeToken')
    src_not_native_token = de_bridge_keys_data()[src_nets].get('notNativeToken')
    DeBridge().EstimateBridge().estimate_bridge_not_native_to_native(src_net=src_net, dst_net=dst_net,
                                                                     src_not_native_token=src_not_native_token,
                                                                     dst_native_token=dst_native_token)


@pytest.mark.parametrize("src_nets", networks)
@pytest.mark.parametrize("dst_nets", networks)
def test_estimate_bridge_not_native_to_not_native(src_nets, dst_nets):
    src_net = de_bridge_keys_data()[src_nets].get('net')
    dst_net = de_bridge_keys_data()[dst_nets].get('net')
    src_not_native_token = de_bridge_keys_data()[src_nets].get('notNativeToken')
    dst_not_native_token = de_bridge_keys_data()[dst_nets].get('notNativeToken')
    if src_net != dst_net:
        DeBridge().EstimateBridge().estimate_bridge_not_native_to_not_native(src_net=src_net, dst_net=dst_net,
                                                                         src_not_native_token=src_not_native_token,
                                                                         dst_not_native_token=dst_not_native_token)
    else:
        pytest.skip("Сеть отправления = сети назначения")


@pytest.mark.parametrize("network", networks)  # todo разобрать ошибку
def test_get_allowance(network):  # "error":"No available RPC's for ETH"
    net = de_bridge_keys_data()[network].get('net')
    not_native_token = de_bridge_keys_data()[network].get('notNativeToken')
    owner = de_bridge_keys_data()[network].get('owner')
    DeBridge().get_allowance(net=net, not_native_token=not_native_token, owner=owner)


@pytest.mark.special()
def test_get_approve_tx():  # error":"Network undefined is not available in DeBridge"
    DeBridge().get_approve_tx()


@pytest.mark.parametrize("network", networks)
def test_get_approve_tx_not_native_token(network):
    net = de_bridge_keys_data()[network].get('net')
    owner = de_bridge_keys_data()[network].get('owner')
    token_address = de_bridge_keys_data()[network].get('notNativeToken')
    DeBridge().get_approve_tx_query_params(net=net, owner=owner, token_address=token_address)


@pytest.mark.parametrize("network", networks)
def test_get_approve_tx_native_token(network):
    net = de_bridge_keys_data()[network].get('net')
    owner = de_bridge_keys_data()[network].get('owner')
    token_address = de_bridge_keys_data()[network].get('nativeToken')
    DeBridge().get_approve_tx_query_params(net=net, owner=owner, token_address=token_address)


@pytest.mark.parametrize("network", networks)
def test_get_approve_tx_stablecoin(network):
    net = de_bridge_keys_data()[network].get('net')
    owner = de_bridge_keys_data()[network].get('owner')
    token_address = de_bridge_keys_data()[network].get('stableCoin')
    DeBridge().get_approve_tx_query_params(net=net, owner=owner, token_address=token_address)


@pytest.mark.parametrize("network", networks)
def test_get_tokens_by_chain(network):
    chain_id = de_bridge_keys_data()[network].get('chainId')
    DeBridge().get_tokens_by_chain(chain_id=chain_id)


@pytest.mark.parametrize("src_network", networks)
@pytest.mark.parametrize("dst_network", networks)
def test_get_bridge_tx_not_native_to_not_native(src_network, dst_network):
    src_net = de_bridge_keys_data()[src_network].get('net')
    dst_net = de_bridge_keys_data()[dst_network].get('net')
    src_token_address = de_bridge_keys_data()[src_network].get('notNativeToken')
    dst_token_address = de_bridge_keys_data()[dst_network].get('notNativeToken')
    src_token_amount = 100000
    dst_chain_recipient_address = de_bridge_keys_data()[dst_network].get('owner')
    dst_chain_fallback_address = de_bridge_keys_data()[dst_network].get('owner')
    owner = de_bridge_keys_data()[dst_network].get('owner')
    if src_net != dst_net:
        DeBridge().get_bridge_tx(src_net=src_net, dst_net=dst_net, src_token_address=src_token_address,
                                 dst_token_address=dst_token_address, src_token_amount=src_token_amount,
                                 dst_chain_recipient_address=dst_chain_recipient_address,
                                 dst_chain_fallback_address=dst_chain_fallback_address, owner=owner)
    else:
        pytest.skip("Сеть отправления = сети назначения")


@pytest.mark.parametrize("src_network", networks)
@pytest.mark.parametrize("dst_network", networks)
def test_get_bridge_tx_native_to_not_native(src_network, dst_network):
    src_net = de_bridge_keys_data()[src_network].get('net')
    dst_net = de_bridge_keys_data()[dst_network].get('net')
    src_token_address = de_bridge_keys_data()[src_network].get('nativeToken')
    dst_token_address = de_bridge_keys_data()[dst_network].get('notNativeToken')
    src_token_amount = 10000
    dst_chain_recipient_address = de_bridge_keys_data()[dst_network].get('owner')
    dst_chain_fallback_address = de_bridge_keys_data()[dst_network].get('owner')
    owner = de_bridge_keys_data()[dst_network].get('owner')
    if src_net != dst_net:
        DeBridge().get_bridge_tx(src_net=src_net, dst_net=dst_net, src_token_address=src_token_address,
                                 dst_token_address=dst_token_address, src_token_amount=src_token_amount,
                                 dst_chain_recipient_address=dst_chain_recipient_address,
                                 dst_chain_fallback_address=dst_chain_fallback_address, owner=owner)
    else:
        pytest.skip("Сеть отправления = сети назначения")


@pytest.mark.parametrize("src_network", networks)
@pytest.mark.parametrize("dst_network", networks)
def test_get_bridge_tx_not_native_to_native(src_network, dst_network):
    src_net = de_bridge_keys_data()[src_network].get('net')
    dst_net = de_bridge_keys_data()[dst_network].get('net')
    src_token_address = de_bridge_keys_data()[src_network].get('notNativeToken')
    dst_token_address = de_bridge_keys_data()[dst_network].get('nativeToken')
    src_token_amount = 10000
    dst_chain_recipient_address = de_bridge_keys_data()[dst_network].get('owner')
    dst_chain_fallback_address = de_bridge_keys_data()[dst_network].get('owner')
    owner = de_bridge_keys_data()[dst_network].get('owner')
    if src_net != dst_net:
        DeBridge().get_bridge_tx(src_net=src_net, dst_net=dst_net, src_token_address=src_token_address,
                                 dst_token_address=dst_token_address, src_token_amount=src_token_amount,
                                 dst_chain_recipient_address=dst_chain_recipient_address,
                                 dst_chain_fallback_address=dst_chain_fallback_address, owner=owner)
    else:
        pytest.skip("Сеть отправления = сети назначения")


@pytest.mark.parametrize("src_network", networks)
@pytest.mark.parametrize("dst_network", networks)
def test_get_bridge_tx_not_native_to_stablecoin(src_network, dst_network):
    src_net = de_bridge_keys_data()[src_network].get('net')
    dst_net = de_bridge_keys_data()[dst_network].get('net')
    src_token_address = de_bridge_keys_data()[src_network].get('notNativeToken')
    dst_token_address = de_bridge_keys_data()[dst_network].get('stableCoin')
    src_token_amount = 100000
    dst_chain_recipient_address = de_bridge_keys_data()[dst_network].get('owner')
    dst_chain_fallback_address = de_bridge_keys_data()[dst_network].get('owner')
    owner = de_bridge_keys_data()[dst_network].get('owner')
    if src_net != dst_net:
        DeBridge().get_bridge_tx(src_net=src_net, dst_net=dst_net, src_token_address=src_token_address,
                                 dst_token_address=dst_token_address, src_token_amount=src_token_amount,
                                 dst_chain_recipient_address=dst_chain_recipient_address,
                                 dst_chain_fallback_address=dst_chain_fallback_address, owner=owner)
    else:
        pytest.skip("Сеть отправления = сети назначения")


@pytest.mark.parametrize("src_network", networks)
@pytest.mark.parametrize("dst_network", networks)
def test_get_bridge_tx_native_to_stablecoin(src_network, dst_network):
    src_net = de_bridge_keys_data()[src_network].get('net')
    dst_net = de_bridge_keys_data()[dst_network].get('net')
    src_token_address = de_bridge_keys_data()[src_network].get('nativeToken')
    dst_token_address = de_bridge_keys_data()[dst_network].get('stableCoin')
    src_token_amount = 10000
    dst_chain_recipient_address = de_bridge_keys_data()[dst_network].get('owner')
    dst_chain_fallback_address = de_bridge_keys_data()[dst_network].get('owner')
    owner = de_bridge_keys_data()[dst_network].get('owner')
    if src_net != dst_net:
        DeBridge().get_bridge_tx(src_net=src_net, dst_net=dst_net, src_token_address=src_token_address,
                                 dst_token_address=dst_token_address, src_token_amount=src_token_amount,
                                 dst_chain_recipient_address=dst_chain_recipient_address,
                                 dst_chain_fallback_address=dst_chain_fallback_address, owner=owner)
    else:
        pytest.skip("Сеть отправления = сети назначения")


@pytest.mark.parametrize("src_network", networks)
@pytest.mark.parametrize("dst_network", networks)
def test_get_bridge_tx_stablecoin_to_native(src_network, dst_network):
    src_net = de_bridge_keys_data()[src_network].get('net')
    dst_net = de_bridge_keys_data()[dst_network].get('net')
    src_token_address = de_bridge_keys_data()[src_network].get('stableCoin')
    dst_token_address = de_bridge_keys_data()[dst_network].get('nativeToken')
    src_token_amount = 10000
    dst_chain_recipient_address = de_bridge_keys_data()[dst_network].get('owner')
    dst_chain_fallback_address = de_bridge_keys_data()[dst_network].get('owner')
    owner = de_bridge_keys_data()[dst_network].get('owner')
    if src_net != dst_net:
        DeBridge().get_bridge_tx(src_net=src_net, dst_net=dst_net, src_token_address=src_token_address,
                                 dst_token_address=dst_token_address, src_token_amount=src_token_amount,
                                 dst_chain_recipient_address=dst_chain_recipient_address,
                                 dst_chain_fallback_address=dst_chain_fallback_address, owner=owner)
    else:
        pytest.skip("Сеть отправления = сети назначения")


@pytest.mark.parametrize("src_network", networks)
@pytest.mark.parametrize("dst_network", networks)
def test_get_bridge_tx_stablecoin_to_not_native(src_network, dst_network):
    src_net = de_bridge_keys_data()[src_network].get('net')
    dst_net = de_bridge_keys_data()[dst_network].get('net')
    src_token_address = de_bridge_keys_data()[src_network].get('stableCoin')
    dst_token_address = de_bridge_keys_data()[dst_network].get('notNativeToken')
    src_token_amount = 10000
    dst_chain_recipient_address = de_bridge_keys_data()[dst_network].get('owner')
    dst_chain_fallback_address = de_bridge_keys_data()[dst_network].get('owner')
    owner = de_bridge_keys_data()[dst_network].get('owner')
    if src_net != dst_net:
        DeBridge().get_bridge_tx(src_net=src_net, dst_net=dst_net, src_token_address=src_token_address,
                                 dst_token_address=dst_token_address, src_token_amount=src_token_amount,
                                 dst_chain_recipient_address=dst_chain_recipient_address,
                                 dst_chain_fallback_address=dst_chain_fallback_address, owner=owner)
    else:
        pytest.skip("Сеть отправления = сети назначения")
