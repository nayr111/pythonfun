# knights and knaves. credit to Gemini AI for helping me solve this.
# (though, with the solution, i came up with this logic and code on my own.)
# outline/rough draft of solution
def knightorknave(Knight, Knave):
    if "A" == Knight:
        return True
    elif "A" == Knave:
        return False

#logical steps:
# A and B. 
# A steps up. 
# A says, "At least one of us is a knave."
# If A is a knight, then A's statement is true,
# which means that at least one of them is a knave.
# If A is a knave, then A's statement is false, because 
# knaves always lie. Therefore, that means A is NOT a knave,
# which means they are both knights, but that contradicts A's
# statement, so A cannot be a knave. 
# Therefore, A must be a knight.

#final draft/updated solution
Knights = "Truth"
Knaves = "Lies"
if "A" == Knights: # branch 1
    print(True) # because knights always tell the truth
    print("B is a knave.")
if "A" == Knaves: # branch 2
    print(False) # because knaves always lie
    print("A is a knight.") # which means they are both knights
    print("B is a knight.")
    # but then if A is a knight, then A cannot be a knave,
    # which contradicts A's statement, Knight != Knave
    # -> logical conflict/compiler error
# therefore, A must be a knight, and B must be a knave. 
# Branch 1 is the only valid branch.
