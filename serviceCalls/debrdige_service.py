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
            response = requests.get(self.url)  # без query параметров
            logger.info(f"Отправлен запрос на роут - {response.url}")
            logger.info(response.text)
            assert response.status_code == 400 and response.text == '{"ok":false,"data":null,"error":"\\"srcNet\\" is ' \
                                                                    'required"}', f"Ожидался status = {400}, " \
                                                                                  f"пришел status = {response.status_code}. " \
                                                                                  f"Тело ответа: \n{response.text}."

            return response

        def estimate_bridge_native_to_not_native(self, net, native_token, not_native_token):
            response = requests.get(
                f"{self.url}?srcNet={net}&srcTokenAddress={native_token}"
                f"&srcTokenAmount=10&dstNet={net}&dstTokenAddress={not_native_token}")
            logger.info(f"Отправлен запрос на роут - {response.url}")
            logger.info(response.text)
            assert response.status_code == 200, f"Ожидался status = {200}, " \
                                                f"пришел status = {response.status_code}. " \
                                                f"Тело ответа: \n{response.text}."
            validate(json.loads(response.text), estimate_bridge_schema)

            return response

        def estimate_bridge_stablecoin_to_not_native(self, net, stable_coin, not_native_token):
            response = requests.get(
                f"{self.url}?srcNet={net}&srcTokenAddress={stable_coin}"
                f"&srcTokenAmount=10&dstNet={net}&dstTokenAddress={not_native_token}")
            logger.info(f"Отправлен запрос на роут - {response.url}")
            logger.info(response.text)
            assert response.status_code == 200, f"Ожидался status = {200}, " \
                                                f"пришел status = {response.status_code}. " \
                                                f"Тело ответа: \n{response.text}."
            validate(json.loads(response.text), estimate_bridge_schema)

            return response

        def estimate_bridge_not_native_to_native(self, net, not_native_token, native_token):
            response = requests.get(
                f"{self.url}?srcNet={net}&srcTokenAddress={not_native_token}"
                f"&srcTokenAmount=10&dstNet={net}&dstTokenAddress={native_token}")
            logger.info(f"Отправлен запрос на роут - {response.url}")
            logger.info(response.text)
            assert response.status_code == 200, f"Ожидался status = {200}, " \
                                                f"пришел status = {response.status_code}. " \
                                                f"Тело ответа: \n{response.text}."
            validate(json.loads(response.text), estimate_bridge_schema)

            return response

    def get_allowance(
            self, net, not_native_token,
            owner):  # todo: написать метод для урла с параметрами (параметры затребовать с Егора). в конфлюенс не
        # указан параметр net валится с 504 ошибкой. сделать после исправления
        response = requests.get(f"{self.url}getAllowance?net={net}&tokenAddress={not_native_token}&owner={owner}")
        logger.info(f"Отправлен запрос на роут - {response.url}")
        logger.info(response.text)
        assert response.status_code == 200, f"Ожидался status = {200}, " \
                                            f"пришел status = {response.status_code}. " \
                                            f"Тело ответа: \n{response.text}."
        validate(json.loads(response.text),
                 get_allowance_schema), f"Ответ от сервера не соответствует ожидаемой схеме. Поля: {get_allowance_schema}"

        return response

    def get_approve_tx(self):
        response = requests.get(f"{self.url}getApproveTx")
        logger.info(f"Отправлен запрос на роут - {response.url}")
        logger.info(response.text)
        assert response.status_code == 400 and response.text == '{"ok":false,"data":null,"error":"\\"net\\"' \
                                                                ' is required"}', f"Ожидался status = {400}, " \
                                                                                  f"пришел status = {response.status_code}. " \
                                                                                  f"Тело ответа: \n{response.text}."

        return response

    def get_approve_tx_query_params(self, net, token_address, owner):
        response = requests.get(f"{self.url}getApproveTx?tokenAddress={token_address}&net={net}&owner={owner}")
        logger.info(f"Отправлен запрос на роут - {response.url}")
        logger.info(response.text)
        assert response.status_code == 200, f"Ожидался status = {200}, " \
                                            f"пришел status = {response.status_code}. " \
                                            f"Тело ответа: \n{response.text}."

        return response

    def get_supported_chains(self):
        response = requests.get(f"{self.url}getSupportedChains")
        logger.info(f"Отправлен запрос на роут - {response.url}")
        logger.info(response.text)
        assert response.status_code == 200, f"Ожидался status = {200}, " \
                                            f"пришел status = {response.status_code}. " \
                                            f"Тело ответа: \n{response.text}."
        validate(json.loads(response.text), get_supported_chains_schema)
        return response

    def get_tokens_by_chain(self, chain_id):
        response = requests.get(f"{self.url}getTokensByChain?chainId={chain_id}")
        logger.info(f"Отправлен запрос на роут - {response.url}")
        logger.info(response.text)
        assert response.status_code == 200, f"Ожидался status = {200}, " \
                                            f"пришел status = {response.status_code}. " \
                                            f"Тело ответа: \n{response.text}."
        validate(json.loads(response.text), get_tokens_by_chain_schema)
        return response

    def get_bridge_tx(self, src_net, dst_net, src_token_address, dst_token_address, src_token_amount,
                      dst_chain_recipient_address, dst_chain_fallback_address, owner):
        response = requests.get(
            f"{self.url}getBridgeTx?srcNet={src_net}&srcTokenAddress={src_token_address}&"
            f"srcTokenAmount={src_token_amount}&dstNet={dst_net}&dstTokenAddress={dst_token_address}&"
            f"dstChainRecipientAddress={dst_chain_recipient_address}&"
            f"dstChainFallbackAddress={dst_chain_fallback_address}&owner={owner}")
        logger.info(f"Отправлен запрос на роут - {response.url}")
        logger.info(response.text)
        assert response.status_code == 200, f"Ожидался status = {200}, " \
                                            f"пришел status = {response.status_code}. " \
                                            f"Тело ответа: \n{response.text}."
        validate(json.loads(response.text), get_bridge_tx_schema)

        return response
