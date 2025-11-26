from itertools import combinations, permutations

NUM_CHILDREN = 7
NUM_COINS = 49
MAX_COINS_PER_CHILD = 7

# Generate the list of coin weights: 1 to 49 grams
coins = list(range(1, NUM_COINS+1))

print(coins)

# The total weight
total_weight = sum(coins)

print(total_weight)

# Each child should get the same total weight
if total_weight % NUM_CHILDREN != 0:
    print("Impossible: total weight cannot be equally divided among children.")
    exit(1)

target_weight = total_weight // NUM_CHILDREN

# Brute-force is too slow, so let's use recursive backtracking with constraints
def distribute(children, available_coins, so_far):
    """
    Recursive function to find a valid distribution.
    children: which child we are allocating to
    available_coins: set of coins left
    so_far: list of allocations [{child: [coins]}]
    Returns: valid allocation or None
    """
    if children == NUM_CHILDREN:
        # All coins should be distributed and all constraints matched
        if not available_coins:
            return so_far
        else:
            return None

    # Try all combinations that are possible for this child
    # The child gets MAX_COINS_PER_CHILD coins whose sum is target_weight
    for kid_coins in combinations(available_coins, MAX_COINS_PER_CHILD):
        if sum(kid_coins) == target_weight:
            # Try this assignment
            next_available = set(available_coins) - set(kid_coins)
            result = distribute(children+1, next_available, so_far + [list(kid_coins)])
            if result is not None:
                return result
    return None

def main():
    result = distribute(0, set(coins), [])
    if result:
        for idx, child_coins in enumerate(result):
            print(f"Child {idx+1}: coins = {sorted(child_coins)} (total weight: {sum(child_coins)})")
    else:
        print("No valid distribution found.")

if __name__ == "__main__":
    main()
