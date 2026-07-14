from config import WALLETS
from scanner import scan_wallet

print("🐋 Whale Hunter iniciado")

for wallet in WALLETS:
    scan_wallet(wallet)
