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
