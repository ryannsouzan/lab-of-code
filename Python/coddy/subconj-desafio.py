def check_sets (set1,set2):
    is_subset = set1 <= set2
    is_superset = set1 >= set2
    is_proper_subset = set1 < set2
    is_proper_superset = set1 > set2
    return {
        "is_subset": is_subset,
        "is_superset": is_superset,
        "is_proper_subset": is_proper_subset,
        "is_proper_superset": is_proper_superset
    }

set1 = {1, 2}
set2 = {1, 2, 3, 4}
check_sets(set1,set2)