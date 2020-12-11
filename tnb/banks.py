from typing import Union

from tnb.base_client import BaseClient


class Bank(BaseClient):
    def fetch_accounts(self, offset: int = 0, limit: int = 50) -> Union[dict, list]:
        """
        Fetch accounts from a Bank

        :param offset: The offset to start at. Default: 0
        :param limit: The limit of results to retrieve. Default: 50

        Return response as Python object
        """
        params = {"offset": offset, "limit": limit}
        return self.fetch("/accounts", params=params)

    def fetch_bank_transactions(
        self, offset: int = 0, limit: int = 50
    ) -> Union[dict, list]:
        """
        Get transactions from a Bank

        :param offset: The offset to start at. Default: 0
        :param limit: The limit of results to retrieve. Default: 50

        Return response as Python object
        """
        params = {"offset": offset, "limit": limit}
        return self.fetch("/bank_transactions", params=params)

    def fetch_invalid_blocks(
        self, offset: int = 0, limit: int = 50
    ) -> Union[dict, list]:
        """
        Get invalid block from a Bank

        :param offset: The offset to start at. Default: 0
        :param limit: The limit of results to retrieve. Default: 50

        Return response as Python object
        """
        params = {"offset": offset, "limit": limit}
        return self.fetch("/invalid_blocks", params=params)

    def fetch_confirmation_blocks(
        self, offset: int = 0, limit: int = 50
    ) -> Union[dict, list]:
        """
        Get confirmation blocks from a Bank

        :param offset: The offset to start at. Default: 0
        :param limit: The limit of results to retrieve. Default: 50

        Return response as Python object
        """
        params = {"offset": offset, "limit": limit}
        return self.fetch("/confirmation_blocks", params=params)

    def fetch_validators(self, offset: int = 0, limit: int = 50) -> Union[dict, list]:
        """
        Get validators from a Bank

        :param offset: The offset to start at. Default: 0
        :param limit: The limit of results to retrieve. Default: 50

        Return response as Python object
        """
        params = {"offset": offset, "limit": limit}
        return self.fetch("/validators", params=params)

    def fetch_validator_confirmation_services(
        self, offset: int = 0, limit: int = 50
    ) -> Union[dict, list]:
        """
        Get validators confirmation services from a Bank

        :param offset: The offset to start at. Default: 0
        :param limit: The limit of results to retrieve. Default: 50

        Return response as list
        """
        params = {"offset": offset, "limit": limit}
        return self.fetch("/validator_confirmation_services", params=params)

    def create_validator_confirmation_service(
        self, msg_end: str, msg_start: str, node_id: str, signature: str
    ) -> Union[dict, list]:
        """
        Create validators confirmation services from a Bank

        :param msg_end: ISO 8601 string that represents the end datetime
            of message
        :param msg_start: ISO 8601 string that represents the start datetime
            of message
        :param node_id: The Node Identifier of the Bank
        :param signature: The signature is signed by Bank's Node Identifier
            Signing Key

        Return response as dict
        """
        body = {
            "message": {"end": msg_end, "start": msg_start},
            "node_identifier": node_id,
            "signature": signature,
        }
        return self.post("/validator_confirmation_services", body=body)

    def fetch_banks(self, offset: int = 0, limit: int = 50) -> Union[dict, list]:
        """
        Get banks from current bank.

        :param offset: The offset to start at. Default: 0
        :param limit: The limit of results to retrieve. Default: 50

        Return response as a Python object
        """
        params = {"offset": offset, "limit": limit}
        return self.fetch("/banks", params=params)

    def fetch_config(self) -> Union[dict, list]:
        """
        Get config from a Bank
        Return response as Python object
        """
        return self.fetch("/config")

    def patch_trust_level(
        self, trust: float, node_identifier: str, signature: str
    ) -> Union[dict, list]:
        """
        Set bank trust level
        :param trust: Trust value as a float
        :param node_identifier: Node identifier of bank
        :param signature: Message signed by signing key
        Returns response as Python object
        """
        resource = f"/banks/{node_identifier}"
        body = {
            "message": {"trust": trust},
            "node_identifier": node_identifier,
            "signature": signature,
        }

        return self.patch(resource, body=body)

    def patch_account(
        self, account_number: str, node_id: str, trust: float, signature: str
    ) -> Union[dict, list]:
        """
        Send a PATCH request of an account to a Bank

        :param account_number: Specify the account will be patched
        :param node_id: The Node Identifier of the Bank
        :param trust: The value assigned to trust level of an account
        :param signature: The signature is signed by Bank's Node Identifier
            Signing Key

        Return response as Python object
        """
        resource = f"/accounts/{account_number}"
        body = {
            "message": {"trust": trust},
            "node_identifier": node_id,
            "signature": signature,
        }

        return self.patch(resource, body=body)

    def patch_validator(
        self, node_id: str, trust: float, signature: str
    ) -> Union[dict, list]:
        """
        Send a PATCH request of a validator to a Bank

        :param node_id: Node identifier of the Bank
        :param trust: The value assigned to trust level of an account
        :param signature: The signature is signed by Bank's Node Identifier
            Signing Key

        Return response as Python object
        """
        resource = f"/validators/{node_id}"

        body = {
            "message": {"trust": trust},
            "node_identifier": node_id,
            "signature": signature,
        }

        return self.patch(resource, body=body)

    def send_confirmation_block(
        self, message: dict, node_id: str, signature: str
    ) -> Union[dict, list]:
        """
        Send a confirmation block to a Bank.

        :param message: The message inside the confirmation block
        :param node_id: The Node Identifier of the Bank
        :param signature: The signature is signed by Bank's Node Identifier
            Signing Key

        Return response as Python object
        """
        body = {
            "message": message,
            "node_identifier": node_id,
            "signature": signature,
        }

        return self.post("/confirmation_blocks", body=body)

    def connection_requests(
        self, address: str, port: int, protocol: str, node_id: str, signature: str
    ) -> Union[dict, list]:
        """
        Send a connection request to the Bank

        :param address: The IP address of requesting node
        :param port: The port of requesting node
        :param protocol: The protocol of requesting node
        :param node_id: The Node Identifier of the requesting node
        :param signature: The signature is signed by requesting Node Identifier
            Signing Key

        Return response as Python object
        """
        body = {
            "message": {
                "ip_address": address,
                "port": port,
                "protocol": protocol,
            },
            "node_identifier": node_id,
            "signature": signature,
        }

        return self.post("/connection_requests", body=body)

    def post_invalid_block(
        self,
        block: dict,
        block_identifier: str,
        primary_validator_node_identifier: str,
        node_identifier: str,
        signature: str,
    ) -> Union[dict, list]:
        """
        Post an invalid block to a Bank

        :param block: The invalid block
        :param block_identifier: ID for the block
        :param primary_validator_node_identifier: Primary Validator's Node Identifier
        :param node_identifier: Node Identifier of Confirmation Validator \
        sending the request
        :param signature: Hex value of the signed message

        Return response as Python object
        """

        body = {
            "message": {
                "block": block,
                "block_identifier": block_identifier,
                "primary_validator_node_identifier": primary_validator_node_identifier,
            },
            "node_identifier": node_identifier,
            "signature": signature,
        }

        return self.post("/invalid_blocks", body=body)

    def post_upgrade_notice(
        self, bank_node_identifier: str, node_identifier: str, signature: str
    ) -> Union[dict, list]:
        """
        Post an upgrade notice to a bank and get the result status code

        :param bank_node_identifier: Node identifier of bank receiving the request
        :param node_identifier: Node identifier of Validator sending the request
        :param signature: Signature of the message

        Return response as Python object
        """
        message = {"bank_node_identifier": bank_node_identifier}
        body = {
            "message": message,
            "node_identifier": node_identifier,
            "signature": signature,
        }
        return self.post("/upgrade_notice", body=body)

    def fetch_blocks(self, offset: int = 0, limit: int = 50) -> Union[dict, list]:
        """
        Get blocks from a Bank

        :param offset: The offset to start at. Default: 0
        :param limit: The limit of results to retrieve. Default: 50

        Return response as Python object
        """
        params = {"offset": offset, "limit": limit}
        return self.fetch("/blocks", params=params)

    def post_block(
        self, account_number: str, balance_key: str, transactions: list, signature: str
    ) -> Union[dict, list]:
        """
        Send a block request to a Bank

        :param account_number: The sender's account number
        :param balance_key: The balance_key matching the sending accounts balance_lock
        :param transactions: A list of transactions
        :param signature: Hex value of the signed message

        Return response as Python object
        """

        body = {
            "account_number": account_number,
            "message": {
                "balance_key": balance_key,
                "txs": transactions,
            },
            "signature": signature,
        }

        return self.post("/blocks", body=body)
