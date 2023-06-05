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
                    "symbol": {
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
                    "symbol",
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
                "required": ["code", "name", "decimals", "address", "logoURI"]
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
                        "from": {
                            "type": "string"
                        },
                        "to": {
                            "type": "string"
                        },
                        "value": {
                            "type": "string"
                        },
                        "data": {
                            "type": "string"
                        },
                        "chainId": {
                            "type": "integer"
                        }
                    },
                    "required": ["from", "to", "value", "data", "chainId"]
                },
                "type": {
                    "type": "string"
                },
                "net": {
                    "type": "string"
                },
                "address": {
                    "type": "string"
                },
                "meta_info": {
                    "type": "array"
                }
            },
            "required": ["transaction", "type", "net", "address", "meta_info"]
        },
        "error": {
            "type": "string"
        }
    },
    "required": ["ok", "data", "error"]
}
