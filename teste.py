from tcgdexsdk import Query, TCGdex

# Init the SDK
tcgdex = TCGdex()
# Or use the sync version
card = tcgdex.card.listSync(Query().contains("name", 'clefairy'))

print(f"Found: {card}")