def brew_chai(flavor):
    if flavor not in ["masala", "ginbger", "elaichi"]:
        raise ValueError("Unsupported chai flavor...")
    print(f"Brewing {flavor} chai...")

brew_chai("masala")
brew_chai("mint")
brew_chai("ginger")