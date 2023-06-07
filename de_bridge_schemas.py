get_supported_chains_schema = {
    "type": "object",
    "properties": {
        "ok": {
            "type": "boolean"
        },
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "chainId": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "code": {
                        "type": "string"
                    },
                    "decimals": {
                        "type": "integer"
                    },
                    "net": {
                        "type": "string"
                    },
                    "logoURI": {
                        "type": "string",
                        "format": "uri"
                    }
                },
                "required": [
                    "chainId",
                    "name",
                    "code",
                    "decimals",
                    "net",
                    "logoURI"
                ]
            }
        },
        "error": {
            "type": "string"
        }
    },
    "required": [
        "ok",
        "data",
        "error"
    ]
}

get_tokens_by_chain_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "ok": {
            "type": "boolean"
        },
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "decimals": {
                        "type": "integer"
                    },
                    "address": {
                        "type": "string"
                    },
                    "logoURI": {
                        "type": "string"
                    }
                },
                "required": ["code", "name", "decimals", "address"]
            }
        },
        "error": {
            "type": "string"
        }
    },
    "required": ["ok", "data", "error"]
}

get_allowance_schema = {
    "type": "object",
    "properties": {
        "ok": {
            "type": "boolean"
        },
        "data": {
            "type": "string"
        },
        "error": {
            "type": "string"
        }
    },
    "required": ["ok", "data", "error"]
}

estimate_bridge_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "ok": {
            "type": "boolean"
        },
        "data": {
            "type": "object",
            "properties": {
                "srcTokenAmount": {
                    "type": "string"
                },
                "dstTokenAmount": {
                    "type": "string"
                },
                "estimatedGas": {
                    "type": "string"
                }
            },
            "required": ["srcTokenAmount", "dstTokenAmount", "estimatedGas"]
        },
        "error": {
            "type": "string"
        }
    },
    "required": ["ok", "data", "error"]
}

get_bridge_tx_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "ok": {
            "type": "boolean"
        },
        "data": {
            "type": "object",
            "properties": {
                "transaction": {
                    "type": "object",
                    "properties": {
                        "data": {
                            "type": "string"
                        },
                        "from": {
                            "type": "string"
                        },
                        "to": {
                            "type": "string"
                        },
                        "chainId": {
                            "type": "integer"
                        },
                        "value": {
                            "type": "string"
                        }
                    },
                    "required": ["data", "from", "to", "chainId", "value"]
                }
            },
            "required": ["transaction"]
        },
        "error": {
            "type": "string"
        }
    },
    "required": ["ok", "data", "error"]
}
