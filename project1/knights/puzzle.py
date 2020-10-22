# https://cs50.harvard.edu/ai/2020/projects/1/knights/
# A program to solve logic puzzles.
# Done by JemboDev (Alexander Saprygin) @ 22.10.20


from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Rules of the game
    # It's either a knight or a knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # Knights always tell truth
    Implication(AKnight, And(AKnight, AKnave)),
    # Knaves always lie
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Rules of the game
    # It's either a knight or a knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # Knights always tell truth
    Implication(AKnight, And(AKnave, BKnave)),
    # Knaves always lie
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Rules of the game
    # It's either a knight or a knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # Knights always tell truth
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # Knaves always lie
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # Knights always tell truth
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # Knaves always lie
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Rules of the game
    # It's either a knight or a knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    # Knights always tell truth
    Implication(AKnight, Or(AKnight, AKnave)),
    # Knaves always lie
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    # Knights always tell truth
    Implication(BKnight, Implication(AKnight, AKnave)),
    # Knaves always lie
    Implication(BKnave, Not(Implication(AKnight, AKnave))),
    # Knights always tell truth
    Implication(BKnight, CKnave),
    # Knaves always lie
    Implication(BKnave, Not(CKnave)),
    # Knights always tell truth
    Implication(CKnight, AKnight),
    # Knaves always lie
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
