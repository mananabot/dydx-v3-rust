# ------------ Ethereum Network IDs ------------
NETWORK_ID_MAINNET = 1
NETWORK_ID_ROPSTEN = 3

# ------------ Signature Types ------------
SIGNATURE_TYPE_NO_PREPEND = 0
SIGNATURE_TYPE_DECIMAL = 1
SIGNATURE_TYPE_HEXADECIMAL = 2

# ------------ Asset IDs ------------
COLLATERAL_ASSET_ID_BY_NETWORK_ID = {
    NETWORK_ID_MAINNET: int(
        '0x02893294412a4c8f915f75892b395ebbf6859ec246ec365c3b1f56f47c3a0a5d',
        16,
    ),
    NETWORK_ID_GOERLI: int(
        '0x03bda2b4764039f2df44a00a9cf1d1569a83f95406a983ce4beb95791c376008',
        16,
    ),
}

# ------------ Other ------------
COLLATERAL_ASSET = "USDC"
