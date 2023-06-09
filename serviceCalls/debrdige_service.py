import json
import logging
import os

import requests
from jsonschema import validate

from de_bridge_schemas import get_supported_chains_schema, get_tokens_by_chain_schema, get_allowance_schema, \
    estimate_bridge_schema, get_bridge_tx_schema

logger = logging.getLogger("api")


class DeBridge:
    def __init__(self):
        self.url = os.environ["BASE_URL"]

    class EstimateBridge:
        def __init__(self):
            self.url = os.environ['BASE_URL'] + 'estimateBridge'

        def estimate_bridge_not_query(self):
            response = requests.get(url=self.url)
            logger.info(f"Отправлен запрос на роут - {response.url}")
            logger.info(response.text)
            assert response.status_code == 400 and response.text == '{"ok":false,"data":null,"error":"\\"srcNet\\" is ' \
                                                                    'required"}', f"Ожидался status = 400, " \
                                                                                  f"пришел status = {response.status_code}. " \
                                                                                  f"Тело ответа: \n{response.text}."

            return response

        def estimate_bridge_native_to_not_native(self, src_net, dst_net, src_native_token, dst_not_native_token):
            params = {'srcNet': src_net, 'srcTokenAddress': src_native_token, 'srcTokenAmount': 100000,
                      'dstNet': dst_net, 'dstTokenAddress': dst_not_native_token}
            response = requests.get(url=self.url, params=params)
            logger.info(f"Отправлен запрос на роут - {response.url}")
            logger.info(response.text)
            assert response.status_code == 200, f"Ожидался status = 200, " \
                                                f"пришел status = {response.status_code}. " \
                                                f"Тело ответа: \n{response.text}."
            validate(json.loads(response.text), estimate_bridge_schema)

            return response

        def estimate_bridge_stablecoin_to_not_native(self, src_net, dst_net, src_stable_coin, dst_not_native_token):
            params = {'srcNet': src_net, 'srcTokenAddress': src_stable_coin, 'srcTokenAmount': 100000,
                      'dstNet': dst_net, 'dstTokenAddress': dst_not_native_token}
            response = requests.get(url=self.url, params=params)
            logger.info(f"Отправлен запрос на роут - {response.url}")
            logger.info(response.text)
            assert response.status_code == 200, f"Ожидался status = 200, " \
                                                f"пришел status = {response.status_code}. " \
                                                f"Тело ответа: \n{response.text}."
            validate(json.loads(response.text), estimate_bridge_schema)

            return response

        def estimate_bridge_not_native_to_native(self, src_net, dst_net, src_not_native_token, dst_native_token):
            params = {'srcNet': src_net, 'srcTokenAddress': src_not_native_token, 'srcTokenAmount': 100000,
                      'dstNet': dst_net, 'dstTokenAddress': dst_native_token}
            response = requests.get(url=self.url, params=params)
            logger.info(f"Отправлен запрос на роут - {response.url}")
            logger.info(response.text)
            assert response.status_code == 200, f"Ожидался status = 200, " \
                                                f"пришел status = {response.status_code}. " \
                                                f"Тело ответа: \n{response.text}."
            validate(json.loads(response.text), estimate_bridge_schema)

            return response

        def estimate_bridge_not_native_to_not_native(self, src_net, dst_net, src_not_native_token,
                                                     dst_not_native_token):
            params = {'srcNet': src_net, 'srcTokenAddress': src_not_native_token, 'srcTokenAmount': 100000,
                      'dstNet': dst_net, 'dstTokenAddress': dst_not_native_token}
            response = requests.get(url=self.url, params=params)
            logger.info(f"Отправлен запрос на роут - {response.url}")
            logger.info(response.text)
            assert response.status_code == 200, f"Ожидался status = 200, " \
                                                f"пришел status = {response.status_code}. " \
                                                f"Тело ответа: \n{response.text}."
            validate(json.loads(response.text), estimate_bridge_schema)

            return response

    def get_allowance(
            self, net, not_native_token,
            owner):
        url = f"{self.url}getAllowance"
        params = {'net': net, 'tokenAddress': not_native_token, 'owner': owner}
        response = requests.get(url=url, params=params)
        logger.info(f"Отправлен запрос на роут - {response.url}")
        logger.info(response.text)
        assert response.status_code == 200, f"Ожидался status = 200, " \
                                            f"пришел status = {response.status_code}. " \
                                            f"Тело ответа: \n{response.text}."
        validate(json.loads(response.text),
                 get_allowance_schema), f"Ответ от сервера не соответствует ожидаемой схеме. Поля: {get_allowance_schema}"

        return response

    def get_approve_tx(self):
        url = f"{self.url}getApproveTx"
        response = requests.get(url=url)
        logger.info(f"Отправлен запрос на роут - {response.url}")
        logger.info(response.text)
        assert response.status_code == 400 and response.text == '{"ok":false,"data":null,"error":"\\"net\\"' \
                                                                ' is required"}', f"Ожидался status = 400, " \
                                                                                  f"пришел status = {response.status_code}. " \
                                                                                  f"Тело ответа: \n{response.text}."

        return response

    def get_approve_tx_query_params(self, net, token_address, owner):
        url = f"{self.url}getApproveTx"
        params = {'net': net, 'tokenAddress': token_address, 'owner': owner}
        response = requests.get(url=url, params=params)
        logger.info(f"Отправлен запрос на роут - {response.url}")
        logger.info(response.text)
        assert response.status_code == 200, f"Ожидался status = 200, " \
                                            f"пришел status = {response.status_code}. " \
                                            f"Тело ответа: \n{response.text}."

        return response

    def get_supported_chains(self):
        url = f"{self.url}getSupportedChains"
        response = requests.get(url=url)
        logger.info(f"Отправлен запрос на роут - {response.url}")
        logger.info(response.text)
        assert response.status_code == 200, f"Ожидался status = 200, " \
                                            f"пришел status = {response.status_code}. " \
                                            f"Тело ответа: \n{response.text}."
        validate(json.loads(response.text), get_supported_chains_schema)
        return response

    def get_tokens_by_chain(self, chain_id):
        url = f"{self.url}getTokensByChain"
        params = {'chainId': chain_id}
        response = requests.get(url=url, params=params)
        logger.info(f"Отправлен запрос на роут - {response.url}")
        logger.info(response.text)
        assert response.status_code == 200, f"Ожидался status = 200, " \
                                            f"пришел status = {response.status_code}. " \
                                            f"Тело ответа: \n{response.text}."
        validate(json.loads(response.text), get_tokens_by_chain_schema)
        return response

    def get_bridge_tx(self, src_net, dst_net, src_token_address, dst_token_address, src_token_amount,
                      dst_chain_recipient_address, dst_chain_fallback_address, owner):
        params = {'srcNet': src_net, 'srcTokenAddress': src_token_address, 'srcTokenAmount': src_token_amount,
                  'dstNet': dst_net, 'dstTokenAddress': dst_token_address,
                  'dstChainRecipientAddress': dst_chain_recipient_address,
                  'dstChainFallbackAddress': dst_chain_fallback_address, 'owner': owner}
        response = requests.get(url=self.url, params=params)
        logger.info(f"Отправлен запрос на роут - {response.url}")
        logger.info(response.text)
        assert response.status_code == 200, f"Ожидался status = 200, " \
                                            f"пришел status = {response.status_code}. " \
                                            f"Тело ответа: \n{response.text}."
        validate(json.loads(response.text), get_bridge_tx_schema)

        return response
