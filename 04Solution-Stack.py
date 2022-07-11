'''
Stack Problem to Solve Code Solution

Prompt:

Is the Giant Soldier of Stone successfully summoned? Or will Trap Hole gobble him up after all?

Do the following:

    * Pop items off of the stack to activate them. When activating a card, print its card_title and card_activation

    * If a card destroys another card, pop the destroyed card off of the stack and print only its card_title and that it was destroyed.

    * After all cards have been activated or destroyed, check to see if the stack is empty. If so, print "Chain Complete!"

Code you would have copied from the Example Problem:
'''

class Card:
    card_title = None
    card_activation = None
    destroy_previous = False

giant_soldier_of_stone = Card()

giant_soldier_of_stone.card_title = "Giant Soldier of Stone"
giant_soldier_of_stone.card_activation = "This monster card is successfully summoned to the field"

trap_hole = Card()

trap_hole.card_title = "Trap Hole"
trap_hole.card_activation = "When your opponent Normal or Flip Summons a monster with 1000 or more ATK: Target that monster; destroy that target."
trap_hole.destroy_previous = True

mystical_space_typhoon1 = Card()

mystical_space_typhoon1.card_title = "Mystical Space Typhoon"
mystical_space_typhoon1.card_activation = "Target 1 Spell/Trap Card on the field; destroy that target."
mystical_space_typhoon1.destroy_previous = True

mystical_space_typhoon2 = Card()

mystical_space_typhoon2.card_title = "Mystical Space Typhoon"
mystical_space_typhoon2.card_activation = "Target 1 Spell/Trap Card on the field; destroy that target."
mystical_space_typhoon2.destroy_previous = True

curse_of_royal = Card()

curse_of_royal.card_title = "Curse of Royal"
curse_of_royal.card_activation = "Negate the activation of a Spell or Trap Card that includes the effect of destroying 1 Spell or Trap Card and destroy it."
curse_of_royal.destroy_previous = True

chain = []
chain.append(giant_soldier_of_stone)
chain.append(trap_hole)
chain.append(mystical_space_typhoon1)
chain.append(mystical_space_typhoon2)
chain.append(curse_of_royal)

print(f"\nTotal links in Chain: {len(chain)}\n")

'''
_________________________________________________________________________________________________________________________
Now onto Problem to Solve:
'''

while len(chain) > 0:
    #Activate the Card 
    current_card = chain.pop()
    print(f"Activating {current_card.card_title}:")
    print(current_card.card_activation)

    #If the activated card destroys the card proceeding it in the stack:
    if current_card.destroy_previous == True:
        destroyed_card = chain.pop()
        print(f"\nCard destroyed by {current_card.card_title}: {destroyed_card.card_title}.\n")

#After all cards have been activated or destroyed, check to see if the stack is empty. If so, print "Chain Complete!" 
if len(chain) == 0:
    print("\nChain Complete!\n")
