import random

# Suits and Ranks
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = [
    "Ace", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "Jack", "Queen", "King"
]

# Create Full Deck
deck = [(rank, suit) for suit in suits for rank in ranks]

# Total Cards
total_cards = len(deck)

print("----- 52 Card Deck Probability Calculator -----")
print(f"\nTotal Cards in Deck: {total_cards}")

# Probability of Drawing an Ace
aces = [card for card in deck if card[0] == "Ace"]

prob_ace = len(aces) / total_cards

print("\nProbability of Drawing an Ace:")
print(f"Favorable Outcomes = {len(aces)}")
print(f"Sample Space = {total_cards}")

print(f"P(Ace) = {len(aces)}/{total_cards} = {prob_ace:.4f}")

# Probability of Drawing a Heart
hearts = [card for card in deck if card[1] == "Hearts"]

prob_heart = len(hearts) / total_cards

print("\nProbability of Drawing a Heart:")
print(f"Favorable Outcomes = {len(hearts)}")
print(f"Sample Space = {total_cards}")

print(f"P(Heart) = {len(hearts)}/{total_cards} = {prob_heart:.4f}")

# Random Card Draw
drawn_card = random.choice(deck)

print("\nRandomly Drawn Card:")
print(drawn_card)

# Remove Drawn Card
deck.remove(drawn_card)

# Remaining Cards
remaining_cards = len(deck)

# Updated Ace Probability
remaining_aces = [card for card in deck if card[0] == "Ace"]

updated_prob_ace = len(remaining_aces) / remaining_cards

print("\nProbability of Drawing an Ace After One Card Removed:")

print(f"Remaining Aces = {len(remaining_aces)}")
print(f"Remaining Cards = {remaining_cards}")

print(
    f"P(Ace) = {len(remaining_aces)}/{remaining_cards} = {updated_prob_ace:.4f}"
)

print("\n----- Probability Analysis Completed -----")
